# ServiceNow - Export Events (0.0.1)

> Entity Name: event_source

ServiceNow Instance Security Center export events track UI exports of record data.

## References
* [Monitor security events](https://docs.servicenow.com/bundle/washingtondc-platform-security/page/administer/security/concept/instance-sec-center-event-ribbon.html)

## Retention

Based on our research, ServiceNow retains audit logs for Infinite.


### Comments
Can be changed by an instance admin.


## Latency

Based on our research, ServiceNow has a latency of Near Real-Time.

### Comments
Can vary based on system conditions and configurations.


## Licensing

Included with ServiceNow instances.

## Mappings

| Category | Event Type | Attributes | Examples |
| -------- | ---------- | ---------- | -------- |
| C0004 | ET0034 |A0001 -> sys_created_on<br />A0002 -> event<br />A0003 -> sys_class_name<br />A0005 -> user_name<br />A0006 -> user<br />A0030 -> table<br />|[download](/products/servicenow/event_examples/export/activity_audit_download_resource.json)<br />|


