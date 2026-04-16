# AppOmni — Audit Logs

📌 **v1.0.0** · 🗄 **Retention:** 180 days · ⚡ **Latency:** Near Real-Time

🗄 Historical audit logs are stored for 180 days.⚡ Logs are available in near real-time.📜 **Licensing:** Included for all customers.

AppOmni audit logs that provide a record of user activity.
## References
* [Audit Log Schema](N/A)
## Field mappings

| Category | Event type | Attribute | Source field(s) |
| -------- | ---------- | --------- | ---------------- |
| Authentication | Account Login | Timestamp | action_at |
| Authentication | Account Login | Event ID | log_id |
| Authentication | Account Login | Event Code / Type | action_type |
| Authentication | Account Login | Result | action_type |
| Authentication | Account Login | Username | action_data.user_username |
| Authentication | Account Login | User ID | user_id |
| Authentication | Account Login | IP Address | action_data.user_ip |
| Authentication | Account Login | User Agent Name | action_data.user_agent |
| Authentication | Account Login | Identity Service Provider Context | action_type |
| Authentication | Account Logout | Timestamp | action_at |
| Authentication | Account Logout | Event ID | log_id |
| Authentication | Account Logout | Event Code / Type | action_type |
| Authentication | Account Logout | Result | action_type |
| Authentication | Account Logout | Username | action_data.user_username |
| Authentication | Account Logout | User ID | user_id |
| Authentication | Account Logout | IP Address | action_data.user_ip |
| Authentication | Account Logout | User Agent Name | action_data.user_agent |
| Authentication | MFA Verification | Timestamp | action_at |
| Authentication | MFA Verification | Event ID | log_id |
| Authentication | MFA Verification | Event Code / Type | action_type |
| Authentication | MFA Verification | Username | action_data.user_username |
| Authentication | MFA Verification | User ID | user_id |
| Authentication | MFA Verification | IP Address | action_data.user_ip |
| Authentication | MFA Verification | User Agent Name | action_data.user_agent |
| Authentication | MFA Verification | Verification Method | action_type |
| Authorization | Create User | Timestamp | action_at |
| Authorization | Create User | Event ID | log_id |
| Authorization | Create User | Event Code / Type | action_type |
| Authorization | Create User | Username | action_data.user_username |
| Authorization | Create User | User ID | user_id |
| Authorization | Create User | IP Address | action_data.user_ip |
| Authorization | Create User | User Agent Name | action_data.user_agent |
| Authorization | Create User | Target Username | action_data.target_user_username |
| Authorization | Delete User | Timestamp | action_at |
| Authorization | Delete User | Event ID | log_id |
| Authorization | Delete User | Event Code / Type | action_type |
| Authorization | Delete User | Username | user_username |
| Authorization | Delete User | User ID | user_id |
| Authorization | Delete User | IP Address | action_data.user_ip |
| Authorization | Delete User | User Agent Name | action_data.user_agent |
| Authorization | Delete User | Target Username | action_data.user_username |
| Authorization | Add Enrollment | Timestamp | action_at |
| Authorization | Add Enrollment | Event ID | log_id |
| Authorization | Add Enrollment | Event Code / Type | action_type |
| Authorization | Add Enrollment | Username | action_data.user_username |
| Authorization | Add Enrollment | User ID | user_id |
| Authorization | Add Enrollment | IP Address | action_data.user_ip |
| Authorization | Add Enrollment | User Agent Name | action_data.user_agent |
| Authorization | Add Enrollment | Target Username | action_data.target_user_username |
| Authorization | Add Enrollment | Enrollment Type | action_data.detail_str |
| Authorization | Remove Enrollment | Timestamp | action_at |
| Authorization | Remove Enrollment | Event ID | log_id |
| Authorization | Remove Enrollment | Event Code / Type | action_type |
| Authorization | Remove Enrollment | Username | action_data.target_user_username |
| Authorization | Remove Enrollment | User ID | user_id |
| Authorization | Remove Enrollment | IP Address | action_data.user_ip |
| Authorization | Remove Enrollment | User Agent Name | action_data.user_agent |
| Authorization | Remove Enrollment | Target Username | action_data.target_user_username |
| System Audit | Update Security Configuration | Timestamp | action_at |
| System Audit | Update Security Configuration | Event ID | log_id |
| System Audit | Update Security Configuration | Event Code / Type | action_type |
| System Audit | Update Security Configuration | Username | action_data.user_username |
| System Audit | Update Security Configuration | User ID | user_id |
| System Audit | Update Security Configuration | IP Address | action_data.user_ip |
| System Audit | Update Security Configuration | User Agent Name | action_data.user_agent |
| System Audit | Update Security Configuration | Configuration / Setting Name | action_data.setting_name |
| System Audit | Update Security Configuration | Configuration / Setting Value | action_data.new_value |
| System Audit | Update Security Configuration | Previous Configuration / Setting Value | action_data.old_value |
| Activity Audit | Create Resource | Timestamp | action_at |
| Activity Audit | Create Resource | Event ID | log_id |
| Activity Audit | Create Resource | Event Code / Type | action_type |
| Activity Audit | Create Resource | Username | action_data.user_username |
| Activity Audit | Create Resource | User ID | user_id |
| Activity Audit | Create Resource | IP Address | action_data.user_ip |
| Activity Audit | Create Resource | User Agent Name | action_data.user_agent |
| Activity Audit | Create Resource | Resource Name | action_data.policy_name |
| Activity Audit | Create Resource | Resource Type | action_type |
| Activity Audit | Update Resource | Timestamp | action_at |
| Activity Audit | Update Resource | Event ID | log_id |
| Activity Audit | Update Resource | Event Code / Type | action_type |
| Activity Audit | Update Resource | Username | action_data.user_username |
| Activity Audit | Update Resource | User ID | user_id |
| Activity Audit | Update Resource | Resource Name | action_data.eventsource_name |
| Activity Audit | Update Resource | Resource Type | action_type |
| Activity Audit | Delete Resource | Timestamp | action_at |
| Activity Audit | Delete Resource | Event ID | log_id |
| Activity Audit | Delete Resource | Event Code / Type | action_type |
| Activity Audit | Delete Resource | Username | action_data.user_username |
| Activity Audit | Delete Resource | User ID | user_id |
| Activity Audit | Delete Resource | IP Address | action_data.user_ip |
| Activity Audit | Delete Resource | User Agent Name | action_data.user_agent |
| Activity Audit | Delete Resource | Resource Name | policy_name |
| Activity Audit | Delete Resource | Resource Type | service_type |

