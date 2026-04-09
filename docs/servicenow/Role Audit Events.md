# ServiceNow — Role Audit Events

📌 **v0.0.1** · 🗄 **Retention:** Infinite · ⚡ **Latency:** Near Real-Time

🗄 Can be changed by an instance admin.⚡ Can vary based on system conditions and configurations.📜 **Licensing:** Must be enabled and configured by an instance admin.

The ServiceNow role audit table contains user role assignments.
## References
* [Enable role auditing](https://docs.servicenow.com/bundle/utah-platform-security/page/administer/roles/task/enable-audit-roles.html)
## Field mappings

| Category | Event type | Attribute | Source field(s) |
| -------- | ---------- | --------- | ---------------- |
| Authorization | Add Permission | Timestamp | sys_created_on |
| Authorization | Add Permission | Event Code / Type | operation |
| Authorization | Add Permission | Username | user\.name |
| Authorization | Add Permission | User ID | user\.name |
| Authorization | Remove Permission | Timestamp | sys_created_on |
| Authorization | Remove Permission | Event Code / Type | operation |
| Authorization | Remove Permission | Username | user\.name |
| Authorization | Remove Permission | User ID | user\.name |

## Example logs

| Category | Event type | Log | Sample field values |
| -------- | ---------- | --- | ------------------- |
| Authorization | Add Permission | [add](/products/servicenow/event_examples/audit_role/authorization_add_permission.json) | Timestamp=2024-04-19 18:30:54; Event Code / Type=Added; Username=user.name; User ID=user.name |
| Authorization | Remove Permission | [add](/products/servicenow/event_examples/audit_role/authorization_remove_permission.json) | Timestamp=2024-04-17 17:54:47; Event Code / Type=Removed; Username=user.name; User ID=user.name |


