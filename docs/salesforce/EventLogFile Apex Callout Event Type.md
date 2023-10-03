# Salesforce - EventLogFile Apex Callout Event Type (0.0.1)

> Entity Name: event_source

Provides details about callouts (external requests) during Apex code execution.

## References
* [EventLogFile Apex Event](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_eventlogfile_apexcallout.htm)

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
| C0004 | ET0031 |A0001 -> TIMESTAMP_DERIVED<br />A0003 -> EVENT_TYPE<br />A0004 -> SUCCESS<br />A0008 -> SESSION_KEY<br />A0009 -> CLIENT_IP<br />A0012 -> TYPE<br />A0030 -> URL<br />|[success](/products/salesforce/event_examples/activity_audit_read_resource_apexcallout.json)<br />|


