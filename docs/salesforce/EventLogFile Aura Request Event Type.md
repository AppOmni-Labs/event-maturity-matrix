# Salesforce - EventLogFile Aura Request Event Type (0.0.1)

> Entity Name: event_source

Provides details of requests to Apex methods from Aura and Lightning web components.

## References
* [EventLogFile Aura Request Event](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_eventlogfile_lightning_component.htm)

## Retention

Based on our research, Salesforce retains audit logs for 30 Days.


### Comments
N/A


## Latency

Based on our research, Salesforce has a latency of 3 Hours.

### Comments
Event log files are accessible via hourly and 24 hour log files. It can take between 3–6 hours from the time of the event to be available in the hourly log file.


## Licensing

Requires Salesforce Shield or a Salesforce Event Monitoring add-on subscription.

## Mappings

| Category | Event Type | Attributes | Examples |
| -------- | ---------- | ---------- | -------- |
| C0004 | ET0030 |A0001 -> TIMESTAMP_DERIVED<br />A0003 -> EVENT_TYPE<br />A0004 -> REQUEST_STATUS<br />A0006 -> USER_ID<br />A0007 -> USER_TYPE<br />A0008 -> SESSION_KEY<br />A0009 -> CLIENT_IP<br />A0011 -> USER_AGENT<br />A0030 -> ACTION_MESSAGE<br />|[create](/products/salesforce/event_examples/activity_audit_create_resource_aurarequest.json)<br />|
| C0004 | ET0031 |A0001 -> TIMESTAMP_DERIVED<br />A0003 -> EVENT_TYPE<br />A0004 -> REQUEST_STATUS<br />A0006 -> USER_ID<br />A0007 -> USER_TYPE<br />A0008 -> SESSION_KEY<br />A0009 -> CLIENT_IP<br />A0011 -> USER_AGENT<br />A0030 -> ACTION_MESSAGE<br />|[read](/products/salesforce/event_examples/activity_audit_read_resource_aurarequest.json)<br />|
| C0004 | ET0032 |A0001 -> TIMESTAMP_DERIVED<br />A0003 -> EVENT_TYPE<br />A0004 -> REQUEST_STATUS<br />A0006 -> USER_ID<br />A0007 -> USER_TYPE<br />A0008 -> SESSION_KEY<br />A0009 -> CLIENT_IP<br />A0011 -> USER_AGENT<br />A0030 -> ACTION_MESSAGE<br />|[update](/products/salesforce/event_examples/activity_audit_update_resource_aurarequest.json)<br />|
| C0004 | ET0033 |A0001 -> TIMESTAMP_DERIVED<br />A0003 -> EVENT_TYPE<br />A0004 -> REQUEST_STATUS<br />A0006 -> USER_ID<br />A0007 -> USER_TYPE<br />A0008 -> SESSION_KEY<br />A0009 -> CLIENT_IP<br />A0011 -> USER_AGENT<br />A0030 -> ACTION_MESSAGE<br />|[delete](/products/salesforce/event_examples/activity_audit_delete_resource_aurarequest.json)<br />|


