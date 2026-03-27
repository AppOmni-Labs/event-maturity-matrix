# Microsoft 365 - General Audit Logs (1.0.0)

> Entity Name: event_source

Includes workloads not included in other audit log types.

## References
* [Common Audit Schema](https://learn.microsoft.com/en-us/office/office-365-management-api/office-365-management-activity-api-schema#common-schema)

## Retention

Based on our research, Microsoft 365 retains audit logs for 180 days.


### Comments
Minimum retention is 180 days, but organizations can set a retention policy up to 10 years dependent on licensing, reference https://learn.microsoft.com/en-us/purview/audit-log-retention-policies


## Latency

Based on our research, Microsoft 365 has a latency of Typically 60 to 90 minutes after an event occurs..

### Comments
Microsoft does not provide a specific audit logging latency SLA, reference https://learn.microsoft.com/en-us/purview/audit-search?view=o365-worldwide&tabs=microsoft-purview-portal


## Licensing

Standard and Premium audit licenses are available, with log availability and retention dependent on the license level. For more information, see https://learn.microsoft.com/en-us/purview/audit-search?view=o365-worldwide&tabs=microsoft-purview-portal

## Mappings

| Category | Event Type | Attributes | Examples |
| -------- | ---------- | ---------- | -------- |
| C0002 | ET0008 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0006 -> UserKey<br />A0007 -> UserId<br />A0021 -> TeamName<br />|[success](/products/microsoft 365/event_examples/general/authorization_create_group.json)<br />|
| C0002 | ET0010 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0021 -> TeamName<br />A0020 -> NewValue<br />|[success](/products/microsoft 365/event_examples/general/authorization_update_group.json)<br />|
| C0002 | ET0011 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0021 -> TeamName<br />|[success](/products/microsoft 365/event_examples/general/authorization_delete_group.json)<br />|
| C0002 | ET0012 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0021 -> TeamName<br />A0019 -> Members.DisplayName<br />|[success](/products/microsoft 365/event_examples/general/authorization_add_member_to_group.json)<br />|
| C0002 | ET0013 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0021 -> TeamName<br />A0019 -> Members.DisplayName<br />|[success](/products/microsoft 365/event_examples/general/authorization_remove_member_from_group.json)<br />|
| C0003 | ET0026 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0029 -> AddOnName<br />|[success](/products/microsoft 365/event_examples/general/system_audit_create_integration.json)<br />|
| C0003 | ET0029 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0005 -> UserId<br />A0006 -> UserKey<br />|[success](/products/microsoft 365/event_examples/general/system_audit_delete_integration.json)<br />|
| C0004 | ET0030 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0031 -> ExtraProperties<br />|[success](/products/microsoft 365/event_examples/general/activity_audit_create_resource.json)<br />|
| C0004 | ET0033 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0009 -> ClientIP<br />|[success](/products/microsoft 365/event_examples/general/activity_audit_delete_resource.json)<br />|


