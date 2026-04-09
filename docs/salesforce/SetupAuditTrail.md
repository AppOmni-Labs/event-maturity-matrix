





# Salesforce — SetupAuditTrail

📌 **v1.0.0** · 🗄 **Retention:** 180 Days · ⚡ **Latency:** Real-Time





📜 **Licensing:** Free


The SetupAuditTrail object provides an audit trail of changes to user profiles, permission sets, security settings, custom objects, and other settings.
## References
* [SetupAuditTrail](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_setupaudittrail.htm)
## Field mappings

| Category | Event type | Attribute | Source field(s) |
| -------- | ---------- | --------- | ---------------- |
| Authorization | Create User | Timestamp | sfdc_created_date |
| Authorization | Create User | Event ID | record_id |
| Authorization | Create User | Event Code / Type | action |
| Authorization | Create User | Username | sfdc_created_by_username |
| Authorization | Create User | User ID | sfdc_created_by_id |
| Authorization | Update User | Timestamp | sfdc_created_date |
| Authorization | Update User | Event ID | record_id |
| Authorization | Update User | Event Code / Type | action |
| Authorization | Update User | Username | sfdc_created_by_username |
| Authorization | Update User | User ID | sfdc_created_by_id |
| Authorization | Update User | Target Attribute Context | display |
| Authorization | Delete User | Timestamp | sfdc_created_date |
| Authorization | Delete User | Event ID | record_id |
| Authorization | Delete User | Event Code / Type | action |
| Authorization | Delete User | Username | sfdc_created_by_username |
| Authorization | Delete User | User ID | sfdc_created_by_id |
| Authorization | Delete User | Target Attribute Context | display |
| Authorization | Create Group | Timestamp | sfdc_created_date |
| Authorization | Create Group | Event ID | record_id |
| Authorization | Create Group | Event Code / Type | action |
| Authorization | Create Group | Username | sfdc_created_by_username |
| Authorization | Create Group | User ID | sfdc_created_by_id |
| Authorization | Create Group | Target Group Name | display |
| Authorization | Update Group | Timestamp | sfdc_created_date |
| Authorization | Update Group | Event ID | record_id |
| Authorization | Update Group | Event Code / Type | action |
| Authorization | Update Group | Username | sfdc_created_by_username |
| Authorization | Update Group | User ID | sfdc_created_by_id |
| Authorization | Update Group | Target Attribute Context | display |
| Authorization | Update Group | Target Group Name | display |
| Authorization | Delete Group | Timestamp | sfdc_created_date |
| Authorization | Delete Group | Event ID | record_id |
| Authorization | Delete Group | Event Code / Type | action |
| Authorization | Delete Group | Username | sfdc_created_by_username |
| Authorization | Delete Group | User ID | sfdc_created_by_id |
| Authorization | Delete Group | Target Group Name | display |
| Authorization | Add To Group | Timestamp | sfdc_created_date |
| Authorization | Add To Group | Event ID | record_id |
| Authorization | Add To Group | Event Code / Type | action |
| Authorization | Add To Group | Username | sfdc_created_by_username |
| Authorization | Add To Group | User ID | sfdc_created_by_id |
| Authorization | Add To Group | Target Group Name | display |
| Authorization | Remove From Group | Timestamp | sfdc_created_date |
| Authorization | Remove From Group | Event ID | record_id |
| Authorization | Remove From Group | Event Code / Type | action |
| Authorization | Remove From Group | Username | sfdc_created_by_username |
| Authorization | Remove From Group | User ID | sfdc_created_by_id |
| Authorization | Remove From Group | Target Group Name | display |
| Authorization | Create Role | Timestamp | sfdc_created_date |
| Authorization | Create Role | Event ID | record_id |
| Authorization | Create Role | Event Code / Type | action |
| Authorization | Create Role | Username | sfdc_created_by_username |
| Authorization | Create Role | User ID | sfdc_created_by_id |
| Authorization | Create Role | Target Role Name | display |
| Authorization | Update Role | Timestamp | sfdc_created_date |
| Authorization | Update Role | Event ID | record_id |
| Authorization | Update Role | Event Code / Type | action |
| Authorization | Update Role | Username | sfdc_created_by_username |
| Authorization | Update Role | User ID | sfdc_created_by_id |
| Authorization | Update Role | Target Attribute Context | display |
| Authorization | Update Role | Target Role Name | display |
| Authorization | Delete Role | Timestamp | sfdc_created_date |
| Authorization | Delete Role | Event ID | record_id |
| Authorization | Delete Role | Event Code / Type | action |
| Authorization | Delete Role | Username | sfdc_created_by_username |
| Authorization | Delete Role | User ID | sfdc_created_by_id |
| Authorization | Delete Role | Target Role Name | display |
| Authorization | Add Permission | Timestamp | sfdc_created_date |
| Authorization | Add Permission | Event ID | record_id |
| Authorization | Add Permission | Event Code / Type | action |
| Authorization | Add Permission | Username | sfdc_created_by_username |
| Authorization | Add Permission | User ID | sfdc_created_by_id |
| Authorization | Add Permission | Permission Name | display |
| Authorization | Add Permission | Target Resource Name | display |
| Authorization | Remove Permission | Timestamp | sfdc_created_date |
| Authorization | Remove Permission | Event ID | record_id |
| Authorization | Remove Permission | Event Code / Type | action |
| Authorization | Remove Permission | Username | sfdc_created_by_username |
| Authorization | Remove Permission | User ID | sfdc_created_by_id |
| Authorization | Remove Permission | Permission Name | display |
| Authorization | Remove Permission | Target Resource Name | display |
| Authorization | Add Enrollment | Timestamp | sfdc_created_date |
| Authorization | Add Enrollment | Event ID | record_id |
| Authorization | Add Enrollment | Event Code / Type | action |
| Authorization | Add Enrollment | Username | sfdc_created_by_username |
| Authorization | Add Enrollment | User ID | sfdc_created_by_id |
| Authorization | Add Enrollment | Target Username | display |
| Authorization | Add Enrollment | Enrollment Type | display |
| Authorization | Remove Enrollment | Timestamp | sfdc_created_date |
| Authorization | Remove Enrollment | Event ID | record_id |
| Authorization | Remove Enrollment | Event Code / Type | action |
| Authorization | Remove Enrollment | Username | sfdc_created_by_username |
| Authorization | Remove Enrollment | User ID | sfdc_created_by_id |
| Authorization | Remove Enrollment | Target Username | display |
| Authorization | Remove Enrollment | Enrollment Type | display |
| System Audit | Create Security Configuration | Timestamp | sfdc_created_date |
| System Audit | Create Security Configuration | Event ID | record_id |
| System Audit | Create Security Configuration | Event Code / Type | action |
| System Audit | Create Security Configuration | Username | sfdc_created_by_username |
| System Audit | Create Security Configuration | User ID | sfdc_created_by_id |
| System Audit | Create Security Configuration | Configuration / Setting Name | display |
| System Audit | Update Security Configuration | Timestamp | sfdc_created_date |
| System Audit | Update Security Configuration | Event ID | record_id |
| System Audit | Update Security Configuration | Event Code / Type | action |
| System Audit | Update Security Configuration | Username | sfdc_created_by_username |
| System Audit | Update Security Configuration | User ID | sfdc_created_by_id |
| System Audit | Update Security Configuration | Configuration / Setting Name | display |
| System Audit | Delete Security Configuration | Timestamp | sfdc_created_date |
| System Audit | Delete Security Configuration | Event ID | record_id |
| System Audit | Delete Security Configuration | Event Code / Type | action |
| System Audit | Delete Security Configuration | Username | sfdc_created_by_username |
| System Audit | Delete Security Configuration | User ID | sfdc_created_by_id |
| System Audit | Delete Security Configuration | Configuration / Setting Name | display |
| System Audit | Create Integration | Timestamp | sfdc_created_date |
| System Audit | Create Integration | Event ID | record_id |
| System Audit | Create Integration | Event Code / Type | action |
| System Audit | Create Integration | Username | sfdc_created_by_username |
| System Audit | Create Integration | User ID | sfdc_created_by_id |
| System Audit | Create Integration | Integration / App Name | display |
| System Audit | Update Integration | Timestamp | sfdc_created_date |
| System Audit | Update Integration | Event ID | record_id |
| System Audit | Update Integration | Event Code / Type | action |
| System Audit | Update Integration | Username | sfdc_created_by_username |
| System Audit | Update Integration | User ID | sfdc_created_by_id |
| System Audit | Update Integration | Integration / App Name | display |
| System Audit | Delete Integration | Timestamp | sfdc_created_date |
| System Audit | Delete Integration | Event ID | record_id |
| System Audit | Delete Integration | Event Code / Type | action |
| System Audit | Delete Integration | Username | sfdc_created_by_username |
| System Audit | Delete Integration | User ID | sfdc_created_by_id |
| System Audit | Delete Integration | Integration / App Name | display |

