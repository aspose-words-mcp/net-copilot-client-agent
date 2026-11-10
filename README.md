# Aspose.Words for .NET — GitHub Copilot Client Agent

Use GitHub Copilot Chat to explore Aspose.Words for .NET with answers and C# examples grounded in your deployed MCP server's documentation and API tools.

This repository provides the **Aspose.Words for .NET MCP** custom agent and VS Code client configuration. Deploy the MCP server separately, then connect this client to its HTTP endpoint.

[Browse 99 example answers](showcase/runs/published-01/showcase.md) · [Run metrics](showcase/runs/published-01/metrics.md) · [Setup and troubleshooting](docs/setup.md)

## Project family

These repositories work together to provide documentation-backed MCP services and a GitHub Copilot client for Aspose.Words for .NET. The shared engine is maintained under **aspose-core-mcp**; the Words/.NET components are maintained under **aspose-words-mcp**.

| Repository | Responsibility |
| --- | --- |
| [context-engine](https://github.com/aspose-core-mcp/context-engine) | Shared documentation ingestion, indexing, retrieval, and MCP infrastructure |
| [net-plugin](https://github.com/aspose-words-mcp/net-plugin) | Aspose.Words for .NET documentation/API extraction and retrieval configuration |
| [net-server](https://github.com/aspose-words-mcp/net-server) | Deployment helpers that combine pinned engine and plugin versions |
| [net-client-copilot-agent](https://github.com/aspose-words-mcp/net-client-copilot-agent) **(this repository)** | GitHub Copilot agent, C# compilation checks, and example-answer showcase |

## Quick start

1. Install and deploy the MCP server using its repository instructions (link above). Obtain its full HTTP MCP endpoint URL and any authentication requirements.
2. Install VS Code with GitHub Copilot Chat access, and open `net-client-copilot-agent.code-workspace` from this repository.
3. Replace `https://YOUR_MCP_HOST/YOUR_MCP_ENDPOINT` in `.vscode/mcp.json` with the full HTTP endpoint URL supplied by your deployment. Run **MCP: List Servers**, select **words-net**, and start it.
4. If your server requires authentication, complete the configuration described in [setup](docs/setup.md#authentication) before connecting.
5. Start a new Copilot chat and choose **Aspose.Words for .NET MCP** from the agent picker.
6. Ask, for example: **How to convert DOC/DOCX to PDF using Aspose.Words for .NET?**

The agent queries the server for evidence, checks relevant APIs, and cites documentation returned by the tools. It can read saved tool responses in bounded chunks when a response is too large to display directly.

## What is included

- `.github/agents/aspose-words-mcp.agent.md`: custom agent scope, retrieval, and response-reading workflow.
- `.github/copilot-instructions.md`: shared evidence and answer guidance.
- `examples/`: pinned compilation project, build rules, and error-correction examples.
- `.vscode/mcp.json`: HTTP connection configuration with an endpoint placeholder.
- `showcase/runs/published-01/`: published questions and answers with their run metrics.
- `showcase/`: question runner with optional compilation/repair and concise showcase and metrics reports. See [generation instructions](showcase/README.md).

## Showcase

[Explore the showcase](showcase/runs/published-01/showcase.md) for document conversion, reporting, editing, and other Aspose.Words tasks. Initial generations use fresh sessions. Each entry identifies the generation model and whether a repair was used. See the [run metrics](showcase/runs/published-01/metrics.md) for compilation outcomes, model usage, repairs, and timing.

## Contributing

Include your VS Code version, selected model, and a minimal prompt when reporting a client issue. Remove credentials and private endpoint details from logs. Report server deployment or tool issues in the MCP server repository once its public link is available.

## Compile generated examples

Install the .NET 10 SDK to enable Copilot compilation checks. The custom agent reads the rules under `examples/`, writes each C# block into a separate scratch project, and runs restore/build against Aspose.Words 26.10.0. It can attempt two repairs after an initial compiler failure and reports the actual result. Allow the required edit/terminal permissions when prompted. See [build verification](examples/README.md) for manual commands and requirements.

## License

[MIT](LICENSE), copyright (c) 2001–2026 Aspose Pty Ltd.
