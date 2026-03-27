# PingOne - Read User Activities API (0.0.1)

> Entity Name: event_source

The PingOne Read User Activities API provides near real-time, read-only access to an organization's audit activity events.

## References
* [Read User Activities API Documentation](https://apidocs.pingidentity.com/pingone/platform/v1/api/#get-read-user-activities)

## Retention

Based on our research, PingOne retains audit logs for Unknown.


### Comments
N/A


## Latency

Based on our research, PingOne has a latency of Near real-time.

### Comments
N/A


## Licensing

A PingOne license is required to access the Read User Activities API.

## Mappings

| Category | Event Type | Attributes | Examples |
| -------- | ---------- | ---------- | -------- |
| C0001 | ET0001 |A0001 -> recordedAt<br />A0002 -> id<br />A0003 -> action.type<br />A0004 -> result.status<br />A0005 -> actors.user.name<br />A0006 -> actors.user.id<br />A0008 -> correlationId<br />A0009 -> source.ipAddress<br />A0011 -> source.userAgent<br />|[success](/products/pingone/event_examples/authentication_account_login_session_success.json)<br />[failure](/products/pingone/event_examples/authentication_account_login_session_failure.json)<br />|
| C0001 | ET0002 |A0001 -> recordedAt<br />A0002 -> id<br />A0003 -> action.type<br />A0004 -> result.status<br />A0005 -> resources.name<br />A0006 -> resources.id<br />A0008 -> correlationId<br />A0009 -> source.ipAddress<br />A0011 -> source.userAgent<br />|[success](/products/pingone/event_examples/authentication_account_logout.json)<br />|
| C0001 | ET0003 |A0001 -> recordedAt<br />A0002 -> id<br />A0003 -> action.type<br />A0004 -> result.status<br />A0005 -> actors.user.name<br />A0006 -> actors.user.id<br />A0008 -> correlationId<br />A0009 -> source.ipAddress<br />A0011 -> source.userAgent<br />A0016 -> resources.name<br />|[success](/products/pingone/event_examples/authentication_mfa_verification.json)<br />|
| C0002 | ET0004 |A0001 -> recordedAt<br />A0002 -> id<br />A0003 -> action.type<br />A0004 -> result.status<br />A0005 -> actors.user.name<br />A0006 -> actors.user.id<br />A0008 -> correlationId<br />A0009 -> source.ipAddress<br />A0011 -> source.userAgent<br />A0019 -> resources[type=USER].name<br />|[success](/products/pingone/event_examples/authorization_create_user.json)<br />|
| C0002 | ET0006 |A0001 -> recordedAt<br />A0002 -> id<br />A0003 -> action.type<br />A0004 -> result.status<br />A0005 -> actors.user.name<br />A0006 -> actors.user.id<br />A0008 -> correlationId<br />A0009 -> source.ipAddress<br />A0011 -> source.userAgent<br />A0019 -> resources[type=USER].name<br />A0020 -> result.description<br />|[success](/products/pingone/event_examples/authorization_update_user.json)<br />|
| C0002 | ET0007 |A0001 -> recordedAt<br />A0002 -> id<br />A0003 -> action.type<br />A0004 -> result.status<br />A0005 -> actors.user.name<br />A0006 -> actors.user.id<br />A0008 -> correlationId<br />A0009 -> source.ipAddress<br />A0011 -> source.userAgent<br />A0019 -> resources[type=USER].name<br />|[success](/products/pingone/event_examples/authorization_delete_user.json)<br />|
| C0002 | ET0008 |A0001 -> recordedAt<br />A0002 -> id<br />A0003 -> action.type<br />A0004 -> result.status<br />A0005 -> actors.user.name<br />A0006 -> actors.user.id<br />A0008 -> correlationId<br />A0009 -> source.ipAddress<br />A0011 -> source.userAgent<br />A0021 -> ['resources[type=GROUP].name', 'resources[type=MEMBER_OF_GROUP].name']<br />|[success](/products/pingone/event_examples/authorization_create_group.json)<br />|
| C0002 | ET0011 |A0001 -> recordedAt<br />A0002 -> id<br />A0003 -> action.type<br />A0004 -> result.status<br />A0005 -> actors.user.name<br />A0006 -> actors.user.id<br />A0008 -> correlationId<br />A0009 -> source.ipAddress<br />A0011 -> source.userAgent<br />A0021 -> ['resources[type=GROUP].name', 'resources[type=MEMBER_OF_GROUP].name']<br />|[success](/products/pingone/event_examples/authorization_delete_group.json)<br />|
| C0002 | ET0012 |A0001 -> recordedAt<br />A0002 -> id<br />A0003 -> action.type<br />A0004 -> result.status<br />A0005 -> actors.user.name<br />A0006 -> actors.user.id<br />A0008 -> correlationId<br />A0009 -> source.ipAddress<br />A0011 -> source.userAgent<br />A0021 -> ['resources[type=GROUP].name', 'resources[type=MEMBER_OF_GROUP].name']<br />|[success](/products/pingone/event_examples/authorization_add_to_group.json)<br />|
| C0002 | ET0013 |A0001 -> recordedAt<br />A0002 -> id<br />A0003 -> action.type<br />A0004 -> result.status<br />A0005 -> actors.user.name<br />A0006 -> actors.user.id<br />A0008 -> correlationId<br />A0009 -> source.ipAddress<br />A0011 -> source.userAgent<br />A0021 -> ['resources[type=GROUP].name', 'resources[type=MEMBER_OF_GROUP].name']<br />|[success](/products/pingone/event_examples/authorization_remove_from_group.json)<br />|
| C0002 | ET0018 |A0001 -> recordedAt<br />A0002 -> id<br />A0003 -> action.type<br />A0004 -> result.status<br />A0005 -> actors.user.name<br />A0006 -> actors.user.id<br />A0008 -> correlationId<br />A0009 -> source.ipAddress<br />A0011 -> source.userAgent<br />A0023 -> result.description<br />A0024 -> resources[type=USER].name<br />|[success](/products/pingone/event_examples/authorization_add_permission.json)<br />|
| C0002 | ET0019 |A0001 -> recordedAt<br />A0002 -> id<br />A0003 -> action.type<br />A0004 -> result.status<br />A0005 -> actors.user.name<br />A0006 -> actors.user.id<br />A0008 -> correlationId<br />A0009 -> source.ipAddress<br />A0011 -> source.userAgent<br />A0023 -> result.description<br />A0024 -> resources[type=USER].name<br />|[success](/products/pingone/event_examples/authorization_remove_permission.json)<br />|
| C0002 | ET0020 |A0001 -> recordedAt<br />A0002 -> id<br />A0003 -> action.type<br />A0004 -> result.status<br />A0005 -> actors.user.name<br />A0006 -> actors.user.id<br />A0008 -> correlationId<br />A0009 -> source.ipAddress<br />A0011 -> source.userAgent<br />A0019 -> resources[type=USER].name<br />|[success](/products/pingone/event_examples/authorization_add_enrollment.json)<br />|
| C0002 | ET0021 |A0001 -> recordedAt<br />A0002 -> id<br />A0003 -> action.type<br />A0004 -> result.status<br />A0005 -> actors.user.name<br />A0006 -> actors.user.id<br />A0008 -> correlationId<br />A0009 -> source.ipAddress<br />A0011 -> source.userAgent<br />|[success](/products/pingone/event_examples/authorization_remove_enrollment.json)<br />|
| C0003 | ET0022 |A0001 -> recordedAt<br />A0002 -> id<br />A0003 -> action.type<br />A0004 -> result.status<br />A0005 -> actors.user.name<br />A0006 -> actors.user.id<br />A0008 -> correlationId<br />A0009 -> source.ipAddress<br />A0011 -> source.userAgent<br />A0026 -> ['action.type', 'resources[0].name']<br />|[success](/products/pingone/event_examples/system_audit_create_security_configuration_idp.json)<br />|
| C0003 | ET0024 |A0001 -> recordedAt<br />A0002 -> id<br />A0003 -> action.type<br />A0004 -> result.status<br />A0005 -> actors.user.name<br />A0006 -> actors.user.id<br />A0008 -> correlationId<br />A0009 -> source.ipAddress<br />A0011 -> source.userAgent<br />A0026 -> ['action.type', 'resources[0].name']<br />|[success](/products/pingone/event_examples/system_audit_update_security_configuration_idp.json)<br />|
| C0003 | ET0025 |A0001 -> recordedAt<br />A0002 -> id<br />A0003 -> action.type<br />A0004 -> result.status<br />A0005 -> actors.user.name<br />A0006 -> actors.user.id<br />A0008 -> correlationId<br />A0009 -> source.ipAddress<br />A0011 -> source.userAgent<br />A0026 -> ['action.type', 'resources[0].name']<br />|[success](/products/pingone/event_examples/system_audit_delete_security_configuration_idp.json)<br />|
| C0003 | ET0026 |A0001 -> recordedAt<br />A0002 -> id<br />A0003 -> action.type<br />A0004 -> result.status<br />A0005 -> actors.user.name<br />A0006 -> actors.user.id<br />A0008 -> correlationId<br />A0009 -> source.ipAddress<br />A0011 -> source.userAgent<br />A0029 -> ['resources[type=IDENTITY_PROVIDER].name', 'resources[type=APPLICATION].name']<br />|[success](/products/pingone/event_examples/system_audit_create_integration.json)<br />|
| C0003 | ET0028 |A0001 -> recordedAt<br />A0002 -> id<br />A0003 -> action.type<br />A0004 -> result.status<br />A0005 -> actors.user.name<br />A0006 -> actors.user.id<br />A0008 -> correlationId<br />A0009 -> source.ipAddress<br />A0011 -> source.userAgent<br />A0029 -> ['resources[type=IDENTITY_PROVIDER].name', 'resources[type=APPLICATION].name']<br />|[success](/products/pingone/event_examples/system_audit_update_integration.json)<br />|
| C0003 | ET0029 |A0001 -> recordedAt<br />A0002 -> id<br />A0003 -> action.type<br />A0004 -> result.status<br />A0005 -> actors.user.name<br />A0006 -> actors.user.id<br />A0008 -> correlationId<br />A0009 -> source.ipAddress<br />A0011 -> source.userAgent<br />A0029 -> ['resources[type=IDENTITY_PROVIDER].name', 'resources[type=APPLICATION].name']<br />|[success](/products/pingone/event_examples/system_audit_delete_integration.json)<br />|


