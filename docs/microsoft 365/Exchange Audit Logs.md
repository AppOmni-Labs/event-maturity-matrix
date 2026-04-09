# Microsoft 365 — Exchange Audit Logs

📌 **v1.0.0** · 🗄 **Retention:** 180 days · ⚡ **Latency:** Typically 60 to 90 minutes after an event occurs.

🗄 Minimum retention is 180 days, but organizations can set a retention policy up to 10 years dependent on licensing, reference https://learn.microsoft.com/en-us/purview/audit-log-retention-policies⚡ Microsoft does not provide a specific audit logging latency SLA, reference https://learn.microsoft.com/en-us/purview/audit-search?view=o365-worldwide&tabs=microsoft-purview-portal📜 **Licensing:** Standard and Premium audit licenses are available, with log availability and retention dependent on the license level.

For more information, see https://learn.microsoft.com/en-us/purview/audit-search?view=o365-worldwide&tabs=microsoft-purview-portal


Includes logs for Exchange administration and mailbox activities.
## References
* [Exchange Admin Schema](https://learn.microsoft.com/en-us/office/office-365-management-api/office-365-management-activity-api-schema#exchange-admin-schema)
* [Exchange Mailbox Schema](https://learn.microsoft.com/en-us/office/office-365-management-api/office-365-management-activity-api-schema#exchange-mailbox-schema)
## Field mappings

| Category | Event type | Attribute | Source field(s) |
| -------- | ---------- | --------- | ---------------- |
| Authentication | Account Login | Timestamp | CreationTime |
| Authentication | Account Login | Event ID | Id |
| Authentication | Account Login | Event Code / Type | Operation |
| Authentication | Account Login | Username | UserId |
| Authentication | Account Login | User ID | LogonUserSid |
| Authentication | Account Login | User Type / Role | UserType |
| Authentication | Account Login | Session ID | SessionId |
| Authentication | Account Login | IP Address | ClientIP |
| Authentication | Account Login | User Agent Name | ClientInfoString |
| Authentication | Account Login | Device/Client Type | ClientInfoString |
| Authorization | Create Group | Timestamp | CreationTime |
| Authorization | Create Group | Event ID | Id |
| Authorization | Create Group | Event Code / Type | Operation |
| Authorization | Create Group | Result | ResultStatus |
| Authorization | Create Group | Username | UserId |
| Authorization | Create Group | User ID | UserKey |
| Authorization | Create Group | User Type / Role | UserType |
| Authorization | Create Group | Session ID | SessionId |
| Authorization | Create Group | IP Address | ClientIP |
| Authorization | Create Group | Target Group Name | Parameters[Name=DisplayName].Value |
| Authorization | Update Group | Timestamp | CreationTime |
| Authorization | Update Group | Event ID | Id |
| Authorization | Update Group | Event Code / Type | Operation |
| Authorization | Update Group | Result | ResultStatus |
| Authorization | Update Group | Username | UserId |
| Authorization | Update Group | User ID | UserKey |
| Authorization | Update Group | User Type / Role | UserType |
| Authorization | Update Group | Session ID | SessionId |
| Authorization | Update Group | IP Address | ClientIP |
| Authorization | Update Group | Target Group Name | Parameters[Name=DisplayName].Value |
| Authorization | Delete Group | Timestamp | CreationTime |
| Authorization | Delete Group | Event ID | Id |
| Authorization | Delete Group | Event Code / Type | Operation |
| Authorization | Delete Group | Result | ResultStatus |
| Authorization | Delete Group | Username | UserId |
| Authorization | Delete Group | User ID | UserKey |
| Authorization | Delete Group | User Type / Role | UserType |
| Authorization | Delete Group | Session ID | SessionId |
| Authorization | Delete Group | IP Address | ClientIP |
| Authorization | Add To Group | Timestamp | CreationTime |
| Authorization | Add To Group | Event ID | Id |
| Authorization | Add To Group | Event Code / Type | Operation |
| Authorization | Add To Group | Result | ResultStatus |
| Authorization | Add To Group | Username | UserId |
| Authorization | Add To Group | User ID | UserKey |
| Authorization | Add To Group | User Type / Role | UserType |
| Authorization | Add To Group | Session ID | SessionId |
| Authorization | Add To Group | IP Address | ClientIP |
| Authorization | Remove From Group | Timestamp | CreationTime |
| Authorization | Remove From Group | Event ID | Id |
| Authorization | Remove From Group | Event Code / Type | Operation |
| Authorization | Remove From Group | Result | ResultStatus |
| Authorization | Remove From Group | Username | UserId |
| Authorization | Remove From Group | User ID | UserKey |
| Authorization | Remove From Group | User Type / Role | UserType |
| Authorization | Remove From Group | Session ID | SessionId |
| Authorization | Remove From Group | IP Address | ClientIP |
| Authorization | Create Role | Timestamp | CreationTime |
| Authorization | Create Role | Event ID | Id |
| Authorization | Create Role | Event Code / Type | Operation |
| Authorization | Create Role | Result | ResultStatus |
| Authorization | Create Role | Username | UserId |
| Authorization | Create Role | User ID | UserKey |
| Authorization | Create Role | User Type / Role | UserType |
| Authorization | Create Role | Session ID | SessionId |
| Authorization | Create Role | IP Address | ClientIP |
| Authorization | Create Role | Target Role Name | Parameters.Name |
| Authorization | Update Role | Timestamp | CreationTime |
| Authorization | Update Role | Event ID | Id |
| Authorization | Update Role | Event Code / Type | Operation |
| Authorization | Update Role | Result | ResultStatus |
| Authorization | Update Role | Username | UserId |
| Authorization | Update Role | User ID | UserKey |
| Authorization | Update Role | User Type / Role | UserType |
| Authorization | Update Role | Session ID | SessionId |
| Authorization | Update Role | IP Address | ClientIP |
| Authorization | Update Role | Target Role Name | Parameters.Name |
| Authorization | Delete Role | Timestamp | CreationTime |
| Authorization | Delete Role | Event ID | Id |
| Authorization | Delete Role | Event Code / Type | Operation |
| Authorization | Delete Role | Result | ResultStatus |
| Authorization | Delete Role | Username | UserId |
| Authorization | Delete Role | User ID | UserKey |
| Authorization | Delete Role | User Type / Role | UserType |
| Authorization | Delete Role | Session ID | SessionId |
| Authorization | Delete Role | IP Address | ClientIP |
| Authorization | Add Permission | Timestamp | CreationTime |
| Authorization | Add Permission | Event ID | Id |
| Authorization | Add Permission | Event Code / Type | Operation |
| Authorization | Add Permission | Result | ResultStatus |
| Authorization | Add Permission | Username | UserId |
| Authorization | Add Permission | User ID | UserKey |
| Authorization | Add Permission | User Type / Role | UserType |
| Authorization | Add Permission | Session ID | SessionId |
| Authorization | Add Permission | IP Address | ClientIP |
| Authorization | Remove Permission | Timestamp | CreationTime |
| Authorization | Remove Permission | Event ID | Id |
| Authorization | Remove Permission | Event Code / Type | Operation |
| Authorization | Remove Permission | Result | ResultStatus |
| Authorization | Remove Permission | Username | UserId |
| Authorization | Remove Permission | User ID | UserKey |
| Authorization | Remove Permission | User Type / Role | UserType |
| Authorization | Remove Permission | Session ID | SessionId |
| Authorization | Remove Permission | IP Address | ClientIP |
| Authorization | Remove Permission | Permission Name | ObjectId |
| System Audit | Create Security Configuration | Timestamp | CreationTime |
| System Audit | Create Security Configuration | Event ID | Id |
| System Audit | Create Security Configuration | Event Code / Type | Operation |
| System Audit | Create Security Configuration | Result | ResultStatus |
| System Audit | Create Security Configuration | Username | UserId |
| System Audit | Create Security Configuration | User ID | UserKey |
| System Audit | Create Security Configuration | User Type / Role | UserType |
| System Audit | Create Security Configuration | Session ID | SessionId |
| System Audit | Create Security Configuration | IP Address | ClientIP |
| System Audit | Create Security Configuration | Configuration / Setting Name | Parameters.Name |
| System Audit | Create Security Configuration | Configuration / Setting Value | Parameters.Value |
| System Audit | Update Security Configuration | Timestamp | CreationTime |
| System Audit | Update Security Configuration | Event ID | Id |
| System Audit | Update Security Configuration | Event Code / Type | Operation |
| System Audit | Update Security Configuration | Result | ResultStatus |
| System Audit | Update Security Configuration | Username | UserId |
| System Audit | Update Security Configuration | User ID | UserKey |
| System Audit | Update Security Configuration | User Type / Role | UserType |
| System Audit | Update Security Configuration | Session ID | SessionId |
| System Audit | Update Security Configuration | IP Address | ClientIP |
| System Audit | Update Security Configuration | Configuration / Setting Name | Parameters.Name |
| System Audit | Update Security Configuration | Configuration / Setting Value | Parameters.Value |
| System Audit | Delete Security Configuration | Timestamp | CreationTime |
| System Audit | Delete Security Configuration | Event ID | Id |
| System Audit | Delete Security Configuration | Event Code / Type | Operation |
| System Audit | Delete Security Configuration | Result | ResultStatus |
| System Audit | Delete Security Configuration | Username | UserId |
| System Audit | Delete Security Configuration | User ID | UserKey |
| System Audit | Delete Security Configuration | User Type / Role | UserType |
| System Audit | Delete Security Configuration | Session ID | SessionId |
| System Audit | Delete Security Configuration | IP Address | ClientIP |
| System Audit | Delete Security Configuration | Configuration / Setting Name | Parameters.Name |
| System Audit | Create Integration | Timestamp | CreationTime |
| System Audit | Create Integration | Event ID | Id |
| System Audit | Create Integration | Event Code / Type | Operation |
| System Audit | Create Integration | Result | ResultStatus |
| System Audit | Create Integration | Username | UserId |
| System Audit | Create Integration | User ID | UserKey |
| System Audit | Create Integration | User Type / Role | UserType |
| System Audit | Create Integration | Session ID | SessionId |
| System Audit | Create Integration | IP Address | ClientIP |
| System Audit | Create Integration | Integration / App Name | AppId |
| System Audit | Update Integration | Timestamp | CreationTime |
| System Audit | Update Integration | Event ID | Id |
| System Audit | Update Integration | Event Code / Type | Operation |
| System Audit | Update Integration | Result | ResultStatus |
| System Audit | Update Integration | Username | UserId |
| System Audit | Update Integration | User ID | UserKey |
| System Audit | Update Integration | User Type / Role | UserType |
| System Audit | Update Integration | Session ID | SessionId |
| System Audit | Update Integration | IP Address | ClientIP |
| System Audit | Update Integration | Integration / App Name | AppId |
| System Audit | Delete Integration | Timestamp | CreationTime |
| System Audit | Delete Integration | Event ID | Id |
| System Audit | Delete Integration | Event Code / Type | Operation |
| System Audit | Delete Integration | Result | ResultStatus |
| System Audit | Delete Integration | Username | UserId |
| System Audit | Delete Integration | User ID | UserKey |
| System Audit | Delete Integration | User Type / Role | UserType |
| System Audit | Delete Integration | Session ID | SessionId |
| System Audit | Delete Integration | IP Address | ClientIP |
| System Audit | Delete Integration | Integration / App Name | AppId |
| Activity Audit | Create Resource | Timestamp | CreationTime |
| Activity Audit | Create Resource | Event ID | Id |
| Activity Audit | Create Resource | Event Code / Type | Operation |
| Activity Audit | Create Resource | Result | ResultStatus |
| Activity Audit | Create Resource | Username | UserId |
| Activity Audit | Create Resource | User ID | UserKey |
| Activity Audit | Create Resource | User Type / Role | UserType |
| Activity Audit | Create Resource | Session ID | SessionId |
| Activity Audit | Create Resource | IP Address | ClientIP |
| Activity Audit | Create Resource | Resource Name | Item |
| Activity Audit | Create Resource | Resource Type | Item.Subject |
| Activity Audit | Read Resource | Timestamp | CreationTime |
| Activity Audit | Read Resource | Event ID | Id |
| Activity Audit | Read Resource | Event Code / Type | Operation |
| Activity Audit | Read Resource | Result | ResultStatus |
| Activity Audit | Read Resource | Username | UserId |
| Activity Audit | Read Resource | User ID | UserKey |
| Activity Audit | Read Resource | User Type / Role | UserType |
| Activity Audit | Read Resource | Session ID | SessionId |
| Activity Audit | Read Resource | IP Address | ClientIPAddress |
| Activity Audit | Read Resource | Resource Name | OperationProperties |
| Activity Audit | Read Resource | Resource Type | Operation |
| Activity Audit | Update Resource | Timestamp | CreationTime |
| Activity Audit | Update Resource | Event ID | Id |
| Activity Audit | Update Resource | Event Code / Type | Operation |
| Activity Audit | Update Resource | Result | ResultStatus |
| Activity Audit | Update Resource | Username | UserId |
| Activity Audit | Update Resource | User ID | UserKey |
| Activity Audit | Update Resource | User Type / Role | UserType |
| Activity Audit | Update Resource | Session ID | SessionId |
| Activity Audit | Update Resource | IP Address | ClientIP |
| Activity Audit | Delete Resource | Timestamp | CreationTime |
| Activity Audit | Delete Resource | Event ID | Id |
| Activity Audit | Delete Resource | Event Code / Type | Operation |
| Activity Audit | Delete Resource | Result | ResultStatus |
| Activity Audit | Delete Resource | Username | UserId |
| Activity Audit | Delete Resource | User ID | UserKey |
| Activity Audit | Delete Resource | User Type / Role | UserType |
| Activity Audit | Delete Resource | Session ID | SessionId |
| Activity Audit | Delete Resource | IP Address | ClientIP |
| Activity Audit | Delete Resource | Resource Name | AffectedItems |
| Activity Audit | Delete Resource | Resource Type | AffectedItems |
| Activity Audit | Query Resource | Timestamp | CreationTime |
| Activity Audit | Query Resource | Event ID | Id |
| Activity Audit | Query Resource | Event Code / Type | Operation |
| Activity Audit | Query Resource | Username | UserId |
| Activity Audit | Query Resource | User ID | UserKey |
| Activity Audit | Query Resource | User Type / Role | UserType |
| Activity Audit | Query Resource | IP Address | ClientIP |
| Activity Audit | Query Resource | Resource Name | QuerySource |
| Activity Audit | Query Resource | Query String | QueryText |

## Example logs

| Category | Event type | Log | Sample field values |
| -------- | ---------- | --- | ------------------- |
| Authentication | Account Login | [success](/products/microsoft_365/event_examples/exchange/authentication_account_login.json) | Timestamp=2024-04-30T01:50:30; Event ID=15146ca7-c8b4-4661-1189-08dc68b7ea96; Event Code / Type=MailboxLogin; Username=test4@test.onmicrosoft.com; User ID=S-1-5-21-1587198437-855871042-1312952668-23578732 |
| Authorization | Create Group | [success](/products/microsoft_365/event_examples/exchange/authorization_create_group_distro.json) | Timestamp=2024-05-01T16:25:27; Event ID=60ee7c61-f9d1-49eb-1743-08dc69fb4fdc; Event Code / Type=New-DistributionGroup; Result=True; Username=example@test.onmicrosoft.com |
| Authorization | Update Group | [success](/products/microsoft_365/event_examples/exchange/authorization_update_group_distro.json) | Timestamp=2024-05-01T16:26:29; Event ID=baba650a-2d56-4b03-586a-08dc69fb74e4; Event Code / Type=Set-DistributionGroup; Result=True; Username=example@test.onmicrosoft.com |
| Authorization | Delete Group | [success](/products/microsoft_365/event_examples/exchange/authorization_delete_group_distro.json) | Timestamp=2024-05-01T16:26:51; Event ID=165ebb45-ec0e-40a2-0a76-08dc69fb81d7; Event Code / Type=Remove-DistributionGroup; Result=True; Username=example@test.onmicrosoft.com |
| Authorization | Add To Group | [success](/products/microsoft_365/event_examples/exchange/authorization_add_to_group_distro.json) | Timestamp=2024-05-01T16:26:08; Event ID=33c59316-c708-4a04-7a24-08dc69fb680a; Event Code / Type=Add-DistributionGroupMember; Result=True; Username=example@test.onmicrosoft.com |
| Authorization | Remove From Group | [success](/products/microsoft_365/event_examples/exchange/authorization_remove_from_group_distro.json) | Timestamp=2024-05-01T16:41:15; Event ID=5c59f5eb-e4fb-49aa-8a57-08dc69fd84ef; Event Code / Type=Remove-DistributionGroupMember; Result=True; Username=example@test.onmicrosoft.com |
| Authorization | Create Role | [success](/products/microsoft_365/event_examples/exchange/authorization_create_role.json) | Timestamp=2024-05-01T04:00:43; Event ID=f09281ab-848e-4de0-6356-08dc69934603; Event Code / Type=New-RoleGroup; Result=True; Username=example@test.onmicrosoft.com |
| Authorization | Update Role | [success](/products/microsoft_365/event_examples/exchange/authorization_update_role.json) | Timestamp=2024-05-01T04:22:00; Event ID=557d12c8-6bd9-4ad4-3b52-08dc69963f27; Event Code / Type=Set-RoleGroup; Result=True; Username=example@test.onmicrosoft.com |
| Authorization | Delete Role | [success](/products/microsoft_365/event_examples/exchange/authorization_delete_role.json) | Timestamp=2024-05-01T04:07:35; Event ID=e7305c7e-6db5-410e-e973-08dc69943bab; Event Code / Type=Remove-RoleGroup; Result=True; Username=example@test.onmicrosoft.com |
| Authorization | Add Permission | [success](/products/microsoft_365/event_examples/exchange/authorization_add_permission.json) | Timestamp=2024-05-01T04:06:31; Event ID=3f044723-212c-4b70-966f-08dc6994156a; Event Code / Type=New-ManagementRoleAssignment; Result=True; Username=example@test.onmicrosoft.com |
| Authorization | Remove Permission | [success](/products/microsoft_365/event_examples/exchange/authorization_remove_permission.json) | Timestamp=2024-05-01T04:06:22; Event ID=159c17b5-7735-4d7f-d5a5-08dc69941015; Event Code / Type=Remove-ManagementRoleAssignment; Result=True; Username=example@test.onmicrosoft.com |
| System Audit | Create Security Configuration | [success](/products/microsoft_365/event_examples/exchange/system_audit_create_security_configuration_spam.json) | Timestamp=2024-05-01T04:47:03; Event ID=02a67a6e-bddc-4a8b-bd8a-08dc6999bf35; Event Code / Type=New-HostedContentFilterPolicy; Result=True; Username=example@test.onmicrosoft.com |
| System Audit | Update Security Configuration | [success](/products/microsoft_365/event_examples/exchange/system_audit_update_security_configuration_spam.json) | Timestamp=2024-05-01T04:47:36; Event ID=c3d67096-6e45-4642-6454-08dc6999d2cd; Event Code / Type=Set-HostedContentFilterPolicy; Result=True; Username=example@test.onmicrosoft.com |
| System Audit | Delete Security Configuration | [success](/products/microsoft_365/event_examples/exchange/system_audit_delete_security_configuration_spam.json) | Timestamp=2024-05-01T04:48:06; Event ID=646780a6-8b79-4310-9f6e-08dc6999e476; Event Code / Type=Remove-HostedContentFilterPolicy; Result=True; Username=example@test.onmicrosoft.com |
| System Audit | Create Integration | [success](/products/microsoft_365/event_examples/exchange/system_audit_create_integration.json) | Timestamp=2024-05-01T01:11:16; Event ID=323fd199-99bb-4bd5-5ca7-08dc697b9a0c; Event Code / Type=New-App; Result=True; Username=NT AUTHORITY\SYSTEM (Microsoft.Exchange.AdminApi.NetCore) |
| System Audit | Update Integration | [success](/products/microsoft_365/event_examples/exchange/system_audit_update_integration.json) | Timestamp=2024-04-30T15:48:21; Event ID=ba11eba1-fd2a-4091-9356-08dc692cf680; Event Code / Type=Enable-App; Result=True; Username=example@test.onmicrosoft.com |
| System Audit | Delete Integration | [success](/products/microsoft_365/event_examples/exchange/system_audit_delete_integration.json) | Timestamp=2024-04-30T15:49:40; Event ID=86328dc9-8a8d-4612-2156-08dc692d25cb; Event Code / Type=Remove-App; Result=True; Username=example@test.onmicrosoft.com |
| Activity Audit | Create Resource | [success - email](/products/microsoft_365/event_examples/exchange/activity_audit_create_resource_msg.json) | Timestamp=2024-04-30T01:50:44; Event ID=b879cd77-f6df-4dd0-526a-08dc68b7f338; Event Code / Type=Send; Result=Succeeded; Username=test4@test.onmicrosoft.com |
| Activity Audit | Create Resource | [success - calendar](/products/microsoft_365/event_examples/exchange/activity_audit_create_resource_calendar.json) | Timestamp=2024-05-01T19:00:24; Event ID=64922ffb-a517-43af-a0ea-737e0b67c577; Event Code / Type=Create; Result=Succeeded; Username=example@test.onmicrosoft.com |
| Activity Audit | Read Resource | [success](/products/microsoft_365/event_examples/exchange/activity_audit_read_resource.json) | Timestamp=2024-05-01T17:24:12; Event ID=121899a5-ff77-49a0-b344-e368a192ca4e; Event Code / Type=MailItemsAccessed; Result=Succeeded; Username=example@test.onmicrosoft.com |
| Activity Audit | Update Resource | [success](/products/microsoft_365/event_examples/exchange/activity_audit_update_resource_calendar.json) | Timestamp=2024-05-01T19:00:32; Event ID=0b41bd99-5ab2-4d17-359c-08dc6a10f9ac; Event Code / Type=Update; Result=Succeeded; Username=example@test.onmicrosoft.com |
| Activity Audit | Delete Resource | [success - email](/products/microsoft_365/event_examples/exchange/activity_audit_delete_resource_msg.json) | Timestamp=2024-05-01T17:24:22; Event ID=400c8963-12c3-417e-3e2c-08dc6a038ac8; Event Code / Type=MoveToDeletedItems; Result=Succeeded; Username=example@test.onmicrosoft.com |
| Activity Audit | Delete Resource | [success - calendar](/products/microsoft_365/event_examples/exchange/activity_audit_delete_resource_calendar.json) | Timestamp=2024-05-01T19:21:16; Event ID=e1fb94cb-2adc-4b4c-98bd-08dc6a13df45; Event Code / Type=MoveToDeletedItems; Result=Succeeded; Username=example@test.onmicrosoft.com |
| Activity Audit | Query Resource | [success](/products/microsoft_365/event_examples/exchange/activity_audit_query_resource.json) | Timestamp=2025-02-01T10:01:03; Event ID=67eeaaae-3c3c-4fcf-a18e-351546330c8e; Event Code / Type=SearchQueryInitiatedExchange; Username=test@test.onmicrosoft.com; User ID=100320015ED2DA21 |


