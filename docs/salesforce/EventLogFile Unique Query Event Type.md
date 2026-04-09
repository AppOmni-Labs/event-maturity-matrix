# Salesforce — EventLogFile Unique Query Event Type

📌 **v1.0.0** · 🗄 **Retention:** 1 Day · ⚡ **Latency:** 3 Hours

🗄 Available for free with 1 day retention, otherwise requires an add-on subscription for 30 day retention.⚡ Event log files are accessible via hourly and 24 hour log files. It can take between 3–6 hours from the time of the event to be available in the hourly log file.📜 **Licensing:** Available for free with 1 day retention, otherwise requires Salesforce Shield or a Salesforce Event Monitoring add-on subscription.

Tracks normalized SOQL query patterns (unique query keys) for performance and security analysis.
## References
* [EventLogFile Unique Query Event](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_eventlogfile_unique_query_event_elf.htm)
## Field mappings

| Category | Event type | Attribute | Source field(s) |
| -------- | ---------- | --------- | ---------------- |
| Activity Audit | Query Resource | Timestamp | TIMESTAMP_DERIVED |
| Activity Audit | Query Resource | Event Code / Type | EVENT_TYPE |
| Activity Audit | Query Resource | User ID | USER_ID |
| Activity Audit | Query Resource | Session ID | SESSION_KEY |
| Activity Audit | Query Resource | Query String | QUERY_IDENTIFIER |

## Example logs

| Category | Event type | Log | Sample field values |
| -------- | ---------- | --- | ------------------- |
| Activity Audit | Query Resource | [success](/products/salesforce/event_examples/salesforce_elf_unique_query_event/activity_audit_query_resource_elf_uniquequery.json) | Timestamp=2025-09-02T10:10:01.350Z; Event Code / Type=UniqueQuery; User ID=005Dn000001ab23; Session ID=KyafABkxLMa2abcd; Query String=SELECT ReportsTo.LastModifiedById, ReportsTo.Name, ReportsT… |


