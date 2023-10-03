# Salesforce - Real-Time Event Monitoring IdentityVerificationEvent (0.0.1)

> Entity Name: event_source

Tracks user identity verification events in a Salesforce org.

## References
* [IdentityVerificationEvent](https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/sforce_api_objects_identityverificationevent.htm)

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
| C0001 | ET0003 |A0001 -> EventDate<br />A0002 -> EventIdentifier<br />A0003 -> attributes.type<br />A0004 -> Status<br />A0005 -> Username<br />A0006 -> UserId<br />A0008 -> LoginKey<br />A0009 -> SourceIp<br />A0010 -> City<br />A0016 -> VerificationMethod<br />A0017 -> Status<br />A0018 -> Activity<br />|[success](/products/salesforce/event_examples/authentication_mfa_verification.json)<br />|


