# Salesforce - Real-Time Event Monitoring ReportEventStream (0.0.1)

> Entity Name: event_source

Tracks report-related actions, such as when a user runs or exports a report.

## References
* [ReportEventStream](https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/sforce_api_objects_reporteventstream.htm)

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
| C0004 | ET0031 |A0001 -> EventDate<br />A0002 -> EventIdentifier<br />A0003 -> Operation<br />A0004 -> PolicyOutcome<br />A0005 -> Username<br />A0006 -> UserId<br />A0008 -> SessionKey<br />A0009 -> SourceIp<br />A0012 -> EventSource<br />A0030 -> Name<br />A0031 -> QueriedEntities<br />|[read](/products/salesforce/event_examples/activity_audit_read_resource_reporteventstream.json)<br />|
| C0004 | ET0034 |A0001 -> EventDate<br />A0002 -> EventIdentifier<br />A0003 -> Operation<br />A0004 -> PolicyOutcome<br />A0005 -> Username<br />A0006 -> UserId<br />A0008 -> SessionKey<br />A0009 -> SourceIp<br />A0012 -> EventSource<br />A0032 -> RowsProcessed<br />A0030 -> Name<br />A0031 -> QueriedEntities<br />|[download](/products/salesforce/event_examples/activity_audit_download_resource_reporteventstream.json)<br />|


