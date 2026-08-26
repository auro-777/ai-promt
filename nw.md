Build a complete **local, interactive enterprise architecture web application** based on the attached architecture diagram.

The attached diagram is the visual and structural reference. Do NOT simply display the image. Recreate the architecture as an interactive web application using HTML/SVG/React components so that every major component can be clicked, expanded, animated, and explored.

The application is intended as a **learning and interview-preparation tool for a Senior SRE / DevOps / Cloud / Network / Security Engineer**.

The application must run completely locally using:

* Node.js
* npm
* React
* TypeScript
* Vite
* React Router
* React Flow or an equivalent interactive diagram library
* Tailwind CSS
* Framer Motion for animations
* Lucide React or equivalent icon library

Do not require a backend.

All architecture information should be represented as structured local data/JSON/TypeScript objects so that components can be reused across AWS, Azure, GCP, SaaS, networking, security, and identity pages.

---

# 1. PRIMARY OBJECTIVE

Create an interactive architecture explorer where the user starts on:

**Enterprise Organization — High-Level Network, Cloud, Identity, Security & Access Architecture**

The landing page should visually resemble the supplied reference diagram.

The user should be able to:

* Zoom in/out
* Pan around
* Click major architecture domains
* Hover over components
* See descriptions/tooltips
* Follow animated traffic flows
* Click AWS → open detailed AWS architecture
* Click Azure → open detailed Azure architecture
* Click GCP → open detailed GCP architecture
* Click Identity → open identity architecture
* Click SaaS → open SaaS access architecture
* Click Security → open security architecture
* Click Observability → open monitoring architecture
* Click CI/CD / Artifact → open software supply-chain architecture
* Click a specific service → see what it does and how it connects to other services

Provide breadcrumb navigation such as:

Home
→ Cloud
→ AWS
→ VPC
→ Private Subnet
→ EC2

Allow the user to return to the previous architecture level.

---

# 2. LANDING PAGE

Create the landing page as a large architecture canvas.

Title:

**Enterprise Organization — High-Level Network, Cloud, Identity, Security & Access Architecture**

The landing page should have these major zones:

1. Corporate Users / Endpoints
2. Endpoint Security
3. SASE / Zero Trust
4. Enterprise Identity
5. Corporate Network / VDI
6. Cloud Connectivity
7. Cloud Landing Zones
8. AWS
9. Azure
10. GCP
11. SaaS Applications
12. Internet Egress
13. Security & Governance
14. Observability
15. Incident Management
16. CI/CD / Artifact Governance
17. Privileged Access
18. Application Layer
19. Data / Storage Layer

Use visually distinct boundaries for:

* Corporate environment
* Identity environment
* Cloud environment
* SaaS environment
* Internet
* Security controls
* Observability

---

# 3. USER ENTRY FLOW

The most important flow on the landing page is:

Corporate User
↓
Corporate Laptop / Desktop
↓
Endpoint Security
↓
SASE / ZTNA
↓
Enterprise Identity Provider
↓
MFA / Conditional Access
↓
Corporate Network / VDI where applicable
↓
Cloud / SaaS access policy
↓
AWS / Azure / GCP / SaaS

Animate this flow when the user clicks:

**"Show User Access Flow"**

The animation should highlight each component sequentially.

Display a small explanation panel:

### User Access Flow

1. User starts from a managed corporate endpoint.
2. Endpoint security validates device posture.
3. SASE/ZTNA or VPN establishes the appropriate secure access path.
4. Identity provider authenticates the user.
5. MFA and conditional-access policies are evaluated.
6. Authorization determines what the user can access.
7. Network policy determines the allowed path.
8. Application-level authentication and authorization are enforced.
9. Activity is logged and monitored.

Clearly distinguish:

**Authentication = Who are you?**

**Authorization = What are you allowed to access?**

**Network connectivity = How does traffic reach the destination?**

---

# 4. CORPORATE ENDPOINT PAGE

Create a drill-down page:

**Corporate Endpoint Architecture**

Show:

User
→ Laptop/Desktop
→ Endpoint Agent
→ SASE/ZTNA
→ Enterprise Network

Possible endpoint/security technologies should be displayed as alternatives:

