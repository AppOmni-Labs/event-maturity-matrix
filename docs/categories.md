# categories (1.0.0)

Categories define the logical buckets of event types.

## Items

| Name | Key | Legacy ID | Description |
| ---- | --- | --------- | ----------- |
| Authentication | authentication | C0001 | This category contains events related to authentication. |
| Authorization | authorization | C0002 | This category contains events related to the management of or access of a specific service provider.<br><br>You will often find User, Group and/or Role CRUD (create, read, update, delete, download, etc.) operations under the Authorization category. |
| System Audit | system_audit | C0003 | Tenant level setting / configuration operations that impact an entire product.<br><br>For example, updating of security configurations at a global level are typically within the System Audit category. |
| Activity Audit | activity_audit | C0004 | This category contains events related to general activity within an environment.<br><br>Event types within this category are focused on behavior within a service. |



