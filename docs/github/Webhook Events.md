# GitHub — Webhook Events

📌 **v1.0.0** · 🗄 **Retention:** N/A · ⚡ **Latency:** Near Real-Time

🗄 GitHub does not officially retain webhook events. Recent webhook events can be accessed at `https://github.com/<ORGANIZATION>/<REPOSITORY>/settings/hooks`.


⚡ N/A


📜 **Licensing:** Included with all GitHub accounts.


GitHub webhook events are delivered whenever certain events occur on GitHub.
## References
* [Webhook Event Schema](https://docs.github.com/en/webhooks-and-events/webhooks/webhook-events-and-payloads)
## Field mappings

| Category | Event type | Attribute | Source field(s) |
| -------- | ---------- | --------- | ---------------- |
| Authorization | Update User | Event Code / Type | action |
| Authorization | Update User | Username | sender.login |
| Authorization | Update User | User ID | sender.id |
| Authorization | Update User | User Type / Role | sender.type |
| Authorization | Update User | Target Username | member.login |
| Authorization | Update User | Target Attribute Context | changes |
| Authorization | Create Group | Event Code / Type | action |
| Authorization | Create Group | Username | sender.login |
| Authorization | Create Group | User ID | sender.id |
| Authorization | Create Group | User Type / Role | sender.type |
| Authorization | Create Group | Target Group Name | organization.login, team.name, repository.name |
| Authorization | Update Group | Event Code / Type | action |
| Authorization | Update Group | Username | sender.login |
| Authorization | Update Group | User ID | sender.id |
| Authorization | Update Group | User Type / Role | sender.type |
| Authorization | Update Group | Target Attribute Context | changes |
| Authorization | Update Group | Target Group Name | organization.login, team.name, repository.name |
| Authorization | Delete Group | Event Code / Type | action |
| Authorization | Delete Group | Username | sender.login |
| Authorization | Delete Group | User ID | sender.id |
| Authorization | Delete Group | User Type / Role | sender.type |
| Authorization | Delete Group | Target Group Name | organization.login, team.name, repository.name |
| Authorization | Add To Group | Event Code / Type | action |
| Authorization | Add To Group | Username | sender.login |
| Authorization | Add To Group | User ID | sender.id |
| Authorization | Add To Group | User Type / Role | sender.type |
| Authorization | Add To Group | Target Username | membership.user.login |
| Authorization | Add To Group | Target Group Name | organization.login, team.name, repository.name |
| Authorization | Remove From Group | Event Code / Type | action |
| Authorization | Remove From Group | Username | sender.login |
| Authorization | Remove From Group | User ID | sender.id |
| Authorization | Remove From Group | User Type / Role | sender.type |
| Authorization | Remove From Group | Target Username | membership.user.login |
| Authorization | Remove From Group | Target Group Name | organization.login, team.name, repository.name |
| Activity Audit | Create Resource | Event Code / Type | action |
| Activity Audit | Create Resource | Username | sender.login |
| Activity Audit | Create Resource | User ID | sender.id |
| Activity Audit | Create Resource | User Type / Role | sender.type |
| Activity Audit | Create Resource | Resource Name | repository.name |
| Activity Audit | Create Resource | Resource Type | X-GitHub-Event |
| Activity Audit | Delete Resource | Event Code / Type | action |
| Activity Audit | Delete Resource | Username | sender.login |
| Activity Audit | Delete Resource | User ID | sender.id |
| Activity Audit | Delete Resource | User Type / Role | sender.type |
| Activity Audit | Delete Resource | Resource Name | repository.name |
| Activity Audit | Delete Resource | Resource Type | X-GitHub-Event |

## Example logs

| Category | Event type | Log | Sample field values |
| -------- | ---------- | --- | ------------------- |
| Authorization | Update User | [success](/products/github/event_examples/webhook/authorization_update_user.json) | Event Code / Type=edited; Username=acme-bot; User ID=124079944; User Type / Role=User; Target Username=john.doe |
| Authorization | Create Group | [success](/products/github/event_examples/webhook/authorization_create_group.json) | Event Code / Type=created; Username=john.doe; User ID=64659356; User Type / Role=User; Target Group Name=acme-inc |
| Authorization | Update Group | [success](/products/github/event_examples/webhook/authorization_update_group.json) | Event Code / Type=edited; Username=john.doe; User ID=114508655; User Type / Role=User; Target Attribute Context={'description': {'from': 'Acme devs'}} |
| Authorization | Delete Group | [success](/products/github/event_examples/webhook/authorization_delete_group.json) | Event Code / Type=deleted; Username=john.doe; User ID=74208074; User Type / Role=User; Target Group Name=acme-inc |
| Authorization | Add To Group | [success](/products/github/event_examples/webhook/authorization_add_to_group.json) | Event Code / Type=member_added; Username=gh-automate; User ID=92325258; User Type / Role=User; Target Username=john.doe |
| Authorization | Remove From Group | [success](/products/github/event_examples/webhook/authorization_remove_from_group.json) | Event Code / Type=member_removed; Username=gh-automate; User ID=92325258; User Type / Role=User; Target Username=john.doe |
| Activity Audit | Create Resource | [success](/products/github/event_examples/webhook/activity_audit_create_resource_repo.json) | Event Code / Type=created; Username=john.doe; User ID=126112697; User Type / Role=User; Resource Name=sample-repo |
| Activity Audit | Delete Resource | [success](/products/github/event_examples/webhook/activity_audit_delete_resource_repo.json) | Event Code / Type=deleted; Username=john.doe; User ID=19332128; User Type / Role=User; Resource Name=sample-repo |


