# Google Workspace — Workspace Activity Audit

📌 **v0.0.1** · 🗄 **Retention:** Typically 6 months · ⚡ **Latency:** Near real time up to a couple hours

🗄 Service dependant - see https://support.google.com/a/answer/7061566?hl=en


⚡ Service dependant - see https://support.google.com/a/answer/7061566?hl=en


📜 **Licensing:** Admin logs are available for all Google Workspace plans. Drive audit logs and Device events may not be available as these are not available for the Business Starter plan. Additional configuration is required to get the full set of monitoring capabilities for Devices.


The activity audit log provides log events for actions occurring with your Google Workspace deployment.
## References
* [Google Workspace Activity Report](https://developers.google.com/admin-sdk/reports/reference/rest)
## Field mappings

| Category | Event type | Attribute | Source field(s) |
| -------- | ---------- | --------- | ---------------- |
| Authentication | Account Login | Timestamp | id.time |
| Authentication | Account Login | Event ID | etag |
| Authentication | Account Login | Event Code / Type | event.name |
| Authentication | Account Login | Username | actor.email |
| Authentication | Account Login | User ID | actor.profileId |
| Authentication | Account Login | IP Address | ipAddress |
| Authentication | Account Login | Failure Context | event.name, event.parameters[name=login_failure_type] |
| Authentication | Account Login | Credential Context | event.parameters[name=login_type] |
| Authentication | Account Logout | Timestamp | id.time |
| Authentication | Account Logout | Event ID | etag |
| Authentication | Account Logout | Event Code / Type | event.name |
| Authentication | Account Logout | Result | event.name |
| Authentication | Account Logout | Username | actor.email |
| Authentication | Account Logout | User ID | actor.profileId |
| Authentication | Account Logout | IP Address | ipAddress |
| Authentication | MFA Verification | Timestamp | id.time |
| Authentication | MFA Verification | Event ID | etag |
| Authentication | MFA Verification | Event Code / Type | event.name |
| Authentication | MFA Verification | Result | event.name |
| Authentication | MFA Verification | Username | actor.email |
| Authentication | MFA Verification | User ID | actor.profileId |
| Authentication | MFA Verification | IP Address | ipAddress |
| Authentication | MFA Verification | Verification Method | event.parameters[name=login_challenge_method] |
| Authentication | MFA Verification | Verification Flagged | event.parameters[name=is_suspicious] |
| Authentication | MFA Verification | Activity Performed | event.name |
| Authorization | Create User | Timestamp | id.time |
| Authorization | Create User | Event ID | etag |
| Authorization | Create User | Event Code / Type | event.name |
| Authorization | Create User | Username | actor.email |
| Authorization | Create User | User ID | actor.profileId |
| Authorization | Create User | User Type / Role | actor.callerType |
| Authorization | Create User | IP Address | ipAddress |
| Authorization | Create User | Target Username | event.parameters[name=USER_EMAIL] |
| Authorization | Update User | Timestamp | id.time |
| Authorization | Update User | Event ID | etag |
| Authorization | Update User | Event Code / Type | event.name |
| Authorization | Update User | Username | actor.email |
| Authorization | Update User | User ID | actor.profileId |
| Authorization | Update User | User Type / Role | actor.callerType |
| Authorization | Update User | IP Address | ipAddress |
| Authorization | Update User | Target Username | event.parameters[name=USER_EMAIL] |
| Authorization | Update User | Target Attribute Context | event.parameters[] |
| Authorization | Delete User | Timestamp | id.time |
| Authorization | Delete User | Event ID | etag |
| Authorization | Delete User | Event Code / Type | event.name |
| Authorization | Delete User | Username | actor.email |
| Authorization | Delete User | User ID | actor.profileId |
| Authorization | Delete User | User Type / Role | actor.callerType |
| Authorization | Delete User | IP Address | ipAddress |
| Authorization | Delete User | Target Username | event.parameters[name=USER_EMAIL] |
| Authorization | Create Group | Timestamp | id.time |
| Authorization | Create Group | Event ID | etag |
| Authorization | Create Group | Event Code / Type | event.name |
| Authorization | Create Group | Username | actor.email |
| Authorization | Create Group | User ID | actor.profileId |
| Authorization | Create Group | User Type / Role | actor.callerType |
| Authorization | Create Group | IP Address | ipAddress |
| Authorization | Create Group | Target Group Name | event.parameters[name=GROUP_EMAIL] |
| Authorization | Update Group | Timestamp | id.time |
| Authorization | Update Group | Event ID | etag |
| Authorization | Update Group | Event Code / Type | event.name |
| Authorization | Update Group | Username | actor.email |
| Authorization | Update Group | User ID | actor.profileId |
| Authorization | Update Group | User Type / Role | actor.callerType |
| Authorization | Update Group | Target Group Name | event.parameters[name=GROUP_EMAIL] |
| Authorization | Update Group | Target Attribute Context | event.parameters[name=SETTING_NAME] |
| Authorization | Delete Group | Timestamp | id.time |
| Authorization | Delete Group | Event ID | etag |
| Authorization | Delete Group | Event Code / Type | event.name |
| Authorization | Delete Group | Username | actor.email |
| Authorization | Delete Group | User ID | actor.profileId |
| Authorization | Delete Group | User Type / Role | actor.callerType |
| Authorization | Delete Group | IP Address | ipAddress |
| Authorization | Delete Group | Target Group Name | event.parameters[name=GROUP_EMAIL] |
| Authorization | Add To Group | Timestamp | id.time |
| Authorization | Add To Group | Event ID | etag |
| Authorization | Add To Group | Event Code / Type | event.name |
| Authorization | Add To Group | Username | actor.email |
| Authorization | Add To Group | User ID | actor.profileId |
| Authorization | Add To Group | User Type / Role | actor.callerType |
| Authorization | Add To Group | IP Address | ipAddress |
| Authorization | Add To Group | Target Group Name | event.parameters[name=GROUP_EMAIL] |
| Authorization | Add To Group | Target Username | event.parameters[name=USER_EMAIL] |
| Authorization | Remove From Group | Timestamp | id.time |
| Authorization | Remove From Group | Event ID | etag |
| Authorization | Remove From Group | Event Code / Type | event.name |
| Authorization | Remove From Group | Username | actor.email |
| Authorization | Remove From Group | User ID | actor.profileId |
| Authorization | Remove From Group | User Type / Role | actor.callerType |
| Authorization | Remove From Group | IP Address | ipAddress |
| Authorization | Remove From Group | Target Group Name | event.parameters[name=GROUP_EMAIL] |
| Authorization | Remove From Group | Target Username | event.parameters[name=USER_EMAIL] |
| Authorization | Create Role | Timestamp | id.time |
| Authorization | Create Role | Event ID | etag |
| Authorization | Create Role | Event Code / Type | event.name |
| Authorization | Create Role | Username | actor.email |
| Authorization | Create Role | User ID | actor.profileId |
| Authorization | Create Role | User Type / Role | actor.callerType |
| Authorization | Create Role | IP Address | ipAddress |
| Authorization | Create Role | Target Role Name | event.parameters[name=ROLE_NAME] |
| Authorization | Update Role | Timestamp | id.time |
| Authorization | Update Role | Event ID | etag |
| Authorization | Update Role | Event Code / Type | event.name |
| Authorization | Update Role | Username | actor.email |
| Authorization | Update Role | User ID | actor.profileId |
| Authorization | Update Role | User Type / Role | actor.callerType |
| Authorization | Update Role | IP Address | ipAddress |
| Authorization | Update Role | Target Role Name | event.parameters[name=ROLE_NAME] |
| Authorization | Update Role | Target Attribute Context | event.parameters |
| Authorization | Delete Role | Timestamp | id.time |
| Authorization | Delete Role | Event ID | etag |
| Authorization | Delete Role | Event Code / Type | event.name |
| Authorization | Delete Role | Username | actor.email |
| Authorization | Delete Role | User ID | actor.profileId |
| Authorization | Delete Role | User Type / Role | actor.callerType |
| Authorization | Delete Role | IP Address | ipAddress |
| Authorization | Delete Role | Target Role Name | event.parameters[name=ROLE_NAME] |
| Authorization | Add Permission | Timestamp | id.time |
| Authorization | Add Permission | Event ID | etag |
| Authorization | Add Permission | Event Code / Type | event.name |
| Authorization | Add Permission | Username | actor.email |
| Authorization | Add Permission | User ID | actor.profileId |
| Authorization | Add Permission | User Type / Role | actor.callerType |
| Authorization | Add Permission | IP Address | ipAddress |
| Authorization | Add Permission | Permission Name | event.parameters[name=PRIVILEGE_NAME] |
| Authorization | Add Permission | Target Resource Name | event.parameters[name=ROLE_NAME] |
| Authorization | Remove Permission | Timestamp | id.time |
| Authorization | Remove Permission | Event ID | etag |
| Authorization | Remove Permission | Event Code / Type | event.name |
| Authorization | Remove Permission | Username | actor.email |
| Authorization | Remove Permission | User ID | actor.profileId |
| Authorization | Remove Permission | User Type / Role | actor.callerType |
| Authorization | Remove Permission | IP Address | ipAddress |
| Authorization | Remove Permission | Permission Name | event.parameters[name=PRIVILEGE_NAME] |
| Authorization | Remove Permission | Target Resource Name | event.parameters[name=ROLE_NAME] |
| Authorization | Add Enrollment | Timestamp | id.time |
| Authorization | Add Enrollment | Event ID | etag |
| Authorization | Add Enrollment | Event Code / Type | event.name |
| Authorization | Add Enrollment | Username | actor.email |
| Authorization | Add Enrollment | User ID | actor.profileId |
| Authorization | Add Enrollment | User Type / Role | actor.callerType |
| Authorization | Add Enrollment | IP Address | ipAddress |
| Authorization | Add Enrollment | Target Username | event.parameters[name=USER_EMAIL] |
| Authorization | Remove Enrollment | Timestamp | id.time |
| Authorization | Remove Enrollment | Event ID | etag |
| Authorization | Remove Enrollment | Event Code / Type | event.name |
| Authorization | Remove Enrollment | Username | actor.email |
| Authorization | Remove Enrollment | User ID | actor.profileId |
| Authorization | Remove Enrollment | User Type / Role | actor.callerType |
| Authorization | Remove Enrollment | IP Address | ipAddress |
| Authorization | Remove Enrollment | Target Username | event.parameters[name=USER_EMAIL] |
| System Audit | Create Security Configuration | Timestamp | id.time |
| System Audit | Create Security Configuration | Event ID | etag |
| System Audit | Create Security Configuration | Event Code / Type | event.name |
| System Audit | Create Security Configuration | Username | actor.email |
| System Audit | Create Security Configuration | User ID | actor.profileId |
| System Audit | Create Security Configuration | Configuration / Setting Name | event.parameters |
| System Audit | Create Security Configuration | Configuration / Setting Value | event.parameters |
| System Audit | Update Security Configuration | Timestamp | id.time |
| System Audit | Update Security Configuration | Event ID | etag |
| System Audit | Update Security Configuration | Event Code / Type | event.name |
| System Audit | Update Security Configuration | Username | actor.email |
| System Audit | Update Security Configuration | User ID | actor.profileId |
| System Audit | Update Security Configuration | User Type / Role | actor.callerType |
| System Audit | Update Security Configuration | Configuration / Setting Name | event.parameters[name=*] |
| System Audit | Update Security Configuration | Configuration / Setting Value | event.parameters[name=*] |
| System Audit | Delete Security Configuration | Timestamp | id.time |
| System Audit | Delete Security Configuration | Event ID | etag |
| System Audit | Delete Security Configuration | Event Code / Type | event.name |
| System Audit | Delete Security Configuration | Username | actor.email |
| System Audit | Delete Security Configuration | User ID | actor.profileId |
| System Audit | Delete Security Configuration | User Type / Role | actor.callerType |
| System Audit | Delete Security Configuration | Configuration / Setting Name | event.parameters[name=*] |
| System Audit | Delete Security Configuration | Configuration / Setting Value | event.parameters[name=*] |
| System Audit | Create Integration | Timestamp | id.time |
| System Audit | Create Integration | Event ID | etag |
| System Audit | Create Integration | Event Code / Type | event.name |
| System Audit | Create Integration | Username | actor.email |
| System Audit | Create Integration | User ID | actor.profileId |
| System Audit | Create Integration | User Type / Role | actor.callerType |
| System Audit | Create Integration | Integration / App Name | event.parameters[name=APPLICATION_NAME] |
| System Audit | Update Integration | Timestamp | id.time |
| System Audit | Update Integration | Event ID | etag |
| System Audit | Update Integration | Event Code / Type | event.name |
| System Audit | Update Integration | Username | actor.email |
| System Audit | Update Integration | User ID | actor.profileId |
| System Audit | Update Integration | User Type / Role | actor.callerType |
| System Audit | Update Integration | IP Address | ipAddress |
| System Audit | Update Integration | Integration / App Name | event.parameters[name=APPLICATION_NAME] |
| System Audit | Update Integration | Configuration / Setting Name | event.parameters[name=NEW_VALUE] |
| System Audit | Update Integration | Previous Configuration / Setting Value | event.parameters[name=OLD_VALUE] |
| System Audit | Delete Integration | Timestamp | id.time |
| System Audit | Delete Integration | Event ID | etag |
| System Audit | Delete Integration | Event Code / Type | event.name |
| System Audit | Delete Integration | Username | actor.email |
| System Audit | Delete Integration | User ID | actor.profileId |
| System Audit | Delete Integration | User Type / Role | actor.callerType |
| System Audit | Delete Integration | Integration / App Name | event.parameters[name=APPLICATION_NAME] |
| Activity Audit | Create Resource | Timestamp | id.time |
| Activity Audit | Create Resource | Event ID | etag |
| Activity Audit | Create Resource | Event Code / Type | event.name |
| Activity Audit | Create Resource | Username | actor.email |
| Activity Audit | Create Resource | User ID | actor.profileId |
| Activity Audit | Create Resource | User Type / Role | actor.callerType |
| Activity Audit | Create Resource | IP Address | ipAddress |
| Activity Audit | Create Resource | Resource Name | event.parameters[].name |
| Activity Audit | Create Resource | Resource Type | event.type |
| Activity Audit | Update Resource | Timestamp | id.time |
| Activity Audit | Update Resource | Event ID | etag |
| Activity Audit | Update Resource | Event Code / Type | event.name |
| Activity Audit | Update Resource | Username | actor.email |
| Activity Audit | Update Resource | User ID | actor.profileId |
| Activity Audit | Update Resource | User Type / Role | actor.callerType |
| Activity Audit | Update Resource | IP Address | ipAddress |
| Activity Audit | Update Resource | Resource Name | event.parameters[].name |
| Activity Audit | Update Resource | Resource Type | event.type |
| Activity Audit | Delete Resource | Timestamp | id.time |
| Activity Audit | Delete Resource | Event ID | etag |
| Activity Audit | Delete Resource | Event Code / Type | event.name |
| Activity Audit | Delete Resource | Username | actor.email |
| Activity Audit | Delete Resource | User ID | actor.profileId |
| Activity Audit | Delete Resource | User Type / Role | actor.callerType |
| Activity Audit | Delete Resource | IP Address | ipAddress |
| Activity Audit | Delete Resource | Resource Name | event.parameters[].name |
| Activity Audit | Delete Resource | Resource Type | event.type |
| Activity Audit | Download Resource | Timestamp | id.time |
| Activity Audit | Download Resource | Event ID | etag |
| Activity Audit | Download Resource | Event Code / Type | event.name |
| Activity Audit | Download Resource | Username | actor.email |
| Activity Audit | Download Resource | User ID | actor.profileId |
| Activity Audit | Download Resource | IP Address | ipAddress |
| Activity Audit | Download Resource | Resource Metadata | event.parameters[].name |
| Activity Audit | Download Resource | Resource Name | event.parameters[name=doc_title] |
| Activity Audit | Download Resource | Resource Type | event.parameters[name=doc_type] |
| Activity Audit | Query Resource | Timestamp | id.time |
| Activity Audit | Query Resource | Event ID | etag |
| Activity Audit | Query Resource | Event Code / Type | event.name |
| Activity Audit | Query Resource | Username | actor.email |
| Activity Audit | Query Resource | User ID | actor.profileId |
| Activity Audit | Query Resource | IP Address | ipAddress |
| Activity Audit | Query Resource | Query String | event.parameters[name=user_query] |

## Example logs

| Category | Event type | Log | Sample field values |
| -------- | ---------- | --- | ------------------- |
| Authentication | Account Login | [success](/products/google_workspace/event_examples/authentication_account_login.json) | Timestamp=2023-10-04T17:05:18.707Z; Event ID="rQ3qpTrpjMqlOD9Fi6ZCgnpogfhr6664Y4wU0J6c8Yw/T8TMuJvnXTPKpw…; Event Code / Type=login_success; Username=egrt@test.com; User ID=10206845645323004074611 |
| Authentication | Account Logout | [success](/products/google_workspace/event_examples/authentication_account_logout.json) | Timestamp=2023-10-04T16:44:09.155Z; Event ID="rQ3qpTrpjMqlOD9Fi6ZCsdfsdfsdf0J6c8Yw/g9-7HZArWTv3ua4W8l_Ur…; Event Code / Type=logout; Result=logout; Username=tlsdfr@test.com |
| Authentication | MFA Verification | [success](/products/google_workspace/event_examples/authentication_mfa_verification.json) | Timestamp=2023-10-04T17:00:38.873Z; Event ID="rQ3qpTrpjMqlOD9Fi6ZCgnpo6zAdUtM4hgihb7gw/-PaydDWGhijb567Dz…; Event Code / Type=login_success; Result=login_success; Username=dfggg@test.com |
| Authorization | Create User | [success](/products/google_workspace/event_examples/authorization_create_user.json) | Timestamp=2023-10-04T17:27:02.768Z; Event ID="rQ3qpTrpjMqlOD9Fi6ZCgnwwpo6zAd3g53g55U0J6c8Yw/5pzih88L6fo0…; Event Code / Type=CREATE_USER; Username=test@test.com; User ID=111620519819984096 |
| Authorization | Update User | [success](/products/google_workspace/event_examples/authorization_update_user.json) | Timestamp=2023-10-04T17:12:20.110Z; Event ID="rQ3qpTrpjMqlOD9Fi6ZCgnpo6ze8herg98hJ6c8Yw/jgqx0-DnGyAy2VkA…; Event Code / Type=USER_LICENSE_REVOKE; Username=test2@test2.com; User ID=1169451581811976442 |
| Authorization | Delete User | [success](/products/google_workspace/event_examples/authorization_delete_user.json) | Timestamp=2023-10-04T17:26:56.224Z; Event ID="rQ3qpTrpjMqlOD9Fi6ZCgerfe5t5g0J6c8Yw/jWiJ6tV0iybyuoS8eKnls…; Event Code / Type=DELETE_USER; Username=test@test.com; User ID=11111118126984096 |
| Authorization | Create Group | [success](/products/google_workspace/event_examples/authorization_create_group.json) | Timestamp=2023-10-04T16:19:08.748Z; Event ID="rQ3qpTrpjMqlOD9Fi6ZCgnpo6ref454w4t3f6c8Yw/D6SAzt5ZDFR6eWcn…; Event Code / Type=CREATE_GROUP; Username=test@test.com; User ID=1122063181981927490212 |
| Authorization | Update Group | [success](/products/google_workspace/event_examples/authorization_update_group.json) | Timestamp=2023-10-04T14:33:20.949Z; Event ID="rQ3qpTrpjMqlOD9Fi887ghvuhbu77byv55c8Yw/b20Viygiyu7bUjyhpl5…; Event Code / Type=CHANGE_GROUP_SETTING; Username=test@test.com; User ID=154848611551817490212 |
| Authorization | Delete Group | [success](/products/google_workspace/event_examples/authorization_delete_group.json) | Timestamp=2023-10-09T22:12:29.027Z; Event ID="rQ3qpTrpjMdfg4544rG#GEGrY4w55c8Yw/rpsdsSCER8_5--B_QCoUl8YB…; Event Code / Type=DELETE_GROUP; Username=test@test.com; User ID=117158165166014059 |
| Authorization | Add To Group | [success](/products/google_workspace/event_examples/authorization_add_to_group.json) | Timestamp=2023-10-04T18:24:54.690Z; Event ID="rQ3qpTrpjMqlOD9Fifgh8f1fghf81gh4wU0J6c8Yw/MjJkdF51dfg5np52…; Event Code / Type=ADD_GROUP_MEMBER; Username=testa@test.com; User ID=10248166192532690543 |
| Authorization | Remove From Group | [success](/products/google_workspace/event_examples/authorization_remove_from_group.json) | Timestamp=2023-10-04T18:24:58.074Z; Event ID="rQ345lOD9Fi6Z65145556c8Yw/MFIFIW4tg4g51dg5157HWa1Lwss5Cr6g"; Event Code / Type=REMOVE_GROUP_MEMBER; Username=testa@test.com; User ID=10295165132690543 |
| Authorization | Create Role | [success](/products/google_workspace/event_examples/authorization_create_role.json) | Timestamp=2023-10-17T23:13:13.915Z; Event ID="jc94nIMyBsgegergergergOA9OLU9Ps/8q7ergergergergergeAca075m…; Event Code / Type=CREATE_ROLE; Username=test@test.com; User ID=1169519165745888518 |
| Authorization | Update Role | [success](/products/google_workspace/event_examples/authorization_update_role.json) | Timestamp=2023-10-17T23:13:13.915Z; Event ID="jc94nIMyBsgegergergergOA9OLU9Ps/8q7ergergergergergeAca075m…; Event Code / Type=UPDATE_ROLE; Username=test@test.com; User ID=1169519165745888518 |
| Authorization | Delete Role | [success](/products/google_workspace/event_examples/authorization_delete_role.json) | Timestamp=2023-10-17T23:13:13.915Z; Event ID="jc94nIMyBsgegergergergOA9OLU9Ps/8q7ergergergergergeAca075m…; Event Code / Type=DELETE_ROLE; Username=test@test.com; User ID=1169519165745888518 |
| Authorization | Add Permission | [success](/products/google_workspace/event_examples/authorization_add_permission.json) | Timestamp=2023-10-10T20:59:40.904Z; Event ID="rQ3qpTrpjMqlOD9Fi6ZCgdfgdf4wU0J6c8Yw/9MRxYfzAnE9dVdfgdfgdf…; Event Code / Type=ADD_PRIVILEGE; Username=test@test.com; User ID=10782284568708731702 |
| Authorization | Add Enrollment | [success](/products/google_workspace/event_examples/authorization_add_enrollment.json) | Timestamp=2023-10-03T23:11:59.995Z; Event ID="rQ3qpTrpjMqlOD9Fi6ZCef34f34f36c8Yw/3t4sr-Fc34f34fgC0do"; Event Code / Type=SECURITY_KEY_REGISTERED_FOR_USER; Username=test@test.com; User ID=11290751345894345842 |
| Authorization | Remove Enrollment | [success](/products/google_workspace/event_examples/authorization_remove_enrollment.json) | Timestamp=2023-10-03T22:33:48.843Z; Event ID="rQ3qpTrp45g35log5yh5btM4Y4wU0J6c8Yw/Njl5tg5tg5ergai-Mk"; Event Code / Type=REVOKE_SECURITY_KEY; Username=test@test.com; User ID=221195616515142 |
| System Audit | Create Security Configuration | [success](/products/google_workspace/event_examples/system_audit_create_security_configuration.json) | Timestamp=2023-10-03T21:26:36.365Z; Event ID="rQ3qpTrpjMqlryth5yh5yh5yh5J6c8Yw/0g3r6h6hHHU8fvg5zE"; Event Code / Type=CHANGE_CAA_APP_ASSIGNMENTS; Username=test@test.com; User ID=185459392577373 |
| System Audit | Create Integration | [success](/products/google_workspace/event_examples/system_audit_create_integration.json) | Timestamp=2023-10-12T15:59:23.551Z; Event ID="jc94nIMfgrtgrthrthrtXqUGGHrthrt9OLU9Ps/EN0CkgUCOrthrthrth5…; Event Code / Type=ADD_APPLICATION; Username=test@test.com; User ID=105905796516511368150 |
| System Audit | Update Integration | [success](/products/google_workspace/event_examples/system_audit_update_integration.json) | Timestamp=2023-10-04T16:37:47.039Z; Event ID="rQ3qpTrpjMqlOD9Firtrth56Y4wU0J6c8Yw/TmNY5656h6hhH4-rjrEGWN…; Event Code / Type=CHANGE_APPLICATION_SETTING; Username=test@test.com; User ID=11726318198115861321 |
| System Audit | Delete Integration | [success](/products/google_workspace/event_examples/system_audit_delete_integration.json) | Timestamp=2023-10-12T16:40:07.644Z; Event ID="jc94nIMyBF33ertgrhrthHOA9OLU9Ps/9CWrthretherthrTdaKCiZzGNs…; Event Code / Type=REMOVE_APPLICATION; Username=test@test.com; User ID=105905798198198168150 |
| Activity Audit | Create Resource | [success](/products/google_workspace/event_examples/audit_activity_create_resource.json) | Timestamp=2023-10-12T15:59:23.557Z; Event ID="jc94nIMyBF33rgergergergH0EHOA9OLU9Ps/JergergergereWa6e8Ij7…; Event Code / Type=CREATE_SAML2_SERVICE_PROVIDER_CONFIG; Username=test@test.com; User ID=105951899444368150 |
| Activity Audit | Update Resource | [success](/products/google_workspace/event_examples/audit_activity_update_resource.json) | Timestamp=2023-10-13T13:20:21.544Z; Event ID="jc94nIMyBF33sdsdgefefbe0EHOA9OLU9Ps/iRevefvefvefvCgiwiS_Xw…; Event Code / Type=CHANGE_EMAIL_SETTING; Username=test@test.com; User ID=10785165158808731702 |
| Activity Audit | Delete Resource | [success](/products/google_workspace/event_examples/audit_activity_delete_resource.json) | Timestamp=2023-10-16T09:48:53.629Z; Event ID="jc94nIMyBFdfggbrtbEHOA9OLU9Ps/6AY_7_Kbx--X_ArtbrtbrtbGBo0"; Event Code / Type=DELETE_2SV_SCRATCH_CODES; Username=test@test.com; User ID=10355165165102363077 |
| Activity Audit | Download Resource | [success](/products/google_workspace/event_examples/audit_activity_download_resource.json) | Timestamp=2023-10-15T23:35:01.493Z; Event ID="jc94nIMyBF33504pdfefgegegGH0EHOA9erg6Y7Yn5ugkRL-3ergergcdi…; Event Code / Type=download; Username=test@test.com; User ID=1095156489815781956899 |
| Activity Audit | Query Resource | [success](/products/google_workspace/event_examples/audit_activity_query_resource.json) | Timestamp=2026-02-01T10:15:01.523Z; Event ID="jc94nIMyBF76804pdfefgegegGH0EHOA9erg2Y7Yn5ugkRL-3uaabgecdi…; Event Code / Type=search; Username=test@test.com; User ID=1095156489815745756899 |


