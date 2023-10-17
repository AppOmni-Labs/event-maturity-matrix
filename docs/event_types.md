# event_types (0.0.1)

Event types represent logical buckets of different types of events. These event types
are associated with a defined category and will typically have attributes associated with them.

## Items

| Name | ID | Description                                                            | Categories |
| ---- | -- |------------------------------------------------------------------------| ---------- |
| Account Login | ET0001 | An account attempted to login to a system.                             | C0001 |
| Account Logout | ET0002 | An account attempted to logout of a system.                            | C0001 |
| MFA Verification | ET0003 | Enter or acknowledge an MFA factor which indicates success or failure. | C0001 |
| Create User | ET0004 | Creates a user.                                                        | C0002 |
| Read User | ET0005 | Reads information about a user.                                        | C0002 |
| Update User | ET0006 | Updates information about a user.                                      | C0002 |
| Delete User | ET0007 | Removes or deletes a user.                                             | C0002 |
| Create Group | ET0008 | Creates a logical group.                                               | C0002 |
| Read Group | ET0009 | Reads a group.                                                         | C0002 |
| Update Group | ET0010 | Updates a group.                                                       | C0002 |
| Delete Group | ET0011 | Removes or deletes a group.                                            | C0002 |
| Add To Group | ET0012 | Adds a service, user or account to a group.                            | C0002 |
| Remove From Group | ET0013 | Removes a service, user or account from a group.                       | C0002 |
| Create Role | ET0014 | Creates a new role.                                                    | C0002 |
| Read Role | ET0015 | Reads a role.                                                          | C0002 |
| Update Role | ET0016 | Updates a role.                                                        | C0002 |
| Delete Role | ET0017 | Removes or deletes a role.                                             | C0002 |
| Add Permission | ET0018 | Adds a permission to a resource.                                       | C0002 |
| Remove Permission | ET0019 | Removes a permission from a resource.                                  | C0002 |
| Add Enrollment | ET0020 | A MFA enrollment was added to an account.                              | C0002 |
| Remove Enrollment | ET0021 | A MFA enrollment was removed from an account.                          | C0002 |
| Create Security Configuration | ET0022 | Creates a security configuration policy or enables settings.           | C0003 |
| Read Security Configuration | ET0023 | Reads a security configuration policy or settings.                     | C0003 |
| Update Security Configuration | ET0024 | Updates a security configuration policy or settings.                   | C0003 |
| Delete Security Configuration | ET0025 | Removes or deletes a security configuration policy or setting.         | C0003 |
| Create Integration | ET0026 | Creates a new integration.                                             | C0003 |
| Read Integration | ET0027 | Reads an existing integration.                                         | C0003 |
| Update Integration | ET0028 | Updates an existing integration.                                       | C0003 |
| Delete Integration | ET0029 | Removes or deletes an existing integration.                            | C0003 |
| Create Resource | ET0030 | A resource was created.                                                | C0004 |
| Read Resource | ET0031 | A resource was read.                                                   | C0004 |
| Update Resource | ET0032 | A resource was updated.                                                | C0004 |
| Delete Resource | ET0033 | A resource was removed or deleted.                                     | C0004 |
| Download Resource | ET0034 | A resource was downloaded.                                             | C0004 |



