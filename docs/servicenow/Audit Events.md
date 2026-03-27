# ServiceNow - Audit Events (0.0.1)

> Entity Name: event_source

ServiceNow audit events track changes to records in audited tables.

## References
* [Viewing Sys Audit and Audit Relationship Change tables](https://docs.servicenow.com/bundle/vancouver-platform-security/page/administer/security/concept/c_UnderstandingTheSysAuditTable.html)

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
| C0004 | ET0032 |A0001 -> sys_created_on<br />A0003 -> fieldname<br />A0005 -> user<br />A0030 -> tablename<br />|[update](/products/servicenow/event_examples/audit/activity_audit_update_resource.json)<br />|
| C0004 | ET0033 |A0001 -> sys_created_on<br />A0003 -> fieldname<br />A0005 -> user<br />A0030 -> tablename<br />|[delete](/products/servicenow/event_examples/audit/activity_audit_delete_resource.json)<br />|


