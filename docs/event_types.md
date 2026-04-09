# event_types (1.0.0)

Event types represent logical buckets of different types of events.

These event types are associated with a defined category and will typically have attributes associated with them.

## Items

| Name | Key | Legacy ID | Description | Categories |
| ---- | --- | --------- | ----------- | ---------- |
| Account Login | account_login | ET0001 | An account attempted to login to a system. | authentication |
| Account Logout | account_logout | ET0002 | An account attempted to logout of a system. | authentication |
| MFA Verification | mfa_verification | ET0003 | Enter or acknowledge an MFA factor which indicates success or failure. | authentication |
| Create User | create_user | ET0004 | Creates a user. | authorization |
| Read User | read_user | ET0005 | Reads information about a user. | authorization |
| Update User | update_user | ET0006 | Updates information about a user. | authorization |
| Delete User | delete_user | ET0007 | Removes or deletes a user. | authorization |
| Create Group | create_group | ET0008 | Creates a logical group. | authorization |
| Read Group | read_group | ET0009 | Reads a group. | authorization |
| Update Group | update_group | ET0010 | Updates a group. | authorization |
| Delete Group | delete_group | ET0011 | Removes or deletes a group. | authorization |
| Add To Group | add_to_group | ET0012 | Adds a service, user or account to a group. | authorization |
| Remove From Group | remove_from_group | ET0013 | Removes a service, user or account from a group. | authorization |
| Create Role | create_role | ET0014 | Creates a new role. | authorization |
| Read Role | read_role | ET0015 | Reads a role. | authorization |
| Update Role | update_role | ET0016 | Updates a role. | authorization |
| Delete Role | delete_role | ET0017 | Removes or deletes a role. | authorization |
| Add Permission | add_permission | ET0018 | Adds a permission to a resource. | authorization |
| Remove Permission | remove_permission | ET0019 | Removes a permission from a resource. | authorization |
| Add Enrollment | add_enrollment | ET0020 | A MFA enrollment was added to an account. | authorization |
| Remove Enrollment | remove_enrollment | ET0021 | A MFA enrollment was removed from an account. | authorization |
| Create Security Configuration | create_security_configuration | ET0022 | Creates a security configuration policy or enables settings. | system_audit |
| Read Security Configuration | read_security_configuration | ET0023 | Reads a security configuration policy or settings. | system_audit |
| Update Security Configuration | update_security_configuration | ET0024 | Updates a security configuration policy or settings. | system_audit |
| Delete Security Configuration | delete_security_configuration | ET0025 | Removes or deletes a security configuration policy or setting. | system_audit |
| Create Integration | create_integration | ET0026 | Creates a new integration. | system_audit |
| Read Integration | read_integration | ET0027 | Reads an existing integration. | system_audit |
| Update Integration | update_integration | ET0028 | Updates an existing integration. | system_audit |
| Delete Integration | delete_integration | ET0029 | Removes or deletes an existing integration. | system_audit |
| Create Resource | create_resource | ET0030 | A resource was created. | activity_audit |
| Read Resource | read_resource | ET0031 | A resource was read. | activity_audit |
| Update Resource | update_resource | ET0032 | A resource was updated. | activity_audit |
| Delete Resource | delete_resource | ET0033 | A resource was removed or deleted. | activity_audit |
| Download Resource | download_resource | ET0034 | A resource was downloaded. | activity_audit |
| Query Resource | query_resource | ET0035 | A resource was queried or searched. | activity_audit |



