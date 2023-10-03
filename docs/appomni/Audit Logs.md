# AppOmni - Audit Logs (0.0.1)

> Entity Name: event_source

AppOmni audit logs that provide a record of user activity.

## References
* [Audit Log Schema](N/A)

## Retention

Based on our research, AppOmni retains audit logs for 180 days.


### Comments
Historical audit logs are stored for 180 days.


## Latency

Based on our research, AppOmni has a latency of Near Real-Time.

### Comments
Logs are available in near real-time.


## Licensing

N/A

## Mappings

| Category | Event Type | Attributes | Examples |
| -------- | ---------- | ---------- | -------- |
| C0001 | ET0001 |A0001 -> action_at<br />A0002 -> log_id<br />A0003 -> action_type<br />A0004 -> action_type<br />A0005 -> action_data.user_username<br />A0006 -> user_id<br />A0009 -> action_data.user_ip<br />A0011 -> action_data.user_agent<br />A0015 -> action_type<br />|[failure](/products/appomni/event_examples/authentication_account_login_failed.json)<br />|
| C0001 | ET0002 |A0001 -> action_at<br />A0002 -> log_id<br />A0003 -> action_type<br />A0004 -> action_type<br />A0005 -> action_data.user_username<br />A0006 -> user_id<br />A0009 -> action_data.user_ip<br />A0011 -> action_data.user_agent<br />|[success](/products/appomni/event_examples/authentication_account_logout.json)<br />|
| C0001 | ET0003 |A0001 -> action_at<br />A0002 -> log_id<br />A0003 -> action_type<br />A0005 -> action_data.user_username<br />A0006 -> user_id<br />A0009 -> action_data.user_ip<br />A0011 -> action_data.user_agent<br />A0016 -> action_type<br />|[challenge](/products/appomni/event_examples/authentication_account_login_challenge_totp.json)<br />|
| C0002 | ET0004 |A0001 -> action_at<br />A0002 -> log_id<br />A0003 -> action_type<br />A0005 -> action_data.user_username<br />A0006 -> user_id<br />A0009 -> action_data.user_ip<br />A0011 -> action_data.user_agent<br />A0019 -> action_data.target_user_username<br />|[success](/products/appomni/event_examples/authorization_create_user.json)<br />|
| C0002 | ET0007 |A0001 -> action_at<br />A0002 -> log_id<br />A0003 -> action_type<br />A0005 -> user_username<br />A0006 -> user_id<br />A0009 -> action_data.user_ip<br />A0011 -> action_data.user_agent<br />A0019 -> action_data.user_username<br />|[success](/products/appomni/event_examples/authorization_delete_user.json)<br />|
| C0002 | ET0020 |A0001 -> action_at<br />A0002 -> log_id<br />A0003 -> action_type<br />A0005 -> action_data.user_username<br />A0006 -> user_id<br />A0009 -> action_data.user_ip<br />A0011 -> action_data.user_agent<br />A0025 -> action_data.detail_str<br />A0019 -> action_data.target_user_username<br />|[success](/products/appomni/event_examples/authorization_add_enrollment_totp_json.json)<br />|
| C0002 | ET0021 |A0001 -> action_at<br />A0002 -> log_id<br />A0003 -> action_type<br />A0005 -> action_data.target_user_username<br />A0006 -> user_id<br />A0009 -> action_data.user_ip<br />A0011 -> act_data.user_agent<br />A0019 -> action_data.target_user_username<br />|[success](/products/appomni/event_examples/authorization_remove_enrollment_totp.json)<br />|
| C0003 | ET0024 |A0001 -> action_at<br />A0002 -> log_id<br />A0003 -> action_type<br />A0005 -> action_data.user_username<br />A0006 -> user_id<br />A0009 -> action_data.user_ip<br />A0011 -> action_data.user_agent<br />A0026 -> action_data.setting_name<br />A0027 -> action_data.new_value<br />A0028 -> action_data.old_value<br />|[success](/products/appomni/event_examples/system_audit_update_configuration.json)<br />|
| C0004 | ET0030 |A0001 -> action_at<br />A0002 -> log_id<br />A0003 -> action_type<br />A0005 -> action_data.user_username<br />A0006 -> user_id<br />A0009 -> action_data.user_ip<br />A0011 -> action_data.user_agent<br />A0030 -> service_name<br />A0031 -> service_type<br />|[success](/products/appomni/event_examples/activity_audit_create_resource_policy.json)<br />|
| C0004 | ET0032 |A0001 -> action_at<br />A0002 -> log_id<br />A0003 -> action_type<br />A0005 -> action_data.user_username<br />A0006 -> user_id<br />A0030 -> service_name<br />A0031 -> service_type<br />|[success](/products/appomni/event_examples/activity_audit_update_resource_service.json)<br />|
| C0004 | ET0033 |A0001 -> action_at<br />A0002 -> log_id<br />A0003 -> action_type<br />A0005 -> action_data.user_username<br />A0006 -> user_id<br />A0009 -> action_data.user_ip<br />A0011 -> action_data.user_agent<br />A0030 -> service_name<br />A0031 -> service_type<br />|[success](/products/appomni/event_examples/activity_audit_delete_resource_policy.json)<br />|


