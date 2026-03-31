# Snowflake — Login History

📌 **v1.0.0** · 🗄 **Retention:** 365 days · ⚡ **Latency:** up to 120 minutes

🗄 No comments


⚡ No comments


📜 **Licensing:** Contact Sales


This Account Usage view can be used to query login attempts by Snowflake users within the last 365 days (1 year).
## References
* [About the Login History View](https://docs.snowflake.com/en/sql-reference/account-usage/login_history)
## Field mappings

| Category | Event type | Attribute | Source field(s) |
| -------- | ---------- | --------- | ---------------- |
| Authentication | Account Login | Timestamp | EVENT_TIMESTAMP |
| Authentication | Account Login | Event ID | EVENT_ID |
| Authentication | Account Login | Event Code / Type | EVENT_TYPE |
| Authentication | Account Login | Username | USER_NAME |
| Authentication | Account Login | IP Address | CLIENT_IP |
| Authentication | Account Login | Device/Client Type | REPORTED_CLIENT_TYPE |
| Authentication | Account Login | Credential Context | FIRST_AUTHENTICATION_FACTOR |
| Authentication | MFA Verification | Timestamp | EVENT_TIMESTAMP |
| Authentication | MFA Verification | Event ID | EVENT_ID |
| Authentication | MFA Verification | Event Code / Type | EVENT_TYPE |
| Authentication | MFA Verification | Result | IS_SUCCESS |
| Authentication | MFA Verification | Username | USER_NAME |
| Authentication | MFA Verification | IP Address | CLIENT_IP |
| Authentication | MFA Verification | Device/Client Type | REPORTED_CLIENT_TYPE |
| Authentication | MFA Verification | Verification Method | SECOND_AUTHENTICATION_FACTOR |
| Authentication | MFA Verification | Verification Flagged | IS_SUCCESS |

## Example logs

| Category | Event type | Log | Sample field values |
| -------- | ---------- | --- | ------------------- |
| Authentication | Account Login | [success](/products/snowflake/event_examples/login_history/authentication_account_login.json) | Timestamp=1717764280.813000; Event ID=53754033158915655; Event Code / Type=LOGIN; Username=bruce-wayne; IP Address=12.3.4.56 |
| Authentication | MFA Verification | [success](/products/snowflake/event_examples/login_history/authentication_mfa_verification.json) | Timestamp=1717633886.401000; Event ID=12042414114134585; Event Code / Type=LOGIN; Result=YES; Username=bruce-wayne |


