# Salesforce — EventLogFile Login Event

📌 **v1.0.0** · 🗄 **Retention:** 1 Day · ⚡ **Latency:** 3 Hours

🗄 Available for free with 1 day retention, otherwise requires an add-on subscription for 30 day retention.


⚡ Event log files are accessible via hourly and 24 hour log files. It can take between 3–6 hours from the time of the event to be available in the hourly log file.


📜 **Licensing:** Available for free with 1 day retention, otherwise requires Salesforce Shield or a Salesforce Event Monitoring add-on subscription.


This event source is to track login events in Salesforce.
## References
* [EventLogFile Login Event](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_eventlogfile_login.htm)
## Field mappings

| Category | Event type | Attribute | Source field(s) |
| -------- | ---------- | --------- | ---------------- |
| Authentication | Account Login | Timestamp | TIMESTAMP_DERIVED |
| Authentication | Account Login | Event Code / Type | EVENT_TYPE |
| Authentication | Account Login | Result | LOGIN_STATUS |
| Authentication | Account Login | Username | USER_NAME |
| Authentication | Account Login | User ID | USER_ID |
| Authentication | Account Login | User Type / Role | USER_TYPE |
| Authentication | Account Login | Session ID | LOGIN_KEY |
| Authentication | Account Login | IP Address | SOURCE_IP |
| Authentication | Account Login | User Agent Name | BROWSER_TYPE |
| Authentication | Account Login | Failure Context | LOGIN_STATUS |
| Authentication | Account Login | Credential Context | LOGIN_TYPE |
| Authentication | Account Login | Identity Service Provider Context | AUTHENTICATION_METHOD_REFERENCE |

## Example logs

| Category | Event type | Log | Sample field values |
| -------- | ---------- | --- | ------------------- |
| Authentication | Account Login | [success](/products/salesforce/event_examples/salesforce_elf_login_event/authentication_account_login_elf.json) | Timestamp=2023-03-15T01:38:19.151Z; Event Code / Type=Login; Result=LOGIN_OAUTH_NO_CONSUMER; Username=john@example.com; User ID=000000000000123 |