* Palo Alto GlobalProtect
* Netskope Client
* Zscaler Client Connector
* CrowdStrike Falcon
* Microsoft Defender for Endpoint
* Endpoint DLP
* EDR
* Device Certificate
* Device Compliance

Do not imply all products are deployed simultaneously.

Each technology card should contain:

* What it is
* Why an enterprise uses it
* Where it runs
* What traffic it controls
* How it interacts with identity
* Whether it is endpoint, network, identity, or security functionality

---

# 5. SASE / ZTNA PAGE

Create:

**SASE / Zero Trust Access Architecture**

Show alternatives:

* Netskope
* Zscaler
* Palo Alto Prisma Access
* Cloudflare Zero Trust
* Cisco Secure Access

Explain:

* Secure Web Gateway
* CASB
* DLP
* URL filtering
* Malware inspection
* TLS inspection
* ZTNA
* Device posture
* Identity-based policy
* Risk-based access
* Private application access
* Internet access control

Provide two animated flows.

### Traditional VPN

User
→ VPN Client
→ VPN Gateway
→ Corporate Network
→ Application

### Modern ZTNA

User
→ Identity Provider
→ Device Posture
→ ZTNA Policy
→ Private Application

Clearly explain that ZTNA does not necessarily place the user directly onto the entire corporate network.

---

# 6. IDENTITY PAGE

Create:

**Enterprise Identity & Access Architecture**

Possible IdPs:

* Microsoft Entra ID
* Okta
* Ping Identity
* ADFS for legacy environments

Show:

User
→ IdP
→ MFA
→ Conditional Access
→ Application

Authentication protocols:

* SAML 2.0
* OAuth 2.0
* OpenID Connect

Identity controls:

* MFA
* RBAC
* Group-based access
* Conditional Access
* Privileged Identity Management
* Just-in-Time access
* Service identities
* Managed identities
* API credentials

Create an interactive explanation:

### SAML Example

User
→ Enterprise IdP
→ SAML Assertion
→ SaaS Application
→ Application RBAC

### OIDC Example

User
→ IdP
→ Authorization Code
→ Token
→ Application

### OAuth Example

Application
→ Authorization Server
→ Access Token
→ API

Make these generic architecture examples rather than claiming a specific organization uses one particular protocol.

---

# 7. CLOUD LANDING ZONE PAGE

Create:

**Enterprise Cloud Landing Zone**

Show three major cloud providers:

### AWS

* AWS Organizations
* Management Account
* Security Account
* Log Archive Account
* Shared Services Account
* Network Account
* Development Accounts
* Test Accounts
* Production Accounts

### Azure

* Entra ID
* Management Groups
* Platform subscriptions
* Connectivity subscription
* Management subscription
* Identity subscription
* Production subscriptions
* Non-production subscriptions

### GCP

* Organization
* Folders
* Shared Services
* Security
* Logging
* Development Projects
* Test Projects
* Production Projects

Explain:

**Landing Zone = standardized cloud foundation containing governance, identity, networking, logging, security, and account/subscription/project structure.**

---

# 8. AWS PAGE

When the user clicks AWS from the landing page, open:

**AWS Enterprise Architecture**

The AWS page should contain an interactive VPC diagram.

Example:

VPC
**10.0.0.0/16**

Two Availability Zones:

### Availability Zone A

Public Subnet
Private Application Subnet
Private Database Subnet

### Availability Zone B

Public Subnet
Private Application Subnet
Private Database Subnet

Show:

Internet Gateway
NAT Gateway
Route Tables
Network ACLs
Security Groups
Load Balancer
EC2
ECS/EKS
RDS
ElastiCache/Redis
VPC Endpoints
CloudWatch
CloudTrail
VPC Flow Logs

---

# 9. AWS VPC DRILL DOWN

When the user clicks:

**VPC**

open:

**AWS VPC — Detailed Architecture**

Explain:

VPC
→ CIDR
→ Availability Zones
→ Subnets
→ Route Tables
→ Internet Gateway
→ NAT Gateway
→ Security Groups
→ Network ACLs
→ VPC Endpoints

Provide interactive cards for each.

For example:

### Internet Gateway

