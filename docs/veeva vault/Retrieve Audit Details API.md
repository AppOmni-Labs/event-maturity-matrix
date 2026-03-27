# Veeva Vault - Retrieve Audit Details API (0.0.1)

> Entity Name: event_source

The Veeva Vault Retrieve Audit Details API provides near real-time, read-only access to an organization's audit log.

## References
* [Retrieve Audit Details API Documentation](https://developer.veevavault.com/api/24.1/#retrieve-audit-details)

## Retention

Based on our research, Veeva Vault retains audit logs for 30 days.


### Comments
N/A


## Latency

Based on our research, Veeva Vault has a latency of Near real-time.

### Comments
N/A


## Licensing

A Veeva Vault license is required to access the Retrieve Audit Details API.

## Mappings

| Category | Event Type | Attributes | Examples |
| -------- | ---------- | ---------- | -------- |
| C0001 | ET0001 |A0001 -> timestamp<br />A0002 -> id<br />A0003 -> type<br />A0005 -> user_name<br />A0009 -> source_ip<br />A0011 -> platform<br />A0013 -> status<br />|[success](/products/veeva vault/event_examples/authentication_account_login_session_success.json)<br />[failure](/products/veeva vault/event_examples/authentication_account_login_session_failure.json)<br />|
| C0001 | ET0002 |A0001 -> timestamp<br />A0002 -> id<br />A0003 -> type<br />A0005 -> user_name<br />A0009 -> source_ip<br />A0011 -> platform<br />|[success](/products/veeva vault/event_examples/authentication_account_logout.json)<br />|
| C0002 | ET0004 |A0001 -> timestamp<br />A0002 -> id<br />A0003 -> action<br />A0005 -> user_name<br />A0019 -> item<br />|[success](/products/veeva vault/event_examples/authorization_create_user.json)<br />|
| C0002 | ET0006 |A0001 -> timestamp<br />A0002 -> id<br />A0003 -> action<br />A0005 -> user_name<br />A0019 -> item<br />A0020 -> field_name<br />|[success](/products/veeva vault/event_examples/authorization_update_user.json)<br />|
| C0002 | ET0008 |A0001 -> timestamp<br />A0002 -> id<br />A0003 -> action<br />A0005 -> user_name<br />A0021 -> item<br />|[success](/products/veeva vault/event_examples/authorization_create_group.json)<br />|
| C0002 | ET0010 |A0001 -> timestamp<br />A0002 -> id<br />A0003 -> action<br />A0005 -> user_name<br />A0021 -> item<br />A0020 -> field_name<br />|[success](/products/veeva vault/event_examples/authorization_update_group.json)<br />|
| C0002 | ET0011 |A0001 -> timestamp<br />A0002 -> id<br />A0003 -> action<br />A0005 -> user_name<br />A0021 -> item<br />|[success](/products/veeva vault/event_examples/authorization_delete_group.json)<br />|
| C0002 | ET0012 |A0001 -> timestamp<br />A0002 -> id<br />A0003 -> action<br />A0005 -> user_name<br />A0021 -> item<br />A0019 -> new_value<br />|[success](/products/veeva vault/event_examples/authorization_add_to_group.json)<br />|
| C0002 | ET0013 |A0001 -> timestamp<br />A0002 -> id<br />A0003 -> action<br />A0005 -> user_name<br />A0021 -> item<br />A0019 -> old_value<br />|[success](/products/veeva vault/event_examples/authorization_remove_from_group.json)<br />|
| C0002 | ET0014 |A0001 -> timestamp<br />A0002 -> id<br />A0003 -> action<br />A0005 -> user_name<br />A0022 -> item<br />|[success](/products/veeva vault/event_examples/authorization_create_role.json)<br />|
| C0002 | ET0016 |A0001 -> timestamp<br />A0002 -> id<br />A0003 -> action<br />A0005 -> user_name<br />A0022 -> item<br />A0020 -> field_name<br />|[success](/products/veeva vault/event_examples/authorization_update_role.json)<br />|
| C0002 | ET0017 |A0001 -> timestamp<br />A0002 -> id<br />A0003 -> action<br />A0005 -> user_name<br />A0022 -> item<br />|[success](/products/veeva vault/event_examples/authorization_delete_role.json)<br />|
| C0002 | ET0018 |A0001 -> timestamp<br />A0002 -> id<br />A0003 -> action<br />A0005 -> user_name<br />A0023 -> new_value<br />A0024 -> item<br />|[success](/products/veeva vault/event_examples/authorization_add_permission.json)<br />|
| C0002 | ET0019 |A0001 -> timestamp<br />A0002 -> id<br />A0003 -> action<br />A0005 -> user_name<br />A0023 -> field_name<br />A0024 -> item<br />|[success](/products/veeva vault/event_examples/authorization_remove_permission.json)<br />|
| C0003 | ET0026 |A0001 -> timestamp<br />A0002 -> id<br />A0003 -> action<br />A0005 -> user_name<br />A0029 -> item<br />|[success](/products/veeva vault/event_examples/system_audit_create_integration.json)<br />|
| C0003 | ET0028 |A0001 -> timestamp<br />A0002 -> id<br />A0003 -> action<br />A0005 -> user_name<br />A0029 -> item<br />A0026 -> new_value<br />|[success](/products/veeva vault/event_examples/system_audit_update_integration.json)<br />|
| C0003 | ET0029 |A0001 -> timestamp<br />A0002 -> id<br />A0003 -> action<br />A0005 -> user_name<br />A0029 -> item<br />|[success](/products/veeva vault/event_examples/system_audit_delete_integration.json)<br />|
| C0004 | ET0030 |A0001 -> timestamp<br />A0002 -> id<br />A0003 -> action<br />A0005 -> user_name<br />A0030 -> item<br />A0031 -> object_label<br />|[success](/products/veeva vault/event_examples/activity_audit_create_resource.json)<br />|
| C0004 | ET0031 |A0001 -> timestamp<br />A0002 -> id<br />A0003 -> action<br />A0005 -> user_name<br />A0030 -> item<br />|[success](/products/veeva vault/event_examples/activity_audit_read_resource.json)<br />|
| C0004 | ET0032 |A0001 -> timestamp<br />A0002 -> id<br />A0003 -> action<br />A0005 -> user_name<br />A0030 -> item<br />A0031 -> object_label<br />|[success](/products/veeva vault/event_examples/activity_audit_update_resource.json)<br />|
| C0004 | ET0033 |A0001 -> timestamp<br />A0002 -> id<br />A0003 -> action<br />A0005 -> user_name<br />A0030 -> item<br />A0031 -> object_label<br />|[success](/products/veeva vault/event_examples/activity_audit_delete_resource.json)<br />|
| C0004 | ET0034 |A0001 -> timestamp<br />A0002 -> id<br />A0003 -> action<br />A0005 -> user_name<br />A0032 -> item<br />|[success](/products/veeva vault/event_examples/activity_audit_download_resource.json)<br />|


