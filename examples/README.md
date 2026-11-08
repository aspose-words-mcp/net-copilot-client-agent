# C# build verification

This project compiles examples against **.NET 10 (`net10.0`), C# 14, and Aspose.Words for .NET 26.10.0**. Nullable analysis and warnings-as-errors are enabled; implicit usings are disabled. The SDK selector accepts installed stable .NET 10 feature bands.

Install the .NET 10 SDK separately. From the repository root:

```sh
cd examples
dotnet restore BuildVerification.csproj --configfile NuGet.Config
dotnet build BuildVerification.csproj --no-restore --nologo --verbosity minimal -warnaserror
```

Restore uses nuget.org and may download packages. If your environment restricts package sources, configure an approved mirror or populate the NuGet cache. The exact Aspose.Words version is pinned; only that package is directly referenced.

The checked-in `Program.cs` is a DOCX-to-PDF compilation fixture. Building it does not read `input.docx` or create `output.pdf`; executing it would. The agent must not execute generated programs unless the user separately requests it.

## Copilot workflow

The custom agent and shared workspace guidance explicitly reference [C# rules](csharp-build-rules.instructions.md) and [error-correction examples](error-correction.md). These files are outside `.github/instructions/`, so they are loaded by explicit reads, not automatic directory discovery.

For each answer, Copilot creates a new `examples/.scratch/<unique-request>/block-N/` directory. It copies `BuildVerification.csproj` and `NuGet.Config` there and writes each complete C# block as that directory's `Program.cs`. The SDK selector in `examples/global.json` applies when commands run from those directories. Each block is restored and built independently using the commands above.

The agent may make at most two compiler-driven repairs per block after the initial attempt. It must build the exact final code shown in the answer, retain citations, and state the result. Missing SDK, restore failures, denied tool access, and timeouts are reported as unavailable verification rather than successful builds. Compilation does not check runtime behavior or document output.

Each request uses a fresh scratch directory; existing user files and the checked-in fixture are not overwritten. Scratch files and build outputs are ignored by Git. File edits and commands remain subject to normal client permissions. This is an agent workflow, not an automatic CI gate or a guarantee that every response follows the instructions.

## Rule provenance

Adapted from the existing benchmark C# rules. Paths and package-restore behavior are adjusted for this interactive client; citation preservation is an agent instruction rather than an automated rejection gate.