Explain:

* Connects a VPC to the internet
* Used for internet-routable resources
* Works with route tables
* Does not automatically make every resource public

### NAT Gateway

Explain:

* Used primarily for outbound internet connectivity from private subnets
* Private subnet route table sends default traffic to NAT Gateway
* NAT Gateway sends traffic toward the Internet Gateway
* Internet cannot initiate an inbound connection through NAT Gateway to the private resource

### Security Group

Explain:

* Stateful
* Associated with resources such as EC2
* Controls allowed inbound/outbound traffic

### Network ACL

Explain:

* Stateless
* Associated with subnets
* Supports subnet-level traffic filtering

---

# 10. AWS ROUTING PAGE

Create a dedicated route-table visualization.

Example:

### Public Route Table

10.0.0.0/16 → local

0.0.0.0/0 → Internet Gateway

### Private Route Table

10.0.0.0/16 → local

0.0.0.0/0 → NAT Gateway

Animate packet movement when the user clicks:

**"Show Traffic"**

For example:

Private EC2
→ Private Route Table
→ NAT Gateway
→ Internet Gateway
→ Internet

Clearly show that this is outbound traffic.

---

# 11. AWS USER ACCESS SCENARIOS

Create an interactive scenario selector.

### Scenario 1 — User Accesses AWS Console

User
→ Corporate Endpoint
→ SASE/ZTNA
→ Enterprise IdP
→ MFA
→ AWS IAM Identity Center / SSO
→ AWS Account
→ AWS Console

Explain that console authentication and workload network connectivity are separate concepts.

---

### Scenario 2 — User Accesses Private AWS Application

User
→ Endpoint
→ SASE/ZTNA or VPN
→ Identity validation
→ Private access policy
→ AWS network
→ Load Balancer
→ Private Application
→ Database

---

### Scenario 3 — Administrator Accesses EC2

Admin
→ MFA
→ PAM
→ Bastion / AWS Systems Manager Session Manager
→ Private EC2

Emphasize:

**Do not expose private EC2 instances directly to the public internet merely for administrative access.**

---

# 12. AZURE PAGE

Create:

**Azure Enterprise Architecture**

Show:

Management Groups
→ Subscriptions
→ Hub VNet
→ Spoke VNets

Hub:

* Azure Firewall
* VPN Gateway
* ExpressRoute Gateway
* DNS
* Shared Services

Spoke:

* Application subnet
* Integration subnet
* Private Endpoint subnet
* Database subnet

Services:

* Azure App Service
* Azure Functions
* Azure SQL
* Storage Account
* Key Vault
* Service Bus
* API Management
* Azure Data Factory
* Azure Cache for Redis
* Managed Identity
* Log Analytics
* Azure Monitor

Make every component clickable.

---

# 13. AZURE USER-TO-APPLICATION FLOW

Create scenario:

User
→ Corporate Endpoint
→ SASE/ZTNA
→ Entra ID
→ MFA
→ Conditional Access
→ Application

For a private Azure application:

User
→ ZTNA / VPN / ExpressRoute path
→ Hub VNet
→ Azure Firewall
→ Spoke VNet
→ Application
→ Private Endpoint / Database

Explain where authentication happens and where network traffic travels.

---

# 14. GCP PAGE

Create:

**GCP Enterprise Architecture**

Show:

Organization
→ Folder
→ Project
→ Shared VPC

Include:

* VPC
* Subnets
* Cloud Router
* Cloud NAT
* Firewall Rules
* Load Balancer
* Compute Engine
* GKE
* Cloud SQL
* Cloud Storage
* Secret Manager
* Cloud Logging
* Cloud Monitoring
* IAM

Create drill-down pages for:

GCP Organization
GCP Project
VPC
Subnet
Firewall
Cloud NAT
GKE
Cloud SQL
IAM

---

# 15. SAAS ARCHITECTURE PAGE

Important architectural rule:

**Do not place SaaS applications physically inside the enterprise VPC unless the architecture explicitly uses private connectivity.**

Create a separate:

**Enterprise SaaS Access Architecture**

Examples:

* JFrog Artifactory
* Snyk
* GitHub
* ServiceNow
* Splunk Cloud
* Datadog
* Microsoft 365

