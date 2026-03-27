# Salesforce - EventLogFile Search Event Type (1.0.0)

> Entity Name: event_source

Tracks Salesforce search requests, including the search string and result counts.

## References
* [EventLogFile Search Event](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_eventlogfile_search.htm)

## Retention

Based on our research, Salesforce retains audit logs for 1 Day.


### Comments
Available for free with 1 day retention, otherwise requires an add-on subscription for 30 day retention.


## Latency

Based on our research, Salesforce has a latency of 3 Hours.

### Comments
Event log files are accessible via hourly and 24 hour log files. It can take between 3–6 hours from the time of the event to be available in the hourly log file.


## Licensing

Available for free with 1 day retention, otherwise requires Salesforce Shield or a Salesforce Event Monitoring add-on subscription.

## Mappings

| Category | Event Type | Attributes | Examples |
| -------- | ---------- | ---------- | -------- |
| C0004 | ET0035 |A0001 -> TIMESTAMP_DERIVED<br />A0003 -> EVENT_TYPE<br />A0006 -> USER_ID<br />A0033 -> SEARCH_QUERY<br />|[success](/products/salesforce/event_examples/salesforce_elf_search_event/activity_audit_query_resource_elf_search.json)<br />|


