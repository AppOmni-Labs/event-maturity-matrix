





# Slack — Enterprise Audit Logs

📌 **v1.0.0** · 🗄 **Retention:** 2 years · ⚡ **Latency:** Near real-time

🗄 NA


⚡ NA


📜 **Licensing:** The Audit Logs API is only available to Slack workspaces on an Enterprise Grid plan.


Slack enterprise audit logs that provide an audit trail of user and system activity.
## References
* [Slack Audit Log Event Schema](https://api.slack.com/admins/audit-logs#audit-event)
* [Slack Audit Log Actions](https://api.slack.com/admins/audit-logs-call#actions)
* [Slack Audit Log Anomaly Events](https://api.slack.com/admins/audit-logs-anomaly)
## Field mappings

| Category | Event type | Attribute | Source field(s) |
| -------- | ---------- | --------- | ---------------- |
| Authentication | Account Login | Timestamp | date_create |
| Authentication | Account Login | Event ID | id |
| Authentication | Account Login | Event Code / Type | action |
| Authentication | Account Login | Username | entity.user.email |
| Authentication | Account Login | User ID | entity.user.id |
| Authentication | Account Login | Session ID | context.session_id |
| Authentication | Account Login | IP Address | context.ip_address |
| Authentication | Account Login | User Agent Name | context.ua |
| Authentication | Account Logout | Timestamp | date_create |
| Authentication | Account Logout | Event ID | id |
| Authentication | Account Logout | Event Code / Type | action |
| Authentication | Account Logout | Username | entity.user.email |
| Authentication | Account Logout | User ID | entity.user.id |
| Authentication | Account Logout | Session ID | context.session_id |
| Authentication | Account Logout | IP Address | context.ip_address |
| Authentication | Account Logout | User Agent Name | context.ua |
| Authorization | Create User | Timestamp | date_create |
| Authorization | Create User | Event ID | id |
| Authorization | Create User | Event Code / Type | action |
| Authorization | Create User | Username | actor.user.email |
| Authorization | Create User | User ID | entity.user.id |
| Authorization | Create User | Session ID | context.session_id |
| Authorization | Create User | IP Address | context.ip_address |
| Authorization | Create User | User Agent Name | context.ua |
| Authorization | Create User | Target Username | entity.user.email |
| Authorization | Update User | Timestamp | date_create |
| Authorization | Update User | Event ID | id |
| Authorization | Update User | Event Code / Type | action |
| Authorization | Update User | Username | actor.user.email |
| Authorization | Update User | User ID | entity.user.id |
| Authorization | Update User | Session ID | context.session_id |
| Authorization | Update User | IP Address | context.ip_address |
| Authorization | Update User | User Agent Name | context.ua |
| Authorization | Update User | Target Username | entity.user.email |
| Authorization | Update User | Target Attribute Context | details |
| Authorization | Delete User | Timestamp | date_create |
| Authorization | Delete User | Event ID | id |
| Authorization | Delete User | Event Code / Type | action |
| Authorization | Delete User | Username | actor.user.email |
| Authorization | Delete User | User ID | entity.user.id |
| Authorization | Delete User | Session ID | context.session_id |
| Authorization | Delete User | IP Address | context.ip_address |
| Authorization | Delete User | User Agent Name | context.ua |
| Authorization | Delete User | Target Username | entity.user.email |
| Authorization | Add To Group | Timestamp | date_create |
| Authorization | Add To Group | Event ID | id |
| Authorization | Add To Group | Event Code / Type | action |
| Authorization | Add To Group | Username | details.inviter.user.email |
| Authorization | Add To Group | User ID | details.inviter.user.id |
| Authorization | Add To Group | Session ID | context.session_id |
| Authorization | Add To Group | IP Address | context.ip_address |
| Authorization | Add To Group | User Agent Name | context.ua |
| Authorization | Add To Group | Target Username | entity.usergroup.name |
| Authorization | Remove From Group | Timestamp | date_create |
| Authorization | Remove From Group | Event ID | id |
| Authorization | Remove From Group | Event Code / Type | action |
| Authorization | Remove From Group | Username | details.kicker.user.email |
| Authorization | Remove From Group | User ID | details.kicker.user.id |
| Authorization | Remove From Group | Session ID | context.session_id |
| Authorization | Remove From Group | IP Address | context.ip_address |
| Authorization | Remove From Group | User Agent Name | context.ua |
| Authorization | Remove From Group | Target Username | actor.user.email |
| Authorization | Remove From Group | Target Group Name | entity.usergroup.name |
| Authorization | Create Role | Timestamp | date_create |
| Authorization | Create Role | Event ID | id |
| Authorization | Create Role | Event Code / Type | action |
| Authorization | Create Role | Username | actor.user.email |
| Authorization | Create Role | User ID | actor.user.id |
| Authorization | Create Role | Session ID | context.session_id |
| Authorization | Create Role | IP Address | context.ip_address |
| Authorization | Create Role | User Agent Name | context.ua |
| Authorization | Create Role | Target Role Name | entity.role.name |
| Authorization | Update Role | Timestamp | date_create |
| Authorization | Update Role | Event ID | id |
| Authorization | Update Role | Event Code / Type | action |
| Authorization | Update Role | Username | actor.user.email |
| Authorization | Update Role | User ID | actor.user.id |
| Authorization | Update Role | Session ID | context.session_id |
| Authorization | Update Role | IP Address | context.ip_address |
| Authorization | Update Role | User Agent Name | context.ua |
| Authorization | Update Role | Target Role Name | entity.role.name |
| Authorization | Delete Role | Timestamp | date_create |
| Authorization | Delete Role | Event ID | id |
| Authorization | Delete Role | Event Code / Type | action |
| Authorization | Delete Role | Username | actor.user.email |
| Authorization | Delete Role | User ID | actor.user.id |
| Authorization | Delete Role | Session ID | context.session_id |
| Authorization | Delete Role | IP Address | context.ip_address |
| Authorization | Delete Role | User Agent Name | context.ua |
| Authorization | Delete Role | Target Role Name | entity.role.name |
| Authorization | Add Permission | Timestamp | date_create |
| Authorization | Add Permission | Event ID | id |
| Authorization | Add Permission | Event Code / Type | action |
| Authorization | Add Permission | Username | actor.user.email |
| Authorization | Add Permission | User ID | actor.user.id |
| Authorization | Add Permission | Session ID | context.session_id |
| Authorization | Add Permission | IP Address | context.ip_address |
| Authorization | Add Permission | User Agent Name | context.ua |
| Authorization | Add Permission | Permission Name | entity.role.name |
| Authorization | Add Permission | Target Resource Name | details.target_user |
| Authorization | Remove Permission | Timestamp | date_create |
| Authorization | Remove Permission | Event ID | id |
| Authorization | Remove Permission | Event Code / Type | action |
| Authorization | Remove Permission | Username | actor.user.email |
| Authorization | Remove Permission | User ID | actor.user.id |
| Authorization | Remove Permission | Session ID | context.session_id |
| Authorization | Remove Permission | IP Address | context.ip_address |
| Authorization | Remove Permission | User Agent Name | context.ua |
| Authorization | Remove Permission | Permission Name | details.changed_permissions |
| Authorization | Remove Permission | Target Resource Name | entity.account_type_role.name |
| Authorization | Add Enrollment | Timestamp | date_create |
| Authorization | Add Enrollment | Event ID | id |
| Authorization | Add Enrollment | Event Code / Type | action |
| Authorization | Add Enrollment | Username | actor.user.email |
| Authorization | Add Enrollment | User ID | actor.user.id |
| Authorization | Add Enrollment | Session ID | context.session_id |
| Authorization | Add Enrollment | IP Address | context.ip_address |
| Authorization | Add Enrollment | User Agent Name | context.ua |
| Authorization | Remove Enrollment | Timestamp | date_create |
| Authorization | Remove Enrollment | Event ID | id |
| Authorization | Remove Enrollment | Event Code / Type | action |
| Authorization | Remove Enrollment | Username | actor.user.email |
| Authorization | Remove Enrollment | User ID | actor.user.id |
| Authorization | Remove Enrollment | Session ID | context.session_id |
| Authorization | Remove Enrollment | IP Address | context.ip_address |
| Authorization | Remove Enrollment | User Agent Name | context.ua |
| System Audit | Create Security Configuration | Timestamp | date_create |
| System Audit | Create Security Configuration | Event ID | id |
| System Audit | Create Security Configuration | Event Code / Type | action |
| System Audit | Create Security Configuration | Username | actor.user.email |
| System Audit | Create Security Configuration | User ID | actor.user.id |
| System Audit | Create Security Configuration | Session ID | context.session_id |
| System Audit | Create Security Configuration | IP Address | context.ip_address |
| System Audit | Create Security Configuration | User Agent Name | context.ua |
| System Audit | Create Security Configuration | Configuration / Setting Name | action |
| System Audit | Create Security Configuration | Configuration / Setting Value | details |
| System Audit | Update Security Configuration | Timestamp | date_create |
| System Audit | Update Security Configuration | Event ID | id |
| System Audit | Update Security Configuration | Event Code / Type | action |
| System Audit | Update Security Configuration | Username | actor.user.email |
| System Audit | Update Security Configuration | User ID | actor.user.id |
| System Audit | Update Security Configuration | Session ID | context.session_id |
| System Audit | Update Security Configuration | IP Address | context.ip_address |
| System Audit | Update Security Configuration | User Agent Name | context.ua |
| System Audit | Update Security Configuration | Configuration / Setting Name | action |
| System Audit | Update Security Configuration | Configuration / Setting Value | details.new_value |
| System Audit | Update Security Configuration | Previous Configuration / Setting Value | details.previous_value |
| System Audit | Delete Security Configuration | Timestamp | date_create |
| System Audit | Delete Security Configuration | Event ID | id |
| System Audit | Delete Security Configuration | Event Code / Type | action |
| System Audit | Delete Security Configuration | Username | actor.user.email |
| System Audit | Delete Security Configuration | User ID | actor.user.id |
| System Audit | Delete Security Configuration | Session ID | context.session_id |
| System Audit | Delete Security Configuration | IP Address | context.ip_address |
| System Audit | Delete Security Configuration | User Agent Name | context.ua |
| System Audit | Delete Security Configuration | Configuration / Setting Name | action |
| System Audit | Delete Security Configuration | Configuration / Setting Value | details |
| System Audit | Create Integration | Timestamp | date_create |
| System Audit | Create Integration | Event ID | id |
| System Audit | Create Integration | Event Code / Type | action |
| System Audit | Create Integration | Username | actor.user.email |
| System Audit | Create Integration | User ID | actor.user.id |
| System Audit | Create Integration | Session ID | context.session_id |
| System Audit | Create Integration | IP Address | context.ip_address |
| System Audit | Create Integration | User Agent Name | context.ua |
| System Audit | Create Integration | Integration / App Name | entity.app.name |
| System Audit | Update Integration | Timestamp | date_create |
| System Audit | Update Integration | Event ID | id |
| System Audit | Update Integration | Event Code / Type | action |
| System Audit | Update Integration | Username | actor.user.email |
| System Audit | Update Integration | User ID | actor.user.id |
| System Audit | Update Integration | Session ID | context.session_id |
| System Audit | Update Integration | IP Address | context.ip_address |
| System Audit | Update Integration | User Agent Name | context.ua |
| System Audit | Update Integration | Previous Configuration / Setting Value | details.previous_scopes |
| System Audit | Update Integration | Integration / App Name | entity.app.name |
| System Audit | Delete Integration | Timestamp | date_create |
| System Audit | Delete Integration | Event ID | id |
| System Audit | Delete Integration | Event Code / Type | action |
| System Audit | Delete Integration | Username | actor.user.email |
| System Audit | Delete Integration | User ID | actor.user.id |
| System Audit | Delete Integration | Session ID | context.session_id |
| System Audit | Delete Integration | IP Address | context.ip_address |
| System Audit | Delete Integration | User Agent Name | context.ua |
| System Audit | Delete Integration | Integration / App Name | entity.app.name |
| Activity Audit | Create Resource | Timestamp | date_create |
| Activity Audit | Create Resource | Event ID | id |
| Activity Audit | Create Resource | Event Code / Type | action |
| Activity Audit | Create Resource | Username | actor.user.email |
| Activity Audit | Create Resource | User ID | actor.user.id |
| Activity Audit | Create Resource | Session ID | context.session_id |
| Activity Audit | Create Resource | IP Address | context.ip_address |
| Activity Audit | Create Resource | User Agent Name | context.ua |
| Activity Audit | Create Resource | Resource Name | entity.file.name |
| Activity Audit | Create Resource | Resource Type | action |
| Activity Audit | Update Resource | Timestamp | date_create |
| Activity Audit | Update Resource | Event ID | id |
| Activity Audit | Update Resource | Event Code / Type | action |
| Activity Audit | Update Resource | Username | actor.user.email |
| Activity Audit | Update Resource | User ID | actor.user.id |
| Activity Audit | Update Resource | Session ID | context.session_id |
| Activity Audit | Update Resource | IP Address | context.ip_address |
| Activity Audit | Update Resource | User Agent Name | context.ua |
| Activity Audit | Update Resource | Resource Name | entity.channel.name |
| Activity Audit | Update Resource | Resource Type | entity.type |
| Activity Audit | Delete Resource | Timestamp | date_create |
| Activity Audit | Delete Resource | Event ID | id |
| Activity Audit | Delete Resource | Event Code / Type | action |
| Activity Audit | Delete Resource | Username | actor.user.email |
| Activity Audit | Delete Resource | User ID | actor.user.id |
| Activity Audit | Delete Resource | Session ID | context.session_id |
| Activity Audit | Delete Resource | IP Address | context.ip_address |
| Activity Audit | Delete Resource | User Agent Name | context.ua |
| Activity Audit | Delete Resource | Resource Name | entity.file.name |
| Activity Audit | Delete Resource | Resource Type | entity.type |
| Activity Audit | Download Resource | Timestamp | date_create |
| Activity Audit | Download Resource | Event ID | id |
| Activity Audit | Download Resource | Event Code / Type | action |
| Activity Audit | Download Resource | Username | actor.user.email |
| Activity Audit | Download Resource | User ID | actor.user.id |
| Activity Audit | Download Resource | Session ID | context.session_id |
| Activity Audit | Download Resource | IP Address | context.ip_address |
| Activity Audit | Download Resource | User Agent Name | context.ua |
| Activity Audit | Download Resource | Resource Name | entity.file.name |
| Activity Audit | Download Resource | Resource Type | entity.type |

## Example logs

| Category | Event type | Log | Sample field values |
| -------- | ---------- | --- | ------------------- |
| Authentication | Account Login | [success](/products/slack/event_examples/authentication_account_login_success.json) | Timestamp=1692033908; Event ID=44a8993d-0000-abcd-1e2f-9e7accba9876; Event Code / Type=user_login; Username=alice@example.com; User ID=U0123456ABC |
| Authentication | Account Login | [failure](/products/slack/event_examples/authentication_account_login_failure.json) | Timestamp=1692033735; Event ID=44a8993d-0000-abcd-1e2f-9e7accba9876; Event Code / Type=user_login_failed; Username=john@example.com; User ID=U0123456ABC |
| Authentication | Account Logout | [success](/products/slack/event_examples/authentication_account_logout.json) | Timestamp=1692033072; Event ID=44a8993d-0000-abcd-1e2f-9e7accba9876; Event Code / Type=user_logout; Username=bob@example.com; User ID=U0123456ABC |
| Authorization | Create User | [member](/products/slack/event_examples/authorization_create_user.json) | Timestamp=1691752039; Event ID=18ab534a-0000-4100-a123-aa12bb32ff35; Event Code / Type=user_created; Username=jane@example.com; User ID=U01AA2B2CAA |
| Authorization | Create User | [guest](/products/slack/event_examples/authorization_create_user_guest.json) | Timestamp=1691777609; Event ID=18ab534a-0000-4100-a123-aa12bb32ff35; Event Code / Type=guest_created; Username=jane@example.com; User ID=U01AA2B1CAA |
| Authorization | Update User | [success](/products/slack/event_examples/authorization_update_user.json) | Timestamp=1692023286; Event ID=18ab534a-0000-4100-a123-aa12bb32ff35; Event Code / Type=user_profile_updated; Username=jane@example.com; User ID=U7A1SSBCD |
| Authorization | Delete User | [success](/products/slack/event_examples/authorization_delete_user.json) | Timestamp=1691800883; Event ID=18ab534a-0000-4100-a123-aa12bb32ff35; Event Code / Type=user_deactivated; Username=jane@example.com; User ID=U05MA2B2CAA |
| Authorization | Add To Group | [success](/products/slack/event_examples/authorization_add_to_group.json) | Timestamp=1691766194; Event ID=1c0c1a15-5a11-4ac1-97a9-123fafa3f000; Event Code / Type=user_added_to_usergroup; Username=mallory@example.com; User ID=A01AAB1A5 |
| Authorization | Remove From Group | [success](/products/slack/event_examples/authorization_remove_from_group.json) | Timestamp=1692042606; Event ID=fde9d000-a1b2-3cc4-0000-aed1e3123f10; Event Code / Type=user_removed_from_usergroup; Username=bob@example.com; User ID=U0AA1BBC2AB |
| Authorization | Create Role | [success](/products/slack/event_examples/authorization_create_role.json) | Timestamp=1657550802; Event ID=1234f70-0fb0-00b1-00eb-95ab9a123d12; Event Code / Type=role_created; Username=john@example.com; User ID=U01A2ABCDNG |
| Authorization | Update Role | [success](/products/slack/event_examples/authorization_update_role.json) | Timestamp=1657550802; Event ID=1234f70-0fb0-00b1-00eb-95ab9a123d12; Event Code / Type=role_updated; Username=john@example.com; User ID=U01A2ABCDNG |
| Authorization | Delete Role | [success](/products/slack/event_examples/authorization_delete_role.json) | Timestamp=1657550802; Event ID=1234f70-0fb0-00b1-00eb-95ab9a123d12; Event Code / Type=role_deleted; Username=john@example.com; User ID=U01A2ABCDNG |
| Authorization | Add Permission | [assign_role](/products/slack/event_examples/authorization_add_permission_role_assigned.json) | Timestamp=1691650836; Event ID=00dba123-63a1-4564-bb11-000dd2140ae0; Event Code / Type=role_assigned; Username=Mallory@example.com; User ID=A012ABCDEFG |
| Authorization | Add Permission | [assign_admin](/products/slack/event_examples/authorization_add_permission_role_changed_to_admin.json) | Timestamp=1692081890; Event ID=a940a000-a0d0-00df-a123-b8b899ca6e31; Event Code / Type=role_change_to_admin; Username=alice@example.com; User ID=A012BCDDAB |
| Authorization | Remove Permission | [success](/products/slack/event_examples/authorization_remove_permission.json) | Timestamp=1692096526; Event ID=036ccefd-0000-abcd-bb11-000dd2140ae0; Event Code / Type=permissions_removed; Username=jane@example.com; User ID=U01A2ABCDAB |
| Authorization | Add Enrollment | [success](/products/slack/event_examples/authorization_add_enrollment.json) | Timestamp=1657550802; Event ID=1234f70-0fb0-00b1-00eb-95ab9a123d12; Event Code / Type=pref.two_factor_auth_changed; Username=john@example.com; User ID=U01A2ABCDNG |
| Authorization | Remove Enrollment | [success](/products/slack/event_examples/authorization_remove_enrollment.json) | Timestamp=1657550802; Event ID=1234f70-0fb0-00b1-00eb-95ab9a123d12; Event Code / Type=pref.two_factor_auth_changed; Username=john@example.com; User ID=U01A2ABCDNG |
| System Audit | Create Security Configuration | [success](/products/slack/event_examples/system_audit_create_security_configuration.json) | Timestamp=1693253017; Event ID=be00a00b-3200-4400-8ab0-000de3868a03; Event Code / Type=team_authorized_ip_range_set; Username=mallory@example.com; User ID=U01ABCA1AAD |
| System Audit | Update Security Configuration | [change_sso](/products/slack/event_examples/system_audit_update_security_configuration_sso_changed.json) | Timestamp=1693253139; Event ID=be00a00b-3200-4400-8ab0-000de3868a00; Event Code / Type=pref.sso_setting_changed; Username=john@example.com; User ID=U01ABCA1AAA |
| System Audit | Update Security Configuration | [unapproved_ip](/products/slack/event_examples/system_audit_update_security_configuration_unapproved_ip.json) | Timestamp=1693253017; Event ID=be00a00b-3200-4400-8ab0-000de3868a001; Event Code / Type=pref.block_file_download_for_unapproved_ip; Username=alice@example.com; User ID=U01ABCA1AAB |
| System Audit | Delete Security Configuration | [success](/products/slack/event_examples/system_audit_delete_security_configuration.json) | Timestamp=1693253039; Event ID=be00a00b-3200-4400-8ab0-000de3868a02; Event Code / Type=team_authorized_ip_range_set; Username=bob@example.com; User ID=U01ABCA1AAC |
| System Audit | Create Integration | [success](/products/slack/event_examples/system_audit_create_integration.json) | Timestamp=1692199107; Event ID=51d1abc1-0000-Ae1B-c2d3-65b5b0000a12; Event Code / Type=app_installed; Username=mallory@example.com; User ID=U05ABC123EF |
| System Audit | Update Integration | [success](/products/slack/event_examples/system_audit_update_integration.json) | Timestamp=1692192765; Event ID=51d1abc1-0000-Ae1B-c2d3-65b5b0000a12; Event Code / Type=app_scopes_expanded; Username=mallory@example.com; User ID=U05ABC123EF |
| System Audit | Delete Integration | [success](/products/slack/event_examples/system_audit_delete_integration.json) | Timestamp=1692197604; Event ID=51d1abc1-0000-Ae1B-c2d3-65b5b0000a12; Event Code / Type=app_uninstalled; Username=mallory@example.com; User ID=U05ABC123EF |
| Activity Audit | Create Resource | [success](/products/slack/event_examples/activity_audit_create_resource.json) | Timestamp=1692201912; Event ID=0ab1d7aa-00dc-0ef0-a0b1-0011a55ff12e; Event Code / Type=file_uploaded; Username=alice@example.com; User ID=U01ABA99AB1 |
| Activity Audit | Update Resource | [success](/products/slack/event_examples/activity_audit_update_resource.json) | Timestamp=1693247607; Event ID=0ab1d7aa-00dc-0ef0-a0b1-0011a55ff121; Event Code / Type=public_channel_converted_to_private; Username=jane@example.com; User ID=U01ABA99AB1 |
| Activity Audit | Delete Resource | [success](/products/slack/event_examples/activity_audit_delete_resource.json) | Timestamp=1692202048; Event ID=0ab1d7aa-00dc-0ef0-a0b1-0011a55ff12a; Event Code / Type=file_deleted; Username=bob@example.com; User ID=U01ABA99AB2 |
| Activity Audit | Download Resource | [success](/products/slack/event_examples/activity_audit_download_resource.json) | Timestamp=1692202187; Event ID=0ab1d7aa-00dc-0ef0-a0b1-0011a55ff12b; Event Code / Type=file_downloaded; Username=mallory@example.com; User ID=U01ABA99AB3 |