Show:

User
→ Enterprise IdP
→ SAML/OIDC
→ SaaS

For workload/API access:

CI/CD Runner
→ HTTPS/API
→ SaaS

Possible network path:

Workload
→ NAT / Firewall
→ Secure Web Gateway / Proxy
→ Internet
→ SaaS

Or:

Workload
→ Private connectivity
→ SaaS

depending on the SaaS provider's capabilities.

---

# 16. JFROG EXAMPLE

Create a detailed example:

Developer
→ GitHub
→ GitHub Actions Runner
→ Artifactory
→ Xray
→ Approved Artifact
→ Deployment

Show:

* Repository
* Artifact repository
* Xray
* Vulnerability scanning
* Curation
* Authentication
* RBAC
* API access

Also show:

Direct package download from public internet
→ Restricted / Blocked

and:

Approved dependency
→ Artifactory
→ CI/CD

Explain that Artifactory acts as a controlled artifact/dependency source.

---

# 17. GITHUB RUNNER EXAMPLE

Create a dedicated architecture page:

**GitHub Enterprise Self-Hosted Runner Architecture**

Show:

Developer
→ GitHub Enterprise
→ GitHub Actions
→ Runner Group
→ Self-Hosted Runner
→ AWS EC2 / Azure VM

Runner states:

* Online
* Offline
* Busy
* Idle
* Failed registration
* Degraded

Create an animated runner-health dashboard.

Show example Grafana-style panels:

* Total runners
* Online runners
* Offline runners
* Busy runners
* Idle runners
* Windows runners
* Linux runners
* AIX runners
* Runner groups
* Runner availability

Explain the generic data path:

GitHub / GitHub API
→ Metrics Collection / Automation
→ Metrics Store
→ Grafana Dashboard

Do not claim that GitHub itself natively sends all runner metrics directly to Grafana. Present the collector/API/exporter layer explicitly.

---

# 18. INTERNET EGRESS ARCHITECTURE

Create:

**Enterprise Internet Egress Control**

Example:

Private Workload
→ Route Table
→ NAT Gateway
→ Firewall / Proxy / SASE
→ Internet

Show policy:

Production workloads
→ Restricted Internet Access

Developer workstation
→ Secure Web Gateway
→ URL filtering
→ DLP
→ Malware inspection

Software dependencies:

Build
→ Artifactory
→ Xray / Curation
→ Approved Dependency

Avoid:

Build
→ Direct Public PyPI/npm/Maven
→ Uncontrolled dependency

---

# 19. SECURITY ARCHITECTURE

Create a security page containing:

Identity Security
Network Security
Endpoint Security
Application Security
Data Security
Cloud Security
Supply Chain Security

Controls:

* IAM
* RBAC
* MFA
* PAM
* Secrets Management
* KMS
* Encryption
* DLP
* CASB
* WAF
* Firewall
* Security Groups
* NACL
* Vulnerability Scanning
* SAST
* DAST
* SBOM
* Artifact Scanning
* Policy as Code
* CSPM
* SIEM

Allow the user to click each control and get:

**What it is → Why it exists → Where it operates → Example → What problem it prevents**

---

# 20. OBSERVABILITY PAGE

Create:

**Enterprise Observability Architecture**

Sources:

Infrastructure Metrics
Application Metrics
Logs
Traces
Audit Logs
Cloud Events
Network Flow Logs

→ Collection Layer

→ Observability Platform

Possible tools:

* Prometheus
* Grafana
* CloudWatch
* Azure Monitor
* Log Analytics
* Splunk
* Datadog

Again, treat them as alternatives/examples.

Show:

Metrics → Dashboards → Alerts → Incident Management

Logs → SIEM → Security Operations

---

# 21. INCIDENT MANAGEMENT PAGE

Create:

Monitoring
↓
Alert
↓
Incident
↓
On-Call Engineer
↓
Incident Bridge
↓
Engineering / Network / Cloud / Security
↓
Service Restoration
↓
RCA
↓
Preventive Automation

Possible tools:

* ServiceNow
* PagerDuty
* Opsgenie
* Splunk On-Call

