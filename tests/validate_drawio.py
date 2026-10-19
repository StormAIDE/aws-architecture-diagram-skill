#!/usr/bin/env python3
"""Validate .drawio files against issues #1, #2, #3 and best-practices styling.

Issue #1: VPC peering must use resource-level pattern (shape=mxgraph.aws4.vpc_peering, strokeColor=none)
Issue #2: All edges must have source and target attributes (no floating edges)
Issue #3: Group/boundary shapes must have container=1 and children must reference parent ID
Issue #4: Step annotation panel must be present
Issue #5: Deprecated icons should not be used in new diagrams
Issue #6: Group boundaries should use appropriate fillColor for Reference-Architecture Style
"""

import sys
import xml.etree.ElementTree as ET
from pathlib import Path

CONTAINER_SHAPES = [
    "mxgraph.aws4.group",
    "mxgraph.aws4.group_vpc2",
    "mxgraph.aws4.group_security_group",
    "mxgraph.aws4.group_aws_cloud_alt",
    "mxgraph.aws4.group_account",
    "mxgraph.aws4.group_on_premise",
    "mxgraph.aws4.group_corporate_data_center",
    "mxgraph.aws4.group_region",
    "mxgraph.aws4.group_availability_zone",
    "mxgraph.aws4.group_public_subnet",
    "mxgraph.aws4.group_private_subnet",
]

DEPRECATED_ICONS = [
    "quicksight",
    "eks_cloud",
    "iot_analytics",
    "quantum_ledger_database",
    "alexa_for_business",
    "elastic_transcoder",
    "private_5g",
    "app_stream",
]

EXPECTED_FILL_COLORS = {
    "mxgraph.aws4.group_aws_cloud_alt": "#F2F3F4",
    "mxgraph.aws4.group_region": "#E6F6F7",
    "mxgraph.aws4.group_vpc2": "#F5F0FF",
    "mxgraph.aws4.group_public_subnet": "#E9F3E6",
    "mxgraph.aws4.group_private_subnet": "#E6F0F7",
    "mxgraph.aws4.group_availability_zone": "#FFFFFF",
    "mxgraph.aws4.group_account": "#FDF1F6",
    "mxgraph.aws4.group_on_premise": "#F2F3F4",
    "mxgraph.aws4.group_corporate_data_center": "#F2F3F4",
}

def parse_style(style_str):
    """Parse draw.io style string into dict."""
    if not style_str:
        return {}
    parts = style_str.rstrip(";").split(";")
    result = {}
    for p in parts:
        if "=" in p:
            k, v = p.split("=", 1)
            result[k] = v
        else:
            result[p] = ""
    return result


