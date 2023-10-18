# categories (0.0.1)

Categories define the logical buckets of event types.

## Items

| Name | ID | Description |
| ---- | -- | ----------- |
| Authentication | C0001 | This category contains events related to authentication. |
| Authorization | C0002 | This category contains events related to the management of or access of a specific service provider.\n\nYou will often find User, Group and/or Role CRUD (create, read, update, delete, download, etc.) operations\nunder the Authorization category.\n |
| System Audit | C0003 | Tenant level setting / configuration operations that impact an entire product.\n\nFor example, updating of security configurations at a global level are typically within the System Audit category.\n |
| Activity Audit | C0004 | This category contains events related to general activity within an environment.\n\nThis event types within this category are focused on behavior within a service.\n |


