# C# build rules

**Before writing any C#, read `examples/error-correction.md` in this workspace and follow its rules
R0–R8.** That file has the worked wrong/right example for each rule. The mandatory parts are repeated
here so they apply even if you do not open it.

**These rules tell you _how_ to write code, not _whether_ to include it.** If a question asks how to
perform a task, answer it with a working example. Never fall back to a prose-only answer, a fragment or
a list of type names in order to avoid the risk of a compiler error — an answer with no code where code
was asked for does not answer the task. Prose alone is right only for genuinely conceptual
questions ("what is X", "what is the difference between X and Y"), where an example would not be the
natural response.

For build verification, copy every fenced `csharp` block and compile it **on its own**, as a standalone
console project. Nothing carries over from another block or from your prose.

| Setting | Value |
| --- | --- |
| `TargetFramework` | `net10.0` |
| `LangVersion` | `14.0` (C# 14) |
| `OutputType` | `Exe` |
| `ImplicitUsings` | `disable` |
| `Nullable` | `enable` |
| Warnings | treated as errors |
| NuGet sources | nuget.org for restore; only `Aspose.Words` is a direct package reference |

Every block must therefore:

- **R0** — exist. A "how do I…" question is answered with a compiling example, not a description of
  which types to use. Omitting code to stay safe is a failed answer, not a cautious one.
- **R1** — be a complete, runnable program: top-level statements or a `static void Main`. A block of
  type or method declarations alone does not link.
- **R2** — declare every `using` it needs. `System` is **not** imported for you: `Console`, `DateTime`,
  `Environment` and every exception type require `using System;`.
- **R3** — stand alone: declare every identifier it references, and repeat its own `using` directives
  and setup even when an earlier block already showed them.
- **R4** — assign every non-nullable field and property, with an initializer, `required`, or a
  constructor; otherwise make it nullable.
- **R5** — place any top-level statements before all `class`, `record`, `struct` and `namespace`
  declarations.
- **R6** — leave nothing declared but unused; an uncalled local function fails the build.
- **R7** — reference no NuGet package other than `Aspose.Words`.
- **R8** — when revising an answer, return it complete and reproduce **every** documentation URL the
  original cited. Preserve the original documentation URLs when repairing code; compare them before presenting the revision. Add a URL only from `words-net` evidence retrieved in this session.

Check once more before answering: does a "how do I" question have a code example at all, and does each
block have an entry point, every `using`, every identifier, every non-nullable member assigned, nothing
unused, and statements before types? A compiler error is a failed answer even when the Aspose.Words API
usage is correct — and so is no code at all.
