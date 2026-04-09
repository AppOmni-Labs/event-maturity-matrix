# AppOmni (1.0.0)

AppOmni is a cloud-based platform designed to help organizations assess, monitor, and protect their data and configurations within SaaS applications.

AppOmni audit logs are collected via the *auditlogs* API, and can be streamed to a Threat Detection event sink.

Historical audit logs are also stored for 180 days and can be accessed via the scheduled reports feature.

There are currently minor formatting differences between API/Event Sink logs, and the logs retrieved via scheduled reports.

## Collections

## Audit Logs API (audit_logs_api) Collection

To collect events, make a call to the /core/auditlogs endpoint and specify the desired parameters.

### Audit Logs API Documentation (auditlogs_api_documentation) Reference

Audit Logs API Documentation.URL Reference: [https://appomni.com/](https://appomni.com/)


## Event Sink Streaming (event_sink) Collection

Audit logs are delivered to all Threat Detection event sinks.

### Event Sink Documentation (event_sink_documentation) Reference

Threat Detection Event Sink DocumentationURL Reference: [https://appomni.com/](https://appomni.com/)


## Scheduled Reports (scheduled_reports) Collection

Create a scheduled report of type "AppOmni Audit Logs" to download audit logs.

### Scheduled Reports (scheduled_reports_documentation) Reference

Scheduled Reports Event Sink DocumentationURL Reference: [https://appomni.com/](https://appomni.com/)
