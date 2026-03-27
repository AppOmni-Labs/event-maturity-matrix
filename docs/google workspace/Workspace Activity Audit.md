# Google Workspace - Workspace Activity Audit (0.0.1)

> Entity Name: event_source

The activity audit log provides log events for actions occurring with your Google Workspace deployment.

## References
* [Google Workspace Activity Report](https://developers.google.com/admin-sdk/reports/reference/rest)

## Retention

Based on our research, Google Workspace retains audit logs for Typically 6 months.


### Comments
Service dependant - see https://support.google.com/a/answer/7061566?hl=en


## Latency

Based on our research, Google Workspace has a latency of Near real time up to a couple hours.

### Comments
Service dependant - see https://support.google.com/a/answer/7061566?hl=en


## Licensing

Admin logs are available for all Google Workspace plans. Drive audit logs and Device events may not be available as these are not available for the Business Starter plan. Additional configuration is required to get the full set of monitoring capabilities for Devices.

## Mappings

| Category | Event Type | Attributes | Examples |
| -------- | ---------- | ---------- | -------- |
| C0001 | ET0001 |A0001 -> id.time<br />A0002 -> etag<br />A0003 -> event.name<br />A0005 -> actor.email<br />A0006 -> actor.profileId<br />A0009 -> ipAddress<br />A0013 -> ['event.name', 'event.parameters[name=login_failure_type]']<br />A0014 -> event.parameters[name=login_type]<br />|[success](/products/google workspace/event_examples/authentication_account_login.json)<br />|
| C0001 | ET0002 |A0001 -> id.time<br />A0002 -> etag<br />A0003 -> event.name<br />A0004 -> event.name<br />A0005 -> actor.email<br />A0006 -> actor.profileId<br />A0009 -> ipAddress<br />|[success](/products/google workspace/event_examples/authentication_account_logout.json)<br />|
| C0001 | ET0003 |A0001 -> id.time<br />A0002 -> etag<br />A0003 -> event.name<br />A0004 -> event.name<br />A0005 -> actor.email<br />A0006 -> actor.profileId<br />A0009 -> ipAddress<br />A0016 -> event.parameters[name=login_challenge_method]<br />A0017 -> event.parameters[name=is_suspicious]<br />A0018 -> event.name<br />|[success](/products/google workspace/event_examples/authentication_mfa_verification.json)<br />|
| C0002 | ET0004 |A0001 -> id.time<br />A0002 -> etag<br />A0003 -> event.name<br />A0005 -> actor.email<br />A0006 -> actor.profileId<br />A0007 -> actor.callerType<br />A0009 -> ipAddress<br />A0019 -> event.parameters[name=USER_EMAIL]<br />|[success](/products/google workspace/event_examples/authorization_create_user.json)<br />|
| C0002 | ET0006 |A0001 -> id.time<br />A0002 -> etag<br />A0003 -> event.name<br />A0005 -> actor.email<br />A0006 -> actor.profileId<br />A0007 -> actor.callerType<br />A0009 -> ipAddress<br />A0019 -> event.parameters[name=USER_EMAIL]<br />A0020 -> event.parameters[]<br />|[success](/products/google workspace/event_examples/authorization_update_user.json)<br />|
| C0002 | ET0007 |A0001 -> id.time<br />A0002 -> etag<br />A0003 -> event.name<br />A0005 -> actor.email<br />A0006 -> actor.profileId<br />A0007 -> actor.callerType<br />A0009 -> ipAddress<br />A0019 -> event.parameters[name=USER_EMAIL]<br />|[success](/products/google workspace/event_examples/authorization_delete_user.json)<br />|
| C0002 | ET0008 |A0001 -> id.time<br />A0002 -> etag<br />A0003 -> event.name<br />A0005 -> actor.email<br />A0006 -> actor.profileId<br />A0007 -> actor.callerType<br />A0009 -> ipAddress<br />A0021 -> event.parameters[name=GROUP_EMAIL]<br />|[success](/products/google workspace/event_examples/authorization_create_group.json)<br />|
| C0002 | ET0010 |A0001 -> id.time<br />A0002 -> etag<br />A0003 -> event.name<br />A0005 -> actor.email<br />A0006 -> actor.profileId<br />A0007 -> actor.callerType<br />A0021 -> event.parameters[name=GROUP_EMAIL]<br />A0020 -> event.parameters[name=SETTING_NAME]<br />|[success](/products/google workspace/event_examples/authorization_update_group.json)<br />|
| C0002 | ET0011 |A0001 -> id.time<br />A0002 -> etag<br />A0003 -> event.name<br />A0005 -> actor.email<br />A0006 -> actor.profileId<br />A0007 -> actor.callerType<br />A0009 -> ipAddress<br />A0021 -> event.parameters[name=GROUP_EMAIL]<br />|[success](/products/google workspace/event_examples/authorization_delete_group.json)<br />|
| C0002 | ET0012 |A0001 -> id.time<br />A0002 -> etag<br />A0003 -> event.name<br />A0005 -> actor.email<br />A0006 -> actor.profileId<br />A0007 -> actor.callerType<br />A0009 -> ipAddress<br />A0021 -> event.parameters[name=GROUP_EMAIL]<br />A0019 -> event.parameters[name=USER_EMAIL]<br />|[success](/products/google workspace/event_examples/authorization_add_to_group.json)<br />|
| C0002 | ET0013 |A0001 -> id.time<br />A0002 -> etag<br />A0003 -> event.name<br />A0005 -> actor.email<br />A0006 -> actor.profileId<br />A0007 -> actor.callerType<br />A0009 -> ipAddress<br />A0021 -> event.parameters[name=GROUP_EMAIL]<br />A0019 -> event.parameters[name=USER_EMAIL]<br />|[success](/products/google workspace/event_examples/authorization_remove_from_group.json)<br />|
| C0002 | ET0014 |A0001 -> id.time<br />A0002 -> etag<br />A0003 -> event.name<br />A0005 -> actor.email<br />A0006 -> actor.profileId<br />A0007 -> actor.callerType<br />A0009 -> ipAddress<br />A0022 -> event.parameters[name=ROLE_NAME]<br />|[success](/products/google workspace/event_examples/authorization_create_role.json)<br />|
| C0002 | ET0016 |A0001 -> id.time<br />A0002 -> etag<br />A0003 -> event.name<br />A0005 -> actor.email<br />A0006 -> actor.profileId<br />A0007 -> actor.callerType<br />A0009 -> ipAddress<br />A0022 -> event.parameters[name=ROLE_NAME]<br />A0020 -> event.parameters<br />|[success](/products/google workspace/event_examples/authorization_update_role.json)<br />|
| C0002 | ET0017 |A0001 -> id.time<br />A0002 -> etag<br />A0003 -> event.name<br />A0005 -> actor.email<br />A0006 -> actor.profileId<br />A0007 -> actor.callerType<br />A0009 -> ipAddress<br />A0022 -> event.parameters[name=ROLE_NAME]<br />|[success](/products/google workspace/event_examples/authorization_delete_role.json)<br />|
| C0002 | ET0018 |A0001 -> id.time<br />A0002 -> etag<br />A0003 -> event.name<br />A0005 -> actor.email<br />A0006 -> actor.profileId<br />A0007 -> actor.callerType<br />A0009 -> ipAddress<br />A0023 -> event.parameters[name=PRIVILEGE_NAME]<br />A0024 -> event.parameters[name=ROLE_NAME]<br />|[success](/products/google workspace/event_examples/authorization_add_permission.json)<br />|
| C0002 | ET0019 |A0001 -> id.time<br />A0002 -> etag<br />A0003 -> event.name<br />A0005 -> actor.email<br />A0006 -> actor.profileId<br />A0007 -> actor.callerType<br />A0009 -> ipAddress<br />A0023 -> event.parameters[name=PRIVILEGE_NAME]<br />A0024 -> event.parameters[name=ROLE_NAME]<br />||
| C0002 | ET0020 |A0001 -> id.time<br />A0002 -> etag<br />A0003 -> event.name<br />A0005 -> actor.email<br />A0006 -> actor.profileId<br />A0007 -> actor.callerType<br />A0009 -> ipAddress<br />A0019 -> event.parameters[name=USER_EMAIL]<br />|[success](/products/google workspace/event_examples/authorization_add_enrollment.json)<br />|
| C0002 | ET0021 |A0001 -> id.time<br />A0002 -> etag<br />A0003 -> event.name<br />A0005 -> actor.email<br />A0006 -> actor.profileId<br />A0007 -> actor.callerType<br />A0009 -> ipAddress<br />A0019 -> event.parameters[name=USER_EMAIL]<br />|[success](/products/google workspace/event_examples/authorization_remove_enrollment.json)<br />|
| C0003 | ET0022 |A0001 -> id.time<br />A0002 -> etag<br />A0003 -> event.name<br />A0005 -> actor.email<br />A0006 -> actor.profileId<br />A0026 -> event.parameters<br />A0027 -> event.parameters<br />|[success](/products/google workspace/event_examples/system_audit_create_security_configuration.json)<br />|
| C0003 | ET0024 |A0001 -> id.time<br />A0002 -> etag<br />A0003 -> event.name<br />A0005 -> actor.email<br />A0006 -> actor.profileId<br />A0007 -> actor.callerType<br />A0026 -> event.parameters[name=*]<br />A0027 -> event.parameters[name=*]<br />||
| C0003 | ET0025 |A0001 -> id.time<br />A0002 -> etag<br />A0003 -> event.name<br />A0005 -> actor.email<br />A0006 -> actor.profileId<br />A0007 -> actor.callerType<br />A0026 -> event.parameters[name=*]<br />A0027 -> event.parameters[name=*]<br />||
| C0003 | ET0026 |A0001 -> id.time<br />A0002 -> etag<br />A0003 -> event.name<br />A0005 -> actor.email<br />A0006 -> actor.profileId<br />A0007 -> actor.callerType<br />A0029 -> event.parameters[name=APPLICATION_NAME]<br />|[success](/products/google workspace/event_examples/system_audit_create_integration.json)<br />|
| C0003 | ET0028 |A0001 -> id.time<br />A0002 -> etag<br />A0003 -> event.name<br />A0005 -> actor.email<br />A0006 -> actor.profileId<br />A0007 -> actor.callerType<br />A0009 -> ipAddress<br />A0029 -> event.parameters[name=APPLICATION_NAME]<br />A0026 -> event.parameters[name=NEW_VALUE]<br />A0028 -> event.parameters[name=OLD_VALUE]<br />|[success](/products/google workspace/event_examples/system_audit_update_integration.json)<br />|
| C0003 | ET0029 |A0001 -> id.time<br />A0002 -> etag<br />A0003 -> event.name<br />A0005 -> actor.email<br />A0006 -> actor.profileId<br />A0007 -> actor.callerType<br />A0029 -> event.parameters[name=APPLICATION_NAME]<br />|[success](/products/google workspace/event_examples/system_audit_delete_integration.json)<br />|
| C0004 | ET0030 |A0001 -> id.time<br />A0002 -> etag<br />A0003 -> event.name<br />A0005 -> actor.email<br />A0006 -> actor.profileId<br />A0007 -> actor.callerType<br />A0009 -> ipAddress<br />A0030 -> event.parameters[].name<br />A0031 -> event.type<br />|[success](/products/google workspace/event_examples/audit_activity_create_resource.json)<br />|
| C0004 | ET0032 |A0001 -> id.time<br />A0002 -> etag<br />A0003 -> event.name<br />A0005 -> actor.email<br />A0006 -> actor.profileId<br />A0007 -> actor.callerType<br />A0009 -> ipAddress<br />A0030 -> event.parameters[].name<br />A0031 -> event.type<br />|[success](/products/google workspace/event_examples/audit_activity_update_resource.json)<br />|
| C0004 | ET0033 |A0001 -> id.time<br />A0002 -> etag<br />A0003 -> event.name<br />A0005 -> actor.email<br />A0006 -> actor.profileId<br />A0007 -> actor.callerType<br />A0009 -> ipAddress<br />A0030 -> event.parameters[].name<br />A0031 -> event.type<br />|[success](/products/google workspace/event_examples/audit_activity_delete_resource.json)<br />|
| C0004 | ET0034 |A0001 -> id.time<br />A0002 -> etag<br />A0003 -> event.name<br />A0005 -> actor.email<br />A0006 -> actor.profileId<br />A0009 -> ipAddress<br />A0032 -> event.parameters[].name<br />A0030 -> event.parameters[name=doc_title]<br />A0031 -> event.parameters[name=doc_type]<br />|[success](/products/google workspace/event_examples/audit_activity_download_resource.json)<br />|
| C0004 | ET0035 |A0001 -> id.time<br />A0002 -> etag<br />A0003 -> event.name<br />A0005 -> actor.email<br />A0006 -> actor.profileId<br />A0009 -> ipAddress<br />A0033 -> event.parameters[name=user_query]<br />|[success](/products/google workspace/event_examples/audit_activity_query_resource.json)<br />|


