# Salesforce — Real-Time Event Monitoring LoginEventStream

📌 **v1.0.0** · 🗄 **Retention:** 10 Years · ⚡ **Latency:** Real-Time

📜 **Licensing:** Requires Salesforce Shield or a Salesforce Event Monitoring add-on subscription.

Tracks login activity of users who log in to Salesforce.
## References
* [LoginEventStream](https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/sforce_api_objects_logineventstream.htm)
## Field mappings

| Category | Event type | Attribute | Source field(s) |
| -------- | ---------- | --------- | ---------------- |
| Authentication | Account Login | Timestamp | EventDate |
| Authentication | Account Login | Event ID | EventIdentifier |
| Authentication | Account Login | Event Code / Type | data.payload.attributes.type |
| Authentication | Account Login | Result | Status |
| Authentication | Account Login | Username | Username |
| Authentication | Account Login | User ID | UserId |
| Authentication | Account Login | User Type / Role | UserType |
| Authentication | Account Login | Session ID | LoginKey |
| Authentication | Account Login | IP Address | SourceIp |
| Authentication | Account Login | IP Geolocation / ASN | City |
| Authentication | Account Login | User Agent Name | Browser |
| Authentication | Account Login | Device/Client Type | Platform |
| Authentication | Account Login | Failure Context | Status |
| Authentication | Account Login | Credential Context | LoginType |
| Authentication | Account Login | Identity Service Provider Context | AuthServiceId |

## Example logs

| Category | Event type | Log | Sample field values |
| -------- | ---------- | --- | ------------------- |
| Authentication | Account Login | [success](/products/salesforce/event_examples/salesforce_rtem_logineventstream/authentication_account_login.json) | Timestamp=2023-03-08T18:16:11.493+0000; Event ID=abcdefgh-1234-0000-0000-000000000001; Event Code / Type=LoginEvent; Result=Success; Username=john@example.com |
| Authentication | Account Login | [failure](/products/salesforce/event_examples/salesforce_rtem_logineventstream/authentication_account_login_failure.json) | Timestamp=2023-03-09T15:08:03.054+0000; Event ID=abcdefgh-1234-0000-0000-000000000001; Event Code / Type=LoginEvent; Result=Password Lockout; Username=alice@example.com |


