# Event Maturity Matrix Schema

This document defines the `event-maturity-matrix` (EMM) JSON Schema definitions. 

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

* Authentication - {Add a description here}
* Authorization - {Add a description here}
* System Audit - {Add a description here}
* Activity Audit - {Add a description here}

> These categories are subject to change and will likely be expanded upon in the future.

You can find the `event-maturity-matrix` defined categories [here](../categories.yml) based on our [schema](./categories.yml).

### Event Types

Event Types are the different types of activity that is audited. These are the core of the `event-maturity-matrix` and provide detection, security and IT professionals with understanding what can and cannot be detected / investigated with an event source.

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

The current full list of event types are:

* Account Login - {Add a description here}
* Account Logout - {Add a description here}
* MFA Verification - {Add a description here}
* Create User - {Add a description here}
* Read User - {Add a description here}
* Update User - {Add a description here}
* Delete User - {Add a description here}
* Create Group - {Add a description here}
* Read Group - {Add a description here}
* Update Group - {Add a description here}
* Delete Group - {Add a description here}
* Add to Group - {Add a description here}
* Remove From Group - {Add a description here}
* Create Role - {Add a description here}
* Read Role - {Add a description here}
* Update Role - {Add a description here}
* Delete Role - {Add a description here}
* Add Permission - {Add a description here}
* Remove Permission - {Add a description here}
* Add Enrollment - {Add a description here}
* Remove Enrollment - {Add a description here}
* Create Security Configuration - {Add a description here}
* Read Security Configuration - {Add a description here}
* Update Security Configuration - {Add a description here}
* Delete Security Configuration - {Add a description here}
* Create Integration - {Add a description here}
* Read Integration - {Add a description here}
* Update Integration - {Add a description here}
* Delete integration - {Add a description here}
* Create Resource - {Add a description here}
* Read Resource - {Add a description here}
* Update Resource - {Add a description here}
* Delete Resource - {Add a description here}
* Download Resource - {Add a description here}


> These event_types are subject to change and will likely be expanded upon in the future.

You can find the `event-maturity-matrix` defined event_types [here](../event_types.yml) based on our [schema](./event_types.yml).

### Attributes

Attributes are the individual fields (or keys) from different event_types. These help detction, security and IT professionals identify if they can or cannot detect certain activity effeciently (or even at all). 

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
