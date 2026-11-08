# Client setup

## Prerequisites

- VS Code with GitHub Copilot Chat access.
- A deployed Aspose.Words for .NET MCP server exposing an HTTP MCP endpoint.
- Network access to that endpoint and any credentials required by your deployment.

To execute generated C# examples, separately install the .NET SDK and the Aspose.Words package required by your application. Follow Aspose.Words licensing requirements for your usage. Neither is needed just to open the client configuration.

## Connect the server

Open `net-copilot-client-agent.code-workspace`. The server is named `words-net`; the custom agent's tool configuration refers to that name, so keep it consistent.

Replace `https://YOUR_MCP_HOST/YOUR_MCP_ENDPOINT` in `.vscode/mcp.json` with your full endpoint URL. Use the actual URL reported by your deployment; a repository URL or server homepage is not an MCP endpoint. No private address is bundled here.

Start the server connection through **MCP: List Servers**. Review VS Code's trust and tool-access prompts, then open a new chat with **Aspose.Words for .NET MCP** selected.

## Authentication

See the [server setup guide](https://github.com/aspose-words-mcp/net-server/blob/main/docs/setup.md) for deployment and authentication configuration.

Follow your server's authentication instructions. Configure authentication through VS Code's **MCP Servers → Add Server** flow for your selected session environment, or use the server's documented credential mechanism. Keep actual credentials out of committed files.

The supplied `.vscode/mcp.json` uses VS Code's `servers` format. Portable Copilot configurations use `mcpServers` instead. VS Code input variables are not supported in portable configurations, and servers requiring interactive inputs are not forwarded to Copilot sessions; the supplied endpoint is therefore an editable literal placeholder. See the [configuration guidance](https://code.visualstudio.com/docs/agent-customization/mcp-servers).

## Verify the connection

Ask a simple question such as “How do I convert DOCX to PDF?” Inspect the chat's tool activity for `words-net` requests and documentation citations in the answer. A connected MCP server and a discovered custom agent are separate checks.

## Agent missing from the picker

1. Open the repository root or the supplied workspace file in the same VS Code window as the chat.
2. Confirm `.github/agents/aspose-words-mcp.agent.md` exists and has `user-invocable: true`.
3. Open **Configure Custom Agent…** and check the workspace agent list.
4. Run **Developer: Reload Window** and start a new chat. This refreshes discovery and resolved a stale discovery state during client setup.
5. If it remains missing, inspect **Developer: Open Agent Debug Panel** for discovery diagnostics.

## Server or tool errors

Check the endpoint, authentication, network access, and server logs. Use the server repository's deployment guide once its public link is available. An unavailable tool or failed symbol lookup does not establish that an Aspose.Words feature is unsupported.

## Large responses

The agent can use read-only file and terminal tools to inspect saved MCP responses in small chunks. Normal VS Code permissions apply. If access is declined or unavailable, the agent should request narrower evidence and explain any unresolved gap.

## References

- [VS Code MCP configuration](https://code.visualstudio.com/docs/copilot/customization/mcp-servers)
- [VS Code custom agents](https://code.visualstudio.com/docs/agent-customization/custom-agents)

## C# compilation checks

For generated C# examples, install the .NET 10 SDK and follow [build verification](../examples/README.md). The custom agent can edit isolated scratch projects and run NuGet restore and compilation; these permissions extend its read-only MCP-response inspection workflow. Generated programs are not executed by default.
