# Microsoft 365 — Sharepoint Audit Logs

📌 **v1.0.0** · 🗄 **Retention:** 180 days · ⚡ **Latency:** Typically 60 to 90 minutes after an event occurs.

🗄 Minimum retention is 180 days, but organizations can set a retention policy up to 10 years dependent on licensing, reference https://learn.microsoft.com/en-us/purview/audit-log-retention-policies


⚡ Microsoft does not provide a specific audit logging latency SLA, reference https://learn.microsoft.com/en-us/purview/audit-search?view=o365-worldwide&tabs=microsoft-purview-portal


📜 **Licensing:** Standard and Premium audit licenses are available, with log availability and retention dependent on the license level. For more information, see https://learn.microsoft.com/en-us/purview/audit-search?view=o365-worldwide&tabs=microsoft-purview-portal


Includes logs for Sharepoint and OneDrive.
## References
* [SharePoint Base Schema](https://learn.microsoft.com/en-us/office/office-365-management-api/office-365-management-activity-api-schema#sharepoint-base-schema)
## Field mappings

| Category | Event type | Attribute | Source field(s) |
| -------- | ---------- | --------- | ---------------- |
| Authentication | Account Login | Timestamp | CreationTime |
| Authentication | Account Login | Event ID | Id |
| Authentication | Account Login | Event Code / Type | Operation |
| Authentication | Account Login | Username | UserId |
| Authentication | Account Login | Session ID | AppAccessContext.AADSessionId |
| Authentication | Account Login | IP Address | ClientIP |
| Authentication | Account Login | User Agent Name | UserAgent |
| Authentication | Account Login | Device/Client Type | Platform |
| Authorization | Add To Group | Timestamp | CreationTime |
| Authorization | Add To Group | Event ID | Id |
| Authorization | Add To Group | Event Code / Type | Operation |
| Authorization | Add To Group | Username | UserId |
| Authorization | Add To Group | Session ID | AppAccessContext.AADSessionId |
| Authorization | Add To Group | IP Address | ClientIP |
| Authorization | Add To Group | User Agent Name | UserAgent |
| Authorization | Add To Group | Device/Client Type | Platform |
| Authorization | Add To Group | Target Username | TargetUserOrGroupName |
| Authorization | Add To Group | Target Group Name | EventData |
| Authorization | Remove From Group | Timestamp | CreationTime |
| Authorization | Remove From Group | Event ID | Id |
| Authorization | Remove From Group | Event Code / Type | Operation |
| Authorization | Remove From Group | Username | UserId |
| Authorization | Remove From Group | Session ID | AppAccessContext.AADSessionId |
| Authorization | Remove From Group | IP Address | ClientIP |
| Authorization | Remove From Group | User Agent Name | UserAgent |
| Authorization | Remove From Group | Device/Client Type | Platform |
| Authorization | Remove From Group | Target Username | TargetUserOrGroupName |
| Authorization | Remove From Group | Target Group Name | EventData |
| Authorization | Add Permission | Timestamp | CreationTime |
| Authorization | Add Permission | Event ID | Id |
| Authorization | Add Permission | Event Code / Type | Operation |
| Authorization | Add Permission | Username | UserId |
| Authorization | Add Permission | Session ID | AppAccessContext.AADSessionId |
| Authorization | Add Permission | IP Address | ClientIP |
| Authorization | Add Permission | User Agent Name | UserAgent |
| Authorization | Add Permission | Device/Client Type | Platform |
| Authorization | Add Permission | Permission Name | TargetUserOrGroupType |
| Authorization | Add Permission | Target Resource Name | TargetUserOrGroupName |
| Authorization | Remove Permission | Timestamp | CreationTime |
| Authorization | Remove Permission | Event ID | Id |
| Authorization | Remove Permission | Event Code / Type | Operation |
| Authorization | Remove Permission | Username | UserId |
| Authorization | Remove Permission | Session ID | AppAccessContext.AADSessionId |
| Authorization | Remove Permission | IP Address | ClientIP |
| Authorization | Remove Permission | User Agent Name | UserAgent |
| Authorization | Remove Permission | Device/Client Type | Platform |
| Authorization | Remove Permission | Permission Name | TargetUserOrGroupType |
| Authorization | Remove Permission | Target Resource Name | TargetUserOrGroupName |
| System Audit | Update Security Configuration | Timestamp | CreationTime |
| System Audit | Update Security Configuration | Event ID | Id |
| System Audit | Update Security Configuration | Event Code / Type | Operation |
| System Audit | Update Security Configuration | Username | UserId |
| System Audit | Update Security Configuration | IP Address | ClientIP |
| System Audit | Update Security Configuration | User Agent Name | UserAgent |
| System Audit | Update Security Configuration | Configuration / Setting Name | ModifiedProperties |
| System Audit | Update Security Configuration | Configuration / Setting Value | ModifiedProperties |
| System Audit | Update Security Configuration | Previous Configuration / Setting Value | ModifiedProperties |
| Activity Audit | Create Resource | Timestamp | CreationTime |
| Activity Audit | Create Resource | Event ID | Id |
| Activity Audit | Create Resource | Event Code / Type | Operation |
| Activity Audit | Create Resource | Username | UserId |
| Activity Audit | Create Resource | Session ID | AppAccessContext.AADSessionId |
| Activity Audit | Create Resource | IP Address | ClientIP |
| Activity Audit | Create Resource | User Agent Name | UserAgent |
| Activity Audit | Create Resource | Device/Client Type | Platform |
| Activity Audit | Create Resource | Resource Name | EventData |
| Activity Audit | Create Resource | Resource Type | ItemType |
| Activity Audit | Read Resource | Timestamp | CreationTime |
| Activity Audit | Read Resource | Event ID | Id |
| Activity Audit | Read Resource | Event Code / Type | Operation |
| Activity Audit | Read Resource | Username | UserId |
| Activity Audit | Read Resource | Session ID | AppAccessContext.AADSessionId |
| Activity Audit | Read Resource | IP Address | ClientIP |
| Activity Audit | Read Resource | User Agent Name | UserAgent |
| Activity Audit | Read Resource | Device/Client Type | Platform |
| Activity Audit | Read Resource | Resource Name | ObjectId |
| Activity Audit | Read Resource | Resource Type | ItemType |
| Activity Audit | Delete Resource | Timestamp | CreationTime |
| Activity Audit | Delete Resource | Event ID | Id |
| Activity Audit | Delete Resource | Event Code / Type | Operation |
| Activity Audit | Delete Resource | Username | UserId |
| Activity Audit | Delete Resource | IP Address | ClientIP |
| Activity Audit | Delete Resource | User Agent Name | UserAgent |
| Activity Audit | Delete Resource | Resource Name | ObjectId |
| Activity Audit | Delete Resource | Resource Type | ItemType |
| Activity Audit | Download Resource | Timestamp | CreationTime |
| Activity Audit | Download Resource | Event ID | Id |
| Activity Audit | Download Resource | Event Code / Type | Operation |
| Activity Audit | Download Resource | Username | UserId |
| Activity Audit | Download Resource | Session ID | AppAccessContext.AADSessionId |
| Activity Audit | Download Resource | IP Address | ClientIP |
| Activity Audit | Download Resource | User Agent Name | UserAgent |
| Activity Audit | Download Resource | Device/Client Type | Platform |
| Activity Audit | Download Resource | Resource Name | ItemType |
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
| Authentication | Account Login | [success](/products/microsoft_365/event_examples/sharepoint/authentication_account_login.json) | Timestamp=2024-05-02T20:13:40; Event ID=a35c38f6-ed9d-4ddc-bbfd-08dc6ae45bd7; Event Code / Type=SignInEvent; Username=example@test.onmicrosoft.com; Session ID=c21adbd5-e8d4-44fe-a2a2-43e3251b04b5 |
| Authorization | Add To Group | [success](/products/microsoft_365/event_examples/sharepoint/authorization_add_member_to_group.json) | Timestamp=2024-05-02T20:35:41; Event ID=a18dd05a-4a13-4800-d1f6-08dc6ae76eef; Event Code / Type=AddedToGroup; Username=example@test.onmicrosoft.com; Session ID=c21adbd5-e8d4-44fe-a2a2-43e3251b04b5 |
| Authorization | Remove From Group | [success](/products/microsoft_365/event_examples/sharepoint/authorization_remove_member_from_group.json) | Timestamp=2024-05-02T20:35:46; Event ID=5eda0f9d-927f-4343-5669-08dc6ae77256; Event Code / Type=RemovedFromGroup; Username=example@test.onmicrosoft.com; Session ID=c21adbd5-e8d4-44fe-a2a2-43e3251b04b5 |
| Authorization | Add Permission | [success](/products/microsoft_365/event_examples/sharepoint/authorization_add_permission.json) | Timestamp=2024-05-02T20:38:27; Event ID=8b9a2076-6a67-4c8f-771f-08dc6ae7d259; Event Code / Type=SiteCollectionAdminAdded; Username=example@test.onmicrosoft.com; Session ID=c21adbd5-e8d4-44fe-a2a2-43e3251b04b5 |
| Authorization | Remove Permission | [success](/products/microsoft_365/event_examples/sharepoint/authorization_remove_permission.json) | Timestamp=2024-05-02T20:38:27; Event ID=f8c5fd57-94c1-423b-64b2-08dc6ae7d265; Event Code / Type=SiteCollectionAdminRemoved; Username=example@test.onmicrosoft.com; Session ID=c21adbd5-e8d4-44fe-a2a2-43e3251b04b5 |
| System Audit | Update Security Configuration | [success](/products/microsoft_365/event_examples/sharepoint/system_audit_update_security_configuration.json) | Timestamp=2024-05-01T06:41:58; Event ID=bebaecd3-a9c7-4cd9-211d-08dc69a9ccab; Event Code / Type=SiteIBModeChanged; Username=SHAREPOINT\system; IP Address= |
| Activity Audit | Create Resource | [success](/products/microsoft_365/event_examples/sharepoint/activity_audit_create_resource_site.json) | Timestamp=2024-05-02T20:38:33; Event ID=786cf23e-013b-4fab-105e-08dc6ae7d5e1; Event Code / Type=SiteCollectionCreated; Username=example@test.onmicrosoft.com; Session ID=c21adbd5-e8d4-44fe-a2a2-43e3251b04b5 |
| Activity Audit | Read Resource | [success](/products/microsoft_365/event_examples/sharepoint/activity_audit_read_resource_page.json) | Timestamp=2024-05-02T22:01:37; Event ID=4af4f3a2-6584-48b4-e96d-08dc6af37076; Event Code / Type=PageViewed; Username=example@test.onmicrosoft.com; Session ID=c21adbd5-e8d4-44fe-a2a2-43e3251b04b5 |
| Activity Audit | Delete Resource | [success](/products/microsoft_365/event_examples/sharepoint/activity_audit_delete_resource_site.json) | Timestamp=2024-05-02T20:13:54; Event ID=c3176f6b-847e-4615-3da2-08dc6ae46456; Event Code / Type=SiteDeleted; Username=John Doe; IP Address=198.51.100.1 |
| Activity Audit | Download Resource | [success](/products/microsoft_365/event_examples/sharepoint/activity_audit_download_resource_file.json) | Timestamp=2024-05-02T20:07:27; Event ID=24052721-2860-4804-fe81-08dc6ae37d61; Event Code / Type=FileDownloaded; Username=example@test.onmicrosoft.com; Session ID=c21adbd5-e8d4-44fe-a2a2-43e3251b04b5 |
| Activity Audit | Query Resource | [success](/products/microsoft_365/event_examples/sharepoint/activity_audit_query_resource.json) | Timestamp=2025-02-02T11:02:01; Event ID=86265de6-0f51-4028-a903-c679c212842c; Event Code / Type=SearchQueryInitiatedSharePoint; Username=test@test.onmicrosoft.com; User ID=100320015ED2DA21 |


