# Data Definition Reference

This document describes the individual data files within the Event Maturity Matrix framework in detail as well as how these files relate to each other.

> I will break down each file individually but please review the `notes` left within each section as these will contain pertinent information.

- [Data Definition Reference](#data-definition-reference)
  - [Overview](#overview)
  - [Framework Definitions / Data Files](#framework-definitions--data-files)
    - [Core Definitions](#core-definitions)
    - [Categories](#categories)
    - [Event Types](#event-types)
    - [Attributes](#attributes)
  - [Content Definitions](#content-definitions)
    - [Product](#product)
    - [Event Source](#event-source)
      - [Retention](#retention)
      - [Latency](#latency)
      - [Licensing](#licensing)
      - [Mappings](#mappings)

## Overview

EMM has two main `buckets` of data files within the EMM project. The first bucket being the [core definitions](#core-definitions) themselves and the second being the [content definitions](#content-definitions) mapped to our definitions.

> All of the data definitions within EMM are based on a JSONSchema document which you can find in the [schema](../schema/README.md) folder.

## Framework Definitions / Data Files

The EMM framework is made up of a few core definitions. These definitions are the core of the framework and are used to normalize data from our content definitions.

> **NOTE**: These core definitions within the framework aren't meant to be changed by the consumer in any way. 

### Core Definitions

Within each of our core definition files, a few fields must be present. These are:

```yaml
entity_name: categories # or attributes or event_types or product or event_source
description: |
  A general description of the entity
version: "0.0.1"
```

Depending on the entity, we may have additional fields but these are the base fields which must be present. 

Additionally, the available names for an entity are:

* categories
* attributes
* event_types
* product
* event_source

The sections below will explain each definition in detail and provide examples of each. 

> **NOTE**: Each core definition file contains a set of `items`. Each item represents the logical bucket of that entity's data definitions.

### Categories

| Data Definition                     |Schema|
|-------------------------------------|------|
| [categories.yml](../categories.yml) |[Schema](../schema/categories.yml)|

Categories represent the high-level categorization of different event types.

Each category within EMM will have a set of event types which are considered related to that category. This allows us to normalize and group similar event types into our normalized categories.

> If you are viewing the matrix itself, categories are the column headers.

Each category will be referenced by one or more event_types. Additionally, a category can be referenced as an `include` or `exclude` property value on a defined `attribute`.

Below is an example of a category definition:

> Each category must have a unique ID in the format of `C####` where `####` is a unique (sequential) number.

```yaml
id: C0002
name: Authorization
description: |
    This category contains events related to the management of or access of a specific service provider.

    You will often find User, Group and/or Role CRUD (create, read, update, delete, download, etc.) operations under the Authorization category.
```

### Event Types

| Data Definition                       |Schema|
|---------------------------------------|------|
| [event_types.yml](../event_types.yml) |[Schema](../schema/event_types.yml)|

Event types represent logical buckets of different types of events with in a SaaS service.

Event types are the core of the EMM framework. Each defined event type is unique but represents a normalized event type which can be mapped to a SaaS service.

> If you are viewing the matrix itself, event types are the individual cards under a category.

Each event type must be unique and must be associated with a category. Additionally, an event type can be referenced as an `include` or `exclude` property value on a defined `attribute`.

Below is an example of an event type definition:

For example, a single event_type item is defined as:

```yaml
- id: ET0001
  name: Account Login
  categories:
    - C0001
  description: An account attempted to login to a system.
```

When defining a new `event_type` you must have unique values for the `id`, `name` and `description` fields. Additionally, you must associate this event_type to a defined category. You can associate this event_type to more than one category but many times there is no need to do so.

### Attributes

| Data Definition                     |Schema|
|-------------------------------------|------|
| [attributes.yml](../attributes.yml) |[Schema](../schema/attributes.yml)|

Attributes represent the individual fields within an event. We've normalized these field names to allow for easier mapping of data from different SaaS services.

Each attribute must have a unique `id`, `name`, and `description`. Additionally, each attribute must have a `type` defined. The `type` field is used to define the data type of the attribute. The available types are:

* string
* integer
* boolean

> If you are viewing the matrix itself, attributes are the individual attributes/fields within an event type card.

By default, all defined attributes have a `include` field and this field defaults to `ALL`. **Even if it's not explicitly defined, just know that we consider this the default.**

In the example below we define an attribute with an `id`, `name`, `description`, `type` and one or more `examples`.

```yaml
- id: A0001
  name: Timestamp
  description: The timestamp of when the event first occurred.
  type: string
  examples:
    - "2022-11-17T06:34:18.429Z"
```

Additionally, you can `include` or `exclude` event_types or categories.

Here is an example of attribute `A0019 - Target Username` excluding itself from a list of event types.
Also this attribute is only defined for event_types which are associated with the category `C0002 - Authorization`.

```yaml
- id: A0019
  name: Target Username
  include:
    - C0002
  exclude:
    - ET0008
    - ET0009
    - ET0010
    - ET0011
    - ET0014
    - ET0015
    - ET0016
    - ET0017
    - ET0018
    - ET0019
    - ET0020
  description: The target username of activity within a service provider.
  type: string
  examples:
    - first.lastname
    - first.lastname@company.com
```

## Content Definitions

Content definitions within EMM describe the data which is logged by a specific SaaS service. These definitions are used to map the data from a SaaS service to our core definitions.
Within EMM we consider content definitions to be the external data which we're representing using our core data definitions (above). 

EMM has two main types of content definitions. These are:

* product - A product definition describes a specific SaaS service, available collection details and more. 
* event_source - An event_source definition describes a specific collection method for a SaaS service. For example, a SaaS service may have multiple REST APIs as a collection method. Each of these would be defined as an event_source.

Each event_source must have an associated `product` definition. It's also important to understand that each event_source defines a series of `mappings` that explain what that specific event_source can and will log.

> **NOTE**: You can find more about [contributing](../CONTRIBUTING.md) to EMM in the contributing guide.

### Product

| Data Definition                                 |Schema|
|-------------------------------------------------|------|
| [template.product.yml](../template.product.yml) |[Schema](../schema/product.yml)|

A product describes a specific SaaS service, available collection details and more. 

The product content definition is defined similarly to the other definitions which requires:

```yaml
entity_name: product
version: "0.0.1"
name: Salesforce
  Salesforce audit logs are collected via objects, namely the SetupAuditTrail object, EventLogFile object, or Real-Time Event Monitoring objects. These objects are accessible via the Salesforce API.
  
  Salesforce supports a wide range of APIs, however with regards to audit logs, the primary APIs include the REST API, SOAP API, or Streaming API. 
  
  The REST API and SOAP API can be used to access the EventLogFile and SetupAuditTrail objects, which contains log files for the Setup Audit Trail and Event Monitoring. 
  
  The Streaming API can be used to access the Real-Time Event Monitoring objects, which contains log files for Real-Time Event Monitoring.

  The Setup Audit Trail logs all setup changes made by administrators, providing an audit trail of changes to user profiles, permission sets, security settings, custom objects, and other settings.

  Event Monitoring logs user activity and stores this data in log files for analysis. Over 50 different Event Types are available and provide detailed information about user activity such as login attempts, API calls, report exports, and record modifications. 
  
  Real-time Event Monitoring also logs user activity, however this data is available in real-time as the activity occurs within the system. Over 20 different real-time Monitoring Objects are available and provide detailed information about user activity.
```

> Please note that the name of the `product` must match the `product.name` value in each event_source.

Each product will define one or more `collections` in our content definition. Here is an example of a collection data structure within a product definition:

```yaml
collection:
  - id: rest_api
    name: REST API
    description: A REST interface that can be used to access Salesforce data without using the Salesforce user interface
    references:
      - id: rest_api_documentation
        name: REST API Documentation
        description: REST API documentation
        url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_what_is_rest_api.htm
      - id: rest_api_event_monitoring_documentation
        name: Event Monitoring and REST API Documentation
        description: Using the REST API to access the EventLogFile Object
        url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/using_resources_event_log_files.htm
  - id: soap_api
    name: SOAP API
    description: An interface that can be used to access Salesforce data using the SOAP protocol
    references:
      - id: soap_api_documentation
        name: SOAP API Documentation
        description: SOAP API documentation
        url: https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_quickstart_intro.htm
  - id: streaming_api
    name: Streaming API
    description: An API that provides a subscription mechanism for receiving events in near real-time
    references:
      - id: streaming_api_documentation
        name: Streaming API Documentation
        url: https://developer.salesforce.com/docs/atlas.en-us.api_streaming.meta/api_streaming/intro_stream.htm
      - id: streaming_api_event_monitoring_objects
        name: Real-Time Event Monitoring Objects
        description: Using the Streaming API to access Real-Time Event Monitoring Objects
        url: https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_events_objects_monitoring.htm
```

The `collection` key takes an array of properties which define each collection point, including references and other information.

|Property Name|Value Type|Value Options|Description| Notes                                                                             |
|-------------|----------|-------------|-----------|-----------------------------------------------------------------------------------|
|id|string|N/A|A unique id for this collection.| This unique_id is referenced in event_sources under `product.collection_sources`. |
|name|string|N/A|The name of the collection| This should be unique as well.                                                    |
|description|string|N/A|A description which explains the data collection source.|                                                                                   |
|references|List[str]|N/A|A list of references| Each reference has a unique_id, name, description and a URL to the reference.     |

> It's okay if a reference link is behind a paywall but please try to find an open Uri if possible.

### Event Source

| Data Definition                                           |Schema|
|-----------------------------------------------------------|------|
| [template.event_source.yml](../template.event_source.yml) |[Schema](../schema/event_source.yml)|

Each event_source uniquely describes the event collection source used to detect threats. Each event_source itself has a relationship to a product but also describes the collection method, retention, latency, licensing and more. Each event_source (should) also have one or more mappings which describe the data which is collected by the event_source. These mappings map EMM attribute fields to the actual data fields within the event_source.

Below is an example event_source for [Salesforce EventLogFile Login Event](../products/salesforce/event_sources/elf_login_event.yml) which we will use as an example to explain the structure of an event_source data content definition file.

```yaml
entity_name: event_source
version: "0.0.1"
product: 
  name: Salesforce
  collection_sources:
    - rest_api
    - soap_api
name: EventLogFile Login Event
description: This event source is to track login events in Salesforce.
references:
  - id: login_event
    name: EventLogFile Login Event
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_eventlogfile_login.htm
retention:
  duration: 1 Day
  comments: Available for free with 1 day retention, otherwise requires an add-on subscription for 30 day retention.
latency:
  duration: 3 Hours
  comments: Event log files are accessible via hourly and 24 hour log files. It can take between 3–6 hours from the time of the event to be available in the hourly log file.
licensing:
  comments: Available for free with 1 day retention, otherwise requires Salesforce Shield or a Salesforce Event Monitoring add-on subscription.
mappings:
  - category: C0001
    event_type: ET0001
    attributes:
      A0001: TIMESTAMP_DERIVED
      A0003: EVENT_TYPE
      A0004: LOGIN_STATUS
      A0005: USER_NAME 
      A0006: USER_ID
      A0007: USER_TYPE
      A0008: LOGIN_KEY
      A0009: SOURCE_IP
      A0011: BROWSER_TYPE
      A0013: LOGIN_STATUS
      A0014: LOGIN_TYPE
      A0015: AUTHENTICATION_METHOD_REFERENCE
    examples: 
      - type: success
        location: "./event_examples/authentication_account_login_elf.json"
```

Each event_source should define the following root values:

```yaml
entity_name: event_source
version: "0.0.1"
product: 
  name: Salesforce
  collection_sources:
    - rest_api
    - soap_api
name: EventLogFile Login Event
description: This event source is to track login events in Salesforce.
```

> The name of the product must match what's defined in the `{name}.product.yml` file for said product.

You must define the same core pieces of data like `entity_name`, `version`, `name`, and `description` but you must also define the associated `product`. This definition has two properties `name` and `collection_sources`. The `product.name` property must match the name of the product and the `collection_sources` property takes a list of `collection` IDs from the `{product.name}.product.yml` definition.

An event_source can also define one or more references. These references are meant to provide additional information about the event_source which helps describe event collection, retention, latency, licensing and more. These references are optional but are highly encouraged.

You can provide one or more references using this format:

```yaml
references:
  - id: login_event
    name: EventLogFile Login Event
    url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_eventlogfile_login.htm
# You can add more by uncommenting the below section
#   - id: login_event
#     name: EventLogFile Login Event
#     url: https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_eventlogfile_login.htm
```

Each event_source defines a series of specific information as it relates to detection engineering, operations, and security in general. These properties allow us to better understand the capabilities of an event_source as well as it's usability within the context of your product.

These properties are:

* retention
* latency
* licensing
* mappings

#### Retention

Retention is meant to describe how long an event_source retains logs for retrieval.

An event_source defines retention with two properties; `duration` and `comments`. 

> When defining an event_source you should report the event_sources actual data instead of your experience with the service - keep this unbiased as possible. 

The `duration` value accepts a string but please keep to a standard format of `{number} {days|weeks|years|hours|etc.}` if possible. Also, please add `comments` which helps with understanding the `duration` logs are kept within an event_source as well as any other pertinent information.

#### Latency

Latency is meant to describe the `duration` (or lag) from an event action to receiving the resulting log. The `duration` value accepts a string but please keep to a standard format of `{number} {days|weeks|years|hours|etc.}` if possible. Also, please add `comments` which helps with understanding the `duration` logs are kept within an event_source.

#### Licensing

Licensing is complex, that being said at this time EMM is only tracking any `comments` related to licensing. Please provide them in this section.

#### Mappings

Mappings are the key component of an event_source. `mappings` are a list of objects which define which categories, event_types and attributes are supported by a given event_source.

Each `mapping` object must contain a [category](#categories) ID and [event_type](#event-types) ID which is defined as a core data definition. Additionally, each `mapping` must define a list of [attributes](#attributes) which are supported by the event_source. Each attribute maps to a value within the provided example JSON event.

The `attribute` map must be in the format of `A000X` (which is the ID of an attribute) and the value must be the actual name of the field within the provided example.

To reiterate, this map contains the ID of a defined attribute and the value matches the value within an example JSON file.

If a field value is within nested JSON you can use dot notation. Using the below example, the map attribute value would be `product.name`.

```json
{
    "product":{
        "name: "Test"
    }
}
```
