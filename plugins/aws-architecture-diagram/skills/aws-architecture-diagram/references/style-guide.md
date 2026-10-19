# AWS Architecture Diagram Style Guide

> Based on AWS Reference Architecture diagram best practices (data-mesh-with-amazon-datazone, sd-wan-deployment-models).
> Updated: 2026-05-28

## Diagram Styles

This skill supports two visual styles for group boundaries:

### Reference-Architecture Style (default)
Matches the visual quality of official AWS Reference Architecture PDFs. Uses subtle colored fills for boundaries to create visual depth and hierarchy.

**When to use:** Presentation-quality diagrams, executive communication, AWS Well-Architected reviews, documentation.

### Minimal Style
Uses transparent (`fillColor=none`) backgrounds for all group boundaries. Cleaner but less visual hierarchy.

**When to use:** Quick technical sketches, whiteboard-style diagrams, diagrams with many overlapping boundaries.

## Color Palette

### Service Category Colors (fillColor for icons)
| Category | fillColor | Example Services |
|----------|-----------|-----------------|
| Compute & Containers | `#ED7100` | EC2, Lambda, ECS, EKS, Fargate |
| Database | `#C925D1` | DynamoDB, RDS, Aurora, ElastiCache |
| Application Integration | `#E7157B` | API Gateway, SQS, SNS, EventBridge, Step Functions |
| Management & Governance | `#E7157B` | CloudWatch, CloudFormation, CloudTrail |
| Networking & Content Delivery | `#8C4FFF` | CloudFront, Route 53, VPC, ELB |
| Storage | `#7AA116` | S3, EBS, EFS, Glacier |
| Security, Identity & Compliance | `#DD344C` | IAM, Cognito, WAF, Shield, GuardDuty |
| Analytics | `#8C4FFF` | Athena, Redshift, Kinesis, Glue |
| AI / Machine Learning | `#01A88D` | Bedrock, SageMaker, Amazon Q |
| IoT | `#7AA116` | IoT Core, IoT Greengrass |
| Migration & Modernization | `#01A88D` | DMS, DataSync, Migration Hub |
| Developer Tools | `#C925D1` | CodePipeline, CodeBuild, CodeDeploy |
| Customer Experience | `#E7157B` | Amazon Connect, Pinpoint, SES |
| Multicloud & Hybrid | `#ED7100` | Outposts, Local Zones, EKS Anywhere |

### Boundary Fill Colors (Reference-Architecture Style)
| Boundary | strokeColor | fillColor | Visual Effect |
|----------|-------------|-----------|---------------|
| AWS Cloud | `#232F3E` | `#F2F3F4` | Light warm gray |
| Region | `#00A4A6` | `#E6F6F7` | Light teal tint |
| Availability Zone | `#007FAA` | `#FFFFFF` | White with dashed border |
| VPC | `#8C4FFF` | `#F5F0FF` | Light purple tint |
| Public Subnet | `#248814` | `#E9F3E6` | Light green tint |
| Private Subnet | `#147EBA` | `#E6F0F7` | Light blue tint |
| AWS Account | `#CD2264` | `#FDF1F6` | Light pink tint |
| Security Group | `#DD344C` | `none` | Transparent (border only) |
| On-Premise / Corporate DC | `#5A6C86` | `#F2F3F4` | Light gray |

### Edge Color Coding
| Traffic Type | strokeColor | Style | Usage |
|-------------|-------------|-------|-------|
| General data flow | (default black) | Solid, `strokeWidth=2` | Primary data path |
| User/client traffic | `#2196F3` | Solid, `strokeWidth=2` | Requests from users |
| Management/admin traffic | `#FF9800` | Solid, `strokeWidth=2` | Control plane |
| Async/optional flow | (default black) | Dashed, `strokeWidth=2;dashed=1` | Event-driven, background |
| Error path | `#DD344C` | Dashed, `strokeWidth=2;dashed=1;strokeColor=#DD344C` | Error handling, DLQ |

## Typography

| Element | fontSize | fontStyle | fontColor |
|---------|----------|-----------|-----------|
| Diagram title | 16 | Bold (1) | `#232F3E` |
| Subtitle / metadata | 12 | Normal (0) | `#545B64` |
| Service labels | 12 | Normal (0) | `#232F3E` |
| Edge labels | 11 | Normal (0) | `#232F3E` (with `labelBackgroundColor=#F5F5F5`) |
| Group labels | 12 | Bold (1) | Category-specific (see boundary table) |
| Step annotation title | 13 | Bold (1) | `#232F3E` |
| Step annotation text | 12 | Normal (0) | `#232F3E` |

## Spacing Constants

| Element | Minimum | Recommended |
|---------|---------|-------------|
| Horizontal icon spacing | 220px | 250px |
| Vertical lane spacing | 250px | 280px |
| Auxiliary services gap (below main flow) | 280px | 320px |
| Icon size (main services) | 78x78px | 78x78px |
| Icon size (secondary services) | 65x65px | 65x65px |
| Canvas size | 2400x1400 | 2400x1400 |
| Viewport | dx=2800, dy=1600 | dx=2800, dy=1600 |

## Step Annotation Panel

Every diagram includes a numbered step annotation panel explaining the architecture flow.

### Placement
- **Right side** of the diagram (preferred when horizontal space allows)
- **Bottom** of the diagram (when the diagram is wide)

### Structure
1. **Title:** "Architecture Flow" (bold)
2. **Numbered steps:** ① ② ③ ④ ⑤ — each with a short description
3. **Background:** `fillColor=#F2F3F4;strokeColor=#E0E0E0;rounded=1;arcSize=5;`

### Matching Numbered Edges
Each numbered step in the panel corresponds to a numbered callout on the diagram edges:
- Edge labels: `value="①"` with `fontSize=14;fontStyle=1;labelBackgroundColor=#ffffff;`
- Step badges (optional): Small circles with `fillColor=#232F3E;fontColor=#FFFFFF;` near edge midpoints

## Do's and Don'ts

### Do
- Use official AWS service names ("Amazon EC2", not "EC2 server")
- Include numbered step annotations for every diagram
- Use boundary fills for visual depth (Reference-Architecture Style)
- Add a title block with date, version, and environment
- Use orthogonal edge routing with explicit exit/entry points
- Separate control plane from data plane
- Include a legend when using custom colors or line styles

### Don't
- Don't mix flow directions (left-to-right AND top-to-bottom) in the same diagram
- Don't use colored backgrounds on icon labels
- Don't create floating/unattached edges (always bind source and target)
- Don't guess stencil names — verify against reference files
- Don't use `strokeColor=#ffffff` on resource-level icons (use `strokeColor=none`)
- Don't use deprecated icon names (check reference files for removal notes)
- Don't overlap edges — rearrange components to minimize crossings
