---
name: aws-architecture-diagram
description: Generate AWS architecture diagrams in draw.io format. Activates when the user asks to create, generate, or build an architecture diagram, system diagram, or draw.io diagram for AWS services.
---

## Instructions

Generate a draw.io (.drawio) XML file representing an AWS architecture diagram.

### Layout
- **Left-to-right flow** for data/request path (top-to-bottom is acceptable for vertical architectures)
- Be **consistent** — don't mix flow directions within the same diagram
- **UI/Frontend on the LEFT** (users access from left side)
- **Data sources / external systems on the RIGHT**
- Use horizontal lanes for parallel paths (top lane, bottom lane)
- **Minimum 220px horizontal spacing** between icons (to leave room for edge labels)
- **Minimum 250px vertical spacing** between lanes (so vertical edges don't crowd)
- Secondary/auxiliary services (monitoring, DLQ, error paths) go BELOW the main flow with 280px+ vertical gap
- **Separate control plane from data plane** when relevant
- **Separate management/monitoring** components (CloudWatch, CloudTrail, Config) into a distinct section or sidebar

**Logical Tiers** — organize resources into logical tiers when applicable:
`[Users/Clients] → [Edge/CDN Layer] → [Load Balancing] → [Application Tier] → [Data Tier]`

For example:
- **Edge Layer:** CloudFront, Route 53, WAF
- **Ingress Layer:** ALB/NLB, API Gateway
- **Compute Layer:** EC2, ECS, Lambda, EKS
- **Data Layer:** RDS, DynamoDB, ElastiCache, S3
- **Integration Layer:** SQS, SNS, EventBridge, Step Functions

### Canvas
- Large canvas: `pageWidth="2400" pageHeight="1400"` minimum
- Set `dx="2800" dy="1600"` for proper viewport
- Always include a title block as the first element after the background. Every diagram should include:
  - **Title** — Descriptive name (e.g., "E-Commerce Platform – Production Architecture")
  - **Version/Date** — When the diagram was last updated
  - **Environment** — Production, Staging, Development (when applicable)
```xml
<mxCell value="&lt;b style='font-size:16px'&gt;Diagram Title&lt;/b&gt;&lt;br&gt;&lt;span style='color:#545B64'&gt;Author | Date | Version | Environment&lt;/span&gt;" style="text;html=1;align=left;verticalAlign=top;whiteSpace=wrap;rounded=0;fontSize=14;spacing=10;" vertex="1" parent="1">
  <mxGeometry x="40" y="30" width="500" height="60" as="geometry" />
</mxCell>
```

### Labeling & Annotations
- Use the **official AWS service name** (e.g., "Amazon EC2", "Amazon S3", "AWS Lambda")
- Include the **resource type** where relevant (e.g., "t3.large", "db.r5.xlarge")
- Add **instance counts or scaling information** (e.g., "2× EC2", "Auto Scaling 2–10")
- Use **numbered callouts** to explain the flow sequence (①→②→③→④)
- Add brief text annotations for non-obvious design decisions
- Include a **legend/key** if you use custom colors, line styles, or symbols

### Step Annotation Panel (REQUIRED)
Every diagram MUST include a **numbered step annotation panel** explaining the architecture flow. This matches AWS Reference Architecture PDF standards.

**Panel placement:** Right side of the diagram (x=1800+, width=350) or bottom.

```xml
<mxCell value="&lt;b style='font-size:13px'&gt;Architecture Flow&lt;/b&gt;&lt;br&gt;&lt;br&gt;① User request arrives via Route 53&lt;br&gt;&lt;br&gt;② CloudFront serves cached content&lt;br&gt;&lt;br&gt;③ API Gateway routes the request&lt;br&gt;&lt;br&gt;④ Lambda processes business logic&lt;br&gt;&lt;br&gt;⑤ DynamoDB stores/retrieves data" style="text;html=1;align=left;verticalAlign=top;whiteSpace=wrap;rounded=1;fillColor=#F2F3F4;strokeColor=#E0E0E0;fontSize=12;spacing=10;arcSize=5;" vertex="1" parent="1">
  <mxGeometry x="1800" y="100" width="350" height="280" as="geometry" />
</mxCell>
```

Each numbered step corresponds to a flow edge. Label edges: `value="①"` with `fontSize=14;fontStyle=1;labelBackgroundColor=#ffffff;`

### Diagram Types
Before generating, consider which diagram type best fits the request:

| Diagram Type | Purpose | Key Elements |
|---|---|---|
| High-Level Overview | Executive/stakeholder communication | Major services, data flows, no internal details |
| Detailed Architecture | Implementation blueprint for engineers | Subnets, security groups, instance types, ports |
| Network Diagram | Networking team reference | VPCs, subnets, route tables, peering, TGW, Direct Connect |
| Security Diagram | Security review & compliance | IAM, KMS, WAF, Shield, GuardDuty, security group rules |
| Data Flow Diagram | Data processing & pipeline documentation | Data sources, transformations, storage, analytics |
| Disaster Recovery | DR planning | Multi-Region, failover paths, RPO/RTO annotations |
| Deployment Diagram | CI/CD & DevOps documentation | CodePipeline, CodeBuild, CodeDeploy, ECR |

Create diagrams at different levels of abstraction for different audiences — executives need a high-level view, while engineers need detailed subnet-level diagrams.

### Icon Style
- Icons are from draw.io's built-in `mxgraph.aws4` stencil library — the **official AWS Architecture Icons** (https://aws.amazon.com/architecture/icons/, aligned with April 2026 icon package)
- Icon size: **78x78px** for main services, **65x65px** for secondary
- Use `sketch=0;outlineConnect=0;` on all icons
- Use `strokeColor=#ffffff` on all AWS service icons
- **MUST include `fillColor`** — without it, icons render as invisible/white in PNG export
- Font size: **12px** for labels
- Always include: `fontColor=#232F3E;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;aspect=fixed;`

**Diagram Style Modes:**
- **Reference-Architecture Style (default):** Use subtle colored fills for group boundaries (see Group Boundaries). Best for presentations and documentation.
- **Minimal Style:** All group boxes use `fillColor=none`. Best for quick technical sketches.

**fillColor by AWS service category:**
| Category | fillColor | Services |
|----------|-----------|----------|
| Compute | `#ED7100` | Lambda, EC2, ECS, EKS, Fargate |
| Networking | `#8C4FFF` | VPC, ELB, CloudFront, Route 53, API Gateway |
| Database | `#C925D1` | RDS, DynamoDB, Aurora, ElastiCache |
| Storage | `#3F8624` | S3, EFS, EBS |
| Security | `#DD344C` | IAM, Cognito, KMS, WAF |
| Integration | `#E7157B` | SQS, SNS, EventBridge, Step Functions |
| Analytics | `#8C4FFF` | Kinesis, Athena, Redshift, DataZone |
| Management | `#E7157B` | CloudWatch, CloudTrail |
| AI/ML | `#01A88D` | Bedrock, SageMaker, Amazon Q |
| Customer Experience | `#E7157B` | Connect, Pinpoint, SES |
| Multicloud & Hybrid | `#ED7100` | Outposts, Local Zones, EKS Anywhere |

### Edge Style — CRITICAL FOR CLEAN DIAGRAMS

**Base edge style (all edges):**
```
edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;
```

**Rules for edge labels:**
- Keep labels SHORT (1-2 words max). Use icon labels for detail, not edge labels.
- On horizontal edges: position label ABOVE the line using `verticalAlign=bottom;` in the edge style
- On vertical edges: position label to the LEFT using `align=right;` in the edge style
- Always add `labelBackgroundColor=#F5F5F5;` so labels don't overlap lines
- For edges WITHOUT labels: omit the `value` attribute entirely (don't use `value=""`)

**Edge label positioning (prevents overlap with icons):**
```xml
<mxCell value="Label" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;strokeWidth=2;labelBackgroundColor=#F5F5F5;fontSize=11;" edge="1" source="a" target="b" parent="1">
  <mxGeometry relative="1" as="geometry" />
</mxCell>
```

**For edges that go to services ABOVE or BELOW the main flow:**
- Use explicit exit/entry points to control routing:
  - Exit bottom: `exitX=0.5;exitY=1;exitDx=0;exitDy=0;`
  - Enter top: `entryX=0.5;entryY=0;entryDx=0;entryDy=0;`
  - Exit top: `exitX=0.5;exitY=0;exitDx=0;exitDy=0;`
  - Enter bottom: `entryX=0.5;entryY=1;entryDx=0;entryDy=0;`
- This prevents draw.io from routing lines through other icons

**Edge types:**
- Solid black (`strokeWidth=2`): primary data flow
- Dashed black (`strokeWidth=2;dashed=1;`): optional/async path
- Dashed red (`strokeWidth=2;dashed=1;strokeColor=#DD344C;`): error path

**Color coding for traffic types (use consistently within a diagram):**
- Blue (`strokeColor=#2196F3`): user/client traffic
- Orange (`strokeColor=#FF9800`): management/admin traffic
- Red (`strokeColor=#DD344C`): security events or error paths
- Default black: general data flow

**Bidirectional arrows:**
- Use sparingly; prefer two separate arrows for clarity when different protocols are involved

**Connection best practices:**
- **Avoid crossing lines** wherever possible — rearrange components to minimize crossings
- Use elbowed/orthogonal connectors (already the default style) instead of diagonal lines
- Show VPC Endpoints and PrivateLink connections when private connectivity to AWS services is used
- Show Internet Gateway, NAT Gateway, and Transit Gateway when they are part of the traffic path
- **Label connections with protocols and ports** where helpful (e.g., "HTTPS/443", "SQL/3306", "gRPC")

**Edge attachment (CRITICAL — fixes "green cross" problem):**
- Every edge MUST have both `source="<cell-id>"` and `target="<cell-id>"` attributes referencing valid cell IDs
- NEVER create floating/unattached edges — all edges must be bound to shapes at both ends
- Always include `exitX/exitY` and `entryX/entryY` to define exact connection points on the shape perimeter
- In draw.io, properly attached edges show a "blue dot" anchor; unattached edges show a "green cross"
- If an edge connects to a child inside a container, reference the child's ID directly (not the container)
- **Cross-container edges:** When source and target are in different containers, set the edge's `parent="1"` (root layer) so draw.io can route it across boundaries

**When NOT to label edges:**
- If the flow is obvious from context (e.g., Lambda → DynamoDB doesn't need "Write")
- If the icon labels already explain the relationship
- Prefer fewer, more meaningful labels over labeling every edge

### Two Icon Patterns — CRITICAL

**Pattern 1: Service-level (resourceIcon frame)**
- Style: `sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=<CATEGORY_COLOR>;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.<name>`
- **MUST use `strokeColor=#ffffff`** — without it, the white glyph disappears
- **MUST use `fillColor=<color>`** — without it, icon renders as white/invisible square in PNG export
- Size: 78x78

**Pattern 2: Resource-level (standalone shape)**
- Style: `sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=<CATEGORY_COLOR>;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.<name>`
- **MUST use `strokeColor=none`** — using #ffffff breaks these
- **MUST use `fillColor=<color>`** — same reason as above
- Size: 78x78 or 48x48

**Confusing these patterns guarantees broken icons.**

### Icon Reference Files (load by category as needed)
- `references/aws-icons-compute.md` — Lambda, EC2, ECS, EKS, Fargate
- `references/aws-icons-database.md` — DynamoDB, RDS, Aurora, ElastiCache
- `references/aws-icons-integration.md` — API Gateway, SQS, SNS, EventBridge, Step Functions
- `references/aws-icons-networking.md` — CloudFront, Route 53, VPC, ELB
- `references/aws-icons-storage.md` — S3, EFS, EBS, Glacier, Backup
- `references/aws-icons-security.md` — IAM, Cognito, KMS, WAF, Shield
- `references/aws-icons-analytics-ml.md` — Kinesis, Athena, Bedrock, SageMaker, Amazon Q
- `references/aws-icons-iot-migration-devtools.md` — IoT Core, DMS, CodePipeline
- `references/aws-icons-customer-experience.md` — Connect, Pinpoint, SES
- `references/aws-icons-multicloud-hybrid.md` — Outposts, Local Zones, EKS Anywhere
- `references/aws-icons-common.md` — Groups, general resources, edge styles, base template
- `references/style-guide.md` — Color palette, typography, spacing, do's and don'ts

**Always look up icons from reference files. Never guess icon names.**

**DEPRECATED Icons (April 2026) — Avoid in new diagrams:**
`quicksight`, `eks_cloud`, `iot_analytics`, `quantum_ledger_database`, `alexa_for_business`, `elastic_transcoder`, `private_5g`, `app_stream`

**Fallback for unmapped services:** If a service is NOT found in any reference file, use this generic AWS cloud icon with the service name as label:
```
sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#232F3E;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.general_AWScloud
```
Never render an unknown service as a plain colored rectangle with no label.

### Group Boundaries

**Reference-Architecture Style (default)** — uses subtle colored fills:
- **AWS Cloud:** `shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_aws_cloud_alt;strokeColor=#232F3E;fillColor=#F2F3F4;container=1;dropTarget=1;`
- **Account:** `shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_account;strokeColor=#CD2264;fillColor=#FDF1F6;container=1;dropTarget=1;`
- **On-premise:** `shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_on_premise;strokeColor=#5A6C86;fillColor=#F2F3F4;container=1;dropTarget=1;`
- **VPC:** `shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_vpc2;strokeColor=#8C4FFF;fillColor=#F5F0FF;container=1;dropTarget=1;`
- **Availability Zone:** `shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_availability_zone;strokeColor=#007FAA;fillColor=#FFFFFF;container=1;dropTarget=1;`
- **Subnet (public):** `shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_public_subnet;strokeColor=#248814;fillColor=#E9F3E6;container=1;dropTarget=1;`
- **Subnet (private):** `shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_private_subnet;strokeColor=#147EBA;fillColor=#E6F0F7;container=1;dropTarget=1;`
- **Security Group:** `shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_security_group;strokeColor=#DD344C;fillColor=none;container=1;dropTarget=1;`
- **Logical groups:** Simple dashed boxes: `whiteSpace=wrap;html=1;fillColor=none;dashed=1;dashPattern=8 8;container=1;dropTarget=1;`

> For **Minimal Style**, replace all fillColor values with `fillColor=none`.

**Container nesting (CRITICAL for grouping):**
- ALL boundary/group shapes MUST include `container=1;dropTarget=1;` in their style
- Child cells inside a boundary MUST set `parent="<boundary-cell-id>"` instead of `parent="1"`
- This ensures moving a boundary moves all its children together
- Example:
```xml
<mxCell id="vpc1" value="VPC" style="shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.group_vpc2;strokeColor=#8C4FFF;fillColor=none;container=1;dropTarget=1;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="800" height="500" as="geometry" />
</mxCell>
<mxCell id="lambda1" value="Lambda" style="shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.lambda;strokeColor=#ffffff;" vertex="1" parent="vpc1">
  <mxGeometry x="50" y="50" width="78" height="78" as="geometry" />
</mxCell>
```
Note: child geometry coordinates are **relative to the parent container**, not the canvas.

### PNG Export Background Fix
Place a full-canvas rectangle as the FIRST element (lowest z-order):
```xml
<mxCell value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=none;" vertex="1" parent="1">
  <mxGeometry x="0" y="0" width="2400" height="1400" as="geometry" />
</mxCell>
```
This prevents black background on PNG export. Use `strokeColor=none` (not E0E0E0).

### Multi-page Diagrams
For complex architectures, use multiple pages (tabs) in one .drawio file:
```xml
<mxfile>
  <diagram id="overview" name="Overview">...</diagram>
  <diagram id="networking" name="Networking Detail">...</diagram>
  <diagram id="data-flow" name="Data Flow">...</diagram>
</mxfile>
```
- Page 1: High-level overview (service-level icons only)
- Page 2+: Detail views (resource-level icons, subnet layouts, etc.)

### Layers for Multi-Layer Architectures
For complex or multi-tier diagrams, use **draw.io layers** to organize elements and reduce visual clutter. Layers allow toggling visibility of different architectural concerns (e.g., networking, security, monitoring) within a single page.

**When to use layers:**
- Diagrams with overlapping concerns (e.g., data flow + security controls on the same view)
- Multi-tier architectures where showing everything at once is overwhelming
- Presentations that reveal architecture incrementally

**How to structure layers:**
- **Background layer** (bottom): canvas background, title block, legend
- **Infrastructure layer**: VPCs, subnets, availability zones, networking
- **Application layer**: compute, containers, serverless functions
- **Data layer**: databases, caches, storage
- **Security layer** (optional): WAF, Shield, security groups, IAM boundaries
- **Monitoring layer** (optional): CloudWatch, CloudTrail, alarms

**draw.io XML for layers:**
Each layer is an `mxCell` with `parent="0"`. Child elements reference the layer ID instead of `"1"`:
```xml
<mxCell id="0" />
<mxCell id="infra-layer" value="Infrastructure" parent="0" />
<mxCell id="app-layer" value="Application" parent="0" visible="1" />
<mxCell id="security-layer" value="Security" parent="0" visible="0" />
<!-- Elements on the infrastructure layer -->
<mxCell id="vpc1" value="VPC" style="..." vertex="1" parent="infra-layer">
  <mxGeometry ... />
</mxCell>
<!-- Elements on the application layer -->
<mxCell id="lambda1" value="Lambda" style="..." vertex="1" parent="app-layer">
  <mxGeometry ... />
</mxCell>
```
- Set `visible="0"` on layers that should be hidden by default
- Users can toggle layers via **View → Layers** in draw.io Desktop
- Reference: https://www.drawio.com/doc/layers

### Edge Legend (optional, for complex diagrams)
Place below the title block if the diagram has multiple edge types:
- Solid line: primary data flow
- Dashed line: optional/async
- Red dashed: error path

### File Splitting
Since draw.io XML can be large, split creation across multiple tool calls:
1. Header + left side (frontend, delivery layer)
2. Middle (processing lambdas, database)
3. Right side (ingest, messaging, data sources)
4. Bottom (optional/outbound flows) + close XML

### Audience Mode
Before generating, assess the target audience:
- **Technical**: Use service names, protocol labels (HTTPS, gRPC), CIDR blocks, instance types
- **Non-technical**: Use action labels ("Store Data", "Send Notification"), hide implementation details, use numbered flow (① ② ③)

If unclear, ask: "Technical audience or executive/non-technical?"

### Numbered Flow Edges (for non-technical mode)
Instead of technical labels, show flow order with circled numbers:
- Flow A: ① → ② → ③ → ④ (white circled numbers)
- Flow B: ❶ → ❷ → ❸ → ❹ (black circled numbers for second flow)

Use edge labels: `value="①"` with `fontSize=14;fontStyle=1;labelBackgroundColor=#ffffff;`

### Companion Guide
After generating the .drawio file, also generate a markdown guide:
- Same filename with `.md` extension (e.g., `serverless-api.drawio` + `serverless-api.md`)
- Contents: diagram title, flow description (numbered steps matching edge labels), service list with purpose, key design decisions

### Two-Step Edit Approach
After generating the initial .drawio file:
1. **Export to PNG** using the draw.io CLI (see Output section)
2. **Review the PNG** visually — check for empty/broken icons, overlapping edges, misaligned labels
3. **Fix issues** in the .drawio XML and re-export

This catches rendering problems (wrong stencil names, broken styles) that are invisible in raw XML.

### Icon Name Gotchas — CRITICAL
draw.io stencil names do NOT always match current AWS service names. Services that were renamed keep their legacy stencil names:

| AWS Service Name | draw.io resIcon name | Why |
|---|---|---|
| Amazon OpenSearch Service | `elasticsearch_service` | Renamed from Elasticsearch in 2021; `opensearch_service` also works |
| Amazon EventBridge | `eventbridge` | Was CloudWatch Events |
| AWS Fargate | `fargate` | Correct |
| VPC Peering | `peering` | Resource-level: `shape=mxgraph.aws4.peering;strokeColor=none` — NOT `vpc_peering` or `peering_connection` (those render as blank squares) |
| Amazon MSK | `managed_streaming_for_kafka` | NOT `msk` (renders as blank square) |
| IAM Identity Center | `single_sign_on` | NOT `iam_identity_center` (renders as blank square) |

**Rule:** Always verify icon names from the reference files. If a service icon renders as an empty box, the stencil name is wrong. Check the draw.io source at `src/main/webapp/js/diagramly/sidebar/Sidebar-AWS4.js` for the canonical name.

### Validation Step
After generating XML, mentally verify:
1. Every `resIcon=` value exists in the reference files
2. Service-level icons have `strokeColor=#ffffff`
3. Resource-level icons have `strokeColor=none`
4. No XML comments present
5. All cell IDs are unique
6. Every edge has `<mxGeometry relative="1" as="geometry" />`
7. No icon uses a guessed stencil name — all verified against reference files
8. Every edge has both `source` and `target` attributes referencing valid cell IDs (no floating edges)
9. All group/boundary shapes include `container=1;dropTarget=1;` in their style
10. Children inside boundaries use `parent="<boundary-id>"` (not `parent="1"`)
11. A step annotation panel is present explaining the architecture flow
12. No deprecated icon names are used (see DEPRECATED Icons list)
13. Group boundaries use appropriate fillColor for the chosen style mode

### Output
- Save with descriptive filename ending in `.drawio`
- Open with `open` command (macOS) or `xdg-open` (Linux) after creation
- For PNG/SVG/PDF export, use draw.io CLI:
  - macOS: `/Applications/draw.io.app/Contents/MacOS/draw.io -x -f png -e -b 10 -o output.drawio.png input.drawio`
  - Linux: `drawio -x -f png -e -b 10 -o output.drawio.png input.drawio`
  Flags: `-x` export, `-f` format, `-e` embed diagram XML, `-b 10` border
- Exported files use double extension: `name.drawio.png` (signals embedded XML, re-editable in draw.io)

### XML Well-formedness (CRITICAL)
- **NEVER include XML comments (`<!-- -->`)** — they cause parse errors
- Escape special characters in values: `&amp;` `&lt;` `&gt;` `&quot;`
- Always use unique `id` values for each mxCell
- Every edge MUST have `<mxGeometry relative="1" as="geometry" />` as child element
- Basic structure must include root cells `id="0"` and `id="1"` (parent="0")

### Official Reference
- Full XML/style reference: https://raw.githubusercontent.com/jgraph/drawio-mcp/main/shared/xml-reference.md
- Style properties: https://raw.githubusercontent.com/jgraph/drawio-mcp/main/shared/style-reference.md
- AWS Architecture Icons (April 2026): https://aws.amazon.com/architecture/icons/
- Style guide: See `references/style-guide.md` for complete color palette, typography, and spacing constants
