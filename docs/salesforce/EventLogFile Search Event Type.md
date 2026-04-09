# Salesforce — EventLogFile Search Event Type

📌 **v1.0.0** · 🗄 **Retention:** 1 Day · ⚡ **Latency:** 3 Hours

🗄 Available for free with 1 day retention, otherwise requires an add-on subscription for 30 day retention.⚡ Event log files are accessible via hourly and 24 hour log files. It can take between 3–6 hours from the time of the event to be available in the hourly log file.📜 **Licensing:** Available for free with 1 day retention, otherwise requires Salesforce Shield or a Salesforce Event Monitoring add-on subscription.

Tracks Salesforce search requests, including the search string and result counts.
## References
* [EventLogFile Search Event](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_eventlogfile_search.htm)
## Field mappings

| Category | Event type | Attribute | Source field(s) |
| -------- | ---------- | --------- | ---------------- |
| Activity Audit | Query Resource | Timestamp | TIMESTAMP_DERIVED |
| Activity Audit | Query Resource | Event Code / Type | EVENT_TYPE |
| Activity Audit | Query Resource | User ID | USER_ID |
| Activity Audit | Query Resource | Query String | SEARCH_QUERY |

## Example logs

| Category | Event type | Log | Sample field values |
| -------- | ---------- | --- | ------------------- |
| Activity Audit | Query Resource | [success](/products/salesforce/event_examples/salesforce_elf_search_event/activity_audit_query_resource_elf_search.json) | Timestamp=2025-09-01T10:10:01.510Z; Event Code / Type=Search; User ID=005Dn000001ab23; Query String="""test_search_string_*""" |


