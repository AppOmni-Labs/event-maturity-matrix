# Salesforce - SetupAuditTrail (0.0.1)

> Entity Name: event_source

The SetupAuditTrail object provides an audit trail of changes to user profiles, permission sets, security settings, custom objects, and other settings.

## References
* [SetupAuditTrail](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_setupaudittrail.htm)

## Retention

Based on our research, Salesforce retains audit logs for 180 Days.


### Comments
N/A


## Latency

Based on our research, Salesforce has a latency of Real-Time.

### Comments
N/A


## Licensing

Free

## Mappings

| Category | Event Type | Attributes | Examples |
| -------- | ---------- | ---------- | -------- |
| C0002 | ET0004 |A0001 -> sfdc_created_date<br />A0002 -> record_id<br />A0003 -> action<br />A0005 -> sfdc_created_by_username<br />A0006 -> sfdc_created_by_id<br />|[create](/products/salesforce/event_examples/authorization_create_user.json)<br />|
| C0002 | ET0006 |A0001 -> sfdc_created_date<br />A0002 -> record_id<br />A0003 -> action<br />A0005 -> sfdc_created_by_username<br />A0006 -> sfdc_created_by_id<br />A0020 -> display<br />|[update](/products/salesforce/event_examples/authorization_update_user.json)<br />|
| C0002 | ET0008 |A0001 -> sfdc_created_date<br />A0002 -> record_id<br />A0003 -> action<br />A0005 -> sfdc_created_by_username<br />A0006 -> sfdc_created_by_id<br />A0021 -> display<br />|[create](/products/salesforce/event_examples/authorization_create_group.json)<br />|
| C0002 | ET0010 |A0001 -> sfdc_created_date<br />A0002 -> record_id<br />A0003 -> action<br />A0005 -> sfdc_created_by_username<br />A0006 -> sfdc_created_by_id<br />A0021 -> display<br />A0020 -> display<br />|[update](/products/salesforce/event_examples/authorization_update_group.json)<br />|
| C0002 | ET0011 |A0001 -> sfdc_created_date<br />A0002 -> record_id<br />A0003 -> action<br />A0005 -> sfdc_created_by_username<br />A0006 -> sfdc_created_by_id<br />A0021 -> display<br />|[delete](/products/salesforce/event_examples/authorization_delete_group.json)<br />|
| C0002 | ET0012 |A0001 -> sfdc_created_date<br />A0002 -> record_id<br />A0003 -> action<br />A0005 -> sfdc_created_by_username<br />A0006 -> sfdc_created_by_id<br />A0021 -> display<br />|[add](/products/salesforce/event_examples/authorization_add_to_group.json)<br />|
| C0002 | ET0013 |A0001 -> sfdc_created_date<br />A0002 -> record_id<br />A0003 -> action<br />A0005 -> sfdc_created_by_username<br />A0006 -> sfdc_created_by_id<br />A0021 -> display<br />|[remove](/products/salesforce/event_examples/authorization_remove_fom_group.json)<br />|
| C0002 | ET0014 |A0001 -> sfdc_created_date<br />A0002 -> record_id<br />A0003 -> action<br />A0005 -> sfdc_created_by_username<br />A0006 -> sfdc_created_by_id<br />A0022 -> display<br />|[create](/products/salesforce/event_examples/authorization_create_role.json)<br />|
| C0002 | ET0016 |A0001 -> sfdc_created_date<br />A0002 -> record_id<br />A0003 -> action<br />A0005 -> sfdc_created_by_username<br />A0006 -> sfdc_created_by_id<br />A0022 -> display<br />A0020 -> display<br />|[update](/products/salesforce/event_examples/authorization_update_role.json)<br />|
| C0002 | ET0017 |A0001 -> sfdc_created_date<br />A0002 -> record_id<br />A0003 -> action<br />A0005 -> sfdc_created_by_username<br />A0006 -> sfdc_created_by_id<br />A0022 -> display<br />||
| C0002 | ET0018 |A0001 -> sfdc_created_date<br />A0002 -> record_id<br />A0003 -> action<br />A0005 -> sfdc_created_by_username<br />A0006 -> sfdc_created_by_id<br />A0023 -> display<br />A0024 -> display<br />|[add](/products/salesforce/event_examples/authorization_add_permission.json)<br />|
| C0002 | ET0019 |A0001 -> sfdc_created_date<br />A0002 -> record_id<br />A0003 -> action<br />A0005 -> sfdc_created_by_username<br />A0006 -> sfdc_created_by_id<br />A0023 -> display<br />A0024 -> display<br />|[remove](/products/salesforce/event_examples/authorization_remove_permission.json)<br />|
| C0002 | ET0020 |A0001 -> sfdc_created_date<br />A0002 -> record_id<br />A0003 -> action<br />A0005 -> sfdc_created_by_username<br />A0006 -> sfdc_created_by_id<br />A0025 -> display<br />A0019 -> display<br />|[add](/products/salesforce/event_examples/authorization_add_enrollment.json)<br />|
| C0002 | ET0021 |A0001 -> sfdc_created_date<br />A0002 -> record_id<br />A0003 -> action<br />A0005 -> sfdc_created_by_username<br />A0006 -> sfdc_created_by_id<br />A0025 -> display<br />A0019 -> display<br />|[remove](/products/salesforce/event_examples/authorization_remove_enrollment.json)<br />|
| C0003 | ET0022 |A0001 -> sfdc_created_date<br />A0002 -> record_id<br />A0003 -> action<br />A0005 -> sfdc_created_by_username<br />A0006 -> sfdc_created_by_id<br />A0026 -> display<br />|[create](/products/salesforce/event_examples/system_audit_create_configuration.json)<br />|
| C0003 | ET0024 |A0001 -> sfdc_created_date<br />A0002 -> record_id<br />A0003 -> action<br />A0005 -> sfdc_created_by_username<br />A0006 -> sfdc_created_by_id<br />A0026 -> display<br />|[update](/products/salesforce/event_examples/system_audit_update_configuration.json)<br />|
| C0003 | ET0025 |A0001 -> sfdc_created_date<br />A0002 -> record_id<br />A0003 -> action<br />A0005 -> sfdc_created_by_username<br />A0006 -> sfdc_created_by_id<br />A0026 -> display<br />|[delete](/products/salesforce/event_examples/system_audit_delete_configuration.json)<br />|
| C0003 | ET0026 |A0001 -> sfdc_created_date<br />A0002 -> record_id<br />A0003 -> action<br />A0005 -> sfdc_created_by_username<br />A0006 -> sfdc_created_by_id<br />A0029 -> display<br />|[create](/products/salesforce/event_examples/system_audit_create_integration.json)<br />|
| C0003 | ET0028 |A0001 -> sfdc_created_date<br />A0002 -> record_id<br />A0003 -> action<br />A0005 -> sfdc_created_by_username<br />A0006 -> sfdc_created_by_id<br />A0029 -> display<br />|[update](/products/salesforce/event_examples/system_audit_update_integration.json)<br />|
| C0003 | ET0029 |A0001 -> sfdc_created_date<br />A0002 -> record_id<br />A0003 -> action<br />A0005 -> sfdc_created_by_username<br />A0006 -> sfdc_created_by_id<br />A0029 -> display<br />|[delete](/products/salesforce/event_examples/system_audit_delete_integration.json)<br />|


