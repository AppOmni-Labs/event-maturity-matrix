# Terminology & Definitions

> The document is a reference of all terminology and definitions used within the Event Maturity Matrix.

|EMM Component|Term|Definition|MITRE TTP|
|-------------|----|----------|---------|
|Core         |Product|A SaaS platform. For example, Salesforce or Workday.||
|Core         |Event Source|A SaaS component that generates audit logs that are able to be queried and collected for analysis.||
|Core         |Event Category|The core, top level categories of the Event Maturity Maturity Matrix. Event Categories are used to organize specific Event Types.||
|Core         |Event Type|The different types of event activity that may be audited by a SaaS platform and available within an Event Source. Event Types are organized by Event Categories.||
|Core         |Event Attribute|The individual fields or keys that may be available within different Event Types.||
|Event Categories|Authentication|Event types that occur when an identity (for example, user account, service account, etc.) attempts to access a SaaS platform.||
|Event Categories|Authorization|Event types that occur during the management of access control on a SaaS platform, such as provisioning new access, removing access, or modifying the security controls that facilitate access control.||
|Event Categories|System Audit|Event types that occur during the management of tenant-wide, global security settings and third party integrations.||
|Event Categories|Activity Audit|Event types that occur during the creation, updating, deletion, and downloading of digital information stored or processed by a SaaS platform.||
|Event Types|Account Login|The process of an identity (for example, user account, service account, etc.) authenticating themselves to a SaaS platform.|[Initial Access: Trusted Relationship](https://attack.mitre.org/techniques/T1199/) - [Initial Access: Valid Accounts](https://attack.mitre.org/techniques/T1078/) - [Initial Access: Brute Force](https://attack.mitre.org/techniques/T1110/)|
|Event Types|Account Logout|The process of an identity (for example, user account, service account, etc.) actively logging themselves out of a SaaS platform.|[Impact: Account Access Removal](https://attack.mitre.org/techniques/T1531/)|
|Event Types|MFA Verification|The process of a user identity providing an additional method of authentication to the SaaS platform. For example, providing a one-time password (OTP) or utilizing a security token.|[Credential Access: Multi-Factor Authentication Request Generation](https://attack.mitre.org/techniques/T1621/) - [Credential Access: Multi-Factor Authentication Interception](https://attack.mitre.org/techniques/T1111/)|
|Event Types|Create User|The process of creating a new user account on a SaaS platform.|[Persistence: Create Account](https://attack.mitre.org/techniques/T1136/)|
|Event Types|Read User|The process of viewing a user account object on a SaaS platform.|[Discovery: Account Discovery](https://attack.mitre.org/techniques/T1087/)|
|Event Types|Update User|The process of modifying a user account object on a SaaS platform. For example, modifying the username or email address.|[Persistence: Account Manipulation](https://attack.mitre.org/techniques/T1098/)|
|Event Types|Delete User|The process of deleting or disabling a user account on a SaaS platform.|[Impact: Account Access Removal](https://attack.mitre.org/techniques/T153)|
|Event Types|Create Group|The process of creating a new security group on a SaaS platform. A security group is defined as a collection of users.|[Persistence: Account Manipulation](https://attack.mitre.org/techniques/T1098/)|
|Event Types|Read Group|The process of viewing a security group object or it's members on a SaaS platform. A security group is defined as a collection of users.|[Discovery: Permission Groups Discovery](https://attack.mitre.org/techniques/T1069/)|
|Event Types|Update Group|The process of modifying a security group object on a SaaS platform. For example, renaming a security group. A security group is defined as a collection of users.|[Persistence: Account Manipulation](https://attack.mitre.org/techniques/T1098/)|
|Event Types|Delete Group|The process of deleting a security group on a SaaS platform. A security group is defined as a collection of users.|[Persistence: Account Manipulation](https://attack.mitre.org/techniques/T1098/)|
|Event Types|Add to Group|The process of adding an identity (for example, user account, service account, etc.) to a security group. A security group is defined as a collection of users.|[Persistence: Account Manipulation](https://attack.mitre.org/techniques/T1098/)|
|Event Types|Remove from Group|The process of removing an identity (for example, user account, service account, etc.) to a security group. A security group is defined as a collection of users.|[Persistence: Account Manipulation](https://attack.mitre.org/techniques/T1098/)|
|Event Types|Create Role|The process of creating a new security role on a SaaS platform. A security role is defined as a collection of permissions.|[Persistence: Account Manipulation](https://attack.mitre.org/techniques/T1098/)|
|Event Types|Read Role|The process of viewing a security role object or it's permissions on a SaaS platform. A security role is defined as a collection of permissions.|[Discovery: Permission Groups Discovery](https://attack.mitre.org/techniques/T1069/)|
|Event Types|Update Role|The process of modifying a security role object on a SaaS platform. For example, renaming the security role. A security role is defined as a collection of permissions.|	[Persistence: Account Manipulation](https://attack.mitre.org/techniques/T1098/)|
|Event Types|Delete Role|The process of deleting a security role on a SaaS platform. A security role is defined as a collection of permissions.|[Persistence: Account Manipulation](https://attack.mitre.org/techniques/T1098/)|
|Event Types|Add Permission|The process of adding a new permission to a security role or identity on a SaaS platform. For example, adding admin privileges to a security role or user account.|[Persistence: Account Manipulation](https://attack.mitre.org/techniques/T1098/)|
|Event Types|Remove Permission|The process of removing a permission from a security role or identity on a SaaS platform. For example, removing admin privileges from a security role or user account.|[Persistence: Account Manipulation](https://attack.mitre.org/techniques/T1098/)|
|Event Types|Add Enrollment|The process of adding an MFA factor to an identity (for example, user account, service account, etc.). For example, adding a new authenticator app to a user account.|[Persistence: Account Manipulation](https://attack.mitre.org/techniques/T1098/) - [Credential Access: Multi-Factor Authentication Interception](https://attack.mitre.org/techniques/T1111/)|
|Event Types|Remove Enrollment|The process of removing an MFA factor from an identity (for example, user account, service account, etc.). For example, removing an authenticator app from a user account.|[Persistence: Account Manipulation](https://attack.mitre.org/techniques/T1098/) - [Impact: Account Access Removal](https://attack.mitre.org/techniques/T1531/)|
|Event Types|Create Security Configuration|The process of creating a new, global security policy or configuration setting on a SaaS platform. For example, creating a new IP allowlist or password complexity policy.|[Persistence/Defense Evasion: Modify Authentication Process](https://attack.mitre.org/techniques/T1556/)|
|Event Types|Read Security Configuration|The process of viewing existing security policy or configuration settings on a SaaS platform.|[Discover: Software Discovery](https://attack.mitre.org/techniques/T1518/)|
|Event Types|Update Security Configuration|The process of modifying a global security policy or configuration setting on a SaaS platform. For example, modifying the global tenant MFA requirements.|[Persistence/Defense Evasion: Modify Authentication Process](https://attack.mitre.org/techniques/T1556/) - [Defense Evasion: Impair Defenses](https://attack.mitre.org/techniques/T1562/)|
|Event Types|Delete Security Configuration|The process of deleting a global security policy or configuration setting on a SaaS platform. For example, deleting an IP allowlist or authentication policy.|[Persistence/Defense Evasion: Modify Authentication Process](https://attack.mitre.org/techniques/T1556/) - [Defense Evasion: Impair Defenses](https://attack.mitre.org/techniques/T1562/)|
|Event Types|Create Integration|The process of creating a new integration on a SaaS platform. For example, creating or adding a new third party or OAuth application.|[Persistence: Create Account](https://attack.mitre.org/techniques/T1528/) - [Credential Access: Steal Application Access Token](https://attack.mitre.org/techniques/T1528/)|
|Event Types|Read Integration|The process of viewing an integration on a SaaS platform. For example, viewing the configuration or security settings of a third party or OAuth application.|[Discover: Software Discovery](https://attack.mitre.org/techniques/T1518/)|
|Event Types|Update Integration|The process of modifying an integration on a SaaS platform. For example, modifying the API settings or credentials of a third party or OAuth application.|[Defense Evasion/Lateral Movement: Use Alternate Authentication Material](https://attack.mitre.org/techniques/T1550/) - [Credential Access: Steal Application Access Token](https://attack.mitre.org/techniques/T1528/)|
|Event Types|Delete Integration|The process of deleting an integration on a SaaS platform. For example, deleting or disabling a third party or OAuth application.|[Defense Evasion: Impair Defenses](https://attack.mitre.org/techniques/T1080/)|
|Event Types|Create Resource|The process of creating a new resource on a SaaS platform. For example, creating a new file, folder, or report.|[Lateral Movement: Taint Shared Content](https://attack.mitre.org/techniques/T1080/)|
|Event Types|Read Resource|The process of viewing a resource on a SaaS platform. For example, viewing a file, folder, or report.|[Collection: Automated Collection](https://attack.mitre.org/techniques/T1119/) - [Collection: Data from Information Repositories](https://attack.mitre.org/techniques/T1213/)|
|Event Types|Update Resource|The process of modifying a resource on a SaaS platform. For example, modifying a file, folder, or report.|[Lateral Movement: Taint Shared Content](https://attack.mitre.org/techniques/T1080/) - [Impact: Data Manipulation](https://attack.mitre.org/techniques/T1565/)|
|Event Types|Delete Resource|The process of deleting a resource on a SaaS platform. For example, deleting a file, folder, or report.|[Impact: Data Destruction](https://attack.mitre.org/techniques/T1485/) - [Impact: Data Manipulation](https://attack.mitre.org/techniques/T1565/)|
|Event Types|Download Resource|The process of downloading a resource on a SaaS platform. For example, downloading a file, folder, or report.|[Exfiltration: Exfiltration Over Alternative Protocol](https://attack.mitre.org/techniques/T1048/)|
|Event Attributes|Timestamp|The date and time at which an event occurred.||
|Event Attributes|Event ID|Uniquely identifies the event.||
|Event Attributes|Event Code / Type|Identifies the operation or activity type that occurred and is described in the event.||
|Event Attributes|Result|Indicates whether the event was successful or not.||
|Event Attributes|Username|Identifies the user who performed the event.||
|Event Attributes|User ID|Identifies the unique identifier of the user who performed the event.||
|Event Attributes|User Type / Role|Identifies the type of user or the user's role within the SaaS platform.||
|Event Attributes|Session ID|Identifies the unique session identifier that a user has within the SaaS platform.||
|Event Attributes|IP Address|Identifies the IP address that was used to access the SaaS platform.||
|Event Attributes|IP Address Geo / ASN|Identifies the IP address geolocation or autonomous system (AS) that was used to access the SaaS platform.||
|Event Attributes|User Agent|Identifies the type of device and software that was used to access the SaaS platform.||
|Event Attributes|Device / Client Type|Identifies the type of computer device or client software that was used to access the SaaS platform.||
|Event Attributes|Failure Context|Provides a description or reason for why an event action or operation failed.||
|Event Attributes|Credential Context|Provides information about the credentials that were used to access the SaaS platform.||
|Event Attributes|Identity Service Provider Context|Provides information about the identity service provider (IDP) that was used to authenticate the user.||
|Event Attributes|Verification Method|Identifies the method that was used to verify the user's identity during multi-factor authentication (MFA).||
|Event Attributes|Verification Flagged|Indicates if a user flagged or reported a failed multi-factor authentication (MFA) verification request.||
|Event Attributes|Activity Performed|Identifies the activity that a user performed after step-up multi-factor authentication (MFA) verification.||
|Event Attributes|Target Username|Identifies the user who was affected by the event.||
|Event Attributes|Target Attribute Context|Provides information about the metadata that was affected by the event.||
|Event Attributes|Target Group Name|Identifies the security group name that was affected by the event.||
|Event Attributes|Target Role Name|Identifies the security role name that was affected by the event.||
|Event Attributes|Permission Name|Identifies the name of the permission that was affected by the event.||
|Event Attributes|Target Resource Name|Identifies the name of the resource (for example, application, report, security group, etc.) that was affected by the action or operation of the event.||
|Event Attributes|Enrollment Type|Provides information about the user's multi-factor authentication (MFA) enrollment that was affected by the event.||
|Event Attributes|Configuration / Setting Name|Identifies the name of the setting, policy, or configuration parameter that was affected by the event.||
|Event Attributes|Configuration / Setting Value|Identifies the new value of a changed setting, policy, or configuration parameter that was affected by the event.||
|Event Attributes|Previous Configuration / Setting Value|Identifies the previous value of a changed setting, policy, or configuration parameter that was affected by the event.||
|Event Attributes|Integration / App Name|Identifies the name of the third party or OAuth application that was affected by the event.||
|Event Attributes|Resource Name|Identifies the name of the resource (for example, application, file, report, etc.) that was accessed in the event.||
|Event Attributes|Resource Type|Identifies the type of the resource (for example, application, file, report, etc.) that was accessed in the event.||
|Event Attributes|Resource Metadata|Provides additional information about the resource (for example, application, file, report, etc.) that was accessed in the event.||
