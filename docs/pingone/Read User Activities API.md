





# PingOne — Read User Activities API

📌 **v0.0.1** · 🗄 **Retention:** Unknown · ⚡ **Latency:** Near real-time





📜 **Licensing:** A PingOne license is required to access the Read User Activities API.


The PingOne Read User Activities API provides near real-time, read-only access to an organization's audit activity events.
## References
* [Read User Activities API Documentation](https://apidocs.pingidentity.com/pingone/platform/v1/api/#get-read-user-activities)
## Field mappings

| Category | Event type | Attribute | Source field(s) |
| -------- | ---------- | --------- | ---------------- |
| Authentication | Account Login | Timestamp | recordedAt |
| Authentication | Account Login | Event ID | id |
| Authentication | Account Login | Event Code / Type | action.type |
| Authentication | Account Login | Result | result.status |
| Authentication | Account Login | Username | actors.user.name |
| Authentication | Account Login | User ID | actors.user.id |
| Authentication | Account Login | Session ID | correlationId |
| Authentication | Account Login | IP Address | source.ipAddress |
| Authentication | Account Login | User Agent Name | source.userAgent |
| Authentication | Account Logout | Timestamp | recordedAt |
| Authentication | Account Logout | Event ID | id |
| Authentication | Account Logout | Event Code / Type | action.type |
| Authentication | Account Logout | Result | result.status |
| Authentication | Account Logout | Username | resources.name |
| Authentication | Account Logout | User ID | resources.id |
| Authentication | Account Logout | Session ID | correlationId |
| Authentication | Account Logout | IP Address | source.ipAddress |
| Authentication | Account Logout | User Agent Name | source.userAgent |
| Authentication | MFA Verification | Timestamp | recordedAt |
| Authentication | MFA Verification | Event ID | id |
| Authentication | MFA Verification | Event Code / Type | action.type |
| Authentication | MFA Verification | Result | result.status |
| Authentication | MFA Verification | Username | actors.user.name |
| Authentication | MFA Verification | User ID | actors.user.id |
| Authentication | MFA Verification | Session ID | correlationId |
| Authentication | MFA Verification | IP Address | source.ipAddress |
| Authentication | MFA Verification | User Agent Name | source.userAgent |
| Authentication | MFA Verification | Verification Method | resources.name |
| Authorization | Create User | Timestamp | recordedAt |
| Authorization | Create User | Event ID | id |
| Authorization | Create User | Event Code / Type | action.type |
| Authorization | Create User | Result | result.status |
| Authorization | Create User | Username | actors.user.name |
| Authorization | Create User | User ID | actors.user.id |
| Authorization | Create User | Session ID | correlationId |
| Authorization | Create User | IP Address | source.ipAddress |
| Authorization | Create User | User Agent Name | source.userAgent |
| Authorization | Create User | Target Username | resources[type=USER].name |
| Authorization | Update User | Timestamp | recordedAt |
| Authorization | Update User | Event ID | id |
| Authorization | Update User | Event Code / Type | action.type |
| Authorization | Update User | Result | result.status |
| Authorization | Update User | Username | actors.user.name |
| Authorization | Update User | User ID | actors.user.id |
| Authorization | Update User | Session ID | correlationId |
| Authorization | Update User | IP Address | source.ipAddress |
| Authorization | Update User | User Agent Name | source.userAgent |
| Authorization | Update User | Target Username | resources[type=USER].name |
| Authorization | Update User | Target Attribute Context | result.description |
| Authorization | Delete User | Timestamp | recordedAt |
| Authorization | Delete User | Event ID | id |
| Authorization | Delete User | Event Code / Type | action.type |
| Authorization | Delete User | Result | result.status |
| Authorization | Delete User | Username | actors.user.name |
| Authorization | Delete User | User ID | actors.user.id |
| Authorization | Delete User | Session ID | correlationId |
| Authorization | Delete User | IP Address | source.ipAddress |
| Authorization | Delete User | User Agent Name | source.userAgent |
| Authorization | Delete User | Target Username | resources[type=USER].name |
| Authorization | Create Group | Timestamp | recordedAt |
| Authorization | Create Group | Event ID | id |
| Authorization | Create Group | Event Code / Type | action.type |
| Authorization | Create Group | Result | result.status |
| Authorization | Create Group | Username | actors.user.name |
| Authorization | Create Group | User ID | actors.user.id |
| Authorization | Create Group | Session ID | correlationId |
| Authorization | Create Group | IP Address | source.ipAddress |
| Authorization | Create Group | User Agent Name | source.userAgent |
| Authorization | Create Group | Target Group Name | resources[type=GROUP].name, resources[type=MEMBER_OF_GROUP].name |
| Authorization | Delete Group | Timestamp | recordedAt |
| Authorization | Delete Group | Event ID | id |
| Authorization | Delete Group | Event Code / Type | action.type |
| Authorization | Delete Group | Result | result.status |
| Authorization | Delete Group | Username | actors.user.name |
| Authorization | Delete Group | User ID | actors.user.id |
| Authorization | Delete Group | Session ID | correlationId |
| Authorization | Delete Group | IP Address | source.ipAddress |
| Authorization | Delete Group | User Agent Name | source.userAgent |
| Authorization | Delete Group | Target Group Name | resources[type=GROUP].name, resources[type=MEMBER_OF_GROUP].name |
| Authorization | Add To Group | Timestamp | recordedAt |
| Authorization | Add To Group | Event ID | id |
| Authorization | Add To Group | Event Code / Type | action.type |
| Authorization | Add To Group | Result | result.status |
| Authorization | Add To Group | Username | actors.user.name |
| Authorization | Add To Group | User ID | actors.user.id |
| Authorization | Add To Group | Session ID | correlationId |
| Authorization | Add To Group | IP Address | source.ipAddress |
| Authorization | Add To Group | User Agent Name | source.userAgent |
| Authorization | Add To Group | Target Group Name | resources[type=GROUP].name, resources[type=MEMBER_OF_GROUP].name |
| Authorization | Remove From Group | Timestamp | recordedAt |
| Authorization | Remove From Group | Event ID | id |
| Authorization | Remove From Group | Event Code / Type | action.type |
| Authorization | Remove From Group | Result | result.status |
| Authorization | Remove From Group | Username | actors.user.name |
| Authorization | Remove From Group | User ID | actors.user.id |
| Authorization | Remove From Group | Session ID | correlationId |
| Authorization | Remove From Group | IP Address | source.ipAddress |
| Authorization | Remove From Group | User Agent Name | source.userAgent |
| Authorization | Remove From Group | Target Group Name | resources[type=GROUP].name, resources[type=MEMBER_OF_GROUP].name |
| Authorization | Add Permission | Timestamp | recordedAt |
| Authorization | Add Permission | Event ID | id |
| Authorization | Add Permission | Event Code / Type | action.type |
| Authorization | Add Permission | Result | result.status |
| Authorization | Add Permission | Username | actors.user.name |
| Authorization | Add Permission | User ID | actors.user.id |
| Authorization | Add Permission | Session ID | correlationId |
| Authorization | Add Permission | IP Address | source.ipAddress |
| Authorization | Add Permission | User Agent Name | source.userAgent |
| Authorization | Add Permission | Permission Name | result.description |
| Authorization | Add Permission | Target Resource Name | resources[type=USER].name |
| Authorization | Remove Permission | Timestamp | recordedAt |
| Authorization | Remove Permission | Event ID | id |
| Authorization | Remove Permission | Event Code / Type | action.type |
| Authorization | Remove Permission | Result | result.status |
| Authorization | Remove Permission | Username | actors.user.name |
| Authorization | Remove Permission | User ID | actors.user.id |
| Authorization | Remove Permission | Session ID | correlationId |
| Authorization | Remove Permission | IP Address | source.ipAddress |
| Authorization | Remove Permission | User Agent Name | source.userAgent |
| Authorization | Remove Permission | Permission Name | result.description |
| Authorization | Remove Permission | Target Resource Name | resources[type=USER].name |
| Authorization | Add Enrollment | Timestamp | recordedAt |
| Authorization | Add Enrollment | Event ID | id |
| Authorization | Add Enrollment | Event Code / Type | action.type |
| Authorization | Add Enrollment | Result | result.status |
| Authorization | Add Enrollment | Username | actors.user.name |
| Authorization | Add Enrollment | User ID | actors.user.id |
| Authorization | Add Enrollment | Session ID | correlationId |
| Authorization | Add Enrollment | IP Address | source.ipAddress |
| Authorization | Add Enrollment | User Agent Name | source.userAgent |
| Authorization | Add Enrollment | Target Username | resources[type=USER].name |
| Authorization | Remove Enrollment | Timestamp | recordedAt |
| Authorization | Remove Enrollment | Event ID | id |
| Authorization | Remove Enrollment | Event Code / Type | action.type |
| Authorization | Remove Enrollment | Result | result.status |
| Authorization | Remove Enrollment | Username | actors.user.name |
| Authorization | Remove Enrollment | User ID | actors.user.id |
| Authorization | Remove Enrollment | Session ID | correlationId |
| Authorization | Remove Enrollment | IP Address | source.ipAddress |
| Authorization | Remove Enrollment | User Agent Name | source.userAgent |
| System Audit | Create Security Configuration | Timestamp | recordedAt |
| System Audit | Create Security Configuration | Event ID | id |
| System Audit | Create Security Configuration | Event Code / Type | action.type |
| System Audit | Create Security Configuration | Result | result.status |
| System Audit | Create Security Configuration | Username | actors.user.name |
| System Audit | Create Security Configuration | User ID | actors.user.id |
| System Audit | Create Security Configuration | Session ID | correlationId |
| System Audit | Create Security Configuration | IP Address | source.ipAddress |
| System Audit | Create Security Configuration | User Agent Name | source.userAgent |
| System Audit | Create Security Configuration | Configuration / Setting Name | action.type, resources[0].name |
| System Audit | Update Security Configuration | Timestamp | recordedAt |
| System Audit | Update Security Configuration | Event ID | id |
| System Audit | Update Security Configuration | Event Code / Type | action.type |
| System Audit | Update Security Configuration | Result | result.status |
| System Audit | Update Security Configuration | Username | actors.user.name |
| System Audit | Update Security Configuration | User ID | actors.user.id |
| System Audit | Update Security Configuration | Session ID | correlationId |
| System Audit | Update Security Configuration | IP Address | source.ipAddress |
| System Audit | Update Security Configuration | User Agent Name | source.userAgent |
| System Audit | Update Security Configuration | Configuration / Setting Name | action.type, resources[0].name |
| System Audit | Delete Security Configuration | Timestamp | recordedAt |
| System Audit | Delete Security Configuration | Event ID | id |
| System Audit | Delete Security Configuration | Event Code / Type | action.type |
| System Audit | Delete Security Configuration | Result | result.status |
| System Audit | Delete Security Configuration | Username | actors.user.name |
| System Audit | Delete Security Configuration | User ID | actors.user.id |
| System Audit | Delete Security Configuration | Session ID | correlationId |
| System Audit | Delete Security Configuration | IP Address | source.ipAddress |
| System Audit | Delete Security Configuration | User Agent Name | source.userAgent |
| System Audit | Delete Security Configuration | Configuration / Setting Name | action.type, resources[0].name |
| System Audit | Create Integration | Timestamp | recordedAt |
| System Audit | Create Integration | Event ID | id |
| System Audit | Create Integration | Event Code / Type | action.type |
| System Audit | Create Integration | Result | result.status |
| System Audit | Create Integration | Username | actors.user.name |
| System Audit | Create Integration | User ID | actors.user.id |
| System Audit | Create Integration | Session ID | correlationId |
| System Audit | Create Integration | IP Address | source.ipAddress |
| System Audit | Create Integration | User Agent Name | source.userAgent |
| System Audit | Create Integration | Integration / App Name | resources[type=IDENTITY_PROVIDER].name, resources[type=APPLICATION].name |
| System Audit | Update Integration | Timestamp | recordedAt |
| System Audit | Update Integration | Event ID | id |
| System Audit | Update Integration | Event Code / Type | action.type |
| System Audit | Update Integration | Result | result.status |
| System Audit | Update Integration | Username | actors.user.name |
| System Audit | Update Integration | User ID | actors.user.id |
| System Audit | Update Integration | Session ID | correlationId |
| System Audit | Update Integration | IP Address | source.ipAddress |
| System Audit | Update Integration | User Agent Name | source.userAgent |
| System Audit | Update Integration | Integration / App Name | resources[type=IDENTITY_PROVIDER].name, resources[type=APPLICATION].name |
| System Audit | Delete Integration | Timestamp | recordedAt |
| System Audit | Delete Integration | Event ID | id |
| System Audit | Delete Integration | Event Code / Type | action.type |
| System Audit | Delete Integration | Result | result.status |
| System Audit | Delete Integration | Username | actors.user.name |
| System Audit | Delete Integration | User ID | actors.user.id |
| System Audit | Delete Integration | Session ID | correlationId |
| System Audit | Delete Integration | IP Address | source.ipAddress |
| System Audit | Delete Integration | User Agent Name | source.userAgent |
| System Audit | Delete Integration | Integration / App Name | resources[type=IDENTITY_PROVIDER].name, resources[type=APPLICATION].name |

## Example logs

| Category | Event type | Log | Sample field values |
| -------- | ---------- | --- | ------------------- |
| Authentication | Account Login | [success](/products/pingone/event_examples/authentication_account_login_session_success.json) | Timestamp=2024-04-16T18:52:26.476Z; Event ID=1234abc1-a123-1234-ab12-1ab123a1234a; Event Code / Type=USER.ACCESS_ALLOWED; Result=SUCCESS; Username=jdoe@acme.co |
| Authentication | Account Login | [failure](/products/pingone/event_examples/authentication_account_login_session_failure.json) | Timestamp=2024-04-09T21:41:11.459Z; Event ID=1234abc1-a123-1234-ab12-1ab123a1234a; Event Code / Type=USER.ACCESS_DENIED; Result=FAILED; Username=jsmith@acme.co |
| Authentication | Account Logout | [success](/products/pingone/event_examples/authentication_account_logout.json) | Timestamp=2024-04-16T20:08:56.047Z; Event ID=1234abc1-a123-1234-ab12-1ab123a1234a; Event Code / Type=SESSION.DELETED; Result=SUCCESS; Username=jdoe@acme.co |
| Authentication | MFA Verification | [success](/products/pingone/event_examples/authentication_mfa_verification.json) | Timestamp=2024-04-10T22:25:46.470Z; Event ID=1234abc1-a123-1234-ab12-1ab123a1234a; Event Code / Type=OTP.CHECK_SUCCESS; Result=SUCCESS; Username=jdoe@acme.co |
| Authorization | Create User | [success](/products/pingone/event_examples/authorization_create_user.json) | Timestamp=2024-04-16T20:29:30.951Z; Event ID=1234abc1-a123-1234-ab12-1ab123a1234a; Event Code / Type=USER.CREATED; Result=SUCCESS; Username=jdoe@acme.co |
| Authorization | Update User | [success](/products/pingone/event_examples/authorization_update_user.json) | Timestamp=2024-04-11T21:27:55.327Z; Event ID=1234abc1-a123-1234-ab12-1ab123a1234a; Event Code / Type=USER.UPDATED; Result=SUCCESS; Username=jdoe@acme.co |
| Authorization | Delete User | [success](/products/pingone/event_examples/authorization_delete_user.json) | Timestamp=2024-04-16T20:31:37.745Z; Event ID=1234abc1-a123-1234-ab12-1ab123a1234a; Event Code / Type=USER.DELETED; Result=SUCCESS; Username=jdoe@acme.co |
| Authorization | Create Group | [success](/products/pingone/event_examples/authorization_create_group.json) | Timestamp=2024-04-16T20:32:29.433Z; Event ID=1234abc1-a123-1234-ab12-1ab123a1234a; Event Code / Type=GROUP.CREATED; Result=SUCCESS; Username=jdoe@acme.co |
| Authorization | Delete Group | [success](/products/pingone/event_examples/authorization_delete_group.json) | Timestamp=2024-04-16T20:33:07.000Z; Event ID=1234abc1-a123-1234-ab12-1ab123a1234a; Event Code / Type=GROUP.DELETED; Result=SUCCESS; Username=jdoe@acme.co |
| Authorization | Add To Group | [success](/products/pingone/event_examples/authorization_add_to_group.json) | Timestamp=2024-04-16T20:33:15.525Z; Event ID=1234abc1-a123-1234-ab12-1ab123a1234a; Event Code / Type=MEMBER_OF_GROUP.CREATED; Result=SUCCESS; Username=jdoe@acme.co |
| Authorization | Remove From Group | [success](/products/pingone/event_examples/authorization_remove_from_group.json) | Timestamp=2024-04-16T20:37:01.783Z; Event ID=1234abc1-a123-1234-ab12-1ab123a1234a; Event Code / Type=MEMBER_OF_GROUP.DELETED; Result=SUCCESS; Username=jdoe@acme.co |
| Authorization | Add Permission | [success](/products/pingone/event_examples/authorization_add_permission.json) | Timestamp=2024-04-16T21:09:05.593Z; Event ID=1234abc1-a123-1234-ab12-1ab123a1234a; Event Code / Type=ROLE_ASSIGNMENT.CREATED; Result=SUCCESS; Username=jdoe@acme.co |
| Authorization | Remove Permission | [success](/products/pingone/event_examples/authorization_remove_permission.json) | Timestamp=2024-04-16T21:34:54.934Z; Event ID=1234abc1-a123-1234-ab12-1ab123a1234a; Event Code / Type=ROLE_ASSIGNMENT.DELETED; Result=SUCCESS; Username=jdoe@acme.co |
| Authorization | Add Enrollment | [success](/products/pingone/event_examples/authorization_add_enrollment.json) | Timestamp=2024-04-09T21:33:19.932Z; Event ID=1234abc1-a123-1234-ab12-1ab123a1234a; Event Code / Type=USER.UPDATED; Result=SUCCESS; Username=jdoe@acme.co |
| Authorization | Remove Enrollment | [success](/products/pingone/event_examples/authorization_remove_enrollment.json) | Timestamp=2024-04-09T21:17:42.779Z; Event ID=1234abc1-a123-1234-ab12-1ab123a1234a; Event Code / Type=USER.UPDATED; Result=SUCCESS; Username=jdoe@acme.co |
| System Audit | Create Security Configuration | [success](/products/pingone/event_examples/system_audit_create_security_configuration_idp.json) | Timestamp=2024-04-11T20:39:30.186Z; Event ID=1234abc1-a123-1234-ab12-1ab123a1234a; Event Code / Type=IDENTITY_PROVIDER.CREATED; Result=SUCCESS; Username=jdoe@acme.co |
| System Audit | Update Security Configuration | [success](/products/pingone/event_examples/system_audit_update_security_configuration_idp.json) | Timestamp=2024-04-11T20:39:40.609Z; Event ID=1234abc1-a123-1234-ab12-1ab123a1234a; Event Code / Type=IDENTITY_PROVIDER.UPDATED; Result=SUCCESS; Username=jdoe@acme.co |
| System Audit | Delete Security Configuration | [success](/products/pingone/event_examples/system_audit_delete_security_configuration_idp.json) | Timestamp=2024-04-11T20:39:43.186Z; Event ID=1234abc1-a123-1234-ab12-1ab123a1234a; Event Code / Type=IDENTITY_PROVIDER.DELETED; Result=SUCCESS; Username=jdoe@acme.co |
| System Audit | Create Integration | [success](/products/pingone/event_examples/system_audit_create_integration.json) | Timestamp=2024-04-10T21:57:51.431Z; Event ID=1234abc1-a123-1234-ab12-1ab123a1234a; Event Code / Type=APPLICATION.CREATED; Result=SUCCESS; Username=jdoe@acme.co |
| System Audit | Update Integration | [success](/products/pingone/event_examples/system_audit_update_integration.json) | Timestamp=2024-04-16T22:21:05.813Z; Event ID=1234abc1-a123-1234-ab12-1ab123a1234a; Event Code / Type=APPLICATION.UPDATED; Result=SUCCESS; Username=jdoe@acme.co |
| System Audit | Delete Integration | [success](/products/pingone/event_examples/system_audit_delete_integration.json) | Timestamp=2024-04-16T22:29:48.749Z; Event ID=1234abc1-a123-1234-ab12-1ab123a1234a; Event Code / Type=APPLICATION.DELETED; Result=SUCCESS; Username=jdoe@acme.co |


