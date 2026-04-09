# Salesforce — Real-Time Event Monitoring LogoutEventStream

📌 **v1.0.0** · 🗄 **Retention:** 6 Months · ⚡ **Latency:** Real-Time

📜 **Licensing:** Requires Salesforce Shield or a Salesforce Event Monitoring add-on subscription.

A logout event records a successful user logout from the Salesforce user interface.
## References
* [LogoutEventStream](https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/sforce_api_objects_logouteventstream.htm)
## Field mappings

| Category | Event type | Attribute | Source field(s) |
| -------- | ---------- | --------- | ---------------- |
| Authentication | Account Logout | Timestamp | EventDate |
| Authentication | Account Logout | Event ID | EventIdentifier |
| Authentication | Account Logout | Event Code / Type | data.payload.attributes.type |
| Authentication | Account Logout | Username | Username |
| Authentication | Account Logout | User ID | UserId |
| Authentication | Account Logout | Session ID | SessionKey |
| Authentication | Account Logout | IP Address | SourceIp |

## Example logs

| Category | Event type | Log | Sample field values |
| -------- | ---------- | --- | ------------------- |
| Authentication | Account Logout | [success](/products/salesforce/event_examples/salesforce_rtem_logouteventstream/authentication_account_logout.json) | Timestamp=2023-03-01T19:33:50.037+0000; Event ID=abcdefgh-1234-0000-0000-000000000001; Event Code / Type=LogoutEvent; Username=john@example.com; User ID=000000000000123AbC |


