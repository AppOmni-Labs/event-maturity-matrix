# AppOmni — Audit Logs

📌 **v1.0.0** · 🗄 **Retention:** 180 days · ⚡ **Latency:** Near Real-Time

🗄 Historical audit logs are stored for 180 days.


⚡ Logs are available in near real-time.


📜 **Licensing:** N/A


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
| Authorization | Add Enrollment | Enrollment Type | action_data.detail_str |
| Authorization | Add Enrollment | Target Username | action_data.target_user_username |
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
| Activity Audit | Create Resource | Resource Name | service_name |
| Activity Audit | Create Resource | Resource Type | service_type |
| Activity Audit | Update Resource | Timestamp | action_at |
| Activity Audit | Update Resource | Event ID | log_id |
| Activity Audit | Update Resource | Event Code / Type | action_type |
| Activity Audit | Update Resource | Username | action_data.user_username |
| Activity Audit | Update Resource | User ID | user_id |
| Activity Audit | Update Resource | Resource Name | service_name |
| Activity Audit | Update Resource | Resource Type | service_type |
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
| Authentication | Account Login | [success](/products/appomni/event_examples/authentication_account_login_google.json) | Timestamp=2023-06-22T19:06:47.149965+00:00; Event ID=ad9ddec3-8542-4d5a-b710-67928321abdc; Event Code / Type=user_login_google; Result=user_login_google; Username=jane@example.com |
| Authentication | Account Login | [failure](/products/appomni/event_examples/authentication_account_login_failed.json) | Timestamp=2023-06-14T21:57:50.583325+00:00; Event ID=6cbd2dc5-c125-40d1-8dcf-9936abda6c5f; Event Code / Type=user_login_failed; Result=user_login_failed; Username=pmcandrew+test10 |
| Authentication | Account Logout | [success](/products/appomni/event_examples/authentication_account_logout.json) | Timestamp=2023-06-22T20:48:41.714659+00:00; Event ID=49fc4cd2-653e-4261-bb59-25dc6ee7a1c0; Event Code / Type=user_logout; Result=user_logout; Username=bob@example.com |
| Authentication | MFA Verification | [challenge](/products/appomni/event_examples/authentication_account_login_challenge_totp.json) | Timestamp=2023-06-23T20:11:06.106260+00:00; Event ID=76812b0e-d9b0-4730-b5a1-5d4169743e2e; Event Code / Type=user_mfa_totp_challenge; Username=pmcandrew_test10; User ID=12893 |
| Authorization | Create User | [success](/products/appomni/event_examples/authorization_create_user.json) | Timestamp=2023-06-20T14:20:30.626150+00:00; Event ID=188fdcf3-143a-49e9-ba80-452b48f42e4f; Event Code / Type=user_created; Username=mallory@example.com; User ID=3187 |
| Authorization | Delete User | [success](/products/appomni/event_examples/authorization_delete_user.json) | Timestamp=2023-06-15T02:02:19.147946+00:00; Event ID=7f75c117-f8f8-4739-bfcf-cac8a728d486; Event Code / Type=user_disabled; Username=john@example.com; User ID=3187 |
| Authorization | Add Enrollment | [success](/products/appomni/event_examples/authorization_add_enrollment_totp_json.json) | Timestamp=2023-06-14T22:00:24.705316+00:00; Event ID=7ed13faf-9e3c-4905-839d-ff44309c2f72; Event Code / Type=user_mfa_enabled; Username=pmcandrew_test10; User ID=12893 |
| Authorization | Remove Enrollment | [success](/products/appomni/event_examples/authorization_remove_enrollment_totp.json) | Timestamp=2023-06-23T20:12:09.106337+00:00; Event ID=34628772-1560-46da-81d0-2371c5cc3106; Event Code / Type=user_mfa_disabled; Username=pmcandrew_test10; User ID=12893 |
| System Audit | Update Security Configuration | [success](/products/appomni/event_examples/system_audit_update_configuration.json) | Timestamp=2023-06-22T15:51:50.253793+00:00; Event ID=d2c46cde-44f7-43ac-84f5-79b8184c8105; Event Code / Type=ao_sys_setting_change; Username=jane@example.com; User ID=3187 |
| Activity Audit | Create Resource | [success](/products/appomni/event_examples/activity_audit_create_resource_policy.json) | Timestamp=2023-06-22T20:21:55.407230+00:00; Event ID=cb89b034-2f3b-4b41-9a34-6fdb289f4a6a; Event Code / Type=policy_created; Username=jane@example.com; User ID=3187 |
| Activity Audit | Update Resource | [success](/products/appomni/event_examples/activity_audit_update_resource_service.json) | Timestamp=2023-06-22T20:05:09.728571+00:00; Event ID=ea080b00-2cf0-49fe-b1ba-6081f17a66ff; Event Code / Type=ms_detection_ingestion_disabled; Username=mallory@example.com; User ID=3187 |
| Activity Audit | Delete Resource | [success](/products/appomni/event_examples/activity_audit_delete_resource_policy.json) | Timestamp=2023-07-12T19:07:57.569196+00:00; Event ID=d4b105e8-d29b-436e-947e-52a6be5f58de; Event Code / Type=policy_deleted; Username=bob@example.com; User ID=3187 |


