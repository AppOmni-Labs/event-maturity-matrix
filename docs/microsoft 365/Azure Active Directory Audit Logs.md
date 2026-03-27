# Microsoft 365 - Azure Active Directory Audit Logs (1.0.0)

> Entity Name: event_source

Includes logs from Azure Active Directory including authentication and user management.

## References
* [Azure Active Directory Base Schema](https://learn.microsoft.com/en-us/office/office-365-management-api/office-365-management-activity-api-schema#azure-active-directory-base-schema)

## Retention

Based on our research, Microsoft 365 retains audit logs for 180 days.


### Comments
Minimum retention is 180 days, but organizations can set a retention policy up to 10 years dependent on licensing, reference https://learn.microsoft.com/en-us/purview/audit-log-retention-policies


## Latency

Based on our research, Microsoft 365 has a latency of Typically 60 to 90 minutes after an event occurs..

### Comments
Microsoft does not provide a specific audit logging latency SLA, reference https://learn.microsoft.com/en-us/purview/audit-search?view=o365-worldwide&tabs=microsoft-purview-portal


## Licensing

Standard and Premium audit licenses are available, with log availability and retention dependent on the license level. For more information, see https://learn.microsoft.com/en-us/purview/audit-search?view=o365-worldwide&tabs=microsoft-purview-portal

## Mappings

| Category | Event Type | Attributes | Examples |
| -------- | ---------- | ---------- | -------- |
| C0001 | ET0001 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> Actor[].Type<br />A0008 -> DeviceProperties[Name=SessionId].Value<br />A0009 -> ClientIP<br />A0011 -> ExtendedProperties[Name=UserAgent].Value<br />A0012 -> DeviceProperties<br />A0015 -> ExtendedProperties[Name=RequestType].Value<br />|[success](/products/microsoft 365/event_examples/azure_ad/authentication_account_login_success.json)<br />[failure](/products/microsoft 365/event_examples/azure_ad/authentication_account_login_failure.json)<br />|
| C0001 | ET0003 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0004 -> ResultStatus<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> Actor[].Type<br />A0009 -> ClientIP<br />A0011 -> ExtendedProperties[Name=UserAgent].Value<br />A0012 -> DeviceProperties<br />|[success](/products/microsoft 365/event_examples/azure_ad/authentication_mfa_verification.json)<br />|
| C0002 | ET0004 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0004 -> ResultStatus<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> ['Actor[ID=User].Type', 'Actor[ID=ServicePrincipal].Type']<br />A0019 -> Target.ID<br />|[success](/products/microsoft 365/event_examples/azure_ad/authorization_create_user.json)<br />|
| C0002 | ET0006 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0004 -> ResultStatus<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> ['Actor[ID=User].Type', 'Actor[ID=ServicePrincipal].Type']<br />A0019 -> Target.ID<br />A0020 -> ModifiedProperties<br />|[success](/products/microsoft 365/event_examples/azure_ad/authorization_update_user.json)<br />|
| C0002 | ET0007 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0004 -> ResultStatus<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> ['Actor[ID=User].Type', 'Actor[ID=ServicePrincipal].Type']<br />A0019 -> Target.ID<br />|[success](/products/microsoft 365/event_examples/azure_ad/authorization_delete_user.json)<br />|
| C0002 | ET0008 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0004 -> ResultStatus<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> ['Actor[ID=User].Type', 'Actor[ID=ServicePrincipal].Type']<br />A0021 -> Target.ID<br />|[success](/products/microsoft 365/event_examples/azure_ad/authorization_create_group.json)<br />|
| C0002 | ET0010 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0004 -> ResultStatus<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> ['Actor[ID=User].Type', 'Actor[ID=ServicePrincipal].Type']<br />A0021 -> Target.ID<br />|[success](/products/microsoft 365/event_examples/azure_ad/authorization_update_group.json)<br />|
| C0002 | ET0011 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0004 -> ResultStatus<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> ['Actor[ID=User].Type', 'Actor[ID=ServicePrincipal].Type']<br />A0021 -> Target.ID<br />|[success](/products/microsoft 365/event_examples/azure_ad/authorization_delete_group.json)<br />|
| C0002 | ET0012 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0004 -> ResultStatus<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> ['Actor[ID=User].Type', 'Actor[ID=ServicePrincipal].Type']<br />A0012 -> ExtendedProperties[Name=additionalDetails].Value<br />A0021 -> ModifiedProperties[Name=Group.DisplayName].NewValue<br />A0019 -> Target.ID<br />|[success](/products/microsoft 365/event_examples/azure_ad/authorization_add_member_to_group.json)<br />|
| C0002 | ET0013 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0004 -> ResultStatus<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> ['Actor[ID=User].Type', 'Actor[ID=ServicePrincipal].Type']<br />A0011 -> ExtendedProperties[Name=additionalDetails].Value<br />A0021 -> ModifiedProperties[Name=Group.DisplayName].NewValue<br />A0019 -> Target.ID<br />|[success](/products/microsoft 365/event_examples/azure_ad/authorization_remove_member_from_group.json)<br />|
| C0002 | ET0014 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0004 -> ResultStatus<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> ['Actor[ID=User].Type', 'Actor[ID=ServicePrincipal].Type']<br />A0011 -> ExtendedProperties[Name=additionalDetails].Value<br />A0022 -> Target.ID<br />|[success](/products/microsoft 365/event_examples/azure_ad/authorization_create_role.json)<br />|
| C0002 | ET0016 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0004 -> ResultStatus<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> ['Actor[ID=User].Type', 'Actor[ID=ServicePrincipal].Type']<br />A0011 -> ExtendedProperties[Name=additionalDetails].Value<br />A0022 -> Target.ID<br />A0020 -> ModifiedProperties[Name=GrantedPermissions].NewValue<br />|[success](/products/microsoft 365/event_examples/azure_ad/authorization_update_role.json)<br />|
| C0002 | ET0017 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0004 -> ResultStatus<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> ['Actor[ID=User].Type', 'Actor[ID=ServicePrincipal].Type']<br />A0011 -> ExtendedProperties[Name=additionalDetails].Value<br />A0022 -> Target.ID<br />|[success](/products/microsoft 365/event_examples/azure_ad/authorization_delete_role.json)<br />|
| C0002 | ET0018 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0004 -> ResultStatus<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> ['Actor[ID=User].Type', 'Actor[ID=ServicePrincipal].Type']<br />A0023 -> ModifiedProperties[Name=Role.DisplayName].NewValue<br />A0024 -> Target.ID<br />|[success](/products/microsoft 365/event_examples/azure_ad/authorization_add_permission.json)<br />|
| C0002 | ET0019 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0004 -> ResultStatus<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> ['Actor[ID=User].Type', 'Actor[ID=ServicePrincipal].Type']<br />A0023 -> ModifiedProperties[Name=Role.DisplayName].OldValue<br />A0024 -> Target.ID<br />|[success](/products/microsoft 365/event_examples/azure_ad/authorization_remove_permission.json)<br />|
| C0002 | ET0020 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0004 -> ResultStatus<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> ['Actor[ID=User].Type', 'Actor[ID=ServicePrincipal].Type']<br />A0025 -> ModifiedProperties[Name=StrongAuthenticationUserDetails].NewValue<br />A0019 -> Target.ID<br />|[success](/products/microsoft 365/event_examples/azure_ad/authorization_add_enrollment.json)<br />|
| C0002 | ET0021 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0004 -> ResultStatus<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> ['Actor[ID=User].Type', 'Actor[ID=ServicePrincipal].Type']<br />A0025 -> ModifiedProperties[Name=StrongAuthenticationPhoneAppDetail].OldValue<br />A0019 -> Target.ID<br />|[success](/products/microsoft 365/event_examples/azure_ad/authorization_remove_enrollment.json)<br />|
| C0003 | ET0022 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0004 -> ResultStatus<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> ['Actor[ID=User].Type', 'Actor[ID=ServicePrincipal].Type']<br />A0011 -> ExtendedProperties[Name=additionalDetails].Value<br />A0026 -> ModifiedProperties[Name=PolicyType].NewValue<br />A0027 -> ModifiedProperties<br />|[success](/products/microsoft 365/event_examples/azure_ad/system_audit_create_security_configuration_cap.json)<br />|
| C0003 | ET0024 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0004 -> ResultStatus<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> ['Actor[ID=User].Type', 'Actor[ID=ServicePrincipal].Type']<br />A0011 -> ExtendedProperties[Name=additionalDetails].Value<br />A0026 -> ExtendedProperties[Name=extendedAuditEventCategory].Value<br />A0027 -> ModifiedProperties[Name=Included Updated Properties].NewValue<br />A0028 -> ModifiedProperties<br />|[success](/products/microsoft 365/event_examples/azure_ad/system_audit_update_security_configuration_cap.json)<br />|
| C0003 | ET0025 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0004 -> ResultStatus<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> ['Actor[ID=User].Type', 'Actor[ID=ServicePrincipal].Type']<br />A0011 -> ExtendedProperties[Name=additionalDetails].Value<br />A0026 -> ExtendedProperties[Name=extendedAuditEventCategory].Value<br />|[success](/products/microsoft 365/event_examples/azure_ad/system_audit_delete_security_configuration_cap.json)<br />|
| C0003 | ET0026 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0004 -> ResultStatus<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> ['Actor[ID=User].Type', 'Actor[ID=ServicePrincipal].Type']<br />A0029 -> ModifiedProperties[Name=DisplayName].NewValue<br />|[success](/products/microsoft 365/event_examples/azure_ad/system_audit_create_integration.json)<br />|
| C0003 | ET0028 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0004 -> ResultStatus<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> ['Actor[ID=User].Type', 'Actor[ID=ServicePrincipal].Type']<br />A0029 -> Target.ID<br />A0026 -> ModifiedProperties<br />A0028 -> ModifiedProperties[Name=Entitlement].OldValue<br />|[success](/products/microsoft 365/event_examples/azure_ad/system_audit_update_integration.json)<br />|
| C0003 | ET0029 |A0001 -> CreationTime<br />A0002 -> Id<br />A0003 -> Operation<br />A0004 -> ResultStatus<br />A0005 -> UserId<br />A0006 -> UserKey<br />A0007 -> ['Actor[ID=User].Type', 'Actor[ID=ServicePrincipal].Type']<br />A0029 -> Target.ID<br />|[success](/products/microsoft 365/event_examples/azure_ad/system_audit_delete_integration.json)<br />|


