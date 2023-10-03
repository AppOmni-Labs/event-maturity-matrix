# Salesforce - Real-Time Event Monitoring UriEventStream (0.0.1)

> Entity Name: event_source

Detects when a user creates, accesses, updates, or deletes a record in Salesforce Classic only.

## References
* [UriEventStream](https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/sforce_api_objects_urieventstream.htm)

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
| C0004 | ET0030 |A0001 -> EventDate<br />A0002 -> EventIdentifier<br />A0003 -> Operation<br />A0004 -> OperationStatus<br />A0005 -> UserName<br />A0006 -> UserId<br />A0007 -> UserType<br />A0008 -> SessionKey<br />A0009 -> SourceIp<br />A0030 -> Name<br />A0031 -> QueriedEntities<br />|[create](/products/salesforce/event_examples/activity_audit_create_resource_urieventstream.json)<br />|
| C0004 | ET0031 |A0001 -> EventDate<br />A0002 -> EventIdentifier<br />A0003 -> Operation<br />A0004 -> OperationStatus<br />A0005 -> UserName<br />A0006 -> UserId<br />A0007 -> UserType<br />A0008 -> SessionKey<br />A0009 -> SourceIp<br />A0030 -> Name<br />A0031 -> QueriedEntities<br />|[read](/products/salesforce/event_examples/activity_audit_read_resource_urieventstream.json)<br />|
| C0004 | ET0032 |A0001 -> EventDate<br />A0002 -> EventIdentifier<br />A0003 -> Operation<br />A0004 -> OperationStatus<br />A0005 -> UserName<br />A0006 -> UserId<br />A0007 -> UserType<br />A0008 -> SessionKey<br />A0009 -> SourceIp<br />A0030 -> Name<br />A0031 -> QueriedEntities<br />|[update](/products/salesforce/event_examples/activity_audit_update_resource_urieventstream.json)<br />|
| C0004 | ET0033 |A0001 -> EventDate<br />A0002 -> EventIdentifier<br />A0003 -> Operation<br />A0004 -> OperationStatus<br />A0005 -> UserName<br />A0006 -> UserId<br />A0007 -> UserType<br />A0008 -> SessionKey<br />A0009 -> SourceIp<br />A0030 -> Name<br />A0031 -> QueriedEntities<br />|[delete](/products/salesforce/event_examples/activity_audit_delete_resource_urieventstream.json)<br />|


