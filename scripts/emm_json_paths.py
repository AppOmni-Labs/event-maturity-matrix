"""Extract values from example JSON using EMM field path rules (JMESPath + recursive bare keys)."""
from typing import Any

import jmespath


def _path_segments(path_str: str) -> list[str]:
    segments = []
    current = []
    depth = 0
    i = 0
    while i < len(path_str):
        c = path_str[i]
        if depth > 0:
            current.append(c)
            if c == "[":
                depth += 1
            elif c == "]":
                depth -= 1
            i += 1
            continue
        if c == "[":
            depth += 1
            current.append(c)
            i += 1
        elif c == "\\" and i + 1 < len(path_str):
            nxt = path_str[i + 1]
            if nxt == ".":
                current.append(".")
                i += 2
            elif nxt == "\\":
                current.append("\\")
                i += 2
            else:
                current.append(c)
                i += 1
        elif c == ".":
            segments.append("".join(current))
            current = []
            i += 1
        else:
            current.append(c)
            i += 1
    if current:
        segments.append("".join(current))
    return segments


def _path_to_jmespath(path_str: str) -> str:
    segments = _path_segments(path_str)
    jmespath_parts = []
    for seg in segments:
        if "[" in seg and seg.endswith("]") and "=" in seg:
            key = seg[: seg.index("[")]
            filter_part = seg[seg.index("[") + 1 : -1]
            filter_key, _, filter_value = filter_part.partition("=")
            escaped = filter_value.replace("\\", "\\\\").replace("'", "\\'")
            jmespath_parts.append(f"{key}[?{filter_key}=='{escaped}']")
        elif "." in seg:
            escaped = seg.replace("\\", "\\\\").replace("'", "\\'")
            jmespath_parts.append(f"['{escaped}']")
        else:
            jmespath_parts.append(seg)
    return ".".join(jmespath_parts)


def _values_for_key_recursive(obj: Any, key: str):
    if isinstance(obj, dict):
        if key in obj:
            yield obj[key]
        for v in obj.values():
            yield from _values_for_key_recursive(v, key)
    elif isinstance(obj, list):
        for item in obj:
            yield from _values_for_key_recursive(item, key)


def item_generator(json_input: Any, lookup_key: str):
    """Yield values for lookup_key in json_input."""
    if "." not in lookup_key and "[" not in lookup_key:
        yield from _values_for_key_recursive(json_input, lookup_key)
        return
    expr = _path_to_jmespath(lookup_key)
    try:
        result = jmespath.search(expr, json_input)
    except jmespath.exceptions.JMESPathError:
        return
    if result is None:
        if "[" not in lookup_key:
            segs = _path_segments(lookup_key)
            if len(segs) >= 2:
                parent_expr = _path_to_jmespath(".".join(segs[:-1]))
                try:
                    parent_result = jmespath.search(parent_expr, json_input)
                    if isinstance(parent_result, dict) and segs[-1] in parent_result:
                        yield parent_result[segs[-1]]
                        return
                except jmespath.exceptions.JMESPathError:
                    pass
                for i in range(len(segs) - 1):
                    projection_expr = _path_to_jmespath(
                        ".".join(segs[: i + 1]) + "[*]." + ".".join(segs[i + 1 :])
                    )
                    try:
                        proj_result = jmespath.search(projection_expr, json_input)
                        if isinstance(proj_result, list):
                            for item in proj_result:
                                yield item
                            return
                    except jmespath.exceptions.JMESPathError:
                        continue
        return
    if isinstance(result, list):
        for item in result:
            yield item
    else:
        yield result
