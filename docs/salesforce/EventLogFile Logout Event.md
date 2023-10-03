# Salesforce - EventLogFile Logout Event (0.0.1)

> Entity Name: event_source

This event source is to track logout events in Salesforce.

## References
* [EventLogFile Logout Event](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_eventlogfile_logout.htm)

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
| C0001 | ET0002 |A0001 -> TIMESTAMP_DERIVED<br />A0003 -> EVENT_TYPE<br />A0006 -> USER_ID<br />A0007 -> USER_TYPE<br />A0008 -> LOGIN_KEY<br />A0009 -> CLIENT_IP<br />A0011 -> BROWSER_TYPE<br />A0012 -> PLATFORM_TYPE<br />|[success](/products/salesforce/event_examples/authentication_account_logout_elf.json)<br />|


