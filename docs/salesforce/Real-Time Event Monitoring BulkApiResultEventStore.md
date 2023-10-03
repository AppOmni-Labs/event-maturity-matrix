# Salesforce - Real-Time Event Monitoring BulkApiResultEventStore (0.0.1)

> Entity Name: event_source

Tracks when a user downloads the results of a Bulk API request.

## References
* [BulkApiResultEventStore](https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/sforce_api_objects_bulkapiresulteventstore.htm)

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
| C0004 | ET0030 |A0001 -> EventDate<br />A0002 -> EventIdentifier<br />A0003 -> attributes.type<br />A0004 -> PolicyOutcome<br />A0005 -> Username<br />A0006 -> UserId<br />A0008 -> SessionKey<br />A0009 -> SourceIp<br />A0030 -> Query<br />|[download](/products/salesforce/event_examples/activity_audit_download_resource_bulkapiresulteventstore.json)<br />|


