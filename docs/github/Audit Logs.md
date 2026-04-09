





# GitHub — Audit Logs

📌 **v1.0.0** · 🗄 **Retention:** Infinite · ⚡ **Latency:** Near Real-Time

🗄 Can be changed by an enterprise admin




📜 **Licensing:** Included with GitHub Enterprise accounts.


GitHub enterprise audit logs that provide an audit trail of user and system activity.
## References
* [Enterprise Event Schema](https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/exporting-audit-log-activity-for-your-enterprise)
## Field mappings

| Category | Event type | Attribute | Source field(s) |
| -------- | ---------- | --------- | ---------------- |
| Authentication | Account Login | Timestamp | created_at |
| Authentication | Account Login | Event ID | _document_id |
| Authentication | Account Login | Event Code / Type | action |
| Authentication | Account Login | Username | actor |
| Authentication | Account Login | User ID | actor_id |
| Authentication | Account Login | IP Geolocation / ASN | actor_location.country_code |
| Authentication | Account Login | User Agent Name | user_agent |
| Authentication | Account Login | Credential Context | action |
| Authentication | Account Login | Identity Service Provider Context | issuer |
| Authorization | Create Group | Timestamp | created_at |
| Authorization | Create Group | Event ID | _document_id |
| Authorization | Create Group | Event Code / Type | action |
| Authorization | Create Group | Username | actor |
| Authorization | Create Group | User ID | actor_id |
| Authorization | Create Group | IP Address | actor_ip |
| Authorization | Create Group | IP Geolocation / ASN | actor_location.country_code |
| Authorization | Create Group | User Agent Name | user_agent |
| Authorization | Create Group | Target Group Name | org, team |
| Authorization | Update Group | Timestamp | created_at |
| Authorization | Update Group | Event ID | _document_id |
| Authorization | Update Group | Event Code / Type | action |
| Authorization | Update Group | Username | actor |
| Authorization | Update Group | User ID | actor_id |
| Authorization | Update Group | IP Address | actor_ip |
| Authorization | Update Group | IP Geolocation / ASN | actor_location.country_code |
| Authorization | Update Group | User Agent Name | user_agent |
| Authorization | Update Group | Target Group Name | org, team |
| Authorization | Delete Group | Timestamp | created_at |
| Authorization | Delete Group | Event ID | _document_id |
| Authorization | Delete Group | Event Code / Type | action |
| Authorization | Delete Group | Username | actor |
| Authorization | Delete Group | User ID | actor_id |
| Authorization | Delete Group | IP Address | actor_ip |
| Authorization | Delete Group | IP Geolocation / ASN | actor_location.country_code |
| Authorization | Delete Group | User Agent Name | user_agent |
| Authorization | Delete Group | Target Group Name | org, team |
| Authorization | Add To Group | Timestamp | created_at |
| Authorization | Add To Group | Event ID | _document_id |
| Authorization | Add To Group | Event Code / Type | action |
| Authorization | Add To Group | Username | actor |
| Authorization | Add To Group | User ID | actor_id |
| Authorization | Add To Group | IP Address | actor_ip |
| Authorization | Add To Group | IP Geolocation / ASN | actor_location.country_code |
| Authorization | Add To Group | User Agent Name | user_agent |
| Authorization | Add To Group | Target Username | user |
| Authorization | Add To Group | Target Group Name | org, team, repo |
| Authorization | Remove From Group | Timestamp | created_at |
| Authorization | Remove From Group | Event ID | _document_id |
| Authorization | Remove From Group | Event Code / Type | action |
| Authorization | Remove From Group | Username | actor |
| Authorization | Remove From Group | User ID | actor_id |
| Authorization | Remove From Group | IP Address | actor_ip |
| Authorization | Remove From Group | IP Geolocation / ASN | actor_location.country_code |
| Authorization | Remove From Group | Target Username | user |
| Authorization | Remove From Group | Target Group Name | org, team, repo |
| Authorization | Add Permission | Timestamp | created_at |
| Authorization | Add Permission | Event ID | _document_id |
| Authorization | Add Permission | Event Code / Type | action |
| Authorization | Add Permission | Username | actor |
| Authorization | Add Permission | User ID | actor_id |
| Authorization | Add Permission | IP Address | actor_ip |
| Authorization | Add Permission | IP Geolocation / ASN | actor_location.country_code |
| Authorization | Add Permission | User Agent Name | user_agent |
| Authorization | Add Permission | Permission Name | new_repo_permission |
| Authorization | Add Permission | Target Resource Name | org, team, repo |
| Authorization | Remove Permission | Timestamp | created_at |
| Authorization | Remove Permission | Event ID | _document_id |
| Authorization | Remove Permission | Event Code / Type | action |
| Authorization | Remove Permission | Username | actor |
| Authorization | Remove Permission | User ID | actor_id |
| Authorization | Remove Permission | IP Address | actor_ip |
| Authorization | Remove Permission | IP Geolocation / ASN | actor_location.country_code |
| Authorization | Remove Permission | User Agent Name | user_agent |
| Authorization | Remove Permission | Permission Name | old_repo_permission |
| Authorization | Remove Permission | Target Resource Name | org, team, repo |
| System Audit | Create Security Configuration | Timestamp | created_at |
| System Audit | Create Security Configuration | Event ID | _document_id |
| System Audit | Create Security Configuration | Event Code / Type | action |
| System Audit | Create Security Configuration | Username | actor |
| System Audit | Create Security Configuration | User ID | actor_id |
| System Audit | Create Security Configuration | IP Address | actor_ip |
| System Audit | Create Security Configuration | IP Geolocation / ASN | actor_location.country_code |
| System Audit | Create Security Configuration | User Agent Name | user_agent |
| System Audit | Create Security Configuration | Configuration / Setting Name | action |
| System Audit | Create Security Configuration | Configuration / Setting Value | action |
| System Audit | Update Security Configuration | Timestamp | created_at |
| System Audit | Update Security Configuration | Event ID | _document_id |
| System Audit | Update Security Configuration | Event Code / Type | action |
| System Audit | Update Security Configuration | Username | actor |
| System Audit | Update Security Configuration | User ID | actor_id |
| System Audit | Update Security Configuration | IP Address | actor_ip |
| System Audit | Update Security Configuration | IP Geolocation / ASN | actor_location.country_code |
| System Audit | Update Security Configuration | User Agent Name | user_agent |
| System Audit | Update Security Configuration | Configuration / Setting Name | name |
| System Audit | Update Security Configuration | Configuration / Setting Value | config |
| System Audit | Update Security Configuration | Previous Configuration / Setting Value | config_was |
| System Audit | Create Integration | Timestamp | created_at |
| System Audit | Create Integration | Event ID | _document_id |
| System Audit | Create Integration | Event Code / Type | action |
| System Audit | Create Integration | Username | actor |
| System Audit | Create Integration | User ID | actor_id |
| System Audit | Create Integration | IP Address | actor_ip |
| System Audit | Create Integration | IP Geolocation / ASN | actor_location.country_code |
| System Audit | Create Integration | User Agent Name | user_agent |
| System Audit | Create Integration | Integration / App Name | integration |
| System Audit | Delete Integration | Timestamp | created_at |
| System Audit | Delete Integration | Event ID | _document_id |
| System Audit | Delete Integration | Event Code / Type | action |
| System Audit | Delete Integration | Username | actor |
| System Audit | Delete Integration | User ID | actor_id |
| System Audit | Delete Integration | IP Address | actor_ip |
| System Audit | Delete Integration | IP Geolocation / ASN | actor_location.country_code |
| System Audit | Delete Integration | User Agent Name | user_agent |
| System Audit | Delete Integration | Integration / App Name | integration |
| Activity Audit | Create Resource | Timestamp | created_at |
| Activity Audit | Create Resource | Event ID | _document_id |
| Activity Audit | Create Resource | Event Code / Type | action |
| Activity Audit | Create Resource | Username | actor |
| Activity Audit | Create Resource | User ID | actor_id |
| Activity Audit | Create Resource | IP Address | actor_ip |
| Activity Audit | Create Resource | IP Geolocation / ASN | actor_location.country_code |
| Activity Audit | Create Resource | User Agent Name | user_agent |
| Activity Audit | Create Resource | Resource Name | org, business, repo |
| Activity Audit | Create Resource | Resource Type | action |
| Activity Audit | Update Resource | Timestamp | created_at |
| Activity Audit | Update Resource | Event ID | _document_id |
| Activity Audit | Update Resource | Event Code / Type | action |
| Activity Audit | Update Resource | Username | actor |
| Activity Audit | Update Resource | User ID | actor_id |
| Activity Audit | Update Resource | IP Address | actor_ip |
| Activity Audit | Update Resource | IP Geolocation / ASN | actor_location.country_code |
| Activity Audit | Update Resource | User Agent Name | user_agent |
| Activity Audit | Update Resource | Resource Name | org, business, repo |
| Activity Audit | Update Resource | Resource Type | action |
| Activity Audit | Delete Resource | Timestamp | created_at |
| Activity Audit | Delete Resource | Event ID | _document_id |
| Activity Audit | Delete Resource | Event Code / Type | action |
| Activity Audit | Delete Resource | Username | actor |
| Activity Audit | Delete Resource | User ID | actor_id |
| Activity Audit | Delete Resource | IP Address | actor_ip |
| Activity Audit | Delete Resource | IP Geolocation / ASN | actor_location.country_code |
| Activity Audit | Delete Resource | User Agent Name | user_agent |
| Activity Audit | Delete Resource | Resource Name | org, business, repo |
| Activity Audit | Delete Resource | Resource Type | action |
| Activity Audit | Download Resource | Timestamp | created_at |
| Activity Audit | Download Resource | Event ID | _document_id |
| Activity Audit | Download Resource | Event Code / Type | action |
| Activity Audit | Download Resource | Username | actor |
| Activity Audit | Download Resource | User ID | actor_id |
| Activity Audit | Download Resource | IP Address | actor_ip |
| Activity Audit | Download Resource | IP Geolocation / ASN | actor_location.country_code |
| Activity Audit | Download Resource | User Agent Name | user_agent |
| Activity Audit | Download Resource | Resource Name | repo |
| Activity Audit | Download Resource | Resource Type | action |

