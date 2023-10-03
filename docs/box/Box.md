# Box (0.0.1)

Box is a cloud-based content management and file sharing service. It's designed to help organizations store, manage, and collaborate on files and documents.

The Box Events API provides an event feed for enterprise events that have been generated within Box across the enterprise.

Depending on the specified stream_type, the Events API can provide real-time monitoring or historical querying of events.

The admin_logs_streaming stream type provides low latency, real-time access to events as they are processed by Box. Only two weeks of events are available via this stream type.

The admin_logs stream type emphasizes completeness over latency, and provides access to events up to one year.

## Collections

## Get Enterprise Events (enterprise_events) Collection

To collect enterprise events, make a call to the /events API and specify the desired stream_type.

### Events API Documentation (get_enterprise_events) Reference

Events API documentationURL Reference: [https://developer.box.com/guides/events/enterprise-events/for-enterprise/](https://developer.box.com/guides/events/enterprise-events/for-enterprise/)
### Event Stream Types (stream_types) Reference

Event Stream TeamsURL Reference: [https://developer.box.com/guides/events/parameters/stream-types/](https://developer.box.com/guides/events/parameters/stream-types/)
