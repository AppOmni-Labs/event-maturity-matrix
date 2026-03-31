# Okta — System Log API

📌 **v1.0.0** · 🗄 **Retention:** System Log events are retained in Okta for a period of 90 days. · ⚡ **Latency:** Near real-time

🗄 https://support.okta.com/help/s/article/Customer-Data-Retention-Policy?language=en_US


⚡ N/A


📜 **Licensing:** A paid Okta license is required to access the System Log API.


The Okta System Log API provides near real-time, read-only access to an organization's system log.
## References
* [System Log API Event Schema and Documentation](https://developer.okta.com/docs/reference/api/system-log/)
* [System Log API Event Types](https://developer.okta.com/docs/reference/api/event-types/)
## Field mappings

| Category | Event type | Attribute | Source field(s) |
| -------- | ---------- | --------- | ---------------- |
| Authentication | Account Login | Timestamp | published |
| Authentication | Account Login | Event ID | uuid |
| Authentication | Account Login | Event Code / Type | eventType |
| Authentication | Account Login | Username | actor.alternateId |
| Authentication | Account Login | User ID | actor.id |
| Authentication | Account Login | Session ID | authenticationContext.externalSessionId |
| Authentication | Account Login | IP Address | client.ipAddress |
| Authentication | Account Login | IP Geolocation / ASN | client.geographicalContext |
| Authentication | Account Login | User Agent Name | client.userAgent |
| Authentication | Account Login | Device/Client Type | client.device |
| Authentication | Account Login | Failure Context | outcome.reason |
| Authentication | Account Login | Credential Context | authenticationContext.credentialType |
| Authentication | Account Login | Identity Service Provider Context | authenticationContext.authenticationProvider |
| Authentication | Account Logout | Timestamp | published |
| Authentication | Account Logout | Event ID | uuid |
| Authentication | Account Logout | Event Code / Type | eventType |
| Authentication | Account Logout | Result | outcome.result |
| Authentication | Account Logout | Username | actor.alternateId |
| Authentication | Account Logout | User ID | actor.id |
| Authentication | Account Logout | Session ID | authenticationContext.externalSessionId |
| Authentication | Account Logout | IP Address | client.ipAddress |
| Authentication | Account Logout | IP Geolocation / ASN | client.geographicalContext |
| Authentication | Account Logout | User Agent Name | client.userAgent |
| Authentication | Account Logout | Device/Client Type | client.device |
| Authentication | MFA Verification | Timestamp | published |
| Authentication | MFA Verification | Event ID | uuid |
| Authentication | MFA Verification | Event Code / Type | eventType |
| Authentication | MFA Verification | Result | outcome.result |
| Authentication | MFA Verification | Username | actor.alternateId |
| Authentication | MFA Verification | User ID | actor.id |
| Authentication | MFA Verification | Session ID | authenticationContext.externalSessionId |
| Authentication | MFA Verification | IP Address | client.ipAddress |
| Authentication | MFA Verification | IP Geolocation / ASN | client.geographicalContext |
| Authentication | MFA Verification | User Agent Name | client.userAgent |
| Authentication | MFA Verification | Device/Client Type | client.device |
| Authentication | MFA Verification | Verification Method | debugContext.debugData.factor |
| Authentication | MFA Verification | Verification Flagged | debugContext.debugData |
| Authorization | Create User | Timestamp | published |
| Authorization | Create User | Event ID | uuid |
| Authorization | Create User | Event Code / Type | eventType |
| Authorization | Create User | Result | outcome.result |
| Authorization | Create User | Username | actor.alternateId |
| Authorization | Create User | User ID | actor.id |
| Authorization | Create User | Session ID | authenticationContext.externalSessionId |
| Authorization | Create User | IP Address | client.ipAddress |
| Authorization | Create User | IP Geolocation / ASN | client.geographicalContext |
| Authorization | Create User | User Agent Name | client.userAgent |
| Authorization | Create User | Device/Client Type | client.device |
| Authorization | Create User | Target Username | target.alternateId |
| Authorization | Update User | Timestamp | published |
| Authorization | Update User | Event ID | uuid |
| Authorization | Update User | Event Code / Type | eventType |
| Authorization | Update User | Result | outcome.result |
| Authorization | Update User | Username | actor.alternateId |
| Authorization | Update User | User ID | actor.id |
| Authorization | Update User | Session ID | authenticationContext.externalSessionId |
| Authorization | Update User | IP Address | client.ipAddress |
| Authorization | Update User | IP Geolocation / ASN | client.geographicalContext |
| Authorization | Update User | User Agent Name | client.userAgent |
| Authorization | Update User | Device/Client Type | client.device |
| Authorization | Update User | Target Username | target.alternateId |
| Authorization | Update User | Target Attribute Context | debugContext.debugData.changedAttributes |
| Authorization | Delete User | Timestamp | published |
| Authorization | Delete User | Event ID | uuid |
| Authorization | Delete User | Event Code / Type | eventType |
| Authorization | Delete User | Result | outcome.result |
| Authorization | Delete User | Username | actor.alternateId |
| Authorization | Delete User | User ID | actor.id |
| Authorization | Delete User | Session ID | authenticationContext.externalSessionId |
| Authorization | Delete User | IP Address | client.ipAddress |
| Authorization | Delete User | IP Geolocation / ASN | client.geographicalContext |
| Authorization | Delete User | User Agent Name | client.userAgent |
| Authorization | Delete User | Device/Client Type | client.device |
| Authorization | Delete User | Target Username | target.alternateId |
| Authorization | Create Group | Timestamp | published |
| Authorization | Create Group | Event ID | uuid |
| Authorization | Create Group | Event Code / Type | eventType |
| Authorization | Create Group | Result | outcome.result |
| Authorization | Create Group | Username | actor.alternateId |
| Authorization | Create Group | User ID | actor.id |
| Authorization | Create Group | Session ID | authenticationContext.externalSessionId |
| Authorization | Create Group | IP Address | client.ipAddress |
| Authorization | Create Group | IP Geolocation / ASN | client.geographicalContext |
| Authorization | Create Group | User Agent Name | client.userAgent |
| Authorization | Create Group | Device/Client Type | client.device |
| Authorization | Create Group | Target Group Name | target.displayName |
| Authorization | Update Group | Timestamp | published |
| Authorization | Update Group | Event ID | uuid |
| Authorization | Update Group | Event Code / Type | eventType |
| Authorization | Update Group | Result | outcome.result |
| Authorization | Update Group | Username | actor.alternateId |
| Authorization | Update Group | User ID | actor.id |
| Authorization | Update Group | Session ID | authenticationContext.externalSessionId |
| Authorization | Update Group | IP Address | client.ipAddress |
| Authorization | Update Group | IP Geolocation / ASN | client.geographicalContext |
| Authorization | Update Group | User Agent Name | client.userAgent |
| Authorization | Update Group | Device/Client Type | client.device |
| Authorization | Update Group | Target Group Name | target.displayName |
| Authorization | Update Group | Target Attribute Context | target.displayName |
| Authorization | Delete Group | Timestamp | published |
| Authorization | Delete Group | Event ID | uuid |
| Authorization | Delete Group | Event Code / Type | eventType |
| Authorization | Delete Group | Result | outcome.result |
| Authorization | Delete Group | Username | actor.alternateId |
| Authorization | Delete Group | User ID | actor.id |
| Authorization | Delete Group | Session ID | authenticationContext.externalSessionId |
| Authorization | Delete Group | IP Address | client.ipAddress |
| Authorization | Delete Group | IP Geolocation / ASN | client.geographicalContext |
| Authorization | Delete Group | User Agent Name | client.userAgent |
| Authorization | Delete Group | Device/Client Type | client.device |
| Authorization | Delete Group | Target Group Name | target.displayName |
| Authorization | Add To Group | Timestamp | published |
| Authorization | Add To Group | Event ID | uuid |
| Authorization | Add To Group | Event Code / Type | eventType |
| Authorization | Add To Group | Result | outcome.result |
| Authorization | Add To Group | Username | actor.alternateId |
| Authorization | Add To Group | User ID | actor.id |
| Authorization | Add To Group | Session ID | authenticationContext.externalSessionId |
| Authorization | Add To Group | IP Address | client.ipAddress |
| Authorization | Add To Group | IP Geolocation / ASN | client.geographicalContext |
| Authorization | Add To Group | User Agent Name | client.userAgent |
| Authorization | Add To Group | Device/Client Type | client.device |
| Authorization | Add To Group | Target Group Name | target.displayName |
| Authorization | Add To Group | Target Username | target.displayName |
| Authorization | Remove From Group | Timestamp | published |
| Authorization | Remove From Group | Event ID | uuid |
| Authorization | Remove From Group | Event Code / Type | eventType |
| Authorization | Remove From Group | Result | outcome.result |
| Authorization | Remove From Group | Username | actor.alternateId |
| Authorization | Remove From Group | User ID | actor.id |
| Authorization | Remove From Group | Session ID | authenticationContext.externalSessionId |
| Authorization | Remove From Group | IP Address | client.ipAddress |
| Authorization | Remove From Group | IP Geolocation / ASN | client.geographicalContext |
| Authorization | Remove From Group | User Agent Name | client.userAgent |
| Authorization | Remove From Group | Device/Client Type | client.device |
| Authorization | Remove From Group | Target Group Name | target.displayName |
| Authorization | Remove From Group | Target Username | target.displayName |
| Authorization | Create Role | Timestamp | published |
| Authorization | Create Role | Event ID | uuid |
| Authorization | Create Role | Event Code / Type | eventType |
| Authorization | Create Role | Result | outcome.result |
| Authorization | Create Role | Username | actor.alternateId |
| Authorization | Create Role | User ID | actor.id |
| Authorization | Create Role | Session ID | authenticationContext.externalSessionId |
| Authorization | Create Role | IP Address | client.ipAddress |
| Authorization | Create Role | IP Geolocation / ASN | client.geographicalContext |
| Authorization | Create Role | User Agent Name | client.userAgent |
| Authorization | Create Role | Device/Client Type | client.device |
| Authorization | Create Role | Target Role Name | target.displayName |
| Authorization | Update Role | Timestamp | published |
| Authorization | Update Role | Event ID | uuid |
| Authorization | Update Role | Event Code / Type | eventType |
| Authorization | Update Role | Result | outcome.result |
| Authorization | Update Role | Username | actor.alternateId |
| Authorization | Update Role | User ID | actor.id |
| Authorization | Update Role | Session ID | authenticationContext.externalSessionId |
| Authorization | Update Role | IP Address | client.ipAddress |
| Authorization | Update Role | IP Geolocation / ASN | client.geographicalContext |
| Authorization | Update Role | User Agent Name | client.userAgent |
| Authorization | Update Role | Device/Client Type | client.device |
| Authorization | Update Role | Target Role Name | target.displayName |
| Authorization | Update Role | Target Attribute Context | target.displayName |
| Authorization | Delete Role | Timestamp | published |
| Authorization | Delete Role | Event ID | uuid |
| Authorization | Delete Role | Event Code / Type | eventType |
| Authorization | Delete Role | Result | outcome.result |
| Authorization | Delete Role | Username | actor.alternateId |
| Authorization | Delete Role | User ID | actor.id |
| Authorization | Delete Role | Session ID | authenticationContext.externalSessionId |
| Authorization | Delete Role | IP Address | client.ipAddress |
| Authorization | Delete Role | IP Geolocation / ASN | client.geographicalContext |
| Authorization | Delete Role | User Agent Name | client.userAgent |
| Authorization | Delete Role | Device/Client Type | client.device |
| Authorization | Delete Role | Target Role Name | target.displayName |
| Authorization | Add Permission | Timestamp | published |
| Authorization | Add Permission | Event ID | uuid |
| Authorization | Add Permission | Event Code / Type | eventType |
| Authorization | Add Permission | Result | outcome.result |
| Authorization | Add Permission | Username | actor.alternateId |
| Authorization | Add Permission | User ID | actor.id |
| Authorization | Add Permission | Session ID | authenticationContext.externalSessionId |
| Authorization | Add Permission | IP Address | client.ipAddress |
| Authorization | Add Permission | IP Geolocation / ASN | client.geographicalContext |
| Authorization | Add Permission | User Agent Name | client.userAgent |
| Authorization | Add Permission | Device/Client Type | client.device |
| Authorization | Add Permission | Permission Name | debugContext.debugData.privilegeGranted |
| Authorization | Add Permission | Target Resource Name | target.alternateId |
| Authorization | Remove Permission | Timestamp | published |
| Authorization | Remove Permission | Event ID | uuid |
| Authorization | Remove Permission | Event Code / Type | eventType |
| Authorization | Remove Permission | Result | outcome.result |
| Authorization | Remove Permission | Username | actor.alternateId |
| Authorization | Remove Permission | User ID | actor.id |
| Authorization | Remove Permission | Session ID | authenticationContext.externalSessionId |
| Authorization | Remove Permission | IP Address | client.ipAddress |
| Authorization | Remove Permission | IP Geolocation / ASN | client.geographicalContext |
| Authorization | Remove Permission | User Agent Name | client.userAgent |
| Authorization | Remove Permission | Device/Client Type | client.device |
| Authorization | Remove Permission | Permission Name | debugContext.debugData.privilegeRevoked |
| Authorization | Remove Permission | Target Resource Name | target.alternateId |
| Authorization | Add Enrollment | Timestamp | published |
| Authorization | Add Enrollment | Event ID | uuid |
| Authorization | Add Enrollment | Event Code / Type | eventType |
| Authorization | Add Enrollment | Result | outcome.result |
| Authorization | Add Enrollment | Username | actor.alternateId |
| Authorization | Add Enrollment | User ID | actor.id |
| Authorization | Add Enrollment | Session ID | authenticationContext.externalSessionId |
| Authorization | Add Enrollment | IP Address | client.ipAddress |
| Authorization | Add Enrollment | IP Geolocation / ASN | client.geographicalContext |
| Authorization | Add Enrollment | User Agent Name | client.userAgent |
| Authorization | Add Enrollment | Device/Client Type | client.device |
| Authorization | Add Enrollment | Enrollment Type | outcome.reason |
| Authorization | Add Enrollment | Target Username | target.alternateId |
| Authorization | Remove Enrollment | Timestamp | published |
| Authorization | Remove Enrollment | Event ID | uuid |
| Authorization | Remove Enrollment | Event Code / Type | eventType |
| Authorization | Remove Enrollment | Result | outcome.result |
| Authorization | Remove Enrollment | Username | actor.alternateId |
| Authorization | Remove Enrollment | User ID | actor.id |
| Authorization | Remove Enrollment | Session ID | authenticationContext.externalSessionId |
| Authorization | Remove Enrollment | IP Address | client.ipAddress |
| Authorization | Remove Enrollment | IP Geolocation / ASN | client.geographicalContext |
| Authorization | Remove Enrollment | User Agent Name | client.userAgent |
| Authorization | Remove Enrollment | Device/Client Type | client.device |
| Authorization | Remove Enrollment | Enrollment Type | outcome.reason |
| Authorization | Remove Enrollment | Target Username | target.alternateId |
| System Audit | Create Security Configuration | Timestamp | published |
| System Audit | Create Security Configuration | Event ID | uuid |
| System Audit | Create Security Configuration | Event Code / Type | eventType |
| System Audit | Create Security Configuration | Result | outcome.result |
| System Audit | Create Security Configuration | Username | actor.alternateId |
| System Audit | Create Security Configuration | User ID | actor.id |
| System Audit | Create Security Configuration | Session ID | authenticationContext.externalSessionId |
| System Audit | Create Security Configuration | IP Address | client.ipAddress |
| System Audit | Create Security Configuration | IP Geolocation / ASN | client.geographicalContext |
| System Audit | Create Security Configuration | User Agent Name | client.userAgent |
| System Audit | Create Security Configuration | Device/Client Type | client.device |
| System Audit | Create Security Configuration | Configuration / Setting Name | target.displayName |
| System Audit | Update Security Configuration | Timestamp | published |
| System Audit | Update Security Configuration | Event ID | uuid |
| System Audit | Update Security Configuration | Event Code / Type | eventType |
| System Audit | Update Security Configuration | Result | outcome.result |
| System Audit | Update Security Configuration | Username | actor.alternateId |
| System Audit | Update Security Configuration | User ID | actor.id |
| System Audit | Update Security Configuration | Session ID | authenticationContext.externalSessionId |
| System Audit | Update Security Configuration | IP Address | client.ipAddress |
| System Audit | Update Security Configuration | IP Geolocation / ASN | client.geographicalContext |
| System Audit | Update Security Configuration | User Agent Name | client.userAgent |
| System Audit | Update Security Configuration | Device/Client Type | client.device |
| System Audit | Update Security Configuration | Configuration / Setting Name | target.displayName |
| System Audit | Update Security Configuration | Configuration / Setting Value | debugContext.debugData.zoneData |
| System Audit | Delete Security Configuration | Timestamp | published |
| System Audit | Delete Security Configuration | Event ID | uuid |
| System Audit | Delete Security Configuration | Event Code / Type | eventType |
| System Audit | Delete Security Configuration | Result | outcome.result |
| System Audit | Delete Security Configuration | Username | actor.alternateId |
| System Audit | Delete Security Configuration | User ID | actor.id |
| System Audit | Delete Security Configuration | Session ID | authenticationContext.externalSessionId |
| System Audit | Delete Security Configuration | IP Address | client.ipAddress |
| System Audit | Delete Security Configuration | IP Geolocation / ASN | client.geographicalContext |
| System Audit | Delete Security Configuration | User Agent Name | client.userAgent |
| System Audit | Delete Security Configuration | Device/Client Type | client.device |
| System Audit | Delete Security Configuration | Configuration / Setting Name | target.displayName |
| System Audit | Create Integration | Timestamp | published |
| System Audit | Create Integration | Event ID | uuid |
| System Audit | Create Integration | Event Code / Type | eventType |
| System Audit | Create Integration | Result | outcome.result |
| System Audit | Create Integration | Username | actor.alternateId |
| System Audit | Create Integration | User ID | actor.id |
| System Audit | Create Integration | Session ID | authenticationContext.externalSessionId |
| System Audit | Create Integration | IP Address | client.ipAddress |
| System Audit | Create Integration | IP Geolocation / ASN | client.geographicalContext |
| System Audit | Create Integration | User Agent Name | client.userAgent |
| System Audit | Create Integration | Device/Client Type | client.device |
| System Audit | Create Integration | Integration / App Name | target.displayName |
| System Audit | Update Integration | Timestamp | published |
| System Audit | Update Integration | Event ID | uuid |
| System Audit | Update Integration | Event Code / Type | eventType |
| System Audit | Update Integration | Result | outcome.result |
| System Audit | Update Integration | Username | actor.alternateId |
| System Audit | Update Integration | User ID | actor.id |
| System Audit | Update Integration | Session ID | authenticationContext.externalSessionId |
| System Audit | Update Integration | IP Address | client.ipAddress |
| System Audit | Update Integration | IP Geolocation / ASN | client.geographicalContext |
| System Audit | Update Integration | User Agent Name | client.userAgent |
| System Audit | Update Integration | Device/Client Type | client.device |
| System Audit | Update Integration | Integration / App Name | target.displayName |
| System Audit | Update Integration | Configuration / Setting Name | debugContext.debugData.newSignonModeType |
| System Audit | Update Integration | Previous Configuration / Setting Value | debugContext.debugData.oldSignonModeType |
| System Audit | Delete Integration | Timestamp | published |
| System Audit | Delete Integration | Event ID | uuid |
| System Audit | Delete Integration | Event Code / Type | eventType |
| System Audit | Delete Integration | Result | outcome.result |
| System Audit | Delete Integration | Username | actor.alternateId |
| System Audit | Delete Integration | User ID | actor.id |
| System Audit | Delete Integration | Session ID | authenticationContext.externalSessionId |
| System Audit | Delete Integration | IP Address | client.ipAddress |
| System Audit | Delete Integration | IP Geolocation / ASN | client.geographicalContext |
| System Audit | Delete Integration | User Agent Name | client.userAgent |
| System Audit | Delete Integration | Device/Client Type | client.device |
| System Audit | Delete Integration | Integration / App Name | target.displayName |
| Activity Audit | Create Resource | Timestamp | published |
| Activity Audit | Create Resource | Event ID | uuid |
| Activity Audit | Create Resource | Event Code / Type | eventType |
| Activity Audit | Create Resource | Result | outcome.result |
| Activity Audit | Create Resource | Username | actor.alternateId |
| Activity Audit | Create Resource | User ID | actor.id |
| Activity Audit | Create Resource | Session ID | authenticationContext.externalSessionId |
| Activity Audit | Create Resource | IP Address | client.ipAddress |
| Activity Audit | Create Resource | IP Geolocation / ASN | client.geographicalContext |
| Activity Audit | Create Resource | User Agent Name | client.userAgent |
| Activity Audit | Create Resource | Device/Client Type | client.device |
| Activity Audit | Create Resource | Resource Name | target.displayName |
| Activity Audit | Create Resource | Resource Type | target.type |
| Activity Audit | Update Resource | Timestamp | published |
| Activity Audit | Update Resource | Event ID | uuid |
| Activity Audit | Update Resource | Event Code / Type | eventType |
| Activity Audit | Update Resource | Result | outcome.result |
| Activity Audit | Update Resource | Username | actor.alternateId |
| Activity Audit | Update Resource | User ID | actor.id |
| Activity Audit | Update Resource | Session ID | authenticationContext.externalSessionId |
| Activity Audit | Update Resource | IP Address | client.ipAddress |
| Activity Audit | Update Resource | IP Geolocation / ASN | client.geographicalContext |
| Activity Audit | Update Resource | User Agent Name | client.userAgent |
| Activity Audit | Update Resource | Device/Client Type | client.device |
| Activity Audit | Update Resource | Resource Name | target.displayName |
| Activity Audit | Update Resource | Resource Type | target.type |
| Activity Audit | Delete Resource | Timestamp | published |
| Activity Audit | Delete Resource | Event ID | uuid |
| Activity Audit | Delete Resource | Event Code / Type | eventType |
| Activity Audit | Delete Resource | Result | outcome.result |
| Activity Audit | Delete Resource | Username | actor.alternateId |
| Activity Audit | Delete Resource | User ID | actor.id |
| Activity Audit | Delete Resource | Session ID | authenticationContext.externalSessionId |
| Activity Audit | Delete Resource | IP Address | client.ipAddress |
| Activity Audit | Delete Resource | IP Geolocation / ASN | client.geographicalContext |
| Activity Audit | Delete Resource | User Agent Name | client.userAgent |
| Activity Audit | Delete Resource | Device/Client Type | client.device |
| Activity Audit | Delete Resource | Resource Name | target.displayName |
| Activity Audit | Delete Resource | Resource Type | target.type |
| Activity Audit | Download Resource | Timestamp | published |
| Activity Audit | Download Resource | Event ID | uuid |
| Activity Audit | Download Resource | Event Code / Type | eventType |
| Activity Audit | Download Resource | Result | outcome.result |
| Activity Audit | Download Resource | Username | actor.alternateId |
| Activity Audit | Download Resource | User ID | actor.id |
| Activity Audit | Download Resource | Session ID | authenticationContext.externalSessionId |
| Activity Audit | Download Resource | IP Address | client.ipAddress |
| Activity Audit | Download Resource | IP Geolocation / ASN | client.geographicalContext |
| Activity Audit | Download Resource | User Agent Name | client.userAgent |
| Activity Audit | Download Resource | Device/Client Type | client.device |
| Activity Audit | Download Resource | Resource Name | target.displayName |
| Activity Audit | Download Resource | Resource Type | target.type |

## Example logs

| Category | Event type | Log | Sample field values |
| -------- | ---------- | --- | ------------------- |
| Authentication | Account Login | [success](/products/okta/event_examples/authentication_account_login_session_success.json) | Timestamp=2023-09-06T19:06:27.080Z; Event ID=11111111-2222-3333-4444-abcdef111111111111; Event Code / Type=user.session.start; Username=alice@example.com; User ID=00ua1aaaa1abc0A0B123 |
| Authentication | Account Login | [failure](/products/okta/event_examples/authentication_account_login_session_failure.json) | Timestamp=2023-09-13T16:27:10.220Z; Event ID=11111111-2222-3333-4444-abcdef111111111111; Event Code / Type=user.session.start; Username=alice@example.com; User ID=00ua1aaaa1abc0A0B123 |
| Authentication | Account Logout | [success](/products/okta/event_examples/authentication_account_logout.json) | Timestamp=2023-09-14T16:24:24.572Z; Event ID=11111111-2222-3333-4444-abcdef111111111111; Event Code / Type=user.session.end; Result=SUCCESS; Username=alice@example.com |
| Authentication | MFA Verification | [success](/products/okta/event_examples/authentication_mfa_verification.json) | Timestamp=2023-09-14T19:20:47.234Z; Event ID=11111111-2222-3333-4444-abcdef111111111111; Event Code / Type=user.authentication.auth_via_mfa; Result=SUCCESS; Username=alice@example.com |
| Authentication | MFA Verification | [flagged](/products/okta/event_examples/authentication_mfa_verification_flagged.json) | Timestamp=2023-09-14T19:07:28.185Z; Event ID=11111111-2222-3333-4444-abcdef111111111111; Event Code / Type=user.account.report_suspicious_activity_by_enduser; Result=SUCCESS; Username=alice@example.com |
| Authorization | Create User | [success](/products/okta/event_examples/authorization_create_user.json) | Timestamp=2023-09-14T20:18:47.825Z; Event ID=11111111-2222-3333-4444-abcdef111111111111; Event Code / Type=user.lifecycle.create; Result=SUCCESS; Username=alice@example.com |
| Authorization | Update User | [success](/products/okta/event_examples/authorization_update_user.json) | Timestamp=2023-09-14T20:20:05.557Z; Event ID=11111111-2222-3333-4444-abcdef111111111111; Event Code / Type=user.account.update_profile; Result=SUCCESS; Username=alice@example.com |
| Authorization | Delete User | [success](/products/okta/event_examples/authorization_delete_user.json) | Timestamp=2023-09-14T20:21:30.151Z; Event ID=11111111-2222-3333-4444-abcdef111111111111; Event Code / Type=user.lifecycle.delete.initiated; Result=SUCCESS; Username=alice@example.com |
| Authorization | Create Group | [success](/products/okta/event_examples/authorization_create_group.json) | Timestamp=2023-09-14T18:58:09.243Z; Event ID=11111111-2222-3333-4444-abcdef111111111111; Event Code / Type=group.lifecycle.create; Result=SUCCESS; Username=alice@example.com |
| Authorization | Update Group | [success](/products/okta/event_examples/authorization_update_group.json) | Timestamp=2023-09-14T20:22:38.036Z; Event ID=11111111-2222-3333-4444-abcdef111111111111; Event Code / Type=group.application_assignment.add; Result=SUCCESS; Username=alice@example.com |
| Authorization | Delete Group | [success](/products/okta/event_examples/authorization_delete_group.json) | Timestamp=2023-09-14T20:23:26.473Z; Event ID=11111111-2222-3333-4444-abcdef111111111111; Event Code / Type=group.lifecycle.delete; Result=SUCCESS; Username=alice@example.com |
| Authorization | Add To Group | [success](/products/okta/event_examples/authorization_add_to_group.json) | Timestamp=2023-09-14T20:26:40.529Z; Event ID=11111111-2222-3333-4444-abcdef111111111111; Event Code / Type=group.user_membership.add; Result=SUCCESS; Username=alice@example.com |
| Authorization | Remove From Group | [success](/products/okta/event_examples/authorization_remove_from_group.json) | Timestamp=2023-09-14T20:27:00.112Z; Event ID=11111111-2222-3333-4444-abcdef111111111111; Event Code / Type=group.user_membership.remove; Result=SUCCESS; Username=alice@example.com |
| Authorization | Create Role | [success](/products/okta/event_examples/authorization_create_role.json) | Timestamp=2023-09-14T20:32:05.713Z; Event ID=11111111-2222-3333-4444-abcdef111111111111; Event Code / Type=iam.role.create; Result=SUCCESS; Username=alice@example.com |
| Authorization | Update Role | [success](/products/okta/event_examples/authorization_update_role.json) | Timestamp=2023-09-14T20:32:28.571Z; Event ID=11111111-2222-3333-4444-abcdef111111111111; Event Code / Type=iam.role.permissions.delete; Result=SUCCESS; Username=alice@example.com |
| Authorization | Delete Role | [success](/products/okta/event_examples/authorization_delete_role.json) | Timestamp=2023-09-14T20:32:33.316Z; Event ID=11111111-2222-3333-4444-abcdef111111111111; Event Code / Type=iam.role.delete; Result=SUCCESS; Username=alice@example.com |
| Authorization | Add Permission | [success](/products/okta/event_examples/authorization_add_permission.json) | Timestamp=2023-09-14T20:26:40.657Z; Event ID=11111111-2222-3333-4444-abcdef111111111111; Event Code / Type=user.account.privilege.grant; Result=SUCCESS; Username=alice@example.com |
| Authorization | Remove Permission | [success](/products/okta/event_examples/authorization_remove_permission.json) | Timestamp=2023-09-14T20:27:00.236Z; Event ID=11111111-2222-3333-4444-abcdef111111111111; Event Code / Type=user.account.privilege.revoke; Result=SUCCESS; Username=alice@example.com |
| Authorization | Add Enrollment | [success](/products/okta/event_examples/authorization_add_enrollment.json) | Timestamp=2023-09-14T19:09:25.749Z; Event ID=11111111-2222-3333-4444-abcdef111111111111; Event Code / Type=user.mfa.factor.activate; Result=SUCCESS; Username=alice@example.com |
| Authorization | Remove Enrollment | [success](/products/okta/event_examples/authorization_remove_enrollment.json) | Timestamp=2023-09-14T15:49:03.007Z; Event ID=11111111-2222-3333-4444-abcdef111111111111; Event Code / Type=user.mfa.factor.deactivate; Result=SUCCESS; Username=alice@example.com |
| System Audit | Create Security Configuration | [success](/products/okta/event_examples/system_audit_create_security_configuration_idp.json) | Timestamp=2023-09-14T20:33:22.575Z; Event ID=11111111-2222-3333-4444-abcdef111111111111; Event Code / Type=system.idp.lifecycle.create; Result=SUCCESS; Username=alice@example.com |
| System Audit | Update Security Configuration | [success](/products/okta/event_examples/system_audit_update_security_configuration_zone.json) | Timestamp=2023-09-12T01:40:39.219Z; Event ID=11111111-2222-3333-4444-abcdef111111111111; Event Code / Type=zone.update; Result=SUCCESS; Username=alice@example.com |
| System Audit | Delete Security Configuration | [success](/products/okta/event_examples/system_audit_delete_security_configuration_behavior.json) | Timestamp=2023-09-14T20:34:41.030Z; Event ID=11111111-2222-3333-4444-abcdef111111111111; Event Code / Type=security.behavior.settings.delete; Result=SUCCESS; Username=alice@example.com |
| System Audit | Create Integration | [success](/products/okta/event_examples/system_audit_create_integration.json) | Timestamp=2023-09-14T20:37:50.674Z; Event ID=11111111-2222-3333-4444-abcdef111111111111; Event Code / Type=application.lifecycle.create; Result=SUCCESS; Username=alice@example.com |
| System Audit | Update Integration | [success](/products/okta/event_examples/system_audit_update_integration.json) | Timestamp=2023-09-14T20:39:48.184Z; Event ID=11111111-2222-3333-4444-abcdef111111111111; Event Code / Type=application.lifecycle.update; Result=SUCCESS; Username=alice@example.com |
| System Audit | Delete Integration | [success](/products/okta/event_examples/system_audit_delete_integration.json) | Timestamp=2023-09-14T20:38:09.948Z; Event ID=11111111-2222-3333-4444-abcdef111111111111; Event Code / Type=application.lifecycle.delete; Result=SUCCESS; Username=alice@example.com |
| Activity Audit | Create Resource | [success](/products/okta/event_examples/activity_audit_create_resource.json) | Timestamp=2023-09-14T15:00:54.589Z; Event ID=11111111-2222-3333-4444-abcdef111111111111; Event Code / Type=system.api_token.create; Result=SUCCESS; Username=alice@example.com |
| Activity Audit | Update Resource | [success](/products/okta/event_examples/activity_audit_update_resource.json) | Timestamp=2023-09-19T20:41:41.654Z; Event ID=11111111-2222-3333-4444-abcdef111111111111; Event Code / Type=policy.rule.update; Result=SUCCESS; Username=alice@example.com |
| Activity Audit | Delete Resource | [success](/products/okta/event_examples/activity_audit_delete_resource.json) | Timestamp=2023-09-18T19:16:16.459Z; Event ID=11111111-2222-3333-4444-abcdef111111111111; Event Code / Type=workflows.user.flow.delete; Result=SUCCESS; Username=alice@example.com |
| Activity Audit | Download Resource | [success](/products/okta/event_examples/activity_audit_download_resource.json) | Timestamp=2023-09-14T17:45:28.879Z; Event ID=11111111-2222-3333-4444-abcdef111111111111; Event Code / Type=analytics.reports.export.download; Result=SUCCESS; Username=alice@example.com |


