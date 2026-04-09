# Microsoft 365 — General Audit Logs

📌 **v1.0.0** · 🗄 **Retention:** 180 days · ⚡ **Latency:** Typically 60 to 90 minutes after an event occurs.

🗄 Minimum retention is 180 days, but organizations can set a retention policy up to 10 years dependent on licensing, reference https://learn.microsoft.com/en-us/purview/audit-log-retention-policies⚡ Microsoft does not provide a specific audit logging latency SLA, reference https://learn.microsoft.com/en-us/purview/audit-search?view=o365-worldwide&tabs=microsoft-purview-portal📜 **Licensing:** Standard and Premium audit licenses are available, with log availability and retention dependent on the license level.

For more information, see https://learn.microsoft.com/en-us/purview/audit-search?view=o365-worldwide&tabs=microsoft-purview-portal


Includes workloads not included in other audit log types.
## References
* [Common Audit Schema](https://learn.microsoft.com/en-us/office/office-365-management-api/office-365-management-activity-api-schema#common-schema)
## Field mappings

| Category | Event type | Attribute | Source field(s) |
| -------- | ---------- | --------- | ---------------- |
| Authorization | Create Group | Timestamp | CreationTime |
| Authorization | Create Group | Event ID | Id |
| Authorization | Create Group | Event Code / Type | Operation |
| Authorization | Create Group | User ID | UserKey |
| Authorization | Create Group | User Type / Role | UserId |
| Authorization | Create Group | Target Group Name | TeamName |
| Authorization | Update Group | Timestamp | CreationTime |
| Authorization | Update Group | Event ID | Id |
| Authorization | Update Group | Event Code / Type | Operation |
| Authorization | Update Group | Username | UserId |
| Authorization | Update Group | User ID | UserKey |
| Authorization | Update Group | Target Attribute Context | NewValue |
| Authorization | Update Group | Target Group Name | TeamName |
| Authorization | Delete Group | Timestamp | CreationTime |
| Authorization | Delete Group | Event ID | Id |
| Authorization | Delete Group | Event Code / Type | Operation |
| Authorization | Delete Group | Username | UserId |
| Authorization | Delete Group | User ID | UserKey |
| Authorization | Delete Group | Target Group Name | TeamName |
| Authorization | Add To Group | Timestamp | CreationTime |
| Authorization | Add To Group | Event ID | Id |
| Authorization | Add To Group | Event Code / Type | Operation |
| Authorization | Add To Group | Username | UserId |
| Authorization | Add To Group | User ID | UserKey |
| Authorization | Add To Group | Target Username | Members.DisplayName |
| Authorization | Add To Group | Target Group Name | TeamName |
| Authorization | Remove From Group | Timestamp | CreationTime |
| Authorization | Remove From Group | Event ID | Id |
| Authorization | Remove From Group | Event Code / Type | Operation |
| Authorization | Remove From Group | Username | UserId |
| Authorization | Remove From Group | User ID | UserKey |
| Authorization | Remove From Group | Target Username | Members.DisplayName |
| Authorization | Remove From Group | Target Group Name | TeamName |
| System Audit | Create Integration | Timestamp | CreationTime |
| System Audit | Create Integration | Event ID | Id |
| System Audit | Create Integration | Event Code / Type | Operation |
| System Audit | Create Integration | Username | UserId |
| System Audit | Create Integration | User ID | UserKey |
| System Audit | Create Integration | Integration / App Name | AddOnName |
| System Audit | Delete Integration | Timestamp | CreationTime |
| System Audit | Delete Integration | Event ID | Id |
| System Audit | Delete Integration | Event Code / Type | Operation |
| System Audit | Delete Integration | Username | UserId |
| System Audit | Delete Integration | User ID | UserKey |
| Activity Audit | Create Resource | Timestamp | CreationTime |
| Activity Audit | Create Resource | Event ID | Id |
| Activity Audit | Create Resource | Event Code / Type | Operation |
| Activity Audit | Create Resource | Username | UserId |
| Activity Audit | Create Resource | User ID | UserKey |
| Activity Audit | Create Resource | Resource Type | ExtraProperties |
| Activity Audit | Delete Resource | Timestamp | CreationTime |
| Activity Audit | Delete Resource | Event ID | Id |
| Activity Audit | Delete Resource | Event Code / Type | Operation |
| Activity Audit | Delete Resource | Username | UserId |
| Activity Audit | Delete Resource | User ID | UserKey |
| Activity Audit | Delete Resource | IP Address | ClientIP |

## Example logs

| Category | Event type | Log | Sample field values |
| -------- | ---------- | --- | ------------------- |
| Authorization | Create Group | [success](/products/microsoft_365/event_examples/general/authorization_create_group.json) | Timestamp=2024-05-03T15:34:16; Event ID=64ecdac9-543e-4046-99be-087dd56c2150; Event Code / Type=TeamCreated; User ID=f1c08887-d776-42f8-9911-06faa5ab392f; User Type / Role=example@test.onmicrosoft.com |
| Authorization | Update Group | [success](/products/microsoft_365/event_examples/general/authorization_update_group.json) | Timestamp=2024-05-03T15:50:19; Event ID=2c658d54-4fc9-477f-b98c-48500df799b4; Event Code / Type=TeamSettingChanged; Username=example@test.onmicrosoft.com; User ID=f1c08887-d776-42f8-9911-06faa5ab392f |
| Authorization | Delete Group | [success](/products/microsoft_365/event_examples/general/authorization_delete_group.json) | Timestamp=2024-05-03T15:33:02; Event ID=6718936a-de28-4f7d-9b40-29256adfca43; Event Code / Type=TeamDeleted; Username=Microsoft Teams Sync; User ID=62b732f7-fc71-40bc-b27d-35efcb0509de |
| Authorization | Add To Group | [success](/products/microsoft_365/event_examples/general/authorization_add_member_to_group.json) | Timestamp=2024-05-01T05:10:10; Event ID=d84f2254-5d4b-5274-91ad-6729e781821f; Event Code / Type=MemberAdded; Username=example@test.onmicrosoft.com; User ID=f1c08887-d776-42f8-9911-06faa5ab392f |
| Authorization | Remove From Group | [success](/products/microsoft_365/event_examples/general/authorization_remove_member_from_group.json) | Timestamp=2024-05-03T15:49:22; Event ID=a7c73bdd-0302-533a-bff4-97d64dc681a9; Event Code / Type=MemberRemoved; Username=example@test.onmicrosoft.com; User ID=f1c08887-d776-42f8-9911-06faa5ab392f |
| System Audit | Create Integration | [success](/products/microsoft_365/event_examples/general/system_audit_create_integration.json) | Timestamp=2024-05-02T21:21:45; Event ID=46429b68-d31f-4329-9601-e1d77131f2b2; Event Code / Type=AppInstalled; Username=example@test.onmicrosoft.com; User ID=f1c08887-d776-42f8-9911-06faa5ab392f |
| System Audit | Delete Integration | [success](/products/microsoft_365/event_examples/general/system_audit_delete_integration.json) | Timestamp=2024-05-02T20:14:26; Event ID=1d8ce214-a40b-4d03-b5f1-bc3872fc01f0; Event Code / Type=AppDeleted; Username=Microsoft Teams Sync; User ID=62b732f7-fc71-40bc-b27d-35efcb0509de |
| Activity Audit | Create Resource | [success](/products/microsoft_365/event_examples/general/activity_audit_create_resource.json) | Timestamp=2024-05-02T21:17:51; Event ID=f36fd190-d3c2-47df-a62b-8d31eb7876c5; Event Code / Type=ShiftAdded; Username=example@test.onmicrosoft.com; User ID=f1c08887-d776-42f8-9911-06faa5ab392f |
| Activity Audit | Delete Resource | [success](/products/microsoft_365/event_examples/general/activity_audit_delete_resource.json) | Timestamp=2024-05-02T21:17:24; Event ID=2c506054-42a2-5e31-95b7-4c8c9219dff0; Event Code / Type=MessageDeleted; Username=example@test.onmicrosoft.com; User ID=f1c08887-d776-42f8-9911-06faa5ab392f |