## Example logs

| Category | Event type | Log | Sample field values |
| -------- | ---------- | --- | ------------------- |
| Authentication | Account Login | [success](/products/appomni/event_examples/authentication_account_login_google.json) | Timestamp=2026-04-15T14:37:11.456244+00:00; Event ID=a53b195a-f845-49c1-8640-bb77f1497579; Event Code / Type=user_login_google; Result=user_login_google; Username=jane@example.com |
| Authentication | Account Login | [failure](/products/appomni/event_examples/authentication_account_login_failed.json) | Timestamp=2026-03-27T21:42:31.383524+00:00; Event ID=9d8dad37-c5c2-41bd-9bc3-abdc91f43beb; Event Code / Type=user_login_failed; Result=user_login_failed; Username=joe@example.com |
| Authentication | Account Logout | [success](/products/appomni/event_examples/authentication_account_logout.json) | Timestamp=2026-03-10T15:18:31.885097+00:00; Event ID=3e9de703-1f3c-4d99-ab32-c5ffe91bccb8; Event Code / Type=user_logout; Result=user_logout; Username=bob@example.com |
| Authentication | MFA Verification | [challenge](/products/appomni/event_examples/authentication_account_login_challenge_totp.json) | Timestamp=2026-03-17T21:13:50.353268+00:00; Event ID=f382d720-1f5d-4d88-90db-65cc8eba1be8; Event Code / Type=user_mfa_totp_challenge; Username=jane@example.com; User ID=5432 |
| Authorization | Create User | [success](/products/appomni/event_examples/authorization_create_user.json) | Timestamp=2026-04-09T12:33:22.843747+00:00; Event ID=075c55fb-1e70-472c-a165-67cf61d7a266; Event Code / Type=user_created; Username=alice; User ID=456 |
| Authorization | Delete User | [success](/products/appomni/event_examples/authorization_delete_user.json) | Timestamp=2026-04-12T12:21:01.625083+00:00; Event ID=9ec8c688-5de1-4910-8c0b-2304838ad01f; Event Code / Type=user_disabled; Username=alice; User ID=456 |
| Authorization | Add Enrollment | [success](/products/appomni/event_examples/authorization_add_enrollment_totp.json) | Timestamp=2026-03-17T21:15:35.154828+00:00; Event ID=6dc9e1fb-b865-3e01-8ced-3f4cebcc95bd; Event Code / Type=user_mfa_enabled; Username=alice@example.com; User ID=98765 |
| Authorization | Remove Enrollment | [success](/products/appomni/event_examples/authorization_remove_enrollment_totp.json) | Timestamp=2026-04-16T09:12:37.178135+00:00; Event ID=7482d820-a068-4c9a-810d-0f9e4396ba01; Event Code / Type=user_mfa_disabled; Username=alice@example.com; User ID=3456 |
| System Audit | Update Security Configuration | [success](/products/appomni/event_examples/system_audit_update_configuration.json) | Timestamp=2026-03-19T06:51:54.773871+00:00; Event ID=0ef8a486-600b-46fa-bf5b-0a91b3941083; Event Code / Type=ao_sys_setting_change; Username=john@example.com; User ID=456 |
| Activity Audit | Create Resource | [success](/products/appomni/event_examples/activity_audit_create_resource_policy.json) | Timestamp=2026-02-23T00:36:11.547662+00:00; Event ID=2679bd8f-d94f-4293-9959-878045c668cd; Event Code / Type=policy_created; Username=alice@example.com; User ID=34 |
| Activity Audit | Update Resource | [success](/products/appomni/event_examples/activity_audit_update_resource_event_source.json) | Timestamp=2026-04-16T09:17:48.681362+00:00; Event ID=1a944a69-3503-4705-ac57-4a14c57431dc; Event Code / Type=event_source_updated; Username=john@example.com; User ID=3456 |
| Activity Audit | Delete Resource | [success](/products/appomni/event_examples/activity_audit_delete_resource_policy.json) | Timestamp=2023-07-12T19:07:57.569196+00:00; Event ID=d4b105e8-d29b-436e-947e-52a6be5f58de; Event Code / Type=policy_deleted; Username=bob@example.com; User ID=3187 |


