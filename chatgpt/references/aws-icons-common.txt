# AWS Icons: General, Groups & Arrows

> Updated: 2026-05-28 — Aligned with AWS Architecture Icons (April 2026, Icon-package_04302026)

## General Resources (standalone shapes)
fillColor: `#232F3D` | strokeColor: `none`

| shape suffix | Display Name |
|-------------|-------------|
| `client` | Client / Browser |
| `traditional_server` | Traditional Server |
| `generic_firewall` | Firewall |
| `users` | Users |
| `user` | User |
| `mobile_client` | Mobile Client |
| `disk` | Disk |
| `document` | Document |
| `documents` | Documents |
| `email_2` | Email |
| `forums` | Forums |
| `gear` | Gear |
| `internet` | Internet |
| `internet_alt1` | Internet (alt) |
| `internet_alt2` | Internet Globe |
| `multimedia` | Multimedia |
| `office_building` | Office Building |
| `saml_token` | SAML Token |
| `sdk` | SDK |
| `servers` | Servers |
| `source_code` | Source Code |
| `tape` | Tape |
| `thumbs_up` | Thumbs Up |
| `thumbs_down` | Thumbs Down |

## Group Containers

### Reference-Architecture Style (recommended — matches AWS official diagrams)
Use with `shape=mxgraph.aws4.group;grIcon=mxgraph.aws4.<grIcon>;container=1;dropTarget=1;`

| grIcon | strokeColor | fillColor | fontColor | Display Name |
|--------|-------------|-----------|-----------|-------------|
| `group_aws_cloud_alt` | `#232F3E` | `#F2F3F4` | `#232F3E` | AWS Cloud |
| `group_aws_cloud` | `#232F3E` | `#F2F3F4` | `#232F3E` | AWS Cloud (alt) |
| `group_region` | `#00A4A6` | `#E6F6F7` | `#147EBA` | Region |
| `group_availability_zone` | `#007FAA` | `#FFFFFF` | `#007FAA` | Availability Zone |
| `group_security_group` | `#DD344C` | `none` | `#DD344C` | Security Group |
| `group_vpc` | `#8C4FFF` | `#F5F0FF` | `#8C4FFF` | VPC |
| `group_vpc2` | `#8C4FFF` | `#F5F0FF` | `#8C4FFF` | VPC (alt) |
| `group_private_subnet` | `#147EBA` | `#E6F0F7` | `#147EBA` | Private Subnet |
| `group_public_subnet` | `#248814` | `#E9F3E6` | `#248814` | Public Subnet |
| `group_account` | `#CD2264` | `#FDF1F6` | `#CD2264` | AWS Account |
| `group_corporate_data_center` | `#7D8998` | `#F2F3F4` | `#5A6C86` | Corporate DC |
| `group_on_premise` | `#5A6C86` | `#F2F3F4` | `#5A6C86` | On-Premise |
| `group_elastic_beanstalk` | `#D86613` | `none` | `#D86613` | Elastic Beanstalk |
| `group_ec2_instance_contents` | `#D86613` | `none` | `#D86613` | EC2 Instance |
| `group_spot_fleet` | `#D86613` | `none` | `#D86613` | Spot Fleet |
| `group_aws_step_functions_workflow` | `#CD2264` | `none` | `#CD2264` | Step Functions |
| `group_iot_greengrass` | `#7AA116` | `none` | `#3F8624` | IoT Greengrass |

### Minimal Style (legacy — transparent backgrounds)
Same as above but replace fillColor with `none` for all groups:
```
fillColor=none;
```

> **Choosing a style:** Use **Reference-Architecture Style** for presentation-quality diagrams (executive, documentation, AWS review). Use **Minimal Style** for quick technical sketches or when visual simplicity is preferred.

## Generic Groups (no grIcon)
```
fillColor=none;strokeColor=#5A6C86;dashed=1;verticalAlign=top;fontStyle=0;fontColor=#5A6C86;whiteSpace=wrap;html=1;
```

## Edge Styles
```
edgeStyle=orthogonalEdgeStyle;html=1;endArrow=block;elbow=vertical;startArrow=none;endFill=1;strokeColor=#545B64;rounded=0;
```

## Two Icon Patterns — CRITICAL RULE

### Pattern 1: Service-level (resourceIcon)
- Uses `shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.<name>`
- **MUST have `strokeColor=#ffffff`** — without it, the white glyph won't show
- Size: 78x78

### Pattern 2: Resource-level (standalone shape)
- Uses `shape=mxgraph.aws4.<name>` directly
- **MUST have `strokeColor=none`** — using #ffffff breaks these
- Size: 78x78 or 48x48

**Confusing these two patterns guarantees broken icons.**

## Step Annotation Panel

Every diagram should include a **numbered step annotation panel** to explain the architecture flow. Place this as a text block on the right side or bottom of the diagram.

### Step badge style (circled number on edge):
```
shape=ellipse;fillColor=#232F3E;fontColor=#FFFFFF;strokeColor=none;fontSize=12;fontStyle=1;aspect=fixed;
```
Size: 24x24, placed near the edge midpoint.

### Step description panel style:
```xml
<mxCell value="&lt;b&gt;Architecture Flow&lt;/b&gt;&lt;br&gt;① User request arrives via Route 53&lt;br&gt;② CloudFront serves cached content or forwards to origin&lt;br&gt;③ API Gateway authenticates and routes the request&lt;br&gt;④ Lambda processes business logic&lt;br&gt;⑤ DynamoDB stores/retrieves data" style="text;html=1;align=left;verticalAlign=top;whiteSpace=wrap;rounded=1;fillColor=#F2F3F4;strokeColor=#E0E0E0;fontSize=12;spacing=10;arcSize=5;" vertex="1" parent="1">
  <mxGeometry x="1800" y="100" width="350" height="200" as="geometry" />
</mxCell>
```

## PNG Export Background Fix
Place a light gray rectangle covering the entire diagram as background layer:
```
rounded=1;whiteSpace=wrap;fillColor=#F5F5F5;strokeColor=#E0E0E0;arcSize=2;
```
This prevents black background on areas outside groups when exporting to PNG.

## Title Block (Reference-Architecture Style)
```xml
<mxCell value="&lt;b style='font-size:16px'&gt;Diagram Title&lt;/b&gt;&lt;br&gt;&lt;span style='color:#545B64'&gt;Author | Date | Version | Environment&lt;/span&gt;" style="text;html=1;align=left;verticalAlign=top;whiteSpace=wrap;rounded=0;fontSize=14;spacing=10;" vertex="1" parent="1">
  <mxGeometry x="40" y="30" width="500" height="60" as="geometry" />
</mxCell>
```

## Base Template
```xml
<mxfile host="app.diagrams.net">
  <diagram id="diagram-1" name="Architecture">
    <mxGraphModel dx="2800" dy="1600" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="2400" pageHeight="1400" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```
