# Workday - User Activity Logs (1.0.0)

> Entity Name: event_source

Workday user activity logs provide an audit trail of user activity over a certain time period.

## References
* [Workday Activity Log Schema](https://doc.workday.com/admin-guide/en-us/human-capital-management/unv1636547598141.html)

## Retention

Based on our research, Workday retains audit logs for 30 days.


### Comments
By default, the User Activity Logging REST API retains log entries for 30 days.


## Latency

Based on our research, Workday has a latency of Near real-time.

### Comments
N/A


## Licensing

User Activity Logging is available to Workday customers.

## Mappings

| Category | Event Type | Attributes | Examples |
| -------- | ---------- | ---------- | -------- |
| C0002 | ET0004 |A0001 -> requestTime<br />A0003 -> taskDisplayName<br />A0004 -> activityAction<br />A0005 -> systemAccount<br />A0008 -> sessionId<br />A0009 -> ipAddress<br />A0011 -> userAgent<br />A0012 -> deviceType<br />A0019 -> target.descriptor<br />|[success](/products/workday/event_examples/authorization_create_user.json)<br />|
| C0002 | ET0005 |A0001 -> requestTime<br />A0003 -> taskDisplayName<br />A0004 -> activityAction<br />A0005 -> systemAccount<br />A0008 -> sessionId<br />A0009 -> ipAddress<br />A0011 -> userAgent<br />A0012 -> deviceType<br />A0019 -> target.descriptor<br />|[success](/products/workday/event_examples/authorization_read_user.json)<br />|
| C0002 | ET0006 |A0001 -> requestTime<br />A0003 -> taskDisplayName<br />A0004 -> activityAction<br />A0005 -> systemAccount<br />A0008 -> sessionId<br />A0009 -> ipAddress<br />A0011 -> userAgent<br />A0012 -> deviceType<br />A0019 -> target.descriptor<br />|[success](/products/workday/event_examples/authorization_update_user.json)<br />|
| C0002 | ET0008 |A0001 -> requestTime<br />A0003 -> taskDisplayName<br />A0004 -> activityAction<br />A0005 -> systemAccount<br />A0008 -> sessionId<br />A0009 -> ipAddress<br />A0011 -> userAgent<br />A0012 -> deviceType<br />A0021 -> target.descriptor<br />|[success](/products/workday/event_examples/authorization_create_group.json)<br />|
| C0002 | ET0009 |A0001 -> requestTime<br />A0003 -> taskDisplayName<br />A0004 -> activityAction<br />A0005 -> systemAccount<br />A0008 -> sessionId<br />A0009 -> ipAddress<br />A0011 -> userAgent<br />A0012 -> deviceType<br />A0021 -> target.descriptor<br />|[success](/products/workday/event_examples/authorization_read_group.json)<br />|
| C0002 | ET0010 |A0001 -> requestTime<br />A0003 -> taskDisplayName<br />A0004 -> activityAction<br />A0005 -> systemAccount<br />A0008 -> sessionId<br />A0009 -> ipAddress<br />A0011 -> userAgent<br />A0012 -> deviceType<br />A0021 -> target.descriptor<br />|[success](/products/workday/event_examples/authorization_update_group.json)<br />|
| C0002 | ET0011 |A0001 -> requestTime<br />A0003 -> taskDisplayName<br />A0004 -> activityAction<br />A0005 -> systemAccount<br />A0008 -> sessionId<br />A0009 -> ipAddress<br />A0011 -> userAgent<br />A0012 -> deviceType<br />|[success](/products/workday/event_examples/authorization_delete_group.json)<br />|
| C0002 | ET0012 |A0001 -> requestTime<br />A0003 -> taskDisplayName<br />A0004 -> activityAction<br />A0005 -> systemAccount<br />A0008 -> sessionId<br />A0009 -> ipAddress<br />A0011 -> userAgent<br />A0012 -> deviceType<br />A0021 -> target.descriptor<br />|[success](/products/workday/event_examples/authorization_add_to_group.json)<br />|
| C0002 | ET0013 |A0001 -> requestTime<br />A0003 -> taskDisplayName<br />A0004 -> activityAction<br />A0005 -> systemAccount<br />A0008 -> sessionId<br />A0009 -> ipAddress<br />A0011 -> userAgent<br />A0012 -> deviceType<br />A0021 -> target.descriptor<br />|[success](/products/workday/event_examples/authorization_remove_from_group.json)<br />|
| C0002 | ET0015 |A0001 -> requestTime<br />A0003 -> taskDisplayName<br />A0004 -> activityAction<br />A0005 -> systemAccount<br />A0008 -> sessionId<br />A0009 -> ipAddress<br />A0011 -> userAgent<br />A0012 -> deviceType<br />|[success](/products/workday/event_examples/authorization_read_role.json)<br />|
| C0002 | ET0016 |A0001 -> requestTime<br />A0003 -> taskDisplayName<br />A0004 -> activityAction<br />A0005 -> systemAccount<br />A0008 -> sessionId<br />A0009 -> ipAddress<br />A0011 -> userAgent<br />A0012 -> deviceType<br />A0022 -> target.descriptor<br />|[success](/products/workday/event_examples/authorization_update_role.json)<br />|
| C0002 | ET0018 |A0001 -> requestTime<br />A0003 -> taskDisplayName<br />A0004 -> activityAction<br />A0005 -> systemAccount<br />A0008 -> sessionId<br />A0009 -> ipAddress<br />A0011 -> userAgent<br />A0012 -> deviceType<br />A0024 -> target.descriptor<br />|[success](/products/workday/event_examples/authorization_add_permission.json)<br />|
| C0002 | ET0019 |A0001 -> requestTime<br />A0003 -> taskDisplayName<br />A0004 -> activityAction<br />A0005 -> systemAccount<br />A0008 -> sessionId<br />A0009 -> ipAddress<br />A0011 -> userAgent<br />A0012 -> deviceType<br />A0024 -> target.descriptor<br />|[success](/products/workday/event_examples/authorization_remove_permission.json)<br />|
| C0002 | ET0020 |A0001 -> requestTime<br />A0003 -> taskDisplayName<br />A0004 -> activityAction<br />A0005 -> systemAccount<br />A0008 -> sessionId<br />A0009 -> ipAddress<br />A0011 -> userAgent<br />A0012 -> deviceType<br />A0025 -> taskDisplayName<br />|[success](/products/workday/event_examples/authorization_add_enrollment.json)<br />|
| C0002 | ET0021 |A0001 -> requestTime<br />A0003 -> taskDisplayName<br />A0004 -> activityAction<br />A0005 -> systemAccount<br />A0008 -> sessionId<br />A0009 -> ipAddress<br />A0011 -> userAgent<br />A0012 -> deviceType<br />A0025 -> taskDisplayName<br />|[success](/products/workday/event_examples/authorization_remove_enrollment.json)<br />|
| C0003 | ET0022 |A0001 -> requestTime<br />A0003 -> taskDisplayName<br />A0004 -> activityAction<br />A0005 -> systemAccount<br />A0008 -> sessionId<br />A0009 -> ipAddress<br />A0011 -> userAgent<br />A0012 -> deviceType<br />A0026 -> target.descriptor<br />|[success](/products/workday/event_examples/system_audit_create_security_configuration.json)<br />|
| C0003 | ET0023 |A0001 -> requestTime<br />A0003 -> taskDisplayName<br />A0004 -> activityAction<br />A0005 -> systemAccount<br />A0008 -> sessionId<br />A0009 -> ipAddress<br />A0011 -> userAgent<br />A0012 -> deviceType<br />A0027 -> target.descriptor<br />|[success](/products/workday/event_examples/system_audit_read_security_configuration.json)<br />|
| C0003 | ET0024 |A0001 -> requestTime<br />A0003 -> taskDisplayName<br />A0004 -> activityAction<br />A0005 -> systemAccount<br />A0008 -> sessionId<br />A0009 -> ipAddress<br />A0011 -> userAgent<br />A0012 -> deviceType<br />A0026 -> target.descriptor<br />|[success](/products/workday/event_examples/system_audit_update_security_configuration.json)<br />|
| C0003 | ET0025 |A0001 -> requestTime<br />A0003 -> taskDisplayName<br />A0004 -> activityAction<br />A0005 -> systemAccount<br />A0008 -> sessionId<br />A0009 -> ipAddress<br />A0011 -> userAgent<br />A0012 -> deviceType<br />A0026 -> target.descriptor<br />|[success](/products/workday/event_examples/system_audit_delete_security_configuration.json)<br />|
| C0003 | ET0026 |A0001 -> requestTime<br />A0003 -> taskDisplayName<br />A0004 -> activityAction<br />A0005 -> systemAccount<br />A0008 -> sessionId<br />A0009 -> ipAddress<br />A0011 -> userAgent<br />A0012 -> deviceType<br />A0029 -> target.descriptor<br />|[success](/products/workday/event_examples/system_audit_create_integration.json)<br />|
| C0003 | ET0027 |A0001 -> requestTime<br />A0003 -> taskDisplayName<br />A0004 -> activityAction<br />A0005 -> systemAccount<br />A0008 -> sessionId<br />A0009 -> ipAddress<br />A0011 -> userAgent<br />A0012 -> deviceType<br />|[success](/products/workday/event_examples/system_audit_read_integration.json)<br />|
| C0003 | ET0028 |A0001 -> requestTime<br />A0003 -> taskDisplayName<br />A0004 -> activityAction<br />A0005 -> systemAccount<br />A0008 -> sessionId<br />A0009 -> ipAddress<br />A0011 -> userAgent<br />A0012 -> deviceType<br />A0029 -> target.descriptor<br />|[success](/products/workday/event_examples/system_audit_update_integration.json)<br />|
| C0004 | ET0030 |A0001 -> requestTime<br />A0003 -> taskDisplayName<br />A0004 -> activityAction<br />A0005 -> systemAccount<br />A0008 -> sessionId<br />A0009 -> ipAddress<br />A0011 -> userAgent<br />A0012 -> deviceType<br />A0030 -> target.descriptor<br />|[success](/products/workday/event_examples/activity_audit_create_resource.json)<br />|
| C0004 | ET0031 |A0001 -> requestTime<br />A0003 -> taskDisplayName<br />A0004 -> activityAction<br />A0005 -> systemAccount<br />A0008 -> sessionId<br />A0009 -> ipAddress<br />A0011 -> userAgent<br />A0012 -> deviceType<br />A0030 -> target.descriptor<br />|[success](/products/workday/event_examples/activity_audit_read_resource.json)<br />|
| C0004 | ET0032 |A0001 -> requestTime<br />A0003 -> taskDisplayName<br />A0004 -> activityAction<br />A0005 -> systemAccount<br />A0008 -> sessionId<br />A0009 -> ipAddress<br />A0011 -> userAgent<br />A0012 -> deviceType<br />A0030 -> target.descriptor<br />|[success](/products/workday/event_examples/activity_audit_update_resource.json)<br />|
| C0004 | ET0033 |A0001 -> requestTime<br />A0003 -> taskDisplayName<br />A0004 -> activityAction<br />A0005 -> systemAccount<br />A0008 -> sessionId<br />A0009 -> ipAddress<br />A0011 -> userAgent<br />A0012 -> deviceType<br />|[success](/products/workday/event_examples/activity_audit_delete_resource.json)<br />|
| C0004 | ET0034 |A0001 -> requestTime<br />A0004 -> taskDisplayName<br />A0005 -> systemAccount<br />A0008 -> sessionId<br />A0009 -> ipAddress<br />A0011 -> userAgent<br />A0012 -> deviceType<br />A0030 -> target.descriptor<br />|[success](/products/workday/event_examples/activity_audit_delete_resource.json)<br />|


