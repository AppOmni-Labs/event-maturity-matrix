# Snowflake - Login History (1.0.0)

> Entity Name: event_source

This Account Usage view can be used to query login attempts by Snowflake users within the last 365 days (1 year).

## References
* [About the Login History View](https://docs.snowflake.com/en/sql-reference/account-usage/login_history)

## Retention

Based on our research, Snowflake retains audit logs for 365 days.


### Comments
No comments


## Latency

Based on our research, Snowflake has a latency of up to 120 minutes.

### Comments
No comments


## Licensing

Contact Sales

## Mappings

| Category | Event Type | Attributes | Examples |
| -------- | ---------- | ---------- | -------- |
| C0001 | ET0001 |A0001 -> EVENT_TIMESTAMP<br />A0002 -> EVENT_ID<br />A0003 -> EVENT_TYPE<br />A0005 -> USER_NAME<br />A0009 -> CLIENT_IP<br />A0012 -> REPORTED_CLIENT_TYPE<br />A0014 -> FIRST_AUTHENTICATION_FACTOR<br />|[success](/products/snowflake/event_examples/login_history/authentication_account_login.json)<br />|
| C0001 | ET0003 |A0001 -> EVENT_TIMESTAMP<br />A0002 -> EVENT_ID<br />A0003 -> EVENT_TYPE<br />A0004 -> IS_SUCCESS<br />A0005 -> USER_NAME<br />A0009 -> CLIENT_IP<br />A0012 -> REPORTED_CLIENT_TYPE<br />A0016 -> SECOND_AUTHENTICATION_FACTOR<br />A0017 -> IS_SUCCESS<br />|[success](/products/snowflake/event_examples/login_history/authentication_mfa_verification.json)<br />|


