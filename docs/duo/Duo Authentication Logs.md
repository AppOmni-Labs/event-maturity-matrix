# Duo - Duo Authentication Logs (1.0.0)

> Entity Name: event_source

Provides an audit trail of authentication activity within the Duo Security platform.

## References
* [Duo Authentication Logs](https://duo.com/docs/adminapi#authentication-logs)

## Retention

Based on our research, Duo retains audit logs for 180 days.


### Comments
Maximum retention of 180 days, even if the log retention interval is set to a value greater than 180 days, reference https://help.duo.com/s/article/2990?language=en_US


## Latency

Based on our research, Duo has a latency of Near real-time.

### Comments
There is an intentional two minute delay in availability of new authentication events, reference https://duo.com/docs/adminapi#authentication-logs


## Licensing

The Duo Admin API is available to Duo Premier, Duo Advantage, and Duo Essentials customers, and new customers with an Advantage or Premier trial. For more information, see https://duo.com/docs/adminapi#about-the-admin-api

## Mappings

| Category | Event Type | Attributes | Examples |
| -------- | ---------- | ---------- | -------- |
| C0001 | ET0003 |A0001 -> ['timestamp', 'isotimestamp']<br />A0004 -> result<br />A0005 -> username<br />A0009 -> ip<br />A0010 -> ['location.city', 'location.country', 'location.state']<br />A0011 -> access_device.browser<br />A0012 -> access_device.os<br />A0016 -> ['factor', 'device']<br />A0017 -> reason<br />A0018 -> integration<br />|[success](/products/duo/event_examples/authentication_mfa_verification_success_auth.json)<br />[failure](/products/duo/event_examples/authentication_mfa_verification_failure_auth.json)<br />|


