# Salesforce — EventLogFile SOAP API Event Type

📌 **v1.0.0** · 🗄 **Retention:** 30 Days · ⚡ **Latency:** 3 Hours

🗄 N/A


⚡ Event log files are accessible via hourly and 24 hour log files. It can take between 3–6 hours from the time of the event to be available in the hourly log file.


📜 **Licensing:** Requires Salesforce Shield or a Salesforce Event Monitoring add-on subscription.


Provides details about a Salesforce org's SOAP API request activity.
## References
* [EventLogFile SOAP API](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_eventlogfile_api.htm)
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
| Activity Audit | Create Resource | Device/Client Type | API_TYPE |
| Activity Audit | Create Resource | Resource Type | ENTITY_NAME |
| Activity Audit | Read Resource | Timestamp | TIMESTAMP_DERIVED |
| Activity Audit | Read Resource | Event Code / Type | EVENT_TYPE |
| Activity Audit | Read Resource | Result | REQUEST_STATUS |
| Activity Audit | Read Resource | User ID | USER_ID |
| Activity Audit | Read Resource | User Type / Role | USER_TYPE |
| Activity Audit | Read Resource | Session ID | SESSION_KEY |
| Activity Audit | Read Resource | IP Address | CLIENT_IP |
| Activity Audit | Read Resource | Device/Client Type | API_TYPE |
| Activity Audit | Read Resource | Resource Type | ENTITY_NAME |
| Activity Audit | Update Resource | Timestamp | TIMESTAMP_DERIVED |
| Activity Audit | Update Resource | Event Code / Type | EVENT_TYPE |
| Activity Audit | Update Resource | Result | REQUEST_STATUS |
| Activity Audit | Update Resource | User ID | USER_ID |
| Activity Audit | Update Resource | User Type / Role | USER_TYPE |
| Activity Audit | Update Resource | Session ID | SESSION_KEY |
| Activity Audit | Update Resource | IP Address | CLIENT_IP |
| Activity Audit | Update Resource | Device/Client Type | API_TYPE |
| Activity Audit | Update Resource | Resource Type | ENTITY_NAME |
| Activity Audit | Delete Resource | Timestamp | TIMESTAMP_DERIVED |
| Activity Audit | Delete Resource | Event Code / Type | EVENT_TYPE |
| Activity Audit | Delete Resource | Result | REQUEST_STATUS |
| Activity Audit | Delete Resource | User ID | USER_ID |
| Activity Audit | Delete Resource | User Type / Role | USER_TYPE |
| Activity Audit | Delete Resource | Session ID | SESSION_KEY |
| Activity Audit | Delete Resource | IP Address | CLIENT_IP |
| Activity Audit | Delete Resource | Device/Client Type | API_TYPE |
| Activity Audit | Delete Resource | Resource Type | ENTITY_NAME |
| Activity Audit | Download Resource | Timestamp | TIMESTAMP_DERIVED |
| Activity Audit | Download Resource | Event Code / Type | EVENT_TYPE |
| Activity Audit | Download Resource | Result | REQUEST_STATUS |
| Activity Audit | Download Resource | User ID | USER_ID |
| Activity Audit | Download Resource | User Type / Role | USER_TYPE |
| Activity Audit | Download Resource | Session ID | SESSION_KEY |
| Activity Audit | Download Resource | IP Address | CLIENT_IP |
| Activity Audit | Download Resource | Device/Client Type | API_TYPE |
| Activity Audit | Download Resource | Resource Metadata | ROWS_PROCESSED |
| Activity Audit | Download Resource | Resource Type | ENTITY_NAME |

## Example logs

| Category | Event type | Log | Sample field values |
| -------- | ---------- | --- | ------------------- |
| Activity Audit | Create Resource | [create](/products/salesforce/event_examples/salesforce_elf_soap_api_event/activity_audit_create_resource_soapapi.json) | Timestamp=2023-03-20T14:59:44.655Z; Event Code / Type=API; Result=; User ID=000000000000123; User Type / Role=Standard |
| Activity Audit | Read Resource | [read](/products/salesforce/event_examples/salesforce_elf_soap_api_event/activity_audit_read_resource_soapapi.json) | Timestamp=2023-03-20T14:59:33.958Z; Event Code / Type=API; Result=; User ID=000000000000123; User Type / Role=Standard |
| Activity Audit | Update Resource | [update](/products/salesforce/event_examples/salesforce_elf_soap_api_event/activity_audit_update_resource_soapapi.json) | Timestamp=2023-03-20T14:59:59.965Z; Event Code / Type=API; Result=; User ID=000000000000123; User Type / Role=Standard |
| Activity Audit | Delete Resource | [delete](/products/salesforce/event_examples/salesforce_elf_soap_api_event/activity_audit_delete_resource_soapapi.json) | Timestamp=2023-03-20T05:19:32.701Z; Event Code / Type=API; Result=; User ID=000000000000123; User Type / Role=Standard |
| Activity Audit | Download Resource | [download](/products/salesforce/event_examples/salesforce_elf_soap_api_event/activity_audit_download_resource_soapapi.json) | Timestamp=2023-03-17T18:04:24.293Z; Event Code / Type=API; Result=; User ID=000000000000123; User Type / Role=Standard |


