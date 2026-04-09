# Salesforce — EventLogFile Logout Event

📌 **v1.0.0** · 🗄 **Retention:** 1 Day · ⚡ **Latency:** 3 Hours

🗄 Available for free with 1 day retention, otherwise requires an add-on subscription for 30 day retention.⚡ Event log files are accessible via hourly and 24 hour log files. It can take between 3–6 hours from the time of the event to be available in the hourly log file.📜 **Licensing:** Available for free with 1 day retention, otherwise requires Salesforce Shield or a Salesforce Event Monitoring add-on subscription.

This event source is to track logout events in Salesforce.
## References
* [EventLogFile Logout Event](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_eventlogfile_logout.htm)
## Field mappings

| Category | Event type | Attribute | Source field(s) |
| -------- | ---------- | --------- | ---------------- |
| Authentication | Account Logout | Timestamp | TIMESTAMP_DERIVED |
| Authentication | Account Logout | Event Code / Type | EVENT_TYPE |
| Authentication | Account Logout | User ID | USER_ID |
| Authentication | Account Logout | User Type / Role | USER_TYPE |
| Authentication | Account Logout | Session ID | LOGIN_KEY |
| Authentication | Account Logout | IP Address | CLIENT_IP |
| Authentication | Account Logout | User Agent Name | BROWSER_TYPE |
| Authentication | Account Logout | Device/Client Type | PLATFORM_TYPE |

## Example logs

| Category | Event type | Log | Sample field values |
| -------- | ---------- | --- | ------------------- |
| Authentication | Account Logout | [success](/products/salesforce/event_examples/salesforce_elf_logout_event/authentication_account_logout_elf.json) | Timestamp=2023-03-16T21:07:47.645Z; Event Code / Type=Logout; User ID=000000000000123; User Type / Role=Standard(db=S,api=Standard); Session ID=9870000000012300 |


