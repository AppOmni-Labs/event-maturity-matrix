# Salesforce — Real-Time Event Monitoring ApiEventStream

📌 **v1.0.0** · 🗄 **Retention:** 6 Months · ⚡ **Latency:** Real-Time

📜 **Licensing:** Requires Salesforce Shield or a Salesforce Event Monitoring add-on subscription.

Tracks the user-initiated read-only API calls "query()", "queryMore()", and "count()".

Captures API requests through SOAP API and Bulk API.

## References
* [ApiEventStream](https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/sforce_api_objects_apieventstream.htm)
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
| Activity Audit | Read Resource | User Agent Name | UserAgent |
| Activity Audit | Read Resource | Device/Client Type | Platform |
| Activity Audit | Read Resource | Resource Name | Query |
| Activity Audit | Read Resource | Resource Type | ApiType |
| Activity Audit | Download Resource | Timestamp | EventDate |
| Activity Audit | Download Resource | Event ID | EventIdentifier |
| Activity Audit | Download Resource | Event Code / Type | Operation |
| Activity Audit | Download Resource | Result | PolicyOutcome |
| Activity Audit | Download Resource | Username | Username |
| Activity Audit | Download Resource | User ID | UserId |
| Activity Audit | Download Resource | Session ID | SessionKey |
| Activity Audit | Download Resource | IP Address | SourceIp |
| Activity Audit | Download Resource | User Agent Name | UserAgent |
| Activity Audit | Download Resource | Device/Client Type | Platform |
| Activity Audit | Download Resource | Resource Name | Query |
| Activity Audit | Download Resource | Resource Type | ApiType |
| Activity Audit | Download Resource | Resource Metadata | RowsProcessed |

## Example logs

| Category | Event type | Log | Sample field values |
| -------- | ---------- | --- | ------------------- |
| Activity Audit | Read Resource | [read](/products/salesforce/event_examples/salesforce_rtem_apieventstream/activity_audit_read_resource_apieventstream.json) | Timestamp=2023-03-21T19:42:13.264+0000; Event ID=abcdefgh-1234-0000-0000-000000000001; Event Code / Type=Query; Result=None; Username=john@example.com |
| Activity Audit | Download Resource | [download](/products/salesforce/event_examples/salesforce_rtem_apieventstream/activity_audit_download_resource_apieventstream.json) | Timestamp=2023-03-21T10:04:39.747+0000; Event ID=abcdefgh-1234-0000-0000-000000000001; Event Code / Type=QueryMore; Result=None; Username=john@example.com |


