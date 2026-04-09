





# Salesforce — EventLogFile Apex Callout Event Type

📌 **v1.0.0** · 🗄 **Retention:** 30 Days · ⚡ **Latency:** 3 Hours



⚡ Event log files are accessible via hourly and 24 hour log files. It can take between 3–6 hours from the time of the event to be available in the hourly log file.


📜 **Licensing:** Requires Salesforce Shield or a Salesforce Event Monitoring add-on subscription.


Provides details about callouts (external requests) during Apex code execution.
## References
* [EventLogFile Apex Event](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_eventlogfile_apexcallout.htm)
## Field mappings

| Category | Event type | Attribute | Source field(s) |
| -------- | ---------- | --------- | ---------------- |
| Activity Audit | Read Resource | Timestamp | TIMESTAMP_DERIVED |
| Activity Audit | Read Resource | Event Code / Type | EVENT_TYPE |
| Activity Audit | Read Resource | Result | SUCCESS |
| Activity Audit | Read Resource | Session ID | SESSION_KEY |
| Activity Audit | Read Resource | IP Address | CLIENT_IP |
| Activity Audit | Read Resource | Device/Client Type | TYPE |
| Activity Audit | Read Resource | Resource Name | URL |

## Example logs

| Category | Event type | Log | Sample field values |
| -------- | ---------- | --- | ------------------- |
| Activity Audit | Read Resource | [success](/products/salesforce/event_examples/salesforce_elf_apex_callout_event/activity_audit_read_resource_apexcallout.json) | Timestamp=2023-03-21T17:10:17.871Z; Event Code / Type=ApexCallout; Result=1; Session ID=9870000000012300; IP Address=198.51.100.1 |