## Example logs

| Category | Event type | Log | Sample field values |
| -------- | ---------- | --- | ------------------- |
| Authentication | Account Login | [success](/products/github/event_examples/audit/authentication_account_login.json) | Timestamp=1685981286101; Event ID=mdvjC2kuRvXW_3Gkg7ni7Q; Event Code / Type=org.sso_response; Username=john.doe; User ID=12345678 |
| Authorization | Create Group | [success](/products/github/event_examples/audit/authorization_create_group_team.json) | Timestamp=1686001364120; Event ID=FLl6thHIizqa55S1P1tjIA; Event Code / Type=team.create; Username=john.doe; User ID=12345678 |
| Authorization | Update Group | [success](/products/github/event_examples/audit/authorization_update_group_team.json) | Timestamp=1694792374166; Event ID=JLMgkpYMkGmRiukmKjn4CQ; Event Code / Type=team.rename; Username=john.doe; User ID=12345678 |
| Authorization | Delete Group | [success](/products/github/event_examples/audit/authorization_delete_group_team.json) | Timestamp=1714145080936; Event ID=alg4QbCba1UhZA2VFJSTxQ; Event Code / Type=team.destroy; Username=john.doe; User ID=12345678 |
| Authorization | Add To Group | [success](/products/github/event_examples/audit/authorization_add_to_group_org.json) | Timestamp=1686151363489; Event ID=rLVAJb3ZtiugVygHs84Agw; Event Code / Type=org.add_member; Username=john.doe; User ID=12345678 |
| Authorization | Add To Group | [success](/products/github/event_examples/audit/authorization_add_to_group_repo.json) | Timestamp=1686159261336; Event ID=8s0hw2CW8Y44_rjiM9yNkw; Event Code / Type=repo.add_member; Username=john.doe; User ID=12345678 |
| Authorization | Add To Group | [success](/products/github/event_examples/audit/authorization_add_to_group_team.json) | Timestamp=1686096308885; Event ID=SwDxpQo4Gs5NMybfaD9mig; Event Code / Type=team.add_member; Username=john.doe; User ID=12345678 |
| Authorization | Remove From Group | [success](/products/github/event_examples/audit/authorization_remove_from_group_org.json) | Timestamp=1685999458723; Event ID=7IscVOcqIFzcj5OSXLDtig; Event Code / Type=org.remove_member; Username=john.doe; User ID=12345678 |
| Authorization | Remove From Group | [success](/products/github/event_examples/audit/authorization_remove_from_group_repo.json) | Timestamp=1686096006218; Event ID=Pm9_xkuRvV-rrHd2Tjk0Tw; Event Code / Type=repo.remove_member; Username=john.doe; User ID=12345678 |
| Authorization | Remove From Group | [success](/products/github/event_examples/audit/authorization_remove_from_group_team.json) | Timestamp=1685998981304; Event ID=XQwkRXOV8tJYCbbgk9d6TQ; Event Code / Type=team.remove_member; Username=john.doe; User ID=12345678 |
| Authorization | Add Permission | [success](/products/github/event_examples/audit/authorization_add_permission_team.json) | Timestamp=1686215687636; Event ID=TrmGicxMRvbKCHwf3vmJdD; Event Code / Type=team.update_repository_permission; Username=john.doe; User ID=12345678 |
| Authorization | Remove Permission | [success](/products/github/event_examples/audit/authorization_remove_permission_team.json) | Timestamp=1686215687636; Event ID=TrmGicxMRvbKCHwb3vmJdQ; Event Code / Type=team.update_repository_permission; Username=john.doe; User ID=12345678 |
| System Audit | Create Security Configuration | [success](/products/github/event_examples/audit/system_audit_create_security_configuration_forking.json) | Timestamp=1686011086644; Event ID=RxxlJ0MRNMQR8olkdIgPvQ; Event Code / Type=private_repository_forking.enable; Username=john.doe; User ID=12345678 |
| System Audit | Update Security Configuration | [success](/products/github/event_examples/audit/system_audit_update_security_configuration_hook_config.json) | Timestamp=1686158250381; Event ID=_I3yfAxtGRuNaaiuffqtvA; Event Code / Type=hook.config_changed; Username=john.doe; User ID=12345678 |
| System Audit | Update Security Configuration | [success](/products/github/event_examples/audit/system_audit_update_security_configuration_merge_setting.json) | Timestamp=1686246022669; Event ID=Ko2tnAiduqWy3KZSsh1nGA; Event Code / Type=repo.change_merge_setting; Username=john.doe; User ID=12345678 |
| System Audit | Create Integration | [success](/products/github/event_examples/audit/system_audit_create_integration.json) | Timestamp=1686093901098; Event ID=-hMpj-RFDXOlc43Zf9woMw; Event Code / Type=integration.create; Username=john.doe; User ID=12345678 |
| System Audit | Delete Integration | [success](/products/github/event_examples/audit/system_audit_delete_integration.json) | Timestamp=1689093550092; Event ID=IrAm5tty1DHWLJG7uRCusA; Event Code / Type=integration.destroy; Username=john.doe; User ID=12345678 |
| Activity Audit | Create Resource | [success](/products/github/event_examples/audit/activity_audit_create_resource_hook.json) | Timestamp=1686078595170; Event ID=sMyjmd8KUm6uTtRwQJ1hsw; Event Code / Type=hook.create; Username=john.doe; User ID=12345678 |
| Activity Audit | Create Resource | [success](/products/github/event_examples/audit/activity_audit_create_resource_pull_request.json) | Timestamp=1686078898897; Event ID=Dn-NJGInb1qGinKSmx-Hhg; Event Code / Type=pull_request.create; Username=john.doe; User ID=12345678 |
| Activity Audit | Create Resource | [success](/products/github/event_examples/audit/activity_audit_create_resource_pull_request_review.json) | Timestamp=1686163479794; Event ID=HxMMNJg2Ek8AJoNUGZ_6Yw; Event Code / Type=pull_request_review.submit; Username=john.doe; User ID=12345678 |
| Activity Audit | Create Resource | [success](/products/github/event_examples/audit/activity_audit_create_resource_pull_request_review_comment.json) | Timestamp=1686079082576; Event ID=GohZoGvnLxIsTepkIgnPuA; Event Code / Type=pull_request_review_comment.create; Username=john.doe; User ID=12345678 |
| Activity Audit | Create Resource | [success](/products/github/event_examples/audit/activity_audit_create_resource_repo.json) | Timestamp=1686077942218; Event ID=Mgash4pqBYVy5lV3xeohLg; Event Code / Type=repo.create; Username=john.doe; User ID=12345678 |
| Activity Audit | Create Resource | [success](/products/github/event_examples/audit/activity_audit_create_resource_secret.json) | Timestamp=1685772210579; Event ID=CyTAhfqvaaz5kqONoaJ1hg; Event Code / Type=repo.create_actions_secret; Username=john.doe; User ID=12345678 |
| Activity Audit | Create Resource | [success](/products/github/event_examples/audit/activity_audit_create_resource_workflow.json) | Timestamp=1686078701893; Event ID=RDSIX6X7F8WlXCkyaBqtOA; Event Code / Type=workflows.created_workflow_run; Username=john.doe; User ID=12345678 |
| Activity Audit | Update Resource | [success](/products/github/event_examples/audit/activity_audit_update_resource_pull_request.json) | Timestamp=1686141043334; Event ID=1Ed3MPt5rEKAbpW-k9jKVQ; Event Code / Type=pull_request.create_review_request; Username=john.doe; User ID=12345678 |
| Activity Audit | Update Resource | [success](/products/github/event_examples/audit/activity_audit_update_resource_pull_request_review_comment.json) | Timestamp=1686134016077; Event ID=rRDqrkWAyr4etNHVBN2MdQ; Event Code / Type=pull_request_review_comment.update; Username=john.doe; User ID=12345678 |
| Activity Audit | Update Resource | [success](/products/github/event_examples/audit/activity_audit_update_resource_repo.json) | Timestamp=1686092778658; Event ID=ySsAv7blcNhEhRvlw2cnbQ; Event Code / Type=repo.rename; Username=john.doe; User ID=12345678 |
| Activity Audit | Delete Resource | [success](/products/github/event_examples/audit/activity_audit_delete_resource_hook.json) | Timestamp=1686089206322; Event ID=4qrOaf_n_cB0BEUfoTXeyw; Event Code / Type=hook.destroy; Username=john.doe; User ID=12345678 |
| Activity Audit | Delete Resource | [success](/products/github/event_examples/audit/activity_audit_delete_resource_pull_request_review.json) | Timestamp=1686092779312; Event ID=2AAQbnEVxg_qkh4S5XcQDg; Event Code / Type=pull_request_review.delete; Username=john.doe; User ID=12345678 |
| Activity Audit | Delete Resource | [success](/products/github/event_examples/audit/activity_audit_delete_resource_pull_request_review_comment.json) | Timestamp=1686093347760; Event ID=4cV9xbCwSP5t5IT1TXEY1A; Event Code / Type=pull_request_review_comment.delete; Username=john.doe; User ID=12345678 |
| Activity Audit | Delete Resource | [success](/products/github/event_examples/audit/activity_audit_delete_resource_repo.json) | Timestamp=1686163467515; Event ID=1V2e_uoTEqkgh4EIgIq28g; Event Code / Type=repo.destroy; Username=john.doe; User ID=12345678 |
| Activity Audit | Download Resource | [success](/products/github/event_examples/audit/activity_audit_download_resource_repo.json) | Timestamp=1686153022502; Event ID=TaE7QBpn7eLwzy62M2_I8g; Event Code / Type=repo.download_zip; Username=john.doe; User ID=12345678 |


