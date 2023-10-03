# Salesforce - Real-Time Event Monitoring LogoutEventStream (0.0.1)

> Entity Name: event_source

A logout event records a successful user logout from the Salesforce user interface.

## References
* [LogoutEventStream](https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/sforce_api_objects_logouteventstream.htm)

## Retention

Based on our research, Salesforce retains audit logs for 6 Months.


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
| C0001 | ET0002 |A0001 -> EventDate<br />A0002 -> EventIdentifier<br />A0003 -> attributes.type<br />A0005 -> Username<br />A0006 -> UserId<br />A0008 -> SessionKey<br />A0009 -> SourceIp<br />|[success](/products/salesforce/event_examples/authentication_account_logout.json)<br />|


