# Salesforce — Real-Time Event Monitoring IdentityVerificationEvent

📌 **v1.0.0** · 🗄 **Retention:** 10 Years · ⚡ **Latency:** Real-Time

🗄 N/A


⚡ N/A


📜 **Licensing:** Requires Salesforce Shield or a Salesforce Event Monitoring add-on subscription.


Tracks user identity verification events in a Salesforce org.
## References
* [IdentityVerificationEvent](https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/sforce_api_objects_identityverificationevent.htm)
## Field mappings

| Category | Event type | Attribute | Source field(s) |
| -------- | ---------- | --------- | ---------------- |
| Authentication | MFA Verification | Timestamp | EventDate |
| Authentication | MFA Verification | Event ID | EventIdentifier |
| Authentication | MFA Verification | Event Code / Type | data.payload.attributes.type |
| Authentication | MFA Verification | Result | Status |
| Authentication | MFA Verification | Username | Username |
| Authentication | MFA Verification | User ID | UserId |
| Authentication | MFA Verification | Session ID | LoginKey |
| Authentication | MFA Verification | IP Address | SourceIp |
| Authentication | MFA Verification | IP Geolocation / ASN | City |
| Authentication | MFA Verification | Verification Method | VerificationMethod |
| Authentication | MFA Verification | Verification Flagged | Status |
| Authentication | MFA Verification | Activity Performed | Activity |

## Example logs

| Category | Event type | Log | Sample field values |
| -------- | ---------- | --- | ------------------- |
| Authentication | MFA Verification | [success](/products/salesforce/event_examples/salesforce_rtem_identityverificationevent/authentication_mfa_verification.json) | Timestamp=2023-03-08T16:50:46.153+0000; Event ID=abcdefgh-1234-0000-0000-000000000001; Event Code / Type=IdentityVerificationEvent; Result=Succeeded; Username=john@example.com |
| Authentication | MFA Verification | [inprogress](/products/salesforce/event_examples/salesforce_rtem_identityverificationevent/authentication_mfa_verification_inprogress.json) | Timestamp=2023-03-16T16:00:23.934+0000; Event ID=abcdefgh-1234-0000-0000-000000000001; Event Code / Type=IdentityVerificationEvent; Result=InProgress; Username=alice@example.com |
| Authentication | MFA Verification | [failure](/products/salesforce/event_examples/salesforce_rtem_identityverificationevent/authentication_mfa_verification_failure.json) | Timestamp=2023-03-16T14:37:56.275+0000; Event ID=abcdefgh-1234-0000-0000-000000000001; Event Code / Type=IdentityVerificationEvent; Result=FailedInvalidCode; Username=bob@example.com |


