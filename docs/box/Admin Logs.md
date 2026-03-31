# Box — Admin Logs

📌 **v1.0.0** · 🗄 **Retention:** 365 Days · ⚡ **Latency:** Near Real-Time

🗄 Based on the admin_logs stream type.


⚡ N/A


📜 **Licensing:** Included with Box Business Plus and above.


Box enterprise logs that provide an audit trail of user activity.
## References
* [Enterprise Event Schema](https://developer.box.com/reference/resources/event/)
## Field mappings

| Category | Event type | Attribute | Source field(s) |
| -------- | ---------- | --------- | ---------------- |
| Authentication | Account Login | Timestamp | created_at |
| Authentication | Account Login | Event ID | event_id |
| Authentication | Account Login | Event Code / Type | event_type |
| Authentication | Account Login | Result | event_type |
| Authentication | Account Login | Username | source.login |
| Authentication | Account Login | User ID | source.id |
| Authentication | Account Login | Session ID | session_id |
| Authentication | Account Login | IP Address | ip_address |
| Authorization | Create User | Timestamp | created_at |
| Authorization | Create User | Event ID | event_id |
| Authorization | Create User | Event Code / Type | event_type |
| Authorization | Create User | Username | created_by.login |
| Authorization | Create User | User ID | created_by.id |
| Authorization | Create User | Session ID | session_id |
| Authorization | Create User | IP Address | ip_address |
| Authorization | Create User | Target Username | source.login |
| Authorization | Update User | Timestamp | created_at |
| Authorization | Update User | Event ID | event_id |
| Authorization | Update User | Event Code / Type | event_type |
| Authorization | Update User | Username | created_by.login |
| Authorization | Update User | User ID | created_by.id |
| Authorization | Update User | Session ID | session_id |
| Authorization | Update User | IP Address | ip_address |
| Authorization | Update User | Target Username | source.login |
| Authorization | Delete User | Timestamp | created_at |
| Authorization | Delete User | Event ID | event_id |
| Authorization | Delete User | Event Code / Type | event_type |
| Authorization | Delete User | Username | created_by.login |
| Authorization | Delete User | User ID | created_by.id |
| Authorization | Delete User | Session ID | session_id |
| Authorization | Delete User | IP Address | ip_address |
| Authorization | Delete User | Target Username | source.login |
| Authorization | Create Group | Timestamp | created_at |
| Authorization | Create Group | Event ID | event_id |
| Authorization | Create Group | Event Code / Type | event_type |
| Authorization | Create Group | Username | created_by.login |
| Authorization | Create Group | User ID | created_by.id |
| Authorization | Create Group | Session ID | session_id |
| Authorization | Create Group | IP Address | ip_address |
| Authorization | Create Group | Target Group Name | source.group_name |
| Authorization | Update Group | Timestamp | created_at |
| Authorization | Update Group | Event ID | event_id |
| Authorization | Update Group | Event Code / Type | event_type |
| Authorization | Update Group | Username | created_by.login |
| Authorization | Update Group | User ID | created_by.id |
| Authorization | Update Group | Session ID | session_id |
| Authorization | Update Group | IP Address | ip_address |
| Authorization | Update Group | Target Group Name | source.group_name |
| Authorization | Delete Group | Timestamp | created_at |
| Authorization | Delete Group | Event ID | event_id |
| Authorization | Delete Group | Event Code / Type | event_type |
| Authorization | Delete Group | Username | created_by.login |
| Authorization | Delete Group | User ID | created_by.id |
| Authorization | Delete Group | Session ID | session_id |
| Authorization | Delete Group | IP Address | ip_address |
| Authorization | Delete Group | Target Group Name | source.group_name |
| Authorization | Add To Group | Timestamp | created_at |
| Authorization | Add To Group | Event ID | event_id |
| Authorization | Add To Group | Event Code / Type | event_type |
| Authorization | Add To Group | Username | created_by.login |
| Authorization | Add To Group | User ID | created_by.id |
| Authorization | Add To Group | Session ID | session_id |
| Authorization | Add To Group | IP Address | ip_address |
| Authorization | Add To Group | Target Username | source.login |
| Authorization | Add To Group | Target Group Name | additional_details.group_name |
| Authorization | Remove From Group | Timestamp | created_at |
| Authorization | Remove From Group | Event ID | event_id |
| Authorization | Remove From Group | Event Code / Type | event_type |
| Authorization | Remove From Group | Username | created_by.login |
| Authorization | Remove From Group | User ID | created_by.id |
| Authorization | Remove From Group | Session ID | session_id |
| Authorization | Remove From Group | IP Address | ip_address |
| Authorization | Remove From Group | Target Username | source.login |
| Authorization | Remove From Group | Target Group Name | additional_details.group_name |
| Authorization | Add Permission | Timestamp | created_at |
| Authorization | Add Permission | Event ID | event_id |
| Authorization | Add Permission | Event Code / Type | event_type |
| Authorization | Add Permission | Username | created_by.login |
| Authorization | Add Permission | User ID | created_by.id |
| Authorization | Add Permission | Session ID | session_id |
| Authorization | Add Permission | IP Address | ip_address |
| Authorization | Add Permission | Permission Name | additional_details.role |
| Authorization | Add Permission | Target Resource Name | source.file_name |
| Authorization | Remove Permission | Timestamp | created_at |
| Authorization | Remove Permission | Event ID | event_id |
| Authorization | Remove Permission | Event Code / Type | event_type |
| Authorization | Remove Permission | Username | created_by.login |
| Authorization | Remove Permission | User ID | created_by.id |
| Authorization | Remove Permission | Session ID | session_id |
| Authorization | Remove Permission | IP Address | ip_address |
| Authorization | Remove Permission | Target Resource Name | source.file_name |
| Authorization | Add Enrollment | Timestamp | created_at |
| Authorization | Add Enrollment | Event ID | event_id |
| Authorization | Add Enrollment | Event Code / Type | event_type |
| Authorization | Add Enrollment | Username | created_by.login |
| Authorization | Add Enrollment | User ID | created_by.id |
| Authorization | Add Enrollment | Session ID | session_id |
| Authorization | Add Enrollment | IP Address | ip_address |
| Authorization | Add Enrollment | Target Username | source.login |
| Authorization | Remove Enrollment | Timestamp | created_at |
| Authorization | Remove Enrollment | Event ID | event_id |
| Authorization | Remove Enrollment | Event Code / Type | event_type |
| Authorization | Remove Enrollment | Username | created_by.login |
| Authorization | Remove Enrollment | User ID | created_by.id |
| Authorization | Remove Enrollment | Session ID | session_id |
| Authorization | Remove Enrollment | IP Address | ip_address |
| Authorization | Remove Enrollment | Target Username | source.login |
| Activity Audit | Create Resource | Timestamp | created_at |
| Activity Audit | Create Resource | Event ID | event_id |
| Activity Audit | Create Resource | Event Code / Type | event_type |
| Activity Audit | Create Resource | Username | created_by.login |
| Activity Audit | Create Resource | User ID | created_by.id |
| Activity Audit | Create Resource | Session ID | session_id |
| Activity Audit | Create Resource | IP Address | ip_address |
| Activity Audit | Create Resource | Resource Name | source.item_name |
| Activity Audit | Create Resource | Resource Type | source.item_type |
| Activity Audit | Read Resource | Timestamp | created_at |
| Activity Audit | Read Resource | Event ID | event_id |
| Activity Audit | Read Resource | Event Code / Type | event_type |
| Activity Audit | Read Resource | Username | created_by.login |
| Activity Audit | Read Resource | User ID | created_by.id |
| Activity Audit | Read Resource | Session ID | session_id |
| Activity Audit | Read Resource | IP Address | ip_address |
| Activity Audit | Read Resource | Resource Name | source.item_name |
| Activity Audit | Read Resource | Resource Type | source.item_type |
| Activity Audit | Update Resource | Timestamp | created_at |
| Activity Audit | Update Resource | Event ID | event_id |
| Activity Audit | Update Resource | Event Code / Type | event_type |
| Activity Audit | Update Resource | Username | created_by.login |
| Activity Audit | Update Resource | User ID | created_by.id |
| Activity Audit | Update Resource | Session ID | session_id |
| Activity Audit | Update Resource | IP Address | ip_address |
| Activity Audit | Update Resource | Resource Name | source.item_name |
| Activity Audit | Update Resource | Resource Type | source.item_type |
| Activity Audit | Delete Resource | Timestamp | created_at |
| Activity Audit | Delete Resource | Event ID | event_id |
| Activity Audit | Delete Resource | Event Code / Type | event_type |
| Activity Audit | Delete Resource | Username | created_by.login |
| Activity Audit | Delete Resource | User ID | created_by.id |
| Activity Audit | Delete Resource | Session ID | session_id |
| Activity Audit | Delete Resource | IP Address | ip_address |
| Activity Audit | Delete Resource | Resource Name | source.item_name |
| Activity Audit | Delete Resource | Resource Type | source.item_type |
| Activity Audit | Download Resource | Timestamp | created_at |
| Activity Audit | Download Resource | Event ID | event_id |
| Activity Audit | Download Resource | Event Code / Type | event_type |
| Activity Audit | Download Resource | Username | created_by.login |
| Activity Audit | Download Resource | User ID | created_by.id |
| Activity Audit | Download Resource | Session ID | session_id |
| Activity Audit | Download Resource | IP Address | ip_address |
| Activity Audit | Download Resource | Resource Name | source.item_name |
| Activity Audit | Download Resource | Resource Type | source.item_type |
| Activity Audit | Download Resource | Resource Metadata | additional_details.size |

## Example logs

| Category | Event type | Log | Sample field values |
| -------- | ---------- | --- | ------------------- |
| Authentication | Account Login | [success](/products/box/event_examples/authentication_account_login_success.json) | Timestamp=2023-05-09T08:28:41-07:00; Event ID=00000000-abcd-1234-ab08-2cfe92d42606; Event Code / Type=LOGIN; Result=LOGIN; Username=alice@example.com |
| Authentication | Account Login | [failure](/products/box/event_examples/authentication_account_login_failure.json) | Timestamp=2023-05-09T09:08:06-07:00; Event ID=00000000-abcd-1234-84ee-12298e09cfa9; Event Code / Type=FAILED_LOGIN; Result=FAILED_LOGIN; Username=john@example.com |
| Authorization | Create User | [create](/products/box/event_examples/authorization_create_user.json) | Timestamp=2023-05-09T09:34:43-07:00; Event ID=00000000-abcd-1234-92ad-46f2f69e45cd; Event Code / Type=NEW_USER; Username=bob@example.com; User ID=12345648385 |
| Authorization | Update User | [update](/products/box/event_examples/authorization_update_user.json) | Timestamp=2023-05-09T09:35:29-07:00; Event ID=00000000-abcd-1234-be64-7fdc0421e478; Event Code / Type=EDIT_USER; Username=jane@example.com; User ID=12345648385 |
| Authorization | Delete User | [delete](/products/box/event_examples/authorization_delete_user.json) | Timestamp=2023-05-09T09:35:58-07:00; Event ID=00000000-abcd-1234-9c97-5e32f323b9f0; Event Code / Type=DELETE_USER; Username=bob@example.com; User ID=12345648385 |
| Authorization | Create Group | [create](/products/box/event_examples/authorization_create_group.json) | Timestamp=2023-05-09T09:36:36-07:00; Event ID=00000000-abcd-1234-a8a6-6f5474e5d86d; Event Code / Type=GROUP_CREATION; Username=John Doe; User ID=18863648385 |
| Authorization | Update Group | [update](/products/box/event_examples/authorization_update_group.json) | Timestamp=2023-05-09T09:36:46-07:00; Event ID=49d24c58-a0e5-4ec7-9ccd-347827b0afed; Event Code / Type=GROUP_EDITED; Username=john@example.com; User ID=18863648385 |
| Authorization | Delete Group | [delete](/products/box/event_examples/authorization_delete_group.json) | Timestamp=2023-05-09T10:46:19-07:00; Event ID=24ada35a-a9e9-4c67-8fc9-33b5b9f9b52b; Event Code / Type=GROUP_DELETION; Username=alice@example.com; User ID=18863648385 |
| Authorization | Add To Group | [add](/products/box/event_examples/authorization_add_to_group.json) | Timestamp=2023-05-09T10:24:15-07:00; Event ID=f0545aa9-4be4-451e-a8d2-3c56aa257b8a; Event Code / Type=GROUP_ADD_USER; Username=bob@example.com; User ID=18863648385 |
| Authorization | Remove From Group | [remove](/products/box/event_examples/authorization_remove_from_group.json) | Timestamp=2023-05-09T10:45:45-07:00; Event ID=56ae6ebb-7d6c-418e-bdeb-98d067c52af2; Event Code / Type=GROUP_REMOVE_USER; Username=mallory@example.com; User ID=18863648385 |
| Authorization | Add Permission | [add](/products/box/event_examples/authorization_add_permission.json) | Timestamp=2023-05-18T12:57:12-07:00; Event ID=15f0f70a-4502-496a-badf-5a0b12e49656; Event Code / Type=COLLABORATION_INVITE; Username=jane@example.com; User ID=18863648385 |
| Authorization | Remove Permission | [remove](/products/box/event_examples/authorization_remove_permission.json) | Timestamp=2023-05-18T12:47:09-07:00; Event ID=052e68a2-7a29-4694-a77f-fec5713cb26f; Event Code / Type=COLLABORATION_REMOVE; Username=john@example.com; User ID=18863648385 |
| Authorization | Add Enrollment | [add](/products/box/event_examples/authorization_add_enrollment.json) | Timestamp=2023-05-09T09:27:03-07:00; Event ID=7fd655c7-5a4a-4e13-8375-dc08cd2cf8b9; Event Code / Type=MULTI_FACTOR_AUTH_ENABLE; Username=alice@example.com; User ID=18863648385 |
| Authorization | Remove Enrollment | [remove](/products/box/event_examples/authorization_remove_enrollment.json) | Timestamp=2023-05-09T09:29:19-07:00; Event ID=0bf5e6ad-a068-4770-9979-c7f409eb976b; Event Code / Type=MULTI_FACTOR_AUTH_DISABLE; Username=bob@example.com; User ID=18863648385 |
| Activity Audit | Create Resource | [create](/products/box/event_examples/activity_audit_create_resource.json) | Timestamp=2023-05-09T11:15:47-07:00; Event ID=aeffeb99-f9a5-4243-9d3c-93f862dceec7; Event Code / Type=UPLOAD; Username=mallory@example.com; User ID=18863648385 |
| Activity Audit | Read Resource | [read](/products/box/event_examples/activity_audit_read_resource.json) | Timestamp=2023-05-09T11:16:00-07:00; Event ID=80ddc3b3-dd44-4377-9fe7-a634228cc952; Event Code / Type=CONTENT_ACCESS; Username=jane@example.com; User ID=18863648385 |
| Activity Audit | Update Resource | [update](/products/box/event_examples/activity_audit_update_resource.json) | Timestamp=2023-05-09T11:30:38-07:00; Event ID=00000000-abcd-1234-8b08-418033e43a4b; Event Code / Type=RENAME; Username=john@example.com; User ID=12345678124 |
| Activity Audit | Delete Resource | [delete](/products/box/event_examples/activity_audit_delete_resource.json) | Timestamp=2023-05-09T11:15:12-07:00; Event ID=9fbcf20f-aeb7-4149-ab8e-3f56cab43337; Event Code / Type=DELETE; Username=alice@example.com; User ID=18863648385 |
| Activity Audit | Download Resource | [download](/products/box/event_examples/activity_audit_download_resource.json) | Timestamp=2023-05-09T11:14:52-07:00; Event ID=f70ed75d-9a96-4aac-aef8-5cce1a5c1eb8; Event Code / Type=DOWNLOAD; Username=bob@example.com; User ID=18863648385 |


