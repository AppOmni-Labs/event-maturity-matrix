# Slack - Enterprise Audit Logs (0.0.1)

> Entity Name: event_source

Slack enterprise audit logs that provide an audit trail of user and system activity.

## References
* [Slack Audit Log Event Schema](https://api.slack.com/admins/audit-logs#audit-event)
* [Slack Audit Log Actions](https://api.slack.com/admins/audit-logs-call#actions)
* [Slack Audit Log Anomaly Events](https://api.slack.com/admins/audit-logs-anomaly)

## Retention

Based on our research, Slack retains audit logs for Default 90 days.


### Comments
Can be customized


## Latency

Based on our research, Slack has a latency of Near real-time.

### Comments
NA


## Licensing

The Audit Logs API is only available to Slack workspaces on an Enterprise Grid plan.

## Mappings

| Category | Event Type | Attributes | Examples |
| -------- | ---------- | ---------- | -------- |
| C0001 | ET0001 |A0001 -> date_create<br />A0002 -> id<br />A0003 -> action<br />A0005 -> entity.user.email<br />A0006 -> entity.user.id<br />A0008 -> context.session_id<br />A0009 -> context.ip_address<br />A0011 -> context.ua<br />|[success](/products/slack/event_examples/authentication_account_login_success.json)<br />[failure](/products/slack/event_examples/authentication_account_login_failure.json)<br />|
| C0001 | ET0002 |A0001 -> date_create<br />A0002 -> id<br />A0003 -> action<br />A0005 -> entity.user.email<br />A0006 -> entity.user.id<br />A0008 -> context.session_id<br />A0009 -> context.ip_address<br />A0011 -> context.ua<br />|[success](/products/slack/event_examples/authentication_account_logout.json)<br />|
| C0002 | ET0004 |A0001 -> date_create<br />A0002 -> id<br />A0003 -> action<br />A0005 -> actor.user.email<br />A0006 -> entity.user.id<br />A0008 -> context.session_id<br />A0009 -> context.ip_address<br />A0011 -> context.ua<br />A0019 -> entity.user.email<br />|[member](/products/slack/event_examples/authorization_create_user.json)<br />[guest](/products/slack/event_examples/authorization_create_user_guest.json)<br />|
| C0002 | ET0006 |A0001 -> date_create<br />A0002 -> id<br />A0003 -> action<br />A0005 -> actor.user.email<br />A0006 -> entity.user.id<br />A0008 -> context.session_id<br />A0009 -> context.ip_address<br />A0011 -> context.ua<br />A0019 -> entity.user.email<br />A0020 -> details<br />|[success](/products/slack/event_examples/authorization_update_user.json)<br />|
| C0002 | ET0007 |A0001 -> date_create<br />A0002 -> id<br />A0003 -> action<br />A0005 -> actor.user.email<br />A0006 -> entity.user.id<br />A0008 -> context.session_id<br />A0009 -> context.ip_address<br />A0011 -> context.ua<br />A0019 -> entity.user.email<br />|[success](/products/slack/event_examples/authorization_delete_user.json)<br />|
| C0002 | ET0012 |A0001 -> date_create<br />A0002 -> id<br />A0003 -> action<br />A0005 -> details.inviter.user.email<br />A0006 -> details.inviter.user.id<br />A0008 -> context.session_id<br />A0009 -> context.ip_address<br />A0011 -> context.ua<br />A0019 -> entity.usergroup.name<br />|[success](/products/slack/event_examples/authorization_add_to_group.json)<br />|
| C0002 | ET0013 |A0001 -> date_create<br />A0002 -> id<br />A0003 -> action<br />A0005 -> details.kicker.user.email<br />A0006 -> details.kicker.user.id<br />A0008 -> context.session_id<br />A0009 -> context.ip_address<br />A0011 -> context.ua<br />A0021 -> entity.usergroup.name<br />A0019 -> actor.user.email<br />|[success](/products/slack/event_examples/authorization_remove_from_group.json)<br />|
| C0002 | ET0018 |A0001 -> date_create<br />A0002 -> id<br />A0003 -> action<br />A0005 -> actor.user.email<br />A0006 -> actor.user.id<br />A0008 -> context.session_id<br />A0009 -> context.ip_address<br />A0011 -> context.ua<br />A0023 -> entity.role.name<br />A0024 -> details.target_user<br />|[assign_role](/products/slack/event_examples/authorization_add_permission_role_assigned.json)<br />[assign_admin](/products/slack/event_examples/authorization_add_permission_role_changed_to_admin.json)<br />|
| C0002 | ET0019 |A0001 -> date_create<br />A0002 -> id<br />A0003 -> action<br />A0005 -> actor.user.email<br />A0006 -> actor.user.id<br />A0008 -> context.session_id<br />A0009 -> context.ip_address<br />A0011 -> context.ua<br />A0023 -> details.changed_permissions<br />A0024 -> entity.account_type_role.name<br />|[success](/products/slack/event_examples/authorization_remove_permission.json)<br />|
| C0002 | ET0020 |A0001 -> date_create<br />A0002 -> id<br />A0003 -> action<br />A0005 -> actor.user.email<br />A0006 -> actor.user.id<br />A0008 -> context.session_id<br />A0009 -> context.ip_address<br />A0011 -> context.ua<br />|[success](/products/slack/event_examples/authorization_add_enrollment.json)<br />|
| C0002 | ET0021 |A0001 -> date_create<br />A0002 -> id<br />A0003 -> action<br />A0005 -> actor.user.email<br />A0006 -> actor.user.id<br />A0008 -> context.session_id<br />A0009 -> context.ip_address<br />A0011 -> context.ua<br />|[success](/products/slack/event_examples/authorization_remove_enrollment.json)<br />|
| C0003 | ET0022 |A0001 -> date_create<br />A0002 -> id<br />A0003 -> action<br />A0005 -> actor.user.email<br />A0006 -> entity.user.id<br />A0008 -> context.session_id<br />A0009 -> context.ip_address<br />A0011 -> context.ua<br />A0026 -> action<br />A0027 -> details<br />|[success](/products/slack/event_examples/system_audit_create_security_configuration.json)<br />|
| C0003 | ET0024 |A0001 -> date_create<br />A0002 -> id<br />A0003 -> action<br />A0005 -> actor.user.email<br />A0006 -> entity.user.id<br />A0008 -> context.session_id<br />A0009 -> context.ip_address<br />A0011 -> context.ua<br />A0026 -> action<br />A0027 -> details.new_value<br />A0028 -> details.previous_value<br />|[change_sso](/products/slack/event_examples/system_audit_update_security_configuration_sso_changed.json)<br />[unapproved_ip](/products/slack/event_examples/system_audit_update_security_configuration_unapproved_ip.json)<br />|
| C0003 | ET0025 |A0001 -> date_create<br />A0002 -> id<br />A0003 -> action<br />A0005 -> actor.user.email<br />A0006 -> entity.user.id<br />A0008 -> context.session_id<br />A0009 -> context.ip_address<br />A0011 -> context.ua<br />A0026 -> action<br />A0027 -> details<br />|[success](/products/slack/event_examples/system_audit_delete_security_configuration.json)<br />|
| C0003 | ET0026 |A0001 -> date_create<br />A0002 -> id<br />A0003 -> action<br />A0005 -> actor.user.email<br />A0006 -> entity.user.id<br />A0008 -> context.session_id<br />A0009 -> context.ip_address<br />A0011 -> context.ua<br />A0029 -> entity.app.name<br />|[success](/products/slack/event_examples/system_audit_create_integration.json)<br />|
| C0003 | ET0028 |A0001 -> date_create<br />A0002 -> id<br />A0003 -> action<br />A0005 -> actor.user.email<br />A0006 -> entity.user.id<br />A0008 -> context.session_id<br />A0009 -> context.ip_address<br />A0011 -> context.ua<br />A0029 -> entity.app.name<br />A0028 -> details.previous_scopes<br />|[success](/products/slack/event_examples/system_audit_update_integration.json)<br />|
| C0003 | ET0029 |A0001 -> date_create<br />A0002 -> id<br />A0003 -> action<br />A0005 -> actor.user.email<br />A0006 -> entity.user.id<br />A0008 -> context.session_id<br />A0009 -> context.ip_address<br />A0011 -> context.ua<br />A0029 -> entity.app.name<br />|[success](/products/slack/event_examples/system_audit_delete_integration.json)<br />|
| C0004 | ET0030 |A0001 -> date_create<br />A0002 -> id<br />A0003 -> action<br />A0005 -> actor.user.email<br />A0006 -> entity.user.id<br />A0008 -> context.session_id<br />A0009 -> context.ip_address<br />A0011 -> context.ua<br />A0030 -> entity.file.name<br />A0031 -> action<br />|[success](/products/slack/event_examples/activity_audit_create_resource.json)<br />|
| C0004 | ET0032 |A0001 -> date_create<br />A0002 -> id<br />A0003 -> action<br />A0005 -> actor.user.email<br />A0006 -> entity.user.id<br />A0008 -> context.session_id<br />A0009 -> context.ip_address<br />A0011 -> context.ua<br />A0030 -> entity.channel.name<br />A0031 -> entity.type<br />|[success](/products/slack/event_examples/activity_audit_update_resource.json)<br />|
| C0004 | ET0033 |A0001 -> date_create<br />A0002 -> id<br />A0003 -> action<br />A0005 -> actor.user.email<br />A0006 -> entity.user.id<br />A0008 -> context.session_id<br />A0009 -> context.ip_address<br />A0011 -> context.ua<br />A0030 -> entity.file.name<br />A0031 -> entity.type<br />|[success](/products/slack/event_examples/activity_audit_delete_resource.json)<br />|
| C0004 | ET0034 |A0001 -> date_create<br />A0002 -> id<br />A0003 -> action<br />A0005 -> actor.user.email<br />A0006 -> entity.user.id<br />A0008 -> context.session_id<br />A0009 -> context.ip_address<br />A0011 -> context.ua<br />A0030 -> entity.file.name<br />A0031 -> entity.type<br />|[success](/products/slack/event_examples/activity_audit_download_resource.json)<br />|