## Example logs

| Category | Event type | Log | Sample field values |
| -------- | ---------- | --- | ------------------- |
| Authorization | Create User | [create](/products/salesforce/event_examples/setup_audit_trail/authorization_create_user.json) | Timestamp=2023-03-09T16:51:17+00:00; Event ID=000000000000123AbC; Event Code / Type=createduser; Username=john@example.com; User ID=000000000000123AbC |
| Authorization | Update User | [update](/products/salesforce/event_examples/setup_audit_trail/authorization_update_user.json) | Timestamp=2023-03-09T17:41:59+00:00; Event ID=000000000000123AbC; Event Code / Type=changedemail; Username=bob@example.com; User ID=000000000000123AbC |
| Authorization | Delete User | [disable](/products/salesforce/event_examples/setup_audit_trail/authorization_delete_user.json) | Timestamp=2023-03-09T17:50:17+00:00; Event ID=000000000000123AbC; Event Code / Type=deactivateduser; Username=john@example.com; User ID=000000000000123AbC |
| Authorization | Create Group | [create](/products/salesforce/event_examples/setup_audit_trail/authorization_create_group.json) | Timestamp=2023-03-09T18:14:43+00:00; Event ID=000000000000123AbC; Event Code / Type=createdgroup; Username=john@example.com; User ID=000000000000123AbC |
| Authorization | Update Group | [update](/products/salesforce/event_examples/setup_audit_trail/authorization_update_group.json) | Timestamp=2023-03-07T13:18:30+00:00; Event ID=000000000000123AbC; Event Code / Type=updatedgroup; Username=alice@example.com; User ID=000000000000123AbC |
| Authorization | Delete Group | [delete](/products/salesforce/event_examples/setup_audit_trail/authorization_delete_group.json) | Timestamp=2023-03-09T18:17:00+00:00; Event ID=000000000000123AbC; Event Code / Type=deletedgroup; Username=john@example.com; User ID=000000000000123AbC |
| Authorization | Add To Group | [add](/products/salesforce/event_examples/setup_audit_trail/authorization_add_to_group.json) | Timestamp=2023-03-09T19:15:35+00:00; Event ID=000000000000123AbC; Event Code / Type=groupMembership; Username=john@example.com; User ID=000000000000123AbC |
| Authorization | Remove From Group | [remove](/products/salesforce/event_examples/setup_audit_trail/authorization_remove_fom_group.json) | Timestamp=2023-03-09T19:15:35+00:00; Event ID=000000000000123AbC; Event Code / Type=groupMembership; Username=john@example.com; User ID=000000000000123AbC |
| Authorization | Create Role | [create](/products/salesforce/event_examples/setup_audit_trail/authorization_create_role.json) | Timestamp=2023-03-09T21:16:28+00:00; Event ID=000000000000123AbC; Event Code / Type=profileClonedStandard; Username=john@example.com; User ID=000000000000123AbC |
| Authorization | Update Role | [update](/products/salesforce/event_examples/setup_audit_trail/authorization_update_role.json) | Timestamp=2023-03-09T18:56:52+00:00; Event ID=000000000000123AbC; Event Code / Type=SetupEntityAccessAudit_Profile_ConnectedApplication_Enabled…; Username=john@example.com; User ID=000000000000123AbC |
| Authorization | Add Permission | [add](/products/salesforce/event_examples/setup_audit_trail/authorization_add_permission.json) | Timestamp=2023-03-08T18:43:00+00:00; Event ID=000000000000123AbC; Event Code / Type=PermSetEnableUserPerm; Username=bob@example.com; User ID=000000000000123AbC |
| Authorization | Remove Permission | [remove](/products/salesforce/event_examples/setup_audit_trail/authorization_remove_permission.json) | Timestamp=2023-03-09T08:59:49+00:00; Event ID=000000000000123AbC; Event Code / Type=PermSetDisableUserPerm; Username=alice@example.com; User ID=000000000000123AbC |
| Authorization | Add Enrollment | [add](/products/salesforce/event_examples/setup_audit_trail/authorization_add_enrollment.json) | Timestamp=2023-03-10T14:04:29+00:00; Event ID=000000000000123AbC; Event Code / Type=insertAuthenticatorPairing; Username=john@example.com; User ID=000000000000123AbC |
| Authorization | Remove Enrollment | [remove](/products/salesforce/event_examples/setup_audit_trail/authorization_remove_enrollment.json) | Timestamp=2023-03-10T13:35:40+00:00; Event ID=000000000000123AbC; Event Code / Type=deleteTwoFactorInfo2; Username=john@example.com; User ID=000000000000123AbC |
| System Audit | Create Security Configuration | [create](/products/salesforce/event_examples/setup_audit_trail/system_audit_create_configuration.json) | Timestamp=2023-03-15T07:14:10+00:00; Event ID=000000000000123AbC; Event Code / Type=tenantSecretCreated; Username=john@example.com; User ID=000000000000123AbC |
| System Audit | Update Security Configuration | [update](/products/salesforce/event_examples/setup_audit_trail/system_audit_update_configuration.json) | Timestamp=2023-03-15T13:11:50+00:00; Event ID=000000000000123AbC; Event Code / Type=passwordexpiry; Username=john@example.com; User ID=000000000000123AbC |
| System Audit | Delete Security Configuration | [delete](/products/salesforce/event_examples/setup_audit_trail/system_audit_delete_configuration.json) | Timestamp=2023-03-15T09:50:12+00:00; Event ID=000000000000123AbC; Event Code / Type=deletedLoginIpRange_withProfile; Username=john@example.com; User ID=000000000000123AbC |
| System Audit | Create Integration | [create](/products/salesforce/event_examples/setup_audit_trail/system_audit_create_integration.json) | Timestamp=2023-03-15T03:55:58+00:00; Event ID=000000000000123AbC; Event Code / Type=installedpackagingapp; Username=john@example.com; User ID=000000000000123AbC |
| System Audit | Update Integration | [update](/products/salesforce/event_examples/setup_audit_trail/system_audit_update_integration.json) | Timestamp=2023-03-15T13:17:28+00:00; Event ID=000000000000123AbC; Event Code / Type=upgradedpackagingapp; Username=john@example.com; User ID=000000000000123AbC |
| System Audit | Delete Integration | [delete](/products/salesforce/event_examples/setup_audit_trail/system_audit_delete_integration.json) | Timestamp=2023-03-14T14:50:28+00:00; Event ID=000000000000123AbC; Event Code / Type=uninstalledpackagingapp; Username=john@example.com; User ID=000000000000123AbC |


