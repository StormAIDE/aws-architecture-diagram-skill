# Changelog

## [2.0.0] - 2026-05-28

### Added
- **Reference-Architecture Style**: Configurable boundary fill colors matching AWS official diagrams (light teal for Region, light purple for VPC, light green/blue for subnets)
- **Step annotation panel**: Required on every diagram — numbered flow explanation box (①②③…)
- **Style guide**: New `references/style-guide.md` with complete visual design system (color palette, typography, spacing, do's/don'ts)
- **New icon categories**: Customer Experience (Connect, Pinpoint, SES) and Multicloud & Hybrid (Outposts, Local Zones, EKS Anywhere)
- **New icons**: Amazon Q Business/Developer, Bedrock Agent/Knowledge Base, SageMaker, DataZone
- **New templates**: `data-mesh.drawio` (multi-account DataZone pattern), `hybrid-networking.drawio` (Transit Gateway hub-and-spoke)
- **Validation checks**: Step annotation presence (Issue #4), deprecated icon warnings (Issue #5), boundary fillColor validation (Issue #6)
- Identical updates applied to all 3 platforms (Claude, Kiro, ChatGPT)

### Changed
- All 5 existing templates updated with: boundary fillColors, title blocks, step annotation panels, numbered edges
- Group boundaries table now includes fillColor column for Reference-Architecture Style
- Validation script now auto-scans `templates/` directory
- Updated all icon reference files with April 2026 icon package changes

### Deprecated
- Icons removed from April 2026 package: `quicksight`, `eks_cloud`, `iot_analytics`, `quantum_ledger_database`, `alexa_for_business`, `elastic_transcoder`, `private_5g`, `app_stream`
- `app_runner` and `audit_manager` marked as maintenance mode

## [1.1.0] - 2026-05-22

### Added
- Audience mode (technical vs non-technical label adjustment)
- Numbered flow edges (① ② ③) for presentation diagrams
- Companion markdown guide generation
- Post-generation validation checklist
- IoT, Migration, Developer Tools icon categories
- CONTRIBUTING.md
- GitHub Actions validation workflow
- Claude Code plugin marketplace structure (one-line install)
- 5 reference architecture templates
- Multi-page diagram support
- Legend/title block standard

### Fixed
- Documented two-pattern rule (service-level vs resource-level strokeColor)
- Added PNG export background fix (#F5F5F5 rectangle)

## [1.0.0] - 2026-05-22

### Added
- Initial release
- 8 category reference files with 270+ verified icons
- Kiro CLI and Claude Code support
- Left-to-right layout rules
- Verified icon catalog extracted from Sidebar-AWS4.js
- Broken icons documentation
