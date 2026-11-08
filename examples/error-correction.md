# Code rules — read before writing any C# code

**Read this file before you write a single line of C#. Do not start from memory of how C# examples usually look.**

For build verification, copy every fenced `csharp` block and compile it on its own, in a fresh project, with no
other block and no surrounding prose available to it. A block that would be fine pasted into an existing
project can still fail here. The rules below exist because each one has already broken a real build.

> **These rules tell you _how_ to write code, not _whether_ to include it.** They are a style guide, not a
> reason to answer in prose. See R0.

## The build contract

Your code is compiled with exactly these settings. Nothing else is configured for you.

| Setting | Value | What it means for you |
| --- | --- | --- |
| `TargetFramework` | `net10.0` | .NET 10 |
| `LangVersion` | `14.0` | C# 14 |
| `OutputType` | `Exe` | the block must be a runnable program, not a library |
| `ImplicitUsings` | `disable` | **no namespace is imported for you** |
| `Nullable` | `enable` | nullable reference types are on |
| `-warnaserror` | on | **every warning fails the build** |
| NuGet sources | nuget.org | only `Aspose.Words` is a direct package reference; its transitive dependencies restore normally |

The code is compiled, never executed. Correct compilation is required but does not make the example right.

## Pre-flight checklist

Before you emit a `csharp` block, confirm all eight:

- [ ] The question asked how to do something, and you are in fact giving a code example (R0).
- [ ] It has an entry point — top-level statements, or a `static void Main`.
- [ ] Every namespace it uses is imported by an explicit `using` at the top of **this** block.
- [ ] Every identifier it references is declared inside **this** block.
- [ ] No non-nullable field or property is left unassigned.
- [ ] Nothing is declared and then left unused.
- [ ] Top-level statements, if any, come before every `class` / `record` / `namespace`.
- [ ] It would compile if it were the only file in an empty project.

## Rules

### R0 — Still include the code

If the question asks how to perform a task, answer it with a working C# example. Do not drop to a
prose-only description to avoid the risk of a compiler error, and do not reduce an example to a
fragment, a single method signature or a bulleted list of type names for the same reason.

An answer with no code where code was asked for is a worse answer than one with a compiler error, and
it does not answer the task. The rules that follow exist to make your example compile — they
are never a reason to withhold one.

Prose alone is the right answer in one case only: when the question is genuinely conceptual — "what is
X", "what is the difference between X and Y", "what features are available" — and a code example would
not be the natural response. If you could reasonably open the answer with "here's how", include the
code.

WRONG shape of answer for *"How do I convert a document to an image?"*:

> Load the document as a `Document` and save it with `ImageSaveOptions`, choosing PNG or JPEG.
> See the conversion guide.

Correct, cited, and useless to someone who wanted the call. Give them the call:

```csharp
// RIGHT — the explanation plus a block that actually compiles
using Aspose.Words;
using Aspose.Words.Saving;

var doc = new Document("input.docx");
var options = new ImageSaveOptions(SaveFormat.Png) { Resolution = 300 };
doc.Save("output.png", options);
```

### R1 — Every block is a complete, runnable program

`OutputType` is `Exe`, so a block containing only type or method declarations cannot link.

*Prevents `CS5001` — "Program does not contain a static 'Main' method suitable for an entry point".*

```csharp
// WRONG — a library snippet; nothing runs it
public class ReportGenerator
{
    public static void Generate() { /* ... */ }
}
```

```csharp
// RIGHT — the helper is declared and then actually invoked
using Aspose.Words;
using Aspose.Words.Reporting;

ReportGenerator.Generate();          // top-level statement: this is the entry point

public class ReportGenerator
{
    public static void Generate()
    {
        var doc = new Document("Template.docx");
        new ReportingEngine().BuildReport(doc, new Sender(), "sender");
        doc.Save("Report.docx");
    }
}

public class Sender { }
```

### R2 — Declare every `using` explicitly

`ImplicitUsings` is disabled. `System` is **not** imported. `Console`, `DateTime`, `Environment`,
`Exception` and every exception type need `using System;`. File work needs `using System.IO;`.
Collections need `using System.Collections.Generic;`. LINQ needs `using System.Linq;`.

*Prevents `CS0103` and `CS0246` — "does not exist in the current context" / "could not be found".*