Allow the user to click each stage and understand its purpose.

---

# 22. NEW SAAS ONBOARDING PAGE

Create an interactive workflow:

1. Business Request
2. Security Review
3. Architecture Review
4. Data Classification
5. Identity / SSO Integration
6. Network Connectivity Decision
7. RBAC
8. DLP / Security Controls
9. Logging / SIEM
10. Compliance Review
11. Production Approval
12. Go-Live

When the user clicks each stage, show questions an architect should ask.

For example:

### Network

* Is public internet access acceptable?
* Does the SaaS support private connectivity?
* Is IP allowlisting available?
* Does it require a proxy?
* Where does traffic originate?
* Is inbound connectivity required?
* Is outbound connectivity sufficient?

### Identity

* Does the application support SAML?
* Does it support OIDC?
* Does it support SCIM?
* Is MFA enforced through the enterprise IdP?
* How are roles mapped?
* How are service accounts handled?

### Security

* What data is stored?
* Where is the data hosted?
* Is encryption supported?
* Are audit logs available?
* Can logs be integrated with SIEM?
* Does the vendor provide vulnerability/compliance reports?

---

# 23. GLOBAL ANIMATION SYSTEM

Create a reusable traffic animation engine.

Traffic types:

### Blue

User/application traffic

### Purple

Authentication/identity

### Orange

Management/admin traffic

### Green

Monitoring/logging/telemetry

### Red

Security/block/denied traffic

### Dashed

Optional or alternative path

When the user clicks:

**Play User Flow**

animate:

User
→ Endpoint
→ SASE
→ IdP
→ Cloud
→ Application

When clicking:

**Play Authentication Flow**

animate:

User
→ IdP
→ MFA
→ Token/SAML Assertion
→ Application

When clicking:

**Play Application Traffic**

animate:

User
→ Load Balancer
→ Application
→ Database

When clicking:

**Play Monitoring Flow**

animate:

Application
→ Metrics/Logs
→ Collector
→ Observability
→ Alert
→ Incident Management

When clicking:

**Play Security Block**

animate:

Workload
→ Unauthorized Internet Destination
→ Firewall/Proxy
→ BLOCKED

---

# 24. SERVICE DETAILS PANEL

Every major node should open a reusable detail panel.

Example:

### AWS NAT Gateway

**Category:** Networking

**Purpose:** Provides outbound connectivity from private subnets.

**Located in:** Public subnet.

**Receives traffic from:** Private subnet route table.

**Connects to:** Internet Gateway.

**Inbound internet initiated connection:** Not permitted through NAT Gateway.

**Common use case:** Private EC2 instances downloading approved updates or accessing external services.

**Interview question:**
"Why would you use NAT Gateway instead of an Internet Gateway directly from a private subnet?"

Provide a concise answer.

Use this same format for all major services.

---

# 25. INTERVIEW MODE

Add a toggle:

**Architecture Mode | Interview Mode**

In Interview Mode, clicking a component displays:

* What is it?
* Why is it used?
* Where does it sit?
* What connects to it?
* What security controls apply?
* Common failure scenarios
* Interview question
* 30-second answer

Example:

### Interview Question

"What is the difference between a Security Group and Network ACL?"

Show a concise interview-ready answer.

This mode is extremely important because this application is intended for interview preparation.

---

# 26. SEARCH

Add global search.

Search terms such as:

VPC
NAT Gateway
SAML
OIDC
VPN
ExpressRoute
Direct Connect
Security Group
NACL
Terraform
JFrog
Xray
GitHub Actions
Runner
Grafana
SaaS
IdP
MFA
Bastion
Private Endpoint

should locate the component and navigate to its architecture page.

---

# 27. ARCHITECTURE RELATIONSHIP GRAPH

Every service should contain relationship information.

Example:

EC2:

dependsOn:

* VPC
* Subnet
* Route Table
* Security Group

connectsTo:

* Load Balancer
* RDS
* NAT Gateway

observedBy:

* CloudWatch
* CloudTrail
* VPC Flow Logs

This should allow the application to display:

**"What connects to this component?"**

---

# 28. RESPONSIVE DESIGN

Desktop should provide the full architecture canvas.

