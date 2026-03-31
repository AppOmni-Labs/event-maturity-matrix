# Salesforce — Real-Time Event Monitoring ListViewEventStream

📌 **v1.0.0** · 🗄 **Retention:** 6 Months · ⚡ **Latency:** Real-Time

🗄 N/A


⚡ N/A


📜 **Licensing:** Requires Salesforce Shield or a Salesforce Event Monitoring add-on subscription.


Tracks actions related to list views in Lightning Experience, Salesforce Classic, or the API. For example, the event captures when a user runs or exports a list view.
## References
* [ListViewEventStream](https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/sforce_api_objects_listvieweventstream.htm)
## Field mappings

| Category | Event type | Attribute | Source field(s) |
| -------- | ---------- | --------- | ---------------- |
| Activity Audit | Read Resource | Timestamp | EventDate |
| Activity Audit | Read Resource | Event ID | EventIdentifier |
| Activity Audit | Read Resource | Event Code / Type | EventSource |
| Activity Audit | Read Resource | Result | PolicyOutcome |
| Activity Audit | Read Resource | Username | Username |
| Activity Audit | Read Resource | User ID | UserId |
| Activity Audit | Read Resource | Session ID | SessionKey |
| Activity Audit | Read Resource | IP Address | SourceIp |
| Activity Audit | Read Resource | Resource Name | Name |
| Activity Audit | Read Resource | Resource Type | QueriedEntities |

## Example logs

| Category | Event type | Log | Sample field values |
| -------- | ---------- | --- | ------------------- |
| Activity Audit | Read Resource | [read](/products/salesforce/event_examples/salesforce_rtem_listvieweventstream/activity_audit_read_resource_listvieweventstream.json) | Timestamp=2023-03-20T16:25:52.850+0000; Event ID=abcdefgh-1234-0000-0000-000000000001; Event Code / Type=Classic; Result=None; Username=john@example.com |


