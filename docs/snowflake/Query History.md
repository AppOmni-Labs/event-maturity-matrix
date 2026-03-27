# Snowflake - Query History (1.0.0)

> Entity Name: event_source

This Account Usage view can be used to query Snowflake query history by various dimensions (time range, session, user, warehouse, etc.) within the last 365 days (1 year).

## References
* [About the Query History View](https://docs.snowflake.com/en/sql-reference/account-usage/query_history)

## Retention

Based on our research, Snowflake retains audit logs for 365 days.


### Comments
No comments


## Latency

Based on our research, Snowflake has a latency of up to 45 minutes.

### Comments
No comments


## Licensing

Contact sales

## Mappings

| Category | Event Type | Attributes | Examples |
| -------- | ---------- | ---------- | -------- |
| C0002 | ET0004 |A0001 -> START_TIME<br />A0002 -> QUERY_ID<br />A0003 -> QUERY_TYPE<br />A0004 -> ERROR_CODE<br />A0005 -> USER_NAME<br />A0007 -> ROLE_NAME<br />A0008 -> SESSION_ID<br />A0019 -> QUERY_TEXT<br />|[success](/products/snowflake/event_examples/query_history/authorization_create_user.json)<br />|
| C0002 | ET0005 |A0001 -> START_TIME<br />A0002 -> QUERY_ID<br />A0003 -> QUERY_TYPE<br />A0004 -> ERROR_CODE<br />A0005 -> USER_NAME<br />A0007 -> ROLE_NAME<br />A0008 -> SESSION_ID<br />A0019 -> QUERY_TEXT<br />|[success](/products/snowflake/event_examples/query_history/authorization_read_user.json)<br />|
| C0002 | ET0006 |A0001 -> START_TIME<br />A0002 -> QUERY_ID<br />A0003 -> QUERY_TYPE<br />A0004 -> ERROR_CODE<br />A0005 -> USER_NAME<br />A0007 -> ROLE_NAME<br />A0008 -> SESSION_ID<br />A0019 -> QUERY_TEXT<br />A0020 -> QUERY_TEXT<br />|[success](/products/snowflake/event_examples/query_history/authorization_update_user.json)<br />|
| C0002 | ET0007 |A0001 -> START_TIME<br />A0002 -> QUERY_ID<br />A0003 -> QUERY_TYPE<br />A0004 -> ERROR_CODE<br />A0005 -> USER_NAME<br />A0007 -> ROLE_NAME<br />A0008 -> SESSION_ID<br />|[success](/products/snowflake/event_examples/query_history/authorization_delete_user.json)<br />|
| C0002 | ET0014 |A0001 -> START_TIME<br />A0002 -> QUERY_ID<br />A0003 -> QUERY_TYPE<br />A0004 -> ERROR_CODE<br />A0005 -> USER_NAME<br />A0007 -> ROLE_NAME<br />A0008 -> SESSION_ID<br />A0022 -> QUERY_TEXT<br />|[success](/products/snowflake/event_examples/query_history/authorization_create_role.json)<br />|
| C0002 | ET0015 |A0001 -> START_TIME<br />A0002 -> QUERY_ID<br />A0003 -> QUERY_TYPE<br />A0004 -> ERROR_CODE<br />A0005 -> USER_NAME<br />A0007 -> ROLE_NAME<br />A0008 -> SESSION_ID<br />A0022 -> QUERY_TEXT<br />|[success](/products/snowflake/event_examples/query_history/authorization_read_role.json)<br />|
| C0002 | ET0016 |A0001 -> START_TIME<br />A0002 -> QUERY_ID<br />A0003 -> QUERY_TYPE<br />A0004 -> ERROR_CODE<br />A0005 -> USER_NAME<br />A0007 -> ROLE_NAME<br />A0008 -> SESSION_ID<br />A0020 -> QUERY_TEXT<br />A0022 -> QUERY_TEXT<br />|[success](/products/snowflake/event_examples/query_history/authorization_update_role.json)<br />|
| C0002 | ET0017 |A0001 -> START_TIME<br />A0002 -> QUERY_ID<br />A0003 -> QUERY_TYPE<br />A0004 -> ERROR_CODE<br />A0005 -> USER_NAME<br />A0007 -> ROLE_NAME<br />A0008 -> SESSION_ID<br />A0022 -> QUERY_TEXT<br />|[success](/products/snowflake/event_examples/query_history/authorization_delete_role.json)<br />|
| C0002 | ET0018 |A0001 -> START_TIME<br />A0002 -> QUERY_ID<br />A0003 -> QUERY_TYPE<br />A0004 -> ERROR_CODE<br />A0005 -> USER_NAME<br />A0007 -> ROLE_NAME<br />A0008 -> SESSION_ID<br />A0023 -> QUERY_TEXT<br />A0024 -> QUERY_TEXT<br />|[success](/products/snowflake/event_examples/query_history/authorization_add_permission.json)<br />|
| C0002 | ET0019 |A0001 -> START_TIME<br />A0002 -> QUERY_ID<br />A0003 -> QUERY_TYPE<br />A0004 -> ERROR_CODE<br />A0005 -> USER_NAME<br />A0007 -> ROLE_NAME<br />A0008 -> SESSION_ID<br />A0023 -> QUERY_TEXT<br />A0024 -> QUERY_TEXT<br />|[success](/products/snowflake/event_examples/query_history/authorization_remove_permission.json)<br />|
| C0002 | ET0021 |A0001 -> START_TIME<br />A0002 -> QUERY_ID<br />A0003 -> QUERY_TYPE<br />A0004 -> ERROR_CODE<br />A0005 -> USER_NAME<br />A0007 -> ROLE_NAME<br />A0008 -> SESSION_ID<br />A0019 -> QUERY_TEXT<br />A0025 -> QUERY_TEXT<br />|[success](/products/snowflake/event_examples/query_history/authorization_remove_enrollment.json)<br />|
| C0003 | ET0022 |A0001 -> START_TIME<br />A0002 -> QUERY_ID<br />A0003 -> QUERY_TYPE<br />A0004 -> ERROR_CODE<br />A0005 -> USER_NAME<br />A0007 -> ROLE_NAME<br />A0008 -> SESSION_ID<br />A0026 -> QUERY_TEXT<br />A0027 -> QUERY_TEXT<br />|[success](/products/snowflake/event_examples/query_history/system_audit_create_security_configuration.json)<br />|
| C0003 | ET0023 |A0001 -> START_TIME<br />A0002 -> QUERY_ID<br />A0003 -> QUERY_TYPE<br />A0004 -> ERROR_CODE<br />A0005 -> USER_NAME<br />A0007 -> ROLE_NAME<br />A0008 -> SESSION_ID<br />A0027 -> QUERY_TEXT<br />|[success](/products/snowflake/event_examples/query_history/system_audit_read_security_configuration.json)<br />|
| C0003 | ET0024 |A0001 -> START_TIME<br />A0002 -> QUERY_ID<br />A0003 -> QUERY_TYPE<br />A0004 -> ERROR_CODE<br />A0005 -> USER_NAME<br />A0007 -> ROLE_NAME<br />A0008 -> SESSION_ID<br />A0026 -> QUERY_TEXT<br />A0027 -> QUERY_TEXT<br />|[success](/products/snowflake/event_examples/query_history/system_audit_update_security_configuration.json)<br />|
| C0003 | ET0025 |A0001 -> START_TIME<br />A0002 -> QUERY_ID<br />A0003 -> QUERY_TYPE<br />A0004 -> ERROR_CODE<br />A0005 -> USER_NAME<br />A0007 -> ROLE_NAME<br />A0008 -> SESSION_ID<br />A0026 -> QUERY_TEXT<br />A0027 -> QUERY_TEXT<br />|[success](/products/snowflake/event_examples/query_history/system_audit_delete_security_configuration.json)<br />|
| C0003 | ET0026 |A0001 -> START_TIME<br />A0002 -> QUERY_ID<br />A0003 -> QUERY_TYPE<br />A0004 -> ERROR_CODE<br />A0005 -> USER_NAME<br />A0007 -> ROLE_NAME<br />A0008 -> SESSION_ID<br />A0029 -> QUERY_TEXT<br />|[success](/products/snowflake/event_examples/query_history/system_audit_create_integration.json)<br />|
| C0003 | ET0027 |A0001 -> START_TIME<br />A0002 -> QUERY_ID<br />A0003 -> QUERY_TYPE<br />A0004 -> ERROR_CODE<br />A0005 -> USER_NAME<br />A0007 -> ROLE_NAME<br />A0008 -> SESSION_ID<br />A0029 -> QUERY_TEXT<br />|[success](/products/snowflake/event_examples/query_history/system_audit_read_integration.json)<br />|
| C0003 | ET0028 |A0001 -> START_TIME<br />A0002 -> QUERY_ID<br />A0003 -> QUERY_TYPE<br />A0004 -> ERROR_CODE<br />A0005 -> USER_NAME<br />A0007 -> ROLE_NAME<br />A0008 -> SESSION_ID<br />A0026 -> QUERY_TEXT<br />A0029 -> QUERY_TEXT<br />|[success](/products/snowflake/event_examples/query_history/system_audit_update_integration.json)<br />|
| C0003 | ET0029 |A0001 -> START_TIME<br />A0002 -> QUERY_ID<br />A0003 -> QUERY_TYPE<br />A0004 -> ERROR_CODE<br />A0005 -> USER_NAME<br />A0007 -> ROLE_NAME<br />A0008 -> SESSION_ID<br />A0029 -> QUERY_TEXT<br />|[success](/products/snowflake/event_examples/query_history/system_audit_delete_integration.json)<br />|
| C0004 | ET0030 |A0001 -> START_TIME<br />A0002 -> QUERY_ID<br />A0003 -> QUERY_TYPE<br />A0004 -> ERROR_CODE<br />A0005 -> USER_NAME<br />A0007 -> ROLE_NAME<br />A0008 -> SESSION_ID<br />A0030 -> QUERY_TEXT<br />A0031 -> QUERY_TEXT<br />|[success](/products/snowflake/event_examples/query_history/activity_audit_create_resource.json)<br />|
| C0004 | ET0031 |A0001 -> START_TIME<br />A0002 -> QUERY_ID<br />A0003 -> QUERY_TYPE<br />A0004 -> ERROR_CODE<br />A0005 -> USER_NAME<br />A0007 -> ROLE_NAME<br />A0008 -> SESSION_ID<br />A0030 -> QUERY_TEXT<br />A0031 -> QUERY_TEXT<br />|[success](/products/snowflake/event_examples/query_history/activity_audit_read_resource.json)<br />|
| C0004 | ET0032 |A0001 -> START_TIME<br />A0002 -> QUERY_ID<br />A0003 -> QUERY_TYPE<br />A0004 -> ERROR_CODE<br />A0005 -> USER_NAME<br />A0007 -> ROLE_NAME<br />A0008 -> SESSION_ID<br />A0030 -> QUERY_TEXT<br />A0031 -> QUERY_TEXT<br />|[success](/products/snowflake/event_examples/query_history/activity_audit_update_resource.json)<br />|
| C0004 | ET0033 |A0001 -> START_TIME<br />A0002 -> QUERY_ID<br />A0003 -> QUERY_TYPE<br />A0004 -> ERROR_CODE<br />A0005 -> USER_NAME<br />A0007 -> ROLE_NAME<br />A0008 -> SESSION_ID<br />A0030 -> QUERY_TEXT<br />A0031 -> QUERY_TEXT<br />|[success](/products/snowflake/event_examples/query_history/activity_audit_delete_resource.json)<br />|
| C0004 | ET0034 |A0001 -> START_TIME<br />A0002 -> QUERY_ID<br />A0003 -> QUERY_TYPE<br />A0004 -> ERROR_CODE<br />A0005 -> USER_NAME<br />A0007 -> ROLE_NAME<br />A0008 -> SESSION_ID<br />A0030 -> QUERY_TEXT<br />A0031 -> QUERY_TEXT<br />A0032 -> QUERY_TEXT<br />|[success](/products/snowflake/event_examples/query_history/activity_audit_download_resource.json)<br />|


