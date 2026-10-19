# Architecture Templates

Ready-to-use draw.io templates following AWS Reference Architecture best practices. Use these as starting points or reference for icon placement and styling.

## Available Templates

| Template | Pattern | Services Used |
|----------|---------|---------------|
| `serverless-rest-api.drawio` | Serverless API | CloudFront → API Gateway → Lambda → DynamoDB + S3 + Cognito |
| `event-driven-processing.drawio` | Event-Driven | EventBridge → SQS/SNS/Step Functions → Lambda → DynamoDB |
| `static-website.drawio` | Static Hosting | Route 53 → CloudFront → S3 + ACM + WAF |
| `three-tier-web-app.drawio` | 3-Tier Web | Route 53 → ALB → EC2 (Multi-AZ) → RDS (Primary/Standby) + VPC/Subnets |
| `vpc-networking.drawio` | VPC Network | Internet → IGW → NAT Gateways → EC2 in Private Subnets (Multi-AZ) |
| `data-mesh.drawio` | Data Mesh | DataZone → Lake Formation + Glue → S3 → Athena/Redshift/SageMaker (Multi-Account) |
| `hybrid-networking.drawio` | Hybrid Network | Direct Connect + VPN → Transit Gateway → Prod/Dev/Shared VPCs |

## How to Use

1. Copy a template as starting point
2. Modify services, labels, and connections
3. Add/remove lanes as needed

## Style Conventions in Templates (v2.0)

- **Reference-Architecture Style**: Colored boundary fills (light teal Region, light purple VPC, light green/blue subnets)
- **Step annotation panel**: Every template includes a numbered flow explanation box
- **Numbered edges**: ①②③… labels on edges matching the step panel
- **Title block**: Name, date, version in top-left corner
- Background: `#F5F5F5` rectangle (prevents black on PNG export)
- Left-to-right flow with 78x78 service icons
- All groups use `container=1;dropTarget=1` with proper parent nesting
