# Veeva Vault — Retrieve Audit Details API

📌 **v0.0.1** · 🗄 **Retention:** 30 days · ⚡ **Latency:** Near real-time

📜 **Licensing:** A Veeva Vault license is required to access the Retrieve Audit Details API.

The Veeva Vault Retrieve Audit Details API provides near real-time, read-only access to an organization's audit log.
## References
* [Retrieve Audit Details API Documentation](https://developer.veevavault.com/api/24.1/#retrieve-audit-details)
## Field mappings

| Category | Event type | Attribute | Source field(s) |
| -------- | ---------- | --------- | ---------------- |
| Authentication | Account Login | Timestamp | timestamp |
| Authentication | Account Login | Event ID | id |
| Authentication | Account Login | Event Code / Type | type |
| Authentication | Account Login | Username | user_name |
| Authentication | Account Login | IP Address | source_ip |
| Authentication | Account Login | User Agent Name | platform |
| Authentication | Account Login | Failure Context | status |
| Authentication | Account Logout | Timestamp | timestamp |
| Authentication | Account Logout | Event ID | id |
| Authentication | Account Logout | Event Code / Type | type |
| Authentication | Account Logout | Username | user_name |
| Authentication | Account Logout | IP Address | source_ip |
| Authentication | Account Logout | User Agent Name | platform |
| Authorization | Create User | Timestamp | timestamp |
| Authorization | Create User | Event ID | id |
| Authorization | Create User | Event Code / Type | action |
| Authorization | Create User | Username | user_name |
| Authorization | Create User | Target Username | item |
| Authorization | Update User | Timestamp | timestamp |
| Authorization | Update User | Event ID | id |
| Authorization | Update User | Event Code / Type | action |
| Authorization | Update User | Username | user_name |
| Authorization | Update User | Target Username | item |
| Authorization | Update User | Target Attribute Context | field_name |
| Authorization | Create Group | Timestamp | timestamp |
| Authorization | Create Group | Event ID | id |
| Authorization | Create Group | Event Code / Type | action |
| Authorization | Create Group | Username | user_name |
| Authorization | Create Group | Target Group Name | item |
| Authorization | Update Group | Timestamp | timestamp |
| Authorization | Update Group | Event ID | id |
| Authorization | Update Group | Event Code / Type | action |
| Authorization | Update Group | Username | user_name |
| Authorization | Update Group | Target Attribute Context | field_name |
| Authorization | Update Group | Target Group Name | item |
| Authorization | Delete Group | Timestamp | timestamp |
| Authorization | Delete Group | Event ID | id |
| Authorization | Delete Group | Event Code / Type | action |
| Authorization | Delete Group | Username | user_name |
| Authorization | Delete Group | Target Group Name | item |
| Authorization | Add To Group | Timestamp | timestamp |
| Authorization | Add To Group | Event ID | id |
| Authorization | Add To Group | Event Code / Type | action |
| Authorization | Add To Group | Username | user_name |
| Authorization | Add To Group | Target Username | new_value |
| Authorization | Add To Group | Target Group Name | item |
| Authorization | Remove From Group | Timestamp | timestamp |
| Authorization | Remove From Group | Event ID | id |
| Authorization | Remove From Group | Event Code / Type | action |
| Authorization | Remove From Group | Username | user_name |
| Authorization | Remove From Group | Target Username | old_value |
| Authorization | Remove From Group | Target Group Name | item |
| Authorization | Create Role | Timestamp | timestamp |
| Authorization | Create Role | Event ID | id |
| Authorization | Create Role | Event Code / Type | action |
| Authorization | Create Role | Username | user_name |
| Authorization | Create Role | Target Role Name | item |
| Authorization | Update Role | Timestamp | timestamp |
| Authorization | Update Role | Event ID | id |
| Authorization | Update Role | Event Code / Type | action |
| Authorization | Update Role | Username | user_name |
| Authorization | Update Role | Target Attribute Context | field_name |
| Authorization | Update Role | Target Role Name | item |
| Authorization | Delete Role | Timestamp | timestamp |
| Authorization | Delete Role | Event ID | id |
| Authorization | Delete Role | Event Code / Type | action |
| Authorization | Delete Role | Username | user_name |
| Authorization | Delete Role | Target Role Name | item |
| Authorization | Add Permission | Timestamp | timestamp |
| Authorization | Add Permission | Event ID | id |
| Authorization | Add Permission | Event Code / Type | action |
| Authorization | Add Permission | Username | user_name |
| Authorization | Add Permission | Permission Name | new_value |
| Authorization | Add Permission | Target Resource Name | item |
| Authorization | Remove Permission | Timestamp | timestamp |
| Authorization | Remove Permission | Event ID | id |
| Authorization | Remove Permission | Event Code / Type | action |
| Authorization | Remove Permission | Username | user_name |
| Authorization | Remove Permission | Permission Name | field_name |
| Authorization | Remove Permission | Target Resource Name | item |
| System Audit | Create Integration | Timestamp | timestamp |
| System Audit | Create Integration | Event ID | id |
| System Audit | Create Integration | Event Code / Type | action |
| System Audit | Create Integration | Username | user_name |
| System Audit | Create Integration | Integration / App Name | item |
| System Audit | Update Integration | Timestamp | timestamp |
| System Audit | Update Integration | Event ID | id |
| System Audit | Update Integration | Event Code / Type | action |
| System Audit | Update Integration | Username | user_name |
| System Audit | Update Integration | Configuration / Setting Name | new_value |
| System Audit | Update Integration | Integration / App Name | item |
| System Audit | Delete Integration | Timestamp | timestamp |
| System Audit | Delete Integration | Event ID | id |
| System Audit | Delete Integration | Event Code / Type | action |
| System Audit | Delete Integration | Username | user_name |
| System Audit | Delete Integration | Integration / App Name | item |
| Activity Audit | Create Resource | Timestamp | timestamp |
| Activity Audit | Create Resource | Event ID | id |
| Activity Audit | Create Resource | Event Code / Type | action |
| Activity Audit | Create Resource | Username | user_name |
| Activity Audit | Create Resource | Resource Name | item |
| Activity Audit | Create Resource | Resource Type | object_label |
| Activity Audit | Read Resource | Timestamp | timestamp |
| Activity Audit | Read Resource | Event ID | id |
| Activity Audit | Read Resource | Event Code / Type | action |
| Activity Audit | Read Resource | Username | user_name |
| Activity Audit | Read Resource | Resource Name | item |
| Activity Audit | Update Resource | Timestamp | timestamp |
| Activity Audit | Update Resource | Event ID | id |
| Activity Audit | Update Resource | Event Code / Type | action |
| Activity Audit | Update Resource | Username | user_name |
| Activity Audit | Update Resource | Resource Name | item |
| Activity Audit | Update Resource | Resource Type | object_label |
| Activity Audit | Delete Resource | Timestamp | timestamp |
| Activity Audit | Delete Resource | Event ID | id |
| Activity Audit | Delete Resource | Event Code / Type | action |
| Activity Audit | Delete Resource | Username | user_name |
| Activity Audit | Delete Resource | Resource Name | item |
| Activity Audit | Delete Resource | Resource Type | object_label |
| Activity Audit | Download Resource | Timestamp | timestamp |
| Activity Audit | Download Resource | Event ID | id |
| Activity Audit | Download Resource | Event Code / Type | action |
| Activity Audit | Download Resource | Username | user_name |
| Activity Audit | Download Resource | Resource Metadata | item |

## Example logs

| Category | Event type | Log | Sample field values |
| -------- | ---------- | --- | ------------------- |
| Authentication | Account Login | [success](/products/veeva_vault/event_examples/authentication_account_login_session_success.json) | Timestamp=2024-05-07T21:01:27Z; Event ID=6145782847; Event Code / Type=User Login; Username=bbunny@acme.com; IP Address=8.8.8.8 |
| Authentication | Account Login | [failure](/products/veeva_vault/event_examples/authentication_account_login_session_failure.json) | Timestamp=2024-05-08T21:17:23Z; Event ID=6151724407; Event Code / Type=User Login; Username=granny@acme.com; IP Address=8.8.8.8 |
| Authentication | Account Logout | [success](/products/veeva_vault/event_examples/authentication_account_logout.json) | Timestamp=2024-05-07T20:18:07Z; Event ID=6145624385; Event Code / Type=User Logout; Username=bbunny@acme.com; IP Address=8.8.8.8 |
| Authorization | Create User | [success](/products/veeva_vault/event_examples/authorization_create_user.json) | Timestamp=2024-05-07T23:19:06Z; Event ID=123188; Event Code / Type=Create; Username=bbunny@acme.com; Target Username=User : example_firstname example_lastname |
| Authorization | Update User | [success](/products/veeva_vault/event_examples/authorization_update_user.json) | Timestamp=2024-05-07T23:19:35Z; Event ID=123193; Event Code / Type=Edit; Username=bbunny@acme.com; Target Username=User : example_firstname example_lastname |
| Authorization | Create Group | [success](/products/veeva_vault/event_examples/authorization_create_group.json) | Timestamp=2024-05-07T23:21:12Z; Event ID=726727; Event Code / Type=Create; Username=bbunny@acme.com; Target Group Name=example_group_123 |
| Authorization | Update Group | [success](/products/veeva_vault/event_examples/authorization_update_group.json) | Timestamp=2024-05-07T23:21:28Z; Event ID=726729; Event Code / Type=Edit; Username=bbunny@acme.com; Target Attribute Context=groupDescr |
| Authorization | Delete Group | [success](/products/veeva_vault/event_examples/authorization_delete_group.json) | Timestamp=2024-05-07T23:21:49Z; Event ID=726731; Event Code / Type=Delete; Username=bbunny@acme.com; Target Group Name=example_group_123 |
| Authorization | Add To Group | [success](/products/veeva_vault/event_examples/authorization_add_to_group.json) | Timestamp=2024-05-07T22:20:50Z; Event ID=726692; Event Code / Type=Edit_ListProperty; Username=bbunny@acme.com; Target Username=jdoe@acme.com |
| Authorization | Remove From Group | [success](/products/veeva_vault/event_examples/authorization_remove_from_group.json) | Timestamp=2024-05-07T23:20:35Z; Event ID=726721; Event Code / Type=Edit_ListProperty; Username=System; Target Username=example_user_123@acme.com |
| Authorization | Create Role | [success](/products/veeva_vault/event_examples/authorization_create_role.json) | Timestamp=2024-05-08T20:24:13Z; Event ID=123212; Event Code / Type=Create; Username=bbunny@acme.com; Target Role Name=Application Role : example_new_role |
| Authorization | Update Role | [success](/products/veeva_vault/event_examples/authorization_update_role.json) | Timestamp=2024-05-08T21:16:31Z; Event ID=123221; Event Code / Type=Edit; Username=bbunny@acme.com; Target Attribute Context=Permission Set |
| Authorization | Delete Role | [success](/products/veeva_vault/event_examples/authorization_delete_role.json) | Timestamp=2024-05-08T20:24:33Z; Event ID=123214; Event Code / Type=Delete; Username=bbunny@acme.com; Target Role Name=Application Role : example_new_role |
| Authorization | Add Permission | [success](/products/veeva_vault/event_examples/authorization_add_permission.json) | Timestamp=2024-05-10T13:53:39Z; Event ID=731223; Event Code / Type=Edit; Username=pbunyan@acme.com; Permission Name=Vault Owner |
| Authorization | Remove Permission | [success](/products/veeva_vault/event_examples/authorization_remove_permission.json) | Timestamp=2024-05-08T23:03:03Z; Event ID=726747; Event Code / Type=RemovePermission; Username=bbunny@acme.com; Permission Name=Admin > Configuration > Pages > Edit |
| System Audit | Create Integration | [success](/products/veeva_vault/event_examples/system_audit_create_integration.json) | Timestamp=2024-05-09T18:23:21Z; Event ID=123225; Event Code / Type=Create; Username=System; Integration / App Name=Connection Client : example_external_connection |
| System Audit | Update Integration | [success](/products/veeva_vault/event_examples/system_audit_update_integration.json) | Timestamp=2024-05-09T18:42:23Z; Event ID=123226; Event Code / Type=Edit; Username=bbunny@acme.com; Configuration / Setting Name=https://appomni.test_url.com |
| System Audit | Delete Integration | [success](/products/veeva_vault/event_examples/system_audit_delete_integration.json) | Timestamp=2024-05-09T18:50:15Z; Event ID=123232; Event Code / Type=Delete; Username=bbunny@acme.com; Integration / App Name=Connection : External : example_external_connection |
| Activity Audit | Create Resource | [success](/products/veeva_vault/event_examples/activity_audit_create_resource.json) | Timestamp=2024-05-09T20:18:54Z; Event ID=123244; Event Code / Type=Create; Username=bbunny@acme.com; Resource Name=Study : example_study_1337 |
| Activity Audit | Read Resource | [success](/products/veeva_vault/event_examples/activity_audit_read_resource.json) | Timestamp=2024-05-14T21:37:10Z; Event ID=729; Event Code / Type=GetDocumentVersion; Username=jdoe@acme.com; Resource Name=VV-TMF-12345 |
| Activity Audit | Update Resource | [success](/products/veeva_vault/event_examples/activity_audit_update_resource.json) | Timestamp=2024-05-09T19:59:52Z; Event ID=123243; Event Code / Type=Edit; Username=bbunny@acme.com; Resource Name=Subject : example_subject_id |
| Activity Audit | Delete Resource | [success](/products/veeva_vault/event_examples/activity_audit_delete_resource.json) | Timestamp=2024-05-09T20:19:06Z; Event ID=123245; Event Code / Type=Delete; Username=bbunny@acme.com; Resource Name=Study : example_study_1337 |
| Activity Audit | Download Resource | [success](/products/veeva_vault/event_examples/activity_audit_download_resource.json) | Timestamp=2024-05-07T19:24:09Z; Event ID=650; Event Code / Type=Download; Username=bbunny@acme.com; Resource Metadata=VV-TMF-00017 |


