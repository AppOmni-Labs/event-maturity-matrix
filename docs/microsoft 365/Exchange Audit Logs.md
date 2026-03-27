# Microsoft 365 - Exchange Audit Logs (1.0.0)

> Entity Name: event_source

Includes logs for Exchange administration and mailbox activities.

## References
* [Exchange Admin Schema](https://learn.microsoft.com/en-us/office/office-365-management-api/office-365-management-activity-api-schema#exchange-admin-schema)
* [Exchange Mailbox Schema](https://learn.microsoft.com/en-us/office/office-365-management-api/office-365-management-activity-api-schema#exchange-mailbox-schema)

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
| C0001 | ET0001 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0005 -> UserId<br />A0006 -> LogonUserSid<br />A0007 -> UserType<br />A0008 -> SessionId<br />A0009 -> ClientIP<br />A0011 -> ClientInfoString<br />A0012 -> ClientInfoString<br />|[success](/products/microsoft 365/event_examples/exchange/authentication_account_login.json)<br />|
| C0002 | ET0008 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0004 -> ResultStatus<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> UserType<br />A0008 -> SessionId<br />A0009 -> ClientIP<br />A0021 -> Parameters[Name=DisplayName].Value<br />|[success](/products/microsoft 365/event_examples/exchange/authorization_create_group_distro.json)<br />|
| C0002 | ET0010 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0004 -> ResultStatus<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> UserType<br />A0008 -> SessionId<br />A0009 -> ClientIP<br />A0021 -> Parameters[Name=DisplayName].Value<br />|[success](/products/microsoft 365/event_examples/exchange/authorization_update_group_distro.json)<br />|
| C0002 | ET0011 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0004 -> ResultStatus<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> UserType<br />A0008 -> SessionId<br />A0009 -> ClientIP<br />|[success](/products/microsoft 365/event_examples/exchange/authorization_delete_group_distro.json)<br />|
| C0002 | ET0012 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0004 -> ResultStatus<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> UserType<br />A0008 -> SessionId<br />A0009 -> ClientIP<br />|[success](/products/microsoft 365/event_examples/exchange/authorization_add_to_group_distro.json)<br />|
| C0002 | ET0013 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0004 -> ResultStatus<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> UserType<br />A0008 -> SessionId<br />A0009 -> ClientIP<br />|[success](/products/microsoft 365/event_examples/exchange/authorization_remove_from_group_distro.json)<br />|
| C0002 | ET0014 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0004 -> ResultStatus<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> UserType<br />A0008 -> SessionId<br />A0009 -> ClientIP<br />A0022 -> Parameters.Name<br />|[success](/products/microsoft 365/event_examples/exchange/authorization_create_role.json)<br />|
| C0002 | ET0016 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0004 -> ResultStatus<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> UserType<br />A0008 -> SessionId<br />A0009 -> ClientIP<br />A0022 -> Parameters.Name<br />|[success](/products/microsoft 365/event_examples/exchange/authorization_update_role.json)<br />|
| C0002 | ET0017 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0004 -> ResultStatus<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> UserType<br />A0008 -> SessionId<br />A0009 -> ClientIP<br />|[success](/products/microsoft 365/event_examples/exchange/authorization_delete_role.json)<br />|
| C0002 | ET0018 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0004 -> ResultStatus<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> UserType<br />A0008 -> SessionId<br />A0009 -> ClientIP<br />|[success](/products/microsoft 365/event_examples/exchange/authorization_add_permission.json)<br />|
| C0002 | ET0019 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0004 -> ResultStatus<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> UserType<br />A0008 -> SessionId<br />A0009 -> ClientIP<br />A0023 -> ObjectId<br />|[success](/products/microsoft 365/event_examples/exchange/authorization_remove_permission.json)<br />|
| C0003 | ET0022 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0004 -> ResultStatus<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> UserType<br />A0008 -> SessionId<br />A0009 -> ClientIP<br />A0026 -> Parameters.Name<br />A0027 -> Parameters.Value<br />|[success](/products/microsoft 365/event_examples/exchange/system_audit_create_security_configuration_spam.json)<br />|
| C0003 | ET0024 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0004 -> ResultStatus<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> UserType<br />A0008 -> SessionId<br />A0009 -> ClientIP<br />A0026 -> Parameters.Name<br />A0027 -> Parameters.Value<br />|[success](/products/microsoft 365/event_examples/exchange/system_audit_update_security_configuration_spam.json)<br />|
| C0003 | ET0025 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0004 -> ResultStatus<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> UserType<br />A0008 -> SessionId<br />A0009 -> ClientIP<br />A0026 -> Parameters.Name<br />|[success](/products/microsoft 365/event_examples/exchange/system_audit_delete_security_configuration_spam.json)<br />|
| C0003 | ET0026 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0004 -> ResultStatus<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> UserType<br />A0008 -> SessionId<br />A0009 -> ClientIP<br />A0029 -> AppId<br />|[success](/products/microsoft 365/event_examples/exchange/system_audit_create_integration.json)<br />|
| C0003 | ET0028 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0004 -> ResultStatus<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> UserType<br />A0008 -> SessionId<br />A0009 -> ClientIP<br />A0029 -> AppId<br />|[success](/products/microsoft 365/event_examples/exchange/system_audit_update_integration.json)<br />|
| C0003 | ET0029 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0004 -> ResultStatus<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> UserType<br />A0008 -> SessionId<br />A0009 -> ClientIP<br />A0029 -> AppId<br />|[success](/products/microsoft 365/event_examples/exchange/system_audit_delete_integration.json)<br />|
| C0004 | ET0030 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0004 -> ResultStatus<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> UserType<br />A0008 -> SessionId<br />A0009 -> ClientIP<br />A0030 -> Item<br />A0031 -> Item.Subject<br />|[success - email](/products/microsoft 365/event_examples/exchange/activity_audit_create_resource_msg.json)<br />[success - calendar](/products/microsoft 365/event_examples/exchange/activity_audit_create_resource_calendar.json)<br />|
| C0004 | ET0031 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0004 -> ResultStatus<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> UserType<br />A0008 -> SessionId<br />A0009 -> ClientIPAddress<br />A0030 -> OperationProperties<br />A0031 -> Operation<br />|[success](/products/microsoft 365/event_examples/exchange/activity_audit_read_resource.json)<br />|
| C0004 | ET0032 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0004 -> ResultStatus<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> UserType<br />A0008 -> SessionId<br />A0009 -> ClientIP<br />|[success](/products/microsoft 365/event_examples/exchange/activity_audit_update_resource_calendar.json)<br />|
| C0004 | ET0033 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0004 -> ResultStatus<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> UserType<br />A0008 -> SessionId<br />A0009 -> ClientIP<br />A0030 -> AffectedItems<br />A0031 -> AffectedItems<br />|[success - email](/products/microsoft 365/event_examples/exchange/activity_audit_delete_resource_msg.json)<br />[success - calendar](/products/microsoft 365/event_examples/exchange/activity_audit_delete_resource_calendar.json)<br />|
| C0004 | ET0035 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> UserType<br />A0009 -> ClientIP<br />A0030 -> QuerySource<br />A0033 -> QueryText<br />|[success](/products/microsoft 365/event_examples/exchange/activity_audit_query_resource.json)<br />|


