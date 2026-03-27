# Duo - Duo Administrator Logs (1.0.0)

> Entity Name: event_source

Provides an audit trail of administrative actions taken within the Duo Security platform.

## References
* [Duo Administrator Logs](https://duo.com/docs/adminapi#administrator-logs)

## Retention

Based on our research, Duo retains audit logs for Configurable.


### Comments
Administrator logs are stored based on the log retention interval setting. If no custom log retention interval has been specified, Administrator logs can be retrieved from the time the account was initially created, reference https://help.duo.com/s/article/2990?language=en_US


## Latency

Based on our research, Duo has a latency of Near real-time.

### Comments
N/A


## Licensing

The Duo Admin API is available to Duo Premier, Duo Advantage, and Duo Essentials customers, and new customers with an Advantage or Premier trial. For more information, see https://duo.com/docs/adminapi#about-the-admin-api

## Mappings

| Category | Event Type | Attributes | Examples |
| -------- | ---------- | ---------- | -------- |
| C0001 | ET0001 |A0001 -> ['isotimestamp', 'timestamp']<br />A0003 -> action<br />A0004 -> action<br />A0005 -> ['username', 'description.email']<br />A0007 -> description.role<br />A0009 -> description.ip_address<br />A0012 -> description.device<br />A0013 -> description.error<br />A0014 -> ['description.factor', 'description.primary_auth_method', 'EMM_UPDATE']<br />|[success](/products/duo/event_examples/authentication_account_login_success_admin.json)<br />[failure](/products/duo/event_examples/authentication_account_login_failure_admin.json)<br />|
| C0001 | ET0003 |A0001 -> ['isotimestamp', 'timestamp']<br />A0003 -> action<br />A0004 -> ['action', 'error']<br />A0005 -> ['username', 'description.email']<br />A0009 -> description.ip_address<br />A0016 -> description.factor<br />A0017 -> description.error<br />|[failure](/products/duo/event_examples/authentication_mfa_verification_failure_admin.json)<br />[flagged](/products/duo/event_examples/authentication_mfa_verification_failure_flagged_admin.json)<br />|
| C0002 | ET0004 |A0001 -> ['isotimestamp', 'timestamp']<br />A0003 -> action<br />A0005 -> username<br />A0007 -> description.role<br />A0019 -> ['description.uname', 'object']<br />|[user](/products/duo/event_examples/authorization_create_user_admin.json)<br />[admin](/products/duo/event_examples/authorization_create_user_admin_admin.json)<br />|
| C0002 | ET0006 |A0001 -> ['isotimestamp', 'timestamp']<br />A0003 -> action<br />A0005 -> username<br />A0019 -> object<br />A0020 -> description<br />|[user](/products/duo/event_examples/authorization_update_user_admin.json)<br />[admin](/products/duo/event_examples/authorization_update_user_admin_admin.json)<br />|
| C0002 | ET0007 |A0001 -> ['isotimestamp', 'timestamp']<br />A0003 -> action<br />A0005 -> username<br />A0007 -> description.role<br />A0019 -> object<br />|[user](/products/duo/event_examples/authorization_delete_user_admin.json)<br />[admin](/products/duo/event_examples/authorization_delete_user_admin_admin.json)<br />|
| C0002 | ET0008 |A0001 -> ['isotimestamp', 'timestamp']<br />A0003 -> action<br />A0005 -> username<br />A0021 -> ['description.name', 'object']<br />|[success](/products/duo/event_examples/authorization_create_group_admin.json)<br />|
| C0002 | ET0010 |A0001 -> ['isotimestamp', 'timestamp']<br />A0003 -> action<br />A0005 -> username<br />A0021 -> object<br />A0020 -> description<br />|[success](/products/duo/event_examples/authorization_update_group_admin.json)<br />|
| C0002 | ET0011 |A0001 -> ['isotimestamp', 'timestamp']<br />A0003 -> action<br />A0005 -> username<br />A0021 -> ['object', 'description.name']<br />|[success](/products/duo/event_examples/authorization_delete_group_admin.json)<br />|
| C0002 | ET0012 |A0001 -> ['isotimestamp', 'timestamp']<br />A0003 -> action<br />A0005 -> username<br />A0021 -> description.groups.name<br />A0019 -> object<br />|[success](/products/duo/event_examples/authorization_add_to_group_admin.json)<br />|
| C0002 | ET0013 |A0001 -> ['isotimestamp', 'timestamp']<br />A0003 -> action<br />A0005 -> username<br />A0019 -> object<br />|[success](/products/duo/event_examples/authorization_remove_from_group_admin.json)<br />|
| C0002 | ET0020 |A0001 -> ['isotimestamp', 'timestamp']<br />A0003 -> action<br />A0005 -> username<br />A0011 -> description.user_agent<br />A0025 -> description.authenticator_type<br />A0019 -> description.owner_name<br />|[success](/products/duo/event_examples/authorization_add_enrollment_admin.json)<br />|
| C0002 | ET0021 |A0001 -> ['isotimestamp', 'timestamp']<br />A0003 -> action<br />A0005 -> username<br />A0025 -> description<br />A0019 -> object<br />|[user](/products/duo/event_examples/authorization_remove_enrollment_admin.json)<br />[admin](/products/duo/event_examples/authorization_remove_enrollment_admin_admin.json)<br />|
| C0003 | ET0022 |A0001 -> ['isotimestamp', 'timestamp']<br />A0003 -> action<br />A0005 -> username<br />A0026 -> action<br />|[success](/products/duo/event_examples/system_audit_create_security_configuration_admin.json)<br />|
| C0003 | ET0024 |A0001 -> ['isotimestamp', 'timestamp']<br />A0003 -> action<br />A0005 -> username<br />A0026 -> ['action', 'description']<br />A0027 -> description<br />|[success](/products/duo/event_examples/system_audit_update_security_configuration_admin.json)<br />|
| C0003 | ET0025 |A0001 -> ['isotimestamp', 'timestamp']<br />A0003 -> action<br />A0005 -> username<br />A0026 -> ['action', 'description', 'object']<br />A0027 -> description<br />|[success](/products/duo/event_examples/system_audit_delete_security_configuration_admin.json)<br />|
| C0003 | ET0026 |A0001 -> isotimestamp<br />A0003 -> action<br />A0005 -> username<br />A0029 -> ['description.name', 'object']<br />|[success](/products/duo/event_examples/system_audit_create_integration_admin.json)<br />|
| C0003 | ET0028 |A0001 -> isotimestamp<br />A0003 -> action<br />A0005 -> username<br />A0029 -> object<br />A0026 -> description<br />|[success](/products/duo/event_examples/system_audit_update_integration_admin.json)<br />|
| C0003 | ET0029 |A0001 -> isotimestamp<br />A0003 -> action<br />A0005 -> username<br />A0029 -> ['description.name', 'object']<br />|[success](/products/duo/event_examples/system_audit_delete_integration_admin.json)<br />|
| C0004 | ET0030 |A0001 -> ['isotimestamp', 'timestamp']<br />A0003 -> action<br />A0005 -> username<br />A0030 -> object<br />A0031 -> ['action', 'description']<br />|[success](/products/duo/event_examples/activity_audit_create_resource_admin.json)<br />|
| C0004 | ET0032 |A0001 -> ['isotimestamp', 'timestamp']<br />A0003 -> action<br />A0005 -> username<br />A0030 -> ['action', 'description']<br />A0031 -> ['action', 'description']<br />|[success](/products/duo/event_examples/activity_audit_update_resource_admin.json)<br />|
| C0004 | ET0033 |A0001 -> ['isotimestamp', 'timestamp']<br />A0003 -> action<br />A0005 -> username<br />A0030 -> object<br />A0031 -> ['action', 'description']<br />|[success](/products/duo/event_examples/activity_audit_delete_resource_admin.json)<br />|


