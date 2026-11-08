# Aspose.Words workspace guidance

Apply these rules to Aspose.Words for .NET tasks:

- Prefer the configured `words-net` MCP server for documentation and API evidence. The **Aspose.Words for .NET MCP** custom agent adds an MCP-only retrieval workflow in `.github/agents/aspose-words-mcp.agent.md`.
- Base API and capability claims on inspected evidence. Verify relevant types, members, overloads, and options before using them. A failed lookup does not prove a capability is absent; describe unresolved support as **not verified**.
- If a tool saves an oversized response to a file, read the relevant documentation in bounded chunks before answering; metadata and previews are not evidence. Follow the custom agent’s chunk-reading procedure when using that agent. If the file is inaccessible, request narrower results and report any remaining evidence gap.
- When C# code is requested, include the required packages, namespaces, inputs, and outputs. Use syntax appropriate to the user's target SDK and language version. Clearly identify incomplete snippets and placeholders.
- Never claim code compiled, ran, or produced a valid document unless actually tested; state what was tested when relevant.
- Cite exact documentation URLs returned by tools. Do not construct or repair URLs, or claim HTTP verification without a check.
- Answer directly with the simplest verified solution, concise citations, and relevant limitations. State evidence gaps or conflicts clearly.

- Before generating C# examples, read `examples/csharp-build-rules.instructions.md` and `examples/error-correction.md`. Follow the isolated build workflow in `examples/README.md` and the custom agent. Verify each final block against the pinned configuration when tools are available; report unavailable or failed checks honestly.
