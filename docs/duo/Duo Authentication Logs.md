# Duo — Duo Authentication Logs

📌 **v1.0.0** · 🗄 **Retention:** 180 days · ⚡ **Latency:** Near real-time

🗄 Maximum retention of 180 days, even if the log retention interval is set to a value greater than 180 days, reference https://help.duo.com/s/article/2990?language=en_US


⚡ There is an intentional two minute delay in availability of new authentication events, reference https://duo.com/docs/adminapi#authentication-logs


📜 **Licensing:** The Duo Admin API is available to Duo Premier, Duo Advantage, and Duo Essentials customers, and new customers with an Advantage or Premier trial. For more information, see https://duo.com/docs/adminapi#about-the-admin-api


Provides an audit trail of authentication activity within the Duo Security platform.
## References
* [Duo Authentication Logs](https://duo.com/docs/adminapi#authentication-logs)
## Field mappings

| Category | Event type | Attribute | Source field(s) |
| -------- | ---------- | --------- | ---------------- |
| Authentication | MFA Verification | Timestamp | timestamp, isotimestamp |
| Authentication | MFA Verification | Result | result |
| Authentication | MFA Verification | Username | username |
| Authentication | MFA Verification | IP Address | ip |
| Authentication | MFA Verification | IP Geolocation / ASN | location.city, location.country, location.state |
| Authentication | MFA Verification | User Agent Name | access_device.browser |
| Authentication | MFA Verification | Device/Client Type | access_device.os |
| Authentication | MFA Verification | Verification Method | factor, device |
| Authentication | MFA Verification | Verification Flagged | reason |
| Authentication | MFA Verification | Activity Performed | integration |

## Example logs

| Category | Event type | Log | Sample field values |
| -------- | ---------- | --- | ------------------- |
| Authentication | MFA Verification | [success](/products/duo/event_examples/authentication_mfa_verification_success_auth.json) | Timestamp=1716314997; Result=SUCCESS; Username=Bruce Wayne; IP Address=192.168.10.1; IP Geolocation / ASN=San Francisco |
| Authentication | MFA Verification | [failure](/products/duo/event_examples/authentication_mfa_verification_failure_auth.json) | Timestamp=1716314928; Result=FAILURE; Username=Tony Stark; IP Address=192.168.10.1; IP Geolocation / ASN=San Francisco |


