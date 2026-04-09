





# Workday — User Activity Logs

📌 **v1.0.0** · 🗄 **Retention:** 30 days · ⚡ **Latency:** Near real-time

🗄 By default, the User Activity Logging REST API retains log entries for 30 days.




📜 **Licensing:** User Activity Logging is available to Workday customers.


Workday user activity logs provide an audit trail of user activity over a certain time period.
## References
* [Workday Activity Log Schema](https://doc.workday.com/admin-guide/en-us/human-capital-management/unv1636547598141.html)
## Field mappings

| Category | Event type | Attribute | Source field(s) |
| -------- | ---------- | --------- | ---------------- |
| Authorization | Create User | Timestamp | requestTime |
| Authorization | Create User | Event Code / Type | taskDisplayName |
| Authorization | Create User | Result | activityAction |
| Authorization | Create User | Username | systemAccount |
| Authorization | Create User | Session ID | sessionId |
| Authorization | Create User | IP Address | ipAddress |
| Authorization | Create User | User Agent Name | userAgent |
| Authorization | Create User | Device/Client Type | deviceType |
| Authorization | Create User | Target Username | target.descriptor |
| Authorization | Read User | Timestamp | requestTime |
| Authorization | Read User | Event Code / Type | taskDisplayName |
| Authorization | Read User | Result | activityAction |
| Authorization | Read User | Username | systemAccount |
| Authorization | Read User | Session ID | sessionId |
| Authorization | Read User | IP Address | ipAddress |
| Authorization | Read User | User Agent Name | userAgent |
| Authorization | Read User | Device/Client Type | deviceType |
| Authorization | Read User | Target Username | target.descriptor |
| Authorization | Update User | Timestamp | requestTime |
| Authorization | Update User | Event Code / Type | taskDisplayName |
| Authorization | Update User | Result | activityAction |
| Authorization | Update User | Username | systemAccount |
| Authorization | Update User | Session ID | sessionId |
| Authorization | Update User | IP Address | ipAddress |
| Authorization | Update User | User Agent Name | userAgent |
| Authorization | Update User | Device/Client Type | deviceType |
| Authorization | Update User | Target Username | target.descriptor |
| Authorization | Create Group | Timestamp | requestTime |
| Authorization | Create Group | Event Code / Type | taskDisplayName |
| Authorization | Create Group | Result | activityAction |
| Authorization | Create Group | Username | systemAccount |
| Authorization | Create Group | Session ID | sessionId |
| Authorization | Create Group | IP Address | ipAddress |
| Authorization | Create Group | User Agent Name | userAgent |
| Authorization | Create Group | Device/Client Type | deviceType |
| Authorization | Create Group | Target Group Name | target.descriptor |
| Authorization | Read Group | Timestamp | requestTime |
| Authorization | Read Group | Event Code / Type | taskDisplayName |
| Authorization | Read Group | Result | activityAction |
| Authorization | Read Group | Username | systemAccount |
| Authorization | Read Group | Session ID | sessionId |
| Authorization | Read Group | IP Address | ipAddress |
| Authorization | Read Group | User Agent Name | userAgent |
| Authorization | Read Group | Device/Client Type | deviceType |
| Authorization | Read Group | Target Group Name | target.descriptor |
| Authorization | Update Group | Timestamp | requestTime |
| Authorization | Update Group | Event Code / Type | taskDisplayName |
| Authorization | Update Group | Result | activityAction |
| Authorization | Update Group | Username | systemAccount |
| Authorization | Update Group | Session ID | sessionId |
| Authorization | Update Group | IP Address | ipAddress |
| Authorization | Update Group | User Agent Name | userAgent |
| Authorization | Update Group | Device/Client Type | deviceType |
| Authorization | Update Group | Target Group Name | target.descriptor |
| Authorization | Delete Group | Timestamp | requestTime |
| Authorization | Delete Group | Event Code / Type | taskDisplayName |
| Authorization | Delete Group | Result | activityAction |
| Authorization | Delete Group | Username | systemAccount |
| Authorization | Delete Group | Session ID | sessionId |
| Authorization | Delete Group | IP Address | ipAddress |
| Authorization | Delete Group | User Agent Name | userAgent |
| Authorization | Delete Group | Device/Client Type | deviceType |
| Authorization | Add To Group | Timestamp | requestTime |
| Authorization | Add To Group | Event Code / Type | taskDisplayName |
| Authorization | Add To Group | Result | activityAction |
| Authorization | Add To Group | Username | systemAccount |
| Authorization | Add To Group | Session ID | sessionId |
| Authorization | Add To Group | IP Address | ipAddress |
| Authorization | Add To Group | User Agent Name | userAgent |
| Authorization | Add To Group | Device/Client Type | deviceType |
| Authorization | Add To Group | Target Group Name | target.descriptor |
| Authorization | Remove From Group | Timestamp | requestTime |
| Authorization | Remove From Group | Event Code / Type | taskDisplayName |
| Authorization | Remove From Group | Result | activityAction |
| Authorization | Remove From Group | Username | systemAccount |
| Authorization | Remove From Group | Session ID | sessionId |
| Authorization | Remove From Group | IP Address | ipAddress |
| Authorization | Remove From Group | User Agent Name | userAgent |
| Authorization | Remove From Group | Device/Client Type | deviceType |
| Authorization | Remove From Group | Target Group Name | target.descriptor |
| Authorization | Read Role | Timestamp | requestTime |
| Authorization | Read Role | Event Code / Type | taskDisplayName |
| Authorization | Read Role | Result | activityAction |
| Authorization | Read Role | Username | systemAccount |
| Authorization | Read Role | Session ID | sessionId |
| Authorization | Read Role | IP Address | ipAddress |
| Authorization | Read Role | User Agent Name | userAgent |
| Authorization | Read Role | Device/Client Type | deviceType |
| Authorization | Update Role | Timestamp | requestTime |
| Authorization | Update Role | Event Code / Type | taskDisplayName |
| Authorization | Update Role | Result | activityAction |
| Authorization | Update Role | Username | systemAccount |
| Authorization | Update Role | Session ID | sessionId |
| Authorization | Update Role | IP Address | ipAddress |
| Authorization | Update Role | User Agent Name | userAgent |
| Authorization | Update Role | Device/Client Type | deviceType |
| Authorization | Update Role | Target Role Name | target.descriptor |
| Authorization | Add Permission | Timestamp | requestTime |
| Authorization | Add Permission | Event Code / Type | taskDisplayName |
| Authorization | Add Permission | Result | activityAction |
| Authorization | Add Permission | Username | systemAccount |
| Authorization | Add Permission | Session ID | sessionId |
| Authorization | Add Permission | IP Address | ipAddress |
| Authorization | Add Permission | User Agent Name | userAgent |
| Authorization | Add Permission | Device/Client Type | deviceType |
| Authorization | Add Permission | Target Resource Name | target.descriptor |
| Authorization | Remove Permission | Timestamp | requestTime |
| Authorization | Remove Permission | Event Code / Type | taskDisplayName |
| Authorization | Remove Permission | Result | activityAction |
| Authorization | Remove Permission | Username | systemAccount |
| Authorization | Remove Permission | Session ID | sessionId |
| Authorization | Remove Permission | IP Address | ipAddress |
| Authorization | Remove Permission | User Agent Name | userAgent |
| Authorization | Remove Permission | Device/Client Type | deviceType |
| Authorization | Remove Permission | Target Resource Name | target.descriptor |
| Authorization | Add Enrollment | Timestamp | requestTime |
| Authorization | Add Enrollment | Event Code / Type | taskDisplayName |
| Authorization | Add Enrollment | Result | activityAction |
| Authorization | Add Enrollment | Username | systemAccount |
| Authorization | Add Enrollment | Session ID | sessionId |
| Authorization | Add Enrollment | IP Address | ipAddress |
| Authorization | Add Enrollment | User Agent Name | userAgent |
| Authorization | Add Enrollment | Device/Client Type | deviceType |
| Authorization | Add Enrollment | Enrollment Type | taskDisplayName |
| Authorization | Remove Enrollment | Timestamp | requestTime |
| Authorization | Remove Enrollment | Event Code / Type | taskDisplayName |
| Authorization | Remove Enrollment | Result | activityAction |
| Authorization | Remove Enrollment | Username | systemAccount |
| Authorization | Remove Enrollment | Session ID | sessionId |
| Authorization | Remove Enrollment | IP Address | ipAddress |
| Authorization | Remove Enrollment | User Agent Name | userAgent |
| Authorization | Remove Enrollment | Device/Client Type | deviceType |
| Authorization | Remove Enrollment | Enrollment Type | taskDisplayName |
| System Audit | Create Security Configuration | Timestamp | requestTime |
| System Audit | Create Security Configuration | Event Code / Type | taskDisplayName |
| System Audit | Create Security Configuration | Result | activityAction |
| System Audit | Create Security Configuration | Username | systemAccount |
| System Audit | Create Security Configuration | Session ID | sessionId |
| System Audit | Create Security Configuration | IP Address | ipAddress |
| System Audit | Create Security Configuration | User Agent Name | userAgent |
| System Audit | Create Security Configuration | Device/Client Type | deviceType |
| System Audit | Create Security Configuration | Configuration / Setting Name | target.descriptor |
| System Audit | Read Security Configuration | Timestamp | requestTime |
| System Audit | Read Security Configuration | Event Code / Type | taskDisplayName |
| System Audit | Read Security Configuration | Result | activityAction |
| System Audit | Read Security Configuration | Username | systemAccount |
| System Audit | Read Security Configuration | Session ID | sessionId |
| System Audit | Read Security Configuration | IP Address | ipAddress |
| System Audit | Read Security Configuration | User Agent Name | userAgent |
| System Audit | Read Security Configuration | Device/Client Type | deviceType |
| System Audit | Read Security Configuration | Configuration / Setting Value | target.descriptor |
| System Audit | Update Security Configuration | Timestamp | requestTime |
| System Audit | Update Security Configuration | Event Code / Type | taskDisplayName |
| System Audit | Update Security Configuration | Result | activityAction |
| System Audit | Update Security Configuration | Username | systemAccount |
| System Audit | Update Security Configuration | Session ID | sessionId |
| System Audit | Update Security Configuration | IP Address | ipAddress |
| System Audit | Update Security Configuration | User Agent Name | userAgent |
| System Audit | Update Security Configuration | Device/Client Type | deviceType |
| System Audit | Update Security Configuration | Configuration / Setting Name | target.descriptor |
| System Audit | Delete Security Configuration | Timestamp | requestTime |
| System Audit | Delete Security Configuration | Event Code / Type | taskDisplayName |
| System Audit | Delete Security Configuration | Result | activityAction |
| System Audit | Delete Security Configuration | Username | systemAccount |
| System Audit | Delete Security Configuration | Session ID | sessionId |
| System Audit | Delete Security Configuration | IP Address | ipAddress |
| System Audit | Delete Security Configuration | User Agent Name | userAgent |
| System Audit | Delete Security Configuration | Device/Client Type | deviceType |
| System Audit | Delete Security Configuration | Configuration / Setting Name | target.descriptor |
| System Audit | Create Integration | Timestamp | requestTime |
| System Audit | Create Integration | Event Code / Type | taskDisplayName |
| System Audit | Create Integration | Result | activityAction |
| System Audit | Create Integration | Username | systemAccount |
| System Audit | Create Integration | Session ID | sessionId |
| System Audit | Create Integration | IP Address | ipAddress |
| System Audit | Create Integration | User Agent Name | userAgent |
| System Audit | Create Integration | Device/Client Type | deviceType |
| System Audit | Create Integration | Integration / App Name | target.descriptor |
| System Audit | Read Integration | Timestamp | requestTime |
| System Audit | Read Integration | Event Code / Type | taskDisplayName |
| System Audit | Read Integration | Result | activityAction |
| System Audit | Read Integration | Username | systemAccount |
| System Audit | Read Integration | Session ID | sessionId |
| System Audit | Read Integration | IP Address | ipAddress |
| System Audit | Read Integration | User Agent Name | userAgent |
| System Audit | Read Integration | Device/Client Type | deviceType |
| System Audit | Update Integration | Timestamp | requestTime |
| System Audit | Update Integration | Event Code / Type | taskDisplayName |
| System Audit | Update Integration | Result | activityAction |
| System Audit | Update Integration | Username | systemAccount |
| System Audit | Update Integration | Session ID | sessionId |
| System Audit | Update Integration | IP Address | ipAddress |
| System Audit | Update Integration | User Agent Name | userAgent |
| System Audit | Update Integration | Device/Client Type | deviceType |
| System Audit | Update Integration | Integration / App Name | target.descriptor |
| Activity Audit | Create Resource | Timestamp | requestTime |
| Activity Audit | Create Resource | Event Code / Type | taskDisplayName |
| Activity Audit | Create Resource | Result | activityAction |
| Activity Audit | Create Resource | Username | systemAccount |
| Activity Audit | Create Resource | Session ID | sessionId |
| Activity Audit | Create Resource | IP Address | ipAddress |
| Activity Audit | Create Resource | User Agent Name | userAgent |
| Activity Audit | Create Resource | Device/Client Type | deviceType |
| Activity Audit | Create Resource | Resource Name | target.descriptor |
| Activity Audit | Read Resource | Timestamp | requestTime |
| Activity Audit | Read Resource | Event Code / Type | taskDisplayName |
| Activity Audit | Read Resource | Result | activityAction |
| Activity Audit | Read Resource | Username | systemAccount |
| Activity Audit | Read Resource | Session ID | sessionId |
| Activity Audit | Read Resource | IP Address | ipAddress |
| Activity Audit | Read Resource | User Agent Name | userAgent |
| Activity Audit | Read Resource | Device/Client Type | deviceType |
| Activity Audit | Read Resource | Resource Name | target.descriptor |
| Activity Audit | Update Resource | Timestamp | requestTime |
| Activity Audit | Update Resource | Event Code / Type | taskDisplayName |
| Activity Audit | Update Resource | Result | activityAction |
| Activity Audit | Update Resource | Username | systemAccount |
| Activity Audit | Update Resource | Session ID | sessionId |
| Activity Audit | Update Resource | IP Address | ipAddress |
| Activity Audit | Update Resource | User Agent Name | userAgent |
| Activity Audit | Update Resource | Device/Client Type | deviceType |
| Activity Audit | Update Resource | Resource Name | target.descriptor |
| Activity Audit | Delete Resource | Timestamp | requestTime |
| Activity Audit | Delete Resource | Event Code / Type | taskDisplayName |
| Activity Audit | Delete Resource | Result | activityAction |
| Activity Audit | Delete Resource | Username | systemAccount |
| Activity Audit | Delete Resource | Session ID | sessionId |
| Activity Audit | Delete Resource | IP Address | ipAddress |
| Activity Audit | Delete Resource | User Agent Name | userAgent |
| Activity Audit | Delete Resource | Device/Client Type | deviceType |
| Activity Audit | Download Resource | Timestamp | requestTime |
| Activity Audit | Download Resource | Result | taskDisplayName |
| Activity Audit | Download Resource | Username | systemAccount |
| Activity Audit | Download Resource | Session ID | sessionId |
| Activity Audit | Download Resource | IP Address | ipAddress |
| Activity Audit | Download Resource | User Agent Name | userAgent |
| Activity Audit | Download Resource | Device/Client Type | deviceType |
| Activity Audit | Download Resource | Resource Name | target.descriptor |

## Example logs

| Category | Event type | Log | Sample field values |
| -------- | ---------- | --- | ------------------- |
| Authorization | Create User | [success](/products/workday/event_examples/authorization_create_user.json) | Timestamp=2024-04-15T12:09:31.763Z; Event Code / Type=Create Workday Account; Result=WRITE; Username=test.user@acme.com; Session ID=495269 |
| Authorization | Read User | [success](/products/workday/event_examples/authorization_read_user.json) | Timestamp=2024-04-24T14:32:40.272Z; Event Code / Type=View Workday Account; Result=READ; Username=test.user@acme.com; Session ID=dd7803 |
| Authorization | Update User | [success](/products/workday/event_examples/authorization_update_user.json) | Timestamp=2024-04-22T12:06:18.499Z; Event Code / Type=Edit Workday Account; Result=WRITE; Username=test.user@acme.com; Session ID=208afc |
| Authorization | Create Group | [success](/products/workday/event_examples/authorization_create_group.json) | Timestamp=2024-04-22T11:17:40.737Z; Event Code / Type=Create Security Group; Result=WRITE; Username=test.user@acme.com; Session ID=b4dc5b |
| Authorization | Read Group | [success](/products/workday/event_examples/authorization_read_group.json) | Timestamp=2024-04-29T15:57:47.459Z; Event Code / Type=View Security Group; Result=READ; Username=test.user@acme.com; Session ID=692dd8 |
| Authorization | Update Group | [success](/products/workday/event_examples/authorization_update_group.json) | Timestamp=2024-04-29T15:59:18.710Z; Event Code / Type=Edit User-Based Security Group; Result=WRITE; Username=test.user@acme.com; Session ID=692dd8 |
| Authorization | Delete Group | [success](/products/workday/event_examples/authorization_delete_group.json) | Timestamp=2024-04-29T16:00:31.986Z; Event Code / Type=Delete Security Group; Result=WRITE; Username=test.user@acme.com; Session ID=692dd8 |
| Authorization | Add To Group | [success](/products/workday/event_examples/authorization_add_to_group.json) | Timestamp=2024-04-29T16:09:37.206Z; Event Code / Type=Assign Users to User-Based Security Group; Result=WRITE; Username=test.user@acme.com; Session ID=692dd8 |
| Authorization | Remove From Group | [success](/products/workday/event_examples/authorization_remove_from_group.json) | Timestamp=2024-04-29T16:09:37.206Z; Event Code / Type=Assign Users to User-Based Security Group; Result=WRITE; Username=test.user@acme.com; Session ID=692dd8 |
| Authorization | Read Role | [success](/products/workday/event_examples/authorization_read_role.json) | Timestamp=2024-04-29T17:05:55.030Z; Event Code / Type=Role Assignment Permissions; Result=READ; Username=test.user@acme.com; Session ID=d025f2 |
| Authorization | Update Role | [success](/products/workday/event_examples/authorization_update_role.json) | Timestamp=2024-04-29T16:12:45.263Z; Event Code / Type=Edit Role Assignment Permissions; Result=WRITE; Username=test.user@acme.com; Session ID=692dd8 |
| Authorization | Add Permission | [success](/products/workday/event_examples/authorization_add_permission.json) | Timestamp=2024-04-25T17:45:31.612Z; Event Code / Type=Edit Domain Security Policy Permissions; Result=WRITE; Username=test.user@acme.com; Session ID=a6259b |
| Authorization | Remove Permission | [success](/products/workday/event_examples/authorization_remove_permission.json) | Timestamp=2024-04-22T19:18:56.858Z; Event Code / Type=Edit Permissions; Result=WRITE; Username=test.user@acme.com; Session ID=8413e1 |
| Authorization | Add Enrollment | [success](/products/workday/event_examples/authorization_add_enrollment.json) | Timestamp=2024-04-15T23:06:03.915Z; Event Code / Type=Set up Authenticator App; Result=WRITE; Username=test.user@acme.com; Session ID=67b7bc |
| Authorization | Remove Enrollment | [success](/products/workday/event_examples/authorization_remove_enrollment.json) | Timestamp=2024-03-27T15:22:28.183Z; Event Code / Type=Edit One Time Passcode - Email Setup; Result=WRITE; Username=test.user@acme.com; Session ID=92dc7b |
| System Audit | Create Security Configuration | [success](/products/workday/event_examples/system_audit_create_security_configuration.json) | Timestamp=2024-04-18T17:04:59.204Z; Event Code / Type=Create Security Policy for Domain; Result=WRITE; Username=test.user@acme.com; Session ID=efc2ba |
| System Audit | Read Security Configuration | [success](/products/workday/event_examples/system_audit_read_security_configuration.json) | Timestamp=2024-04-18T17:01:25.414Z; Event Code / Type=Tenant Setup - Security; Result=READ; Username=test.user@acme.com; Session ID=5ced74 |
| System Audit | Update Security Configuration | [success](/products/workday/event_examples/system_audit_update_security_configuration.json) | Timestamp=2024-04-18T17:04:18.829Z; Event Code / Type=Edit One Time Passcode - SMS Setup; Result=WRITE; Username=test.user@acme.com; Session ID=5ced74 |
| System Audit | Delete Security Configuration | [success](/products/workday/event_examples/system_audit_delete_security_configuration.json) | Timestamp=2024-04-18T17:46:17.353Z; Event Code / Type=Edit Tenant Setup - Security; Result=WRITE; Username=test.user@acme.com; Session ID=5ced74 |
| System Audit | Create Integration | [success](/products/workday/event_examples/system_audit_create_integration.json) | Timestamp=2024-04-12T17:48:40.298Z; Event Code / Type=Register API Client for Integrations; Result=WRITE; Username=test.user@acme.com; Session ID=a6894b |
| System Audit | Read Integration | [success](/products/workday/event_examples/system_audit_read_integration.json) | Timestamp=2024-04-24T16:45:01.996Z; Event Code / Type=Register API Client for Integrations; Result=READ; Username=test.user@acme.com; Session ID=23f3c4 |
| System Audit | Update Integration | [success](/products/workday/event_examples/system_audit_update_integration.json) | Timestamp=2024-04-10T18:36:53.137Z; Event Code / Type=Edit Integration System; Result=WRITE; Username=test.user@acme.com; Session ID=9b4f58 |
| Activity Audit | Create Resource | [success](/products/workday/event_examples/activity_audit_create_resource.json) | Timestamp=2024-04-15T18:58:53.582Z; Event Code / Type=Create Expense Report; Result=WRITE; Username=test.user@acme.com; Session ID=a0ce77 |
| Activity Audit | Read Resource | [success](/products/workday/event_examples/activity_audit_read_resource.json) | Timestamp=2024-04-16T15:20:25.595Z; Event Code / Type=Change Election; Result=READ; Username=test.user@acme.com; Session ID=7bfc6f |
| Activity Audit | Update Resource | [success](/products/workday/event_examples/activity_audit_update_resource.json) | Timestamp=2024-04-16T15:00:22.436Z; Event Code / Type=Edit Custom Report; Result=WRITE; Username=test.user@acme.com; Session ID=7bfc6f |
| Activity Audit | Delete Resource | [success](/products/workday/event_examples/activity_audit_delete_resource.json) | Timestamp=2024-04-16T14:58:10.665Z; Event Code / Type=Delete Custom Report; Result=WRITE; Username=test.user@acme.com; Session ID=7bfc6f |
| Activity Audit | Download Resource | [success](/products/workday/event_examples/activity_audit_delete_resource.json) | Timestamp=2024-04-16T14:58:10.665Z; Result=Delete Custom Report; Username=test.user@acme.com; Session ID=7bfc6f; IP Address=192.168.0.1 |


