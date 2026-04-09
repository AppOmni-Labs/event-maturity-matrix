# Snowflake — Query History

📌 **v1.0.0** · 🗄 **Retention:** 365 days · ⚡ **Latency:** Up to 45 minutes

📜 **Licensing:** Contact sales

This Account Usage view can be used to query Snowflake query history by various dimensions (time range, session, user, warehouse, etc.) within the last 365 days (1 year).
## References
* [About the Query History View](https://docs.snowflake.com/en/sql-reference/account-usage/query_history)
## Field mappings

| Category | Event type | Attribute | Source field(s) |
| -------- | ---------- | --------- | ---------------- |
| Authorization | Create User | Timestamp | START_TIME |
| Authorization | Create User | Event ID | QUERY_ID |
| Authorization | Create User | Event Code / Type | QUERY_TYPE |
| Authorization | Create User | Result | ERROR_CODE |
| Authorization | Create User | Username | USER_NAME |
| Authorization | Create User | User Type / Role | ROLE_NAME |
| Authorization | Create User | Session ID | SESSION_ID |
| Authorization | Create User | Target Username | QUERY_TEXT |
| Authorization | Read User | Timestamp | START_TIME |
| Authorization | Read User | Event ID | QUERY_ID |
| Authorization | Read User | Event Code / Type | QUERY_TYPE |
| Authorization | Read User | Result | ERROR_CODE |
| Authorization | Read User | Username | USER_NAME |
| Authorization | Read User | User Type / Role | ROLE_NAME |
| Authorization | Read User | Session ID | SESSION_ID |
| Authorization | Read User | Target Username | QUERY_TEXT |
| Authorization | Update User | Timestamp | START_TIME |
| Authorization | Update User | Event ID | QUERY_ID |
| Authorization | Update User | Event Code / Type | QUERY_TYPE |
| Authorization | Update User | Result | ERROR_CODE |
| Authorization | Update User | Username | USER_NAME |
| Authorization | Update User | User Type / Role | ROLE_NAME |
| Authorization | Update User | Session ID | SESSION_ID |
| Authorization | Update User | Target Username | QUERY_TEXT |
| Authorization | Update User | Target Attribute Context | QUERY_TEXT |
| Authorization | Delete User | Timestamp | START_TIME |
| Authorization | Delete User | Event ID | QUERY_ID |
| Authorization | Delete User | Event Code / Type | QUERY_TYPE |
| Authorization | Delete User | Result | ERROR_CODE |
| Authorization | Delete User | Username | USER_NAME |
| Authorization | Delete User | User Type / Role | ROLE_NAME |
| Authorization | Delete User | Session ID | SESSION_ID |
| Authorization | Create Role | Timestamp | START_TIME |
| Authorization | Create Role | Event ID | QUERY_ID |
| Authorization | Create Role | Event Code / Type | QUERY_TYPE |
| Authorization | Create Role | Result | ERROR_CODE |
| Authorization | Create Role | Username | USER_NAME |
| Authorization | Create Role | User Type / Role | ROLE_NAME |
| Authorization | Create Role | Session ID | SESSION_ID |
| Authorization | Create Role | Target Role Name | QUERY_TEXT |
| Authorization | Read Role | Timestamp | START_TIME |
| Authorization | Read Role | Event ID | QUERY_ID |
| Authorization | Read Role | Event Code / Type | QUERY_TYPE |
| Authorization | Read Role | Result | ERROR_CODE |
| Authorization | Read Role | Username | USER_NAME |
| Authorization | Read Role | User Type / Role | ROLE_NAME |
| Authorization | Read Role | Session ID | SESSION_ID |
| Authorization | Read Role | Target Role Name | QUERY_TEXT |
| Authorization | Update Role | Timestamp | START_TIME |
| Authorization | Update Role | Event ID | QUERY_ID |
| Authorization | Update Role | Event Code / Type | QUERY_TYPE |
| Authorization | Update Role | Result | ERROR_CODE |
| Authorization | Update Role | Username | USER_NAME |
| Authorization | Update Role | User Type / Role | ROLE_NAME |
| Authorization | Update Role | Session ID | SESSION_ID |
| Authorization | Update Role | Target Attribute Context | QUERY_TEXT |
| Authorization | Update Role | Target Role Name | QUERY_TEXT |
| Authorization | Delete Role | Timestamp | START_TIME |
| Authorization | Delete Role | Event ID | QUERY_ID |
| Authorization | Delete Role | Event Code / Type | QUERY_TYPE |
| Authorization | Delete Role | Result | ERROR_CODE |
| Authorization | Delete Role | Username | USER_NAME |
| Authorization | Delete Role | User Type / Role | ROLE_NAME |
| Authorization | Delete Role | Session ID | SESSION_ID |
| Authorization | Delete Role | Target Role Name | QUERY_TEXT |
| Authorization | Add Permission | Timestamp | START_TIME |
| Authorization | Add Permission | Event ID | QUERY_ID |
| Authorization | Add Permission | Event Code / Type | QUERY_TYPE |
| Authorization | Add Permission | Result | ERROR_CODE |
| Authorization | Add Permission | Username | USER_NAME |
| Authorization | Add Permission | User Type / Role | ROLE_NAME |
| Authorization | Add Permission | Session ID | SESSION_ID |
| Authorization | Add Permission | Permission Name | QUERY_TEXT |
| Authorization | Add Permission | Target Resource Name | QUERY_TEXT |
| Authorization | Remove Permission | Timestamp | START_TIME |
| Authorization | Remove Permission | Event ID | QUERY_ID |
| Authorization | Remove Permission | Event Code / Type | QUERY_TYPE |
| Authorization | Remove Permission | Result | ERROR_CODE |
| Authorization | Remove Permission | Username | USER_NAME |
| Authorization | Remove Permission | User Type / Role | ROLE_NAME |
| Authorization | Remove Permission | Session ID | SESSION_ID |
| Authorization | Remove Permission | Permission Name | QUERY_TEXT |
| Authorization | Remove Permission | Target Resource Name | QUERY_TEXT |
| Authorization | Remove Enrollment | Timestamp | START_TIME |
| Authorization | Remove Enrollment | Event ID | QUERY_ID |
| Authorization | Remove Enrollment | Event Code / Type | QUERY_TYPE |
| Authorization | Remove Enrollment | Result | ERROR_CODE |
| Authorization | Remove Enrollment | Username | USER_NAME |
| Authorization | Remove Enrollment | User Type / Role | ROLE_NAME |
| Authorization | Remove Enrollment | Session ID | SESSION_ID |
| Authorization | Remove Enrollment | Target Username | QUERY_TEXT |
| Authorization | Remove Enrollment | Enrollment Type | QUERY_TEXT |
| System Audit | Create Security Configuration | Timestamp | START_TIME |
| System Audit | Create Security Configuration | Event ID | QUERY_ID |
| System Audit | Create Security Configuration | Event Code / Type | QUERY_TYPE |
| System Audit | Create Security Configuration | Result | ERROR_CODE |
| System Audit | Create Security Configuration | Username | USER_NAME |
| System Audit | Create Security Configuration | User Type / Role | ROLE_NAME |
| System Audit | Create Security Configuration | Session ID | SESSION_ID |
| System Audit | Create Security Configuration | Configuration / Setting Name | QUERY_TEXT |
| System Audit | Create Security Configuration | Configuration / Setting Value | QUERY_TEXT |
| System Audit | Read Security Configuration | Timestamp | START_TIME |
| System Audit | Read Security Configuration | Event ID | QUERY_ID |
| System Audit | Read Security Configuration | Event Code / Type | QUERY_TYPE |
| System Audit | Read Security Configuration | Result | ERROR_CODE |
| System Audit | Read Security Configuration | Username | USER_NAME |
| System Audit | Read Security Configuration | User Type / Role | ROLE_NAME |
| System Audit | Read Security Configuration | Session ID | SESSION_ID |
| System Audit | Read Security Configuration | Configuration / Setting Value | QUERY_TEXT |
| System Audit | Update Security Configuration | Timestamp | START_TIME |
| System Audit | Update Security Configuration | Event ID | QUERY_ID |
| System Audit | Update Security Configuration | Event Code / Type | QUERY_TYPE |
| System Audit | Update Security Configuration | Result | ERROR_CODE |
| System Audit | Update Security Configuration | Username | USER_NAME |
| System Audit | Update Security Configuration | User Type / Role | ROLE_NAME |
| System Audit | Update Security Configuration | Session ID | SESSION_ID |
| System Audit | Update Security Configuration | Configuration / Setting Name | QUERY_TEXT |
| System Audit | Update Security Configuration | Configuration / Setting Value | QUERY_TEXT |
| System Audit | Delete Security Configuration | Timestamp | START_TIME |
| System Audit | Delete Security Configuration | Event ID | QUERY_ID |
| System Audit | Delete Security Configuration | Event Code / Type | QUERY_TYPE |
| System Audit | Delete Security Configuration | Result | ERROR_CODE |
| System Audit | Delete Security Configuration | Username | USER_NAME |
| System Audit | Delete Security Configuration | User Type / Role | ROLE_NAME |
| System Audit | Delete Security Configuration | Session ID | SESSION_ID |
| System Audit | Delete Security Configuration | Configuration / Setting Name | QUERY_TEXT |
| System Audit | Delete Security Configuration | Configuration / Setting Value | QUERY_TEXT |
| System Audit | Create Integration | Timestamp | START_TIME |
| System Audit | Create Integration | Event ID | QUERY_ID |
| System Audit | Create Integration | Event Code / Type | QUERY_TYPE |
| System Audit | Create Integration | Result | ERROR_CODE |
| System Audit | Create Integration | Username | USER_NAME |
| System Audit | Create Integration | User Type / Role | ROLE_NAME |
| System Audit | Create Integration | Session ID | SESSION_ID |
| System Audit | Create Integration | Integration / App Name | QUERY_TEXT |
| System Audit | Read Integration | Timestamp | START_TIME |
| System Audit | Read Integration | Event ID | QUERY_ID |
| System Audit | Read Integration | Event Code / Type | QUERY_TYPE |
| System Audit | Read Integration | Result | ERROR_CODE |
| System Audit | Read Integration | Username | USER_NAME |
| System Audit | Read Integration | User Type / Role | ROLE_NAME |
| System Audit | Read Integration | Session ID | SESSION_ID |
| System Audit | Read Integration | Integration / App Name | QUERY_TEXT |
| System Audit | Update Integration | Timestamp | START_TIME |
| System Audit | Update Integration | Event ID | QUERY_ID |
| System Audit | Update Integration | Event Code / Type | QUERY_TYPE |
| System Audit | Update Integration | Result | ERROR_CODE |
| System Audit | Update Integration | Username | USER_NAME |
| System Audit | Update Integration | User Type / Role | ROLE_NAME |
| System Audit | Update Integration | Session ID | SESSION_ID |
| System Audit | Update Integration | Configuration / Setting Name | QUERY_TEXT |
| System Audit | Update Integration | Integration / App Name | QUERY_TEXT |
| System Audit | Delete Integration | Timestamp | START_TIME |
| System Audit | Delete Integration | Event ID | QUERY_ID |
| System Audit | Delete Integration | Event Code / Type | QUERY_TYPE |
| System Audit | Delete Integration | Result | ERROR_CODE |
| System Audit | Delete Integration | Username | USER_NAME |
| System Audit | Delete Integration | User Type / Role | ROLE_NAME |
| System Audit | Delete Integration | Session ID | SESSION_ID |
| System Audit | Delete Integration | Integration / App Name | QUERY_TEXT |
| Activity Audit | Create Resource | Timestamp | START_TIME |
| Activity Audit | Create Resource | Event ID | QUERY_ID |
| Activity Audit | Create Resource | Event Code / Type | QUERY_TYPE |
| Activity Audit | Create Resource | Result | ERROR_CODE |
| Activity Audit | Create Resource | Username | USER_NAME |
| Activity Audit | Create Resource | User Type / Role | ROLE_NAME |
| Activity Audit | Create Resource | Session ID | SESSION_ID |
| Activity Audit | Create Resource | Resource Name | QUERY_TEXT |
| Activity Audit | Create Resource | Resource Type | QUERY_TEXT |
| Activity Audit | Read Resource | Timestamp | START_TIME |
| Activity Audit | Read Resource | Event ID | QUERY_ID |
| Activity Audit | Read Resource | Event Code / Type | QUERY_TYPE |
| Activity Audit | Read Resource | Result | ERROR_CODE |
| Activity Audit | Read Resource | Username | USER_NAME |
| Activity Audit | Read Resource | User Type / Role | ROLE_NAME |
| Activity Audit | Read Resource | Session ID | SESSION_ID |
| Activity Audit | Read Resource | Resource Name | QUERY_TEXT |
| Activity Audit | Read Resource | Resource Type | QUERY_TEXT |
| Activity Audit | Update Resource | Timestamp | START_TIME |
| Activity Audit | Update Resource | Event ID | QUERY_ID |
| Activity Audit | Update Resource | Event Code / Type | QUERY_TYPE |
| Activity Audit | Update Resource | Result | ERROR_CODE |
| Activity Audit | Update Resource | Username | USER_NAME |
| Activity Audit | Update Resource | User Type / Role | ROLE_NAME |
| Activity Audit | Update Resource | Session ID | SESSION_ID |
| Activity Audit | Update Resource | Resource Name | QUERY_TEXT |
| Activity Audit | Update Resource | Resource Type | QUERY_TEXT |
| Activity Audit | Delete Resource | Timestamp | START_TIME |
| Activity Audit | Delete Resource | Event ID | QUERY_ID |
| Activity Audit | Delete Resource | Event Code / Type | QUERY_TYPE |
| Activity Audit | Delete Resource | Result | ERROR_CODE |
| Activity Audit | Delete Resource | Username | USER_NAME |
| Activity Audit | Delete Resource | User Type / Role | ROLE_NAME |
| Activity Audit | Delete Resource | Session ID | SESSION_ID |
| Activity Audit | Delete Resource | Resource Name | QUERY_TEXT |
| Activity Audit | Delete Resource | Resource Type | QUERY_TEXT |
| Activity Audit | Download Resource | Timestamp | START_TIME |
| Activity Audit | Download Resource | Event ID | QUERY_ID |
| Activity Audit | Download Resource | Event Code / Type | QUERY_TYPE |
| Activity Audit | Download Resource | Result | ERROR_CODE |
| Activity Audit | Download Resource | Username | USER_NAME |
| Activity Audit | Download Resource | User Type / Role | ROLE_NAME |
| Activity Audit | Download Resource | Session ID | SESSION_ID |
| Activity Audit | Download Resource | Resource Name | QUERY_TEXT |
| Activity Audit | Download Resource | Resource Type | QUERY_TEXT |
| Activity Audit | Download Resource | Resource Metadata | QUERY_TEXT |

## Example logs

| Category | Event type | Log | Sample field values |
| -------- | ---------- | --- | ------------------- |
| Authorization | Create User | [success](/products/snowflake/event_examples/query_history/authorization_create_user.json) | Timestamp=1717698436.307000; Event ID=01b4d553-0000-83bf-0000-151118855e511e; Event Code / Type=CREATE_USER; Result=None; Username=ALFRED_ADMIN |
| Authorization | Read User | [success](/products/snowflake/event_examples/query_history/authorization_read_user.json) | Timestamp=1717698436.307000; Event ID=01b4d553-0000-83bf-0000-151118855e511e; Event Code / Type=SHOW; Result=None; Username=ALFRED_ADMIN |
| Authorization | Update User | [success](/products/snowflake/event_examples/query_history/authorization_update_user.json) | Timestamp=1717071412.964000; Event ID=01b4ac80-0000-83bf-0000-15165sdc5151; Event Code / Type=ALTER_USER; Result=None; Username=ALFRED_ADMIN |
| Authorization | Delete User | [success](/products/snowflake/event_examples/query_history/authorization_delete_user.json) | Timestamp=1717685383.026000; Event ID=44ed5de-0002-3f81-0001-44ed5de44ed5dee; Event Code / Type=DROP_USER; Result=None; Username=ALFRED_ADMIN@wayneenerprises.org |
| Authorization | Create Role | [success](/products/snowflake/event_examples/query_history/authorization_create_role.json) | Timestamp=1717774231.171000; Event ID=01b4da42-0509-r73t-0068-2j9d9v97eb; Event Code / Type=CREATE_ROLE; Result=None; Username=ALFRED_ADMIN |
| Authorization | Read Role | [success](/products/snowflake/event_examples/query_history/authorization_read_role.json) | Timestamp=1717774231.171000; Event ID=01b4da42-0509-r73t-0068-2j9d9v97eb; Event Code / Type=SHOW; Result=None; Username=ALFRED_ADMIN |
| Authorization | Update Role | [success](/products/snowflake/event_examples/query_history/authorization_update_role.json) | Timestamp=1717310018.655000; Event ID=01b4bc09-5759-e717-002f-5fg5151g61d5f2; Event Code / Type=ALTER_ROLE; Result=None; Username=BWAYNE@wayneenterprises.org |
| Authorization | Delete Role | [success](/products/snowflake/event_examples/query_history/authorization_delete_role.json) | Timestamp=1717763466.536000; Event ID=01b4d98f-0002-55ge-0000-c5165v07e1c9ea; Event Code / Type=DROP_ROLE; Result=None; Username=ALFRED_ADMIN |
| Authorization | Add Permission | [success](/products/snowflake/event_examples/query_history/authorization_add_permission.json) | Timestamp=1716999270.649000; Event ID=01b4a7ce-0000-66gh-0000-65165115a3bda; Event Code / Type=GRANT; Result=None; Username=ALFRED_ADMIN |
| Authorization | Remove Permission | [success](/products/snowflake/event_examples/query_history/authorization_remove_permission.json) | Timestamp=1717740555.111000; Event ID=01b4d811-0509-5f55-0068-2d034deb8633; Event Code / Type=REVOKE; Result=None; Username=ALFRED_ADMIN |
| Authorization | Remove Enrollment | [success](/products/snowflake/event_examples/query_history/authorization_remove_enrollment.json) | Timestamp=1717514614.899000; Event ID=01b4c95b-0000-83c0-1250-045151d18c90e; Event Code / Type=ALTER_USER; Result=None; Username=ALFRED_ADMIN |
| System Audit | Create Security Configuration | [success](/products/snowflake/event_examples/query_history/system_audit_create_security_configuration.json) | Timestamp=1717510863.429000; Event ID=01b4c91d-4444-83bf-0000-566815187b52; Event Code / Type=CREATE; Result=None; Username=ALFRED_ADMIN |
| System Audit | Read Security Configuration | [success](/products/snowflake/event_examples/query_history/system_audit_read_security_configuration.json) | Timestamp=1717685508.585000; Event ID=01b4d47b-0045-3f94-0071-5451651a1de7a2a; Event Code / Type=SHOW; Result=None; Username=BRUCE_WAYN@wayneenterprises.org |
| System Audit | Update Security Configuration | [success](/products/snowflake/event_examples/query_history/system_audit_update_security_configuration.json) | Timestamp=1717685508.585000; Event ID=01b4d47b-0045-3f94-0071-5451651a1de7a2a; Event Code / Type=ALTER; Result=None; Username=BRUCE_WAYN@wayneenterprises.org |
| System Audit | Delete Security Configuration | [success](/products/snowflake/event_examples/query_history/system_audit_delete_security_configuration.json) | Timestamp=1717685508.585000; Event ID=01b4d47b-0045-3f94-0071-5451651a1de7a2a; Event Code / Type=SHOW; Result=None; Username=BRUCE_WAYN@wayneenterprises.org |
| System Audit | Create Integration | [success](/products/snowflake/event_examples/query_history/system_audit_create_integration.json) | Timestamp=1717439033.791000; Event ID=01b4c65d-0504-e717-0000-15894ac5e9c2; Event Code / Type=CREATE; Result=None; Username=ALFRED_ADMIN |
| System Audit | Read Integration | [success](/products/snowflake/event_examples/query_history/system_audit_read_integration.json) | Timestamp=1717439033.791000; Event ID=01b4c65d-0504-e717-0000-15894ac5e9c2; Event Code / Type=DESCRIBE; Result=None; Username=ALFRED_ADMIN |
| System Audit | Update Integration | [success](/products/snowflake/event_examples/query_history/system_audit_update_integration.json) | Timestamp=1717439033.791000; Event ID=01b4c65d-0504-e717-0000-15894ac5e9c2; Event Code / Type=ALTER; Result=None; Username=ALFRED_ADMIN |
| System Audit | Delete Integration | [success](/products/snowflake/event_examples/query_history/system_audit_delete_integration.json) | Timestamp=1717685508.585000; Event ID=01b4d47b-0045-3f94-0071-5451651a1de7a2a; Event Code / Type=SHOW; Result=None; Username=BRUCE_WAYN@wayneenterprises.org |
| Activity Audit | Create Resource | [success](/products/snowflake/event_examples/query_history/activity_audit_create_resource.json) | Timestamp=1717680342.585000; Event ID=01b4d425-0509-54fd-0068-2d034e5caba3; Event Code / Type=INSERT; Result=None; Username=ALFRED_ADMIN |
| Activity Audit | Read Resource | [success](/products/snowflake/event_examples/query_history/activity_audit_read_resource.json) | Timestamp=1717680342.585000; Event ID=01b4d425-0509-54fd-0068-2d034e5caba3; Event Code / Type=SELECT; Result=None; Username=ALFRED_ADMIN |
| Activity Audit | Update Resource | [success](/products/snowflake/event_examples/query_history/activity_audit_update_resource.json) | Timestamp=1717680342.585000; Event ID=01b4d425-0509-54fd-0068-2d034e5caba3; Event Code / Type=INSERT; Result=None; Username=ALFRED_ADMIN |
| Activity Audit | Delete Resource | [success](/products/snowflake/event_examples/query_history/activity_audit_delete_resource.json) | Timestamp=1717680342.585000; Event ID=01b4d425-0509-54fd-0068-2d034e5caba3; Event Code / Type=DROP; Result=None; Username=ALFRED_ADMIN |
| Activity Audit | Download Resource | [success](/products/snowflake/event_examples/query_history/activity_audit_download_resource.json) | Timestamp=1717680342.585000; Event ID=01b4d425-0509-54fd-0068-2d034e5caba3; Event Code / Type=GET_FILES; Result=None; Username=ALFRED_ADMIN |


