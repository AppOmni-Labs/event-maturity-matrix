# Salesforce - Real-Time Event Monitoring LoginEventStream (0.0.1)

> Entity Name: event_source

Tracks login activity of users who log in to Salesforce.

## References
* [LoginEventStream](https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/sforce_api_objects_logineventstream.htm)

## Retention

Based on our research, Salesforce retains audit logs for 10 Years.


### Comments
N/A


## Latency

Based on our research, Salesforce has a latency of Real-Time.

### Comments
N/A


## Licensing

Requires Salesforce Shield or a Salesforce Event Monitoring add-on subscription.

## Mappings

| Category | Event Type | Attributes | Examples |
| -------- | ---------- | ---------- | -------- |
| C0001 | ET0001 |A0001 -> EventDate<br />A0002 -> EventIdentifier<br />A0003 -> attributes.type<br />A0004 -> Status<br />A0005 -> Username<br />A0006 -> UserId<br />A0007 -> UserType<br />A0008 -> LoginKey<br />A0009 -> SourceIp<br />A0010 -> City<br />A0011 -> Browser<br />A0012 -> Platform<br />A0013 -> Status<br />A0014 -> LoginType<br />A0015 -> AuthServiceId<br />|[success](/products/salesforce/event_examples/authentication_account_login.json)<br />|


