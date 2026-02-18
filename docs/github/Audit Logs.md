# GitHub - Audit Logs (0.0.1)

> Entity Name: event_source

GitHub enterprise audit logs that provide an audit trail of user and system activity.

## References
* [Enterprise Event Schema](https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/exporting-audit-log-activity-for-your-enterprise)

## Retention

Based on our research, GitHub retains audit logs for Infinite.


### Comments
Can be changed by an enterprise admin


## Latency

Based on our research, GitHub has a latency of Near Real-Time.

### Comments
N/A


## Licensing

Included with GitHub Enterprise accounts.

## Mappings

| Category | Event Type | Attributes | Examples |
| -------- | ---------- | ---------- | -------- |
| C0001 | ET0001 |A0001 -> created_at<br />A0002 -> _document_id<br />A0003 -> action<br />A0005 -> actor<br />A0006 -> actor_id<br />A0009 -> actor_ip<br />A0010 -> actor_location.country_code<br />A0011 -> user_agent<br />A0014 -> action<br />A0015 -> issuer<br />|[success](/products/github/event_examples/audit/authentication_account_login.json)<br />|
| C0002 | ET0008 |A0001 -> created_at<br />A0002 -> _document_id<br />A0003 -> action<br />A0005 -> actor<br />A0006 -> actor_id<br />A0009 -> actor_ip<br />A0010 -> actor_location.country_code<br />A0011 -> user_agent<br />A0021 -> ['org', 'team']<br />|[success](/products/github/event_examples/audit/authorization_create_group_team.json)<br />|
| C0002 | ET0010 |A0001 -> created_at<br />A0002 -> _document_id<br />A0003 -> action<br />A0005 -> actor<br />A0006 -> actor_id<br />A0009 -> actor_ip<br />A0010 -> actor_location.country_code<br />A0011 -> user_agent<br />A0021 -> ['org', 'team']<br />|[success](/products/github/event_examples/audit/authorization_update_group_team.json)<br />|
| C0002 | ET0012 |A0001 -> created_at<br />A0002 -> _document_id<br />A0003 -> action<br />A0005 -> actor<br />A0006 -> actor_id<br />A0009 -> actor_ip<br />A0010 -> actor_location.country_code<br />A0011 -> user_agent<br />A0019 -> user<br />A0021 -> ['org', 'team', 'repo']<br />|[success](/products/github/event_examples/audit/authorization_add_to_group_org.json)<br />[success](/products/github/event_examples/audit/authorization_add_to_group_repo.json)<br />[success](/products/github/event_examples/audit/authorization_add_to_group_team.json)<br />|
| C0002 | ET0013 |A0001 -> created_at<br />A0002 -> _document_id<br />A0003 -> action<br />A0005 -> actor<br />A0006 -> actor_id<br />A0009 -> actor_ip<br />A0010 -> actor_location.country_code<br />A0019 -> user<br />A0021 -> ['org', 'team', 'repo']<br />|[success](/products/github/event_examples/audit/authorization_remove_from_group_org.json)<br />[success](/products/github/event_examples/audit/authorization_remove_from_group_repo.json)<br />[success](/products/github/event_examples/audit/authorization_remove_from_group_team.json)<br />|
| C0002 | ET0018 |A0001 -> created_at<br />A0002 -> _document_id<br />A0003 -> action<br />A0005 -> actor<br />A0006 -> actor_id<br />A0009 -> actor_ip<br />A0010 -> actor_location.country_code<br />A0011 -> user_agent<br />A0023 -> new_repo_permission<br />A0024 -> ['org', 'team', 'repo']<br />|[success](/products/github/event_examples/audit/authorization_add_permission_team.json)<br />|
| C0002 | ET0019 |A0001 -> created_at<br />A0002 -> _document_id<br />A0003 -> action<br />A0005 -> actor<br />A0006 -> actor_id<br />A0009 -> actor_ip<br />A0010 -> actor_location.country_code<br />A0011 -> user_agent<br />A0023 -> old_repo_permission<br />A0024 -> ['org', 'team', 'repo']<br />|[success](/products/github/event_examples/audit/authorization_remove_permission_team.json)<br />|
| C0003 | ET0022 |A0001 -> created_at<br />A0002 -> _document_id<br />A0003 -> action<br />A0005 -> actor<br />A0006 -> actor_id<br />A0009 -> actor_ip<br />A0010 -> actor_location.country_code<br />A0011 -> user_agent<br />A0026 -> action<br />A0027 -> action<br />|[success](/products/github/event_examples/audit/system_audit_create_security_configuration_forking.json)<br />|
| C0003 | ET0024 |A0001 -> created_at<br />A0002 -> _document_id<br />A0003 -> action<br />A0005 -> actor<br />A0006 -> actor_id<br />A0009 -> actor_ip<br />A0010 -> actor_location.country_code<br />A0011 -> user_agent<br />A0026 -> name<br />A0027 -> config<br />A0028 -> config_was<br />|[success](/products/github/event_examples/audit/system_audit_update_security_configuration_hook_config.json)<br />|
| C0003 | ET0026 |A0001 -> created_at<br />A0002 -> _document_id<br />A0003 -> action<br />A0005 -> actor<br />A0006 -> actor_id<br />A0009 -> actor_ip<br />A0010 -> actor_location.country_code<br />A0011 -> user_agent<br />A0029 -> integration<br />|[success](/products/github/event_examples/audit/system_audit_create_integration.json)<br />|
| C0004 | ET0030 |A0001 -> created_at<br />A0002 -> _document_id<br />A0003 -> action<br />A0005 -> actor<br />A0006 -> actor_id<br />A0009 -> actor_ip<br />A0010 -> actor_location.country_code<br />A0011 -> user_agent<br />A0030 -> ['org', 'business', 'repo']<br />A0031 -> action<br />|[success](/products/github/event_examples/audit/activity_audit_create_resource_hook.json)<br />[success](/products/github/event_examples/audit/activity_audit_create_resource_pull_request.json)<br />[success](/products/github/event_examples/audit/activity_audit_create_resource_pull_request_review.json)<br />[success](/products/github/event_examples/audit/activity_audit_create_resource_pull_request_review_comment.json)<br />[success](/products/github/event_examples/audit/activity_audit_create_resource_repo.json)<br />[success](/products/github/event_examples/audit/activity_audit_create_resource_secret.json)<br />[success](/products/github/event_examples/audit/activity_audit_create_resource_workflow.json)<br />|
| C0004 | ET0032 |A0001 -> created_at<br />A0002 -> _document_id<br />A0003 -> action<br />A0005 -> actor<br />A0006 -> actor_id<br />A0009 -> actor_ip<br />A0010 -> actor_location.country_code<br />A0011 -> user_agent<br />A0030 -> ['org', 'business', 'repo']<br />A0031 -> action<br />|[success](/products/github/event_examples/audit/activity_audit_update_resource_pull_request.json)<br />[success](/products/github/event_examples/audit/activity_audit_update_resource_pull_request_review_comment.json)<br />[success](/products/github/event_examples/audit/activity_audit_update_resource_repo.json)<br />|
| C0004 | ET0033 |A0001 -> created_at<br />A0002 -> _document_id<br />A0003 -> action<br />A0005 -> actor<br />A0006 -> actor_id<br />A0009 -> actor_ip<br />A0010 -> actor_location.country_code<br />A0011 -> user_agent<br />A0030 -> ['org', 'business', 'repo']<br />A0031 -> action<br />|[success](/products/github/event_examples/audit/activity_audit_delete_resource_hook.json)<br />[success](/products/github/event_examples/audit/activity_audit_delete_resource_pull_request_review.json)<br />[success](/products/github/event_examples/audit/activity_audit_delete_resource_pull_request_review_comment.json)<br />[success](/products/github/event_examples/audit/activity_audit_delete_resource_repo.json)<br />|
| C0004 | ET0034 |A0001 -> created_at<br />A0002 -> _document_id<br />A0003 -> action<br />A0005 -> actor<br />A0006 -> actor_id<br />A0009 -> actor_ip<br />A0010 -> actor_location.country_code<br />A0011 -> user_agent<br />A0030 -> repo<br />A0031 -> action<br />|[success](/products/github/event_examples/audit/activity_audit_download_resource_repo.json)<br />|


