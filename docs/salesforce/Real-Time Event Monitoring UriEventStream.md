# Salesforce — Real-Time Event Monitoring UriEventStream

📌 **v1.0.0** · 🗄 **Retention:** 6 Months · ⚡ **Latency:** Real-Time

📜 **Licensing:** Requires Salesforce Shield or a Salesforce Event Monitoring add-on subscription.

Detects when a user creates, accesses, updates, or deletes a record in Salesforce Classic only.
## References
* [UriEventStream](https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/sforce_api_objects_urieventstream.htm)
## Field mappings

| Category | Event type | Attribute | Source field(s) |
| -------- | ---------- | --------- | ---------------- |
| Activity Audit | Create Resource | Timestamp | EventDate |
| Activity Audit | Create Resource | Event ID | EventIdentifier |
| Activity Audit | Create Resource | Event Code / Type | Operation |
| Activity Audit | Create Resource | Result | OperationStatus |
| Activity Audit | Create Resource | Username | Username |
| Activity Audit | Create Resource | User ID | UserId |
| Activity Audit | Create Resource | User Type / Role | UserType |
| Activity Audit | Create Resource | Session ID | SessionKey |
| Activity Audit | Create Resource | IP Address | SourceIp |
| Activity Audit | Create Resource | Resource Name | Name |
| Activity Audit | Create Resource | Resource Type | QueriedEntities |
| Activity Audit | Read Resource | Timestamp | EventDate |
| Activity Audit | Read Resource | Event ID | EventIdentifier |
| Activity Audit | Read Resource | Event Code / Type | Operation |
| Activity Audit | Read Resource | Result | OperationStatus |
| Activity Audit | Read Resource | Username | Username |
| Activity Audit | Read Resource | User ID | UserId |
| Activity Audit | Read Resource | User Type / Role | UserType |
| Activity Audit | Read Resource | Session ID | SessionKey |
| Activity Audit | Read Resource | IP Address | SourceIp |
| Activity Audit | Read Resource | Resource Name | Name |
| Activity Audit | Read Resource | Resource Type | QueriedEntities |
| Activity Audit | Update Resource | Timestamp | EventDate |
| Activity Audit | Update Resource | Event ID | EventIdentifier |
| Activity Audit | Update Resource | Event Code / Type | Operation |
| Activity Audit | Update Resource | Result | OperationStatus |
| Activity Audit | Update Resource | Username | Username |
| Activity Audit | Update Resource | User ID | UserId |
| Activity Audit | Update Resource | User Type / Role | UserType |
| Activity Audit | Update Resource | Session ID | SessionKey |
| Activity Audit | Update Resource | IP Address | SourceIp |
| Activity Audit | Update Resource | Resource Name | Name |
| Activity Audit | Update Resource | Resource Type | QueriedEntities |
| Activity Audit | Delete Resource | Timestamp | EventDate |
| Activity Audit | Delete Resource | Event ID | EventIdentifier |
| Activity Audit | Delete Resource | Event Code / Type | Operation |
| Activity Audit | Delete Resource | Result | OperationStatus |
| Activity Audit | Delete Resource | Username | Username |
| Activity Audit | Delete Resource | User ID | UserId |
| Activity Audit | Delete Resource | User Type / Role | UserType |
| Activity Audit | Delete Resource | Session ID | SessionKey |
| Activity Audit | Delete Resource | IP Address | SourceIp |
| Activity Audit | Delete Resource | Resource Name | Name |
| Activity Audit | Delete Resource | Resource Type | QueriedEntities |

## Example logs

| Category | Event type | Log | Sample field values |
| -------- | ---------- | --- | ------------------- |
| Activity Audit | Create Resource | [create](/products/salesforce/event_examples/salesforce_rtem_urieventstream/activity_audit_create_resource_urieventstream.json) | Timestamp=2023-03-21T22:17:55.090+0000; Event ID=abcdefgh-1234-0000-0000-000000000001; Event Code / Type=Create; Result=Success; Username=john@example.com |
| Activity Audit | Read Resource | [read](/products/salesforce/event_examples/salesforce_rtem_urieventstream/activity_audit_read_resource_urieventstream.json) | Timestamp=2023-03-21T21:59:44.159+0000; Event ID=abcdefgh-1234-0000-0000-000000000001; Event Code / Type=Read; Result=Success; Username=john@example.com |
| Activity Audit | Update Resource | [update](/products/salesforce/event_examples/salesforce_rtem_urieventstream/activity_audit_update_resource_urieventstream.json) | Timestamp=2023-03-21T22:51:43.042+0000; Event ID=abcdefgh-1234-0000-0000-000000000001; Event Code / Type=Update; Result=Initiated; Username=john@example.com |
| Activity Audit | Delete Resource | [delete](/products/salesforce/event_examples/salesforce_rtem_urieventstream/activity_audit_delete_resource_urieventstream.json) | Timestamp=2023-03-21T16:48:57.548+0000; Event ID=abcdefgh-1234-0000-0000-000000000001; Event Code / Type=Delete; Result=Initiated; Username=john@example.com |


