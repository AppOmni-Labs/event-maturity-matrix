





# Salesforce — EventLogFile Aura Request Event Type

📌 **v1.0.0** · 🗄 **Retention:** 30 Days · ⚡ **Latency:** 3 Hours



⚡ Event log files are accessible via hourly and 24 hour log files. It can take between 3–6 hours from the time of the event to be available in the hourly log file.


📜 **Licensing:** Requires Salesforce Shield or a Salesforce Event Monitoring add-on subscription.


Provides details of requests to Apex methods from Aura and Lightning web components.
## References
* [EventLogFile Aura Request Event](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_eventlogfile_lightning_component.htm)
## Field mappings

| Category | Event type | Attribute | Source field(s) |
| -------- | ---------- | --------- | ---------------- |
| Activity Audit | Create Resource | Timestamp | TIMESTAMP_DERIVED |
| Activity Audit | Create Resource | Event Code / Type | EVENT_TYPE |
| Activity Audit | Create Resource | Result | REQUEST_STATUS |
| Activity Audit | Create Resource | User ID | USER_ID |
| Activity Audit | Create Resource | User Type / Role | USER_TYPE |
| Activity Audit | Create Resource | Session ID | SESSION_KEY |
| Activity Audit | Create Resource | IP Address | CLIENT_IP |
| Activity Audit | Create Resource | User Agent Name | USER_AGENT |
| Activity Audit | Create Resource | Resource Name | ACTION_MESSAGE |
| Activity Audit | Read Resource | Timestamp | TIMESTAMP_DERIVED |
| Activity Audit | Read Resource | Event Code / Type | EVENT_TYPE |
| Activity Audit | Read Resource | Result | REQUEST_STATUS |
| Activity Audit | Read Resource | User ID | USER_ID |
| Activity Audit | Read Resource | User Type / Role | USER_TYPE |
| Activity Audit | Read Resource | Session ID | SESSION_KEY |
| Activity Audit | Read Resource | IP Address | CLIENT_IP |
| Activity Audit | Read Resource | User Agent Name | USER_AGENT |
| Activity Audit | Read Resource | Resource Name | ACTION_MESSAGE |
| Activity Audit | Update Resource | Timestamp | TIMESTAMP_DERIVED |
| Activity Audit | Update Resource | Event Code / Type | EVENT_TYPE |
| Activity Audit | Update Resource | Result | REQUEST_STATUS |
| Activity Audit | Update Resource | User ID | USER_ID |
| Activity Audit | Update Resource | User Type / Role | USER_TYPE |
| Activity Audit | Update Resource | Session ID | SESSION_KEY |
| Activity Audit | Update Resource | IP Address | CLIENT_IP |
| Activity Audit | Update Resource | User Agent Name | USER_AGENT |
| Activity Audit | Update Resource | Resource Name | ACTION_MESSAGE |
| Activity Audit | Delete Resource | Timestamp | TIMESTAMP_DERIVED |
| Activity Audit | Delete Resource | Event Code / Type | EVENT_TYPE |
| Activity Audit | Delete Resource | Result | REQUEST_STATUS |
| Activity Audit | Delete Resource | User ID | USER_ID |
| Activity Audit | Delete Resource | User Type / Role | USER_TYPE |
| Activity Audit | Delete Resource | Session ID | SESSION_KEY |
| Activity Audit | Delete Resource | IP Address | CLIENT_IP |
| Activity Audit | Delete Resource | User Agent Name | USER_AGENT |
| Activity Audit | Delete Resource | Resource Name | ACTION_MESSAGE |

## Example logs

| Category | Event type | Log | Sample field values |
| -------- | ---------- | --- | ------------------- |
| Activity Audit | Create Resource | [create](/products/salesforce/event_examples/salesforce_elf_aura_request_event/activity_audit_create_resource_aurarequest.json) | Timestamp=2023-03-17T16:09:37.079Z; Event Code / Type=AuraRequest; Result=; User ID=000000000000123; User Type / Role=Standard |
| Activity Audit | Read Resource | [read](/products/salesforce/event_examples/salesforce_elf_aura_request_event/activity_audit_read_resource_aurarequest.json) | Timestamp=2023-03-17T17:26:46.960Z; Event Code / Type=AuraRequest; Result=; User ID=000000000000123; User Type / Role=Standard |
| Activity Audit | Update Resource | [update](/products/salesforce/event_examples/salesforce_elf_aura_request_event/activity_audit_update_resource_aurarequest.json) | Timestamp=2023-03-17T16:52:02.419Z; Event Code / Type=AuraRequest; Result=; User ID=000000000000123; User Type / Role=Standard |
| Activity Audit | Delete Resource | [delete](/products/salesforce/event_examples/salesforce_elf_aura_request_event/activity_audit_delete_resource_aurarequest.json) | Timestamp=2023-03-17T14:14:57.834Z; Event Code / Type=AuraRequest; Result=; User ID=000000000000123; User Type / Role=Standard |