```csharp
// WRONG — Console and DateTime are in System, which was never imported
using Aspose.Words;

var doc = new Document("in.docx");
Console.WriteLine(DateTime.Now);
```

```csharp
// RIGHT
using System;
using Aspose.Words;

var doc = new Document("in.docx");
Console.WriteLine(DateTime.Now);
```

Aspose namespaces are separate from each other. `Document` is in `Aspose.Words`;
`ReportingEngine` is in `Aspose.Words.Reporting`; watermark option types are in `Aspose.Words`;
saving options live in `Aspose.Words.Saving`. Import each one you touch.

### R3 — Each block stands alone

Blocks do not share state. A variable declared in your first block does not exist in your second.
If you show two examples, each repeats its own `using` directives and its own setup.

*Prevents `CS0103` — "The name 'doc' does not exist in the current context".*

```csharp
// WRONG — `doc` and `response` came from an earlier block or from prose
doc.Range.Replace("a", "b");
Console.WriteLine(response.Text);
```

```csharp
// RIGHT — everything this block needs, it declares
using System;
using Aspose.Words;

var doc = new Document("in.docx");
doc.Range.Replace("a", "b");
doc.Save("out.docx");
```

### R4 — Initialize every non-nullable member

`Nullable` is enabled and warnings are errors, so an unassigned non-nullable property fails the build.
Give it an initializer, mark it `required`, or make it nullable.

*Prevents `CS8618` — "Non-nullable property must contain a non-null value when exiting constructor".*

```csharp
// WRONG
public class Sender
{
    public string Name { get; set; }
    public string Message { get; set; }
}
```

```csharp
// RIGHT — pick one of the two fixes, and keep the block runnable (R1)
using System;

var sender = new Sender { Message = "Hello" };
Console.WriteLine(sender.Name + sender.Message);

public class Sender
{
    public string Name { get; set; } = string.Empty;   // initializer
    public required string Message { get; set; }        // or required (C# 11+)
}
```

### R5 — Top-level statements come first

If a block uses top-level statements, they must precede every `class`, `record`, `struct` and
`namespace` declaration. Mixing the two in the other order is not legal C#.

*Prevents `CS8803` — "Top-level statements must precede namespace and type declarations".*

```csharp
// WRONG
public class Item { public int Id { get; set; } }

var item = new Item();          // too late — a type was declared above
```

```csharp
// RIGHT
var item = new Item();          // statements first

public class Item { public int Id { get; set; } }   // types after
```

If this feels awkward, use the alternative: wrap everything in `class Program { static void Main() { … } }`
and declare no top-level statements at all.

### R6 — Never leave anything unused

`-warnaserror` turns ordinary tidiness warnings into build failures. A local function, local variable or
private member you declare but never use will fail the build.

*Prevents `CS8321` — "The local function is declared but never used", and the unused-variable warnings.*

```csharp
// WRONG — declared, never called
void SplitByPage(Document doc) { /* ... */ }
```

```csharp
// RIGHT — declare it and call it
using Aspose.Words;

var doc = new Document("in.docx");
SplitByPage(doc);

void SplitByPage(Document document)
{
    document.Save("page.docx");
}
```

### R7 — Use only `Aspose.Words`

The verification project permits only `Aspose.Words` as a direct package reference. NuGet restore may download its transitive dependencies. Do not add another `PackageReference` to make an example pass. Do not reach for helper libraries, test frameworks or
JSON packages — use what is in `Aspose.Words` and the base class library.

*Prevents `NU1100` / `NU1101` restore failures.*

### R8 — Preserve every citation when you revise

When you are asked to repair or revise an answer, return the **complete** answer, and reproduce **every**
documentation URL the original contained. Before presenting a repair, compare its citations with the original and restore any missing documentation URLs. Add a new URL only if it came from
`words-net` evidence retrieved in this same session.

*Preserves the evidence accompanying the corrected answer.*

## Before you answer

First: if the question asked how to do something and your answer contains no `csharp` block, that is a
failed answer — add the example (R0).

Then re-read each `csharp` block once, as if it were the only file in an empty project:

1. Does it have an entry point?
2. Is every namespace it uses imported at the top of that same block?
3. Is every identifier it uses declared in that same block?
4. Is every non-nullable member assigned?
5. Is everything declared also used?
6. Do top-level statements precede all type declarations?

If any answer is no, fix the block before you send it. A compiler error is a failed answer even when the
Aspose.Words API usage is perfectly correct.
