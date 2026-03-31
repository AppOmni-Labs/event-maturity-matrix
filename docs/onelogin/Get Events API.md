# OneLogin — Get Events API

📌 **v0.0.1** · 🗄 **Retention:** Unknown · ⚡ **Latency:** Near real-time

🗄 N/A


⚡ N/A


📜 **Licensing:** A OneLogin license is required to access the Get Events API.


The OneLogin events API provides near real-time, read-only access to an organization's activity log.
## References
* [Get Events API Documentation](https://developers.onelogin.com/api-docs/1/events/get-events)
## Field mappings

| Category | Event type | Attribute | Source field(s) |
| -------- | ---------- | --------- | ---------------- |
| Authentication | Account Login | Timestamp | created_at |
| Authentication | Account Login | Event ID | id |
| Authentication | Account Login | Event Code / Type | event_type_id |
| Authentication | Account Login | Username | actor_user_name |
| Authentication | Account Login | User ID | actor_user_id |
| Authentication | Account Login | IP Address | ipaddr |
| Authentication | Account Logout | Timestamp | created_at |
| Authentication | Account Logout | Event ID | id |
| Authentication | Account Logout | Event Code / Type | event_type_id |
| Authentication | MFA Verification | Timestamp | created_at |
| Authentication | MFA Verification | Event ID | id |
| Authentication | MFA Verification | Event Code / Type | event_type_id |
| Authentication | MFA Verification | Username | actor_user_name |
| Authentication | MFA Verification | User ID | actor_user_id |
| Authentication | MFA Verification | IP Address | ipaddr |
| Authentication | MFA Verification | Verification Method | notes |
| Authorization | Create User | Timestamp | created_at |
| Authorization | Create User | Event ID | id |
| Authorization | Create User | Event Code / Type | event_type_id |
| Authorization | Create User | Username | actor_user_name |
| Authorization | Create User | User ID | actor_user_id |
| Authorization | Create User | IP Address | ipaddr |
| Authorization | Create User | Target Username | user_name |
| Authorization | Update User | Timestamp | created_at |
| Authorization | Update User | Event ID | id |
| Authorization | Update User | Event Code / Type | event_type_id |
| Authorization | Update User | Username | actor_user_name |
| Authorization | Update User | User ID | actor_user_id |
| Authorization | Update User | IP Address | ipaddr |
| Authorization | Update User | Target Username | user_name |
| Authorization | Delete User | Timestamp | created_at |
| Authorization | Delete User | Event ID | id |
| Authorization | Delete User | Event Code / Type | event_type_id |
| Authorization | Delete User | Username | actor_user_name |
| Authorization | Delete User | User ID | actor_user_id |
| Authorization | Delete User | IP Address | ipaddr |
| Authorization | Delete User | Target Username | user_name |
| Authorization | Create Group | Timestamp | created_at |
| Authorization | Create Group | Event ID | id |
| Authorization | Create Group | Event Code / Type | event_type_id |
| Authorization | Create Group | Username | actor_user_name |
| Authorization | Create Group | User ID | actor_user_id |
| Authorization | Create Group | IP Address | ipaddr |
| Authorization | Update Group | Timestamp | created_at |
| Authorization | Update Group | Event ID | id |
| Authorization | Update Group | Event Code / Type | event_type_id |
| Authorization | Update Group | Username | actor_user_name |
| Authorization | Update Group | User ID | actor_user_id |
| Authorization | Update Group | IP Address | ipaddr |
| Authorization | Delete Group | Timestamp | created_at |
| Authorization | Delete Group | Event ID | id |
| Authorization | Delete Group | Event Code / Type | event_type_id |
| Authorization | Delete Group | Username | actor_user_name |
| Authorization | Delete Group | User ID | actor_user_id |
| Authorization | Delete Group | IP Address | ipaddr |
| Authorization | Add To Group | Timestamp | created_at |
| Authorization | Add To Group | Event ID | id |
| Authorization | Add To Group | Event Code / Type | event_type_id |
| Authorization | Add To Group | Username | actor_user_name |
| Authorization | Add To Group | User ID | actor_user_id |
| Authorization | Add To Group | IP Address | ipaddr |
| Authorization | Add To Group | Target Username | user_name |
| Authorization | Remove From Group | Timestamp | created_at |
| Authorization | Remove From Group | Event ID | id |
| Authorization | Remove From Group | Event Code / Type | event_type_id |
| Authorization | Remove From Group | Username | actor_user_name |
| Authorization | Remove From Group | User ID | actor_user_id |
| Authorization | Remove From Group | IP Address | ipaddr |
| Authorization | Remove From Group | Target Username | user_name |
| Authorization | Create Role | Timestamp | created_at |
| Authorization | Create Role | Event ID | id |
| Authorization | Create Role | Event Code / Type | event_type_id |
| Authorization | Create Role | Username | actor_user_name |
| Authorization | Create Role | User ID | actor_user_id |
| Authorization | Create Role | IP Address | ipaddr |
| Authorization | Update Role | Timestamp | created_at |
| Authorization | Update Role | Event ID | id |
| Authorization | Update Role | Event Code / Type | event_type_id |
| Authorization | Update Role | Username | actor_user_name |
| Authorization | Update Role | User ID | actor_user_id |
| Authorization | Update Role | IP Address | ipaddr |
| Authorization | Delete Role | Timestamp | created_at |
| Authorization | Delete Role | Event ID | id |
| Authorization | Delete Role | Event Code / Type | event_type_id |
| Authorization | Delete Role | Username | actor_user_name |
| Authorization | Delete Role | User ID | actor_user_id |
| Authorization | Delete Role | IP Address | ipaddr |
| Authorization | Add Permission | Timestamp | created_at |
| Authorization | Add Permission | Event ID | id |
| Authorization | Add Permission | Event Code / Type | event_type_id |
| Authorization | Add Permission | Username | actor_user_name |
| Authorization | Add Permission | User ID | actor_user_id |
| Authorization | Add Permission | IP Address | ipaddr |
| Authorization | Add Permission | Target Resource Name | user_name |
| Authorization | Remove Permission | Timestamp | created_at |
| Authorization | Remove Permission | Event ID | id |
| Authorization | Remove Permission | Event Code / Type | event_type_id |
| Authorization | Remove Permission | Username | actor_user_name |
| Authorization | Remove Permission | User ID | actor_user_id |
| Authorization | Remove Permission | IP Address | ipaddr |
| Authorization | Remove Permission | Target Resource Name | user_name |
| Authorization | Add Enrollment | Timestamp | created_at |
| Authorization | Add Enrollment | Event ID | id |
| Authorization | Add Enrollment | Event Code / Type | event_type_id |
| Authorization | Add Enrollment | Username | actor_user_name |
| Authorization | Add Enrollment | User ID | actor_user_id |
| Authorization | Add Enrollment | IP Address | ipaddr |
| Authorization | Add Enrollment | Target Username | user_name |
| Authorization | Remove Enrollment | Timestamp | created_at |
| Authorization | Remove Enrollment | Event ID | id |
| Authorization | Remove Enrollment | Event Code / Type | event_type_id |
| Authorization | Remove Enrollment | Username | actor_user_name |
| Authorization | Remove Enrollment | User ID | actor_user_id |
| Authorization | Remove Enrollment | IP Address | ipaddr |
| Authorization | Remove Enrollment | Target Username | user_name |
| System Audit | Create Integration | Timestamp | created_at |
| System Audit | Create Integration | Event ID | id |
| System Audit | Create Integration | Event Code / Type | event_type_id |
| System Audit | Create Integration | Username | actor_user_name |
| System Audit | Create Integration | User ID | actor_user_id |
| System Audit | Create Integration | IP Address | ipaddr |
| System Audit | Create Integration | Integration / App Name | app_name |
| System Audit | Update Integration | Timestamp | created_at |
| System Audit | Update Integration | Event ID | id |
| System Audit | Update Integration | Event Code / Type | event_type_id |
| System Audit | Update Integration | Username | actor_user_name |
| System Audit | Update Integration | User ID | actor_user_id |
| System Audit | Update Integration | IP Address | ipaddr |
| System Audit | Update Integration | Integration / App Name | app_name |
| System Audit | Delete Integration | Timestamp | created_at |
| System Audit | Delete Integration | Event ID | id |
| System Audit | Delete Integration | Event Code / Type | event_type_id |
| System Audit | Delete Integration | Username | actor_user_name |
| System Audit | Delete Integration | User ID | actor_user_id |
| System Audit | Delete Integration | IP Address | ipaddr |
| System Audit | Delete Integration | Integration / App Name | app_name |
| Activity Audit | Create Resource | Timestamp | created_at |
| Activity Audit | Create Resource | Event ID | id |
| Activity Audit | Create Resource | Event Code / Type | event_type_id |
| Activity Audit | Create Resource | Username | actor_user_name |
| Activity Audit | Create Resource | User ID | actor_user_id |
| Activity Audit | Create Resource | IP Address | ipaddr |
| Activity Audit | Delete Resource | Timestamp | created_at |
| Activity Audit | Delete Resource | Event ID | id |
| Activity Audit | Delete Resource | Event Code / Type | event_type_id |
| Activity Audit | Delete Resource | Username | actor_user_name |
| Activity Audit | Delete Resource | User ID | actor_user_id |
| Activity Audit | Delete Resource | IP Address | ipaddr |
| Activity Audit | Download Resource | Timestamp | created_at |
| Activity Audit | Download Resource | Event ID | id |
| Activity Audit | Download Resource | Event Code / Type | event_type_id |
| Activity Audit | Download Resource | Username | actor_user_name |
| Activity Audit | Download Resource | User ID | actor_user_id |
| Activity Audit | Download Resource | IP Address | ipaddr |

## Example logs

| Category | Event type | Log | Sample field values |
| -------- | ---------- | --- | ------------------- |
| Authentication | Account Login | [success](/products/onelogin/event_examples/authentication_account_login_session_success.json) | Timestamp=2015-11-26T01:11:22.575Z; Event ID=1234512345; Event Code / Type=5; Username=John Doe; User ID=12345561 |
| Authentication | Account Login | [failure](/products/onelogin/event_examples/authentication_account_login_session_failure.json) | Timestamp=2015-11-26T01:31:48.144Z; Event ID=1234512345; Event Code / Type=6; Username=John Doe; User ID=12345123 |
| Authentication | Account Logout | [success](/products/onelogin/event_examples/authentication_account_logout.json) | Timestamp=2015-11-24T16:53:16.188Z; Event ID=1234512345; Event Code / Type=7 |
| Authentication | MFA Verification | [success](/products/onelogin/event_examples/authentication_mfa_verification.json) | Timestamp=2024-02-26T21:10:40.642Z; Event ID=44962098238; Event Code / Type=1400; Username=Harry Potter; User ID=232044969 |
| Authentication | MFA Verification | [failure](/products/onelogin/event_examples/authentication_mfa_verification_failure.json) | Timestamp=2024-02-27T23:48:09.212Z; Event ID=44994186214; Event Code / Type=1002; Username=Harry Potter; User ID=232044969 |
| Authorization | Create User | [success](/products/onelogin/event_examples/authorization_create_user.json) | Timestamp=2015-11-20T18:29:22.202Z; Event ID=1234512345; Event Code / Type=13; Username=John Doe; User ID=1234517 |
| Authorization | Update User | [success](/products/onelogin/event_examples/authorization_update_user.json) | Timestamp=2015-11-25T05:39:01.919Z; Event ID=1234512345; Event Code / Type=14; Username=John Doe; User ID=12345134 |
| Authorization | Delete User | [success](/products/onelogin/event_examples/authorization_delete_user.json) | Timestamp=2024-02-28T17:58:03.705Z; Event ID=45015573454; Event Code / Type=17; Username=Harry Potter; User ID=232044969 |
| Authorization | Create Group | [success](/products/onelogin/event_examples/authorization_create_group.json) | Timestamp=2024-03-01T23:07:24.993Z; Event ID=45082115051; Event Code / Type=3020; Username=Lance Armstrong; User ID=226011705 |
| Authorization | Update Group | [success](/products/onelogin/event_examples/authorization_update_group.json) | Timestamp=2024-03-01T23:07:45.758Z; Event ID=45082120012; Event Code / Type=3021; Username=Lance Armstrong; User ID=226011705 |
| Authorization | Delete Group | [success](/products/onelogin/event_examples/authorization_delete_group.json) | Timestamp=2024-03-01T23:07:33.053Z; Event ID=45082116944; Event Code / Type=3022; Username=Lance Armstrong; User ID=226011705 |
| Authorization | Add To Group | [success](/products/onelogin/event_examples/authorization_add_to_group.json) | Timestamp=2024-03-06T18:08:39.200Z; Event ID=45191535162; Event Code / Type=14; Username=Lance Armstrong; User ID=226011705 |
| Authorization | Remove From Group | [success](/products/onelogin/event_examples/authorization_remove_from_group.json) | Timestamp=2024-03-06T18:15:09.794Z; Event ID=45191722046; Event Code / Type=14; Username=Lance Armstrong; User ID=226011705 |
| Authorization | Create Role | [success](/products/onelogin/event_examples/authorization_create_role.json) | Timestamp=2024-03-01T23:10:26.647Z; Event ID=45082158160; Event Code / Type=1801; Username=Lance Armstrong; User ID=226011705 |
| Authorization | Update Role | [success](/products/onelogin/event_examples/authorization_update_role.json) | Timestamp=2024-03-06T18:31:12.396Z; Event ID=45192178366; Event Code / Type=1; Username=Lance Armstrong; User ID=226011705 |
| Authorization | Delete Role | [success](/products/onelogin/event_examples/authorization_delete_role.json) | Timestamp=2024-03-06T18:31:50.385Z; Event ID=45192198208; Event Code / Type=1802; Username=Lance Armstrong; User ID=226011705 |
| Authorization | Add Permission | [success](/products/onelogin/event_examples/authorization_add_permission.json) | Timestamp=2024-03-01T23:18:00.847Z; Event ID=45082260689; Event Code / Type=72; Username=Lance Armstrong; User ID=226011705 |
| Authorization | Remove Permission | [success](/products/onelogin/event_examples/authorization_remove_permission.json) | Timestamp=2024-02-26T19:03:42.544Z; Event ID=44958862055; Event Code / Type=73; Username=Lance Armstrong; User ID=226011705 |
| Authorization | Add Enrollment | [success](/products/onelogin/event_examples/authorization_add_enrollment.json) | Timestamp=2015-11-24T09:02:46.359Z; Event ID=1234512345; Event Code / Type=22; Username=John Doe; User ID=12345629 |
| Authorization | Remove Enrollment | [success](/products/onelogin/event_examples/authorization_remove_enrollment.json) | Timestamp=2024-02-26T21:11:23.835Z; Event ID=44962113859; Event Code / Type=24; Username=Lance Armstrong; User ID=226011705 |
| System Audit | Create Integration | [success](/products/onelogin/event_examples/system_audit_create_integration.json) | Timestamp=2024-02-27T20:37:13.351Z; Event ID=44990112363; Event Code / Type=600; Username=Harry Potter; User ID=232044969 |
| System Audit | Update Integration | [success](/products/onelogin/event_examples/system_audit_update_integration.json) | Timestamp=2024-03-04T17:47:42.846Z; Event ID=45133717008; Event Code / Type=601; Username=Lance Armstrong; User ID=226011705 |
| System Audit | Delete Integration | [success](/products/onelogin/event_examples/system_audit_delete_integration.json) | Timestamp=2024-02-27T20:38:22.572Z; Event ID=44990138411; Event Code / Type=602; Username=Harry Potter; User ID=232044969 |
| Activity Audit | Create Resource | [success](/products/onelogin/event_examples/activity_audit_create_resource.json) | Timestamp=2024-02-28T18:31:48.480Z; Event ID=45016591484; Event Code / Type=179; Username=Lance Armstrong; User ID=226011705 |
| Activity Audit | Delete Resource | [success](/products/onelogin/event_examples/activity_audit_delete_resource.json) | Timestamp=2024-03-04T17:54:07.805Z; Event ID=45133880563; Event Code / Type=180; Username=Lance Armstrong; User ID=226011705 |
| Activity Audit | Download Resource | [success](/products/onelogin/event_examples/activity_audit_download_resource.json) | Timestamp=2024-03-04T17:58:38.133Z; Event ID=45133990798; Event Code / Type=27; Username=Lance Armstrong; User ID=226011705 |


