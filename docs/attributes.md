# attributes (1.0.0)

Attributes are associated with many event types.

These attributes describe logging fields in a source platform.

## Items

| Name | Key | Legacy ID | Type | Description | Include | Exclude | Examples |
| ---- | --- | --------- | ---- | ----------- | ------- | ------- | -------- |
| Timestamp | timestamp | A0001 | string | The timestamp of when the event first occurred. |  |  | 2022-11-17T06:34:18.429Z |
| Event ID | event_id | A0002 | string | A unique event ID to describe the event. |  |  | 312b0a2d-a7a3-4529-bd61-bf3c2e2ba11d |
| Event Code / Type | event_code_or_type | A0003 | string | Identification code for this event, if one exists. Some event sources use event codes to identify messages unambiguously, regardless of message language or wording adjustments over time. |  |  | 8080 |
| Result | result | A0004 | string | Describes whether an event action succeeded or failed. |  |  | Success, Failure |
| Username | username | A0005 | string | The username used when this event occurred. |  |  | first.lastname, first.lastname@company.com |
| User ID | user_id | A0006 | string | Unique ID of the user associated with this event. |  |  | ABCDEFG123456 |
| User Type / Role | user_type_or_role | A0007 | string | The role of the user at the time of the event. |  |  | administrator, guest |
| Session ID | session_id | A0008 | string | Unique ID of the session. |  |  | abc123def456 |
| IP Address | ip_address | A0009 | string | The IP address of the source or destination. This is dependent on each service provider. |  |  | 192.0.0.1 |
| IP Geolocation / ASN | ip_geolocation_or_asn | A0010 | string | General IP geolocation information and unique number assigned to the autonomous system. |  |  | {'lon': -73.614830, 'lat': 45.505918}, 15169 |
| User Agent Name | user_agent_name | A0011 | string | Name of the user agent. |  |  | Mozilla/5.0 (Macintosh; Intel Mac OS X) |
| Device/Client Type | device_client_type | A0012 | string | The type of device or client used during the event. |  |  | Mobile |
| Failure Context | failure_context | A0013 | string | Additional failure context may be provided by the service. | account_login |  | Invalid username or password |
| Credential Context | credential_context | A0014 | string | Credential context may provide more details about the credentials used during the event. | account_login |  | Password |
| Identity Service Provider Context | identity_service_provider_context | A0015 | string | Identity service provider (ISP) context related to the request. | account_login |  | Okta Single Sign-On |
| Verification Method | verification_method | A0016 | string | The method used for verification. | mfa_verification |  | MFA Push |
| Verification Flagged | verification_flagged | A0017 | string | Whether or not MFA verification was flagged | mfa_verification |  | The user denied the verification request and flagged the notification as fraudulent. |
| Activity Performed | activity_performed | A0018 | string | The activity or operation that required MFA verification. | mfa_verification |  | Authentication, Resource Access, Configuration Change |
| Target Username | target_username | A0019 | string | The target username of activity within a service provider. | create_user, read_user, update_user, delete_user, add_to_group, remove_from_group, add_enrollment, remove_enrollment |  | first.lastname, first.lastname@company.com |
| Target Attribute Context | target_attribute_context | A0020 | string | Context regarding the target attribute that was changed during a user, group, or role modification. | update_user, update_group, update_role |  | The user's email address was changed |
| Target Group Name | target_group_name | A0021 | string | The target group name of activity within a service provider. A group signifies a collection of users. | create_group, read_group, update_group, delete_group, add_to_group, remove_from_group |  | Administrators |
| Target Role Name | target_role_name | A0022 | string | The target role name of activity within a service provider. A role signifies a collection of permissions. | create_role, read_role, update_role, delete_role |  | Administrators |
| Permission Name | permission_name | A0023 | string | The name of a permission specified within an event. | add_permission, remove_permission |  | Read, Write |
| Target Resource Name | target_resource_name | A0024 | string | The target resource of an action or operation within a service provider. | add_permission, remove_permission |  | Report Name, API Name |
| Enrollment Type | enrollment_type | A0025 | string | The enrollment type of MFA authentication within a service provider. | add_enrollment, remove_enrollment |  | Authenticator App, Time-based One-time Password (TOTP) |
| Configuration / Setting Name | configuration_setting_name | A0026 | string | The name of a service setting or configuration option. | create_security_configuration, update_security_configuration, delete_security_configuration, update_integration |  | Password Policy, MFA Policy |
| Configuration / Setting Value | configuration_setting_value | A0027 | string | The value of the setting or configuration that was changed. | create_security_configuration, read_security_configuration, update_security_configuration, delete_security_configuration |  | Password expiration policy was changed to 90 days |
| Previous Configuration / Setting Value | previous_configuration_setting_value | A0028 | string | The previous value of the setting or configuration that was changed. | update_security_configuration, update_integration |  | Password expiration policy was changed from 90 days to 60 days |
| Integration / App Name | integration_app_name | A0029 | string | The name of an integration or OAuth application. | create_integration, read_integration, update_integration, delete_integration |  | Slack |
| Resource Name | resource_name | A0030 | string | The name of a resource within a service provider. | create_resource, read_resource, update_resource, delete_resource, download_resource |  | Report Name, API Name |
| Resource Type | resource_type | A0031 | string | The type of resource within a service provider. | create_resource, read_resource, update_resource, delete_resource, download_resource |  | Report, API |
| Resource Metadata | resource_metadata | A0032 | string | Metadata about the resource that was created, modified, or deleted. | download_resource |  | The report was 1,000 rows and 25Mb in size |
| Query String | query_string | A0033 | string | The query or search string used when querying a resource. | query_resource |  | from:user@example.com, subject:quarterly report |



