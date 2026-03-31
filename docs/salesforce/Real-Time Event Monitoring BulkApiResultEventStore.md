# Salesforce — Real-Time Event Monitoring BulkApiResultEventStore

📌 **v1.0.0** · 🗄 **Retention:** 6 Months · ⚡ **Latency:** Real-Time

🗄 N/A


⚡ N/A


📜 **Licensing:** Requires Salesforce Shield or a Salesforce Event Monitoring add-on subscription.


Tracks when a user downloads the results of a Bulk API request.
## References
* [BulkApiResultEventStore](https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/sforce_api_objects_bulkapiresulteventstore.htm)
## Field mappings

| Category | Event type | Attribute | Source field(s) |
| -------- | ---------- | --------- | ---------------- |
| Activity Audit | Create Resource | Timestamp | EventDate |
| Activity Audit | Create Resource | Event ID | EventIdentifier |
| Activity Audit | Create Resource | Event Code / Type | data.payload.attributes.type |
| Activity Audit | Create Resource | Result | PolicyOutcome |
| Activity Audit | Create Resource | Username | Username |
| Activity Audit | Create Resource | User ID | UserId |
| Activity Audit | Create Resource | Session ID | SessionKey |
| Activity Audit | Create Resource | IP Address | SourceIp |
| Activity Audit | Create Resource | Resource Name | Query |

## Example logs

| Category | Event type | Log | Sample field values |
| -------- | ---------- | --- | ------------------- |
| Activity Audit | Create Resource | [download](/products/salesforce/event_examples/salesforce_rtem_bulkapiresulteventstore/activity_audit_download_resource_bulkapiresulteventstore.json) | Timestamp=2023-03-22T15:07:16.240+0000; Event ID=abcdefgh-1234-0000-0000-000000000001; Event Code / Type=BulkApiResultEventStore; Result=None; Username=john@example.com |


