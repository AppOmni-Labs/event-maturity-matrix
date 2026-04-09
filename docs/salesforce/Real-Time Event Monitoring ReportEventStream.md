





# Salesforce — Real-Time Event Monitoring ReportEventStream

📌 **v1.0.0** · 🗄 **Retention:** 6 Months · ⚡ **Latency:** Real-Time





📜 **Licensing:** Requires Salesforce Shield or a Salesforce Event Monitoring add-on subscription.


Tracks report-related actions, such as when a user runs or exports a report.
## References
* [ReportEventStream](https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/sforce_api_objects_reporteventstream.htm)
## Field mappings

| Category | Event type | Attribute | Source field(s) |
| -------- | ---------- | --------- | ---------------- |
| Activity Audit | Read Resource | Timestamp | EventDate |
| Activity Audit | Read Resource | Event ID | EventIdentifier |
| Activity Audit | Read Resource | Event Code / Type | Operation |
| Activity Audit | Read Resource | Result | PolicyOutcome |
| Activity Audit | Read Resource | Username | Username |
| Activity Audit | Read Resource | User ID | UserId |
| Activity Audit | Read Resource | Session ID | SessionKey |
| Activity Audit | Read Resource | IP Address | SourceIp |
| Activity Audit | Read Resource | Device/Client Type | EventSource |
| Activity Audit | Read Resource | Resource Name | Name |
| Activity Audit | Read Resource | Resource Type | QueriedEntities |
| Activity Audit | Download Resource | Timestamp | EventDate |
| Activity Audit | Download Resource | Event ID | EventIdentifier |
| Activity Audit | Download Resource | Event Code / Type | Operation |
| Activity Audit | Download Resource | Result | PolicyOutcome |
| Activity Audit | Download Resource | Username | Username |
| Activity Audit | Download Resource | User ID | UserId |
| Activity Audit | Download Resource | Session ID | SessionKey |
| Activity Audit | Download Resource | IP Address | SourceIp |
| Activity Audit | Download Resource | Device/Client Type | EventSource |
| Activity Audit | Download Resource | Resource Name | Name |
| Activity Audit | Download Resource | Resource Type | QueriedEntities |
| Activity Audit | Download Resource | Resource Metadata | RowsProcessed |

## Example logs

| Category | Event type | Log | Sample field values |
| -------- | ---------- | --- | ------------------- |
| Activity Audit | Read Resource | [read](/products/salesforce/event_examples/salesforce_rtem_reporteventstream/activity_audit_read_resource_reporteventstream.json) | Timestamp=2023-03-22T11:59:17.340+0000; Event ID=abcdefgh-1234-0000-0000-000000000001; Event Code / Type=ReportRunFromLightning; Result=None; Username=john@example.com |
| Activity Audit | Download Resource | [download](/products/salesforce/event_examples/salesforce_rtem_reporteventstream/activity_audit_download_resource_reporteventstream.json) | Timestamp=2023-03-22T13:18:46.826+0000; Event ID=abcdefgh-1234-0000-0000-000000000001; Event Code / Type=ReportExported; Result=None; Username=john@example.com |


