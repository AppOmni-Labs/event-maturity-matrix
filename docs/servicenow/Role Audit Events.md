# ServiceNow - Role Audit Events (0.0.1)

> Entity Name: event_source

The ServiceNow role audit table contains user role assignments.

## References
* [Enable role auditing](https://docs.servicenow.com/bundle/utah-platform-security/page/administer/roles/task/enable-audit-roles.html)

## Retention

Based on our research, ServiceNow retains audit logs for Infinite.


### Comments
Can be changed by an instance admin.


## Latency

Based on our research, ServiceNow has a latency of Near Real-Time.

### Comments
Can vary based on system conditions and configurations.


## Licensing

Must be enabled and configured by an instance admin.

## Mappings

| Category | Event Type | Attributes | Examples |
| -------- | ---------- | ---------- | -------- |
| C0002 | ET0018 |A0001 -> sys_created_on<br />A0003 -> operation<br />A0005 -> user\.name<br />A0006 -> user\.name<br />|[add](/products/servicenow/event_examples/audit_role/authorization_add_permission.json)<br />|
| C0002 | ET0019 |A0001 -> sys_created_on<br />A0003 -> operation<br />A0005 -> user\.name<br />A0006 -> user\.name<br />|[add](/products/servicenow/event_examples/audit_role/authorization_remove_permission.json)<br />|


