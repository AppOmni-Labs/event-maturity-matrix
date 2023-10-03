# GitHub - Webhook Events (0.0.1)

> Entity Name: event_source

GitHub webhook events are delivered whenever certain events occur on GitHub.

## References
* [Webhook Event Schema](https://docs.github.com/en/webhooks-and-events/webhooks/webhook-events-and-payloads)

## Retention

Based on our research, GitHub retains audit logs for N/A.


### Comments
GitHub does not officially retain webhook events. Recent webhook events can be accessed at `https://github.com/<ORGANIZATION>/<REPOSITORY>/settings/hooks`.


## Latency

Based on our research, GitHub has a latency of Near Real-Time.

### Comments
N/A


## Licensing

Included with all GitHub accounts.

## Mappings

| Category | Event Type | Attributes | Examples |
| -------- | ---------- | ---------- | -------- |
| C0002 | ET0006 |A0003 -> action<br />A0005 -> sender.login<br />A0006 -> sender.id<br />A0007 -> sender.type<br />A0019 -> member.login<br />A0020 -> changes<br />|[success](/products/github/event_examples/webhook/authorization_update_user.json)<br />|
| C0002 | ET0008 |A0003 -> action<br />A0005 -> sender.login<br />A0006 -> sender.id<br />A0007 -> sender.type<br />A0021 -> ['organization.login', 'team.name', 'repository.name']<br />|[success](/products/github/event_examples/webhook/authorization_create_group.json)<br />|
| C0002 | ET0010 |A0003 -> action<br />A0005 -> sender.login<br />A0006 -> sender.id<br />A0007 -> sender.type<br />A0020 -> changes<br />A0021 -> ['organization.login', 'team.name', 'repository.name']<br />|[success](/products/github/event_examples/webhook/authorization_update_group.json)<br />|
| C0002 | ET0011 |A0003 -> action<br />A0005 -> sender.login<br />A0006 -> sender.id<br />A0007 -> sender.type<br />A0021 -> ['organization.login', 'team.name', 'repository.name']<br />|[success](/products/github/event_examples/webhook/authorization_delete_group.json)<br />|
| C0002 | ET0012 |A0003 -> action<br />A0005 -> sender.login<br />A0006 -> sender.id<br />A0007 -> sender.type<br />A0019 -> membership.user.login<br />A0021 -> ['organization.login', 'team.name', 'repository.name']<br />|[success](/products/github/event_examples/webhook/authorization_add_to_group.json)<br />|
| C0002 | ET0013 |A0003 -> action<br />A0005 -> sender.login<br />A0006 -> sender.id<br />A0007 -> sender.type<br />A0019 -> membership.user.login<br />A0021 -> ['organization.login', 'team.name', 'repository.name']<br />|[success](/products/github/event_examples/webhook/authorization_remove_from_group.json)<br />|
| C0004 | ET0030 |A0003 -> action<br />A0005 -> sender.login<br />A0006 -> sender.id<br />A0007 -> sender.type<br />A0030 -> repository.name<br />A0031 -> X-GitHub-Event<br />|[success](/products/github/event_examples/webhook/activity_audit_create_resource.json)<br />|
| C0004 | ET0033 |A0003 -> action<br />A0005 -> sender.login<br />A0006 -> sender.id<br />A0007 -> sender.type<br />A0030 -> repository.name<br />A0031 -> X-GitHub-Event<br />|[success](/products/github/event_examples/webhook/activity_audit_delete_resource.json)<br />|


