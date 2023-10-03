# Event Maturity Matrix Schema

This document defines the `event-maturity-matrix` (EMM) JSON Schema defintions. 

## Core

The core components of the `EMM` project are hierarchical in order. Each has a JSON Schema document. 

* [categories](./categories.yml)
* [event_types](./event_types.yml)
* [attributes](./attributes.yml)

The base values for each of these schemas are located in the [root](../) of this repository.

* [categories](../categories.yml)
* [event_types](../event_types.yml)
* [attributes](../attributes.yml)

## Product

Each defined `product` is located in the [products](../products) folder. Every `event_source` will have a `product` associated with it.

The `product` JSON schema is located [here](./product.yml).
You can find an example product [here](../template.product.yml).

## Event Source

Each defined `event_source` is located in the associated products folder. Typically will be located in `products/{product name}/event_sources`.

The `event_source` JSON schema is located [here](./event_source.yml).
You can find an example event source [here](../template.event_source.yml).

### Categories

Categories are logical buckets for each `event_type`. The current categories are:

* Authentication - This category contains events related to authentication.
* Authorization - This category contains events related to the management of or access of a specific service provider.
* System Audit - Tenant level setting / configuration operations that impact an entire product.
* Activity Audit - This category contains events related to general activity within an environment.

> These categories are subject to change and will likely be expanded upon in the future.

You can find the `event-maturity-matrix` defined categories [here](../categories.yml) based on our [schema](./categories.yml).

### Event Types

Event Types are the different types of activity that's audited. These are the core of the `event-maturity-matrix` and provide detection, security and IT professionals with understanding what can and can't be detected / investigated with a event source.

The current list of event types by root type are:

* Account Login & Logout
* MFA Verification
* User operations
* Group operations
* Role Operations
* Permission operation
* Enrollment operations
* Security Configuration operations
* Integration operations
* Resource operations

> These event_types are subject to change and will likely be expanded upon in the future.

You can find the `event-maturity-matrix` defined event_types [here](../event_types.yml) based on our [schema](./event_types.yml).

### Attributes

Attributes are the individual fields (or keys) from different event_types. These help detction, security and IT professionals identify if they can or can't detect certain activity effeciently (or even at all). 

Current defined attributes are:

* Timestamp
* Event Id
* Username
* User Id
* User Type / Role
* Session Id
* IP Address
* IP Geolocation
* IP ASN
* User Agent Name
* Device/Client Type
* Login Result
* Failure Context
* Credential Context
* Identity Service Provider Context
* Verification Result
* Verificatio Method
* Verification Flagged
* Activity Performed
* Target Username
* Target Attribute Context
* Target Group Name
* Target Role Name
* Permission Name
* Target Resource Name
* Enrollment Type
* Previous Enrollment Type
* New Enrollment Type
* Event Code / Type

Each of these `attributes` can have several properties but the most important ones are the `include` and `exclude` properties. These properties indicate which `event_types` that this attribute can be referenced.

> These attributes are subject to change and will likely be expanded upon in the future.

You can find the `event-maturity-matrix` defined attributes [here](../attributes.yml) based on our [schema](./attributes.yml).