Tablet should provide a simplified architecture view.

Mobile should convert the architecture into expandable cards and flows rather than trying to display the entire diagram simultaneously.

Use:

* Zoom
* Pan
* Collapse/expand
* Breadcrumbs
* Search
* Side panel
* Modal details

---

# 29. DESIGN LANGUAGE

The visual style should resemble a professional enterprise architecture tool.

Use:

* White/light background
* Dark text
* AWS orange accents
* Azure blue accents
* GCP multicolor accents
* Security red
* Identity purple
* Observability green
* Network blue

Use subtle borders and shadows.

Avoid excessive decoration.

The architecture must remain readable.

---

# 30. IMPORTANT ARCHITECTURAL ACCURACY RULES

Do not make these mistakes:

1. Do not put SaaS applications inside the enterprise VPC by default.
2. Do not imply that authentication automatically provides network connectivity.
3. Do not imply that NAT Gateway allows inbound internet access to private workloads.
4. Do not confuse Security Groups with Network ACLs.
5. Do not confuse SAML authentication with network connectivity.
6. Do not treat ZTNA as necessarily equivalent to a traditional VPN.
7. Do not imply that every AWS resource must be in a public subnet.
8. Do not expose private EC2/database resources directly to the internet.
9. Do not claim that GitHub automatically provides every Grafana metric without an API/exporter/collector layer.
10. Do not assume every organization uses every vendor shown.
11. Clearly label vendor technologies as examples/options when appropriate.
12. Distinguish control-plane/API traffic from application/data-plane traffic wherever useful.

---

# 31. PROJECT STRUCTURE

Create a clean project structure similar to:

src/
components/
ArchitectureCanvas
ArchitectureNode
DetailPanel
FlowAnimation
ServiceCard
Breadcrumbs
Search
Legend
InterviewMode
pages/
Home
Aws
Azure
Gcp
Identity
Network
Security
Saas
Observability
Github
IncidentManagement
Onboarding
data/
aws.ts
azure.ts
gcp.ts
identity.ts
network.ts
security.ts
saas.ts
github.ts
flows/
userAccess.ts
authentication.ts
applicationTraffic.ts
monitoring.ts
securityBlock.ts
types/
architecture.ts
App.tsx
main.tsx

Use reusable components rather than duplicating architecture code.

---

# 32. REQUIRED NPM COMMANDS

The generated project must support:

npm install

npm run dev

npm run build

npm run preview

The application must run locally without requiring a backend.

---

# 33. FINAL ACCEPTANCE TEST

After implementation, verify these flows:

### Test 1

Open Home.

The complete enterprise architecture is visible.

### Test 2

Click AWS.

AWS architecture opens.

### Test 3

Click VPC.

VPC details open.

### Test 4

Click NAT Gateway.

NAT Gateway details and traffic flow appear.

### Test 5

Click Azure.

Azure landing zone appears.

### Test 6

Click GCP.

GCP organization/project/VPC architecture appears.

### Test 7

Click JFrog.

SaaS architecture and authentication flow appear.

### Test 8

Click Identity.

SAML/OIDC/MFA flows appear.

### Test 9

Click "Play User Flow."

The user-to-application path animates.

### Test 10

Click "Play Monitoring Flow."

Metrics/logs flow toward observability and incident management.

### Test 11

Enable Interview Mode.

Clicking a service provides an interview-ready explanation.

### Test 12

Search for "NAT Gateway."

The application navigates directly to the relevant architecture and highlights the component.

---

# 34. MOST IMPORTANT UX REQUIREMENT

The landing page should answer:

**"How does a corporate user get from their laptop to an AWS/Azure/GCP/SaaS application?"**

Then the drill-down pages should answer:

**"What happens inside the cloud?"**

Then the service pages should answer:

**"What does each component do?"**

Then Interview Mode should answer:

**"How do I explain this to an interviewer?"**

The user should be able to move naturally through:

**Organization → User → Endpoint → Security → Identity → Network → Cloud → VPC/VNet → Subnet → Application → Database → Monitoring → Security → Incident**

The final result should feel like an interactive **enterprise architecture map + cloud/network learning tool + SRE interview preparation application**, rather than a static diagram.
