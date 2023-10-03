# Salesforce - EventLogFile SOAP API Event Type (0.0.1)

> Entity Name: event_source

Provides details about a Salesforce org's SOAP API request activity.

## References
* [EventLogFile SOAP API](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_eventlogfile_api.htm)

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
| C0004 | ET0030 |A0001 -> TIMESTAMP_DERIVED<br />A0003 -> EVENT_TYPE<br />A0004 -> REQUEST_STATUS<br />A0006 -> USER_ID<br />A0007 -> USER_TYPE<br />A0008 -> SESSION_KEY<br />A0009 -> CLIENT_IP<br />A0012 -> API_TYPE<br />A0031 -> ENTITY_NAME<br />|[create](/products/salesforce/event_examples/activity_audit_create_resource_soapapi.json)<br />|
| C0004 | ET0031 |A0001 -> TIMESTAMP_DERIVED<br />A0003 -> EVENT_TYPE<br />A0004 -> REQUEST_STATUS<br />A0006 -> USER_ID<br />A0007 -> USER_TYPE<br />A0008 -> SESSION_KEY<br />A0009 -> CLIENT_IP<br />A0012 -> API_TYPE<br />A0031 -> ENTITY_NAME<br />|[read](/products/salesforce/event_examples/activity_audit_read_resource_soapapi.json)<br />|
| C0004 | ET0032 |A0001 -> TIMESTAMP_DERIVED<br />A0003 -> EVENT_TYPE<br />A0004 -> REQUEST_STATUS<br />A0006 -> USER_ID<br />A0007 -> USER_TYPE<br />A0008 -> SESSION_KEY<br />A0009 -> CLIENT_IP<br />A0012 -> API_TYPE<br />A0031 -> ENTITY_NAME<br />|[update](/products/salesforce/event_examples/activity_audit_update_resource_soapapi.json)<br />|
| C0004 | ET0033 |A0001 -> TIMESTAMP_DERIVED<br />A0003 -> EVENT_TYPE<br />A0004 -> REQUEST_STATUS<br />A0006 -> USER_ID<br />A0007 -> USER_TYPE<br />A0008 -> SESSION_KEY<br />A0009 -> CLIENT_IP<br />A0012 -> API_TYPE<br />A0031 -> ENTITY_NAME<br />|[delete](/products/salesforce/event_examples/activity_audit_delete_resource_soapapi.json)<br />|
| C0004 | ET0034 |A0001 -> TIMESTAMP_DERIVED<br />A0003 -> EVENT_TYPE<br />A0004 -> REQUEST_STATUS<br />A0006 -> USER_ID<br />A0007 -> USER_TYPE<br />A0008 -> SESSION_KEY<br />A0009 -> CLIENT_IP<br />A0012 -> API_TYPE<br />A0032 -> ROWS_PROCESSED<br />A0031 -> ENTITY_NAME<br />|[download](/products/salesforce/event_examples/activity_audit_download_resource_soapapi.json)<br />|


