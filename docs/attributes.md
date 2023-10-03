# attributes (0.0.1)

Attributes are associated with many event types. These attributes describe logging fields in a source platform.

## Items

| Name | ID | Type | Description | Categories | Include | Exclude | Examples |
| ---- | -- | ---- | ----------- | ---------- | -------- | -------- | -------- |
| Timestamp | A0001 | string | The timestamp of when the event first occurred. |  |  |  | 2022-11-17T06:34:18.429Z |
| Event ID | A0002 | string | A unique event ID to describe the event. |  |  |  | 312b0a2d-a7a3-4529-bd61-bf3c2e2ba11d |
| Event Code / Type | A0003 | string | Identification code for this event, if one exists. Some event sources use event codes to identify messages unambiguously, regardless of message language or wording adjustments over time. |  |  |  | 8080 |
| Result | A0004 | string | Describes whether an event action succeeded or failed. |  |  |  | Success, Failure |
| Username | A0005 | string | The username used when this event occurred. |  |  |  | first.lastname, first.lastname@company.com |
| User ID | A0006 | string | Unique ID of the user associated with this event. |  |  |  | ABCDEFG123456 |
| User Type / Role | A0007 | string | The role of the user at the time of the event. |  |  |  | administrator, guest |
| Session ID | A0008 | string | Unique ID of the session. |  |  |  | abc123def456 |
| IP Address | A0009 | string | The IP address of the source or destination. This is dependent on each service provider. |  |  |  | 192.0.0.1 |
| IP Geolocation / ASN | A0010 | string | General IP geolocation information and unique number assigned to the autonomous system. |  |  |  | {'lon': -73.614830, 'lat': 45.505918}, 15169 |
| User Agent Name | A0011 | string | Name of the user agent. |  |  |  | Mozilla/5.0 (Macintosh; Intel Mac OS X) |
| Device/Client Type | A0012 | string | The type of device or client used during the event. |  |  |  | Mobile |
| Failure Context | A0013 | string | Additional failure context may be provided by the service. |  | ET0001 |  | Invalid username or password |
| Credential Context | A0014 | string | Credential context may provide more details about the credentials used during the event. |  | ET0001 |  | Password |
| Identity Service Provider Context | A0015 | string | Identity service provider (ISP) context related to the request. |  | ET0001 |  | Okta Single Sign-On |
| Verification Method | A0016 | string | The method used for verification. |  | ET0003 |  | MFA Push |
| Verification Flagged | A0017 | string | Whether or not MFA verification was flagged |  | ET0003 |  | The user denied the verification request and flagged the notification as fraudulent. |
| Activity Performed | A0018 | string | The activity or operation that required MFA verification. |  | ET0003 |  | Authentication, Resource Access, Configuration Change |
| Target Username | A0019 | string | The target username of activity within a service provider. |  | C0002 | ET0008, ET0009, ET0010, ET0011, ET0014, ET0015, ET0016, ET0017, ET0018, ET0019, ET0020 | first.lastname, first.lastname@company.com |
| Target Attribute Context | A0020 | string | Context regarding the target attribute that was changed during a user, group, or role modification. |  | ET0006, ET0010 |  | The user's email address was changed |
| Target Group Name | A0021 | string | The target group name of activity within a service provider. A group signifies a collection of users. |  | ET0008, ET0009, ET0010, ET0011, ET0012, ET0013 |  | Administrators |
| Target Role Name | A0022 | string | The target role name of activity within a service provider. A role signifies a collection of permissions. |  | ET0014, ET0015, ET0016, ET0017 |  | Administrators |
| Permission Name | A0023 | string | The name of a permission specified within an event. |  | ET0018, ET0019, ET0020 |  | Read, Write |
| Target Resource Name | A0024 | string | The target resource of an action or operation within a service provider. |  | ET0018, ET0019, ET0020 |  | Report Name, API Name |
| Enrollment Type | A0025 | string | The enrollment type of MFA authentication within a service provider. |  | ET0021, ET0023 |  | Authenticator App, Time-based One-time Password (TOTP) |
| Configuration / Setting Name | A0026 | string | The name of a service setting or configuration option. |  | ET0022, ET0023, ET0024, ET0025 |  | Password Policy, MFA Policy |
| Configuration / Setting Value | A0027 | string | The value of the setting or configuration that was changed. |  | ET0022, ET0024, ET0025, ET0028 |  | Password expiration policy was changed to 90 days |
| Previous Configuration / Setting Value | A0028 | string | The previous value of the setting or configuration that was changed. |  | ET0024, ET0028 |  | Password expiration policy was changed from 90 days to 60 days |
| Integration / App Name | A0029 | string | The name of an integration or OAuth application. |  | ET0026, ET0027, ET0028, ET0029 |  | Slack |
| Resource Name | A0030 | string | The name of a resource within a service provider. |  | C0004 |  | Report Name, API Name |
| Resource Type | A0031 | string | The type of resource within a service provider. |  | C0004 |  | Report, API |
| Resource Metadata | A0032 | string | Metadata about the resource that was created, modified, or deleted. |  | ET0034 |  | The report was 1,000 rows and 25Mb in size |



