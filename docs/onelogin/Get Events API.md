# OneLogin - Get Events API (0.0.1)

> Entity Name: event_source

The OneLogin events API provides near real-time, read-only access to an organization's activity log.

## References
* [Get Events API Documentation](https://developers.onelogin.com/api-docs/1/events/get-events)

## Retention

Based on our research, OneLogin retains audit logs for Unknown.


### Comments
N/A


## Latency

Based on our research, OneLogin has a latency of Near real-time.

### Comments
N/A


## Licensing

A OneLogin license is required to access the Get Events API.

## Mappings

| Category | Event Type | Attributes | Examples |
| -------- | ---------- | ---------- | -------- |
| C0001 | ET0001 |A0001 -> created_at<br />A0002 -> id<br />A0003 -> event_type_id<br />A0005 -> actor_user_name<br />A0006 -> actor_user_id<br />A0009 -> ipaddr<br />|[success](/products/onelogin/event_examples/authentication_account_login_session_success.json)<br />[failure](/products/onelogin/event_examples/authentication_account_login_session_failure.json)<br />|
| C0001 | ET0002 |A0001 -> created_at<br />A0002 -> id<br />A0003 -> event_type_id<br />|[success](/products/onelogin/event_examples/authentication_account_logout.json)<br />|
| C0001 | ET0003 |A0001 -> created_at<br />A0002 -> id<br />A0003 -> event_type_id<br />A0005 -> actor_user_name<br />A0006 -> actor_user_id<br />A0009 -> ipaddr<br />A0016 -> notes<br />|[success](/products/onelogin/event_examples/authentication_mfa_verification.json)<br />[failure](/products/onelogin/event_examples/authentication_mfa_verification_failure.json)<br />|
| C0002 | ET0004 |A0001 -> created_at<br />A0002 -> id<br />A0003 -> event_type_id<br />A0005 -> actor_user_name<br />A0006 -> actor_user_id<br />A0009 -> ipaddr<br />A0019 -> user_name<br />|[success](/products/onelogin/event_examples/authorization_create_user.json)<br />|
| C0002 | ET0006 |A0001 -> created_at<br />A0002 -> id<br />A0003 -> event_type_id<br />A0005 -> actor_user_name<br />A0006 -> actor_user_id<br />A0009 -> ipaddr<br />A0019 -> user_name<br />|[success](/products/onelogin/event_examples/authorization_update_user.json)<br />|
| C0002 | ET0007 |A0001 -> created_at<br />A0002 -> id<br />A0003 -> event_type_id<br />A0005 -> actor_user_name<br />A0006 -> actor_user_id<br />A0009 -> ipaddr<br />A0019 -> user_name<br />|[success](/products/onelogin/event_examples/authorization_delete_user.json)<br />|
| C0002 | ET0008 |A0001 -> created_at<br />A0002 -> id<br />A0003 -> event_type_id<br />A0005 -> actor_user_name<br />A0006 -> actor_user_id<br />A0009 -> ipaddr<br />|[success](/products/onelogin/event_examples/authorization_create_group.json)<br />|
| C0002 | ET0010 |A0001 -> created_at<br />A0002 -> id<br />A0003 -> event_type_id<br />A0005 -> actor_user_name<br />A0006 -> actor_user_id<br />A0009 -> ipaddr<br />|[success](/products/onelogin/event_examples/authorization_update_group.json)<br />|
| C0002 | ET0011 |A0001 -> created_at<br />A0002 -> id<br />A0003 -> event_type_id<br />A0005 -> actor_user_name<br />A0006 -> actor_user_id<br />A0009 -> ipaddr<br />|[success](/products/onelogin/event_examples/authorization_delete_group.json)<br />|
| C0002 | ET0012 |A0001 -> created_at<br />A0002 -> id<br />A0003 -> event_type_id<br />A0005 -> actor_user_name<br />A0006 -> actor_user_id<br />A0009 -> ipaddr<br />A0019 -> user_name<br />|[success](/products/onelogin/event_examples/authorization_add_to_group.json)<br />|
| C0002 | ET0013 |A0001 -> created_at<br />A0002 -> id<br />A0003 -> event_type_id<br />A0005 -> actor_user_name<br />A0006 -> actor_user_id<br />A0009 -> ipaddr<br />A0019 -> user_name<br />|[success](/products/onelogin/event_examples/authorization_remove_from_group.json)<br />|
| C0002 | ET0014 |A0001 -> created_at<br />A0002 -> id<br />A0003 -> event_type_id<br />A0005 -> actor_user_name<br />A0006 -> actor_user_id<br />A0009 -> ipaddr<br />|[success](/products/onelogin/event_examples/authorization_create_role.json)<br />|
| C0002 | ET0016 |A0001 -> created_at<br />A0002 -> id<br />A0003 -> event_type_id<br />A0005 -> actor_user_name<br />A0006 -> actor_user_id<br />A0009 -> ipaddr<br />|[success](/products/onelogin/event_examples/authorization_update_role.json)<br />|
| C0002 | ET0017 |A0001 -> created_at<br />A0002 -> id<br />A0003 -> event_type_id<br />A0005 -> actor_user_name<br />A0006 -> actor_user_id<br />A0009 -> ipaddr<br />|[success](/products/onelogin/event_examples/authorization_delete_role.json)<br />|
| C0002 | ET0018 |A0001 -> created_at<br />A0002 -> id<br />A0003 -> event_type_id<br />A0005 -> actor_user_name<br />A0006 -> actor_user_id<br />A0009 -> ipaddr<br />A0024 -> user_name<br />|[success](/products/onelogin/event_examples/authorization_add_permission.json)<br />|
| C0002 | ET0019 |A0001 -> created_at<br />A0002 -> id<br />A0003 -> event_type_id<br />A0005 -> actor_user_name<br />A0006 -> actor_user_id<br />A0009 -> ipaddr<br />A0024 -> user_name<br />|[success](/products/onelogin/event_examples/authorization_remove_permission.json)<br />|
| C0002 | ET0020 |A0001 -> created_at<br />A0002 -> id<br />A0003 -> event_type_id<br />A0005 -> actor_user_name<br />A0006 -> actor_user_id<br />A0009 -> ipaddr<br />A0019 -> user_name<br />|[success](/products/onelogin/event_examples/authorization_add_enrollment.json)<br />|
| C0002 | ET0021 |A0001 -> created_at<br />A0002 -> id<br />A0003 -> event_type_id<br />A0005 -> actor_user_name<br />A0006 -> actor_user_id<br />A0009 -> ipaddr<br />A0019 -> user_name<br />|[success](/products/onelogin/event_examples/authorization_remove_enrollment.json)<br />|
| C0003 | ET0026 |A0001 -> created_at<br />A0002 -> id<br />A0003 -> event_type_id<br />A0005 -> actor_user_name<br />A0006 -> actor_user_id<br />A0009 -> ipaddr<br />A0029 -> app_name<br />|[success](/products/onelogin/event_examples/system_audit_create_integration.json)<br />|
| C0003 | ET0028 |A0001 -> created_at<br />A0002 -> id<br />A0003 -> event_type_id<br />A0005 -> actor_user_name<br />A0006 -> actor_user_id<br />A0009 -> ipaddr<br />A0029 -> app_name<br />|[success](/products/onelogin/event_examples/system_audit_update_integration.json)<br />|
| C0003 | ET0029 |A0001 -> created_at<br />A0002 -> id<br />A0003 -> event_type_id<br />A0005 -> actor_user_name<br />A0006 -> actor_user_id<br />A0009 -> ipaddr<br />A0029 -> app_name<br />|[success](/products/onelogin/event_examples/system_audit_delete_integration.json)<br />|
| C0004 | ET0030 |A0001 -> created_at<br />A0002 -> id<br />A0003 -> event_type_id<br />A0005 -> actor_user_name<br />A0006 -> actor_user_id<br />A0009 -> ipaddr<br />|[success](/products/onelogin/event_examples/activity_audit_create_resource.json)<br />|
| C0004 | ET0033 |A0001 -> created_at<br />A0002 -> id<br />A0003 -> event_type_id<br />A0005 -> actor_user_name<br />A0006 -> actor_user_id<br />A0009 -> ipaddr<br />|[success](/products/onelogin/event_examples/activity_audit_delete_resource.json)<br />|
| C0004 | ET0034 |A0001 -> created_at<br />A0002 -> id<br />A0003 -> event_type_id<br />A0005 -> actor_user_name<br />A0006 -> actor_user_id<br />A0009 -> ipaddr<br />|[success](/products/onelogin/event_examples/activity_audit_download_resource.json)<br />|


