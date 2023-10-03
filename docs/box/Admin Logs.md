# Box - Admin Logs (0.0.1)

> Entity Name: event_source

Box enterprise logs that provide an audit trail of user activity.

## References
* [Enterprise Event Schema](https://developer.box.com/reference/resources/event/)

## Retention

Based on our research, Box retains audit logs for 365 Days.


### Comments
Based on the admin_logs stream type.


## Latency

Based on our research, Box has a latency of Near Real-Time.

### Comments
N/A


## Licensing

Included with Box Business Plus and above.

## Mappings

| Category | Event Type | Attributes | Examples |
| -------- | ---------- | ---------- | -------- |
| C0001 | ET0001 |A0001 -> created_at<br />A0002 -> event_id<br />A0003 -> event_type<br />A0004 -> event_type<br />A0005 -> source.login<br />A0006 -> source.id<br />A0008 -> session_id<br />A0009 -> ip_address<br />|[success](/products/box/event_examples/authentication_account_login_success.json)<br />[failure](/products/box/event_examples/authentication_account_login_failure.json)<br />|
| C0002 | ET0004 |A0001 -> created_at<br />A0002 -> event_id<br />A0003 -> event_type<br />A0005 -> created_by.login<br />A0006 -> created_by.id<br />A0008 -> session_id<br />A0009 -> ip_address<br />A0019 -> source.login<br />|[create](/products/box/event_examples/authorization_create_user.json)<br />|
| C0002 | ET0006 |A0001 -> created_at<br />A0002 -> event_id<br />A0003 -> event_type<br />A0005 -> created_by.login<br />A0006 -> created_by.id<br />A0008 -> session_id<br />A0009 -> ip_address<br />A0019 -> source.login<br />|[update](/products/box/event_examples/authorization_update_user.json)<br />|
| C0002 | ET0007 |A0001 -> created_at<br />A0002 -> event_id<br />A0003 -> event_type<br />A0005 -> created_by.login<br />A0006 -> created_by.id<br />A0008 -> session_id<br />A0009 -> ip_address<br />A0019 -> source.login<br />|[delete](/products/box/event_examples/authorization_delete_user.json)<br />|
| C0002 | ET0008 |A0001 -> created_at<br />A0002 -> event_id<br />A0003 -> event_type<br />A0005 -> created_by.login<br />A0006 -> created_by.id<br />A0008 -> session_id<br />A0009 -> ip_address<br />A0021 -> source.group_name<br />|[create](/products/box/event_examples/authorization_create_group.json)<br />|
| C0002 | ET0010 |A0001 -> created_at<br />A0002 -> event_id<br />A0003 -> event_type<br />A0005 -> created_by.login<br />A0006 -> created_by.id<br />A0008 -> session_id<br />A0009 -> ip_address<br />A0021 -> source.group_name<br />|[update](/products/box/event_examples/authorization_update_group.json)<br />|
| C0002 | ET0011 |A0001 -> created_at<br />A0002 -> event_id<br />A0003 -> event_type<br />A0005 -> created_by.login<br />A0006 -> created_by.id<br />A0008 -> session_id<br />A0009 -> ip_address<br />A0021 -> source.group_name<br />|[delete](/products/box/event_examples/authorization_delete_group.json)<br />|
| C0002 | ET0012 |A0001 -> created_at<br />A0002 -> event_id<br />A0003 -> event_type<br />A0005 -> created_by.login<br />A0006 -> created_by.id<br />A0008 -> session_id<br />A0009 -> ip_address<br />A0021 -> additional_details.group_name<br />A0019 -> source.login<br />|[add](/products/box/event_examples/authorization_add_to_group.json)<br />|
| C0002 | ET0013 |A0001 -> created_at<br />A0002 -> event_id<br />A0003 -> event_type<br />A0005 -> created_by.login<br />A0006 -> created_by.id<br />A0008 -> session_id<br />A0009 -> ip_address<br />A0021 -> additional_details.group_name<br />A0019 -> source.login<br />|[remove](/products/box/event_examples/authorization_remove_from_group.json)<br />|
| C0002 | ET0018 |A0001 -> created_at<br />A0002 -> event_id<br />A0003 -> event_type<br />A0005 -> created_by.login<br />A0006 -> created_by.id<br />A0008 -> session_id<br />A0009 -> ip_address<br />A0023 -> additional_details.role<br />A0024 -> source.file_name<br />|[add](/products/box/event_examples/authorization_add_permission.json)<br />|
| C0002 | ET0019 |A0001 -> created_at<br />A0002 -> event_id<br />A0003 -> event_type<br />A0005 -> created_by.login<br />A0006 -> created_by.id<br />A0008 -> session_id<br />A0009 -> ip_address<br />A0024 -> source.file_name<br />|[remove](/products/box/event_examples/authorization_remove_permission.json)<br />|
| C0002 | ET0020 |A0001 -> created_at<br />A0002 -> event_id<br />A0003 -> event_type<br />A0005 -> created_by.login<br />A0006 -> created_by.id<br />A0008 -> session_id<br />A0009 -> ip_address<br />A0019 -> source.login<br />|[add](/products/box/event_examples/authorization_add_enrollment.json)<br />|
| C0002 | ET0021 |A0001 -> created_at<br />A0002 -> event_id<br />A0003 -> event_type<br />A0005 -> created_by.login<br />A0006 -> created_by.id<br />A0008 -> session_id<br />A0009 -> ip_address<br />A0019 -> source.login<br />|[remove](/products/box/event_examples/authorization_remove_enrollment.json)<br />|
| C0004 | ET0030 |A0001 -> created_at<br />A0002 -> event_id<br />A0003 -> event_type<br />A0005 -> created_by.login<br />A0006 -> created_by.id<br />A0008 -> session_id<br />A0009 -> ip_address<br />A0030 -> source.item_name<br />A0031 -> source.item_type<br />|[create](/products/box/event_examples/activity_audit_create_resource.json)<br />|
| C0004 | ET0031 |A0001 -> created_at<br />A0002 -> event_id<br />A0003 -> event_type<br />A0005 -> created_by.login<br />A0006 -> created_by.id<br />A0008 -> session_id<br />A0009 -> ip_address<br />A0030 -> source.item_name<br />A0031 -> source.item_type<br />|[read](/products/box/event_examples/activity_audit_read_resource.json)<br />|
| C0004 | ET0032 |A0001 -> created_at<br />A0002 -> event_id<br />A0003 -> event_type<br />A0005 -> created_by.login<br />A0006 -> created_by.id<br />A0008 -> session_id<br />A0009 -> ip_address<br />A0030 -> source.item_name<br />A0031 -> source.item_type<br />|[update](/products/box/event_examples/activity_audit_update_resource.json)<br />|
| C0004 | ET0033 |A0001 -> created_at<br />A0002 -> event_id<br />A0003 -> event_type<br />A0005 -> created_by.login<br />A0006 -> created_by.id<br />A0008 -> session_id<br />A0009 -> ip_address<br />A0030 -> source.item_name<br />A0031 -> source.item_type<br />|[delete](/products/box/event_examples/activity_audit_delete_resource.json)<br />|
| C0004 | ET0034 |A0001 -> created_at<br />A0002 -> event_id<br />A0003 -> event_type<br />A0005 -> created_by.login<br />A0006 -> created_by.id<br />A0008 -> session_id<br />A0009 -> ip_address<br />A0032 -> additional_details.size<br />A0030 -> source.item_name<br />A0031 -> source.item_type<br />|[download](/products/box/event_examples/activity_audit_download_resource.json)<br />|


