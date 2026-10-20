# AWS Architecture Diagram Skill

This skill makes AWS architecture diagrams as native draw.io files (`.drawio`). The diagrams follow the Storm Reply diagram standard ([Confluence: How-to create an AWS Architecture Diagram](https://storm-ai.atlassian.net/wiki/spaces/StormAI/pages/136937485/How-to+create+an+AWS+Architecture+Diagram)).

This repository is a fork of [vidanov/aws-architecture-diagram-skill](https://github.com/vidanov/aws-architecture-diagram-skill) (MIT license).

![Example: Web Platform, Production architecture](examples/example-storm-3tier.drawio.png)

## What the skill does

- Uses the official AWS Architecture Icons from the draw.io library `mxgraph.aws4`.
- Uses only icon names that render correctly. For unknown icons, the skill gets the style from the draw.io MCP.
- Puts users on the left and data stores on the right. The flow goes from left to right.
- Adds a title block with title, version, date and environment.
- Adds numbered flow steps (①②③), a step panel and a legend.
- Uses a white background.
- Writes a companion `.md` file that explains the flow.
- Exports PNG, SVG or PDF with the draw.io Desktop CLI. The exported file contains the diagram XML, so you can edit it again in draw.io.

## Installation

### Claude Code (plugin)

Run these commands in Claude Code:

```bash
/plugin marketplace add StormAIDE/aws-architecture-diagram-skill
/plugin install aws-architecture-diagram@stormai-skills
```

To get a new release, run:

```bash
/plugin marketplace update stormai-skills
```

> **Note:** Did you install the skill manually before (`~/.claude/skills/aws-architecture-diagram`)? Then remove that copy with `rm -r ~/.claude/skills/aws-architecture-diagram`. If you keep it, two versions of the skill are active at the same time.

### MCP servers (recommended)

Add the two MCP servers once:

```bash
claude mcp add drawio -- npx -y @drawio/mcp
claude mcp add --transport http aws-knowledge https://knowledge-mcp.global.api.aws
```

| MCP server | The skill uses it to |
|---|---|
| draw.io MCP | find the correct icon style (`search_shapes`), show a preview (`open_drawio_xml`), change one page of a file (`get_page`, `set_page`) |
| AWS Knowledge MCP | get the official service names, find AWS reference architectures, check that each service is available in the region |

Without the MCP servers, the skill uses only the icon reference files in `references/`.

### Kiro CLI

```bash
mkdir -p ~/.kiro/skills/aws-architecture-diagram
cp kiro/SKILL.md ~/.kiro/skills/aws-architecture-diagram/SKILL.md
cp -r references ~/.kiro/skills/aws-architecture-diagram/references
```

For one project only, use `.kiro/skills/` in the project folder.

### Other AI assistants (ChatGPT, Claude Projects, internal agents)

1. Copy [`chatgpt/PROMPT.md`](chatgpt/PROMPT.md) into the system prompt or the custom instructions.
2. Upload the files from [`chatgpt/references/`](chatgpt/references/) to the knowledge base.
3. Ask for an AWS architecture diagram.

This version has no MCP workflow. Set the temperature to 0.3 to get stable XML.

## Usage

Write the diagram type, the services, the region and the environment in the prompt:

```
Create a High-Level AWS diagram for the customer portal: CloudFront → ALB → ECS Fargate → Aurora, eu-central-1, Production
```

If information is missing, the skill asks for it. Then the skill does these steps:

1. It checks the service names and the regional availability (AWS Knowledge MCP).
2. It gets the style of each icon (draw.io MCP).
3. It writes the `.drawio` file.
4. It shows a preview in draw.io.
5. It exports a PNG and checks the PNG for broken icons and crossing lines. Then it corrects the diagram.
6. It writes the companion `.md` file.

The skill knows these diagram types: High-Level Overview, Detailed Architecture, Network, Security, Data Flow, Disaster Recovery and Deployment.

After the skill finishes:

- Save the `.drawio` file in the project SharePoint or in the Git repository.
- For a new version, add a page to the same file. Do not make a new file.

## Repository content

| Path | Content |
|---|---|
| `claude/SKILL.md` | Skill for Claude Code (manual install) |
| `plugins/aws-architecture-diagram/` | Claude Code plugin (same skill, with references and templates) |
| `kiro/SKILL.md` | Skill for Kiro CLI |
| `chatgpt/` | Prompt and reference files for other AI assistants |
| `references/` | Verified icon names per AWS category, and the style guide |
| `templates/` | Start diagrams, for example serverless API, 3-tier web application, VPC networking |
| `examples/` | Example diagrams. `example-storm-3tier` follows the Storm Reply standard |
| `tests/validate_drawio.py` | Validator for `.drawio` files |

## Validation

Run the validator on a diagram:

```bash
python3 tests/validate_drawio.py path/to/diagram.drawio
```

The validator finds edges without a source or target, groups without `container=1`, a missing title block, a background that is not white, and deprecated icons. Without arguments, it checks all files in `tests/` and `templates/`.

## Changes

See [CHANGELOG.md](CHANGELOG.md).

## License

MIT. See [LICENSE](LICENSE).
