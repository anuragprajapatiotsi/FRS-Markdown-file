**FUNCTIONAL REQUIREMENTS SPECIFICATION**

**Unified Web Portal & Dashboard  
Social Statistics Division (SSD)  
Ministry of Statistics and Programme Implementation (MoSPI)  
Government of India**

*Aligned with IEEE 830 and ISO/IEC/IEEE 29148 principles for practical Government of India software projects*

| **Item** | **Details** |
| --- | --- |
| Document Title | Functional Requirements Specification (FRS) |
| Project Name | SSD Unified Web Portal & Dashboard |
| Tender Reference | M-12012/01/2024-SSD-III-Part(1) |
| Client | Ministry of Statistics and Programme Implementation (MoSPI), Government of India |
| Business Division | Social Statistics Division (SSD) |
| Enterprise Baseline Version | 1.2 |
| Prepared By | Mohan Kadium |
| Reviewed By | Mayank Pachauri |
| Approved By | Pratap Bodimalla |
| Document Date | 15 July 2026 |

Table of Contents

[**Document Control 6**](#_Toc235009788 "#_Toc235009788")

[**Document Status 6**](#_Toc235009789 "#_Toc235009789")

[**Revision History 6**](#_Toc235009790 "#_Toc235009790")

[**Approvals 6**](#_Toc235009791 "#_Toc235009791")

[**Distribution List 7**](#_Toc235009792 "#_Toc235009792")

[**Confidentiality Statement 7**](#_Toc235009793 "#_Toc235009793")

[**Change Control 7**](#_Toc235009794 "#_Toc235009794")

[**Requirement Wording and Priority Conventions 8**](#_Toc235009795 "#_Toc235009795")

[**1. Introduction 8**](#_Toc235009797 "#_Toc235009797")

[**1.1 Purpose 8**](#_Toc235009798 "#_Toc235009798")

[**1.2 Scope 8**](#_Toc235009799 "#_Toc235009799")

[**1.3 Scope Boundaries 8**](#_Toc235009800 "#_Toc235009800")

[**2. Organizational Overview 9**](#_Toc235009801 "#_Toc235009801")

[**3. Product Overview 9**](#_Toc235009802 "#_Toc235009802")

[**3.1 Product Perspective 9**](#_Toc235009803 "#_Toc235009803")

[**3.2 Product Functions 9**](#_Toc235009804 "#_Toc235009804")

[**3.3 User Classes and Characteristics 10**](#_Toc235009805 "#_Toc235009805")

[**4. Stakeholders and User Classes 10**](#_Toc235009806 "#_Toc235009806")

[**5. Architecture and UML Catalogue 12**](#_Toc235009807 "#_Toc235009807")

[**5.1 Cloud Infrastructure Architecture 12**](#_Toc235009808 "#_Toc235009808")

[**5.2 Solution Architecture 13**](#_Toc235009809 "#_Toc235009809")

[**5.3 Technical Architecture 14**](#_Toc235009810 "#_Toc235009810")

[**5.4 Use Case Context Diagram 15**](#_Toc235009811 "#_Toc235009811")

[**5.5 Sequence Diagram - Login, Role and Pillar Access 16**](#_Toc235009812 "#_Toc235009812")

[**5.6 Sequence Diagram - Framework, Indicator, Dimension and Template Setup 17**](#_Toc235009813 "#_Toc235009813")

[**5.7 Sequence Diagram - Collection Request, Invitation, Data Entry and Ingestion 18**](#_Toc235009814 "#_Toc235009814")

[**5.8 Sequence Diagram - Validation, Review, Approval and Published Facts 19**](#_Toc235009815 "#_Toc235009815")

[**5.9 Sequence Diagram - Publication Workspace, CMS, DMS and Public Output 20**](#_Toc235009817 "#_Toc235009817")

[**5.10 Setup to Template User Flow 21**](#_Toc235009818 "#_Toc235009818")

[**5.11 Request to Submission User Flow 22**](#_Toc235009819 "#_Toc235009819")

[**5.12 Validation to Published Facts User Flow 23**](#_Toc235009820 "#_Toc235009820")

[**5.13 Publication and Dashboard User Flow 24**](#_Toc235009822 "#_Toc235009822")

[**5.14 Core Module Entity Flow 25**](#_Toc235009823 "#_Toc235009823")

[**5.15 Masters, Framework and Indicator Entities 26**](#_Toc235009824 "#_Toc235009824")

[**5.16 Dimensions and Template Designer Entities 27**](#_Toc235009826 "#_Toc235009826")

[**5.17 Request to Published Data Entities 28**](#_Toc235009827 "#_Toc235009827")

[**5.18 Functional Architecture 28**](#_Toc235009828 "#_Toc235009828")

[**6. External Interface Requirements 29**](#_Toc235009829 "#_Toc235009829")

[**6.1 Technology Stack 29**](#_Toc235009830 "#_Toc235009830")

[**6.2 Browser Compatibility 29**](#_Toc235009831 "#_Toc235009831")

[**7. Functional Requirements 30**](#_Toc235009832 "#_Toc235009832")

[**7.1 Authentication, User Access and Security 30**](#_Toc235009833 "#_Toc235009833")

[**7.2 Application Setup, Pillar and Workstreams 32**](#_Toc235009834 "#_Toc235009834")

[**7.3 Reference Masters 33**](#_Toc235009835 "#_Toc235009835")

[**7.4 Framework Setup and Hierarchy 35**](#_Toc235009836 "#_Toc235009836")

[**7.5 Indicator Management and Source Mapping 36**](#_Toc235009837 "#_Toc235009837")

[**7.6 Dimension Management 38**](#_Toc235009838 "#_Toc235009838")

[**7.7 Template Management and Excel-like Designer 39**](#_Toc235009839 "#_Toc235009839")

[**7.8 Collection Requests and Assignment 41**](#_Toc235009840 "#_Toc235009840")

[**7.9 Invitation Access and Temporary Contributor 43**](#_Toc235009841 "#_Toc235009841")

[**7.10 Data Entry, Excel Upload and Ingestion 44**](#_Toc235009842 "#_Toc235009842")

[**7.11 Validation Rule Execution and Report 46**](#_Toc235009843 "#_Toc235009843")

[**7.12 Review, Approval and Published Fact Creation 48**](#_Toc235009844 "#_Toc235009844")

[**7.13 Published Data and Fact Store 50**](#_Toc235009845 "#_Toc235009845")

[**7.14 Publication Management Workspace and PDF Designer 51**](#_Toc235009846 "#_Toc235009846")

[**7.15 Dashboards and Analytics Views 53**](#_Toc235009847 "#_Toc235009847")

[**7.16 Content Management System - Plone 54**](#_Toc235009848 "#_Toc235009848")

[**7.17 Document Management System - ownCloud 56**](#_Toc235009849 "#_Toc235009849")

[**7.18 Notification Engine, Reminders and Schedulers 57**](#_Toc235009850 "#_Toc235009850")

[**7.19 Logs, Monitoring, Backup and Audit 59**](#_Toc235009851 "#_Toc235009851")

[**7.20 Accessibility, Bilingual Support and Preferences 60**](#_Toc235009852 "#_Toc235009852")

[**8. Business Rules 62**](#_Toc235009853 "#_Toc235009853")

[**9. Data Dictionary 63**](#_Toc235009854 "#_Toc235009854")

[**10. Non-Functional Requirements 65**](#_Toc235009855 "#_Toc235009855")

[**10.1 Production Parameter Baseline 66**](#_Toc235009856 "#_Toc235009856")

[**10.2 Phase I Scope and Future / Approval-Based Scope 66**](#_Toc235009857 "#_Toc235009857")

[**11. Security Requirements 67**](#_Toc235009858 "#_Toc235009858")

[**11.1 Security Acceptance Criteria 67**](#_Toc235009859 "#_Toc235009859")

[**12. Compliance Requirements 68**](#_Toc235009860 "#_Toc235009860")

[**13. Integration Requirements 68**](#_Toc235009861 "#_Toc235009861")

[**14. Requirements Traceability Matrix 68**](#_Toc235009862 "#_Toc235009862")

[**15. Deliverables and Milestones 69**](#_Toc235009863 "#_Toc235009863")

[**16. Assumptions, Dependencies, Risks, and Constraints 70**](#_Toc235009864 "#_Toc235009864")

[**16.1 Assumptions 70**](#_Toc235009865 "#_Toc235009865")

[**16.2 Dependencies 70**](#_Toc235009866 "#_Toc235009866")

[**16.3 Risks and Constraints 70**](#_Toc235009867 "#_Toc235009867")

[**17. Glossary and Acronyms 71**](#_Toc235009868 "#_Toc235009868")

[**18. Minimum Client Submission Enhancements 71**](#_Toc235009869 "#_Toc235009869")

[**18.1 Atomic Functional Requirement ID Catalogue 71**](#_Toc235009870 "#_Toc235009870")

[**18.2 Screen Inventory and UI Specification Baseline 72**](#_Toc235009871 "#_Toc235009871")

[**18.3 Field-Level Logical Data Dictionary Addendum 72**](#_Toc235009872 "#_Toc235009872")

[**18.4 Enhanced Requirements Traceability Matrix Addendum 74**](#_Toc235009873 "#_Toc235009873")

[**18.5 Role-Permission Matrix 75**](#_Toc235009874 "#_Toc235009874")

[**18.6 API Inventory 75**](#_Toc235009875 "#_Toc235009875")

[**18.7 Master Tables Catalogue 76**](#_Toc235009876 "#_Toc235009876")

[**18.8 State Transition Diagrams and Tables 76**](#_Toc235009877 "#_Toc235009877")

[**18.9 Role Matrix and Permission Matrix Summary 77**](#_Toc235009878 "#_Toc235009878")

[**18.10 Screen-wise Detailed Use Case Baseline 77**](#_Toc235009879 "#_Toc235009879")

[**18.11 End-to-End User Journey 78**](#_Toc235009880 "#_Toc235009880")

[**18.12 Production Scope Clarification and Pending SRS Values 79**](#_Toc235009881 "#_Toc235009881")

[**19. Document List to be submitted 80**](#_Toc235009882 "#_Toc235009882")

[**20. Document Approval 80**](#_Toc235009882 "#_Toc235009882")

# Document Control

## Document Status

This FRS is an enterprise baseline candidate prepared from the existing MoSPI SSD FRS. Version 2.2 incorporates the final NIC/DIID client-submission correction pass required before sharing with stakeholders. It shall be reviewed and baselined by MoSPI through the formal approval process. Any addition, deletion, or change to approved scope after baseline approval shall be managed through formal change control.

## Revision History

| **Version** | **Date** | **Description of Change** | **Author/Owner** | **Status** |
| --- | --- | --- | --- | --- |
| 0.1 | 21 May 2026 | Initial Draft | Prepared by Megha Pandey | Draft |
| 0.2 | To be confirmed | Review Updates | MoSPI/Project Team | Review |
| 0.3 | To be confirmed | Final Approved Version | MoSPI/Project Team | Approved in source history |
| 1.0 | 26 May 2026 | Source FRS version used as baseline for this enhancement | MoSPI SSD Project Team | Source Baseline |
| 1.1 | Current | Enterprise-grade restructuring aligned with IEEE 830 / ISO/IEC/IEEE 29148 principles; added document control, interfaces, requirement IDs, data dictionary, business rules, measurable NFRs, compliance, security, and RTM. No scope expansion intended. | Solution Architecture / Requirements Engineering Review | Draft for MoSPI Review |
| 2.1 | Current | Minimum client-submission readiness updates incorporated: version control corrected; atomic FR-ID catalogue added; screen inventory and UI specification baseline added; field-level logical data dictionary added; enhanced RTM addendum added; role-permission matrix added; sequence diagrams added; terminology and capitalization cleanup completed. No scope expansion intended. | Solution Architecture / Requirements Engineering Review | Client Submission Draft |
| 2.2 | Current | NIC/DIID client-submission correction pass incorporated: Table of Contents updated; MFA explicitly added for privileged users; Maker-Checker rule added; scanned/non-machine-readable source handling clarified; DBIM compliance and glossary entry added; Integration/Middleware Layer wording restored; functional nodal officer approval language added; Phase I exclusions clarified; DIID closure matrix added; formatting/font readability improved. No scope expansion intended. | Solution Architecture / Requirements Engineering Review | Client Submission Ready |

## Approvals

| **Name** | **Role** | **Organization** | **Signature** | **Date** |
| --- | --- | --- | --- | --- |
| SSD-MOSPI | Approver / Client Representative | MoSPI |  |  |
| Mayank Pachauri | Reviewer | MoSPI / Project Team( OTSI) |  |  |
| Mohan Kadium | Prepared By | Project Team(OTSI) |  |  |
| Project Manager | Implementation Owner | Project Team(OTSI) |  |  |
| Technical Lead | Technical Review | Project Team(OTSI) |  |  |
| QA Lead | Quality Assurance Review | OTSI |  |  |
| Security / Compliance Reviewer | CERT-In/STQC/GIGW Readiness Review | MoSPI / Auditor |  |  |

## Distribution List

| **Recipient / Group** | **Organization** | **Purpose** | **Access Level** |
| --- | --- | --- | --- |
| MoSPI SSD Senior Stakeholders | MoSPI | Review, approval, governance | Confidential |
| SSD Department Users | MoSPI SSD | Business validation and UAT | Confidential |
| DIID, MoSPI | MoSPI | Cloud infrastructure coordination | Confidential |
| Selected Implementation Agency | Vendor | Design, development, testing, implementation | Confidential |
| CERT-In Empanelled Auditor | Auditor | Security audit and VAPT | Confidential |
| STQC / GIGW Certification Team | Government certification/audit | Portal quality and compliance verification | Confidential |
| Line Ministry / Department Nodal Users | Government data providers | Submission workflow and UAT inputs | Restricted |

## Confidentiality Statement

This document is confidential and intended solely for MoSPI, authorized Government of India stakeholders, and approved implementation/audit partners. It contains business, functional, architectural, operational, security, and compliance requirements for the SSD Unified Web Portal & Dashboard project. Unauthorized disclosure, distribution, reproduction, or use of this document is prohibited without written approval from MoSPI.

## Change Control

| **Change Control Principle** | **Requirement** |
| --- | --- |
| Baseline Control | After MoSPI approval, this FRS shall be treated as the baseline requirements document for design, development, QA, UAT, security audit, and project governance. |
| Change Request | Any scope, functionality, module, workflow, interface, integration, data model, security, or compliance change shall be raised through a formal Change Request (CR). |
| Impact Analysis | Each CR shall include impact on scope, schedule, cost, architecture, data, security, test cases, training, operations, and documentation. |
| Approval | No CR shall be implemented until approved by MoSPI or the designated change control authority. |
| Traceability | All approved changes shall be mapped to requirement IDs, design components, test cases, release notes, and audit records. |

## Requirement Wording and Priority Conventions

| **Term** | **Usage in this FRS** |
| --- | --- |
| Shall | Mandatory requirement to be implemented and verified. |
| Should | Recommended requirement; avoided unless implementation flexibility is explicitly intended. |
| May | Permissive statement; used only for optional behavior or stakeholder discretion. |
| Must | Used only where external law, Government mandate, security control, or compliance rule requires mandatory conformance. |
| Priority: High | Required for Go-Live / contractual compliance / core business workflow. |
| Priority: Medium | Required for full release or operational efficiency but not a blocker to minimum viable Go-Live unless specified by MoSPI. |
| Priority: Low | Useful enhancement or configuration preference that does not affect core workflow acceptance. |

# 1. Introduction

## 1.1 Purpose

This FRS explains how the SSD portal will work for setup, data collection, validation, review, approval, publication and dashboard use. It is written for business users, developers, testers, deployment teams and governance reviewers. The wording is intentionally practical and screen-oriented.

## 1.2 Scope

* Internal portal for SSD Pillar SDG, SWS, ENV, BRICS.
* Role-based access for Super Admin, Pillar Admin, metadata users, template users, data providers, validators, reviewers, approvers, auditors and public users.
* Framework, masters, dimensions, indicators, templates, requests, invitations, data entry, ingestion, validation, review, publication and dashboards.
* Plone CMS, ownCloud DMS, notifications, reminders, email reports, audit, monitoring and accessibility/bilingual support.

## 1.3 Scope Boundaries

* SSO/LDAP is not part of the current active implementation scope. It may be taken up later only if approved.
* Public users can see only approved data, Dashboard and public CMS pages.
* Raw passwords, raw tokens, token hashes, source hashes, internal IDs and sensitive payloads are not displayed in normal screens or reports.
* Multi-Factor Authentication (MFA) shall be mandatory for Super Admin, Admin, Reviewer, Approver, Publisher and other privileged users or workflow roles as approved by MoSPI security policy.
* Scanned or non-machine-readable source submissions shall be preserved as source artifacts and handled through manual entry, template-based resubmission, or clarification workflow; automated OCR is not included in Phase I unless separately approved by MoSPI.
* SMS, WhatsApp, OCR, Digital Signature, PDF Watermark, AI Insights and SSO/LDAP are not part of Phase I unless specifically approved by MoSPI through change control.

# 2. Organizational Overview

|  |  |
| --- | --- |
| **Area** | **Description** |
| SSD | Responsible for the statistical data collection, review, publication and dashboard process. |
| SDG | Top-level pillar with its own admin, setup, requests and dashboards. |
| SWS | Top-level pillar with its own admin, setup, requests and dashboards. |
| ENV | Top-level pillar for environment-related work. |
| BRICS | Top-level pillar for BRICS related work. |

# 3. Product Overview

## 3.1 Product Perspective

The portal is a microservices-style web platform deployed through Docker services. It has a React UI, FastAPI middle layer, PostgreSQL database schemas, published fact tables, Plone CMS, ownCloud DMS and a separate notification service.

## 3.2 Product Functions

|  |  |  |
| --- | --- | --- |
| **Sl.no** | **Main Function** | **Simple Description** |
| 1 | Authentication, User Access and Security | This module controls who can enter the portal, what pillar they can access and which screens/actions they can use. |
| 2 | Application Setup, Pillar and Workstreams | This module keeps the portal configurable for SDG, SWS, ENV and BRICS. |
| 3 | Reference Masters | Masters are controlled lists used by the rest of the portal: locales, organizations, officers, periodicities, measures and units. |
| 4 | Framework Setup and Hierarchy | A framework is the approved structure used to arrange indicators. It may have levels such as Goal and Target, but level names are dynamic and configurable. |
| 5 | Indicator Management and Source Mapping | This module defines national indicators, global mappings, metadata, versions, measures, formulas and one or more source assignments. |
| 6 | Dimension Management | Dimensions define how data is broken down, for example geography, time, area type and gender. Users can also create additional dimensions. |
| 7 | Template Management and Excel-like Designer | Templates are governed Excel-like formats. The user sees a grid, but the system saves dimensions, measures, cell mappings and render options in database tables. |
| 8 | Collection Requests and Assignment | A request assigns data collection work to the correct source organization/officer for a template and indicator. |
| 9 | Invitation Access and Temporary Contributor | This module lets request-linked external contributors access only their assigned data entry page through a temporary link. |
| 10 | Data Entry, Excel Upload and Ingestion | This module receives values entered in the template or uploaded in Excel and converts them to staged records. |
| 11 | Validation Rule Execution and Report | Validation checks submitted/staged data before review. |
| 12 | Review, Approval and Published Fact Creation | Reviewers take the decision on validated submissions. Final approval publishes approved facts. |
| 13 | Published Data and Fact Store | This is the trusted final data store after approval. |
| 14 | Publication Management Workspace and PDF Designer | After facts are published, this module helps prepare official PDF publications. |
| 15 | Dashboards and Analytics Views | Dashboards show work status and approved statistical output. |
| 16 | Content Management System - Plone | CMS manages public portal pages, menus and bilingual content. |
| 17 | Document Management System - ownCloud | DMS stores documents, evidence and generated publication files with access and retention. |
| 18 | Notification Engine, Reminders and Schedulers | Notifications are a separate Phase I support service for email, notification logs, reminders, escalation and reports. |
| 19 | Logs, Monitoring, Backup and Audit | This module gives operations and audit teams a safe view of system health, logs, backups and activity. |
| 20 | Accessibility, Bilingual Support and Preferences | This is a cross-cutting requirement so the application is usable by Hindi/English users and persons with disabilities, including blind users. |

## 3.3 User Classes and Characteristics

|  |  |
| --- | --- |
| **User Class** | **Main Work** |
| Super Admin | Cross-Pillar configuration, users, monitoring and governance views. |
| Pillar Admin | Own Pillar setup, requests, review status and dashboards. |
| Metadata Officer | Framework, indicators, dimensions, sources and measures. |
| Template Officer | Template list, template design and active template version. |
| Data Provider / Temporary Contributor | Open request-linked data entry page, fill data, upload Excel and submit. |
| Validator | Check validation queue and validation report. |
| Reviewer / Approver | Review, approve, reject, send back or ask clarification. |
| Publication Officer | Create official publication PDF from approved data. |
| Auditor / Operations | View audit, logs, health, backups and evidence. |
| Public User | View public CMS pages and approved dashboard where enabled. |

# 4. Stakeholders and User Classes

|  |  |
| --- | --- |
| **Stakeholder** | **Interest in System** |
| MoSPI / SSD Leadership | Approved data, publication status, dashboards and audit readiness. |
| Source Ministries / Departments / Divisions | Receive collection requests and submit data. |
| Validators / Reviewers / Approvers | Check data quality and make decisions. |
| Public Users | View approved information where public access is enabled. |
| Operations / Security / Audit | Monitor logs, backups, alerts and compliance evidence. |

# 5. Architecture and UML Catalogue

## 5.1 Cloud Infrastructure Architecture

<!-- IMAGE_PLACEHOLDER -->

## 5.2 Solution Architecture

<!-- IMAGE_PLACEHOLDER -->

## 5.3 Technical Architecture

<!-- IMAGE_PLACEHOLDER -->

## 5.4 Use Case Context Diagram

<!-- IMAGE_PLACEHOLDER -->

## 5.5 Sequence Diagram - Login, Role and Pillar Access

<!-- IMAGE_PLACEHOLDER -->

## 5.6 Sequence Diagram - Framework, Indicator, Dimension and Template Setup

<!-- IMAGE_PLACEHOLDER -->

## 5.7 Sequence Diagram - Collection Request, Invitation, Data Entry and Ingestion

<!-- IMAGE_PLACEHOLDER -->

## 5.8 Sequence Diagram - Validation, Review, Approval and Published Facts

## 

## 5.9 Sequence Diagram - Publication Workspace, CMS, DMS and Public Output

<!-- IMAGE_PLACEHOLDER -->

## 5.10 Setup to Template User Flow

<!-- IMAGE_PLACEHOLDER -->

## 5.11 Request to Submission User Flow

<!-- IMAGE_PLACEHOLDER -->

## 5.12 Validation to Published Facts User Flow

## 

## 5.13 Publication and Dashboard User Flow

<!-- IMAGE_PLACEHOLDER -->

## 5.14 Core Module Entity Flow

<!-- IMAGE_PLACEHOLDER -->

## 5.15 Masters, Framework and Indicator Entities

## 

## 5.16 Dimensions and Template Designer Entities

<!-- IMAGE_PLACEHOLDER -->

## 5.17 Request to Published Data Entities

<!-- IMAGE_PLACEHOLDER -->

## 5.18 Functional Architecture

|  |  |  |
| --- | --- | --- |
| **Layer** | **Modules** | **Purpose** |
| Access and setup | Auth, Pillar, application setup | Control who can access which Pillar and page. |
| Reference setup | Masters, framework, indicators, dimensions | Prepare controlled lists and structures. |
| Collection design | Templates and requests | Prepare the format and assign data collection work. |
| Submission processing | Invitation, data entry, ingestion | Collect and stage source data. |
| Quality and decision | Validation, review, approval | Check quality and record decisions. |
| Publication | Published data, publication workspace, dashboard, CMS/DMS | Use approved data for reporting and public output. |
| Support | Notifications, logs, monitoring, backup, accessibility | Support reliable operation and compliance. |
| Integration / Middleware | FastAPI services, API gateway, authentication, RBAC, routing, validation, logging and integration adapters | Provide controlled API orchestration, secure service-to-service communication, message processing, external connectivity and mediation between presentation, application and data layers. |

# 6. External Interface Requirements

|  |  |
| --- | --- |
| **Interface** | **Requirement** |
| UI | React/Vite portal with responsive layout, bilingual labels, accessible forms/tables and role-aware navigation. |
| API / Integration / Middleware Layer | FastAPI services and approved middleware/integration controls with RBAC, Pillar scope, stable-code response, safe field exposure, request validation, audit logging, routing, retry/fallback handling and secure connectivity to approved internal/external services. |
| Database | PostgreSQL schemas for all business modules and published fact tables. |
| CMS | Plone for public content and page workflow. |
| DMS | ownCloud for document storage, versioning and retention. |
| Notifications | Email, OTP, notification logs and configurable reminders/escalations. |
| SSO/LDAP | Not used in current scope. Future integration only if approved. |

## 6.1 Technology Stack

|  |  |  |  |
| --- | --- | --- | --- |
| **Layer** | **Technology** | **Purpose** | **Status** |
| Database | PostgreSQL | Main relational database and approved fact tables. | Production baseline |
| Database scale | Citus | Distributed analytics/fact-table option for large data volume. | Phase I production scope |
| Graph / lineage | Apache AGE | Graph projection for lineage and impact traversal. | Phase I production scope |
| API | Python FastAPI, Pydantic, psycopg | REST APIs, validation, SQL-first DB access. | Production baseline |
| Runtime | Docker, Uvicorn, reverse proxy | Container deployment and health checks. | Production baseline |
| UI | React, Vite, TypeScript, Tailwind | Internal portal, temporary contributor page and public dashboard. | Production baseline |
| UI helpers | TanStack Query, React Hook Form, Zod, lucide-react | API state, form validation and icons. | Approved UI stack |
| Charts | Apache ECharts and D3.js | Dashboard charts, drilldown and custom visualizations. | Production scope |
| Maps | Leaflet | Geography/map visualization where required. | Production scope |
| CMS | Plone | Public page and content management. | External CMS integration; not custom-built inside SSD Phase I |
| DMS | ownCloud | Document storage, versions, retention and preview. | External DMS integration; not custom-built inside SSD Phase I |
| Notification | Separate email notification service | Request mail, OTP/email alerts, reminders, escalation and report delivery. | Phase I production support service |

## 6.2 Browser Compatibility

|  |  |  |
| --- | --- | --- |
| **Browser** | **Supported Version** | **Notes** |
| Google Chrome | Latest and previous two stable versions | Primary desktop browser support. |
| Microsoft Edge | Latest and previous two stable versions | Primary Government/enterprise Windows support. |
| Mozilla Firefox | Latest and previous two stable versions | Supported for internal portal. |
| Apple Safari | Current supported macOS/iPadOS versions | Supported for responsive/public views; full internal testing subject to device availability. |
| Chrome for Android | Latest stable version | Responsive access for supported workflows. |
| Safari on iOS/iPadOS | Current supported iOS/iPadOS versions | Responsive access for supported workflows. |
| Internet Explorer | Not supported | Modern accessibility/security features are not supported in IE. |

# 7. Functional Requirements

## 7.1 Authentication, User Access and Security

This module controls who can enter the portal, what pillar they can access and which screens/actions they can use.

|  |  |
| --- | --- |
| **Item** | **Details** |
| Primary Screen(s) | Login / Role Landing; Password Management; Profile; Preferences |
| Initiating Actor | All internal users; temporary contributors for request-linked setup |
| Process Overview | User enters credentials or opens a request-linked setup page. The system checks the user, password policy, account status, role, pillar/workstream access and permission. Successful login redirects to the allowed dashboard. Failed attempts show safe messages and are logged. MFA verification shall be enforced for Super Admin, Admin, Reviewer, Approver, Publisher and other privileged users or workflow roles as configured by MoSPI. |
| Notifications / Scheduler / Reminder | Login failures, password reset and account lock events generate application audit records. Password reset or OTP flows use email notification where configured. |

|  |  |  |
| --- | --- | --- |
| **Sl.no** | **Sub Module** | **Functionality** |
| 1 | Login | Credential entry, required-field validation, safe error message and dashboard redirect. |
| 2 | Role landing | Load user roles, pages, permissions and pillar/workstream scope. |
| 3 | Password | Forgot password, first login, change password, expiry and lockout policy. |
| 4 | Profile/preferences | User language, notification preference and accessibility preference. |
| 5 | Audit/session | Login audit, logout, timeout and user action audit. |
| 6 | MFA for privileged users | Second-factor verification for Super Admin, Admin, Reviewer, Approver, Publisher and other privileged users/workflow roles as per MoSPI security policy. |

|  |  |
| --- | --- |
| **Data Aspect** | **Detail** |
| Where Data Is Saved | auth.users, auth.roles, auth.permissions, auth.pillar, auth.auth\_sessions, auth.login\_audit |
| From Where Data Is Fetched | User profile, roles, permissions, language preference, session and audit data |
| Where Data Is Validated | Password hash, active/locked state, role mapping, pillar scope and permission. MFA challenge status for privileged users and approval/publishing roles. |

|  |  |
| --- | --- |
| **Screen Action ID** | **User Action** |
| SCR-AUTH-001 | Enter credentials |
| SCR-AUTH-002 | View safe error |
| SCR-AUTH-003 | Continue to role dashboard |
| SCR-AUTH-004 | Change password |
| SCR-AUTH-005 | Update preferences |
| SCR-AUTH-006 | Logout |
| SCR-AUTH-007 | Complete MFA challenge where required |

|  |  |  |
| --- | --- | --- |
| **Requirement ID** | **Functional Requirement** | **Acceptance Criteria** |
| FR-AUTH-001 | System shall validate username/email/contact and password before creating a session. | Valid user gets session and dashboard redirect; invalid user gets safe error. |
| FR-AUTH-002 | System shall apply role, permission and pillar/workstream scope on every protected page and API. | User cannot open pages or perform actions outside assigned permission. |
| FR-AUTH-003 | System shall support profile, preference, password reset/change and logout flows. | Preference changes persist; password policy failures are clearly shown. |
| FR-AUTH-004 | System shall enforce MFA for Super Admin, Admin, Reviewer, Approver, Publisher and other privileged users/workflow roles before granting access to protected administrative or approval/publishing functions. | Privileged user cannot access protected functions until MFA challenge is successfully completed and the event is audit logged. |

|  |  |
| --- | --- |
| **Business Rule ID** | **Business Rule** |
| BR-AUTH-001 | Blank credentials are rejected before server login. |
| BR-AUTH-002 | Inactive or locked user cannot login even if password is correct. |
| BR-AUTH-003 | Session expiry redirects to login without losing audit trail. |
| BR-AUTH-004 | Raw password values are never saved or logged. |
| BR-AUTH-005 | MFA is mandatory for Super Admin, Admin, Reviewer, Approver, Publisher and other privileged users/workflow roles unless MoSPI explicitly approves an exception. |

|  |  |
| --- | --- |
| **Post Condition ID** | **Post Condition** |
| POST-AUTH-001 | Successful login session exists. |
| POST-AUTH-002 | Login audit row is written. |
| POST-AUTH-003 | Failed attempt count/status is updated when login fails. |
| POST-AUTH-004 | MFA success/failure audit record is written for privileged login/workflow access. |

|  |  |
| --- | --- |
| **Test Scenario ID** | **Test Scenario** |
| TC-AUTH-001 | Login success by Super Admin. |
| TC-AUTH-002 | Wrong password safe error. |
| TC-AUTH-003 | Locked user blocked. |
| TC-AUTH-004 | User without permission cannot open protected route. |
| TC-AUTH-005 | Privileged user is challenged for MFA and blocked when MFA fails. |

## 7.2 Application Setup, Pillars and Workstreams

This module keeps the portal configurable for SDG, SWS/ ENV and BRICS.

|  |  |
| --- | --- |
| **Item** | **Details** |
| Primary Screen(s) | Application Setup / Branding; Pillar Selector |
| Initiating Actor | Super Admin; Pillar Admin for own Pillar only |
| Process Overview | Super Admin configures Pillar/workstream settings. Pillar Admin can manage only permitted settings for their own Pillar. Branding, public dashboard flag, default language and local asset placeholders are maintained here. |
| Notifications / Scheduler / Reminder | Important setup changes write audit events. Public dashboard enable/disable can notify configured admins. |

|  |  |  |
| --- | --- | --- |
| **Sl.no** | **Sub Module** | **Functionality** |
| 1 | Pillar setup | Maintain SDG, SWS, ENV and BRICS |
| 2 | Branding | Portal title, logo/banner placeholders and theme settings. |
| 3 | Public dashboard setting | Enable or disable public dashboard per Pillar/workstream. |
| 4 | Application preferences | Default language and common UI settings. |

|  |  |
| --- | --- |
| **Data Aspect** | **Detail** |
| Where Data Is Saved | auth.pillar, and application configuration records |
| From Where Data Is Fetched | Pillar/workstream setup, branding, public dashboard flag and theme tokens |
| Where Data Is Validated | Pillar scope, allowed file placeholder type and admin permission. |

|  |  |
| --- | --- |
| **Screen Action ID** | **User Action** |
| SCR-APP-001 | Select Pillar |
| SCR-APP-002 | Update branding |
| SCR-APP-003 | Toggle public dashboard |
| SCR-APP-004 | Save settings |
| SCR-APP-005 | Reset to approved default |

|  |  |  |
| --- | --- | --- |
| **Requirement ID** | **Functional Requirement** | **Acceptance Criteria** |
| FR-APP-001 | System shall maintain SDG, SWS, ENV, BRICS pillar settings | Each pillar setting opens separately and one pillar cannot overwrite another. |
| FR-APP-002 | System shall store portal title, logo/banner placeholders, theme tokens and default language. | Saved settings reload on the setup page. |
| FR-APP-003 | System shall control public dashboard access by pillar/workstream. | Public dashboard is visible only when enabled. |

|  |  |
| --- | --- |
| **Business Rule ID** | **Business Rule** |
| BR-APP-001 | Pillar code is mandatory. |
| BR-APP-002 | Pillar Admin cannot update another pillar. |
| BR-APP-003 | File placeholders must not expose local server secrets. |

|  |  |
| --- | --- |
| **Post Condition ID** | **Post Condition** |
| POST-APP-001 | Settings are saved. |
| POST-APP-002 | Audit trail is written. |
| POST-APP-003 | Public dashboard status is refreshed. |

|  |  |
| --- | --- |
| **Test Scenario ID** | **Test Scenario** |
| TC-APP-001 | Save SDG/ SWS/ BRICS/ ENV. |
| TC-APP-002 | Pillar Admin tries cross-pillar update and is blocked. |
| TC-APP-003 | Public dashboard toggle changes visibility. |

## 7.3 Reference Masters

Masters are controlled lists used by the rest of the portal: locales, organizations, officers, periodicities, measures and units.

|  |  |
| --- | --- |
| **Item** | **Details** |
| Primary Screen(s) | Reference Masters |
| Initiating Actor | Super Admin; Pillar Admin; Metadata Officer |
| Process Overview | User opens the relevant master tab, searches records, opens add/edit modal, saves valid record or deactivates a record where references exist. |
| Notifications / Scheduler / Reminder | Master updates normally create audit records. Notifications are required only if a master change affects active request/template readiness. |

|  |  |  |
| --- | --- | --- |
| **Sl.no** | **Sub Module** | **Functionality** |
| 1 | Locale Master | English/Hindi local references. |
| 2 | Organization Master | Ministry, department, division and source organization hierarchy. |
| 3 | Officer Master | Officer/contact details and organization mapping. |
| 4 | Periodicity Master | Annual/quarter/month/frequency setup. |
| 5 | Measure and Unit Master | Measure, unit, datatype, decimal and validation defaults. |

|  |  |
| --- | --- |
| **Data Aspect** | **Detail** |
| Where Data Is Saved | metadata.locales, metadata.indicator\_periodicities, metadata.indicator\_measures, org.organizations, org.officers |
| From Where Data Is Fetched | Master records used by indicators, templates, requests and dashboards |
| Where Data Is Validated | Duplicate code, parent organization, active status and required labels. |

|  |  |
| --- | --- |
| **Screen Action ID** | **User Action** |
| SCR-MST-001 | Open master tab |
| SCR-MST-002 | Search/filter/sort |
| SCR-MST-003 | Add/edit modal |
| SCR-MST-004 | Deactivate |
| SCR-MST-005 | View dependency note |

|  |  |  |
| --- | --- | --- |
| **Requirement ID** | **Functional Requirement** | **Acceptance Criteria** |
| FR-MST-001 | System shall manage Locale Master for English/Hindi display. | Locales can be listed, activated and used by labels/messages. |
| FR-MST-002 | System shall manage Organization and Officer Masters for ministry, department, division and source contacts. | Officer can be linked to organization and later used in source assignment/request. |
| FR-MST-003 | System shall manage Periodicity, Measure and Unit of Measure Masters. | Templates and indicators can reuse active measures/units/periodicities. |

|  |  |
| --- | --- |
| **Business Rule ID** | **Business Rule** |
| BR-MST-001 | Stable codes must be unique. |
| BR-MST-002 | Referenced records should be deactivated, not hard deleted. |
| BR-MST-003 | Officer must belong to an organization. |

|  |  |
| --- | --- |
| **Post Condition ID** | **Post Condition** |
| POST-MST-001 | Master appears in dropdown/search. |
| POST-MST-002 | Dependent screens use updated active records. |
| POST-MST-003 | Audit is available. |

|  |  |
| --- | --- |
| **Test Scenario ID** | **Test Scenario** |
| TC-MST-001 | Create organization hierarchy. |
| TC-MST-002 | Create officer under division. |
| TC-MST-003 | Duplicate measure code rejected. |
| TC-MST-004 | Inactive measure hidden from template creation. |

## 7.4 Framework Setup and Hierarchy

A framework is the approved structure used to arrange indicators. It may have levels such as Goal and Target, but level names are dynamic and configurable.

|  |  |
| --- | --- |
| **Item** | **Details** |
| Primary Screen(s) | Framework Setup; Framework Hierarchy Builder |
| Initiating Actor | Super Admin; Pillar Admin; Metadata Officer |
| Process Overview | User selects pillar/workstream, creates framework edition, creates hierarchy levels, creates root/child nodes, links parent-child nodes and maps indicators to allowed levels. |
| Notifications / Scheduler / Reminder | Framework publish/archive events can notify metadata and template teams through application notification and email if configured. |

|  |  |  |
| --- | --- | --- |
| **Sl.no** | **Sub Module** | **Functionality** |
| 1 | Framework edition | Create draft/active/archive framework edition by pillar. |
| 2 | Hierarchy levels | Create dynamic levels such as Goal, Target, Theme or Chapter. |
| 3 | Framework nodes | Create root and child nodes. |
| 4 | Node relationships | Maintain parent-child hierarchy and depth. |
| 5 | Indicator mapping | Map indicator to allowed framework node. |

|  |  |
| --- | --- |
| **Data Aspect** | **Detail** |
| Where Data Is Saved | metadata.framework\_editions, metadata.framework\_hierarchy\_levels, metadata.framework\_nodes, metadata.framework\_node\_relationships, metadata.framework\_indicator\_mappings |
| From Where Data Is Fetched | Framework tree and indicator placement |
| Where Data Is Validated | One active edition rule, valid parent-child relation and allowed indicator mapping level. |

|  |  |
| --- | --- |
| **Screen Action ID** | **User Action** |
| SCR-FRM-001 | Select pillar |
| SCR-FRM-002 | Create edition |
| SCR-FRM-003 | Create level |
| SCR-FRM-004 | Add root node |
| SCR-FRM-005 | Add child node |
| SCR-FRM-006 | Map indicator |
| SCR-FRM-007 | Publish/archive |

|  |  |  |
| --- | --- | --- |
| **Requirement ID** | **Functional Requirement** | **Acceptance Criteria** |
| FR-FRM-001 | System shall create and maintain framework editions by pillar/workstream. | Draft/Active/Archived statuses are visible and searchable. |
| FR-FRM-002 | System shall support dynamic hierarchy levels and parent-child node mapping. | Root and child nodes display correctly in hierarchy tree with depth. |
| FR-FRM-003 | System shall map indicators to framework nodes where the level allows indicator mapping. | Mapped indicator appears under selected node and dashboard drilldown. |

|  |  |
| --- | --- |
| **Business Rule ID** | **Business Rule** |
| BR-FRM-001 | Only one active edition per framework/pillar unless governance approves otherwise. |
| BR-FRM-002 | Child node cannot be linked to invalid parent. |
| BR-FRM-003 | Indicator mapping must use active indicator/version. |

|  |  |
| --- | --- |
| **Post Condition ID** | **Post Condition** |
| POST-FRM-001 | Framework tree updates. |
| POST-FRM-002 | Indicator mapping is available for request/dashboard. |
| POST-FRM-003 | Publish/archive audit is written. |

|  |  |
| --- | --- |
| **Test Scenario ID** | **Test Scenario** |
| TC-FRM-001 | Create root node. |
| TC-FRM-002 | Create child under selected parent. |
| TC-FRM-003 | Search hierarchy tree. |
| TC-FRM-004 | Map indicator to target-level node. |

## 7.5 Indicator Management and Source Mapping

This module defines national indicators, global mappings, metadata, versions, measures, formulas and one or more source assignments.

|  |  |
| --- | --- |
| **Item** | **Details** |
| Primary Screen(s) | Indicator Management |
| Initiating Actor | Metadata Officer; Pillar Admin |
| Process Overview | User creates indicator with minimum information, maps it to framework node and global indicator, creates active version(without mapping with indicator), adds metadata/measures/periodicity and maps one or more source organizations/officers. |
| Notifications / Scheduler / Reminder | Indicator readiness changes can notify template/request users. Source assignment changes can notify affected source officers where configured. |

|  |  |  |
| --- | --- | --- |
| **Sl.no** | **Sub Module** | **Functionality** |
| 1 | National indicators | Create and maintain national indicator records. |
| 2 | Global indicators | Create/maintain global indicator reference. |
| 3 | Mappings | Map national to global indicator and framework node.(even without mapping with indicator/ data table) |
| 4 | Versions | Maintain active/retired indicator versions. |
| 5 | Metadata | Reference period, source note, computation text and availability. |
| 6 | Measures | Multiple measures with different unit/datatype. |
| 7 | Sources | Multiple source organizations/officers per indicator. |
| 8 | Framework | Map Chapter with Data Table |

|  |  |
| --- | --- |
| **Data Aspect** | **Detail** |
| Where Data Is Saved | metadata.national\_indicators, metadata.global\_indicators, metadata.indicator\_versions, metadata.indicator\_metadata\_details, metadata.indicator\_measures, metadata.national\_global\_indicator\_mappings, org.indicator\_source\_assignments |
| From Where Data Is Fetched | Indicator setup, mappings, measures and source assignment |
| Where Data Is Validated | Stable indicator code, active version, source validity and measure/unit rules. |

|  |  |
| --- | --- |
| **Screen Action ID** | **User Action** |
| SCR-IND-001 | Create indicator |
| SCR-IND-002 | Open detail modal |
| SCR-IND-003 | Map framework node(even without indicator mapping) |
| SCR-IND-004 | Map global indicator |
| SCR-IND-005 | Add source |
| SCR-IND-006 | Add measure |
| SCR-IND-007 | Update metadata |

|  |  |  |
| --- | --- | --- |
| **Requirement ID** | **Functional Requirement** | **Acceptance Criteria** |
| FR-IND-001 | System shall create/update national and global indicators with localized labels. | Indicator detail shows overview, versions, measures, metadata, global mapping and sources. |
| FR-IND-002 | System shall map one national indicator to global indicator and framework node. | Mapping appears in detail and framework drilldown. |
| FR-IND-003 | System shall support multiple source assignments for one indicator. | Each source can be tracked separately through request/submission/finalized data. |

|  |  |
| --- | --- |
| **Business Rule ID** | **Business Rule** |
| BR-IND-001 | Indicator code is stable. |
| BR-IND-002 | Active version is required before template/request readiness. |
| BR-IND-003 | Source assignment must have organization and validity period. |

|  |  |
| --- | --- |
| **Post Condition ID** | **Post Condition** |
| POST-IND-001 | Indicator is available for template creation(even without indicator mapping) |
| POST-IND-002 | Sources are available for request assignment. |
| POST-IND-003 | Version history is maintained. |

|  |  |
| --- | --- |
| **Test Scenario ID** | **Test Scenario** |
| TC-IND-001 | Create indicator. |
| TC-IND-002 | Add two source assignments. |
| TC-IND-003 | Map global indicator. |
| TC-IND-004 | Retire old version and keep history. |

## 7.6 Dimension Management

Dimensions define how data is broken down, for example geography, time, area type and gender. Users can also create additional dimensions.

|  |  |
| --- | --- |
| **Item** | **Details** |
| Primary Screen(s) | Dimension Management |
| Initiating Actor | Metadata Officer; Pillar Admin |
| Process Overview | User creates dimension definition, adds root member, adds child members, defines relationships, creates member sets, bulk uploads members if needed and defines rollup rules such as Total from Rural + Urban. |
| Notifications / Scheduler / Reminder | Dimension changes affecting active templates can notify template owners as readiness warning. |

|  |  |  |
| --- | --- | --- |
| **Sl.no** | **Sub Module** | **Functionality** |
| 1 | Dimension definitions | Create any dimension, not only fixed geography/time/area/gender. |
| 2 | Dimension members | Create root and child members with editable codes. |
| 3 | Hierarchy browser | Traverse parent-child member tree. |
| 4 | Member sets | Reusable member groups for template/request scope. |
| 5 | Rollup rules | Parent total can be manual, derived or manual-with-validation. |
| 6 | Bulk upload | Download format and upload members with examples. |

|  |  |
| --- | --- |
| **Data Aspect** | **Detail** |
| Where Data Is Saved | dimensions.dimension\_definitions, dimensions.dimension\_members, dimensions.dimension\_member\_relationships, dimensions.dimension\_member\_sets, dimensions.dimension\_member\_set\_items, dimensions.dimension\_member\_rollup\_rules |
| From Where Data Is Fetched | Dimension tree, member sets and rollup behavior |
| Where Data Is Validated | Unique member code, valid parent, depth and rollup child membership. |

|  |  |
| --- | --- |
| **Screen Action ID** | **User Action** |
| SCR-DIM-001 | Create dimension |
| SCR-DIM-002 | Add root |
| SCR-DIM-003 | Add child |
| SCR-DIM-004 | Search tree |
| SCR-DIM-005 | Bulk upload |
| SCR-DIM-006 | Download format |
| SCR-DIM-007 | Create rollup |

|  |  |  |
| --- | --- | --- |
| **Requirement ID** | **Functional Requirement** | **Acceptance Criteria** |
| FR-DIM-001 | System shall create dynamic dimension definitions with editable code and labels. | New dimension appears in template designer binding dropdown. |
| FR-DIM-002 | System shall maintain member hierarchy and depth. | India -> State -> District tree is visible with parent-child relationship. |
| FR-DIM-003 | System shall support member sets, bulk upload format download and rollup rules. | Bulk upload validates and rollup rule is available to template/validation. |

|  |  |
| --- | --- |
| **Business Rule ID** | **Business Rule** |
| BR-DIM-001 | Member code is unique within dimension. |
| BR-DIM-002 | Child cannot be linked to missing parent. |
| BR-DIM-003 | Rollup rule must name parent, child members and entry mode. |

|  |  |
| --- | --- |
| **Post Condition ID** | **Post Condition** |
| POST-DIM-001 | Dimension tree is updated. |
| POST-DIM-002 | Template designer can bind active members. |
| POST-DIM-003 | Validation can use rollup rule. |

|  |  |
| --- | --- |
| **Test Scenario ID** | **Test Scenario** |
| TC-DIM-001 | Create geography root India. |
| TC-DIM-002 | Add state child. |
| TC-DIM-003 | Bulk upload members. |
| TC-DIM-004 | Create Total -> Rural/Urban rollup. |

## 7.7 Template Management and Excel-like Designer

Templates are governed Excel-like formats. The user sees a grid, but the system saves dimensions, measures, cell mappings and render options in database tables.

|  |  |
| --- | --- |
| **Item** | **Details** |
| Primary Screen(s) | Template List; Template Designer; JSON Preview |
| Initiating Actor | Template Officer; Pillar Admin |
| Process Overview | User creates draft by selecting or not selecting pillar and indicator, designs grid, binds dimensions/measures, sets header/editable/freeze/validation options, saves draft, reloads draft, previews JSON contract and publishes active version. Template structure, validation bindings and approved formats shall be confirmed by the concerned functional nodal officers before publication/active use. |
| Notifications / Scheduler / Reminder | Template published, template rejected by validation, or active template changed can notify request/data-entry owners. Draft save is not emailed unless configured. |

|  |  |  |
| --- | --- | --- |
| **Sl.no** | **Sub Module** | **Functionality** |
| 1 | Template list | List templates by pillar, indicator, source, status and active version. |
| 2 | Draft creation | Create template draft for selected indicator. |
| 3 | Excel-like designer | Bind rows, columns, headers, measures and validation options. |
| 4 | JSON/render contract | Preview contract used by data entry and Excel upload. |
| 5 | Draft readback | Reload saved draft exactly on canvas. |
| 6 | Publish active | Publish validated template version. |

|  |  |
| --- | --- |
| **Data Aspect** | **Detail** |
| Where Data Is Saved | templates.template\_definitions, template\_versions, template\_axes, template\_axis\_members, template\_measures, template\_binding\_groups, template\_cells, template\_cell\_axis\_members, template\_render\_elements |
| From Where Data Is Fetched | Template contract, designer layout and generated data-entry cell mapping |
| Where Data Is Validated | Valid dimensions/members/measures, no duplicate binding under same scope, published version status. |

|  |  |
| --- | --- |
| **Screen Action ID** | **User Action** |
| SCR-TPL-001 | Search template |
| SCR-TPL-002 | Create draft |
| SCR-TPL-003 | Bind dimension |
| SCR-TPL-004 | Bind measure |
| SCR-TPL-005 | Merge/unmerge |
| SCR-TPL-006 | Save draft |
| SCR-TPL-007 | Preview JSON |
| SCR-TPL-008 | Publish |

|  |  |  |
| --- | --- | --- |
| **Requirement ID** | **Functional Requirement** | **Acceptance Criteria** |
| FR-TPL-001 | System shall list templates with indicator, source, active version, Subject and status. | User can search, view, edit draft/published and see mapped indicator. |
| FR-TPL-002 | System shall save and reload designer draft with binding groups, axes, members, measures, cells and render elements. | Opening edit shows the same Excel canvas design. |
| FR-TPL-003 | System shall publish active template only after contract validation. | Published version is available for request/data entry and old version remains in history. |

|  |  |
| --- | --- |
| **Business Rule ID** | **Business Rule** |
| BR-TPL-001 | Published template is not overwritten directly. |
| BR-TPL-002 | Each data-entry cell maps to axis tuple plus measure. |
| BR-TPL-003 | Access/public/shared option is deferred unless separately governed. |

|  |  |
| --- | --- |
| **Post Condition ID** | **Post Condition** |
| POST-TPL-001 | Draft or active version exists. |
| POST-TPL-002 | Render contract can be fetched. |
| POST-TPL-003 | Data-entry cell binding is generated. |

|  |  |
| --- | --- |
| **Test Scenario ID** | **Test Scenario** |
| TC-TPL-001 | Save draft then reload. |
| TC-TPL-002 | Bind geography/time/area/gender/measure. |
| TC-TPL-003 | Unbind group safely. |
| TC-TPL-004 | Publish active version. |

## 7.8 Collection Requests and Assignment

A request assigns data collection work to the correct source organization/officer for a template and indicator.

|  |  |
| --- | --- |
| **Item** | **Details** |
| Primary Screen(s) | Collection Request Creation |
| Initiating Actor | Pillar Admin; Data Collection Officer |
| Process Overview | User creates request draft, adds item/template instance, selects scope members, assigns officer, adds To/CC email recipients, sends request and tracks status events. |
| Notifications / Scheduler / Reminder | On send, system creates email outbox and notification log records for To/CC recipients. Reminders and escalation are configurable based on due date and status. |

|  |  |  |
| --- | --- | --- |
| **Sl.no** | **Sub Module** | **Functionality** |
| 1 | Collection cycle | Reporting cycle and due window. |
| 2 | Request header | Source organization/officer, due date, priority and status. |
| 3 | Request item | Indicator/template instance item. |
| 4 | Scope members | Requested dimension members/year/source scope. |
| 5 | Assignments | Data provider/reviewer responsibility. |
| 6 | Email recipients | To and CC recipient collections. |
| 7 | Status trail | Append-only request events. |

|  |  |
| --- | --- |
| **Data Aspect** | **Detail** |
| Where Data Is Saved | requests.collection\_cycles, collection\_requests, collection\_request\_items, collection\_request\_scope\_members, template\_instances, request\_assignments, request\_status\_events, invitation\_access.notification\_outbox |
| From Where Data Is Fetched | Request, items, assignments, scope and communication status |
| Where Data Is Validated | Active template, source/officer validity, scope member belongs to template/dimension. |

|  |  |
| --- | --- |
| **Screen Action ID** | **User Action** |
| SCR-REQ-001 | Create request |
| SCR-REQ-002 | Add item |
| SCR-REQ-003 | Select template |
| SCR-REQ-004 | Add scope |
| SCR-REQ-005 | Assign officer |
| SCR-REQ-006 | Add To/CC |
| SCR-REQ-007 | Send request |
| SCR-REQ-008 | Open detail modal |

|  |  |  |
| --- | --- | --- |
| **Requirement ID** | **Functional Requirement** | **Acceptance Criteria** |
| FR-REQ-001 | System shall create/update request draft, item, scope and assignment. | Request detail modal shows collection detail, item/scope, assignment and status trail. |
| FR-REQ-002 | System shall support To and CC recipient collections for request communication. | Multiple recipients are stored and delivery status is tracked. |
| FR-REQ-003 | System shall generate status events for draft/sent/opened/submitted/validated/reviewed/published flow. | Status trail is visible without exposing tokens. |

|  |  |
| --- | --- |
| **Business Rule ID** | **Business Rule** |
| BR-REQ-001 | Active template is required. |
| BR-REQ-002 | Scope member must fit template/dimension. |
| BR-REQ-003 | Assignment officer must belong to source organization. |

|  |  |
| --- | --- |
| **Post Condition ID** | **Post Condition** |
| POST-REQ-001 | Request is sent or saved as draft. |
| POST-REQ-002 | Notification outbox rows exist. |
| POST-REQ-003 | Invitation can be generated if required. |

|  |  |
| --- | --- |
| **Test Scenario ID** | **Test Scenario** |
| TC-REQ-001 | Create request with two items. |
| TC-REQ-002 | Add To and CC recipients. |
| TC-REQ-003 | Send request and see notification status. |
| TC-REQ-004 | Invalid scope rejected. |

## 7.9 Invitation Access and Temporary Contributor

This module lets request-linked external contributors access only their assigned data entry page through a temporary link.

|  |  |
| --- | --- |
| **Item** | **Details** |
| Primary Screen(s) | Invitation Access Monitor; Temporary Contributor Setup |
| Initiating Actor | System; Data Provider; Pillar Admin |
| Process Overview | System generates invitation for assignment, stores hash-only token metadata, sends setup link by email and tracks first open, setup completed, revoked/expired state and audit events. |
| Notifications / Scheduler / Reminder | Invitation generated, resent, revoked, expired and first-open events create email delivery and notification log records. Raw link is shown only at generation time if policy allows. |

|  |  |  |
| --- | --- | --- |
| **Sl.no** | **Sub Module** | **Functionality** |
| 1 | Invitation generation | Generate request-linked setup/access link. |
| 2 | Hash-only token metadata | Store hash and expiry, not raw token. |
| 3 | Invitation monitor | Track generated/sent/opened/setup/revoked/expired. |
| 4 | Audit trail | View invitation events. |
| 5 | Resend/revoke | Governed resend/revoke visual/admin actions. |

|  |  |
| --- | --- |
| **Data Aspect** | **Detail** |
| Where Data Is Saved | invitation\_access.external\_contributor\_invitations, invitation\_setup\_tokens, invitation\_events, notification\_outbox |
| From Where Data Is Fetched | Invitation status, token metadata and delivery event |
| Where Data Is Validated | Assignment link, expiry, status and token secrecy. |

|  |  |
| --- | --- |
| **Screen Action ID** | **User Action** |
| SCR-INV-001 | Generate invitation |
| SCR-INV-002 | View monitor |
| SCR-INV-003 | Open detail |
| SCR-INV-004 | Resend |
| SCR-INV-005 | Revoke |
| SCR-INV-006 | Check first-open |

|  |  |  |
| --- | --- | --- |
| **Requirement ID** | **Functional Requirement** | **Acceptance Criteria** |
| FR-INV-001 | System shall generate request-linked one-time setup link without storing raw token. | Normal read APIs show status only, never token/hash. |
| FR-INV-002 | System shall monitor invitation status and audit trail. | Detail modal shows request, assignment, officer, expiry, first opened and setup completed. |
| FR-INV-003 | System shall support visual/admin actions for resend/revoke/copy immediate link where governed. | Status event is written for each action. |

|  |  |
| --- | --- |
| **Business Rule ID** | **Business Rule** |
| BR-INV-001 | Expired/revoked link cannot open data entry. |
| BR-INV-002 | Invitation is tied to one or more assignment. |
| BR-INV-003 | Token hash is never displayed. |

|  |  |
| --- | --- |
| **Post Condition ID** | **Post Condition** |
| POST-INV-001 | Invitation status updated. |
| POST-INV-002 | Email/outbox status available. |
| POST-INV-003 | Contributor can open only assigned template. |

|  |  |
| --- | --- |
| **Test Scenario ID** | **Test Scenario** |
| TC-INV-001 | Generate invitation. |
| TC-INV-002 | Open monitor. |
| TC-INV-003 | Expired link blocked. |
| TC-INV-004 | Raw token absent in normal readback. |

## 7.10 Data Entry, Excel Upload and Ingestion

This module receives values entered in the template or uploaded in Excel and converts them to staged records.

|  |  |
| --- | --- |
| **Item** | **Details** |
| Primary Screen(s) | Department Data Entry; Ingestion Readback |
| Initiating Actor | Data Provider; Ingestion Admin; System |
| Process Overview | Data provider opens assigned template, enters values, edits allowed year headers, adds comments/notes, saves draft, validates preview and submits. System creates submission/version/manifest/job/run/events and staged records with dimension tuple and measure. Scanned or non-machine-readable submissions shall be stored as source artifacts and shall be converted only through manual entry, template-based resubmission or clarification workflow; they shall not be treated as validated data until structured and approved. |
| Notifications / Scheduler / Reminder | Draft saved is application-level only. Submit creates email notification and notification log records for validator/reviewer where configured. Failed ingestion creates operations alert. |

|  |  |  |
| --- | --- | --- |
| **Sl.no** | **Sub Module** | **Functionality** |
| 1 | Portal data entry | Fill governed template values. |
| 2 | Excel upload/ PDF/ Word | Upload approved sample format. |
| 3 | Draft/resume | Save and resume work. |
| 4 | Submission version | Each submit creates version. |
| 5 | Manifest | File/payload reference without exposing raw payload. |
| 6 | Staged records | Structured rows by cell, dimensions and measure. |
| 7 | Import history | View accepted/rejected/warning summary. |
| 8 | Non-machine-readable source handling | Preserve scanned/non-machine-readable submissions as source artifacts and route them through manual entry, resubmission or clarification workflow. |

|  |  |
| --- | --- |
| **Data Aspect** | **Detail** |
| Where Data Is Saved | ingestion.submissions, submission\_versions, payload\_manifests, ingestion\_jobs, ingestion\_runs, staged\_record\_index, staged\_record\_dimensions, ingestion\_events |
| From Where Data Is Fetched | Submission, file reference, staged rows and events |
| Where Data Is Validated | Template cell mapping, datatype, duplicate year/header and allowed editable scope. |

|  |  |
| --- | --- |
| **Screen Action ID** | **User Action** |
| SCR-ING-001 | Open assignment |
| SCR-ING-002 | Enter value |
| SCR-ING-003 | Add comment |
| SCR-ING-004 | Save draft |
| SCR-ING-005 | Upload Excel/ PDF/ Word |
| SCR-ING-006 | Validate preview |
| SCR-ING-007 | Submit |
| SCR-ING-008 | View ingestion readback |

|  |  |  |
| --- | --- | --- |
| **Requirement ID** | **Functional Requirement** | **Acceptance Criteria** |
| FR-ING-001 | System shall render data-entry template from published template contract. | Only editable value/year cells can be edited. |
| FR-ING-002 | System shall support portal data entry and Excel upload, with sample format, duplicate detection, validation summary and rejected record download. | Upload result shows accepted/rejected/warning counts and history. |
| FR-ING-003 | System shall stage values with exact axis tuple and measure code. | Each staged record can be traced to request, template cell, dimensions and measure. |
| FR-ING-004 | System shall preserve scanned or non-machine-readable submissions as source artifacts and shall support manual entry, template-based resubmission or clarification workflow for conversion into structured data; OCR is not included in Phase I unless separately approved by MoSPI. | Non-machine-readable source files are stored and traceable, but are not treated as validated data until structured, validated and approved through the configured workflow. |
| FR-ING-005 | System shall support collection of ministry submissions received through email attachments, Word documents, email body text, URLs, website links, system generated PDF, supporting images/charts and approved document formats. | System supports capture of ministry submission source records in supported formats. |
| FR-ING-006 | System shall support API-based data ingestion from approved ministry and department systems where APIs are available. | API-based data ingestion is supported for approved source systems. |

|  |  |
| --- | --- |
| **Business Rule ID** | **Business Rule** |
| BR-ING-001 | Raw payload and source hash are not shown in normal screens. |
| BR-ING-002 | Duplicate year/header is warned or rejected as configured. |
| BR-ING-003 | Submitted version does not overwrite earlier version. |
| BR-ING-004 | Scanned/non-machine-readable submissions are source artifacts only and shall not be used for publication or dashboard output until converted to structured data and approved. |

|  |  |
| --- | --- |
| **Post Condition ID** | **Post Condition** |
| POST-ING-001 | Submission version exists. |
| POST-ING-002 | Manifest and staged records exist. |
| POST-ING-003 | Validation can run. |
| POST-ING-004 | Source artifact is linked to submission, manual entry/resubmission or clarification record. |

|  |  |
| --- | --- |
| **Test Scenario ID** | **Test Scenario** |
| TC-ING-001 | Fill numeric cell. |
| TC-ING-002 | Add allowed year. |
| TC-ING-003 | Upload Excel with bad row/column and download rejected records. |
| TC-ING-004 | Submit creates staged records. |
| TC-ING-005 | Upload a scanned/non-machine-readable source artifact and verify it is retained for audit but excluded from validated data until structured and approved. |

## 7.11 Validation Rule Execution and Report

Validation checks submitted/staged data before review.

|  |  |
| --- | --- |
| **Item** | **Details** |
| Primary Screen(s) | Validation Queue; Validation Report |
| Initiating Actor | Validator; System |
| Process Overview | Validator opens queue, selects indicator/submission, views goal-target-indicator context, runs or reads validation result, checks errors/warnings/comparison and sends back or forwards to review. Validation rule catalogue and thresholds shall be based on inputs approved by functional nodal officers. |
| Notifications / Scheduler / Reminder | Validation complete, validation failed and send-back events create email notifications and notification log records for data provider/reviewer where configured. |

|  |  |  |
| --- | --- | --- |
| **Sl.no** | **Sub Module** | **Functionality** |
| 1 | Validation queue | Submitted items waiting for validation. |
| 2 | Rule catalogue | Validation rules and bindings. |
| 3 | Validation run | Execute/read run for submission version. |
| 4 | Result detail | Record, rule, severity, message and affected cell. |
| 5 | Comparison | Previous approved comparison. |
| 6 | Send-back/forward | Move to data entry or review. |

|  |  |
| --- | --- |
| **Data Aspect** | **Detail** |
| Where Data Is Saved | validation.validation\_rules, validation\_rule\_bindings, validation\_runs, validation\_results, validation\_comparison\_results |
| From Where Data Is Fetched | Rules, runs, results and comparisons |
| Where Data Is Validated | Rule binding, staged record, severity, status and comparison reference. |

|  |  |
| --- | --- |
| **Screen Action ID** | **User Action** |
| SCR-VAL-001 | Open queue |
| SCR-VAL-002 | Open report |
| SCR-VAL-003 | View template/cell |
| SCR-VAL-004 | Run validation |
| SCR-VAL-005 | Send back |
| SCR-VAL-006 | Continue to review |

|  |  |  |
| --- | --- | --- |
| **Requirement ID** | **Functional Requirement** | **Acceptance Criteria** |
| FR-VAL-001 | System shall show validation queue by submitted request item. | Queue shows source, indicator, status, pending and failed counts. |
| FR-VAL-002 | System shall execute/read validation rules and show record-level errors/warnings. | Report shows selected record, rule, severity, status, message and affected cell. |
| FR-VAL-003 | System shall compare current value with previous approved value where available. | Comparison states reference/no reference/difference are shown. |

|  |  |
| --- | --- |
| **Business Rule ID** | **Business Rule** |
| BR-VAL-001 | Blocker/error rules prevent review forwarding unless resolved/overridden by approved policy. |
| BR-VAL-002 | Validation results must not expose raw payload. |
| BR-VAL-003 | Every run/result has status trail. |

|  |  |
| --- | --- |
| **Post Condition ID** | **Post Condition** |
| POST-VAL-001 | Validation run/results exist. |
| POST-VAL-002 | Review task can be created if pass/allowed. |
| POST-VAL-003 | Send-back comment is visible to data provider. |

|  |  |
| --- | --- |
| **Test Scenario ID** | **Test Scenario** |
| TC-VAL-001 | Run validation pass. |
| TC-VAL-002 | Missing numeric value produces error. |
| TC-VAL-003 | No previous reference returns clean status. |
| TC-VAL-004 | Send back sends notification. |

## 7.12 Review, Approval and Published Fact Creation

Reviewers take the decision on validated submissions. Final approval publishes approved facts.

|  |  |
| --- | --- |
| **Item** | **Details** |
| Primary Screen(s) | Review / Approval |
| Initiating Actor | Reviewer; Approver; Pillar Admin |
| Process Overview | Reviewer opens task, sees full request-data entry-ingestion-validation-review trail, compares previous approved data, records note and action. Terminal approval writes published snapshot and observations. |
| Notifications / Scheduler / Reminder | Task assigned, clarification requested, send-back, rejection, final approval and publish events create email notifications and notification log records as configured. |

|  |  |  |
| --- | --- | --- |
| **Sl.no** | **Sub Module** | **Functionality** |
| 1 | Task queue | Assigned reviewer tasks. |
| 2 | Review workspace | Request-data entry-ingestion-validation-review trail. |
| 3 | Action logs | Approve/reject/send back/clarify actions. |
| 4 | Approval logs | Review level decisions. |
| 5 | Previous approved data | Comparison with last approved facts. |
| 6 | Publish trigger | Final approval publishes facts. |

|  |  |
| --- | --- |
| **Data Aspect** | **Detail** |
| Where Data Is Saved | review.review\_tasks, review.review\_action\_logs, review.approval\_logs, published\_data.approved\_snapshots, approved\_observations |
| From Where Data Is Fetched | Review decisions and final publish output |
| Where Data Is Validated | Task status, terminal action, duplicate final approval guard and approved fact generation. |

|  |  |
| --- | --- |
| **Screen Action ID** | **User Action** |
| SCR-REV-001 | Open task |
| SCR-REV-002 | Review validation |
| SCR-REV-003 | Compare previous data |
| SCR-REV-004 | Add note |
| SCR-REV-005 | Approve |
| SCR-REV-006 | Reject |
| SCR-REV-007 | Send back |
| SCR-REV-008 | Request clarification |

|  |  |  |
| --- | --- | --- |
| **Requirement ID** | **Functional Requirement** | **Acceptance Criteria** |
| FR-REV-001 | System shall show review task queue and full context trail. | Reviewer can see request, source, template, validation and previous approved data. |
| FR-REV-002 | System shall support approve, reject, send-back and request-clarification actions with comments. | Action log and approval log are written. |
| FR-REV-003 | System shall prevent duplicate final approval and publish approved facts only once per approved action/snapshot rule. | Duplicate final approval is blocked or superseded as configured. |
| FR-REV-004 | System shall enforce Maker-Checker separation for review, approval, publishing and other configured governance workflows so that the maker/initiator and checker/approver roles remain distinct as per MoSPI-approved workflow rules. | A user who creates or submits a workflow item cannot approve the same item where Maker-Checker separation is configured; override, if any, requires configured authorization and audit justification. |

|  |  |
| --- | --- |
| **Business Rule ID** | **Business Rule** |
| BR-REV-001 | Terminal action requires comment where configured. |
| BR-REV-002 | Final approval requires valid validation context. |
| BR-REV-003 | Reviewer cannot change submitted values directly. |
| BR-REV-004 | Maker-Checker shall be enforced for review/approval workflows. The maker/initiator and checker/approver shall be separate users or roles wherever configured by MoSPI. |

|  |  |
| --- | --- |
| **Post Condition ID** | **Post Condition** |
| POST-REV-001 | Review task status updated. |
| POST-REV-002 | Approval/action log exists. |
| POST-REV-003 | Published snapshot/facts created after final approval. |
| POST-REV-004 | Maker-Checker validation result and approving user identity are stored in the workflow audit trail. |

|  |  |
| --- | --- |
| **Test Scenario ID** | **Test Scenario** |
| TC-REV-001 | Approve path publishes facts. |
| TC-REV-002 | Reject path records reason. |
| TC-REV-003 | Clarification sends notification. |
| TC-REV-004 | Duplicate final approval guard works. |
| TC-REV-005 | Maker user attempts to approve own submission and is blocked as per configured workflow rule. |

## 7.13 Published Data and Fact Store

This is the trusted final data store after approval.

|  |  |
| --- | --- |
| **Item** | **Details** |
| Primary Screen(s) | Published Snapshot Dashboard; Previous Approved Lookup |
| Initiating Actor | System; Pillar Admin; Dashboard User; Reviewer |
| Process Overview | Final approval creates approved snapshot and observation rows. Dashboards, comparison and publication workspace read latest approved observations. |
| Notifications / Scheduler / Reminder | Publish event can notify pillar admins, publication team and dashboard/report subscribers. |

|  |  |  |
| --- | --- | --- |
| **Sl.no** | **Sub Module** | **Functionality** |
| 1 | Approved snapshots | Final approval snapshot. |
| 2 | Approved observations | Fact values by indicator/measure/source/time/dimensions. |
| 3 | Observation dimensions | Dimension tuple for each value. |
| 4 | Latest view | Read latest active/superseded-aware value. |
| 5 | Previous approved lookup | Fetch previous value for validation/review comparison. |

|  |  |
| --- | --- |
| **Data Aspect** | **Detail** |
| Where Data Is Saved | published\_data.approved\_snapshots, approved\_observations, approved\_observation\_dimensions, v\_latest\_approved\_observation\_codes |
| From Where Data Is Fetched | Approved facts and latest lookup |
| Where Data Is Validated | Approval reference, snapshot status, dimension tuple and source/indicator/time filters. |

|  |  |
| --- | --- |
| **Screen Action ID** | **User Action** |
| SCR-PDATA-001 | Publish approval |
| SCR-PDATA-002 | View snapshot |
| SCR-PDATA-003 | Filter latest observations |
| SCR-PDATA-004 | Lookup previous approved |
| SCR-PDATA-005 | Open submitted snapshot dashboard |

|  |  |  |
| --- | --- | --- |
| **Requirement ID** | **Functional Requirement** | **Acceptance Criteria** |
| FR-PDATA-001 | System shall store approved snapshots and observations with dimension members. | Each approved value is traceable to snapshot, indicator, source, measure and dimensions. |
| FR-PDATA-002 | System shall support latest-observation lookup by pillar, indicator, time and source. | Dashboard and review comparison can fetch latest values. |
| FR-PDATA-003 | System shall manage duplicate publish/superseded snapshot behavior. | Latest view returns current active value and old snapshot remains auditable. |

|  |  |
| --- | --- |
| **Business Rule ID** | **Business Rule** |
| BR-PDATA-001 | Only approved review path can publish. |
| BR-PDATA-002 | Public views use approved data only. |
| BR-PDATA-003 | Internal IDs/source hashes are not exposed. |

|  |  |
| --- | --- |
| **Post Condition ID** | **Post Condition** |
| POST-PDATA-001 | Fact rows exist. |
| POST-PDATA-002 | Dashboard read models can refresh. |
| POST-PDATA-003 | Publication workspace can use approved data. |

|  |  |
| --- | --- |
| **Test Scenario ID** | **Test Scenario** |
| TC-PDATA-001 | Publish approval. |
| TC-PDATA-002 | Latest observation filter by year. |
| TC-PDATA-003 | Previous approved lookup found/not found. |
| TC-PDATA-004 | Superseded snapshot not shown as latest. |

## 7.14 Publication Management Workspace and PDF Designer

After facts are published, this module helps prepare official PDF publications.

|  |  |
| --- | --- |
| **Item** | **Details** |
| Primary Screen(s) | Publication Workspace; PDF Designer; Publication Review |
| Initiating Actor | Publication Officer; Reviewer; Approver |
| Process Overview | User creates workspace, reuses previous PDF layout, drags/resizes widgets on A4 pages, binds approved data, auto-saves draft, sends for review, receives approval and downloads final PDF. |
| Notifications / Scheduler / Reminder | Draft submitted, review assigned, approval, rejection, PDF generated and publication released events create email notifications and notification log records. |

|  |  |  |
| --- | --- | --- |
| **Sl.no** | **Sub Module** | **Functionality** |
| 1 | Workspace | Create publication workspace after facts are approved. |
| 2 | PDF designer | A4 page, drag/drop, resize and widgets. |
| 3 | Previous format reuse | Open previous publication layout with latest data. |
| 4 | Draft/version | Auto-save and version publication design. |
| 5 | Review/approval | Send publication draft for review. |
| 6 | PDF output | Generate/download approved PDF and link to DMS/CMS. |

|  |  |
| --- | --- |
| **Data Aspect** | **Detail** |
| Where Data Is Saved | Publication workspace/layout/version tables or CMS/DMS references in production scope |
| From Where Data Is Fetched | Publication layout, widgets, approved-data bindings, review status and generated file reference |
| Where Data Is Validated | Approved fact availability, widget mapping, review status and file generation result. |

|  |  |
| --- | --- |
| **Screen Action ID** | **User Action** |
| SCR-PUBWS-001 | Create workspace |
| SCR-PUBWS-002 | Reuse previous layout |
| SCR-PUBWS-003 | Drag widget |
| SCR-PUBWS-004 | Bind data |
| SCR-PUBWS-005 | Auto-save |
| SCR-PUBWS-006 | Submit review |
| SCR-PUBWS-007 | Approve PDF |
| SCR-PUBWS-008 | Download |

|  |  |  |
| --- | --- | --- |
| **Requirement ID** | **Functional Requirement** | **Acceptance Criteria** |
| FR-PUBWS-001 | System shall create publication workspace from approved data. | Workspace cannot be finalized without approved facts. |
| FR-PUBWS-002 | System shall provide no-code/low-code A4 PDF designer with reusable previous layout. | Widgets can be placed, resized, saved and versioned. |
| FR-PUBWS-003 | System shall support publication review, approval and final PDF download. Digital Signature and PDF Watermark are not included in Phase I unless separately approved. | Approved PDF is generated and version history is maintained. |
| FR-PUBWS-004 | System shall support tracking of publication progress across data collection, ingestion, drafting, review and publishing stages. | Publication progress is available across defined workflow stages. |

|  |  |
| --- | --- |
| **Business Rule ID** | **Business Rule** |
| BR-PUBWS-001 | Draft PDF carries draft watermark. |
| BR-PUBWS-002 | Official PDF requires approval. |
| BR-PUBWS-003 | Generated file reference is stored safely in DMS/file storage. |

|  |  |
| --- | --- |
| **Post Condition ID** | **Post Condition** |
| POST-PUBWS-001 | Publication version saved. |
| POST-PUBWS-002 | Approved PDF available. |
| POST-PUBWS-003 | CMS/DMS link can be published where permitted. |

|  |  |
| --- | --- |
| **Test Scenario ID** | **Test Scenario** |
| TC-PUBWS-001 | Create workspace from previous layout. |
| TC-PUBWS-002 | Auto-save draft. |
| TC-PUBWS-003 | Submit for review. |
| TC-PUBWS-004 | Approve and download PDF. |

## 7.15 Dashboards and Analytics Views

Dashboards show work status and approved statistical output.

|  |  |
| --- | --- |
| **Item** | **Details** |
| Primary Screen(s) | Super Admin Dashboard; Pillar Admin Dashboard; Submitted Snapshot Dashboard; Public Dashboard |
| Initiating Actor | Super Admin; Pillar Admin; Analyst; Public User where enabled |
| Process Overview | User opens dashboard, selects pillar/workstream, filters goal/target/indicator/source/time and drills into approved data or workflow status. The chart/visualization catalogue shall be finalized with functional owners during SRS/detailed design and configured only after MoSPI approval. |
| Notifications / Scheduler / Reminder | Dashboard reports can be scheduled and emailed to configured admins. Saved filter subscriptions can create scheduled report notifications. |

|  |  |  |
| --- | --- | --- |
| **Sl.no** | **Sub Module** | **Functionality** |
| 1 | Super Admin dashboard | Cross-pillar operations. |
| 2 | Pillar Admin dashboard | Pillar goal/target/indicator stats. |
| 3 | Submitted snapshot dashboard | Approved values and drilldown. |
| 4 | Public dashboard | Approved public view when enabled. |
| 5 | Saved filters/reports | Saved filters and scheduled email report. |
| 6 | Charts/maps | ECharts/D3 charts and Leaflet maps where needed. |

|  |  |
| --- | --- |
| **Data Aspect** | **Detail** |
| Where Data Is Saved | dashboard.v\_\* read models, published\_data approved facts, workflow summaries |
| From Where Data Is Fetched | Summary, drilldown, latest approved values and operational counts |
| Where Data Is Validated | Public flag, pillar scope, approved-only data and cache freshness. |

|  |  |
| --- | --- |
| **Screen Action ID** | **User Action** |
| SCR-DASH-001 | Open dashboard |
| SCR-DASH-002 | Filter unit/time/source |
| SCR-DASH-003 | Drill down goal/target/indicator |
| SCR-DASH-004 | View chart data table |
| SCR-DASH-005 | Schedule report |

|  |  |  |
| --- | --- | --- |
| **Requirement ID** | **Functional Requirement** | **Acceptance Criteria** |
| FR-DASH-001 | System shall show internal operational dashboards by role and pillar. | Cards/charts/drilldowns reflect user scope. |
| FR-DASH-002 | System shall show approved snapshot/dashboard values from published fact store. | Dashboard never shows unapproved staged data as final data. |
| FR-DASH-003 | System shall support saved filters, drill-through, performance cache and scheduled email reports. | Saved reports are generated and mailed to configured recipients. |
| FR-DASH-004 | System shall provide views for tracking data ingestion progress, including submission status, validation status and processing status. | Data ingestion progress status is available through dashboard views. |
| FR-DASH-005 | System shall allow users to select validated datasets, indicators and dimensions, apply multiple filters, and preview dataset structure and sample data. | Users can select datasets and preview dataset details. |
| FR-DASH-006 | System shall support pivot views, tabular views, multi-indicator comparison and cross-framework analysis. | Users can perform analytical comparison using available views. |

|  |  |
| --- | --- |
| **Business Rule ID** | **Business Rule** |
| BR-DASH-001 | Public dashboard requires pillar public flag. |
| BR-DASH-002 | Charts must have accessible data table alternative. |
| BR-DASH-003 | No data filters return clean empty result. |

|  |  |
| --- | --- |
| **Post Condition ID** | **Post Condition** |
| POST-DASH-001 | Dashboard renders latest data. |
| POST-DASH-002 | Report subscription/audit created where configured. |
| POST-DASH-003 | Public users see approved data only. |

|  |  |
| --- | --- |
| **Test Scenario ID** | **Test Scenario** |
| TC-DASH-001 | Pillar dashboard filter. |
| TC-DASH-002 | Public dashboard disabled blocked. |
| TC-DASH-003 | No-data returns empty list. |
| TC-DASH-004 | Email report schedule visible. |

## 7.16 Content Management System - Plone

CMS manages public portal pages, menus and bilingual content.

|  |  |
| --- | --- |
| **Item** | **Details** |
| Primary Screen(s) | CMS Content Admin; Public Pages |
| Initiating Actor | Content Admin; Super Admin; Public User |
| Process Overview | Content admin creates/edits page, adds SEO metadata/friendly URL/media, previews draft, schedules publish, rolls back if required and monitors page analytics. |
| Notifications / Scheduler / Reminder | Scheduled publish, broken link alert, page approval and report email events notify content admins. |

|  |  |  |
| --- | --- | --- |
| **Sl.no** | **Sub Module** | **Functionality** |
| 1 | Page CRUD | Create/edit/preview/publish/unpublish/archive pages. |
| 2 | Menu/navigation | Public portal navigation structure. |
| 3 | Bilingual content | English/Hindi page content with fallback. |
| 4 | SEO/friendly URL | Metadata, slug and link checks. |
| 5 | Analytics | Site/application analytics and reports. |

|  |  |
| --- | --- |
| **Data Aspect** | **Detail** |
| Where Data Is Saved | Plone CMS content store and portal integration references |
| From Where Data Is Fetched | Page content, language, status, URL, media references and analytics events |
| Where Data Is Validated | Approval status, slug uniqueness, language fallback and broken link checks. |

|  |  |
| --- | --- |
| **Screen Action ID** | **User Action** |
| SCR-CMS-001 | Create page |
| SCR-CMS-002 | Edit page |
| SCR-CMS-003 | Preview |
| SCR-CMS-004 | Schedule publish |
| SCR-CMS-005 | Rollback |
| SCR-CMS-006 | View analytics |

|  |  |  |
| --- | --- | --- |
| **Requirement ID** | **Functional Requirement** | **Acceptance Criteria** |
| FR-CMS-001 | System shall integrate with Plone for public page CRUD workflow. | Pages can be drafted, previewed, published, unpublished/archived. |
| FR-CMS-002 | System shall support bilingual content, SEO metadata, friendly URLs and media compression. | Public page renders in selected language with fallback. |
| FR-CMS-003 | System shall support analytics dashboard and configured email reports for site/application usage. | Admin can view/report public page usage. |
| FR-CMS-004 | System shall support management of website theme including colors, fonts, icons, UI styles and logo. System shall support preview of theme changes before publishing. | Theme configuration and preview functionality are available before publishing. |

|  |  |
| --- | --- |
| **Business Rule ID** | **Business Rule** |
| BR-CMS-001 | Public content must be approved before publish. |
| BR-CMS-002 | Fallback language shown when translation missing. |
| BR-CMS-003 | Broken links should be reported. |

|  |  |
| --- | --- |
| **Post Condition ID** | **Post Condition** |
| POST-CMS-001 | Page status updated. |
| POST-CMS-002 | Public URL available when published. |
| POST-CMS-003 | Analytics event captured. |

|  |  |
| --- | --- |
| **Test Scenario ID** | **Test Scenario** |
| TC-CMS-001 | Create page draft. |
| TC-CMS-002 | Schedule publish. |
| TC-CMS-003 | Rollback page. |
| TC-CMS-004 | View analytics report. |

## 7.17 Document Management System - ownCloud

DMS stores documents, evidence and generated publication files with access and retention.

|  |  |
| --- | --- |
| **Item** | **Details** |
| Primary Screen(s) | DMS Listing; Upload/Metadata; File Preview |
| Initiating Actor | Document Admin; Pillar Admin; Auditor |
| Process Overview | User uploads document, system checks file policy/virus-scan handoff, metadata is saved, access and retention are applied, users search/preview/download if allowed. |
| Notifications / Scheduler / Reminder | Document expiry, virus scan failure, review-needed and publication-file-ready events can notify owners/admins. |

|  |  |  |
| --- | --- | --- |
| **Sl.no** | **Sub Module** | **Functionality** |
| 1 | Upload | Upload internal/supporting documents. |
| 2 | Metadata | Classify document by pillar/module/type. |
| 3 | Versioning | Keep document versions. |
| 4 | Preview/search | File preview/search handled by ownCloud; OCR Search only if separately approved. |
| 5 | Retention | Expiry/archive policy. |
| 6 | Access control | Role/pillar-based document access. |

|  |  |
| --- | --- |
| **Data Aspect** | **Detail** |
| Where Data Is Saved | ownCloud file metadata and portal integration references |
| From Where Data Is Fetched | Document code, version, classification, retention and access mapping |
| Where Data Is Validated | File type/size, virus scan handoff, permission and retention policy. |

|  |  |
| --- | --- |
| **Screen Action ID** | **User Action** |
| SCR-DMS-001 | Upload document |
| SCR-DMS-002 | Edit metadata |
| SCR-DMS-003 | Preview |
| SCR-DMS-004 | Search |
| SCR-DMS-005 | Download |
| SCR-DMS-006 | Archive |

|  |  |  |
| --- | --- | --- |
| **Requirement ID** | **Functional Requirement** | **Acceptance Criteria** |
| FR-DMS-001 | System shall integrate with ownCloud for file storage and versioning. | Document version history is available. |
| FR-DMS-002 | System shall support metadata, classification, retention, expiry and ownCloud-based preview/search integration. OCR Search is not included in Phase I unless separately approved. | Authorized users can find and preview permitted documents. |
| FR-DMS-003 | System shall enforce access control and avoid exposing restricted files. | Unauthorized download is blocked and audited. |
| FR-DMS-004 | System shall support hierarchical folder and sub-folder creation and management for organizing documents. | System supports creation and management of document folders and sub-folders. |

|  |  |
| --- | --- |
| **Business Rule ID** | **Business Rule** |
| BR-DMS-001 | Unsupported file type/size is rejected. |
| BR-DMS-002 | Retention policy controls archive/expiry. |
| BR-DMS-003 | Sensitive file paths are not shown. |

|  |  |
| --- | --- |
| **Post Condition ID** | **Post Condition** |
| POST-DMS-001 | Document metadata saved. |
| POST-DMS-002 | File version visible. |
| POST-DMS-003 | Audit trail written. |

|  |  |
| --- | --- |
| **Test Scenario ID** | **Test Scenario** |
| TC-DMS-001 | Upload PDF/ Excel/ Word |
| TC-DMS-002 | Preview document. |
| TC-DMS-003 | Restricted user blocked. |
| TC-DMS-004 | Expired document archived. |

## 7.18 Notification Engine, Reminders and Schedulers

Notifications are a separate Phase I support service for email, notification logs, reminders, escalation and reports.

|  |  |
| --- | --- |
| **Item** | **Details** |
| Primary Screen(s) | Notifications; Reminders; Logs & Monitor |
| Initiating Actor | System; Admin; All users depending on event |
| Process Overview | Business modules create notification events. Notification service reads event/outbox, sends email where configured, retries failures and records delivery status. Stream/webhook style delivery is future technical extension. |
| Notifications / Scheduler / Reminder | This is the module that owns notification behavior for request, submission, validation, review, publication, dashboard reports and admin alerts. |

|  |  |  |
| --- | --- | --- |
| **Sl.no** | **Sub Module** | **Functionality** |
| 1 | Notification logs | Searchable event and delivery history. |
| 2 | Email | Request, OTP, reminder, escalation and reports. |
| 3 | Future stream events | Application-level workflow event stream as future technical extension. |
| 4 | Reminder scheduler | Due/overdue request reminders. |
| 5 | Retry queue | Retry failed notification deliveries. |
| 6 | Notification logs | Safe delivery audit. |

|  |  |
| --- | --- |
| **Data Aspect** | **Detail** |
| Where Data Is Saved | invitation\_access.notification\_outbox and notification service logs/outbox |
| From Where Data Is Fetched | Notification event, recipient, channel, delivery status and retry count |
| Where Data Is Validated | Recipient, template, channel, status and token masking. |

|  |  |
| --- | --- |
| **Screen Action ID** | **User Action** |
| SCR-NOTIF-001 | Open notifications |
| SCR-NOTIF-002 | Open reminders |
| SCR-NOTIF-003 | Filter events |
| SCR-NOTIF-004 | View delivery status |
| SCR-NOTIF-005 | Retry failed |
| SCR-NOTIF-006 | Schedule report |

|  |  |  |
| --- | --- | --- |
| **Requirement ID** | **Functional Requirement** | **Acceptance Criteria** |
| FR-NOTIF-001 | System shall create notification events for request sent, submission received, validation complete, review assigned, clarification, approval and publication. | Events appear in notification list and delivery logs. |
| FR-NOTIF-002 | System shall support email notifications and auditable notification logs in Phase I. | Configured recipient receives message and event is auditable. |
| FR-NOTIF-003 | System shall support reminder scheduler, escalation rules, retry queue and scheduled email reports. | Pending/overdue work generates reminders and failed delivery can retry. |

|  |  |
| --- | --- |
| **Business Rule ID** | **Business Rule** |
| BR-NOTIF-001 | No raw tokens in normal notification list. |
| BR-NOTIF-002 | Recipient To/CC must be validated. |
| BR-NOTIF-003 | Failed delivery remains auditable. |

|  |  |
| --- | --- |
| **Post Condition ID** | **Post Condition** |
| POST-NOTIF-001 | Outbox row created. |
| POST-NOTIF-002 | Delivery status updated. |
| POST-NOTIF-003 | User/admin can view safe notification detail. |

|  |  |
| --- | --- |
| **Test Scenario ID** | **Test Scenario** |
| TC-NOTIF-001 | Request sent email event. |
| TC-NOTIF-002 | Reminder due event. |
| TC-NOTIF-003 | Failed email retry status. |
| TC-NOTIF-004 | Notification popup shows safe text. |

## 7.19 Logs, Monitoring, Backup and Audit

This module gives operations and audit teams a safe view of system health, logs, backups and activity.

|  |  |
| --- | --- |
| **Item** | **Details** |
| Primary Screen(s) | Logs & Monitor; Audit Views |
| Initiating Actor | Super Admin; Auditor; Operations User |
| Process Overview | User opens monitor, sees API/DB/storage/notification/job status, searches logs/audit rows, opens safe details and checks backup/retention evidence. |
| Notifications / Scheduler / Reminder | Service down, backup failed, job failed and log threshold events can trigger admin notification/email. |

|  |  |  |
| --- | --- | --- |
| **Sl.no** | **Sub Module** | **Functionality** |
| 1 | Health | API, DB, storage and service status. |
| 2 | Logs | Search/filter operational logs. |
| 3 | Audit | User/action/workflow audit. |
| 4 | Backup | Backup/restore evidence. |
| 5 | Infrastructure | Docker/service/deployment monitor. |

|  |  |
| --- | --- |
| **Data Aspect** | **Detail** |
| Where Data Is Saved | application logs, audit logs, health checks, backup reports |
| From Where Data Is Fetched | Health status, audit events, backup state and safe log detail |
| Where Data Is Validated | Role access, retention window and sensitive field masking. |

|  |  |
| --- | --- |
| **Screen Action ID** | **User Action** |
| SCR-MON-001 | Open monitor |
| SCR-MON-002 | Filter logs |
| SCR-MON-003 | View audit detail |
| SCR-MON-004 | Check backup |
| SCR-MON-005 | View service health |

|  |  |  |
| --- | --- | --- |
| **Requirement ID** | **Functional Requirement** | **Acceptance Criteria** |
| FR-MON-001 | System shall show API, DB, storage, notification, ingestion and validation job status. | Monitor shows UP/DOWN/DEGRADED with timestamp. |
| FR-MON-002 | System shall provide searchable audit/log table with retention policy. | User can filter logs without seeing sensitive payloads. |
| FR-MON-003 | System shall show backup status and disaster-recovery drill evidence where configured. | Latest backup/restore status is visible. |
| FR-MON-004 | System shall support data lineage and traceability of datasets from submission through publication. | Authorized users can trace dataset flow from submission, validation, approval, and publication stages, including access to related source and published data references. |

|  |  |
| --- | --- |
| **Business Rule ID** | **Business Rule** |
| BR-MON-001 | Sensitive payload/token/hash is masked. |
| BR-MON-002 | Log retention follows policy. |
| BR-MON-003 | Only authorized auditor/admin can view logs. |

|  |  |
| --- | --- |
| **Post Condition ID** | **Post Condition** |
| POST-MON-001 | Health status visible. |
| POST-MON-002 | Audit detail opens safely. |
| POST-MON-003 | Operational issue can be followed up. |

|  |  |
| --- | --- |
| **Test Scenario ID** | **Test Scenario** |
| TC-MON-001 | Filter ERROR logs. |
| TC-MON-002 | Open audit detail. |
| TC-MON-003 | Sensitive token absent. |
| TC-MON-004 | Backup failed alert visible. |

## 7.20 Accessibility, Bilingual Support and Preferences

This is a cross-cutting requirement so the application is usable by Hindi/English users and persons with disabilities, including blind users.

|  |  |
| --- | --- |
| **Item** | **Details** |
| Primary Screen(s) | Accessibility Compliance; Preferences; all screens |
| Initiating Actor | All users |
| Process Overview | System loads language/accessibility preference, displays labels/messages in selected language with fallback and allows keyboard/screen-reader operation. |
| Notifications / Scheduler / Reminder | Preference changes are local/audit events. Accessibility warnings are tracked in test evidence rather than sent to users. |

|  |  |  |
| --- | --- | --- |
| **Sl.no** | **Sub Module** | **Functionality** |
| 1 | Language | English/Hindi switch and fallback. |
| 2 | Screen reader | Labels, roles and announcements. |
| 3 | Keyboard | Operate forms/tables/modals without mouse. |
| 4 | Accessible charts | Text/table alternative for charts. |
| 5 | Preferences | Save language/display/notification preference. |

|  |  |
| --- | --- |
| **Data Aspect** | **Detail** |
| Where Data Is Saved | auth.languages, locale/i18n tables and user preferences |
| From Where Data Is Fetched | Language labels, preference and accessibility evidence |
| Where Data Is Validated | Translation fallback, focus order, contrast and aria labels. |

|  |  |
| --- | --- |
| **Screen Action ID** | **User Action** |
| SCR-ACC-001 | Switch language |
| SCR-ACC-002 | Navigate keyboard-only |
| SCR-ACC-003 | Open modal |
| SCR-ACC-004 | Read chart as table |
| SCR-ACC-005 | Save preference |

|  |  |  |
| --- | --- | --- |
| **Requirement ID** | **Functional Requirement** | **Acceptance Criteria** |
| FR-ACC-001 | System shall support English and Hindi labels/messages with English fallback. | Language switch changes menus/messages where translations exist. |
| FR-ACC-002 | System shall support keyboard navigation, focus order, screen-reader labels and error announcements. | Blind users can complete main workflows using assistive technology. |
| FR-ACC-003 | System shall provide accessible charts/tables and avoid color-only status meaning. | Chart data is available as table/text and status has label. |
| FR-ACC-004 | System shall provide unified search across publications, dashboards, documents and portal pages using keywords. | Users can search required portal content across supported sections. |

|  |  |
| --- | --- |
| **Business Rule ID** | **Business Rule** |
| BR-ACC-001 | English default. |
| BR-ACC-002 | Missing Hindi label falls back to English. |
| BR-ACC-003 | Keyboard path must exist for modal/table/form actions. |

|  |  |
| --- | --- |
| **Post Condition ID** | **Post Condition** |
| POST-ACC-001 | Preference saved. |
| POST-ACC-002 | Screen renders with selected language/accessibility settings. |
| POST-ACC-003 | Accessibility evidence can be tested. |

|  |  |
| --- | --- |
| **Test Scenario ID** | **Test Scenario** |
| TC-ACC-001 | Keyboard-only data entry path. |
| TC-ACC-002 | Screen reader label check. |
| TC-ACC-003 | Hindi fallback check. |
| TC-ACC-004 | Chart table alternative check. |

# 8. Business Rules

|  |  |
| --- | --- |
| Rule ID | Business Rule |
| BR-GEN-001 | All protected actions require role, permission and pillar/workstream scope check. |
| BR-GEN-002 | English is default and Hindi is supported with English fallback. |
| BR-GEN-003 | Stable business codes are exposed to UI/API; internal database IDs are hidden. |
| BR-GEN-004 | Published/public data must come only from approved facts. |
| BR-GEN-005 | Every request, submission, validation, review, publication and notification action must keep an audit/status trail. |
| BR-GEN-006 | Phase I notifications must support email delivery and auditable notification logs. Stream/webhook delivery is future technical extension. |
| BR-GEN-007 | Referenced records should be deactivated/archived rather than hard deleted. |
| BR-GEN-008 | Maker-Checker workflow separation shall apply to configured review, approval, publishing and governance workflows so that the user/role initiating an item cannot approve the same item unless MoSPI approves an exception with audit justification. |
| BR-GEN-009 | Template formats, validation rules, controlled vocabularies, chart/visualization catalogue and role-permission mappings shall be confirmed by the concerned functional nodal officers or authorized MoSPI business administrators before baseline use. |
| BR-GEN-010 | Scanned or non-machine-readable source submissions shall be preserved as source artifacts and shall not become curated data until manually structured, resubmitted or clarified and reviewed by authorized users. |
| BR-GEN-011 | SMS, WhatsApp, OCR, Digital Signature, PDF Watermark, AI Insights and SSO/LDAP shall not be treated as Phase I commitments unless separately approved by MoSPI through change control. |
| BR-GEN-012 | MFA shall be mandatory for Super Admin, Administrator, Reviewer, Approver, Publisher and other privileged/internal workflow roles as per MoSPI-approved security policy. |

# 9. Data Dictionary

Only important fields are shown here for business and testing understanding. Full column lists, constraints and indexes remain in the migration SQL files.

|  |  |  |  |
| --- | --- | --- | --- |
| **Module** | **Entity / Table** | **Purpose** | **Important Fields** |
| Auth | auth.pillars | Pillar/workstream scope. | pillar\_code, parent\_pillar\_id, status |
| Auth | auth.users | User identity and account status. | username, email, password\_hash, status |
| Auth | auth.roles / auth.permissions | RBAC master and permission mapping. | role\_code, permission\_code, module\_code, action\_code |
| Auth | auth.user\_role\_assignments | Assign user to role/pillar. | user\_id, role\_id, pillar\_id, status |
| Masters | metadata.framework\_editions | Framework version/edition. | framework\_code, edition\_code, version\_label, status |
| Masters | metadata.framework\_hierarchy\_levels | Dynamic hierarchy levels. | level\_code, level\_number, allows\_indicator\_mapping |
| Masters | metadata.framework\_nodes | Framework nodes. | node\_code, level\_id, node\_number, status |
| Masters | metadata.framework\_node\_relationships | Parent-child framework links. | parent\_node\_id, child\_node\_id, relationship\_type |
| Masters | metadata.national\_indicators | National indicator master. | national\_indicator\_code, indicator\_number, owning\_pillar\_code |
| Masters | metadata.global\_indicators | Global indicator master. | global\_indicator\_code, indicator\_number |
| Masters | metadata.indicator\_versions | Indicator versions. | version\_code, version\_number, data\_type, status |
| Masters | metadata.indicator\_metadata\_details | Version metadata. | reference\_period, latest\_availability, source\_reference\_code |
| Masters | metadata.indicator\_measures | Indicator measures. | measure\_code, value\_type, pillar\_code, decimal\_places |
| Masters | metadata.indicator\_periodicities | Periodicity master. | periodicity\_code, months\_interval |
| Masters | metadata.framework\_indicator\_mappings | Indicator to framework node. | node\_id, national\_indicator\_id, mapping\_type |
| Masters | metadata.national\_global\_indicator\_mappings | National to global mapping. | national\_indicator\_id, global\_indicator\_id, mapping\_type |
| Masters | org.organizations | Ministry/department/division/source hierarchy. | organization\_code, parent\_organization\_id, organization\_type |
| Masters | org.officers | Officer/contact master. | officer\_code, organization\_id, designation, email |
| Masters | org.indicator\_source\_assignments | Indicator to source/officer mapping. | national\_indicator\_id, source\_organization\_id, officer\_id, assignment\_role |
| Dimensions | dimensions.dimension\_definitions | Dimension master. | dimension\_code, dimension\_type, is\_active |
| Dimensions | dimensions.dimension\_members | Dimension members. | member\_code, dimension\_id, sort\_order |
| Dimensions | dimensions.dimension\_member\_relationships | Dimension hierarchy. | parent\_member\_id, child\_member\_id, depth |
| Dimensions | dimensions.dimension\_member\_sets | Reusable member set. | member\_set\_code, dimension\_id, set\_type |
| Dimensions | dimensions.dimension\_member\_set\_items | Members in set. | member\_set\_id, member\_id, sort\_order |
| Dimensions | dimensions.dimension\_member\_rollup\_rules | Rollup behavior. | parent\_member\_id, entry\_mode, aggregation\_method |
| Dimensions | dimensions.dimension\_member\_rollup\_rule\_children | Rollup child members. | rollup\_rule\_id, child\_member\_id, child\_weight |
| Dimensions | dimensions.geographies | Geography specialized records. | geography\_code, geography\_level\_id, member\_id |
| Dimensions | dimensions.time\_periods | Time specialized records. | time\_period\_code, frequency\_id, start\_date, end\_date |
| Templates | templates.template\_definitions | Stable template. | template\_code, framework\_code, national\_indicator\_id |
| Templates | templates.template\_versions | Template version/draft/published state. | template\_version\_code, version\_number, status |
| Templates | templates.template\_axes | Template axes. | axis\_code, axis\_role, dimension\_id |
| Templates | templates.template\_axis\_members | Axis selected members. | axis\_id, member\_id, display\_order |
| Templates | templates.template\_measures | Measures used in template. | measure\_code, value\_type, pillar\_code |
| Templates | templates.template\_binding\_groups | Designer group/options. | binding\_group\_code, parent\_binding\_group\_code, axis\_role, show\_header |
| Templates | templates.template\_cells | Generated/editable cells. | cell\_code, measure\_id, editable, required |
| Templates | templates.template\_cell\_axis\_members | Cell axis tuple. | cell\_id, axis\_id, member\_id |
| Templates | templates.template\_render\_elements | Canvas render elements. | element\_code, element\_type, row\_index, column\_index |
| Requests | requests.collection\_cycles | Collection cycle. | cycle\_code, reporting\_year, status |
| Requests | requests.collection\_requests | Request header. | request\_code, source\_organization\_id, officer\_id, status |
| Requests | requests.collection\_request\_items | Indicator/template item. | item\_code, request\_id, national\_indicator\_id, template\_instance\_id |
| Requests | requests.collection\_request\_scope\_members | Requested dimension scope. | item\_id, dimension\_id, member\_id |
| Requests | requests.request\_assignments | Assigned data provider/reviewer. | assignment\_code, request\_id, item\_id, officer\_id |
| Requests | requests.request\_status\_events | Request status trail. | event\_code, entity\_code, event\_type |
| Invitation | invitation\_access.external\_contributor\_invitations | Temporary contributor invite. | invitation\_code, assignment\_id, status, expires\_at |
| Invitation | invitation\_access.invitation\_setup\_tokens | Hash-only token metadata. | token\_code, invitation\_id, token\_hash, expires\_at |
| Invitation | invitation\_access.notification\_outbox | Request/invitation email outbox. | notification\_code, channel, recipient, delivery\_status |
| Ingestion | ingestion.submissions | Submission header. | submission\_code, request\_id, current\_version\_number, status |
| Ingestion | ingestion.submission\_versions | Submission version. | version\_code, submission\_id, version\_number, status |
| Ingestion | ingestion.payload\_manifests | File/payload reference. | manifest\_code, version\_id, storage\_provider, payload\_uri |
| Ingestion | ingestion.staged\_record\_index | Structured staged data row. | record\_code, version\_id, value\_text, value\_numeric |
| Ingestion | ingestion.staged\_record\_dimensions | Dimensions for staged row. | record\_id, dimension\_id, member\_id |
| Validation | validation.validation\_rules | Validation rule master. | rule\_code, rule\_type, severity |
| Validation | validation.validation\_rule\_bindings | Rule binding. | binding\_code, rule\_id, template\_version\_id, measure\_code |
| Validation | validation.validation\_runs | Validation run. | run\_code, version\_id, status |
| Validation | validation.validation\_results | Result row. | result\_code, run\_id, record\_id, severity, status |
| Validation | validation.validation\_comparison\_results | Previous/current comparison. | comparison\_code, result\_id, comparison\_status |
| Review | review.review\_tasks | Review task. | task\_code, run\_id, review\_level, status |
| Review | review.review\_action\_logs | Review action. | action\_code, task\_id, action\_type\_code, action\_status |
| Review | review.approval\_logs | Approval decision. | approval\_code, task\_id, approval\_status |
| Published Data | published\_data.approved\_snapshots | Published snapshot. | snapshot\_code, approval\_code, snapshot\_status |
| Published Data | published\_data.approved\_observations | Approved fact value. | observation\_code, snapshot\_id, value\_numeric, value\_text |
| Published Data | published\_data.approved\_observation\_dimensions | Dimensions for fact row. | observation\_id, dimension\_id, member\_id |
| Dashboard | dashboard.v\_\* read models | Read-only dashboard summaries. | pillar\_code, indicator\_code, source, status, latest\_value |

# 10. Non-Functional Requirements

|  |  |  |
| --- | --- | --- |
| **NFR ID** | **Requirement** | **Suggested Production Answer / Acceptance** |
| NFR-001 | Availability | Production services shall run as separately configured Docker services on MoSPI-provided server infrastructure, with health checks and restart policy. |
| NFR-002 | Performance | Normal API/page response target is 3 seconds for common operations. Large report/PDF generation target is 60-120 seconds depending on data volume and template complexity. |
| NFR-003 | Concurrent Users | System shall support 300 concurrent internal users and 1,500 concurrent public dashboard users subject to production sizing and performance testing. |
| NFR-004 | Bulk Upload Limit | Excel/CSV upload size shall default to 50 MB and remain backend-configurable. Maximum rows are controlled by file size rather than a fixed row count. Maximum files per bulk upload is 3. |
| NFR-005 | Browser Compatibility | Chrome, Edge, Firefox latest/previous two versions; Safari current versions; IE not supported. |
| NFR-006 | Mobile/Responsive | Core public views and supported internal views shall be responsive. Complex designer grids may provide optimized desktop experience. |
| NFR-007 | Log Retention | Application log rotation, archival, retention period and purging policy shall be detailed in SRS/technical design. Audit/security retention shall follow approved MoSPI/CERT-In policy. |
| NFR-008 | Backup and DR | Daily/weekly/monthly incremental and full backups shall be planned for hot and cold backup needs. RPO target is 0 hours. DR drill shall be conducted yearly. |
| NFR-009 | Accessibility | Core screens shall be keyboard usable, screen-reader friendly and have adequate contrast and error announcements. |
| NFR-010 | Bilingual | English and Hindi labels/messages supported with English fallback when translation is missing. |

## 10.1 Production Parameter Baseline

|  |  |  |
| --- | --- | --- |
| **Parameter** | **Confirmed Baseline** | **Notes** |
| Maximum Excel/CSV upload size | 50 MB | Backend-configurable. |
| Maximum rows per Excel/CSV upload | No fixed row count | Controlled by file size and validation performance. |
| Maximum files/documents per bulk upload | 3 files | Applies to user-facing bulk upload action. |
| Allowed data upload file types | .xlsx, .csv | Other file types are not part of data upload scope. |
| Resume upload | Not included in Phase I | Can be considered later if large-file upload requirement changes. |
| Concurrent internal users | 300 | To be validated in performance testing. |
| Concurrent public dashboard users | 1,500 | To be validated in performance testing and infrastructure sizing. |
| Normal API/page response target | 3 seconds | Applies to common list/detail/form operations under normal load. |
| Large report/PDF generation target | 60-120 seconds | Depends on volume, layout complexity and rendering workload. |
| Dashboard refresh/cache duration | Configurable | Exact default cache duration to be finalized in SRS/performance design. |
| Uploaded source file retention | 2 days | After retention window, archive/purge policy applies as per SRS. |
| Published report/document retention | 1 year, then archive | Archive storage and retrieval process to be defined in operations design. |
| Backup retention | 3 months, then archive | Backup archival policy to be detailed in operations/SRS. |
| Backup frequency | Daily, weekly and monthly | Incremental and full backup strategy covering hot and cold backup needs. |
| RPO | 0 hours | Production architecture and operations must be designed to meet this target. |
| RTO | To be finalized in SRS/technical design | Not yet confirmed. |
| DR drill frequency | Yearly | Evidence to be maintained for operations/compliance review. |

## 10.2 Phase I Scope and Future / Approval-Based Scope

|  |  |  |
| --- | --- | --- |
| **Area** | **Phase I Scope** | **Not Included / Future / Approval-Based** |
| Notification channels | Email-only notification channel, including request emails, OTP/email alerts, reminders, escalation emails and report emails where configured. | SMS and WhatsApp are not included in Phase I unless separately approved by MoSPI through change control. |
| Reminder and escalation | Reminder schedule is configurable. Escalation starts 1 day after due date by default and remains configurable. | Advanced multi-channel escalation is future/approval-based. |
| Identity | Internal application user management, role and permission control. | SSO/LDAP is not included in current Phase I scope unless separately approved by MoSPI through change control. |
| Security controls | IP restriction for admin users is included and configurable. Password expiry is configurable with 90-day default. Failed login lockout is configurable with 5-attempt default. Session timeout is configurable with 30-minute default. | Captcha is not required in Phase I and is future/approval-based. |
| Analytics | Dashboards, drilldowns, charts and approved-data views. | AI Insights, forecast/regression analytics and advanced analytics playground features are future/approval-based and are not part of Phase I unless approved by MoSPI. |
| Publication output | PDF generation and publication workflow using approved data. | Digital Signature and PDF Watermark are not included in Phase I unless separately approved by MoSPI. |
| CMS | SSD portal will integrate/link with Plone where required. CMS page CRUD is handled inside Plone. | Plone implementation is not custom-built inside SSD Phase I. |
| DMS | SSD portal will integrate/link with ownCloud where required. File preview/search is handled by ownCloud. | ownCloud implementation is not custom-built inside SSD Phase I. |
| Search/media | Normal portal search/filtering and document integration references. | OCR Search and Media Compression are not included in Phase I unless separately approved by MoSPI; scanned/non-machine-readable statistical submissions are retained as source artifacts only. |
| API keys | Normal authenticated API access for portal use. | API key management is future scope. |
| Worker/scheduler | Separate email notification service is included. | Separate background worker/scheduler service is not included in Phase I and is future scope. |
| Database extensions | Citus and Apache AGE are Phase I production scope. | Sizing and exact use of distribution/graph projections to be detailed in technical design. |

# 11. Security Requirements

|  |  |
| --- | --- |
| **SEC ID** | **Requirement** |
| SEC-001 | Password values are never stored or logged in plain text. |
| SEC-002 | Raw tokens, token hashes, source hashes and internal IDs are not exposed in normal APIs/screens. |
| SEC-003 | Account lockout, password complexity and password expiry policy shall be configurable. Default password expiry is 90 days, failed-login lockout threshold is 5 attempts, and session timeout is 30 minutes. |
| SEC-004 | API rate limit/throttling shall be configured at gateway/API layer. |
| SEC-005 | Secrets shall be stored in environment/secret management, not in source code. |
| SEC-006 | Encryption key rotation shall be part of production operations/security policy. |
| SEC-007 | File uploads shall be type/size checked and routed through virus-scan handoff where configured. |
| SEC-008 | VAPT/STQC/CERT-In/GIGW evidence shall be available before go-live. |
| SEC-009 | IP restriction for admin users shall be included and configurable. |
| SEC-010 | Captcha is not required in Phase I. It may be added later only if approved by MoSPI. |
| SEC-011 | MFA shall be enforced for Super Admin, Admin, Reviewer, Approver, Publisher and other privileged users/workflow roles as configured by MoSPI. MFA success/failure shall be audit logged. |

## 11.1 Security Acceptance Criteria

|  |  |
| --- | --- |
| **Criteria ID** | **Acceptance Criteria** |
| SAC-001 | Unauthorized user cannot access protected API or UI route. |
| SAC-002 | Wrong password does not reveal whether account exists beyond safe message. |
| SAC-003 | Request/invitation readback does not expose raw token or token hash. |
| SAC-004 | Uploaded file outside allowed policy is rejected. |
| SAC-005 | Audit log is written for login, request, submit, validation, review, approval and publish actions. |

# 12. Compliance Requirements

* GIGW-aligned accessibility, responsive behavior and bilingual support.
* STQC, CERT-In empanelled VAPT and applicable Government of India cybersecurity advisory compliance before go-live.
* NDSAP-aligned public data access for approved data only.
* DBIM and applicable Government of India data/business intelligence management guidance shall be considered for data governance, dashboards, metadata, auditability and analytical reporting where applicable to MoSPI scope.
* Audit, log retention, backup/restore, patching and vulnerability management evidence during O&M.

# 13. Integration Requirements

|  |  |  |
| --- | --- | --- |
| **Integration** | **Purpose** | **Current Scope** |
| Plone CMS | Public pages, menu, bilingual content and content workflow. | External CMS integration. CMS page CRUD is handled inside Plone; SSD portal integrates/links where required. |
| ownCloud DMS | Documents, publications, metadata, preview, retention and versioning. | External DMS integration. File preview/search is handled by ownCloud; SSD portal integrates/links where required. |
| Email/OTP | OTP, request mail, reminders, escalation and reports. | Included as Phase I notification channel. |
| Notification Logs | Searchable notification event and delivery trail. | Included for audit/monitoring; email is the confirmed Phase I delivery channel. |
| Webhook/Stream Events | Application-level event stream for workflow notifications and future integrations. | Future/technical extension, not a Phase I user notification channel. |
| SSO/LDAP | Enterprise identity provider. | Not used in current Phase I scope unless separately approved by MoSPI. |
| Citus / Apache AGE | Scale and graph/lineage extension. | Phase I production scope; detailed usage to be finalized in technical design. |
| Integration / Middleware Layer | API orchestration, request validation, authentication/RBAC enforcement, message processing, routing, retry/fallback handling and audit logging between UI, services, databases and approved external systems. | Included as the controlled API/middleware layer for Phase I; detailed API contracts and deployment design will be finalized in SRS/solution design. |

# 14. Requirements Traceability Matrix

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **RTM ID** | **Module** | **Primary Screens** | **Database Area** | **Main Test Focus** |
| RTM-001 | Authentication, User Access and Security | Login / Role Landing; Password Management; Profile; Preferences | AUTH | Login success by Super Admin., Wrong password safe error. |
| RTM-002 | Application Setup, Pillar and Workstreams | Application Setup / Branding; Pillar Selector | APP | Save SDG branding., Pillar Admin tries cross-pillar update and is blocked. |
| RTM-003 | Reference Masters | Reference Masters | MST | Create organization hierarchy., Create officer under division. |
| RTM-004 | Framework Setup and Hierarchy | Framework Setup; Framework Hierarchy Builder | FRM | Create root node., Create child under selected parent. |
| RTM-005 | Indicator Management and Source Mapping | Indicator Management | IND | Create indicator., Add two source assignments. |
| RTM-006 | Dimension Management | Dimension Management | DIM | Create geography root India., Add state child. |
| RTM-007 | Template Management and Excel-like Designer | Template List; Template Designer; JSON Preview | TPL | Save draft then reload., Bind geography/time/area/gender/measure. |
| RTM-008 | Collection Requests and Assignment | Collection Request Creation | REQ | Create request with two items., Add To and CC recipients. |
| RTM-009 | Invitation Access and Temporary Contributor | Invitation Access Monitor; Temporary Contributor Setup | INV | Generate invitation., Open monitor. |
| RTM-010 | Data Entry, Excel Upload and Ingestion | Department Data Entry; Ingestion Readback | ING | Fill numeric cell., Add allowed year. |
| RTM-011 | Validation Rule Execution and Report | Validation Queue; Validation Report | VAL | Run validation pass., Missing numeric value produces error. |
| RTM-012 | Review, Approval and Published Fact Creation | Review / Approval | REV | Approve path publishes facts., Reject path records reason. |
| RTM-013 | Published Data and Fact Store | Published Snapshot Dashboard; Previous Approved Lookup | PDATA | Publish approval., Latest observation filter by year. |
| RTM-014 | Publication Management Workspace and PDF Designer | Publication Workspace; PDF Designer; Publication Review | PUBWS | Create workspace from previous layout., Auto-save draft. |
| RTM-015 | Dashboards and Analytics Views | Super Admin Dashboard; Pillar Admin Dashboard; Submitted Snapshot Dashboard; Public Dashboard | DASH | Pillar dashboard filter., Public dashboard disabled blocked. |
| RTM-016 | Content Management System - Plone | CMS Content Admin; Public Pages | CMS | Create page draft., Schedule publish. |
| RTM-017 | Document Management System - ownCloud | DMS Listing; Upload/Metadata; File Preview | DMS | Upload PDF., Preview document. |
| RTM-018 | Notification Engine, Reminders and Schedulers | Notifications; Reminders; Logs & Monitor | NOTIF | Request sent email event., Reminder due event. |
| RTM-019 | Logs, Monitoring, Backup and Audit | Logs & Monitor; Audit Views | MON | Filter ERROR logs., Open audit detail. |
| RTM-020 | Accessibility, Bilingual Support and Preferences | Accessibility Compliance; Preferences; all screens | ACC | Keyboard-only data entry path., Screen reader label check. |

# 15. Deliverables and Milestones

The project is organized into 4 milestones (Phase I: 15 months) and an O&M phase (Phase II: 21 months).

|  |  |  |
| --- | --- | --- |
| **Phase** | **Timeline / Payment** | **Key Deliverables** |
| M1 | 4 Months (20% of the Phase 1 amount) | Requirement Gathering; Preparation of Requirement Specific Documents (FRS/SRS); Design and document the system and data architecture; Setup of cloud infrastructure; Procurement of staging server from MoSPI; Development of Data Ingestion Module; Migration of Legacy Data; UAT and Go-Live of the Data Ingestion Module. |
| M2 | 4 Months (25% of the Phase 1 amount) | Development of customized dashboards along with customized visualization for all publications; Development of Content Management Module; Implementation of Report Generation Module; UAT and Security Audit; Go-Live of the above modules. |
| M3 | 4 Months (25% of the Phase 1 amount) | Implementation of Document Management Module; Development of Virtual Book Module; UAT and Security Audit; Go-Live of the above modules. |
| M4 | 3 Months (30% of the Phase 1 amount) | Implementation of Admin module; Full system integration; End-to-end testing and UAT; User Training; Security Audit; Final Go-Live of the Unified Portal. |
| O&M | 21 Months (Quarterly Payments) | Operations and Maintenance. |

# 16. Assumptions, Dependencies, Risks, and Constraints

## 16.1 Assumptions

* Production deployment will use separately configured Docker services on MoSPI-provided server infrastructure.
* Separate email notification service is included in Phase I. A separate background worker/scheduler service is future scope unless later approved.
* Plone and ownCloud are external systems. SSD portal will integrate/link with them where required, but their CMS/DMS capabilities are not custom-built inside SSD Phase I.
* Dashboard cache default duration, RTO, and detailed log rotation/archive/purge policy will be finalized during SRS/technical design.
* Functional nodal officers shall confirm and approve template formats, validation rules, controlled vocabularies, chart catalogue, role-permission mappings and other business-configurable parameters before production baseline use.

## 16.2 Dependencies

* Reference masters and indicators must be ready before templates and requests.
* Approved template version is required before collection request.
* Published facts are required before publication workspace can create final official output.

## 16.3 Risks and Constraints

* Large Excel uploads may need queueing and worker sizing.
* Complex Excel-like designer is best used on desktop/tablet; mobile is primarily for simpler review/dashboard flows.
* Public dashboard must never show unapproved data.

# 17. Glossary and Acronyms

|  |  |
| --- | --- |
| **Term** | **Meaning** |
| SSD | Social Statistics Division / project statistical system context. |
| SDG | Sustainable Development Goals pillar. |
| SWS | Social Welfare Statistics pillar. |
| ENV | Environment statistics pillar. |
| BRICS | BRICS pillar |
| CMS | Content Management System, Plone. |
| DMS | Document Management System, ownCloud. |
| FRS | Functional Requirements Specification. |
| RBAC | Role Based Access Control. |
| RTM | Requirements Traceability Matrix. |
| Fact Store | Approved published observation tables used for dashboard and publication. |
| DBIM | Data and Business Intelligence Management / applicable Government data and business intelligence management guidance referenced by MoSPI/DIID for data governance and analytics alignment. |
| MFA | Multi-Factor Authentication for privileged and configured workflow users. |
| Maker-Checker | Workflow control in which the maker/initiator and checker/approver are separate users or roles for configured review/approval workflows. |
| Integration / Middleware Layer | Controlled API and integration layer providing API orchestration, authentication/RBAC enforcement, message processing, routing, retry/fallback handling and audit logging between portal layers and approved external systems. |
| Functional Nodal Officer | MoSPI or business-nominated official responsible for confirming functional rules such as templates, validation rules, controlled vocabularies, chart catalogues and role-permission mappings. |

# 18. Minimum Client Submission Enhancements

## 18.1 Atomic Functional Requirement ID Catalogue

|  |  |
| --- | --- |
| **Module** | **Requirement IDs** |
| Authentication, User Access and Security | FR-AUTH-001, FR-AUTH-002, FR-AUTH-003, FR-AUTH-004 |
| Application Setup, Pillars and Workstreams | FR-APP-001, FR-APP-002, FR-APP-003 |
| Reference Masters | FR-MST-001, FR-MST-002, FR-MST-003 |
| Framework Setup and Hierarchy | FR-FRM-001, FR-FRM-002, FR-FRM-003 |
| Indicator Management and Source Mapping | FR-IND-001, FR-IND-002, FR-IND-003 |
| Dimension Management | FR-DIM-001, FR-DIM-002, FR-DIM-003 |
| Template Management and Excel-like Designer | FR-TPL-001, FR-TPL-002, FR-TPL-003 |
| Collection Requests and Assignment | FR-REQ-001, FR-REQ-002, FR-REQ-003 |
| Invitation Access and Temporary Contributor | FR-INV-001, FR-INV-002, FR-INV-003 |
| Data Entry, Excel Upload and Ingestion | FR-ING-001, FR-ING-002, FR-ING-003, FR-ING-004 |
| Validation Rule Execution and Report | FR-VAL-001, FR-VAL-002, FR-VAL-003 |
| Review, Approval and Published Fact Creation | FR-REV-001, FR-REV-002, FR-REV-003, FR-REV-004 |
| Published Data and Fact Store | FR-PDATA-001, FR-PDATA-002, FR-PDATA-003 |
| Publication Management Workspace and PDF Designer | FR-PUBWS-001, FR-PUBWS-002, FR-PUBWS-003 |
| Dashboards and Analytics Views | FR-DASH-001, FR-DASH-002, FR-DASH-003 |
| Content Management System - Plone | FR-CMS-001, FR-CMS-002, FR-CMS-003 |
| Document Management System - ownCloud | FR-DMS-001, FR-DMS-002, FR-DMS-003 |
| Notification Engine, Reminders and Schedulers | FR-NOTIF-001, FR-NOTIF-002, FR-NOTIF-003 |
| Logs, Monitoring, Backup and Audit | FR-MON-001, FR-MON-002, FR-MON-003 |
| Accessibility, Bilingual Support and Preferences | FR-ACC-001, FR-ACC-002, FR-ACC-003 |

## 18.2 Screen Inventory and UI Specification Baseline

|  |  |  |
| --- | --- | --- |
| **Screen ID** | **Screen** | **Module** |
| UI-001 | Login / Role Landing; Password Management; Profile; Preferences | Authentication, User Access and Security |
| UI-002 | Application Setup / Branding; Pillar Selector | Application Setup, Pillars and Workstreams |
| UI-003 | Reference Masters | Reference Masters |
| UI-004 | Framework Setup; Framework Hierarchy Builder | Framework Setup and Hierarchy |
| UI-005 | Indicator Management | Indicator Management and Source Mapping |
| UI-006 | Dimension Management | Dimension Management |
| UI-007 | Template List; Template Designer; JSON Preview | Template Management and Excel-like Designer |
| UI-008 | Collection Request Creation | Collection Requests and Assignment |
| UI-009 | Invitation Access Monitor; Temporary Contributor Setup | Invitation Access and Temporary Contributor |
| UI-010 | Department Data Entry; Ingestion Readback | Data Entry, Excel Upload and Ingestion |
| UI-011 | Validation Queue; Validation Report | Validation Rule Execution and Report |
| UI-012 | Review / Approval | Review, Approval and Published Fact Creation |
| UI-013 | Published Snapshot Dashboard; Previous Approved Lookup | Published Data and Fact Store |
| UI-014 | Publication Workspace; PDF Designer; Publication Review | Publication Management Workspace and PDF Designer |
| UI-015 | Super Admin Dashboard; Pillar Admin Dashboard; Submitted Snapshot Dashboard; Public Dashboard | Dashboards and Analytics Views |
| UI-016 | CMS Content Admin; Public Pages | Content Management System - Plone |
| UI-017 | DMS Listing; Upload/Metadata; File Preview | Document Management System - ownCloud |
| UI-018 | Notifications; Reminders; Logs & Monitor | Notification Engine, Reminders and Schedulers |
| UI-019 | Logs & Monitor; Audit Views | Logs, Monitoring, Backup and Audit |
| UI-020 | Accessibility Compliance; Preferences; all screens | Accessibility, Bilingual Support and Preferences |

## 18.3 Field-Level Logical Data Dictionary Addendum

|  |  |  |
| --- | --- | --- |
| **Module** | **Entity / Table** | **Important Fields** |
| Auth | auth.pillars | pillar\_code, parent\_pillar\_id, status |
| Auth | auth.users | username, email, password\_hash, status |
| Auth | auth.roles / auth.permissions | role\_code, permission\_code, module\_code, action\_code |
| Auth | auth.user\_role\_assignments | user\_id, role\_id, pillar\_id, status |
| Masters | metadata.framework\_editions | framework\_code, edition\_code, version\_label, status |
| Masters | metadata.framework\_hierarchy\_levels | level\_code, level\_number, allows\_indicator\_mapping |
| Masters | metadata.framework\_nodes | node\_code, level\_id, node\_number, status |
| Masters | metadata.framework\_node\_relationships | parent\_node\_id, child\_node\_id, relationship\_type |
| Masters | metadata.national\_indicators | national\_indicator\_code, indicator\_number, owning\_pillar\_code |
| Masters | metadata.global\_indicators | global\_indicator\_code, indicator\_number |
| Masters | metadata.indicator\_versions | version\_code, version\_number, data\_type, status |
| Masters | metadata.indicator\_metadata\_details | reference\_period, latest\_availability, source\_reference\_code |
| Masters | metadata.indicator\_measures | measure\_code, value\_type, pillar\_code, decimal\_places |
| Masters | metadata.indicator\_periodicities | periodicity\_code, months\_interval |
| Masters | metadata.framework\_indicator\_mappings | node\_id, national\_indicator\_id, mapping\_type |
| Masters | metadata.national\_global\_indicator\_mappings | national\_indicator\_id, global\_indicator\_id, mapping\_type |
| Masters | org.organizations | organization\_code, parent\_organization\_id, organization\_type |
| Masters | org.officers | officer\_code, organization\_id, designation, email |
| Masters | org.indicator\_source\_assignments | national\_indicator\_id, source\_organization\_id, officer\_id, assignment\_role |
| Dimensions | dimensions.dimension\_definitions | dimension\_code, dimension\_type, is\_active |
| Dimensions | dimensions.dimension\_members | member\_code, dimension\_id, sort\_order |
| Dimensions | dimensions.dimension\_member\_relationships | parent\_member\_id, child\_member\_id, depth |
| Dimensions | dimensions.dimension\_member\_sets | member\_set\_code, dimension\_id, set\_type |
| Dimensions | dimensions.dimension\_member\_set\_items | member\_set\_id, member\_id, sort\_order |
| Dimensions | dimensions.dimension\_member\_rollup\_rules | parent\_member\_id, entry\_mode, aggregation\_method |
| Dimensions | dimensions.dimension\_member\_rollup\_rule\_children | rollup\_rule\_id, child\_member\_id, child\_weight |
| Dimensions | dimensions.geographies | geography\_code, geography\_level\_id, member\_id |
| Dimensions | dimensions.time\_periods | time\_period\_code, frequency\_id, start\_date, end\_date |
| Templates | templates.template\_definitions | template\_code, framework\_code, national\_indicator\_id |
| Templates | templates.template\_versions | template\_version\_code, version\_number, status |
| Templates | templates.template\_axes | axis\_code, axis\_role, dimension\_id |
| Templates | templates.template\_axis\_members | axis\_id, member\_id, display\_order |
| Templates | templates.template\_measures | measure\_code, value\_type, pillar\_code |
| Templates | templates.template\_binding\_groups | binding\_group\_code, parent\_binding\_group\_code, axis\_role, show\_header |
| Templates | templates.template\_cells | cell\_code, measure\_id, editable, required |
| Templates | templates.template\_cell\_axis\_members | cell\_id, axis\_id, member\_id |
| Templates | templates.template\_render\_elements | element\_code, element\_type, row\_index, column\_index |
| Requests | requests.collection\_cycles | cycle\_code, reporting\_year, status |
| Requests | requests.collection\_requests | request\_code, source\_organization\_id, officer\_id, status |
| Requests | requests.collection\_request\_items | item\_code, request\_id, national\_indicator\_id, template\_instance\_id |
| Requests | requests.collection\_request\_scope\_members | item\_id, dimension\_id, member\_id |
| Requests | requests.request\_assignments | assignment\_code, request\_id, item\_id, officer\_id |
| Requests | requests.request\_status\_events | event\_code, entity\_code, event\_type |
| Invitation | invitation\_access.external\_contributor\_invitations | invitation\_code, assignment\_id, status, expires\_at |
| Invitation | invitation\_access.invitation\_setup\_tokens | token\_code, invitation\_id, token\_hash, expires\_at |
| Invitation | invitation\_access.notification\_outbox | notification\_code, channel, recipient, delivery\_status |
| Ingestion | ingestion.submissions | submission\_code, request\_id, current\_version\_number, status |
| Ingestion | ingestion.submission\_versions | version\_code, submission\_id, version\_number, status |
| Ingestion | ingestion.payload\_manifests | manifest\_code, version\_id, storage\_provider, payload\_uri |
| Ingestion | ingestion.staged\_record\_index | record\_code, version\_id, value\_text, value\_numeric |
| Ingestion | ingestion.staged\_record\_dimensions | record\_id, dimension\_id, member\_id |
| Validation | validation.validation\_rules | rule\_code, rule\_type, severity |
| Validation | validation.validation\_rule\_bindings | binding\_code, rule\_id, template\_version\_id, measure\_code |
| Validation | validation.validation\_runs | run\_code, version\_id, status |
| Validation | validation.validation\_results | result\_code, run\_id, record\_id, severity, status |
| Validation | validation.validation\_comparison\_results | comparison\_code, result\_id, comparison\_status |
| Review | review.review\_tasks | task\_code, run\_id, review\_level, status |
| Review | review.review\_action\_logs | action\_code, task\_id, action\_type\_code, action\_status |
| Review | review.approval\_logs | approval\_code, task\_id, approval\_status |
| Published Data | published\_data.approved\_snapshots | snapshot\_code, approval\_code, snapshot\_status |
| Published Data | published\_data.approved\_observations | observation\_code, snapshot\_id, value\_numeric, value\_text |
| Published Data | published\_data.approved\_observation\_dimensions | observation\_id, dimension\_id, member\_id |
| Dashboard | dashboard.v\_\* read models | pillar\_code, indicator\_code, source, status, latest\_value |

## 18.4 Enhanced Requirements Traceability Matrix Addendum

|  |  |  |  |
| --- | --- | --- | --- |
| **Requirement** | **Business Rule** | **Post Condition** | **Test Scenario** |
| FR-AUTH-001 | BR-AUTH-001 | POST-AUTH-001 | TC-AUTH-001 |
| FR-APP-001 | BR-APP-001 | POST-APP-001 | TC-APP-001 |
| FR-MST-001 | BR-MST-001 | POST-MST-001 | TC-MST-001 |
| FR-FRM-001 | BR-FRM-001 | POST-FRM-001 | TC-FRM-001 |
| FR-IND-001 | BR-IND-001 | POST-IND-001 | TC-IND-001 |
| FR-DIM-001 | BR-DIM-001 | POST-DIM-001 | TC-DIM-001 |
| FR-TPL-001 | BR-TPL-001 | POST-TPL-001 | TC-TPL-001 |
| FR-REQ-001 | BR-REQ-001 | POST-REQ-001 | TC-REQ-001 |
| FR-INV-001 | BR-INV-001 | POST-INV-001 | TC-INV-001 |
| FR-ING-001 | BR-ING-001 | POST-ING-001 | TC-ING-001 |
| FR-VAL-001 | BR-VAL-001 | POST-VAL-001 | TC-VAL-001 |
| FR-REV-001 | BR-REV-001 | POST-REV-001 | TC-REV-001 |
| FR-PDATA-001 | BR-PDATA-001 | POST-PDATA-001 | TC-PDATA-001 |
| FR-PUBWS-001 | BR-PUBWS-001 | POST-PUBWS-001 | TC-PUBWS-001 |
| FR-DASH-001 | BR-DASH-001 | POST-DASH-001 | TC-DASH-001 |
| FR-CMS-001 | BR-CMS-001 | POST-CMS-001 | TC-CMS-001 |
| FR-DMS-001 | BR-DMS-001 | POST-DMS-001 | TC-DMS-001 |
| FR-NOTIF-001 | BR-NOTIF-001 | POST-NOTIF-001 | TC-NOTIF-001 |
| FR-MON-001 | BR-MON-001 | POST-MON-001 | TC-MON-001 |
| FR-ACC-001 | BR-ACC-001 | POST-ACC-001 | TC-ACC-001 |
| FR-AUTH-004 | BR-AUTH-005 | POST-AUTH-004 | TC-AUTH-005 |
| FR-ING-004 | BR-ING-004 | POST-ING-004 | TC-ING-005 |
| FR-REV-004 | BR-REV-004 | POST-REV-004 | TC-REV-005 |

## 18.5 Role-Permission Matrix

|  |  |  |
| --- | --- | --- |
| **Role** | **Default Access Pages** | **Main Operations** |
| Super Admin | All admin dashboards, setup, monitoring | Cross-pillar configuration, audit, users, reports. |
| Pillar Admin | Own pillar dashboard, setup, requests, review status | Manage own pillar only. |
| Metadata Officer | Masters, framework, indicators, dimensions | Create/update controlled metadata. |
| Template Officer | Template list/designer | Create draft, bind dimensions/measures, publish template. |
| Data Provider | Assigned data-entry link/page | Fill/upload/save/submit assigned data. |
| Validator | Validation queue/report | Check results, send back or forward. |
| Reviewer/Approver | Review queue/workspace | Approve/reject/send back/clarify. |
| Publication Officer | Publication workspace | Create PDF draft, submit for review. |
| Auditor | Logs, audit and read-only evidence | View evidence only. |
| Public User | Public CMS/dashboard only | View approved public content. |

## 18.6 API Inventory

|  |  |  |  |
| --- | --- | --- | --- |
| **API Area** | **Main Operations** | **Auth / Scope** | **Used By** |
| Auth | login, logout, profile, preferences, password change/reset, session checks | Bearer token, role and pillar scope | Login, role landing, profile and preference screens |
| Masters | list/create/update/deactivate locales, organizations, officers, periodicities, measures and units | ADMIN/MASTERS permissions with pillar scope where applicable | Reference Masters, dropdowns and setup screens |
| Framework | framework editions, hierarchy levels, nodes, relationships, indicator mappings | Pillar-scoped metadata permissions | Framework Setup and hierarchy builder |
| Indicators | national/global indicators, versions, measures, metadata, global mapping and multiple source assignments | Pillar-scoped metadata permissions | Indicator Management and source mapping |
| Dimensions | dimension definitions, members, hierarchy, member sets, rollup rules and bulk upload/download format | DIMENSIONS permissions with pillar scope | Dimension Management and Template Designer |
| Templates | template list, draft create/update/readback, binding groups, axes, measures, cells, render contract and publish | TEMPLATES permissions with pillar scope | Template List, Template Designer and Data Entry |
| Requests | cycle, request header, item, scope members, assignment, status events and request send | REQUESTS permissions with pillar/source scope | Collection Request Creation and status trail |
| Invitation Access | generate link metadata, read monitor, resend/revoke visual/admin action and audit | REQUESTS/AUTH permissions; no raw token readback | Invitation Access Monitor and temporary contributor flow |
| Ingestion | submission draft/submit, manifest, job/run, staged records, import history and rejected-record readback | INGESTION permissions or request-linked contributor access | Data Entry, Excel Upload and Ingestion Admin |
| Validation | run validation, upsert results, comparison, queue/report and send-back/forward | VALIDATION permissions | Validation Queue and Validation Report |
| Review | tasks, action logs, approvals, clarification/reject/send-back/final approve | REVIEW permissions | Review / Approval Workspace |
| Published Data | publish approval, snapshots, latest observations and previous-approved lookup | PUBLISHED\_DATA/DASHBOARD permissions | Dashboard, Review comparison and Publication Workspace |
| Dashboard | overall summary, pillar/goal/target/indicator drilldowns, queue, pipeline and public views | DASHBOARD view; public only when enabled | Super Admin, Pillar Admin, Submitted Snapshot and Public Dashboard |
| CMS/DMS | page/document workflow integrations and link/reference management | CMS/DMS role policy | Public Portal, Publication Management and document library |

## 18.7 Master Tables Catalogue

|  |  |  |
| --- | --- | --- |
| **Master Area** | **Purpose** | **Used By** |
| Locale Master | English/Hindi label and message support with fallback. | All UI/API display labels. |
| Pillar / Workstream Master | SDG, SWS, ENV, BRICS pillars | All pillar-scoped workflows. |
| Organization Master | Ministry, department, division and source organization hierarchy. | Indicator source assignment and requests. |
| Officer Master | Officer/contact mapping to organization. | Assignments, invitations and notification recipients. |
| Periodicity Master | Annual/quarter/month/frequency references. | Indicators, templates, requests and dashboards. |
| Measure and Unit Master | Measure, datatype, unit, decimal and validation defaults. | Indicators, template designer, data entry and published facts. |
| Framework Level and Node Masters | Dynamic hierarchy levels and nodes. | Framework setup and indicator mapping. |
| Dimension and Member Masters | Any dimension, member hierarchy, member sets and rollups. | Templates, requests, validation and published fact dimensions. |

## 18.8 State Transition Diagrams and Tables

|  |  |
| --- | --- |
| **Workflow** | **State Transition Summary** |
| Template | DRAFT -> VALIDATED -> PUBLISHED/ACTIVE -> ARCHIVED/INACTIVE. Draft readback is allowed until publish; published version is used by requests. |
| Collection Request | DRAFT -> SENT -> OPENED/IN\_PROGRESS -> SUBMITTED -> VALIDATION\_PENDING -> REVIEW\_PENDING -> CLOSED/CANCELLED. |
| Invitation | GENERATED -> SENT -> OPENED -> SETUP\_COMPLETED -> USED/EXPIRED/REVOKED. Raw link is available only immediately after generation. |
| Submission/Ingestion | DRAFT -> RECEIVED -> INGESTED/STAGED -> VALIDATION\_PENDING -> VALIDATED or RETURNED\_FOR\_CORRECTION. |
| Validation | PENDING -> RUNNING -> PASSED/WARNING/FAILED -> FORWARDED\_TO\_REVIEW or SENT\_BACK. |
| Review/Approval | ASSIGNED -> IN\_REVIEW -> CLARIFICATION\_REQUESTED/SENT\_BACK/REJECTED/APPROVED. Final approval can publish once only. |
| Published Data | PUBLISHED -> SUPERSEDED when a newer approved snapshot replaces the same indicator/source/dimension/time scope. |
| Publication Workspace | DRAFT -> REVIEW\_SUBMITTED -> REVIEWED -> APPROVED -> GENERATED -> PUBLISHED/ARCHIVED. |
| CMS Page | DRAFT -> PREVIEW -> REVIEW -> APPROVED -> PUBLISHED -> ROLLED\_BACK/ARCHIVED. |
| DMS Document | UPLOADED -> SCANNED -> CLASSIFIED -> ACTIVE -> EXPIRED/ARCHIVED. |

## 18.9 Role Matrix and Permission Matrix Summary

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Role** | **Create** | **Read/View** | **Update** | **Delete/Archive** | **Review** | **Approve** | **Publish** | **Configure** |
| Super Admin | Yes | Yes | Yes | Yes | Oversight | Where assigned | Where assigned | All pillars/settings |
| Pillar Admin | Own pillar | Own pillar | Own pillar | Own pillar | Own pillar | Own pillar where assigned | Own pillar where assigned | Own pillar only |
| Metadata Officer | Masters/framework/indicator/dimension | Assigned pillar | Assigned metadata | Deactivate only | No | No | No | Metadata setup |
| Template Officer | Template drafts | Templates | Template drafts | Archive draft/version | No | No | Publish if permitted | Template setup |
| Data Provider | Submission draft | Own assignments | Own draft values | No | No | No | Submit only | No |
| Validator | Validation run/result | Validation queue | Validation notes/status | No | Validation decision | No | No | No |
| Reviewer | Review action | Assigned tasks | Review note/action | No | Yes | Recommend | No | No |
| Approver | Approval action | Assigned tasks | Approval note/action | No | Yes | Yes | Final publish trigger | No |
| Publication Officer | Publication draft | Approved facts/publications | Publication layout | Archive draft | Submit for review | No | After approval | Publication workspace |
| Auditor | No | Audit/evidence only | No | No | No | No | No | No |

## 18.10 Screen-wise Detailed Use Case Baseline

|  |  |  |  |
| --- | --- | --- | --- |
| **Screen / Page** | **Primary User Action** | **System Response** | **Main Data Used** |
| Login / Role Landing | Enter credentials and continue. | Validate account, load roles, pillar and default dashboard or show safe error. | auth users, roles, sessions and audit. |
| Super Admin Dashboard | Review cross-pillar counts, alerts, reminders and drilldowns. | Show approved summaries, workflow queues and operational status. | dashboard read models, requests, validation, review and published facts. |
| Pillar Admin Dashboard | Review pillar goal/target/indicator status. | Show requested/submitted/validated/published counts and charts. | framework, indicators, requests, review and published facts. |
| Framework Setup | Create edition, levels, root/child nodes and indicator mapping. | Maintain dynamic hierarchy and show mapping/readiness. | framework editions, levels, nodes, relationships and mappings. |
| Indicator Management | Create/update indicator, versions, measures, metadata, global mapping and sources. | Maintain complete indicator record and source responsibility. | indicator, measure, metadata, global mapping and source tables. |
| Dimension Management | Create dimension, root/member hierarchy, member sets and rollups. | Show hierarchy tree, selected member detail and bulk upload status. | dimension definitions, members, relationships, sets and rollup rules. |
| Template List / Designer | Create draft, bind dimensions/measures, save draft, preview JSON and publish. | Persist render contract and reload canvas exactly for edit. | template versions, binding groups, axes, measures, cells and render elements. |
| Collection Request | Create request, add item/scope/assignment, send to source. | Create status trail and notification/invitation records. | cycles, requests, items, scope members, template instances and assignments. |
| Invitation Access Monitor | View generated/sent/opened/setup/revoked/expired invitations. | Show safe audit without raw tokens or hashes. | invitation metadata, events and notification outbox. |
| Data Entry / Excel Upload | Fill template or upload sample format, save draft, validate preview, submit. | Create submission version, manifest, staged records and import history. | template render contract, request assignment and ingestion tables. |
| Validation Queue / Report | Run/check validation, inspect failed cells, send back or forward. | Show counts, comparison and affected template cell. | validation runs/results, staged records and previous approved facts. |
| Review / Approval | Review context, previous approved value, comments and approve/reject/send back. | Record action log, approval log and final publish trigger. | review tasks, approval logs, validation and published data. |
| Published Snapshot Dashboard | Filter approved facts by unit/indicator/source/time. | Show latest approved value and drilldown only from fact store. | approved snapshots, observations and dimensions. |
| Publication Workspace | Reuse previous layout, edit A4 PDF, bind latest facts and route for approval. | Auto-save version and generate approved PDF after workflow approval. | published facts, publication layout and DMS/CMS references. |
| CMS / Public Portal | Create/edit/preview/schedule/publish bilingual public pages. | Apply CMS workflow, SEO/friendly URL, link checks and analytics. | Plone content, public dashboard links and analytics events. |
| DMS | Upload, classify, preview, search, retain and archive documents. | Store document versions and apply access/retention policy. | ownCloud metadata and portal references. |
| Logs & Monitor | Search logs, check health, jobs, backups, audit and notification delivery. | Show safe log details and operational evidence. | logs, audit, health, backup and notification records. |

## 18.11 End-to-End User Journey

The end-to-end user journey starts with approved pillar setup and ends with approved facts being used in dashboards, publications, CMS pages and DMS records. The same journey applies to SDG, SWS, ENV, BRICS.

|  |  |  |  |
| --- | --- | --- | --- |
| **Step** | **Actor** | **Action** | **Outcome** |
| 1 | Super Admin / Pillar Admin | Configure pillar/workstream, roles, permissions, branding and public dashboard setting. | Correct users see the correct dashboard and cannot override another pillar. |
| 2 | Metadata Officer | Create/update masters, framework edition, hierarchy levels, nodes, indicators, measures, sources and dimensions. | Controlled metadata is ready for template and request creation. |
| 3 | Template Officer | Create template draft, bind dimension/measure axes, preview JSON/render contract and publish active version. | Approved template version can be used for collection requests and data entry. |
| 4 | Pillar Admin | Create collection request, select template/indicator/scope, assign source officer and send request. | Request status trail, assignment and invitation/notification records are created. |
| 5 | Data Provider | Open login/request-linked page, fill template or upload Excel format, add comments and submit. | Submission version, manifest and staged records are created without exposing raw token/hash/internal IDs. |
| 6 | Validator | Run/check validation, view errors/warnings and compare previous approved data where available. | Clean records move to review; failed records can be sent back for correction. |
| 7 | Reviewer / Approver | Review request, data entry, ingestion and validation context; approve/reject/send back/request clarification. | Final approval creates published snapshot and approved observations. |
| 8 | Publication Officer | Use approved facts in publication workspace, generate PDF draft, route for review and publish approved output. | Publication output is versioned and linked with DMS/CMS where required. |
| 9 | Admin / Public User | View approved dashboards, CMS pages, publications and reports. | Only approved/published data is visible outside internal workflow. |
| 10 | Operations / Auditor | Monitor logs, notifications, jobs, backups, security evidence and audit trails. | Operational and compliance evidence is available for review. |

## 18.12 Production Scope Clarification and Pending SRS Values

The following values clarify Phase I scope and identify only those production details that still need SRS/technical design confirmation. This prevents optional or future items from being read as committed Phase I delivery.

|  |  |  |
| --- | --- | --- |
| **Topic** | **Confirmed FRS Position** | **Pending / SRS Detail** |
| Data upload | Structured ingestion uses Excel/CSV only; 50 MB backend-configurable file size; 3 files per bulk upload; no fixed row count. Scanned/non-machine-readable files may be preserved only as source artifacts and routed through manual entry/resubmission/clarification. | Validation throughput, final server-side configuration values and any OCR change request, if later approved by MoSPI. |
| Resume upload | Not included in Phase I. | None unless MoSPI later approves this as change request. |
| User load | 300 concurrent internal users and 1,500 concurrent public dashboard users. | Performance test sizing and environment tuning. |
| Response time | 3 seconds for normal API/page operations; 60-120 seconds for large report/PDF generation. | Detailed transaction-wise benchmark and test scripts. |
| Dashboard cache | Configurable cache/refresh duration. | Default duration to be finalized in SRS/performance design. |
| Log retention | Application log rotation, archival, retention and purge policy will be defined in SRS/technical design. | Exact retention days/months by log type. |
| Source upload retention | Uploaded source files retained for 2 days. | Archive/purge implementation detail. |
| Published document retention | Published reports/documents retained for 1 year, then archived. | Archive storage and retrieval procedure. |
| Backup retention | Backups retained for 3 months, then archived. | Archive medium and restoration procedure. |
| Backup and DR | Daily/weekly/monthly incremental and full backups, hot/cold backup needs, RPO 0 hours, yearly DR drill. | RTO to be finalized in SRS/technical design. |
| Notification | Email-only Phase I notification channel; reminders configurable; escalation starts after 1 day by default and is configurable. | Email gateway configuration and templates. |
| SMS/WhatsApp | Not included in Phase I unless approved by MoSPI. | Future only through approved change request and communication gateway approval. |
| Identity | Internal application user management only; MFA for privileged users is included. | SSO/LDAP is not included in Phase I unless approved by MoSPI. |
| Security defaults | Password expiry 90 days configurable; failed login lock at 5 attempts configurable; session timeout 30 minutes configurable; admin IP restriction included; Captcha not required. | Final password complexity text and IP allowlist operations procedure. |
| Dashboards, User & Site Analytics | Operational dashboards, drilldowns and approved-data charts included, measure website traffic, engagement, total users, new users, returning users and active users. Monitor sessions, page views, engagement time and bounce/engagement | AI Insights, forecast/regression and aggregated analytics data to improve navigation, content quality, accessibility and public-service delivery are not Phase I unless approved by MoSPI. |
| CMS | SSD integrates/links with Plone where required. CMS page CRUD is handled inside Plone. | Plone endpoint and integration configuration if provided. |
| DMS | SSD integrates/links with ownCloud where required. Preview/search handled by ownCloud. | ownCloud endpoint and integration configuration if provided. |
| Database extensions | Citus and Apache AGE are Phase I production scope. | Exact Citus distribution strategy and AGE graph projection design. |
| Worker/scheduler | Separate email notification service included. | Separate background worker/scheduler service is future scope. |
| Document control | Prepared by, reviewed by, approved by, version/date and client submission date are to be filled before final sign-off. | Names/dates/signatures. |
| Future / approval-based exclusions | SMS, WhatsApp, OCR, Digital Signature, PDF Watermark, AI Insights and SSO/LDAP are excluded from Phase I unless separately approved by MoSPI. | If approved, each item shall be handled through formal scope/change control, SRS update and design impact assessment. |

# 19. Document List to be submitted

* Functional Requirements Specification (FRS)
* Software Requirements Specification (SRS)
* Solution Architecture / Design Document
* UI/UX Specification and Wireframes
* Data Dictionary and Database Design Document
* API and Integration Specification
* Requirement Traceability Matrix (RTM)
* Test Plan, Test Cases and Test Summary Report
* Security, VAPT and Compliance Reports
* Deployment, Rollback and Release Documents
* User Manual and Administrator Manual
* UAT Report and Sign-off
* Project Management Plan, Risk Register and Status Reports
* Source Code and Final Handover Document

# 20. Document Approval

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | **Role** | **Signature** | **Date** |
|  | MoSPI/SSD Reviewer |  |  |
|  | Project Manager |  |  |
|  | Technical Lead |  |  |
|  | Quality/Test Lead |  |  |
