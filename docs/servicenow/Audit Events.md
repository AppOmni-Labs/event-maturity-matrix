# ServiceNow — Audit Events

📌 **v0.0.1** · 🗄 **Retention:** Infinite · ⚡ **Latency:** Near Real-Time

🗄 Can be changed by an instance admin.


⚡ Can vary based on system conditions and configurations.


📜 **Licensing:** Included with ServiceNow instances.


ServiceNow audit events track changes to records in audited tables.
## References
* [Viewing Sys Audit and Audit Relationship Change tables](https://docs.servicenow.com/bundle/vancouver-platform-security/page/administer/security/concept/c_UnderstandingTheSysAuditTable.html)
## Field mappings

| Category | Event type | Attribute | Source field(s) |
| -------- | ---------- | --------- | ---------------- |
| Activity Audit | Update Resource | Timestamp | sys_created_on |
| Activity Audit | Update Resource | Event Code / Type | fieldname |
| Activity Audit | Update Resource | Username | user |
| Activity Audit | Update Resource | Resource Name | tablename |
| Activity Audit | Delete Resource | Timestamp | sys_created_on |
| Activity Audit | Delete Resource | Event Code / Type | fieldname |
| Activity Audit | Delete Resource | Username | user |
| Activity Audit | Delete Resource | Resource Name | tablename |

## Example logs

| Category | Event type | Log | Sample field values |
| -------- | ---------- | --- | ------------------- |
| Activity Audit | Update Resource | [update](/products/servicenow/event_examples/audit/activity_audit_update_resource.json) | Timestamp=2024-04-22 13:45:41; Event Code / Type=u_date_last_risk_updated; Username=system; Resource Name=demo_table |
| Activity Audit | Delete Resource | [delete](/products/servicenow/event_examples/audit/activity_audit_delete_resource.json) | Timestamp=2024-04-22 14:21:25; Event Code / Type=DELETED; Username=system; Resource Name=demo_table |


