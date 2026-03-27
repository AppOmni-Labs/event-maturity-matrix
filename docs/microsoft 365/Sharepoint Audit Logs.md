# Microsoft 365 - Sharepoint Audit Logs (1.0.0)

> Entity Name: event_source

Includes logs for Sharepoint and OneDrive.

## References
* [SharePoint Base Schema](https://learn.microsoft.com/en-us/office/office-365-management-api/office-365-management-activity-api-schema#sharepoint-base-schema)

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
| C0001 | ET0001 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0005 -> UserId<br />A0008 -> AppAccessContext.AADSessionId<br />A0009 -> ClientIP<br />A0011 -> UserAgent<br />A0012 -> Platform<br />|[success](/products/microsoft 365/event_examples/sharepoint/authentication_account_login.json)<br />|
| C0002 | ET0012 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0005 -> UserId<br />A0008 -> AppAccessContext.AADSessionId<br />A0009 -> ClientIP<br />A0011 -> UserAgent<br />A0012 -> Platform<br />A0021 -> EventData<br />A0019 -> TargetUserOrGroupName<br />|[success](/products/microsoft 365/event_examples/sharepoint/authorization_add_member_to_group.json)<br />|
| C0002 | ET0013 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0005 -> UserId<br />A0008 -> AppAccessContext.AADSessionId<br />A0009 -> ClientIP<br />A0011 -> UserAgent<br />A0012 -> Platform<br />A0021 -> EventData<br />A0019 -> TargetUserOrGroupName<br />|[success](/products/microsoft 365/event_examples/sharepoint/authorization_remove_member_from_group.json)<br />|
| C0002 | ET0018 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0005 -> UserId<br />A0008 -> AppAccessContext.AADSessionId<br />A0009 -> ClientIP<br />A0011 -> UserAgent<br />A0012 -> Platform<br />A0023 -> TargetUserOrGroupType<br />A0024 -> TargetUserOrGroupName<br />|[success](/products/microsoft 365/event_examples/sharepoint/authorization_add_permission.json)<br />|
| C0002 | ET0019 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0005 -> UserId<br />A0008 -> AppAccessContext.AADSessionId<br />A0009 -> ClientIP<br />A0011 -> UserAgent<br />A0012 -> Platform<br />A0023 -> TargetUserOrGroupType<br />A0024 -> TargetUserOrGroupName<br />|[success](/products/microsoft 365/event_examples/sharepoint/authorization_remove_permission.json)<br />|
| C0003 | ET0024 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0005 -> UserId<br />A0009 -> ClientIP<br />A0011 -> UserAgent<br />A0026 -> ModifiedProperties<br />A0027 -> ModifiedProperties<br />A0028 -> ModifiedProperties<br />|[success](/products/microsoft 365/event_examples/sharepoint/system_audit_update_security_configuration.json)<br />|
| C0004 | ET0030 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0005 -> UserId<br />A0008 -> AppAccessContext.AADSessionId<br />A0009 -> ClientIP<br />A0011 -> UserAgent<br />A0012 -> Platform<br />A0030 -> EventData<br />A0031 -> ItemType<br />|[success](/products/microsoft 365/event_examples/sharepoint/activity_audit_create_resource_site.json)<br />|
| C0004 | ET0031 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0005 -> UserId<br />A0008 -> AppAccessContext.AADSessionId<br />A0009 -> ClientIP<br />A0011 -> UserAgent<br />A0012 -> Platform<br />A0030 -> ObjectId<br />A0031 -> ItemType<br />|[success](/products/microsoft 365/event_examples/sharepoint/activity_audit_read_resource_page.json)<br />|
| C0004 | ET0033 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0005 -> UserId<br />A0009 -> ClientIP<br />A0011 -> UserAgent<br />A0030 -> ObjectId<br />A0031 -> ItemType<br />|[success](/products/microsoft 365/event_examples/sharepoint/activity_audit_delete_resource_site.json)<br />|
| C0004 | ET0034 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0005 -> UserId<br />A0008 -> AppAccessContext.AADSessionId<br />A0009 -> ClientIP<br />A0011 -> UserAgent<br />A0012 -> Platform<br />A0030 -> ItemType<br />|[success](/products/microsoft 365/event_examples/sharepoint/activity_audit_download_resource_file.json)<br />|
| C0004 | ET0035 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> UserType<br />A0009 -> ClientIP<br />A0030 -> QuerySource<br />A0033 -> QueryText<br />|[success](/products/microsoft 365/event_examples/sharepoint/activity_audit_query_resource.json)<br />|


