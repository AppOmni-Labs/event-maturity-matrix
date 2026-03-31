# Duo — Duo Administrator Logs

📌 **v1.0.0** · 🗄 **Retention:** Configurable · ⚡ **Latency:** Near real-time

🗄 Administrator logs are stored based on the log retention interval setting. If no custom log retention interval has been specified, Administrator logs can be retrieved from the time the account was initially created, reference https://help.duo.com/s/article/2990?language=en_US


⚡ N/A


📜 **Licensing:** The Duo Admin API is available to Duo Premier, Duo Advantage, and Duo Essentials customers, and new customers with an Advantage or Premier trial. For more information, see https://duo.com/docs/adminapi#about-the-admin-api


Provides an audit trail of administrative actions taken within the Duo Security platform.
## References
* [Duo Administrator Logs](https://duo.com/docs/adminapi#administrator-logs)
## Field mappings

| Category | Event type | Attribute | Source field(s) |
| -------- | ---------- | --------- | ---------------- |
| Authentication | Account Login | Timestamp | isotimestamp, timestamp |
| Authentication | Account Login | Event Code / Type | action |
| Authentication | Account Login | Result | action |
| Authentication | Account Login | Username | username, description.email |
| Authentication | Account Login | User Type / Role | description.role |
| Authentication | Account Login | IP Address | description.ip_address |
| Authentication | Account Login | Device/Client Type | description.device |
| Authentication | Account Login | Failure Context | description.error |
| Authentication | MFA Verification | Timestamp | isotimestamp, timestamp |
| Authentication | MFA Verification | Event Code / Type | action |
| Authentication | MFA Verification | Result | action, error |
| Authentication | MFA Verification | Username | username, description.email |
| Authentication | MFA Verification | IP Address | description.ip_address |
| Authentication | MFA Verification | Verification Method | description.factor |
| Authentication | MFA Verification | Verification Flagged | description.error |
| Authorization | Create User | Timestamp | isotimestamp, timestamp |
| Authorization | Create User | Event Code / Type | action |
| Authorization | Create User | Username | username |
| Authorization | Create User | User Type / Role | description.role |
| Authorization | Create User | Target Username | description.uname, object |
| Authorization | Update User | Timestamp | isotimestamp, timestamp |
| Authorization | Update User | Event Code / Type | action |
| Authorization | Update User | Username | username |
| Authorization | Update User | Target Username | object |
| Authorization | Update User | Target Attribute Context | description |
| Authorization | Delete User | Timestamp | isotimestamp, timestamp |
| Authorization | Delete User | Event Code / Type | action |
| Authorization | Delete User | Username | username |
| Authorization | Delete User | User Type / Role | description.role |
| Authorization | Delete User | Target Username | object |
| Authorization | Create Group | Timestamp | isotimestamp, timestamp |
| Authorization | Create Group | Event Code / Type | action |
| Authorization | Create Group | Username | username |
| Authorization | Create Group | Target Group Name | description.name, object |
| Authorization | Update Group | Timestamp | isotimestamp, timestamp |
| Authorization | Update Group | Event Code / Type | action |
| Authorization | Update Group | Username | username |
| Authorization | Update Group | Target Attribute Context | description |
| Authorization | Update Group | Target Group Name | object |
| Authorization | Delete Group | Timestamp | isotimestamp, timestamp |
| Authorization | Delete Group | Event Code / Type | action |
| Authorization | Delete Group | Username | username |
| Authorization | Delete Group | Target Group Name | object, description.name |
| Authorization | Add To Group | Timestamp | isotimestamp, timestamp |
| Authorization | Add To Group | Event Code / Type | action |
| Authorization | Add To Group | Username | username |
| Authorization | Add To Group | Target Username | object |
| Authorization | Add To Group | Target Group Name | description.groups.name |
| Authorization | Remove From Group | Timestamp | isotimestamp, timestamp |
| Authorization | Remove From Group | Event Code / Type | action |
| Authorization | Remove From Group | Username | username |
| Authorization | Remove From Group | Target Username | object |
| Authorization | Add Enrollment | Timestamp | isotimestamp, timestamp |
| Authorization | Add Enrollment | Event Code / Type | action |
| Authorization | Add Enrollment | Username | username |
| Authorization | Add Enrollment | User Agent Name | description.user_agent |
| Authorization | Add Enrollment | Target Username | description.owner_name |
| Authorization | Add Enrollment | Enrollment Type | description.authenticator_type |
| Authorization | Remove Enrollment | Timestamp | isotimestamp, timestamp |
| Authorization | Remove Enrollment | Event Code / Type | action |
| Authorization | Remove Enrollment | Username | username |
| Authorization | Remove Enrollment | Target Username | object |
| Authorization | Remove Enrollment | Enrollment Type | description |
| System Audit | Create Security Configuration | Timestamp | isotimestamp, timestamp |
| System Audit | Create Security Configuration | Event Code / Type | action |
| System Audit | Create Security Configuration | Username | username |
| System Audit | Create Security Configuration | Configuration / Setting Name | action |
| System Audit | Update Security Configuration | Timestamp | isotimestamp, timestamp |
| System Audit | Update Security Configuration | Event Code / Type | action |
| System Audit | Update Security Configuration | Username | username |
| System Audit | Update Security Configuration | Configuration / Setting Name | action, description |
| System Audit | Update Security Configuration | Configuration / Setting Value | description |
| System Audit | Delete Security Configuration | Timestamp | isotimestamp, timestamp |
| System Audit | Delete Security Configuration | Event Code / Type | action |
| System Audit | Delete Security Configuration | Username | username |
| System Audit | Delete Security Configuration | Configuration / Setting Name | action, description, object |
| System Audit | Delete Security Configuration | Configuration / Setting Value | description |
| System Audit | Create Integration | Timestamp | isotimestamp |
| System Audit | Create Integration | Event Code / Type | action |
| System Audit | Create Integration | Username | username |
| System Audit | Create Integration | Integration / App Name | description.name, object |
| System Audit | Update Integration | Timestamp | isotimestamp |
| System Audit | Update Integration | Event Code / Type | action |
| System Audit | Update Integration | Username | username |
| System Audit | Update Integration | Configuration / Setting Name | description |
| System Audit | Update Integration | Integration / App Name | object |
| System Audit | Delete Integration | Timestamp | isotimestamp |
| System Audit | Delete Integration | Event Code / Type | action |
| System Audit | Delete Integration | Username | username |
| System Audit | Delete Integration | Integration / App Name | description.name, object |
| Activity Audit | Create Resource | Timestamp | isotimestamp, timestamp |
| Activity Audit | Create Resource | Event Code / Type | action |
| Activity Audit | Create Resource | Username | username |
| Activity Audit | Create Resource | Resource Name | object |
| Activity Audit | Create Resource | Resource Type | action, description |
| Activity Audit | Update Resource | Timestamp | isotimestamp, timestamp |
| Activity Audit | Update Resource | Event Code / Type | action |
| Activity Audit | Update Resource | Username | username |
| Activity Audit | Update Resource | Resource Name | action, description |
| Activity Audit | Update Resource | Resource Type | action, description |
| Activity Audit | Delete Resource | Timestamp | isotimestamp, timestamp |
| Activity Audit | Delete Resource | Event Code / Type | action |
| Activity Audit | Delete Resource | Username | username |
| Activity Audit | Delete Resource | Resource Name | object |
| Activity Audit | Delete Resource | Resource Type | action, description |

## Example logs

| Category | Event type | Log | Sample field values |
| -------- | ---------- | --- | ------------------- |
| Authentication | Account Login | [success](/products/duo/event_examples/authentication_account_login_success_admin.json) | Timestamp=2024-05-17T17:24:21+00:00; Event Code / Type=admin_login; Result=admin_login; Username=John Doe; User Type / Role=Owner |
| Authentication | Account Login | [failure](/products/duo/event_examples/authentication_account_login_failure_admin.json) | Timestamp=2024-05-20T19:23:45+00:00; Event Code / Type=admin_login_error; Result=admin_login_error; Username=Jane Doe; IP Address=192.168.1.1 |
| Authentication | MFA Verification | [failure](/products/duo/event_examples/authentication_mfa_verification_failure_admin.json) | Timestamp=2024-05-21T17:58:04+00:00; Event Code / Type=admin_2fa_error; Result=admin_2fa_error; Username=Smith, John; IP Address=192.168.10.1 |
| Authentication | MFA Verification | [flagged](/products/duo/event_examples/authentication_mfa_verification_failure_flagged_admin.json) | Timestamp=2024-05-23T19:17:28+00:00; Event Code / Type=admin_2fa_error; Result=admin_2fa_error; Username=Joe Smith; IP Address=192.168.1.2 |
| Authorization | Create User | [user](/products/duo/event_examples/authorization_create_user_admin.json) | Timestamp=2024-05-17T17:24:53+00:00; Event Code / Type=user_create; Username=Jane Doe; Target Username=bbanner@example.com |
| Authorization | Create User | [admin](/products/duo/event_examples/authorization_create_user_admin_admin.json) | Timestamp=2024-05-23T20:16:23+00:00; Event Code / Type=admin_create; Username=Jane Doe; User Type / Role=Administrator; Target Username=Bruce Wayne |
| Authorization | Update User | [user](/products/duo/event_examples/authorization_update_user_admin.json) | Timestamp=2024-05-23T19:41:21+00:00; Event Code / Type=user_update; Username=James Doe; Target Username=tonystark; Target Attribute Context={'email': 'tonystark@acme.com', 'realname': 'Tony Stark'} |
| Authorization | Update User | [admin](/products/duo/event_examples/authorization_update_user_admin_admin.json) | Timestamp=2024-05-29T12:54:47+00:00; Event Code / Type=admin_update; Username=John Doe; Target Username=Bruce Banner; Target Attribute Context={'administrative_units': '', 'restricted_by_admin_units': F… |
| Authorization | Delete User | [user](/products/duo/event_examples/authorization_delete_user_admin.json) | Timestamp=2024-05-17T17:30:04+00:00; Event Code / Type=user_pending_delete; Username=John Doe; Target Username=sally.smith@example.com |
| Authorization | Delete User | [admin](/products/duo/event_examples/authorization_delete_user_admin_admin.json) | Timestamp=2024-05-23T20:16:36+00:00; Event Code / Type=admin_delete; Username=Jane Doe; User Type / Role=Administrator; Target Username=Bob Smith |
| Authorization | Create Group | [success](/products/duo/event_examples/authorization_create_group_admin.json) | Timestamp=2024-05-17T17:31:18+00:00; Event Code / Type=group_create; Username=Jane Doe; Target Group Name=custom_admin_group_east |
| Authorization | Update Group | [success](/products/duo/event_examples/authorization_update_group_admin.json) | Timestamp=2024-05-23T19:42:49+00:00; Event Code / Type=group_update; Username=John Doe; Target Attribute Context={'_status': 'Disabled'}; Target Group Name=custom_group_bypass_users |
| Authorization | Delete Group | [success](/products/duo/event_examples/authorization_delete_group_admin.json) | Timestamp=2024-05-23T19:43:09+00:00; Event Code / Type=group_delete; Username=John Doe; Target Group Name=custom_group_west_users |
| Authorization | Add To Group | [success](/products/duo/event_examples/authorization_add_to_group_admin.json) | Timestamp=2024-05-23T19:43:23+00:00; Event Code / Type=user_update; Username=Jane Doe; Target Username=Mary Smith; Target Group Name=custom_group_user_bypass |
| Authorization | Remove From Group | [success](/products/duo/event_examples/authorization_remove_from_group_admin.json) | Timestamp=2024-05-23T19:43:42+00:00; Event Code / Type=user_update; Username=Jane Doe; Target Username=Steve Smith |
| Authorization | Add Enrollment | [success](/products/duo/event_examples/authorization_add_enrollment_admin.json) | Timestamp=2024-05-17T17:36:03+00:00; Event Code / Type=webauthncredential_create; Username=Jane Doe; User Agent Name=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit…; Target Username=luke.skywalker@republic.com |
| Authorization | Remove Enrollment | [user](/products/duo/event_examples/authorization_remove_enrollment_admin.json) | Timestamp=2024-05-28T17:17:58+00:00; Event Code / Type=user_update; Username=John Doe; Target Username=bob.smith@acme.com; Enrollment Type={"phones": ""} |
| Authorization | Remove Enrollment | [admin](/products/duo/event_examples/authorization_remove_enrollment_admin_admin.json) | Timestamp=2024-05-28T17:18:45+00:00; Event Code / Type=admin_update; Username=Jane Doe; Target Username=Bruce Banner; Enrollment Type={"phone": null} |
| System Audit | Create Security Configuration | [success](/products/duo/event_examples/system_audit_create_security_configuration_admin.json) | Timestamp=2024-05-29T15:03:35+00:00; Event Code / Type=cloudsso_add_saml_authsource; Username=John Doe; Configuration / Setting Name=cloudsso_add_saml_authsource |
| System Audit | Update Security Configuration | [success](/products/duo/event_examples/system_audit_update_security_configuration_admin.json) | Timestamp=2024-05-29T14:34:59+00:00; Event Code / Type=updated_risk_profile; Username=Jane Doe; Configuration / Setting Name=updated_risk_profile; Configuration / Setting Value={'applications': 'Admin API', 'countries': 'Ascension, Afgh… |
| System Audit | Delete Security Configuration | [success](/products/duo/event_examples/system_audit_delete_security_configuration_admin.json) | Timestamp=2024-05-29T14:49:14+00:00; Event Code / Type=policy_delete; Username=Jane Doe; Configuration / Setting Name=policy_delete; Configuration / Setting Value={'admin_email': 'jane.doe@example.com', 'anonymous_ip_polic… |
| System Audit | Create Integration | [success](/products/duo/event_examples/system_audit_create_integration_admin.json) | Timestamp=2024-05-21T15:49:00+00:00; Event Code / Type=integration_create; Username=Jane Doe; Integration / App Name=Salesforce - Single Sign-On |
| System Audit | Update Integration | [success](/products/duo/event_examples/system_audit_update_integration_admin.json) | Timestamp=2024-05-24T18:51:14+00:00; Event Code / Type=integration_update; Username=John Doe; Configuration / Setting Name={'adminapi_admins': True, 'adminapi_info': True, 'adminapi_…; Integration / App Name=Admin API |
| System Audit | Delete Integration | [success](/products/duo/event_examples/system_audit_delete_integration_admin.json) | Timestamp=2024-05-21T15:52:12+00:00; Event Code / Type=integration_delete; Username=Jane Doe; Integration / App Name=Workday - Single Sign-On |
| Activity Audit | Create Resource | [success](/products/duo/event_examples/activity_audit_create_resource_admin.json) | Timestamp=2024-05-29T15:55:42+00:00; Event Code / Type=administrative_unit_create; Username=John Doe; Resource Name=Test Admin Unit; Resource Type=administrative_unit_create |
| Activity Audit | Update Resource | [success](/products/duo/event_examples/activity_audit_update_resource_admin.json) | Timestamp=2024-05-29T16:04:19+00:00; Event Code / Type=custom_messaging_update; Username=John Doe; Resource Name=custom_messaging_update; Resource Type=custom_messaging_update |
| Activity Audit | Delete Resource | [success](/products/duo/event_examples/activity_audit_delete_resource_admin.json) | Timestamp=2024-05-28T17:17:58+00:00; Event Code / Type=phone_delete; Username=Jane Doe; Resource Name=123-456-6789; Resource Type=phone_delete |


