<img src="./images/emm-logo.svg" alt="logo" width="600"/>

> You can view the Event Maturity Matrix at [https://eventmaturitymatrix.com/](https://eventmaturitymatrix.com/)

The Event Maturity Matrix (EMM) is a comprehensive framework that provides clarity regarding the capabilities and nuances of SaaS audit logging. EMM is a valuable resource for security practitioners who want to obtain visibility into the different types of user activities that are logged, see real-world examples of SaaS audit logs, and use these insights to guide security monitoring and operational objectives.

> If you have not read our blog post, [Introducing the SaaS Event Maturity Matrix](https://appomni.com/blog_post/appomni-saas-event-maturity-matrix/), we recommend doing so before proceeding.

- [Scope](#scope)
- [Matrix Overview](#matrix-overview)
- [Documentation](#documentation)
- [License](#license)
- [Security](#security)
- [Issues](#issues)
- [Credits](#credits)
- [Roadmap](#roadmap)

## Scope

SaaS is the operating system of business. As such, it's essential to protect the sensitive data that's stored and processed in SaaS platforms by monitoring for malicious and anomalous activity.

Historically, enterprise security monitoring has focused heavily on endpoint, network, and infrastructure services. However, with the increasing adoption of SaaS, defenders must shift their focus to also include security monitoring for tens to hundreds of SaaS platforms. Complicating matters, each SaaS platform has its own unique challenges and nuances involving audit log collection, event schemas, and levels of visibility into user activity.

This problem led to the creation of the SaaS Event Maturity Matrix (EMM): a comprehensive framework dedicated to SaaS application audit logging. The EMM is designed to serve as a reference for organizations to clearly understand security monitoring capabilities, event types, and event sources across SaaS platforms.

## Matrix Overview

> **Note:** We recommend reviewing our [Terminology & Definitions](./docs/terminology.md) section before proceeding.

The SaaS Event Maturity Matrix (EMM) was developed with the defensive security practitioner in mind. As such, the matrix’s overarching theme is to provide context regarding the depth of visibility as it pertains to security monitoring use cases. The matrix consists of the following concepts:

* [Products: represent the different SaaS platforms](./docs/data-defintion-reference.md#products)
* [Event Sources: represent the different audit log files / sources that can be queried and collected](./docs/data-defintion-reference.md#event-sources)
* [Event Categories: represent the primary, top level categories of SaaS audit logging](./docs/data-defintion-reference.md#event-categories)
* [Event Types: represent the different types of activity that's audited, organized by categories](./docs/data-defintion-reference.md#event-types)
* [Event Attributes: represent the the individual fields or keys from different event types](./docs/data-defintion-reference.md#event-attributes)

The EMM is built using various yml files and JSON schema docs. You can read more about these definitions, as well as their relationships, in the [Data Defintion Reference](./docs/data-defintion-reference.md) section.

## Documentation

You can find most documentation in the [docs](./docs/) folder. Below is a list of helpful documentation:

* [Terminology & Defintions](./docs/terminology.md)
* [Data Defintion Reference](./docs/data-defintion-reference.md)

## License

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.

Additionally, you can view the license in the [LICENSE.md](./LICENSE.md) file.

## Security

Security concerns are a top priority for us, please review our [Security Policy](SECURITY.md).

## Issues

If you encounter any problems,
please [file an issue](https://github.com/appomni/event_maturity_matrix/issues/new) along with a detailed description.

## Credits

This project was developed by the Threat Detection team at [AppOmni](https://appomni.com).

## Roadmap

We currently have identified the following roadmap items. If you have any suggestions, please [file an issue](https://github.com/appomni/event-maturity-matrix/issues/new).

* [ ] Add Microsoft as a product
* [ ] Add Google Workspace as a product
* [ ] Identify and add additional products as needed & requested
* [ ] Consider extending Event Categories by tailoring to distinct classes of SaaS platforms
* [ ] Expand nuances of SaaS platforms by adding additional context around licensing, permissions, and other relevant details
* [ ] Visualize attack paths that impact event sources, and ultimately those defined event sources
* [ ] Add Mitre ATT&CK mappings to event types
* [ ] Update site to be mobile friendly
* [ ] Add ability to compare visibility across products and event sources