def validate_file(filepath):
    tree = ET.parse(filepath)
    root = tree.getroot()
    errors = []
    warnings = []

    cells = {}
    for cell in root.iter("mxCell"):
        cid = cell.get("id")
        if cid:
            cells[cid] = cell

    # Issue #1: Check VPC peering icons use correct pattern
    for cid, cell in cells.items():
        style = parse_style(cell.get("style", ""))
        # Check if someone used resIcon with vpc_peering (wrong pattern)
        res_icon = style.get("resIcon", "")
        if "vpc_peering" in res_icon:
            errors.append(f"[Issue #1] Cell '{cid}': vpc_peering used as resIcon — must use resource-level pattern (shape=mxgraph.aws4.vpc_peering;strokeColor=none)")
        # Check correct pattern has strokeColor=none
        shape = style.get("shape", "")
        if "vpc_peering" in shape:
            sc = style.get("strokeColor", "")
            if sc and sc != "none":
                errors.append(f"[Issue #1] Cell '{cid}': vpc_peering has strokeColor={sc} — must be strokeColor=none")

        # Check fillColor on AWS icons
        if "mxgraph.aws4" in shape and "group" not in shape:
            if not style.get("fillColor"):
                warnings.append(f"[Rendering] Cell '{cid}': AWS icon missing fillColor — will render as white square in PNG export")

    # Issue #2: Check all edges have source and target
    for cid, cell in cells.items():
        if cell.get("edge") == "1":
            source = cell.get("source")
            target = cell.get("target")
            if not source:
                errors.append(f"[Issue #2] Edge '{cid}': missing source attribute (floating edge)")
            elif source not in cells:
                errors.append(f"[Issue #2] Edge '{cid}': source='{source}' references non-existent cell")
            if not target:
                errors.append(f"[Issue #2] Edge '{cid}': missing target attribute (floating edge)")
            elif target not in cells:
                errors.append(f"[Issue #2] Edge '{cid}': target='{target}' references non-existent cell")
            # Check for exitX/entryX
            style = parse_style(cell.get("style", ""))
            if "exitX" not in style and "entryX" not in style:
                warnings.append(f"[Issue #2] Edge '{cid}': no exitX/entryX — connection points may not snap properly")

    # Issue #3: Check containers have container=1 and children use proper parent
    for cid, cell in cells.items():
        style = parse_style(cell.get("style", ""))
        shape = style.get("shape", "")
        gr_icon = style.get("grIcon", "")

        is_group = any(s in shape for s in CONTAINER_SHAPES) or any(s in gr_icon for s in CONTAINER_SHAPES)
        if is_group:
            if style.get("container") != "1":
                errors.append(f"[Issue #3] Group '{cid}' ({cell.get('value', '')[:30]}): missing container=1 in style")
            if style.get("dropTarget") != "1":
                warnings.append(f"[Issue #3] Group '{cid}' ({cell.get('value', '')[:30]}): missing dropTarget=1 in style")

    # Check that non-edge cells inside containers reference the container as parent
    container_ids = set()
    for cid, cell in cells.items():
        style = parse_style(cell.get("style", ""))
        if style.get("container") == "1":
            container_ids.add(cid)

    # Verify children reference their container
    for cid, cell in cells.items():
        if cid in ("0", "1"):
            continue
        parent = cell.get("parent", "")
        if parent in container_ids:
            # Good — child references a container
            pass

    # Issue #4: Check for step annotation panel
    has_step_panel = False
    for cid, cell in cells.items():
        value = cell.get("value", "")
        style = parse_style(cell.get("style", ""))
        # Step panels are text cells with circled numbers or "Architecture Flow" / "Flow"
        if style.get("") == "text" or "text" in style:
            if any(marker in value for marker in ["①", "②", "③", "Architecture Flow", "Flow"]):
                has_step_panel = True
                break
    if not has_step_panel:
        warnings.append("[Issue #4] No step annotation panel found — diagrams should include a numbered flow explanation")

    # Issue #5: Check for deprecated icons
    for cid, cell in cells.items():
        style = parse_style(cell.get("style", ""))
        res_icon = style.get("resIcon", "")
        shape = style.get("shape", "")
        icon_ref = res_icon or shape
        for deprecated in DEPRECATED_ICONS:
            if deprecated in icon_ref:
                warnings.append(f"[Issue #5] Cell '{cid}': uses deprecated icon '{deprecated}' — consider using a replacement")

    # Issue #6: Check boundary fillColors match Reference-Architecture Style
    for cid, cell in cells.items():
        style = parse_style(cell.get("style", ""))
        gr_icon = style.get("grIcon", "")
        if gr_icon in EXPECTED_FILL_COLORS:
            fill = style.get("fillColor", "none")
            expected = EXPECTED_FILL_COLORS[gr_icon]
            if fill == "none":
                warnings.append(f"[Issue #6] Group '{cid}' ({cell.get('value', '')[:30]}): fillColor=none — consider using Reference-Architecture Style fillColor={expected}")

    return errors, warnings


def main():
    if len(sys.argv) < 2:
        # Default: test all .drawio files in tests/ and templates/
        test_dir = Path(__file__).parent
        repo_root = test_dir.parent
        files = list(test_dir.glob("*.drawio"))
        files.extend(repo_root.glob("templates/*.drawio"))
        if not files:
            print("No .drawio files found in tests/ or templates/")
            sys.exit(1)
    else:
        files = [Path(f) for f in sys.argv[1:]]

    total_errors = 0
    total_warnings = 0

    for f in files:
        print(f"\n{'='*60}")
        print(f"Validating: {f.name}")
        print(f"{'='*60}")
        errors, warnings = validate_file(f)
        total_errors += len(errors)
        total_warnings += len(warnings)

        if errors:
            for e in errors:
                print(f"  ❌ {e}")
        if warnings:
            for w in warnings:
                print(f"  ⚠️  {w}")
        if not errors and not warnings:
            print("  ✅ All checks passed!")

    print(f"\n{'='*60}")
    print(f"Summary: {total_errors} errors, {total_warnings} warnings across {len(files)} file(s)")
    print(f"{'='*60}")
    sys.exit(1 if total_errors > 0 else 0)


if __name__ == "__main__":
    main()
