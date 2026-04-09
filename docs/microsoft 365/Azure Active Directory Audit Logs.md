# Microsoft 365 — Azure Active Directory Audit Logs

📌 **v1.0.0** · 🗄 **Retention:** 180 days · ⚡ **Latency:** Typically 60 to 90 minutes after an event occurs.

🗄 Minimum retention is 180 days, but organizations can set a retention policy up to 10 years dependent on licensing, reference https://learn.microsoft.com/en-us/purview/audit-log-retention-policies⚡ Microsoft does not provide a specific audit logging latency SLA, reference https://learn.microsoft.com/en-us/purview/audit-search?view=o365-worldwide&tabs=microsoft-purview-portal📜 **Licensing:** Standard and Premium audit licenses are available, with log availability and retention dependent on the license level.

For more information, see https://learn.microsoft.com/en-us/purview/audit-search?view=o365-worldwide&tabs=microsoft-purview-portal


Includes logs from Azure Active Directory including authentication and user management.
## References
* [Azure Active Directory Base Schema](https://learn.microsoft.com/en-us/office/office-365-management-api/office-365-management-activity-api-schema#azure-active-directory-base-schema)
## Field mappings

| Category | Event type | Attribute | Source field(s) |
| -------- | ---------- | --------- | ---------------- |
| Authentication | Account Login | Timestamp | CreationTime |
| Authentication | Account Login | Event ID | Id |
| Authentication | Account Login | Event Code / Type | Operation |
| Authentication | Account Login | Username | UserId |
| Authentication | Account Login | User ID | UserKey |
| Authentication | Account Login | User Type / Role | Actor[].Type |
| Authentication | Account Login | Session ID | DeviceProperties[Name=SessionId].Value |
| Authentication | Account Login | IP Address | ClientIP |
| Authentication | Account Login | User Agent Name | ExtendedProperties[Name=UserAgent].Value |
| Authentication | Account Login | Device/Client Type | DeviceProperties |
| Authentication | Account Login | Identity Service Provider Context | ExtendedProperties[Name=RequestType].Value |
| Authentication | MFA Verification | Timestamp | CreationTime |
| Authentication | MFA Verification | Event ID | Id |
| Authentication | MFA Verification | Event Code / Type | Operation |
| Authentication | MFA Verification | Result | ResultStatus |
| Authentication | MFA Verification | Username | UserId |
| Authentication | MFA Verification | User ID | UserKey |
| Authentication | MFA Verification | User Type / Role | Actor[].Type |
| Authentication | MFA Verification | IP Address | ClientIP |
| Authentication | MFA Verification | User Agent Name | ExtendedProperties[Name=UserAgent].Value |
| Authentication | MFA Verification | Device/Client Type | DeviceProperties |
| Authorization | Create User | Timestamp | CreationTime |
| Authorization | Create User | Event ID | Id |
| Authorization | Create User | Event Code / Type | Operation |
| Authorization | Create User | Result | ResultStatus |
| Authorization | Create User | Username | UserId |
| Authorization | Create User | User ID | UserKey |
| Authorization | Create User | User Type / Role | Actor[ID=User].Type, Actor[ID=ServicePrincipal].Type |
| Authorization | Create User | Target Username | Target.ID |
| Authorization | Update User | Timestamp | CreationTime |
| Authorization | Update User | Event ID | Id |
| Authorization | Update User | Event Code / Type | Operation |
| Authorization | Update User | Result | ResultStatus |
| Authorization | Update User | Username | UserId |
| Authorization | Update User | User ID | UserKey |
| Authorization | Update User | User Type / Role | Actor[ID=User].Type, Actor[ID=ServicePrincipal].Type |
| Authorization | Update User | Target Username | Target.ID |
| Authorization | Update User | Target Attribute Context | ModifiedProperties |
| Authorization | Delete User | Timestamp | CreationTime |
| Authorization | Delete User | Event ID | Id |
| Authorization | Delete User | Event Code / Type | Operation |
| Authorization | Delete User | Result | ResultStatus |
| Authorization | Delete User | Username | UserId |
| Authorization | Delete User | User ID | UserKey |
| Authorization | Delete User | User Type / Role | Actor[ID=User].Type, Actor[ID=ServicePrincipal].Type |
| Authorization | Delete User | Target Username | Target.ID |
| Authorization | Create Group | Timestamp | CreationTime |
| Authorization | Create Group | Event ID | Id |
| Authorization | Create Group | Event Code / Type | Operation |
| Authorization | Create Group | Result | ResultStatus |
| Authorization | Create Group | Username | UserId |
| Authorization | Create Group | User ID | UserKey |
| Authorization | Create Group | User Type / Role | Actor[ID=User].Type, Actor[ID=ServicePrincipal].Type |
| Authorization | Create Group | Target Group Name | Target.ID |
| Authorization | Update Group | Timestamp | CreationTime |
| Authorization | Update Group | Event ID | Id |
| Authorization | Update Group | Event Code / Type | Operation |
| Authorization | Update Group | Result | ResultStatus |
| Authorization | Update Group | Username | UserId |
| Authorization | Update Group | User ID | UserKey |
| Authorization | Update Group | User Type / Role | Actor[ID=User].Type, Actor[ID=ServicePrincipal].Type |
| Authorization | Update Group | Target Group Name | Target.ID |
| Authorization | Delete Group | Timestamp | CreationTime |
| Authorization | Delete Group | Event ID | Id |
| Authorization | Delete Group | Event Code / Type | Operation |
| Authorization | Delete Group | Result | ResultStatus |
| Authorization | Delete Group | Username | UserId |
| Authorization | Delete Group | User ID | UserKey |
| Authorization | Delete Group | User Type / Role | Actor[ID=User].Type, Actor[ID=ServicePrincipal].Type |
| Authorization | Delete Group | Target Group Name | Target.ID |
| Authorization | Add To Group | Timestamp | CreationTime |
| Authorization | Add To Group | Event ID | Id |
| Authorization | Add To Group | Event Code / Type | Operation |
| Authorization | Add To Group | Result | ResultStatus |
| Authorization | Add To Group | Username | UserId |
| Authorization | Add To Group | User ID | UserKey |
| Authorization | Add To Group | User Type / Role | Actor[ID=User].Type, Actor[ID=ServicePrincipal].Type |
| Authorization | Add To Group | Device/Client Type | ExtendedProperties[Name=additionalDetails].Value |
| Authorization | Add To Group | Target Username | Target.ID |
| Authorization | Add To Group | Target Group Name | ModifiedProperties[Name=Group.DisplayName].NewValue |
| Authorization | Remove From Group | Timestamp | CreationTime |
| Authorization | Remove From Group | Event ID | Id |
| Authorization | Remove From Group | Event Code / Type | Operation |
| Authorization | Remove From Group | Result | ResultStatus |
| Authorization | Remove From Group | Username | UserId |
| Authorization | Remove From Group | User ID | UserKey |
| Authorization | Remove From Group | User Type / Role | Actor[ID=User].Type, Actor[ID=ServicePrincipal].Type |
| Authorization | Remove From Group | User Agent Name | ExtendedProperties[Name=additionalDetails].Value |
| Authorization | Remove From Group | Target Username | Target.ID |
| Authorization | Remove From Group | Target Group Name | ModifiedProperties[Name=Group.DisplayName].NewValue |
| Authorization | Create Role | Timestamp | CreationTime |
| Authorization | Create Role | Event ID | Id |
| Authorization | Create Role | Event Code / Type | Operation |
| Authorization | Create Role | Result | ResultStatus |
| Authorization | Create Role | Username | UserId |
| Authorization | Create Role | User ID | UserKey |
| Authorization | Create Role | User Type / Role | Actor[ID=User].Type, Actor[ID=ServicePrincipal].Type |
| Authorization | Create Role | User Agent Name | ExtendedProperties[Name=additionalDetails].Value |
| Authorization | Create Role | Target Role Name | Target.ID |
| Authorization | Update Role | Timestamp | CreationTime |
| Authorization | Update Role | Event ID | Id |
| Authorization | Update Role | Event Code / Type | Operation |
| Authorization | Update Role | Result | ResultStatus |
| Authorization | Update Role | Username | UserId |
| Authorization | Update Role | User ID | UserKey |
| Authorization | Update Role | User Type / Role | Actor[ID=User].Type, Actor[ID=ServicePrincipal].Type |
| Authorization | Update Role | User Agent Name | ExtendedProperties[Name=additionalDetails].Value |
| Authorization | Update Role | Target Attribute Context | ModifiedProperties[Name=GrantedPermissions].NewValue |
| Authorization | Update Role | Target Role Name | Target.ID |
| Authorization | Delete Role | Timestamp | CreationTime |
| Authorization | Delete Role | Event ID | Id |
| Authorization | Delete Role | Event Code / Type | Operation |
| Authorization | Delete Role | Result | ResultStatus |
| Authorization | Delete Role | Username | UserId |
| Authorization | Delete Role | User ID | UserKey |
| Authorization | Delete Role | User Type / Role | Actor[ID=User].Type, Actor[ID=ServicePrincipal].Type |
| Authorization | Delete Role | User Agent Name | ExtendedProperties[Name=additionalDetails].Value |
| Authorization | Delete Role | Target Role Name | Target.ID |
| Authorization | Add Permission | Timestamp | CreationTime |
| Authorization | Add Permission | Event ID | Id |
| Authorization | Add Permission | Event Code / Type | Operation |
| Authorization | Add Permission | Result | ResultStatus |
| Authorization | Add Permission | Username | UserId |
| Authorization | Add Permission | User ID | UserKey |
| Authorization | Add Permission | User Type / Role | Actor[ID=User].Type, Actor[ID=ServicePrincipal].Type |
| Authorization | Add Permission | Permission Name | ModifiedProperties[Name=Role.DisplayName].NewValue |
| Authorization | Add Permission | Target Resource Name | Target.ID |
| Authorization | Remove Permission | Timestamp | CreationTime |
| Authorization | Remove Permission | Event ID | Id |
| Authorization | Remove Permission | Event Code / Type | Operation |
| Authorization | Remove Permission | Result | ResultStatus |
| Authorization | Remove Permission | Username | UserId |
| Authorization | Remove Permission | User ID | UserKey |
| Authorization | Remove Permission | User Type / Role | Actor[ID=User].Type, Actor[ID=ServicePrincipal].Type |
| Authorization | Remove Permission | Permission Name | ModifiedProperties[Name=Role.DisplayName].OldValue |
| Authorization | Remove Permission | Target Resource Name | Target.ID |
| Authorization | Add Enrollment | Timestamp | CreationTime |
| Authorization | Add Enrollment | Event ID | Id |
| Authorization | Add Enrollment | Event Code / Type | Operation |
| Authorization | Add Enrollment | Result | ResultStatus |
| Authorization | Add Enrollment | Username | UserId |
| Authorization | Add Enrollment | User ID | UserKey |
| Authorization | Add Enrollment | User Type / Role | Actor[ID=User].Type, Actor[ID=ServicePrincipal].Type |
| Authorization | Add Enrollment | Target Username | Target.ID |
| Authorization | Add Enrollment | Enrollment Type | ModifiedProperties[Name=StrongAuthenticationUserDetails].NewValue |
| Authorization | Remove Enrollment | Timestamp | CreationTime |
| Authorization | Remove Enrollment | Event ID | Id |
| Authorization | Remove Enrollment | Event Code / Type | Operation |
| Authorization | Remove Enrollment | Result | ResultStatus |
| Authorization | Remove Enrollment | Username | UserId |
| Authorization | Remove Enrollment | User ID | UserKey |
| Authorization | Remove Enrollment | User Type / Role | Actor[ID=User].Type, Actor[ID=ServicePrincipal].Type |
| Authorization | Remove Enrollment | Target Username | Target.ID |
| Authorization | Remove Enrollment | Enrollment Type | ModifiedProperties[Name=StrongAuthenticationPhoneAppDetail].OldValue |
| System Audit | Create Security Configuration | Timestamp | CreationTime |
| System Audit | Create Security Configuration | Event ID | Id |
| System Audit | Create Security Configuration | Event Code / Type | Operation |
| System Audit | Create Security Configuration | Result | ResultStatus |
| System Audit | Create Security Configuration | Username | UserId |
| System Audit | Create Security Configuration | User ID | UserKey |
| System Audit | Create Security Configuration | User Type / Role | Actor[ID=User].Type, Actor[ID=ServicePrincipal].Type |
| System Audit | Create Security Configuration | User Agent Name | ExtendedProperties[Name=additionalDetails].Value |
| System Audit | Create Security Configuration | Configuration / Setting Name | ModifiedProperties[Name=PolicyType].NewValue |
| System Audit | Create Security Configuration | Configuration / Setting Value | ModifiedProperties |
| System Audit | Update Security Configuration | Timestamp | CreationTime |
| System Audit | Update Security Configuration | Event ID | Id |
| System Audit | Update Security Configuration | Event Code / Type | Operation |
| System Audit | Update Security Configuration | Result | ResultStatus |
| System Audit | Update Security Configuration | Username | UserId |
| System Audit | Update Security Configuration | User ID | UserKey |
| System Audit | Update Security Configuration | User Type / Role | Actor[ID=User].Type, Actor[ID=ServicePrincipal].Type |
| System Audit | Update Security Configuration | User Agent Name | ExtendedProperties[Name=additionalDetails].Value |
| System Audit | Update Security Configuration | Configuration / Setting Name | ExtendedProperties[Name=extendedAuditEventCategory].Value |
| System Audit | Update Security Configuration | Configuration / Setting Value | ModifiedProperties[Name=Included Updated Properties].NewValue |
| System Audit | Update Security Configuration | Previous Configuration / Setting Value | ModifiedProperties |
| System Audit | Delete Security Configuration | Timestamp | CreationTime |
| System Audit | Delete Security Configuration | Event ID | Id |
| System Audit | Delete Security Configuration | Event Code / Type | Operation |
| System Audit | Delete Security Configuration | Result | ResultStatus |
| System Audit | Delete Security Configuration | Username | UserId |
| System Audit | Delete Security Configuration | User ID | UserKey |
| System Audit | Delete Security Configuration | User Type / Role | Actor[ID=User].Type, Actor[ID=ServicePrincipal].Type |
| System Audit | Delete Security Configuration | User Agent Name | ExtendedProperties[Name=additionalDetails].Value |
| System Audit | Delete Security Configuration | Configuration / Setting Name | ExtendedProperties[Name=extendedAuditEventCategory].Value |
| System Audit | Create Integration | Timestamp | CreationTime |
| System Audit | Create Integration | Event ID | Id |
| System Audit | Create Integration | Event Code / Type | Operation |
| System Audit | Create Integration | Result | ResultStatus |
| System Audit | Create Integration | Username | UserId |
| System Audit | Create Integration | User ID | UserKey |
| System Audit | Create Integration | User Type / Role | Actor[ID=User].Type, Actor[ID=ServicePrincipal].Type |
| System Audit | Create Integration | Integration / App Name | ModifiedProperties[Name=DisplayName].NewValue |
| System Audit | Update Integration | Timestamp | CreationTime |
| System Audit | Update Integration | Event ID | Id |
| System Audit | Update Integration | Event Code / Type | Operation |
| System Audit | Update Integration | Result | ResultStatus |
| System Audit | Update Integration | Username | UserId |
| System Audit | Update Integration | User ID | UserKey |
| System Audit | Update Integration | User Type / Role | Actor[ID=User].Type, Actor[ID=ServicePrincipal].Type |
| System Audit | Update Integration | Configuration / Setting Name | ModifiedProperties |
| System Audit | Update Integration | Previous Configuration / Setting Value | ModifiedProperties[Name=Entitlement].OldValue |
| System Audit | Update Integration | Integration / App Name | Target.ID |
| System Audit | Delete Integration | Timestamp | CreationTime |
| System Audit | Delete Integration | Event ID | Id |
| System Audit | Delete Integration | Event Code / Type | Operation |
| System Audit | Delete Integration | Result | ResultStatus |
| System Audit | Delete Integration | Username | UserId |
| System Audit | Delete Integration | User ID | UserKey |
| System Audit | Delete Integration | User Type / Role | Actor[ID=User].Type, Actor[ID=ServicePrincipal].Type |
| System Audit | Delete Integration | Integration / App Name | Target.ID |

## Example logs

| Category | Event type | Log | Sample field values |
| -------- | ---------- | --- | ------------------- |
| Authentication | Account Login | [success](/products/microsoft_365/event_examples/azure_ad/authentication_account_login_success.json) | Timestamp=2024-05-01T17:24:06; Event ID=0e523898-a3ab-4ba8-9c33-a6cc38050b03; Event Code / Type=UserLoggedIn; Username=example@test.onmicrosoft.comm; User ID=1a3b0ad5-eda1-4f48-b877-3b002e5d85b5 |
| Authentication | Account Login | [failure](/products/microsoft_365/event_examples/azure_ad/authentication_account_login_failure.json) | Timestamp=2024-05-02T02:15:53; Event ID=514d0006-6b28-446c-8f7c-e85271a31200; Event Code / Type=UserLoginFailed; Username=Not Available; User ID=1a3b0ad5-eda1-4f48-b877-3b002e5d85b5 |
| Authentication | MFA Verification | [success](/products/microsoft_365/event_examples/azure_ad/authentication_mfa_verification.json) | Timestamp=2024-05-01T03:59:39; Event ID=ffdb8af6-ce7e-4218-93f8-79024f7e3300; Event Code / Type=UserLoggedIn; Result=Success; Username=Not Available |
| Authorization | Create User | [success](/products/microsoft_365/event_examples/azure_ad/authorization_create_user.json) | Timestamp=2024-05-01T21:29:10; Event ID=d17a8564-4f63-4792-a063-4ecf01e1b7a1; Event Code / Type=Add user.; Result=Success; Username=example@test.onmicrosoft.com |
| Authorization | Update User | [success](/products/microsoft_365/event_examples/azure_ad/authorization_update_user.json) | Timestamp=2024-05-01T19:03:01; Event ID=7df508c4-a9a3-4c58-b39f-a6ef3c171d41; Event Code / Type=Update user.; Result=Success; Username=ServicePrincipal_ac1c885a-da2e-446e-9f3f-544e5f988861 |
| Authorization | Delete User | [success](/products/microsoft_365/event_examples/azure_ad/authorization_delete_user.json) | Timestamp=2024-05-01T21:34:00; Event ID=d168a319-f0e6-4fff-900f-447a4f624d9d; Event Code / Type=Delete user.; Result=Success; Username=example@test.onmicrosoft.com |
| Authorization | Create Group | [success](/products/microsoft_365/event_examples/azure_ad/authorization_create_group.json) | Timestamp=2024-05-01T16:25:27; Event ID=dadb97b5-59e0-40e8-9d39-0be9bbcf584b; Event Code / Type=Add group.; Result=Success; Username=ServicePrincipal_ac1c885a-da2e-446e-9f3f-544e5f988861 |
| Authorization | Update Group | [success](/products/microsoft_365/event_examples/azure_ad/authorization_update_group.json) | Timestamp=2024-05-01T16:26:29; Event ID=469d7f6a-494e-42ef-aebd-195301726b0c; Event Code / Type=Update group.; Result=Success; Username=ServicePrincipal_ac1c885a-da2e-446e-9f3f-544e5f988861 |
| Authorization | Delete Group | [success](/products/microsoft_365/event_examples/azure_ad/authorization_delete_group.json) | Timestamp=2024-05-01T16:26:51; Event ID=1bcdf6d9-d41e-408a-ad70-0a2ec1e040d2; Event Code / Type=Delete group.; Result=Success; Username=ServicePrincipal_ac1c885a-da2e-446e-9f3f-544e5f988861 |
| Authorization | Add To Group | [success](/products/microsoft_365/event_examples/azure_ad/authorization_add_member_to_group.json) | Timestamp=2024-05-01T05:10:05; Event ID=d74b2827-73e9-4ca4-8d9e-882f11a1f354; Event Code / Type=Add member to group.; Result=Success; Username=example@test.onmicrosoft.com |
| Authorization | Remove From Group | [success](/products/microsoft_365/event_examples/azure_ad/authorization_remove_member_from_group.json) | Timestamp=2024-05-01T05:27:56; Event ID=1ab6721e-1557-4138-8417-15378b431bda; Event Code / Type=Remove member from group.; Result=Success; Username=example@test.onmicrosoft.com |
| Authorization | Create Role | [success](/products/microsoft_365/event_examples/azure_ad/authorization_create_role.json) | Timestamp=2024-05-01T21:35:05; Event ID=414a577a-6bcc-489d-a3c3-6919423134b1; Event Code / Type=Add role definition.; Result=Success; Username=example@test.onmicrosoft.com |
| Authorization | Update Role | [success](/products/microsoft_365/event_examples/azure_ad/authorization_update_role.json) | Timestamp=2024-05-01T21:35:59; Event ID=c7a002e8-8dbd-43a7-8c64-8de5910f49ff; Event Code / Type=Update role definition.; Result=Success; Username=example@test.onmicrosoft.com |
| Authorization | Delete Role | [success](/products/microsoft_365/event_examples/azure_ad/authorization_delete_role.json) | Timestamp=2024-05-01T21:36:10; Event ID=f377408a-4cde-46ae-a658-f0042cc3f652; Event Code / Type=Delete role definition.; Result=Success; Username=example@test.onmicrosoft.com |
| Authorization | Add Permission | [success](/products/microsoft_365/event_examples/azure_ad/authorization_add_permission.json) | Timestamp=2024-05-01T21:31:15; Event ID=87025648-8434-4b73-a311-9eb82a0845fd; Event Code / Type=Add member to role.; Result=Success; Username=ServicePrincipal_09eaff3d-53e5-4fbe-9752-92c8505c97cd |
| Authorization | Remove Permission | [success](/products/microsoft_365/event_examples/azure_ad/authorization_remove_permission.json) | Timestamp=2024-05-01T21:31:15; Event ID=b6973e19-e37e-4b03-b077-0a1d2de71106; Event Code / Type=Remove member from role.; Result=Success; Username=ServicePrincipal_09eaff3d-53e5-4fbe-9752-92c8505c97cd |
| Authorization | Add Enrollment | [success](/products/microsoft_365/event_examples/azure_ad/authorization_add_enrollment.json) | Timestamp=2024-05-02T01:47:58; Event ID=d13709bc-1139-4afe-996c-40d28014186b; Event Code / Type=Update user.; Result=Success; Username=TestUser10@test.onmicrosoft.com |
| Authorization | Remove Enrollment | [success](/products/microsoft_365/event_examples/azure_ad/authorization_remove_enrollment.json) | Timestamp=2024-05-02T02:16:16; Event ID=0ec7c8b7-77cb-4aa4-bee9-834e4dc9491a; Event Code / Type=Update user.; Result=Success; Username=ServicePrincipal_14de7e5c-d71d-4803-afd0-4cbc978b0d84 |
| System Audit | Create Security Configuration | [success](/products/microsoft_365/event_examples/azure_ad/system_audit_create_security_configuration_cap.json) | Timestamp=2024-05-01T21:41:34; Event ID=b1fe6046-32f3-4464-9769-1fedc9122000; Event Code / Type=Add policy.; Result=Success; Username=example@test.onmicrosoft.com |
| System Audit | Update Security Configuration | [success](/products/microsoft_365/event_examples/azure_ad/system_audit_update_security_configuration_cap.json) | Timestamp=2024-05-01T21:41:53; Event ID=5bf46a0b-5c14-468e-9b1f-bbb861d60411; Event Code / Type=Update policy.; Result=Success; Username=example@test.onmicrosoft.com |
| System Audit | Delete Security Configuration | [success](/products/microsoft_365/event_examples/azure_ad/system_audit_delete_security_configuration_cap.json) | Timestamp=2024-05-01T21:42:17; Event ID=f26d627b-40b0-42d6-9ab1-97de7ec000d6; Event Code / Type=Delete policy.; Result=Success; Username=example@test.onmicrosoft.com |
| System Audit | Create Integration | [success](/products/microsoft_365/event_examples/azure_ad/system_audit_create_integration.json) | Timestamp=2024-05-01T21:43:37; Event ID=2f2af1ba-6d5f-40d2-863e-5263bb46a62c; Event Code / Type=Add application.; Result=Success; Username=ServicePrincipal_4f990b57-c537-4671-b080-8b6ffd9aded7 |
| System Audit | Update Integration | [success](/products/microsoft_365/event_examples/azure_ad/system_audit_update_integration.json) | Timestamp=2024-05-01T21:43:39; Event ID=86732c26-5672-4756-acad-6d336ecaea71; Event Code / Type=Update application.; Result=Success; Username=ServicePrincipal_4f990b57-c537-4671-b080-8b6ffd9aded7 |
| System Audit | Delete Integration | [success](/products/microsoft_365/event_examples/azure_ad/system_audit_delete_integration.json) | Timestamp=2024-05-01T21:45:46; Event ID=dc3a6b43-7cbf-4e35-8cc0-0ac7622aedcb; Event Code / Type=Delete application.; Result=Success; Username=example@test.onmicrosoft.com |


