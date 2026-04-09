





# ServiceNow — Export Events

📌 **v0.0.1** · 🗄 **Retention:** Infinite · ⚡ **Latency:** Near Real-Time

🗄 Can be changed by an instance admin.


⚡ Can vary based on system conditions and configurations.


📜 **Licensing:** Included with ServiceNow instances.


ServiceNow Instance Security Center export events track UI exports of record data.
## References
* [Monitor security events](https://docs.servicenow.com/bundle/washingtondc-platform-security/page/administer/security/concept/instance-sec-center-event-ribbon.html)
## Field mappings

| Category | Event type | Attribute | Source field(s) |
| -------- | ---------- | --------- | ---------------- |
| Activity Audit | Download Resource | Timestamp | sys_created_on |
| Activity Audit | Download Resource | Event ID | event |
| Activity Audit | Download Resource | Event Code / Type | sys_class_name |
| Activity Audit | Download Resource | Username | user_name |
| Activity Audit | Download Resource | User ID | user |
| Activity Audit | Download Resource | Resource Name | table |

## Example logs

| Category | Event type | Log | Sample field values |
| -------- | ---------- | --- | ------------------- |
| Activity Audit | Download Resource | [download](/products/servicenow/event_examples/export/activity_audit_download_resource.json) | Timestamp=2024-04-16 17:06:11; Event ID=34abc1234abc1234abc1234abc1234ab; Event Code / Type=isc_export_event; Username=admin; User ID=234abc1234abc1234abc1234abc1234a |


