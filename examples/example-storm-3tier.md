# Web Platform – Production Architecture

v1.0 | 2026-10-19 | Environment: Production | Region: eu-central-1 | Type: High-Level Overview

## Flow

1. Users call the platform over HTTPS/443.
2. Amazon CloudFront caches static content and forwards dynamic requests to the Application Load Balancer. AWS WAF (Web ACL on the distribution) filters requests at the edge.
3. The Application Load Balancer spreads requests across the Amazon ECS tasks on AWS Fargate in the private app subnets (HTTP/8080).
4. The ECS service reads and writes data in Amazon Aurora PostgreSQL (SQL/5432).
5. The tasks send logs and metrics to Amazon CloudWatch (async).

## Services

| Service | Purpose |
|---|---|
| Amazon CloudFront | CDN and TLS termination at the edge |
| AWS WAF | Web ACL against common web exploits |
| Application Load Balancer | Layer-7 load balancing into the VPC |
| Amazon ECS on AWS Fargate | Serverless containers, Auto Scaling 2–10 tasks |
| Amazon Aurora PostgreSQL | Relational database, db.r6g.large, Multi-AZ |
| Amazon CloudWatch | Logs, metrics and alarms |

## Design decisions

- Only the ALB is in the public subnets. Compute and data are in private subnets.
- Aurora Multi-AZ for high availability. AZ groups are omitted because this is a High-Level diagram.
- All services were checked as available in eu-central-1 with the AWS Knowledge MCP (`get_regional_availability`).
