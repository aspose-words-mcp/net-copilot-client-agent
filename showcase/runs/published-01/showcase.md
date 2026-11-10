# Aspose.Words for .NET — Copilot Showcase

99 questions and answers generated with GitHub Copilot CLI and the Aspose.Words for .NET MCP server, using `csharp-build-rules.instructions.md` and `error-correction.md`. C# examples were checked for compilation using Aspose.Words for .NET 26.10.0 with target framework net10.0; see [metrics](metrics.md) for outcomes. Initial generations use fresh sessions.

[Client setup](../../../README.md#quick-start)

## Questions

### Word to PDF

- [How to convert DOC/DOCX to PDF?](#word-to-pdf-01)
- [How to convert a document to PDF?](#word-to-pdf-02)
- [How to convert DOC/DOCX to PDF in C#?](#word-to-pdf-03)
- [How do I convert a DOC/DOCX document to PDF in C#?](#word-to-pdf-04)

### Word to HTML

- [How to convert DOC/DOCX to HTML?](#word-to-html-01)
- [How to convert a document to HTML?](#word-to-html-02)
- [How to convert DOC/DOCX to HTML in C#?](#word-to-html-03)
- [How do I convert a DOC/DOCX document to HTML in C#?](#word-to-html-04)

### Word to Excel

- [How to convert DOC/DOCX to Excel?](#word-to-excel-01)
- [How to convert a Word document to Excel?](#word-to-excel-02)
- [How to convert DOC/DOCX to XLSX in C#?](#word-to-excel-03)
- [How do I convert a DOC/DOCX document to Excel in C#?](#word-to-excel-04)
- [How to convert Word to XLSX in C#?](#word-to-excel-05)
- [Can Aspose.Words convert DOCX to Excel?](#word-to-excel-06)

### Word to Markdown

- [How to convert DOC/DOCX to Markdown?](#word-to-markdown-01)
- [How to convert a Word document to Markdown?](#word-to-markdown-02)
- [How to convert DOC/DOCX to Markdown in C#?](#word-to-markdown-03)
- [How do I convert a DOC/DOCX document to Markdown in C#?](#word-to-markdown-04)
- [How to save a Word document as a Markdown file?](#word-to-markdown-05)
- [Can Aspose.Words convert DOCX to Markdown?](#word-to-markdown-06)

### Word to Image

- [How to convert DOC/DOCX to an image?](#word-to-image-01)
- [How to convert a Word document to an image?](#word-to-image-02)
- [How to convert DOC/DOCX to PNG in C#?](#word-to-image-03)
- [How do I convert a DOC/DOCX document to an image in C#?](#word-to-image-04)
- [How to save a Word document as an image?](#word-to-image-05)
- [Can Aspose.Words convert DOCX to JPG or PNG?](#word-to-image-06)

### PDF to Other Formats

- [How to convert PDF to other document formats?](#pdf-to-other-01)
- [How to convert PDF to DOCX in C#?](#pdf-to-other-02)
- [How to convert a PDF document to Word in C#?](#pdf-to-other-03)
- [How do I convert PDF to DOC or DOCX using Aspose.Words?](#pdf-to-other-04)
- [How to convert PDF to HTML or an image in C#?](#pdf-to-other-05)
- [Can Aspose.Words convert PDF to other formats?](#pdf-to-other-06)
- [How to load a PDF document with PdfLoadOptions?](#pdf-to-other-07)

### LINQ Reporting

- [What is the LINQ Reporting Engine in Aspose.Words?](#linq-reporting-01)
- [How to generate reports using the LINQ Reporting Engine in C#?](#linq-reporting-02)
- [How to create a Word document from a LINQ Reporting template and data source using Aspose.Words ReportingEngine in C#?](#linq-reporting-03)
- [How to populate a LINQ Reporting template with data using Aspose.Words ReportingEngine.BuildReport in C#?](#linq-reporting-04)
- [How to use LINQ expressions in a Word document template?](#linq-reporting-05)
- [How to use loops and conditions in LINQ Reporting Engine templates?](#linq-reporting-06)
- [How to generate reports from JSON or XML data in C#?](#linq-reporting-07)
- [What is the difference between LINQ Reporting Engine and Mail Merge?](#linq-reporting-08)

### Mail Merge

- [What is Mail Merge in Aspose.Words?](#mail-merge-01)
- [How to perform mail merge in C#?](#mail-merge-02)
- [How to populate a Word template with data using Mail Merge?](#mail-merge-03)
- [How to generate personalized documents from a template?](#mail-merge-04)
- [How to perform mail merge with a data source in C#?](#mail-merge-05)
- [How to use mail merge fields in a Word document?](#mail-merge-06)
- [How to execute mail merge with regions in Aspose.Words?](#mail-merge-07)
- [What is the difference between Mail Merge and LINQ Reporting Engine?](#mail-merge-08)

### Compare Documents

- [How to compare two Word documents in C#?](#compare-01)
- [How to find differences between DOCX documents using Aspose.Words?](#compare-02)
- [How to compare two documents and identify changes?](#compare-03)
- [How to generate a document that shows differences between two versions?](#compare-04)
- [How to compare Word documents programmatically?](#compare-05)
- [Can Aspose.Words compare documents and mark revisions?](#compare-06)
- [How to compare documents while ignoring formatting changes?](#compare-07)

### Split Documents

- [How to split a Word document into multiple documents in C#?](#split-01)
- [How to split a DOCX file by pages using Aspose.Words?](#split-02)
- [How to extract each page of a Word document into a separate file?](#split-03)
- [How to split a Word document by sections?](#split-04)
- [How to split a document by headings or other structural elements?](#split-05)
- [How to save each page of a Word document separately?](#split-06)
- [How to use DocumentSplitCriteria in Aspose.Words?](#split-07)

### Merge Documents

- [How to merge multiple Word documents into one document in C#?](#merge-01)
- [How to combine DOCX files using Aspose.Words?](#merge-02)
- [How to append one Word document to another?](#merge-03)
- [How to insert the contents of one document into another?](#merge-04)
- [How to merge Word documents while preserving formatting?](#merge-05)
- [What is the difference between InsertDocument and AppendDocument?](#merge-06)
- [How to combine several Word documents into a single DOCX file?](#merge-07)

### Find and Replace

- [How to find and replace text in a Word document using C#?](#find-replace-01)
- [How to replace a string in a DOCX file with Aspose.Words?](#find-replace-02)
- [How to replace all occurrences of a word in a document?](#find-replace-03)
- [How to find and replace text using regular expressions?](#find-replace-04)
- [How to perform a case-insensitive text replacement in Word documents?](#find-replace-05)
- [How to replace text while preserving document formatting?](#find-replace-06)
- [How to use FindReplaceOptions in Aspose.Words?](#find-replace-07)

### Digital Signatures

- [How to digitally sign a Word document in C#?](#digital-signatures-01)
- [How to add a digital signature to a DOCX file using Aspose.Words?](#digital-signatures-02)
- [How to verify digital signatures in a Word document?](#digital-signatures-03)
- [How to check whether a Word document is digitally signed?](#digital-signatures-04)
- [How to sign a document with a PFX certificate?](#digital-signatures-05)
- [How to remove digital signatures from a Word document?](#digital-signatures-06)
- [How to use DigitalSignatureUtil in Aspose.Words?](#digital-signatures-07)

### Watermarks

- [How to add a watermark to a Word document in C#?](#watermark-01)
- [How to insert a text watermark into a DOCX file?](#watermark-02)
- [How to add an image watermark to a Word document?](#watermark-03)
- [How to remove a watermark from a Word document using Aspose.Words?](#watermark-04)
- [How to change the font, size, or color of a text watermark?](#watermark-05)
- [How to add a diagonal watermark to a document?](#watermark-06)
- [How to use the Watermark class in Aspose.Words?](#watermark-07)

### AI Features

- [What AI-powered features are available in Aspose.Words?](#ai-01)
- [How to use AI with Aspose.Words in C#?](#ai-02)
- [How to summarize a document using AI in Aspose.Words?](#ai-03)
- [How to translate a document using AI?](#ai-04)
- [How to use a large language model to process Word documents?](#ai-05)
- [How to integrate Aspose.Words with OpenAI?](#ai-06)
- [How to use AI models to analyze document content?](#ai-07)
- [What classes are available in the Aspose.Words.AI namespace?](#ai-08)


## Answers

<a id="ai-01"></a>

### What AI-powered features are available in Aspose.Words?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Aspose.Words exposes AI features in the `Aspose.Words.AI` namespace:

- **Summarization** — summarize one or more documents and choose a summary length. ([Guide](https://docs.aspose.com/words/net/summarize-a-document/))
- **Translation** — translate a document using Google generative models; the docs describe support for 300+ languages. ([Guide](https://docs.aspose.com/words/net/translate-a-document/))
- **Grammar checking** — detect and highlight grammar issues, with an option to improve stylistics. ([Guide](https://docs.aspose.com/words/net/grammar-checking/))

The documented model families include **OpenAI, Google Gemini, and Anthropic Claude**; translation is specifically documented with Google models. The docs also describe integrating self-hosted LLM implementations. ([Supported models](https://docs.aspose.com/words/net/supported-ai-models/))

<a id="ai-02"></a>

### How to use AI with Aspose.Words in C#?

Answer generated on first attempt.  
Generation model: gpt-6.1-terra

Aspose.Words provides an `Aspose.Words.AI` API for tasks such as summarizing, translating, and checking the grammar of documents. For example, to summarize a DOCX with OpenAI:

1. Add the **Aspose.Words** NuGet package to a C# console project.
2. Set the `OPENAI_API_KEY` environment variable to your OpenAI API key.
3. Put `input.docx` in the program’s working directory and run:

```csharp
using System;
using Aspose.Words;
using Aspose.Words.AI;

string apiKey = Environment.GetEnvironmentVariable("OPENAI_API_KEY")
    ?? throw new InvalidOperationException("Set OPENAI_API_KEY first.");

Document document = new Document("input.docx");
AiModel model = AiModel.Create(AiModelType.Gpt4OMini).WithApiKey(apiKey);

var options = new SummarizeOptions { SummaryLength = SummaryLength.Short };
Document summary = model.Summarize(document, options);
summary.Save("summary.docx");
```

The result is saved as `summary.docx`. The request uses the connected AI provider, so consider its costs and data-handling policies before processing sensitive documents. Review AI-generated content for accuracy.

See the [summarization guide](https://docs.aspose.com/words/net/summarize-a-document/) and [AI model API](https://reference.aspose.com/words/net/aspose.words.ai/aimodel/).

<a id="ai-03"></a>

### How to summarize a document using AI in Aspose.Words?

Answer generated on first attempt.  
Generation model: claude-sonnet-5.5

Use the `Aspose.Words.AI` namespace. Create an `AiModel` with your API key, then call `AiModel.Summarize`. It takes one `Document` or a `Document[]`, plus optional `SummarizeOptions`, and returns a new `Document` containing the summary.

```csharp
using System;
using Aspose.Words;
using Aspose.Words.AI;

string? apiKey = Environment.GetEnvironmentVariable("API_KEY");
if (string.IsNullOrEmpty(apiKey))
{
    Console.WriteLine("Set the API_KEY environment variable first.");
    return;
}

Document firstDoc = new Document("Big document.docx");
Document secondDoc = new Document("Document.docx");

// OpenAI, Google and Anthropic models are listed in the AiModelType enum.
AiModel model = AiModel.Create(AiModelType.Gpt4OMini).WithApiKey(apiKey);

SummarizeOptions options = new SummarizeOptions();

options.SummaryLength = SummaryLength.Short;
Document oneDocumentSummary = model.Summarize(firstDoc, options);
oneDocumentSummary.Save("AI.AiSummarize.One.docx");

options.SummaryLength = SummaryLength.Long;
Document multiDocumentSummary = model.Summarize(new Document[] { firstDoc, secondDoc }, options);
multiDocumentSummary.Save("AI.AiSummarize.Multi.docx");
```

- **Package:** `Aspose.Words`.
- **Inputs:** two DOCX files, plus an AI provider API key in `API_KEY`.
- **Outputs:** two DOCX summaries.
- **Not tested:** I didn't compile or run this. It is adapted from the documented sample.
- **Change from the docs:** I dropped the docs' `(OpenAiModel)` cast and `.WithOrganization(...).WithProject(...)` calls. I didn't check that `WithApiKey` returns `AiModel` directly. If you need organization or project settings, use the cast form shown in the docs.

Sources:
- https://docs.aspose.com/words/net/summarize-a-document/
- https://reference.aspose.com/words/net/aspose.words.ai/aimodel/summarize/

<a id="ai-04"></a>

### How to translate a document using AI?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Install the `Aspose.Words` NuGet package, set your Google AI API key in the `API_KEY` environment variable, then translate and save the document:

```csharp
using System;
using Aspose.Words;
using Aspose.Words.AI;

string apiKey = Environment.GetEnvironmentVariable("API_KEY")
    ?? throw new InvalidOperationException("Set the API_KEY environment variable.");

Document source = new Document("input.docx");
AiModel model = AiModel.Create(AiModelType.GeminiFlashLatest).WithApiKey(apiKey);
Document translated = model.Translate(source, Language.Arabic);
translated.Save("translated.docx");
```

Change `Language.Arabic` to your target language. Translation uses Google’s AI service, so an internet connection is required; the `Translate` method processes the whole document. [Translation guide](https://docs.aspose.com/words/net/translate-a-document/) · [Translate API](https://reference.aspose.com/words/net/aspose.words.ai/aimodel/translate/)

<a id="ai-05"></a>

### How to use a large language model to process Word documents?

Answer generated on first attempt.  
Generation model: gpt-6-luna

A practical pattern is: **load the Word file with Aspose.Words, send it to an LLM for a specific task, then save the result as a new document**. Aspose.Words’ `Aspose.Words.AI` namespace supports tasks such as summarizing, translating, and grammar checking with supported model providers. Here’s a complete C# example that summarizes a DOCX:

```csharp
using System;
using Aspose.Words;
using Aspose.Words.AI;

if (args.Length != 2)
    throw new ArgumentException("Usage: app <input.docx> <summary.docx>");

string apiKey = Environment.GetEnvironmentVariable("API_KEY")
    ?? throw new InvalidOperationException("Set API_KEY to your model provider key.");

Document input = new Document(args[0]);
AiModel model = AiModel.Create(AiModelType.Gpt4OMini).WithApiKey(apiKey);

var options = new SummarizeOptions { SummaryLength = SummaryLength.Medium };
Document summary = model.Summarize(input, options);
summary.Save(args[1]);
```

Install the `Aspose.Words` NuGet package with AI support, set `API_KEY`, then run the program with input and output paths. The document is sent to the configured model provider, so check your organization’s data-handling requirements; the Aspose documentation also notes an AI add-on subscription requirement. For model support and details, see [Summarize a Document](https://docs.aspose.com/words/net/summarize-a-document/) and [Supported AI Models](https://docs.aspose.com/words/net/supported-ai-models/).

<a id="ai-06"></a>

### How to integrate Aspose.Words with OpenAI?

Answer generated on first attempt.  
Generation model: claude-sonnet-5.5

Aspose.Words integrates with OpenAI through the `Aspose.Words.AI` namespace. It supports summarizing, translating and grammar-checking documents with OpenAI, Google and Claude models. You create a model with `AiModel.Create(AiModelType)`, set your key with `WithApiKey`, then call `Summarize`, `Translate` or `CheckGrammar`.

Requirements:
- NuGet package `Aspose.Words`.
- An OpenAI API key in the `API_KEY` environment variable.
- An input `.docx` file. The code writes the summary to a new file.

```csharp
using System;
using Aspose.Words;
using Aspose.Words.AI;

string? apiKey = Environment.GetEnvironmentVariable("API_KEY");
if (string.IsNullOrEmpty(apiKey))
{
    Console.WriteLine("Set the API_KEY environment variable.");
    return;
}

Document doc = new Document("input.docx");

AiModel model = AiModel.Create(AiModelType.Gpt4OMini).WithApiKey(apiKey);

SummarizeOptions options = new SummarizeOptions();
options.SummaryLength = SummaryLength.Short;

Document summary = model.Summarize(doc, options);
summary.Save("summary.docx");
```

Other operations use the same `model` object:
- `model.Translate(doc, Language.Russian)` translates a document.
- `model.CheckGrammar(doc)` checks grammar. `CheckGrammarOptions` is optional.
- `model.Summarize(new Document[] { a, b }, options)` summarizes several documents together.

For a self-hosted or OpenAI-compatible endpoint, subclass `OpenAiModel` and override `Url` and `Name`. The docs show this with `Translate`.

Notes:
- **Enum names:** the docs use both `AiModelType.Gpt4OMini` and `AiModelType.OpenAi_Gpt4o`. I couldn't list the enum members, so check the `AiModelType` reference page for your SDK version.
- **Testing:** I didn't compile or run this code.
- **Hand-rolled alternative:** you can instead extract text with Aspose.Words and call OpenAI yourself. I didn't verify that route.

Sources:
- https://docs.aspose.com/words/net/supported-ai-models/
- https://docs.aspose.com/words/net/summarize-a-document/
- https://docs.aspose.com/words/net/translate-a-document/
- https://docs.aspose.com/words/net/grammar-checking/
- https://docs.aspose.com/words/net/ai-powered-features/
- https://reference.aspose.com/words/net/aspose.words.ai/aimodel/
- https://reference.aspose.com/words/net/aspose.words.ai/aimodeltype/

<a id="ai-07"></a>

### How to use AI models to analyze document content?

Answer generated on first attempt.  
Generation model: claude-sonnet-5.5

Aspose.Words has an `Aspose.Words.AI` namespace. You create an `AiModel` for a hosted LLM (OpenAI, Google or Anthropic Claude), give it your API key, then call it on a `Document`. I didn't compile or run the code below.

Supported tasks:
- **Summarize:** `Summarize`, with `SummarizeOptions.SummaryLength`. It also accepts several documents at once.
- **Translate:** `Translate(doc, Language.X)`.
- **Check grammar:** `CheckGrammar`, with `CheckGrammarOptions`.

Each call returns a new `Document`, so you save it or read its text.

```csharp
using System;
using Aspose.Words;
using Aspose.Words.AI;

string? apiKey = Environment.GetEnvironmentVariable("API_KEY");
if (string.IsNullOrEmpty(apiKey))
{
    Console.WriteLine("Set the API_KEY environment variable.");
    return;
}

Document doc = new Document("Big document.docx");

// Model types come from the AiModelType enum; Gpt4OMini is the one used in the docs.
AiModel model = AiModel.Create(AiModelType.Gpt4OMini).WithApiKey(apiKey);

// 1. Summarize
SummarizeOptions summarizeOptions = new SummarizeOptions { SummaryLength = SummaryLength.Short };
Document summary = model.Summarize(doc, summarizeOptions);
summary.Save("Summary.docx");
Console.WriteLine(summary.GetText());

// 2. Translate
Document translated = model.Translate(doc, Language.Arabic);
translated.Save("Translated.docx");

// 3. Grammar check
CheckGrammarOptions grammarOptions = new CheckGrammarOptions { ImproveStylistics = true };
Document proofed = model.CheckGrammar(doc, grammarOptions);
proofed.Save("Proofed.docx");
```

Notes:
- **Input:** the code reads `Big document.docx` from the working directory. Replace it with your file.
- **Package:** it needs the `Aspose.Words` NuGet package, and an API key for the chosen provider.
- **Licensing:** the docs say the AI features need an active subscription that includes the AI add-on.
- **Self-hosted models:** you can use your own LLM by subclassing `OpenAiModel` and overriding `Url` and `Name`. See the supported-models page.
- **Not verified:** the `AiModelType` member list didn't resolve, so I used the enum names from the doc examples. The docs show both `Gpt4OMini` and `OpenAi_Gpt4o`, so check the enum in your installed version.

Sources:
- https://docs.aspose.com/words/net/ai-powered-features/
- https://docs.aspose.com/words/net/supported-ai-models/
- https://docs.aspose.com/words/net/summarize-a-document/
- https://docs.aspose.com/words/net/translate-a-document/
- https://docs.aspose.com/words/net/grammar-checking/
- https://reference.aspose.com/words/net/aspose.words.ai/aimodel/

<a id="ai-08"></a>

### What classes are available in the Aspose.Words.AI namespace?

Answer generated on first attempt.  
Generation model: gpt-6-luna

The `Aspose.Words.AI` namespace contains these classes:

- [`AiModel`](https://reference.aspose.com/words/net/aspose.words.ai/aimodel/)
- [`AnthropicAiModel`](https://reference.aspose.com/words/net/aspose.words.ai/anthropicaimodel/)
- [`AsposeLlmModel`](https://reference.aspose.com/words/net/aspose.words.ai/asposellmmodel/)
- [`CheckGrammarOptions`](https://reference.aspose.com/words/net/aspose.words.ai/checkgrammaroptions/)
- [`GoogleAiModel`](https://reference.aspose.com/words/net/aspose.words.ai/googleaimodel/)
- [`OpenAiModel`](https://reference.aspose.com/words/net/aspose.words.ai/openaimodel/)
- [`SummarizeOptions`](https://reference.aspose.com/words/net/aspose.words.ai/summarizeoptions/)

The namespace also includes the enums `AiModelType`, `Language`, and `SummaryLength`.

<a id="compare-01"></a>

### How to compare two Word documents in C#?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Install the `Aspose.Words` NuGet package, then compare the documents and save the first document with tracked revisions:

```csharp
using System;
using Aspose.Words;

var original = new Document("original.docx");
var revised = new Document("revised.docx");

if (original.Revisions.Count != 0 || revised.Revisions.Count != 0)
    throw new InvalidOperationException("Both documents must be free of existing revisions.");

original.Compare(revised, "Comparer", DateTime.Now);
original.Save("comparison.docx");
```

`comparison.docx` contains the comparison revisions on the original document. The `Compare` API also has an overload that accepts `CompareOptions` for filtering or tailoring comparison behavior. See the [Compare API](https://reference.aspose.com/words/net/aspose.words/document/compare/) and [document comparison guide](https://docs.aspose.com/words/net/compare-documents/).

<a id="compare-02"></a>

### How to find differences between DOCX documents using Aspose.Words?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Use `Document.Compare` to compare a baseline DOCX with a newer version. Aspose.Words records detected differences as revisions in the **first** document; save that document as the comparison result. Both input documents must be free of existing revisions.

Install the package with `dotnet add package Aspose.Words`, then run this complete example with the baseline, updated, and output file paths:

```csharp
using System;
using Aspose.Words;

if (args.Length != 3)
{
    Console.Error.WriteLine("Usage: compare <baseline.docx> <updated.docx> <comparison.docx>");
    return;
}

var baseline = new Document(args[0]);
var updated = new Document(args[1]);

if (baseline.Revisions.Count > 0 || updated.Revisions.Count > 0)
{
    throw new InvalidOperationException(
        "Both documents must have no existing revisions before comparison.");
}

baseline.Compare(updated, "Document comparison", DateTime.Now);
baseline.Save(args[2]);

Console.WriteLine(
    baseline.Revisions.Count == 0
        ? "No differences found."
        : $"Found {baseline.Revisions.Count} revisions. Open the output DOCX to review them.");
```

For settings such as ignoring formatting or headers and footers, see [`CompareOptions`](https://reference.aspose.com/words/net/aspose.words.comparing/compareoptions/). [Comparison guide](https://docs.aspose.com/words/net/compare-documents/) · [`Document.Compare` API](https://reference.aspose.com/words/net/aspose.words/document/compare/)

<a id="compare-03"></a>

### How to compare two documents and identify changes?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Use `Document.Compare`; it records differences as revisions in the first document. You can inspect each revision’s type and text, then save that document as a marked-up comparison copy. Install the **Aspose.Words** NuGet package and run this console app with the original, revised, and output file paths:

```csharp
using System;
using Aspose.Words;

if (args.Length != 3)
{
    Console.WriteLine("Usage: app <original.docx> <revised.docx> <comparison.docx>");
    return;
}

Document original = new Document(args[0]);
Document revised = new Document(args[1]);

if (original.Revisions.Count > 0 || revised.Revisions.Count > 0)
{
    throw new InvalidOperationException(
        "Both documents must have no existing revisions before comparison.");
}

original.Compare(revised, "Comparison", DateTime.Now);

foreach (Revision revision in original.Revisions)
{
    Console.WriteLine($"{revision.RevisionType}: {revision.ParentNode.GetText()}");
}

original.Save(args[2]);
```

The output file contains the detected changes as revisions; `Revisions.Count == 0` means no differences were detected. For options such as ignoring formatting or headers and footers, use the `CompareOptions` overload. [Compare documents guide](https://docs.aspose.com/words/net/compare-documents/) · [Document.Compare API](https://reference.aspose.com/words/net/aspose.words/document/compare/) · [Revision API](https://reference.aspose.com/words/net/aspose.words/revision/)

<a id="compare-04"></a>

### How to generate a document that shows differences between two versions?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Use `Document.Compare` to record the differences as revisions in the first document, then save it as a new file. Replace the sample paths with your files; the source documents should not already contain revisions.

```csharp
using System;
using Aspose.Words;

var original = new Document("version1.docx");
var updated = new Document("version2.docx");

original.Compare(updated, "Comparison", DateTime.Now);
original.Save("differences.docx");
```

Open `differences.docx` in Word to review the changes. The comparison API records edits and formatting changes as revisions in the compared document. [Compare documents](https://docs.aspose.com/words/net/compare-documents/) · [Document.Compare](https://reference.aspose.com/words/net/aspose.words/document/compare/) · [Document.Save](https://reference.aspose.com/words/net/aspose.words/document/save/)

<a id="compare-05"></a>

### How to compare Word documents programmatically?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Use `Document.Compare` to record differences as tracked revisions, then save the document you called `Compare` on. Install the package with `dotnet add package Aspose.Words`.

```csharp
using System;
using Aspose.Words;

var original = new Document("original.docx");
var revised = new Document("revised.docx");

if (original.Revisions.Count != 0 || revised.Revisions.Count != 0)
{
    throw new InvalidOperationException(
        "Both documents must be free of existing revisions before comparison.");
}

original.Compare(revised, "Comparison", DateTime.Now);
original.Save("comparison.docx");

Console.WriteLine(
    original.Revisions.Count == 0
        ? "No differences found."
        : $"Found {original.Revisions.Count} revisions.");
```

`comparison.docx` contains the first document with the detected changes marked as revisions. Aspose.Words requires both inputs to have no existing revisions before comparing. [Document.Compare API](https://reference.aspose.com/words/net/aspose.words/document/compare/) · [Compare Documents guide](https://docs.aspose.com/words/net/compare-documents/)

<a id="compare-06"></a>

### Can Aspose.Words compare documents and mark revisions?

Answer refined after a compilation repair.  
Generation model: gpt-6-luna · Repair model: claude-sonnet-5.5

Yes. `Document.Compare` compares two documents. It records the detected edits and formatting differences as tracked revisions in the document you call it on.

```csharp
using System;
using Aspose.Words;

class Program
{
    static void Main()
    {
        Document original = new Document("original.docx");
        Document edited = new Document("edited.docx");

        original.Compare(edited, "Reviewer", DateTime.Now);
        original.Save("comparison.docx");
    }
}
```

Neither document can already contain revisions when you compare them. The [`Document.Compare` API reference](https://reference.aspose.com/words/net/aspose.words/document/compare/) describes the behavior and options.

I haven't compiled or run this code. The only fix was adding the missing `using System;` for `DateTime`.

<a id="compare-07"></a>

### How to compare documents while ignoring formatting changes?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Set `CompareOptions.IgnoreFormatting` to `true`, then call `Document.Compare`. Formatting-only differences are ignored; content differences are recorded as revisions in the compared document.

```csharp
using System;
using Aspose.Words;
using Aspose.Words.Comparing;

var original = new Document("original.docx");
var revised = new Document("revised.docx");

var options = new CompareOptions
{
    IgnoreFormatting = true
};

original.Compare(revised, "Reviewer", DateTime.Now, options);
original.Save("comparison.docx");
```

The input documents must not already contain revisions when compared. See [`IgnoreFormatting`](https://reference.aspose.com/words/net/aspose.words.comparing/compareoptions/ignoreformatting/) and [`Document.Compare`](https://reference.aspose.com/words/net/aspose.words/document/compare/).

<a id="digital-signatures-01"></a>

### How to digitally sign a Word document in C#?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Install the package:

```sh
dotnet add package Aspose.Words
```

Set `PFX_PASSWORD` to the password for your PKCS#12 `.pfx` certificate, then use this complete console program. The certificate should contain the signing private key.

```csharp
using System;
using Aspose.Words.DigitalSignatures;

if (args.Length != 3)
{
    Console.Error.WriteLine("Usage: SignWord <input.docx> <certificate.pfx> <signed.docx>");
    return 2;
}

string password = Environment.GetEnvironmentVariable("PFX_PASSWORD")
    ?? throw new InvalidOperationException("Set the PFX_PASSWORD environment variable.");

CertificateHolder certificate = CertificateHolder.Create(args[1], password);
DigitalSignatureUtil.Sign(args[0], args[2], certificate);
return 0;
```

Pass the input Word file, certificate path, and output path as arguments. Aspose.Words supports signing DOC and DOCX files; avoid opening and saving the signed output with Aspose.Words afterward, as that can remove its digital signatures.

[Digital-signature guide](https://docs.aspose.com/words/net/working-with-digital-signatures/) · [CertificateHolder.Create](https://reference.aspose.com/words/net/aspose.words.digitalsignatures/certificateholder/create/) · [DigitalSignatureUtil.Sign](https://reference.aspose.com/words/net/aspose.words.digitalsignatures/digitalsignatureutil/sign/)

<a id="digital-signatures-02"></a>

### How to add a digital signature to a DOCX file using Aspose.Words?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Install the **Aspose.Words** NuGet package, then sign the DOCX with a PKCS#12 certificate (`.pfx`/`.p12`) that contains the private key:

```csharp
using System;
using Aspose.Words.DigitalSignatures;

string inputPath = "input.docx";
string certificatePath = "signing-certificate.pfx";
string outputPath = "input.signed.docx";
string certificatePassword = "your-certificate-password";

CertificateHolder certificate =
    CertificateHolder.Create(certificatePath, certificatePassword);

var options = new SignOptions
{
    Comments = "Approved",
    SignTime = DateTime.Now
};

DigitalSignatureUtil.Sign(inputPath, outputPath, certificate, options);

Console.WriteLine($"Signed document saved to {outputPath}");
```

The certificate must include a private key and have the `X509KeyStorageFlags.Exportable` flag set. Aspose.Words supports signing DOCX files; avoid opening and saving an already-signed document if you need to preserve its existing signature.

[Digital-signature guide](https://docs.aspose.com/words/net/working-with-digital-signatures/) · [CertificateHolder.Create](https://reference.aspose.com/words/net/aspose.words.digitalsignatures/certificateholder/create/) · [DigitalSignatureUtil.Sign](https://reference.aspose.com/words/net/aspose.words.digitalsignatures/digitalsignatureutil/sign/)

<a id="digital-signatures-03"></a>

### How to verify digital signatures in a Word document?

Answer generated on first attempt.  
Generation model: gpt-6-luna

With **Aspose.Words for .NET**, load the signatures and check both the count and `IsValid`. The count check matters because `IsValid` returns `true` when there are no signatures.

Install the `Aspose.Words` NuGet package, then run this console app with the signed Word file path as its argument:

```csharp
using System;
using Aspose.Words.DigitalSignatures;

if (args.Length != 1)
{
    Console.Error.WriteLine("Usage: VerifySignatures <signed-document.docx>");
    return;
}

DigitalSignatureCollection signatures =
    DigitalSignatureUtil.LoadSignatures(args[0]);

if (signatures.Count == 0)
{
    Console.WriteLine("No digital signatures found.");
    return;
}

Console.WriteLine(signatures.IsValid
    ? $"All {signatures.Count} signature(s) are valid."
    : "At least one signature is invalid.");
```

`IsValid` reports whether all signatures are valid and the document has not been tampered with. Avoid loading and then saving the document with Aspose.Words if you need to preserve its signatures; that can remove them. [Verification guide](https://docs.aspose.com/words/net/working-with-digital-signatures/) · [`LoadSignatures`](https://reference.aspose.com/words/net/aspose.words.digitalsignatures/digitalsignatureutil/loadsignatures/) · [`IsValid`](https://reference.aspose.com/words/net/aspose.words.digitalsignatures/digitalsignaturecollection/isvalid/)

<a id="digital-signatures-04"></a>

### How to check whether a Word document is digitally signed?

Answer generated on first attempt.  
Generation model: gpt-6-luna

With Aspose.Words for .NET, check `FileFormatInfo.HasDigitalSignature`:

```csharp
using System;
using Aspose.Words;
using Aspose.Words.DigitalSignatures;

string filePath = args.Length > 0 ? args[0] : "input.docx";

FileFormatInfo info = FileFormatUtil.DetectFileFormat(filePath);

if (!info.HasDigitalSignature)
{
    Console.WriteLine("The document has no digital signature.");
}
else
{
    var signatures = DigitalSignatureUtil.LoadSignatures(filePath);
    Console.WriteLine($"Found {signatures.Count} signature(s).");
    Console.WriteLine($"All signatures valid: {signatures.IsValid}");
}
```

Add the `Aspose.Words` NuGet package. `HasDigitalSignature` checks for the **presence** of a signature; `IsValid` checks whether all signatures are valid and the document has not been tampered with. [Detect signatures](https://docs.aspose.com/words/net/working-with-digital-signatures/) · [HasDigitalSignature API](https://reference.aspose.com/words/net/aspose.words/fileformatinfo/hasdigitalsignature/)

<a id="digital-signatures-05"></a>

### How to sign a document with a PFX certificate?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Use `CertificateHolder.Create` to load the PFX, then `DigitalSignatureUtil.Sign` to write a signed copy. Install the **Aspose.Words** NuGet package, and replace the example paths and password with yours:

```csharp
using Aspose.Words.DigitalSignatures;

const string inputPath = "input.docx";
const string signedPath = "signed.docx";
const string pfxPath = "certificate.pfx";
const string pfxPassword = "your-pfx-password";

CertificateHolder certificate = CertificateHolder.Create(pfxPath, pfxPassword);
DigitalSignatureUtil.Sign(inputPath, signedPath, certificate);
```

The PFX must contain the certificate’s private key. Sign after making your document edits; changes made after signing can invalidate the signature. See [Working with digital signatures](https://docs.aspose.com/words/net/working-with-digital-signatures/) and the API references for [`CertificateHolder.Create`](https://reference.aspose.com/words/net/aspose.words.digitalsignatures/certificateholder/create/) and [`DigitalSignatureUtil.Sign`](https://reference.aspose.com/words/net/aspose.words.digitalsignatures/digitalsignatureutil/sign/).

<a id="digital-signatures-06"></a>

### How to remove digital signatures from a Word document?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Use `DigitalSignatureUtil.RemoveAllSignatures` to save an unsigned copy. It removes **all** digital signatures; Aspose.Words does not support removing just one.

Install the `Aspose.Words` NuGet package, then run this complete C# example with the filenames changed to yours:

```csharp
using Aspose.Words.DigitalSignatures;

DigitalSignatureUtil.RemoveAllSignatures("signed.docx", "unsigned.docx");
```

The signed original is left unchanged, and the unsigned copy is written to `unsigned.docx`. [API reference](https://reference.aspose.com/words/net/aspose.words.digitalsignatures/digitalsignatureutil/removeallsignatures/) · [Digital signatures guide](https://docs.aspose.com/words/net/working-with-digital-signatures/)

<a id="digital-signatures-07"></a>

### How to use DigitalSignatureUtil in Aspose.Words?

Answer generated on first attempt.  
Generation model: gpt-6-luna

`DigitalSignatureUtil` is a static helper for signing documents, reading their signatures, and removing all signatures. This example signs an unsigned DOCX, checks the resulting signatures, then writes a separate unsigned copy. It expects an X.509 `.pfx` certificate containing a private key, and reads its password from the `ASPOSE_CERT_PASSWORD` environment variable.

Install the `Aspose.Words` NuGet package. Run the program with four arguments: input DOCX, certificate PFX, signed output path, and unsigned output path.

```csharp
using System;
using Aspose.Words.DigitalSignatures;

if (args.Length != 4)
    throw new ArgumentException(
        "Usage: <input.docx> <certificate.pfx> <signed.docx> <unsigned.docx>");

string? password = Environment.GetEnvironmentVariable("ASPOSE_CERT_PASSWORD");
if (string.IsNullOrWhiteSpace(password))
    throw new InvalidOperationException("Set ASPOSE_CERT_PASSWORD to the PFX password.");

CertificateHolder certificate = CertificateHolder.Create(args[1], password);

// Sign writes a signed copy; it does not overwrite the source.
DigitalSignatureUtil.Sign(args[0], args[2], certificate);

var signatures = DigitalSignatureUtil.LoadSignatures(args[2]);
if (signatures.Count == 0)
    throw new InvalidOperationException("The signed output contains no signatures.");
if (!signatures.IsValid)
    throw new InvalidOperationException("At least one signature is invalid or the document was modified.");

Console.WriteLine($"Verified {signatures.Count} signature(s).");

// This removes every signature and writes another copy; it does not remove just one.
DigitalSignatureUtil.RemoveAllSignatures(args[2], args[3]);
```

`LoadSignatures(...).IsValid` indicates whether all signatures are valid and the document has not been tampered with. Be careful when loading and saving a signed document for other edits: that can discard its signatures.

References: [Digital signature guide](https://docs.aspose.com/words/net/working-with-digital-signatures/), [DigitalSignatureUtil](https://reference.aspose.com/words/net/aspose.words.digitalsignatures/digitalsignatureutil/), [Sign](https://reference.aspose.com/words/net/aspose.words.digitalsignatures/digitalsignatureutil/sign/), [LoadSignatures](https://reference.aspose.com/words/net/aspose.words.digitalsignatures/digitalsignatureutil/loadsignatures/), [RemoveAllSignatures](https://reference.aspose.com/words/net/aspose.words.digitalsignatures/digitalsignatureutil/removeallsignatures/).

<a id="find-replace-01"></a>

### How to find and replace text in a Word document using C#?

Answer generated after resuming the run.  
Generation model: gpt-6-luna

Install the NuGet package with `dotnet add package Aspose.Words`, then use `Range.Replace` to replace every match and save the document:

```csharp
using System;
using Aspose.Words;

var doc = new Document("input.docx");
int replacements = doc.Range.Replace("old text", "new text");
doc.Save("output.docx");

Console.WriteLine($"Replaced {replacements} occurrence(s).");
```

The method returns the number of replacements. For case-sensitive or whole-word matching, use `FindReplaceOptions`. [Find and replace guide](https://docs.aspose.com/words/net/find-and-replace/) · [`Range.Replace` API](https://reference.aspose.com/words/net/aspose.words/range/replace/) · [`FindReplaceOptions` API](https://reference.aspose.com/words/net/aspose.words.replacing/findreplaceoptions/)

<a id="find-replace-02"></a>

### How to replace a string in a DOCX file with Aspose.Words?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Use `Document.Range.Replace` to replace every occurrence, then save the document:

```csharp
using System;
using Aspose.Words;

var document = new Document("input.docx");
int replacements = document.Range.Replace("old text", "new text");
document.Save("output.docx");

Console.WriteLine($"Replacements made: {replacements}");
```

Install the package with `dotnet add package Aspose.Words`. See the [find-and-replace guide](https://docs.aspose.com/words/net/find-and-replace/) and [`Range.Replace` API reference](https://reference.aspose.com/words/net/aspose.words/range/replace/).

<a id="find-replace-03"></a>

### How to replace all occurrences of a word in a document?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Use `Document.Range.Replace` to replace every matching occurrence, then save the document. Install the **Aspose.Words** NuGet package:

```csharp
using System;
using Aspose.Words;

var doc = new Document("input.docx");
int replacements = doc.Range.Replace("oldWord", "newWord");
doc.Save("output.docx");

Console.WriteLine($"Replaced {replacements} occurrence(s).");
```

This replaces the specified text throughout the document. See the [Replace API](https://reference.aspose.com/words/net/aspose.words/range/replace/) and [find-and-replace guide](https://docs.aspose.com/words/net/find-and-replace/).

<a id="find-replace-04"></a>

### How to find and replace text using regular expressions?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Install the package with `dotnet add package Aspose.Words`. Then pass a .NET `Regex` to `Range.Replace`; this example replaces “color” or “colour,” ignoring case, and reports how many replacements it made.

```csharp
using System;
using System.Text.RegularExpressions;
using Aspose.Words;

var doc = new Document("input.docx");
int count = doc.Range.Replace(
    new Regex(@"\bcolou?r\b", RegexOptions.IgnoreCase),
    "color");
doc.Save("output.docx");

Console.WriteLine($"Replacements: {count}");
```

`Range.Replace(Regex, string)` returns the replacement count. Change the pattern and replacement text to suit your case. See the [Replace API](https://reference.aspose.com/words/net/aspose.words/range/replace/), [Document constructor](https://reference.aspose.com/words/net/aspose.words/document/document/), and [Save API](https://reference.aspose.com/words/net/aspose.words/document/save/).

<a id="find-replace-05"></a>

### How to perform a case-insensitive text replacement in Word documents?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Set `FindReplaceOptions.MatchCase` to `false` and pass the options to `Range.Replace`:

```csharp
using Aspose.Words;
using Aspose.Words.Replacing;

var doc = new Document("input.docx");
var options = new FindReplaceOptions { MatchCase = false };

int replacements = doc.Range.Replace("Customer", "Client", options);

doc.Save("output.docx");
```

This replaces case-insensitive matches throughout the document; `replacements` contains the number made. Add the **Aspose.Words** NuGet package to your project. See the [find-and-replace guide](https://docs.aspose.com/words/net/find-and-replace/) and the references for [`MatchCase`](https://reference.aspose.com/words/net/aspose.words.replacing/findreplaceoptions/matchcase/) and [`Range.Replace`](https://reference.aspose.com/words/net/aspose.words/range/replace/).

<a id="find-replace-06"></a>

### How to replace text while preserving document formatting?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Use `Document.Range.Replace` to replace text in place rather than rebuilding the paragraph; it preserves the formatting of surrounding nodes.

```csharp
using System;
using Aspose.Words;

var doc = new Document("input.docx");
int count = doc.Range.Replace("old value", "new value");
doc.Save("output.docx");

Console.WriteLine($"Replaced {count} occurrence(s).");
```

Add the **Aspose.Words** NuGet package. The [`Range.Replace` API](https://reference.aspose.com/words/net/aspose.words/range/replace/) replaces matches, and the [ranges guide](https://docs.aspose.com/words/net/working-with-ranges/) describes preserving surrounding formatting.

<a id="find-replace-07"></a>

### How to use FindReplaceOptions in Aspose.Words?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Use `FindReplaceOptions` to configure the search, then pass it to `Range.Replace`. With `doc.Range`, the search covers the document.

```csharp
using System;
using Aspose.Words;
using Aspose.Words.Replacing;

Document doc = new Document("input.docx");

var options = new FindReplaceOptions
{
    MatchCase = false,        // Ignore case
    FindWholeWordsOnly = true // Don't match inside longer words
};

int replacements = doc.Range.Replace("Customer", "Client", options);

doc.Save("output.docx");
Console.WriteLine($"Replaced {replacements} occurrence(s).");
```

Add the **Aspose.Words** NuGet package and change the input/output paths for your files. `Replace` returns the number of replacements. Other options can control formatting and which document content is searched.

Docs: [Find and Replace guide](https://docs.aspose.com/words/net/find-and-replace/), [`FindReplaceOptions`](https://reference.aspose.com/words/net/aspose.words.replacing/findreplaceoptions/), [`MatchCase`](https://reference.aspose.com/words/net/aspose.words.replacing/findreplaceoptions/matchcase/), [`FindWholeWordsOnly`](https://reference.aspose.com/words/net/aspose.words.replacing/findreplaceoptions/findwholewordsonly/), and [`Range.Replace`](https://reference.aspose.com/words/net/aspose.words/range/replace/).

<a id="linq-reporting-01"></a>

### What is the LINQ Reporting Engine in Aspose.Words?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Aspose.Words’ **LINQ Reporting Engine** generates reports by filling Word document templates with application data. You place plain-text tags containing expressions in the template; the engine evaluates them against your data and replaces them with report content. Those expressions use a subset of C# and support LINQ-style operations such as sorting and grouping. It can work with custom .NET objects and data sources such as ADO.NET, JSON, XML, and CSV.

Unlike Mail Merge, it uses its own tag syntax rather than Word’s merge fields, and offers more flexibility for complex reports. [Introduction](https://docs.aspose.com/words/net/introduction-to-linq-reporting-engine/) · [Features](https://docs.aspose.com/words/net/linq-reporting-engine-features/) · [Comparison with Mail Merge](https://docs.aspose.com/words/net/linq-reporting-engine-or-mail-merge/)

<a id="linq-reporting-02"></a>

### How to generate reports using the LINQ Reporting Engine in C#?

Answer refined after a compilation repair.  
Generation model: gpt-6-luna · Repair model: gpt-6.1-terra

Use a Word document as the template, pass it and a data object to `ReportingEngine.BuildReport`, then save the populated document. For .NET 10, install Aspose.Words 26.10.0 with `dotnet add package Aspose.Words --version 26.10.0`.

In the template, add `<<[report.CustomerName]>>` where the customer name should appear. Then run this program with the template and output paths:

```csharp
using System;
using Aspose.Words;
using Aspose.Words.Reporting;

if (args.Length != 2)
{
    Console.Error.WriteLine("Usage: ReportApp <template.docx> <output.docx>");
    return;
}

var document = new Document(args[0]);
var engine = new ReportingEngine();
engine.BuildReport(document, new ReportData { CustomerName = "Contoso" }, "report");
document.Save(args[1]);

public class ReportData
{
    public string CustomerName { get; set; } = string.Empty;
}
```

For example: `dotnet run -- Template.docx Report.docx`. The `"report"` argument names the data source for template expressions; `BuildReport` fills the template, and `Save` writes the result. See the [report-building guide](https://docs.aspose.com/words/net/building-reports/) and the [`BuildReport` API reference](https://reference.aspose.com/words/net/aspose.words.reporting/reportingengine/buildreport/).

<a id="linq-reporting-03"></a>

### How to create a Word document from a LINQ Reporting template and data source using Aspose.Words ReportingEngine in C#?

Answer generated on first attempt.  
Generation model: claude-sonnet-5.5

The code below builds the template in memory with `DocumentBuilder` so it runs standalone. You can load your own `.docx` template instead. I haven't compiled or run it.

```csharp
using System;
using System.Collections.Generic;
using Aspose.Words;
using Aspose.Words.Reporting;

var template = new Document();
var builder = new DocumentBuilder(template);
builder.Writeln("Customer: <<[c.Name]>>");
builder.Writeln("<<foreach [o in c.Orders]>>");
builder.Writeln("<<[o.Product]>> x <<[o.Quantity]>> = <<[o.Quantity * o.Price]>>");
builder.Writeln("<</foreach>>");
builder.Writeln("Total: <<[c.Orders.Sum(o => o.Quantity * o.Price)]>>");

var customer = new Customer
{
    Name = "Contoso Ltd.",
    Orders = new List<Order>
    {
        new Order { Product = "Widget", Quantity = 3, Price = 9.5m },
        new Order { Product = "Gadget", Quantity = 1, Price = 24m }
    }
};

var engine = new ReportingEngine();
engine.BuildReport(template, customer, "c");

template.Save("Report.docx");
Console.WriteLine("Saved Report.docx");

public class Order
{
    public string Product { get; set; } = "";
    public int Quantity { get; set; }
    public decimal Price { get; set; }
}

public class Customer
{
    public string Name { get; set; } = "";
    public List<Order> Orders { get; set; } = new List<Order>();
}
```

**Key points**
- Install the `Aspose.Words` NuGet package.
- Template tags use `<<[expression]>>`, and `<<foreach [item in collection]>> … <</foreach>>` repeats a block.
- `BuildReport(Document, object, string)` fills the template. The third argument is the name the template uses for the data source (`c` above). You can omit it if the template uses contextual member access.
- The data source can be a custom public type, as above. It can also be a `DataSet`, `XmlDataSource`, `JsonDataSource` or `CsvDataSource`.
- To use a file template, replace the first lines with `new Document("Template.docx")`.
- I confirmed the `BuildReport` overloads and the data source types from the docs. I didn't check the `Sum` expression syntax against the docs, so confirm it in the LINQ Reporting Engine page.

Sources:
- https://docs.aspose.com/words/net/building-reports/
- https://reference.aspose.com/words/net/aspose.words.reporting/reportingengine/buildreport/
- https://docs.aspose.com/words/net/linq-reporting-engine/

<a id="linq-reporting-04"></a>

### How to populate a LINQ Reporting template with data using Aspose.Words ReportingEngine.BuildReport in C#?

Answer generated on first attempt.  
Generation model: claude-sonnet-5.5

Build the template (or load an existing `.docx`), then pass a data object to `BuildReport`. The overloads below were checked against the API reference. I haven't compiled or run the example.

```csharp
using System;
using System.Collections.Generic;
using Aspose.Words;
using Aspose.Words.Reporting;

Document doc = new Document();
DocumentBuilder builder = new DocumentBuilder(doc);

// In practice: Document doc = new Document("Template.docx");
builder.Writeln("Customer: <<[c.Name]>>");
builder.Writeln("<<foreach [item in c.Items]>>");
builder.Writeln("<<[item.Title]>> - <<[item.Price]>>");
builder.Writeln("<</foreach>>");

Customer customer = new Customer
{
    Name = "Jane Doe",
    Items = new List<OrderItem>
    {
        new OrderItem { Title = "Keyboard", Price = 49.90m },
        new OrderItem { Title = "Mouse", Price = 19.50m }
    }
};

ReportingEngine engine = new ReportingEngine();
// "c" is the data source name used in the template
engine.BuildReport(doc, customer, "c");

doc.Save("Report.docx");
Console.WriteLine("Saved Report.docx");

public class OrderItem
{
    public string Title { get; set; } = "";
    public decimal Price { get; set; }
}

public class Customer
{
    public string Name { get; set; } = "";
    public List<OrderItem> Items { get; set; } = new List<OrderItem>();
}
```

**Notes**
- Package: `Aspose.Words`. Namespace: `Aspose.Words.Reporting`.
- Overloads: `BuildReport(Document, object)`, `BuildReport(Document, object, string)` and `BuildReport(Document, object[], string[])` for several sources.
- The data source can be a mail-merge source such as a `DataSet`, an object of a public custom type, or an `XmlDataSource`, `JsonDataSource` or `CsvDataSource`.
- You can omit the name if the template uses contextual member access, for example `<<[Name]>>`.
- The data types must be public so the engine can see them.

Sources:
- https://docs.aspose.com/words/net/building-reports/
- https://reference.aspose.com/words/net/aspose.words.reporting/reportingengine/buildreport/

<a id="linq-reporting-05"></a>

### How to use LINQ expressions in a Word document template?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Use Aspose.Words’ **LINQ Reporting Engine**: put expressions in template tags, then pass the template and a data object to `BuildReport`.

In `Template.docx`, add tags such as:

```text
<<foreach [order in report.Orders.Where(o => o.Total >= 100).OrderBy(o => o.Total)]>>
<<[order.Customer]>> | <<[order.Total]>>
<</foreach>>
```

Then build the report:

```csharp
using System.Collections.Generic;
using Aspose.Words;
using Aspose.Words.Reporting;

var data = new ReportData
{
    Orders = new List<Order>
    {
        new() { Customer = "Northwind", Total = 125m },
        new() { Customer = "Contoso", Total = 80m }
    }
};

var document = new Document("Template.docx");
var engine = new ReportingEngine();
engine.BuildReport(document, data, "report");
document.Save("Report.docx");

public sealed class ReportData
{
    public List<Order> Orders { get; set; } = new();
}

public sealed class Order
{
    public string Customer { get; set; } = string.Empty;
    public decimal Total { get; set; }
}
```

The name `"report"` is the data-source name used in `report.Orders`. The engine supports lambda expressions as arguments to its built-in enumeration methods, including `Where` and `OrderBy`; lambdas aren’t general-purpose delegates in template expressions. [Template loops](https://docs.aspose.com/words/net/outputting-sequential-data/) · [Lambda functions](https://docs.aspose.com/words/net/using-lambda-functions/) · [`BuildReport`](https://reference.aspose.com/words/net/aspose.words.reporting/reportingengine/buildreport/)

<a id="linq-reporting-06"></a>

### How to use loops and conditions in LINQ Reporting Engine templates?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Use `<<foreach [...]>>...<</foreach>>` to repeat content for each item, and `<<if [...]>>...<<else>>...<</if>>` to choose content. The expressions in square brackets are evaluated against your data; an `if` expression must return a Boolean.

For example, put this in a Word template:

```text
<<if [report.Items.Count > 0]>>
Items:
<<foreach [item in report.Items]>>
- <<[item.Name]>>
<</foreach>>
<<else>>
No items.
<</if>>
```

Pass data with a matching `report` object when building the document:

```csharp
using System.Collections.Generic;
using Aspose.Words;
using Aspose.Words.Reporting;

var data = new ReportData
{
    Items = new List<Line>
    {
        new() { Name = "Alpha" },
        new() { Name = "Beta" }
    }
};

var document = new Document("Template.docx");
new ReportingEngine().BuildReport(document, data, "report");
document.Save("Report.docx");

public sealed class ReportData
{
    public List<Line> Items { get; set; } = new();
}

public sealed class Line
{
    public string Name { get; set; } = string.Empty;
}
```

Use `<<elseif [condition]>>` for additional branches; if no condition matches and there’s no `else`, the block is removed. Loops and conditional blocks can be nested. For the full syntax and examples, see [Outputting Sequential Data](https://docs.aspose.com/words/net/outputting-sequential-data/), [Using Conditional Blocks](https://docs.aspose.com/words/net/using-conditional-blocks/), and the [`BuildReport` API](https://reference.aspose.com/words/net/aspose.words.reporting/reportingengine/buildreport/).

<a id="linq-reporting-07"></a>

### How to generate reports from JSON or XML data in C#?

Answer generated on first attempt.  
Generation model: claude-sonnet-5.5

Use the LINQ Reporting Engine. Put `<<[Field]>>` tags in a template, wrap the data in `JsonDataSource` or `XmlDataSource`, and call `ReportingEngine.BuildReport`.

The program below needs the `Aspose.Words` NuGet package. It builds a template in code and writes sample data to a temp folder. It then produces `json-report.docx` and `xml-report.docx` in the working directory. I haven't compiled or run it.

```csharp
using System;
using System.IO;
using Aspose.Words;
using Aspose.Words.Reporting;

class Program
{
    static Document CreateTemplate()
    {
        Document doc = new Document();
        DocumentBuilder builder = new DocumentBuilder(doc);
        builder.Writeln("Name: <<[Name]>>, Age: <<[Age]>>, Born: <<[Birth]:\"dd.MM.yyyy\">>");
        builder.Writeln("Children:");
        builder.Writeln("<<foreach [in Child]>><<[Child_Text]>>");
        builder.Writeln("<</foreach>>");
        return doc;
    }

    static void Main()
    {
        string dir = Path.GetTempPath();
        string jsonPath = Path.Combine(dir, "person.json");
        string xmlPath = Path.Combine(dir, "person.xml");

        File.WriteAllText(jsonPath,
            "{ \"Name\": \"John Doe\", \"Age\": 30, \"Birth\": \"1989-04-01 4:00:00 pm\", \"Child\": [\"Ann Doe\", \"Charles Doe\"] }");
        File.WriteAllText(xmlPath,
            "<Person><Name>John Doe</Name><Age>30</Age><Birth>1989-04-01 4:00:00 pm</Birth>" +
            "<Child>Ann Doe</Child><Child>Charles Doe</Child></Person>");

        // JSON report
        Document jsonDoc = CreateTemplate();
        JsonDataSource jsonSource = new JsonDataSource(jsonPath);
        new ReportingEngine().BuildReport(jsonDoc, jsonSource);
        jsonDoc.Save("json-report.docx");

        // XML report
        Document xmlDoc = CreateTemplate();
        XmlDataSource xmlSource = new XmlDataSource(xmlPath);
        new ReportingEngine().BuildReport(xmlDoc, xmlSource);
        xmlDoc.Save("xml-report.docx");

        Console.WriteLine("Reports saved.");
    }
}
```

- **Template syntax:** For repeated simple XML elements, use the element name (`Child`) in `foreach` and `Child_Text` for the value. The same pattern is shown for JSON arrays.
- **Named data source:** If the root holds a single array (such as `persons`), pass a name. For example, `BuildReport(doc, source, "persons")` lets the template use `<<foreach [in persons]>>`.
- **Typed values:** `XmlDataSource` recognizes `Int64?`, `Double?`, `Boolean?` and `DateTime?` from their string form. For XML this works only if the values use invariant culture formatting. `JsonDataSource` gives typed values too.
- **Stream constructors:** Both data sources also accept streams, and options classes exist for each.

I checked `JsonDataSource`, `XmlDataSource` and `BuildReport` against the API lookups. The template syntax comes from the docs pages below. I didn't confirm the `XmlDataSource` stream constructor overloads beyond the symbol listing.

Sources:
- https://docs.aspose.com/words/net/accessing-json-data/
- https://docs.aspose.com/words/net/accessing-xml-data/
- https://docs.aspose.com/words/net/linq-reporting-engine-api/
- https://reference.aspose.com/words/net/aspose.words.reporting/jsondatasource/
- https://reference.aspose.com/words/net/aspose.words.reporting/xmldatasource/
- https://reference.aspose.com/words/net/aspose.words.reporting/reportingengine/buildreport/

<a id="linq-reporting-08"></a>

### What is the difference between LINQ Reporting Engine and Mail Merge?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Both **Mail Merge** and the **LINQ Reporting Engine** fill Word templates with data, but they use different template formats and suit different levels of complexity.

- **Mail Merge** uses Word’s built-in merge fields. It’s a good fit for existing mail-merge templates and straightforward tasks such as filling fields, formatting values, inserting images, or repeating data regions.
- **LINQ Reporting Engine** uses its own plain-text tags with C#-style expressions. It’s better suited to complex reports involving multiple data sources, LINQ operations such as sorting and grouping, or dynamic content such as charts and HTML.

**The templates aren’t interchangeable:** the LINQ Reporting Engine doesn’t process Word’s standard mail-merge fields. Keep using Mail Merge to reuse those templates; choose LINQ Reporting Engine when you need its richer expressions and reporting features. [Aspose.Words comparison](https://docs.aspose.com/words/net/linq-reporting-engine-or-mail-merge/)

<a id="mail-merge-01"></a>

### What is Mail Merge in Aspose.Words?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Mail Merge in Aspose.Words generates personalized documents from a template and a data source. You place merge fields—such as `FirstName` or `Address`—in the template; Aspose.Words fills them with values from each data record to create the merged document.

A simple merge fills fields in the document for each record. A merge with regions can repeat only designated sections, such as a table of order items. It’s commonly used for letters, labels, invoices, and reports. [Aspose.Words: Mail Merge and Reporting](https://docs.aspose.com/words/net/mail-merge-and-reporting/)

<a id="mail-merge-02"></a>

### How to perform mail merge in C#?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Install Aspose.Words with `dotnet add package Aspose.Words`. In a Word template, add merge fields named `FirstName` and `LastName` (for example, `«FirstName»` and `«LastName»`). Then load the template, supply matching field names and values, and save the result:

```csharp
using Aspose.Words;

var document = new Document("Template.docx");

document.MailMerge.Execute(
    new[] { "FirstName", "LastName" },
    new object[] { "Ada", "Lovelace" });

document.Save("Merged.docx");
```

The field names must match those in the template. This example merges one record; for multiple records, use the `DataTable` overload of `Execute`. See the [mail merge guide](https://docs.aspose.com/words/net/mail-merge-and-reporting/), [mail merge operation types](https://docs.aspose.com/words/net/types-of-mail-merge-operations/), and [`MailMerge.Execute` API reference](https://reference.aspose.com/words/net/aspose.words.mailmerging/mailmerge/execute/).

<a id="mail-merge-03"></a>

### How to populate a Word template with data using Mail Merge?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Use **Aspose.Words for .NET** to load the template, pass values whose names match its merge fields, and save the merged document. In Word, add fields such as `FirstName` and `LastName` using **Mailings → Insert Merge Field**.

Install the `Aspose.Words` NuGet package, then run this complete example with `Template.docx` in the working directory:

```csharp
using Aspose.Words;

var doc = new Document("Template.docx");

doc.MailMerge.Execute(
    new[] { "FirstName", "LastName" },
    new object[] { "Ada", "Lovelace" });

doc.Save("Completed.docx");
```

This fills a single record. For repeating data such as order items, use a template with **mail merge regions** instead; regions repeat only the designated part of the document. See the [Mail Merge template guide](https://docs.aspose.com/words/net/mail-merge-template/), [operation types](https://docs.aspose.com/words/net/types-of-mail-merge-operations/), and [`MailMerge.Execute` API reference](https://reference.aspose.com/words/net/aspose.words.mailmerging/mailmerge/execute/).

<a id="mail-merge-04"></a>

### How to generate personalized documents from a template?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Use **mail merge**: add merge fields such as `FirstName` and `Company` to your Word template, then load a fresh copy for each person and supply that person’s values.

Install the `Aspose.Words` NuGet package. This standalone example assumes `template.docx` contains `MERGEFIELD FirstName` and `MERGEFIELD Company`; it saves one personalized DOCX per recipient.

```csharp
using Aspose.Words;

var recipients = new[]
{
    new { FileName = "welcome-ava.docx", FirstName = "Ava", Company = "Northwind" },
    new { FileName = "welcome-liam.docx", FirstName = "Liam", Company = "Contoso" }
};

foreach (var recipient in recipients)
{
    var document = new Document("template.docx");
    document.MailMerge.Execute(
        new[] { "FirstName", "Company" },
        new object[] { recipient.FirstName, recipient.Company });
    document.Save(recipient.FileName);
}
```

The field names must match the template’s merge fields, and the names and values arrays must have the same number of entries. See the [mail merge guide](https://docs.aspose.com/words/net/mail-merge-and-reporting/), [`MailMerge.Execute`](https://reference.aspose.com/words/net/aspose.words.mailmerging/mailmerge/execute/), and [loading a document](https://docs.aspose.com/words/net/create-or-load-a-document/).

<a id="mail-merge-05"></a>

### How to perform mail merge with a data source in C#?

Answer generated on first attempt.  
Generation model: claude-sonnet-5.5

Use `Document.MailMerge.Execute` with a data source. It accepts a `DataTable`, `DataView`, `DataRow`, `IDataReader`, `IMailMergeDataSource`, or `string[]` field names with `object[]` values. I checked these overloads in the API reference. I haven't compiled or run the code.

The example needs the `Aspose.Words` NuGet package. It builds a template with `MERGEFIELD`s, merges a `DataTable` into it (one record per page), and saves `merged.docx`.

```csharp
using System.Data;
using Aspose.Words;

var doc = new Document();
var builder = new DocumentBuilder(doc);

builder.Write("Dear ");
builder.InsertField("MERGEFIELD FirstName");
builder.Write(" ");
builder.InsertField("MERGEFIELD LastName");
builder.Writeln(",");
builder.Writeln("Your order is confirmed.");

var table = new DataTable("Customers");
table.Columns.Add("FirstName", typeof(string));
table.Columns.Add("LastName", typeof(string));
table.Rows.Add("John", "Doe");
table.Rows.Add("Jane", "Smith");

doc.MailMerge.Execute(table);

doc.Save("merged.docx");
```

- **Existing template:** Use `new Document("template.docx")` instead of building one. Its merge fields must match the column names.
- **Repeating rows or regions:** Use `doc.MailMerge.ExecuteWithRegions(table)`. The table's `TableName` must match the region name.
- **A single record:** Use `Execute(string[] fieldNames, object[] values)`.

Sources:
- https://docs.aspose.com/words/net/mail-merge-and-reporting/
- https://docs.aspose.com/words/net/types-of-mail-merge-operations/
- https://reference.aspose.com/words/net/aspose.words.mailmerging/mailmerge/execute/

<a id="mail-merge-06"></a>

### How to use mail merge fields in a Word document?

Answer generated on first attempt.  
Generation model: gpt-6-luna

In Word, add a merge field where personalized text should appear: use **Mailings → Insert Merge Field** and choose a field such as `FirstName`. When merging, the field name must match a column in your data source.

With Aspose.Words for .NET, you can insert and fill a field in code:

```csharp
using Aspose.Words;

var doc = new Document();
var builder = new DocumentBuilder(doc);

builder.Write("Dear ");
builder.InsertField(" MERGEFIELD FirstName ");
builder.Write(",");
builder.InsertParagraph();
builder.Write("Welcome!");

doc.MailMerge.Execute(
    new[] { "FirstName" },
    new object[] { "Ava" });

doc.Save("merged.docx");
```

Install the **Aspose.Words** NuGet package. For multiple recipients, pass multiple records through a data source; simple mail merge creates a document for each record. [Mail merge operations](https://docs.aspose.com/words/net/types-of-mail-merge-operations/) · [InsertField API](https://reference.aspose.com/words/net/aspose.words/documentbuilder/insertfield/) · [MailMerge.Execute API](https://reference.aspose.com/words/net/aspose.words.mailmerging/mailmerge/execute/)

<a id="mail-merge-07"></a>

### How to execute mail merge with regions in Aspose.Words?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Install the package with `dotnet add package Aspose.Words`. Define a region in the template using `MERGEFIELD TableStart:People` and `MERGEFIELD TableEnd:People`; the region name must match the data table, and merge field names must match its columns.

This complete example creates a table whose data row repeats for each person, then saves the merged document:

```csharp
using System.Data;
using Aspose.Words;

var people = new DataTable("People");
people.Columns.Add("FirstName");
people.Columns.Add("LastName");
people.Rows.Add(new object[] { "Ada", "Lovelace" });
people.Rows.Add(new object[] { "Alan", "Turing" });

var doc = new Document();
var builder = new DocumentBuilder(doc);

builder.StartTable();
builder.InsertCell();
builder.Write("First name");
builder.InsertCell();
builder.Write("Last name");
builder.EndRow();

builder.InsertCell();
builder.InsertField(" MERGEFIELD TableStart:People");
builder.InsertField(" MERGEFIELD FirstName");
builder.InsertCell();
builder.InsertField(" MERGEFIELD LastName");
builder.InsertField(" MERGEFIELD TableEnd:People");
builder.EndRow();
builder.EndTable();

doc.MailMerge.ExecuteWithRegions(people);
doc.Save("output.docx");
```

For an existing template, load it with `new Document("template.docx")` instead of building it with `DocumentBuilder`. Keep the `TableStart` and `TableEnd` fields in the same table row. [Mail merge regions guide](https://docs.aspose.com/words/net/types-of-mail-merge-operations/) · [`ExecuteWithRegions(DataTable)` API](https://reference.aspose.com/words/net/aspose.words.mailmerging/mailmerge/executewithregions/)

<a id="mail-merge-08"></a>

### What is the difference between Mail Merge and LINQ Reporting Engine?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Both fill Word templates with data; the main difference is the template format and how much reporting logic you need.

| Mail Merge | LINQ Reporting Engine |
|---|---|
| Uses Word’s built-in merge fields, so it suits existing mail-merge templates and users familiar with Word’s feature. | Uses its own plain-text tags and expressions in the template. |
| Handles common needs such as formatting values, basic calculations, images, repeated regions, and conditional content. | Suits more complex reports: it supports multiple data sources, LINQ expressions, and features such as dynamic charts, HTML insertion, and merging table cells. |
| Supports ADO.NET data sources; custom sources can be implemented with `IMailMergeDataSource`. | Has built-in support for custom .NET objects, ADO.NET, JSON, XML, and CSV. |

**Rule of thumb:** keep Mail Merge for a standard Word mail-merge workflow. Choose the LINQ Reporting Engine when you need richer data manipulation or report layouts. Its templates use a different syntax, so it does not process Word’s standard merge fields directly.

[ Aspose.Words: LINQ Reporting Engine or Mail Merge](https://docs.aspose.com/words/net/linq-reporting-engine-or-mail-merge/)

<a id="merge-01"></a>

### How to merge multiple Word documents into one document in C#?

Answer generated on first attempt.  
Generation model: claude-sonnet-5.5

Signature confirmed: `AppendDocument(Document srcDoc, ImportFormatMode importFormatMode)`.

Use `Document.AppendDocument` in a loop. It appends each source document to the end of a destination document.

```csharp
using System;
using System.IO;
using Aspose.Words;

class Program
{
    static void Main()
    {
        string[] inputFiles = { "doc1.docx", "doc2.docx", "doc3.docx" };

        // Start with the first document as the destination.
        Document merged = new Document(inputFiles[0]);

        for (int i = 1; i < inputFiles.Length; i++)
        {
            if (!File.Exists(inputFiles[i]))
            {
                Console.WriteLine("Missing: " + inputFiles[i]);
                continue;
            }

            Document src = new Document(inputFiles[i]);
            // KeepSourceFormatting preserves each document's styles.
            // Use UseDestinationStyles to adopt the first document's styles.
            merged.AppendDocument(src, ImportFormatMode.KeepSourceFormatting);
        }

        merged.Save("Merged.docx");
    }
}
```

**Notes**
- Package: `Aspose.Words` (NuGet). Inputs: the listed .docx files. Output: `Merged.docx`.
- `ImportFormatMode.KeepSourceFormatting` keeps each document's look. `UseDestinationStyles` makes everything use the first document's styles.
- I didn't compile or run this snippet. The `AppendDocument` signature was checked against the API reference.

Docs:
- https://docs.aspose.com/words/net/insert-and-append-documents/
- https://docs.aspose.com/words/net/joining-word-documents-together/
- https://reference.aspose.com/words/net/aspose.words/document/appenddocument/

<a id="merge-02"></a>

### How to combine DOCX files using Aspose.Words?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Use `Document.AppendDocument` to append each file to the first document, then save the result. Add the `Aspose.Words` NuGet package and adjust the filenames as needed.

```csharp
using Aspose.Words;

var combined = new Document("first.docx");

string[] filesToAppend = { "second.docx", "third.docx" };

foreach (string file in filesToAppend)
{
    combined.AppendDocument(
        new Document(file),
        ImportFormatMode.KeepSourceFormatting);
}

combined.Save("combined.docx");
```

`KeepSourceFormatting` retains each appended document’s formatting. Use `ImportFormatMode.UseDestinationStyles` instead when you want imported content to follow the first document’s styles. [AppendDocument API](https://reference.aspose.com/words/net/aspose.words/document/appenddocument/) · [Combining documents guide](https://docs.aspose.com/words/net/insert-and-append-documents/) · [ImportFormatMode](https://reference.aspose.com/words/net/aspose.words/importformatmode/)

<a id="merge-03"></a>

### How to append one Word document to another?

Answer generated on first attempt.  
Generation model: gpt-6-luna

With **Aspose.Words for .NET**, load the destination and source documents, then append the source to the destination:

```csharp
using Aspose.Words;

var destination = new Document("destination.docx");
var source = new Document("source.docx");

destination.AppendDocument(source, ImportFormatMode.KeepSourceFormatting);
destination.Save("combined.docx");
```

Add the **Aspose.Words** NuGet package. `KeepSourceFormatting` aims to preserve the appended document’s formatting; use `ImportFormatMode.UseDestinationStyles` if you want its content to follow the destination’s styles instead.

[Append documents guide](https://docs.aspose.com/words/net/insert-and-append-documents/) · [`Document.AppendDocument` reference](https://reference.aspose.com/words/net/aspose.words/document/appenddocument/)

<a id="merge-04"></a>

### How to insert the contents of one document into another?

Answer generated on first attempt.  
Generation model: gpt-6-luna

To append one document to another, load both documents and call `AppendDocument`. This example keeps the source document’s formatting:

```csharp
using Aspose.Words;

var destination = new Document("destination.docx");
var source = new Document("source.docx");

destination.AppendDocument(source, ImportFormatMode.KeepSourceFormatting);
destination.Save("combined.docx");
```

For insertion at a particular position instead of the end, use `DocumentBuilder.InsertDocument`. [AppendDocument docs](https://reference.aspose.com/words/net/aspose.words/document/appenddocument/) · [InsertDocument docs](https://reference.aspose.com/words/net/aspose.words/documentbuilder/insertdocument/) · [Import format options](https://reference.aspose.com/words/net/aspose.words/importformatmode/)

<a id="merge-05"></a>

### How to merge Word documents while preserving formatting?

Answer generated on first attempt.  
Generation model: gpt-6-luna

With **Aspose.Words for .NET**, append each document using `ImportFormatMode.KeepSourceFormatting` to retain the appended document’s formatting.

Install the package with `dotnet add package Aspose.Words`, then run this complete example with `first.docx` and `second.docx` in the working directory:

```csharp
using Aspose.Words;

var merged = new Document("first.docx");
merged.AppendDocument(
    new Document("second.docx"),
    ImportFormatMode.KeepSourceFormatting);

merged.Save("merged.docx");
```

For additional documents, repeat the `AppendDocument` call before saving. See the [append and insert guide](https://docs.aspose.com/words/net/insert-and-append-documents/) and [`AppendDocument` API reference](https://reference.aspose.com/words/net/aspose.words/document/appenddocument/).

<a id="merge-06"></a>

### What is the difference between InsertDocument and AppendDocument?

Answer generated on first attempt.  
Generation model: gpt-6-luna

`DocumentBuilder.InsertDocument` inserts a source document at the builder’s **current cursor position**, so you can choose where it goes. `Document.AppendDocument` adds the source document to the **end** of the destination document.

Both accept an `ImportFormatMode` to control how formatting is handled. Note that `InsertDocument` is a method on `DocumentBuilder`, while `AppendDocument` is on `Document`.

[Insert and append documents guide](https://docs.aspose.com/words/net/insert-and-append-documents/) · [InsertDocument API](https://reference.aspose.com/words/net/aspose.words/documentbuilder/insertdocument/) · [AppendDocument API](https://reference.aspose.com/words/net/aspose.words/document/appenddocument/)

<a id="merge-07"></a>

### How to combine several Word documents into a single DOCX file?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Install Aspose.Words with `dotnet add package Aspose.Words`, then load the first DOCX and append the others:

```csharp
using Aspose.Words;

string[] inputFiles = { "first.docx", "second.docx", "third.docx" };

var combined = new Document(inputFiles[0]);

for (int i = 1; i < inputFiles.Length; i++)
{
    var next = new Document(inputFiles[i]);
    combined.AppendDocument(next, ImportFormatMode.KeepSourceFormatting);
}

combined.Save("combined.docx");
```

`AppendDocument` adds each document to the end; `KeepSourceFormatting` preserves the appended document’s formatting. Replace the filenames with your paths. [Append/insert guide](https://docs.aspose.com/words/net/insert-and-append-documents/) · [AppendDocument API](https://reference.aspose.com/words/net/aspose.words/document/appenddocument/)

<a id="pdf-to-other-01"></a>

### How to convert PDF to other document formats?

Answer generated on first attempt.  
Generation model: gpt-6-luna

With **Aspose.Words for .NET**, install the `Aspose.Words` NuGet package, then load the PDF and save it in a supported format:

```csharp
using Aspose.Words;

var document = new Document("input.pdf");
document.Save("output.docx");
document.Save("output.html", SaveFormat.Html);
```

Change the output filename or `SaveFormat` to choose another supported format. The [PDF conversion guide](https://docs.aspose.com/words/net/convert-pdf-to-other-document-formats/) covers PDF input, and the [supported formats list](https://docs.aspose.com/words/net/supported-document-formats/) shows available exports. For image-only or scanned PDFs, note that OCR is listed as an early-development or roadmap feature, so text extraction may require separate OCR.

<a id="pdf-to-other-02"></a>

### How to convert PDF to DOCX in C#?

Answer generated on first attempt.  
Generation model: claude-sonnet-5.5

Install the `Aspose.Words` NuGet package. Aspose.Words can load a PDF directly and save it as DOCX.

```csharp
using System;
using Aspose.Words;

class Program
{
    static void Main()
    {
        Document doc = new Document("input.pdf");
        doc.Save("output.docx", SaveFormat.Docx);
        Console.WriteLine("Saved output.docx");
    }
}
```

To control how the PDF is loaded, for example a password-protected file, pass a `PdfLoadOptions` object:

```csharp
using System;
using Aspose.Words;
using Aspose.Words.Loading;

class Program
{
    static void Main()
    {
        PdfLoadOptions options = new PdfLoadOptions();
        Document doc = new Document("input.pdf", options);
        doc.Save("output.docx");
        Console.WriteLine("Saved output.docx");
    }
}
```

- **Input and output:** `input.pdf` is read from the working directory, and `output.docx` is written there.
- **Verification:** I haven't compiled or run either snippet. I did not inspect the members of `PdfLoadOptions`, so check them before relying on any option.
- **Output quality:** A PDF has no flowing text structure, so the layout of the DOCX may differ from the PDF.

Docs:
- https://docs.aspose.com/words/net/convert-pdf-to-other-document-formats/
- https://docs.aspose.com/words/net/convert-a-document/
- https://reference.aspose.com/words/net/aspose.words.loading/pdfloadoptions/
- https://reference.aspose.com/words/net/aspose.words/document/save/

<a id="pdf-to-other-03"></a>

### How to convert a PDF document to Word in C#?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Install the NuGet package with `dotnet add package Aspose.Words`, then load the PDF and save it with a `.docx` extension:

```csharp
using Aspose.Words;

var document = new Document("input.pdf");
document.Save("output.docx");
```

The paths are relative to the app’s working directory; replace them with your PDF and desired output paths. PDF conversion supports common content such as text, images, tables, and lists, but some layouts or features—such as OCR and multicolumn text—may not convert as expected.

Docs: [Convert PDF to other formats](https://docs.aspose.com/words/net/convert-pdf-to-other-document-formats/) · [Document.Save API](https://reference.aspose.com/words/net/aspose.words/document/save/)

<a id="pdf-to-other-04"></a>

### How do I convert PDF to DOC or DOCX using Aspose.Words?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Install the **Aspose.Words** NuGet package, then load the PDF as a `Document` and save with the desired file extension:

```csharp
using Aspose.Words;

var document = new Document("input.pdf");

document.Save("output.doc");
document.Save("output.docx");
```

Save just the format you need, or both as shown. PDF-to-Word conversion can have fidelity limitations, especially with complex layouts; see Aspose’s [PDF conversion guide](https://docs.aspose.com/words/net/convert-pdf-to-other-document-formats/) and the [`Document` loading](https://reference.aspose.com/words/net/aspose.words/document/document/) and [`Save`](https://reference.aspose.com/words/net/aspose.words/document/save/) API references.

<a id="pdf-to-other-05"></a>

### How to convert PDF to HTML or an image in C#?

Answer generated on first attempt.  
Generation model: claude-sonnet-5.5

Aspose.Words can load a PDF into a `Document` and save it as HTML or as images. Pass `SaveFormat.Html` or `HtmlSaveOptions` for HTML, and `ImageSaveOptions` for images. I haven't compiled or run this code.

**Package:** `Aspose.Words` (NuGet)

```csharp
using System;
using Aspose.Words;
using Aspose.Words.Loading;
using Aspose.Words.Saving;

class Program
{
    static void Main()
    {
        string pdfPath = "input.pdf";

        Document doc = new Document(pdfPath, new PdfLoadOptions());

        // PDF -> HTML (images embedded as base64 in the HTML file)
        HtmlSaveOptions htmlOptions = new HtmlSaveOptions
        {
            ExportImagesAsBase64 = true,
            PrettyFormat = true
        };
        doc.Save("output.html", htmlOptions);

        // PDF -> PNG, one file per page
        ImageSaveOptions imageOptions = new ImageSaveOptions(SaveFormat.Png)
        {
            Resolution = 150
        };
        for (int i = 0; i < doc.PageCount; i++)
        {
            imageOptions.PageSet = new PageSet(i); // zero-based page index
            doc.Save($"page_{i + 1}.png", imageOptions);
        }

        Console.WriteLine($"Converted {doc.PageCount} page(s).");
    }
}
```

**Notes**
- **Input and output:** the input is `input.pdf` in the working directory. The output is `output.html` plus `page_N.png` files.
- **Default image behavior:** saving to an image renders only the first page unless you set `PageSet`.
- **Other image formats:** use `SaveFormat.Jpeg`, `Tiff` or `Gif` for other image types.
- **Accuracy:** PDF is converted through a flowing-document model, so the layout in the output may differ slightly from the original.

**Sources**
- https://docs.aspose.com/words/net/convert-pdf-to-other-document-formats/
- https://docs.aspose.com/words/net/convert-a-document-to-an-image/
- https://reference.aspose.com/words/net/aspose.words.loading/pdfloadoptions/
- https://reference.aspose.com/words/net/aspose.words.saving/imagesaveoptions/pageset/
- https://reference.aspose.com/words/net/aspose.words.saving/imagesaveoptions/resolution/
- https://reference.aspose.com/words/net/aspose.words.saving/htmlsaveoptions/exportimagesasbase64/

<a id="pdf-to-other-06"></a>

### Can Aspose.Words convert PDF to other formats?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Yes. Aspose.Words can load a PDF and save it in other supported formats, such as DOCX, DOC, HTML, PNG, or JPEG. For example:

```csharp
var doc = new Aspose.Words.Document("input.pdf");
doc.Save("output.docx");
```

PDF import supports content such as text, images, and tables, but conversion may not preserve every layout perfectly. OCR for scanned or non-searchable PDFs is not listed as supported. See [PDF conversion](https://docs.aspose.com/words/net/convert-pdf-to-other-document-formats/) and [supported formats](https://docs.aspose.com/words/net/supported-document-formats/).

<a id="pdf-to-other-07"></a>

### How to load a PDF document with PdfLoadOptions?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Install the `Aspose.Words` NuGet package, then pass `PdfLoadOptions` to the `Document` constructor:

```csharp
using Aspose.Words;
using Aspose.Words.Loading;

var options = new PdfLoadOptions();
var document = new Document("input.pdf", options);
document.Save("output.docx");
```

`input.pdf` is the PDF to load; the example saves the loaded document as `output.docx`. See the [PDF loading options guide](https://docs.aspose.com/words/net/convert-pdf-to-other-document-formats/) and the [`PdfLoadOptions` API reference](https://reference.aspose.com/words/net/aspose.words.loading/pdfloadoptions/).

<a id="split-01"></a>

### How to split a Word document into multiple documents in C#?

Answer generated on first attempt.  
Generation model: gpt-6-luna

With **Aspose.Words for .NET**, use `PageCount` and extract each page with `ExtractPages(index, 1)`. Add the package with `dotnet add package Aspose.Words`, then run this program from a directory containing `input.docx`:

```csharp
using System;
using System.IO;
using Aspose.Words;

string inputPath = "input.docx";
string outputDirectory = "split";

Directory.CreateDirectory(outputDirectory);

Document source = new Document(inputPath);

for (int pageIndex = 0; pageIndex < source.PageCount; pageIndex++)
{
    Document page = source.ExtractPages(pageIndex, 1);
    string outputPath = Path.Combine(outputDirectory, $"page-{pageIndex + 1}.docx");
    page.Save(outputPath);
}

Console.WriteLine($"Created {source.PageCount} page documents in '{outputDirectory}'.");
```

`ExtractPages` uses a zero-based page index, so the loop starts at `0`; `PageCount` calculates the document’s page layout. See the [ExtractPages API](https://reference.aspose.com/words/net/aspose.words/document/extractpages/) and [PageCount API](https://reference.aspose.com/words/net/aspose.words/document/pagecount/).

<a id="split-02"></a>

### How to split a DOCX file by pages using Aspose.Words?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Use `Document.PageCount` and extract one page at a time with `Document.ExtractPages` (its page index is zero-based). Install the NuGet package with `dotnet add package Aspose.Words`, then run this program from the directory containing `input.docx`:

```csharp
using Aspose.Words;

var document = new Document("input.docx");

for (int pageIndex = 0; pageIndex < document.PageCount; pageIndex++)
{
    Document page = document.ExtractPages(pageIndex, 1);
    page.Save($"page_{pageIndex + 1}.docx");
}
```

This creates `page_1.docx`, `page_2.docx`, and so on in the current directory. Aspose.Words notes that complex documents may have slight layout differences in extracted pages.

[Split a document](https://docs.aspose.com/words/net/split-a-document/) · [`ExtractPages` API](https://reference.aspose.com/words/net/aspose.words/document/extractpages/)

<a id="split-03"></a>

### How to extract each page of a Word document into a separate file?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Use `Document.PageCount` to get the number of pages, then `ExtractPages(index, 1)` to extract each page. This standalone C# example saves each page as a separate DOCX in a `pages` folder; replace `input.docx` with your file path. It requires the **Aspose.Words** NuGet package.

```csharp
using System.IO;
using Aspose.Words;

var document = new Document("input.docx");
const string outputDirectory = "pages";
Directory.CreateDirectory(outputDirectory);

for (int pageIndex = 0; pageIndex < document.PageCount; pageIndex++)
{
    Document page = document.ExtractPages(pageIndex, 1);
    page.Save(Path.Combine(outputDirectory, $"page-{pageIndex + 1}.docx"));
}
```

The extraction index is zero-based. Aspose.Words notes that complex documents may have slight layout differences in extracted pages. [Split a Document](https://docs.aspose.com/words/net/split-a-document/) · [`ExtractPages`](https://reference.aspose.com/words/net/aspose.words/document/extractpages/) · [`PageCount`](https://reference.aspose.com/words/net/aspose.words/document/pagecount/)

<a id="split-04"></a>

### How to split a Word document by sections?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Use the document’s section collection to create one DOCX per section. Add the `Aspose.Words` NuGet package, then set the input and output paths:

```csharp
using System.IO;
using Aspose.Words;

string inputPath = "input.docx";
string outputDirectory = "sections";

Directory.CreateDirectory(outputDirectory);
Document source = new Document(inputPath);

for (int i = 0; i < source.Sections.Count; i++)
{
    Document part = new Document();
    part.Sections.RemoveAt(0); // Remove the blank document's default section.

    Section section = source.Sections[i].Clone();
    part.Sections.Add(part.ImportNode(section, true));

    string outputPath = Path.Combine(outputDirectory, $"section-{i + 1}.docx");
    part.Save(outputPath);
}
```

This splits at existing section breaks; it does not split by page. [Aspose.Words: Split a Document](https://docs.aspose.com/words/net/split-a-document/) · [Document.ImportNode](https://reference.aspose.com/words/net/aspose.words/documentbase/importnode/) · [Section.Clone](https://reference.aspose.com/words/net/aspose.words/section/clone/)

<a id="split-05"></a>

### How to split a document by headings or other structural elements?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Aspose.Words can split **HTML output** at headings or other structural breaks. For example, split at Heading 1 and Heading 2 paragraphs:

```csharp
using Aspose.Words;
using Aspose.Words.Saving;

var doc = new Document("input.docx");
var options = new HtmlSaveOptions
{
    DocumentSplitCriteria = DocumentSplitCriteria.HeadingParagraph,
    DocumentSplitHeadingLevel = 2
};

doc.Save("output.html", options);
```

This creates separate HTML files at qualifying headings; use the built-in **Heading 1**, **Heading 2**, etc. styles for heading paragraphs. To split at another boundary, set `DocumentSplitCriteria` to `SectionBreak`, `ColumnBreak`, or `PageBreak`. With EPUB, the result stays in one EPUB file, divided into chapters; MHTML does not support this splitting option.

For **separate DOCX files by section**, iterate through `doc.Sections`, clone each section into a new document, and save it. The [split-document guide](https://docs.aspose.com/words/net/split-a-document/) covers both approaches; see also [`DocumentSplitCriteria`](https://reference.aspose.com/words/net/aspose.words.saving/documentsplitcriteria/) and [`DocumentSplitHeadingLevel`](https://reference.aspose.com/words/net/aspose.words.saving/htmlsaveoptions/documentsplitheadinglevel/).

<a id="split-06"></a>

### How to save each page of a Word document separately?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Use `Document.PageCount` to get the number of pages, then extract each page with `ExtractPages` and save it as a separate DOCX:

```csharp
using System.IO;
using Aspose.Words;

var document = new Document("input.docx");
var outputDirectory = "pages";
Directory.CreateDirectory(outputDirectory);

for (int page = 0; page < document.PageCount; page++)
{
    var extractedPage = document.ExtractPages(page, 1);
    extractedPage.Save(Path.Combine(outputDirectory, $"page-{page + 1}.docx"));
}
```

Install the **Aspose.Words** NuGet package and change `"input.docx"` to your file path. Complex documents may have slight layout differences in the extracted pages. [Split a document](https://docs.aspose.com/words/net/split-a-document/) · [`ExtractPages` API](https://reference.aspose.com/words/net/aspose.words/document/extractpages/)

<a id="split-07"></a>

### How to use DocumentSplitCriteria in Aspose.Words?

Answer generated on first attempt.  
Generation model: gpt-6.1-terra

Set `HtmlSaveOptions.DocumentSplitCriteria` before saving. For example, this splits a DOCX into HTML files at **Heading 1** and **Heading 2** paragraphs.

Install the **Aspose.Words** NuGet package, then use:

```csharp
using Aspose.Words;
using Aspose.Words.Saving;

var document = new Document("input.docx");

var options = new HtmlSaveOptions
{
    DocumentSplitCriteria = DocumentSplitCriteria.HeadingParagraph,
    DocumentSplitHeadingLevel = 2
};

document.Save("output.html", options);
```

The output starts with `output.html`; additional parts are named `output-01.html`, `output-02.html`, and so on. The source paragraphs must use the corresponding heading styles.

Other criteria include `SectionBreak`, `ColumnBreak`, and `PageBreak`; flags can be combined with `|`. `PageBreak` means an **explicit** page break, not every rendered page. For splitting by rendered pages or producing separate DOCX files, see the [document splitting guide](https://docs.aspose.com/words/net/split-a-document/).

`DocumentSplitCriteria` applies when saving to HTML, EPUB, or AZW3. For EPUB, it splits internal HTML parts rather than producing multiple EPUB files. See the [criteria reference](https://reference.aspose.com/words/net/aspose.words.saving/documentsplitcriteria/) and [heading-level option](https://reference.aspose.com/words/net/aspose.words.saving/htmlsaveoptions/documentsplitheadinglevel/).

<a id="watermark-01"></a>

### How to add a watermark to a Word document in C#?

Answer generated on first attempt.  
Generation model: claude-sonnet-5.5

Use `Document.Watermark.SetText` with `TextWatermarkOptions`. Package: `Aspose.Words`. I haven't compiled or run this.

```csharp
using System.Drawing;
using Aspose.Words;

class Program
{
    static void Main()
    {
        // Input: an existing file. Output: a copy with the watermark.
        Document doc = new Document("input.docx");

        TextWatermarkOptions options = new TextWatermarkOptions
        {
            FontFamily = "Arial",
            FontSize = 72,
            Color = Color.Gray,
            Layout = WatermarkLayout.Diagonal,
            IsSemitrasparent = true
        };

        doc.Watermark.SetText("CONFIDENTIAL", options);
        doc.Save("output.docx");
    }
}
```

- Call `doc.Watermark.SetText("text")` with no options to use the defaults.
- Call `doc.Watermark.SetImage(...)` for an image watermark.
- Call `doc.Watermark.Remove()` to remove a watermark.
- I verified the `TextWatermarkOptions` members above. I did not check the `WatermarkLayout.Diagonal` enum value separately.

Docs:
- https://docs.aspose.com/words/net/working-with-watermark/
- https://docs.aspose.com/words/net/add-watermark/
- https://reference.aspose.com/words/net/aspose.words/watermark/settext/
- https://reference.aspose.com/words/net/aspose.words/textwatermarkoptions/

<a id="watermark-02"></a>

### How to insert a text watermark into a DOCX file?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Install the `Aspose.Words` NuGet package, then load the DOCX, add the watermark, and save the result:

```csharp
using Aspose.Words;

var document = new Document("input.docx");
document.Watermark.SetText("CONFIDENTIAL");
document.Save("output.docx");
```

For formatting options such as font, size, color, and diagonal layout, see the [watermark guide](https://docs.aspose.com/words/net/working-with-watermark/) and [`Watermark.SetText`](https://reference.aspose.com/words/net/aspose.words/watermark/settext/).

<a id="watermark-03"></a>

### How to add an image watermark to a Word document?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Install the package with `dotnet add package Aspose.Words`, then load the document, apply the image watermark, and save:

```csharp
using Aspose.Words;

var document = new Document("input.docx");
var options = new ImageWatermarkOptions
{
    Scale = 5,
    IsWashout = true
};

document.Watermark.SetImage("watermark.png", options);
document.Save("output.docx");
```

Replace the filenames with your paths. The watermark guide shows this approach; see also the [`SetImage` API](https://reference.aspose.com/words/net/aspose.words/watermark/setimage/) and [`ImageWatermarkOptions`](https://reference.aspose.com/words/net/aspose.words/imagewatermarkoptions/).

<a id="watermark-04"></a>

### How to remove a watermark from a Word document using Aspose.Words?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Use `Document.Watermark.Remove()` to remove a standard text or image watermark, then save the document:

```csharp
using Aspose.Words;

var doc = new Document("input.docx");

if (doc.Watermark.Type != WatermarkType.None)
    doc.Watermark.Remove();

doc.Save("output.docx");
```

Install the **Aspose.Words** NuGet package. If the watermark was added as a custom shape rather than through the watermark API, remove that shape separately; the [watermark guide](https://docs.aspose.com/words/net/working-with-watermark/) describes that case. API references: [`Watermark.Remove`](https://reference.aspose.com/words/net/aspose.words/watermark/remove/) and [`Watermark.Type`](https://reference.aspose.com/words/net/aspose.words/watermark/type/).

<a id="watermark-05"></a>

### How to change the font, size, or color of a text watermark?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Set the formatting on `TextWatermarkOptions`, then pass those options when adding the text watermark:

```csharp
using System.Drawing;
using Aspose.Words;

var document = new Document();

var options = new TextWatermarkOptions
{
    FontFamily = "Arial",
    FontSize = 36f,
    Color = Color.DarkRed
};

document.Watermark.SetText("CONFIDENTIAL", options);
document.Save("watermarked.docx");
```

Change `FontFamily`, `FontSize`, or `Color` to customize the appearance. See the [TextWatermarkOptions reference](https://reference.aspose.com/words/net/aspose.words/textwatermarkoptions/) and [`Watermark.SetText`](https://reference.aspose.com/words/net/aspose.words/watermark/settext/).

<a id="watermark-06"></a>

### How to add a diagonal watermark to a document?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Create a rotated text shape and place a copy in each section’s primary, first-page, and even-page headers. Install the **Aspose.Words** NuGet package; this example reads `input.docx` and writes `output.docx`.

```csharp
using Aspose.Words;
using Aspose.Words.Drawing;

var doc = new Document("input.docx");

var watermark = new Shape(doc, ShapeType.TextPlainText)
{
    Width = 500,
    Height = 100,
    Rotation = -40,
    RelativeHorizontalPosition = RelativeHorizontalPosition.Page,
    RelativeVerticalPosition = RelativeVerticalPosition.Page,
    WrapType = WrapType.None,
    VerticalAlignment = VerticalAlignment.Center,
    HorizontalAlignment = HorizontalAlignment.Center,
    StrokeColor = System.Drawing.Color.LightGray
};

watermark.TextPath.Text = "CONFIDENTIAL";
watermark.TextPath.FontFamily = "Arial";
watermark.Fill.Color = System.Drawing.Color.LightGray;

var watermarkParagraph = new Paragraph(doc);
watermarkParagraph.AppendChild(watermark);

foreach (Section section in doc.Sections)
{
    InsertIntoHeader(watermarkParagraph, section, HeaderFooterType.HeaderPrimary);
    InsertIntoHeader(watermarkParagraph, section, HeaderFooterType.HeaderFirst);
    InsertIntoHeader(watermarkParagraph, section, HeaderFooterType.HeaderEven);
}

doc.Save("output.docx");

void InsertIntoHeader(Paragraph paragraph, Section section, HeaderFooterType headerType)
{
    HeaderFooter? header = section.HeadersFooters[headerType];

    if (header is null)
    {
        header = new HeaderFooter(section.Document, headerType);
        section.HeadersFooters.Add(header);
    }

    header.AppendChild(paragraph.Clone(true));
}
```

Adjust the text, angle, dimensions, and color to suit the document. [Aspose.Words watermark guide](https://docs.aspose.com/words/net/add-watermark/) · [Shape rotation reference](https://reference.aspose.com/words/net/aspose.words.drawing/shapebase/rotation/)

<a id="watermark-07"></a>

### How to use the Watermark class in Aspose.Words?

Answer generated on first attempt.  
Generation model: gpt-6-luna

`Watermark` is accessed through `Document.Watermark`; use `SetText` or `SetImage` to add one, and `Remove` to delete it. Install the **Aspose.Words** NuGet package. This example reads `input.docx` and writes `watermarked.docx`:

```csharp
using Aspose.Words;

var doc = new Document("input.docx");

var options = new TextWatermarkOptions
{
    FontFamily = "Arial",
    FontSize = 36,
    Layout = WatermarkLayout.Diagonal,
    IsSemitrasparent = true
};

doc.Watermark.SetText("DRAFT", options);
doc.Save("watermarked.docx");
```

For an image watermark, use `doc.Watermark.SetImage("logo.png", imageOptions)` with `ImageWatermarkOptions`. To remove a text watermark, check `doc.Watermark.Type == WatermarkType.Text` before calling `doc.Watermark.Remove()`.

[Watermark guide](https://docs.aspose.com/words/net/working-with-watermark/) · [SetText API](https://reference.aspose.com/words/net/aspose.words/watermark/settext/) · [Remove API](https://reference.aspose.com/words/net/aspose.words/watermark/remove/)

<a id="word-to-excel-01"></a>

### How to convert DOC/DOCX to Excel?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Use Aspose.Words for .NET to load the DOC or DOCX, then save it as XLSX. Add the package with `dotnet add package Aspose.Words`, then run this standalone program with the input and output paths:

```csharp
using Aspose.Words;
using Aspose.Words.Saving;

var inputPath = args.Length > 0 ? args[0] : "input.docx";
var outputPath = args.Length > 1 ? args[1] : "output.xlsx";

var doc = new Document(inputPath);
doc.Save(outputPath, new XlsxSaveOptions { SaveFormat = SaveFormat.Xlsx });
```

For example: `dotnet run -- report.doc report.xlsx`. Word page layout may not map directly to spreadsheet cells, so check the resulting workbook. See the [Word-to-Excel guide](https://docs.aspose.com/words/net/convert-a-document-to-excel/) and [XlsxSaveOptions reference](https://reference.aspose.com/words/net/aspose.words.saving/xlsxsaveoptions/).

<a id="word-to-excel-02"></a>

### How to convert a Word document to Excel?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Install the NuGet package with `dotnet add package Aspose.Words`, then load the Word file and save it as XLSX:

```csharp
using Aspose.Words;

var document = new Document("input.docx");
document.Save("output.xlsx", SaveFormat.Xlsx);
```

This exports to an Excel workbook. Word page layout may not map neatly to spreadsheet cells, so check the result—especially if the document contains tables or complex formatting. See the [Word-to-Excel conversion guide](https://docs.aspose.com/words/net/convert-a-document-to-excel/) and [supported formats](https://docs.aspose.com/words/net/supported-document-formats/).

<a id="word-to-excel-03"></a>

### How to convert DOC/DOCX to XLSX in C#?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Install Aspose.Words, then load the `.doc` or `.docx` and save as XLSX:

```bash
dotnet add package Aspose.Words
```

```csharp
using Aspose.Words;

var document = new Document("input.docx"); // "input.doc" works too
document.Save("output.xlsx", SaveFormat.Xlsx);
```

Aspose.Words supports exporting Word documents to XLSX. The result is a spreadsheet, not a layout-preserving copy of the Word pages; check the workbook if the document contains content beyond tables. See the [Word-to-Excel guide](https://docs.aspose.com/words/net/convert-a-document-to-excel/) and [supported formats](https://docs.aspose.com/words/net/supported-document-formats/).

<a id="word-to-excel-04"></a>

### How do I convert a DOC/DOCX document to Excel in C#?

Answer generated on first attempt.  
Generation model: gpt-6.1-terra

Use **Aspose.Words for .NET** to load the Word document and save it directly as an XLSX workbook.

Install the NuGet package:

```bash
dotnet add package Aspose.Words
```

Then run this C# program, changing the input path to your `.doc` or `.docx` file:

```csharp
using Aspose.Words;

var document = new Document("input.docx"); // Also accepts input.doc
document.Save("output.xlsx");
```

The `.xlsx` extension selects the output format. An existing `output.xlsx` is overwritten. Because Word and Excel use different layouts, review the resulting workbook for formatting and cell arrangement.

See the [Word-to-Excel conversion guide](https://docs.aspose.com/words/net/convert-a-document-to-excel/) and [`Document.Save` reference](https://reference.aspose.com/words/net/aspose.words/document/save/).

<a id="word-to-excel-05"></a>

### How to convert Word to XLSX in C#?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Install the NuGet package with `dotnet add package Aspose.Words`, then load the Word file and save it with an `.xlsx` extension:

```csharp
using Aspose.Words;

var document = new Document("input.docx");
document.Save("output.xlsx");
```

Replace the paths with your input and desired output files. Aspose.Words supports saving Word documents as XLSX; review the resulting workbook if you need specific table-to-column mapping. See the [Word-to-Excel guide](https://docs.aspose.com/words/net/convert-a-document-to-excel/) and [`Document.Save`](https://reference.aspose.com/words/net/aspose.words/document/save/).

<a id="word-to-excel-06"></a>

### Can Aspose.Words convert DOCX to Excel?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Yes. Aspose.Words for .NET can save a DOCX as an XLSX workbook. It exports document content to a spreadsheet, but complex layouts may not translate exactly; check the result for your document. [Convert Word to Excel](https://docs.aspose.com/words/net/convert-a-document-to-excel/) · [Supported formats](https://docs.aspose.com/words/net/supported-document-formats/)

<a id="word-to-html-01"></a>

### How to convert DOC/DOCX to HTML?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Install the `Aspose.Words` NuGet package, then load the Word file and save it with an `.html` extension:

```csharp
using Aspose.Words;

var document = new Document("input.docx"); // or "input.doc"
document.Save("output.html");
```

Aspose.Words determines the output format from the filename extension. See the [document conversion guide](https://docs.aspose.com/words/net/convert-a-document-to-html-mhtml-or-epub/) and [`Document.Save`](https://reference.aspose.com/words/net/aspose.words/document/save/).

<a id="word-to-html-02"></a>

### How to convert a document to HTML?

Answer generated on first attempt.  
Generation model: gpt-6-luna

With Aspose.Words for .NET, load the source document and save it with an `.html` filename:

```csharp
using Aspose.Words;

var document = new Document("input.docx");
document.Save("output.html");
```

Add the **Aspose.Words** NuGet package. The output extension determines the save format. [HTML conversion guide](https://docs.aspose.com/words/net/convert-a-document-to-html-mhtml-or-epub/) · [Document.Save API](https://reference.aspose.com/words/net/aspose.words/document/save/)

<a id="word-to-html-03"></a>

### How to convert DOC/DOCX to HTML in C#?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Install Aspose.Words with `dotnet add package Aspose.Words`, then load the DOC or DOCX and save it as HTML:

```csharp
using Aspose.Words;

var document = new Document("input.docx"); // Also accepts .doc
document.Save("output.html", SaveFormat.Html);
```

Aspose.Words determines the input format from the file and writes HTML using the specified save format. See the [HTML conversion guide](https://docs.aspose.com/words/net/convert-a-document-to-html-mhtml-or-epub/) and [`Document.Save`](https://reference.aspose.com/words/net/aspose.words/document/save/).

<a id="word-to-html-04"></a>

### How do I convert a DOC/DOCX document to HTML in C#?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Install the **Aspose.Words** NuGet package, then load the Word file and save it as HTML:

```csharp
using Aspose.Words;

var inputPath = args.Length > 0 ? args[0] : "input.docx";
var outputPath = args.Length > 1 ? args[1] : "output.html";

var document = new Document(inputPath);
document.Save(outputPath, SaveFormat.Html);
```

Pass either a `.doc` or `.docx` path as the first argument; the second argument is the HTML output path. Aspose.Words documents this load-and-save conversion pattern in its [HTML conversion guide](https://docs.aspose.com/words/net/convert-a-document-to-html-mhtml-or-epub/). See [installation instructions](https://docs.aspose.com/words/net/installation/) for adding the NuGet package.

<a id="word-to-image-01"></a>

### How to convert DOC/DOCX to an image?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Install the **Aspose.Words** NuGet package, then load the DOC or DOCX and save it as an image:

```csharp
using Aspose.Words;
using Aspose.Words.Saving;

var document = new Document("input.docx"); // A .doc file works too.
var options = new ImageSaveOptions(SaveFormat.Png) { Resolution = 300 };

document.Save("output.png", options);
```

For JPEG, use `SaveFormat.Jpeg` and an `.jpg` output filename. For multi-page documents, use `PageSet` to select pages or `MultiPageLayout` to arrange them in a single image.

[Convert a document to an image](https://docs.aspose.com/words/net/convert-a-document-to-an-image/) · [ImageSaveOptions](https://reference.aspose.com/words/net/aspose.words.saving/imagesaveoptions/) · [Resolution](https://reference.aspose.com/words/net/aspose.words.saving/imagesaveoptions/resolution/)

<a id="word-to-image-02"></a>

### How to convert a Word document to an image?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Use `Document.Save` with `ImageSaveOptions` to render a Word document as PNG:

```csharp
using Aspose.Words;
using Aspose.Words.Saving;

var doc = new Document("input.docx");
var options = new ImageSaveOptions(SaveFormat.Png)
{
    Resolution = 300
};

doc.Save("output.png", options);
```

Add the **Aspose.Words** NuGet package. For documents with multiple pages, Aspose.Words also supports multi-page image layouts and TIFF frames; see the [multi-page image guide](https://docs.aspose.com/words/net/convert-a-multi-page-document-to-an-image/). More rendering options are in the [image conversion guide](https://docs.aspose.com/words/net/convert-a-document-to-an-image/) and [`ImageSaveOptions` reference](https://reference.aspose.com/words/net/aspose.words.saving/imagesaveoptions/).

<a id="word-to-image-03"></a>

### How to convert DOC/DOCX to PNG in C#?

Answer generated on first attempt.  
Generation model: gpt-6.1-terra

Install the **Aspose.Words** NuGet package, then load the DOC or DOCX and save each page as a separate PNG:

```csharp
using Aspose.Words;
using Aspose.Words.Saving;

string inputPath = "input.docx"; // Also accepts a .doc file.
Document document = new Document(inputPath);

ImageSaveOptions options = new ImageSaveOptions(SaveFormat.Png);
options.Resolution = 150; // DPI

for (int page = 0; page < document.PageCount; page++)
{
    options.PageSet = new PageSet(page); // Page indexes are zero-based.
    document.Save($"page-{page + 1}.png", options);
}
```

The output files are `page-1.png`, `page-2.png`, and so on, in the working directory. Existing files with those names are overwritten. Adjust `Resolution` to change the image DPI.

See the [Word-to-PNG guide](https://docs.aspose.com/words/net/convert-word-document-to-png/) and [PageSet reference](https://reference.aspose.com/words/net/aspose.words.saving/pageset/pageset/).

<a id="word-to-image-04"></a>

### How do I convert a DOC/DOCX document to an image in C#?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Install Aspose.Words with `dotnet add package Aspose.Words`. This example saves each page of a DOC or DOCX as a separate PNG:

```csharp
using System.IO;
using Aspose.Words;
using Aspose.Words.Saving;

var document = new Document("input.docx"); // A .doc file works too.
var outputDirectory = "images";
Directory.CreateDirectory(outputDirectory);

var options = new ImageSaveOptions(SaveFormat.Png);

for (int pageIndex = 0; pageIndex < document.PageCount; pageIndex++)
{
    options.PageSet = new PageSet(pageIndex);
    document.Save(
        Path.Combine(outputDirectory, $"page-{pageIndex + 1}.png"),
        options);
}
```

`PageSet` uses zero-based page indexes. To save JPEG instead, use `SaveFormat.Jpeg` and a `.jpg` filename extension. [Convert a document to an image](https://docs.aspose.com/words/net/convert-a-document-to-an-image/) · [Convert a multi-page document](https://docs.aspose.com/words/net/convert-a-multi-page-document-to-an-image/) · [PageSet API](https://reference.aspose.com/words/net/aspose.words.saving/pageset/)

<a id="word-to-image-05"></a>

### How to save a Word document as an image?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Use `ImageSaveOptions` with `Document.Save`. Install the **Aspose.Words** NuGet package, then run this standalone C# example with your input and output paths:

```csharp
using Aspose.Words;
using Aspose.Words.Saving;

var document = new Document("input.docx");
var options = new ImageSaveOptions(SaveFormat.Png)
{
    Resolution = 300
};

document.Save("output.png", options);
```

For JPEG, use `SaveFormat.Jpeg` and an output filename ending in `.jpg`. See the [Document.Save API](https://reference.aspose.com/words/net/aspose.words/document/save/) and [ImageSaveOptions](https://reference.aspose.com/words/net/aspose.words.saving/imagesaveoptions/).

<a id="word-to-image-06"></a>

### Can Aspose.Words convert DOCX to JPG or PNG?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Yes. Aspose.Words can render a DOCX as PNG or JPEG. For multi-page documents, it can create an image for each page; you can also select specific pages. See the [document-to-image guide](https://docs.aspose.com/words/net/convert-a-document-to-an-image/) and [multi-page image guide](https://docs.aspose.com/words/net/convert-a-multi-page-document-to-an-image/).

<a id="word-to-markdown-01"></a>

### How to convert DOC/DOCX to Markdown?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Use Aspose.Words for .NET: load the `.doc` or `.docx` file, then save it with an `.md` extension.

Install the **Aspose.Words** NuGet package, then run this complete example:

```csharp
using Aspose.Words;

var document = new Document("input.docx"); // Or "input.doc"
document.Save("output.md");
```

Images are saved alongside the Markdown file by default. To choose another image folder, use `MarkdownSaveOptions.ImagesFolder`.

[Markdown conversion guide](https://docs.aspose.com/words/net/convert-a-document-to-markdown/) · [Document.Save API](https://reference.aspose.com/words/net/aspose.words/document/save/) · [ImagesFolder API](https://reference.aspose.com/words/net/aspose.words.saving/markdownsaveoptions/imagesfolder/)

<a id="word-to-markdown-02"></a>

### How to convert a Word document to Markdown?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Use Aspose.Words: load the Word file as a `Document`, then save it with an `.md` extension. Install the package with `dotnet add package Aspose.Words`.

```csharp
using Aspose.Words;

var document = new Document("input.docx");
document.Save("output.md");
```

Replace the filenames with your input and output paths. Aspose.Words determines the output format from the filename extension. [Markdown conversion guide](https://docs.aspose.com/words/net/convert-a-document-to-markdown/) · [`Document.Save`](https://reference.aspose.com/words/net/aspose.words/document/save/)

<a id="word-to-markdown-03"></a>

### How to convert DOC/DOCX to Markdown in C#?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Install Aspose.Words:

```bash
dotnet add package Aspose.Words
```

Pass the input and output paths as command-line arguments. The `.md` extension selects Markdown output:

```csharp
using System;
using Aspose.Words;

if (args.Length != 2)
    throw new ArgumentException("Usage: ConvertToMarkdown <input.doc|input.docx> <output.md>");

var document = new Document(args[0]);
document.Save(args[1]);
```

Aspose.Words loads supported Word formats and saves them as Markdown. If the document contains images, they are saved as separate files alongside the Markdown by default; `MarkdownSaveOptions.ImagesFolder` lets you choose another folder.

Sources: [Convert a Document to Markdown](https://docs.aspose.com/words/net/convert-a-document-to-markdown/) · [Document.Save API](https://reference.aspose.com/words/net/aspose.words/document/save/)

<a id="word-to-markdown-04"></a>

### How do I convert a DOC/DOCX document to Markdown in C#?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Install Aspose.Words, then load the DOC/DOCX and save with a `.md` extension:

```sh
dotnet add package Aspose.Words
```

```csharp
using System;
using Aspose.Words;

if (args.Length != 2)
{
    Console.Error.WriteLine("Usage: convert <input.doc|input.docx> <output.md>");
    return 2;
}

var document = new Document(args[0]);
document.Save(args[1]);
return 0;
```

For example: `dotnet run -- input.docx output.md`. Aspose.Words detects the input format and selects Markdown from the output extension. Images are saved alongside the Markdown by default; use `MarkdownSaveOptions.ImagesFolder` to choose another folder.

Docs: [Convert a Document to Markdown](https://docs.aspose.com/words/net/convert-a-document-to-markdown/), [`Document.Save`](https://reference.aspose.com/words/net/aspose.words/document/save/), [`MarkdownSaveOptions.ImagesFolder`](https://reference.aspose.com/words/net/aspose.words.saving/markdownsaveoptions/imagesfolder/).

<a id="word-to-markdown-05"></a>

### How to save a Word document as a Markdown file?

Answer generated on first attempt.  
Generation model: gpt-6-luna

With Aspose.Words for .NET, load the Word file and save it with a `.md` extension:

```csharp
using Aspose.Words;

var document = new Document("input.docx");
document.Save("output.md");
```

Add the `Aspose.Words` NuGet package. `Save` determines the output format from the filename extension. [Convert a Document to Markdown](https://docs.aspose.com/words/net/convert-a-document-to-markdown/) · [Document.Save API](https://reference.aspose.com/words/net/aspose.words/document/save/)

<a id="word-to-markdown-06"></a>

### Can Aspose.Words convert DOCX to Markdown?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Yes. Aspose.Words for .NET can load a DOCX and save it as Markdown:

```csharp
using Aspose.Words;

var document = new Document("input.docx");
document.Save("output.md");
```

The output extension selects Markdown format. For options such as controlling image output, use `MarkdownSaveOptions`. [Conversion guide](https://docs.aspose.com/words/net/convert-a-document-to-markdown/) · [MarkdownSaveOptions](https://reference.aspose.com/words/net/aspose.words.saving/markdownsaveoptions/)

<a id="word-to-pdf-01"></a>

### How to convert DOC/DOCX to PDF?

Answer generated on first attempt.  
Generation model: gpt-6-luna

Install the package with `dotnet add package Aspose.Words`, then load the DOC or DOCX and save with a `.pdf` extension:

```csharp
using Aspose.Words;

const string inputPath = "input.docx"; // Or use a .doc file.
const string outputPath = "output.pdf";

var document = new Document(inputPath);
document.Save(outputPath);
```

Replace the input path with your file’s location. Aspose.Words detects the output format from the `.pdf` extension. [DOC/DOCX to PDF guide](https://docs.aspose.com/words/net/convert-a-document-to-pdf/) · [`Document.Save`](https://reference.aspose.com/words/net/aspose.words/document/save/)

<a id="word-to-pdf-02"></a>

### How to convert a document to PDF?

Answer generated on first attempt.  
Generation model: gpt-6-luna

With Aspose.Words for .NET, load the source document and save it with a `.pdf` extension. Install the package with `dotnet add package Aspose.Words`, then run this console app with `input.docx` in its working directory:

```csharp
using Aspose.Words;

Document doc = new Document("input.docx");
doc.Save("output.pdf");
```

Aspose.Words detects the input format and uses the output extension to select PDF. See the [conversion guide](https://docs.aspose.com/words/net/convert-a-document-to-pdf/) and [`Document.Save`](https://reference.aspose.com/words/net/aspose.words/document/save/).

<a id="word-to-pdf-03"></a>

### How to convert DOC/DOCX to PDF in C#?

Answer generated on first attempt.  
Generation model: claude-sonnet-5.5

Load the DOC or DOCX into `Aspose.Words.Document`, then save it with a `.pdf` extension. `Document.Save` picks the PDF format from the extension. I haven't compiled or run this code.

Install the NuGet package `Aspose.Words`.

```csharp
using System;
using Aspose.Words;
using Aspose.Words.Saving;

class Program
{
    static void Main()
    {
        // Input can be .doc or .docx; the format is detected automatically.
        Document doc = new Document("input.docx");

        // Simple conversion: the format is inferred from the extension.
        doc.Save("output.pdf");

        // Optional: control PDF output with PdfSaveOptions.
        PdfSaveOptions options = new PdfSaveOptions();
        doc.Save("output-options.pdf", options);

        Console.WriteLine("Done");
    }
}
```

- `input.docx` must exist in the working directory. The code produces `output.pdf` and `output-options.pdf`.
- I only listed the documentation pages below. I didn't check the exact `PdfSaveOptions` members.

Sources:
- https://docs.aspose.com/words/net/convert-a-document-to-pdf/
- https://reference.aspose.com/words/net/aspose.words/document/save/
- https://reference.aspose.com/words/net/aspose.words.saving/pdfsaveoptions/

<a id="word-to-pdf-04"></a>

### How do I convert a DOC/DOCX document to PDF in C#?

Answer generated on first attempt.  
Generation model: claude-sonnet-5.5

Load the document with `Aspose.Words.Document`, then save it with a `.pdf` extension. The format is inferred from the extension. Both DOC and DOCX load the same way.

Package: `Aspose.Words` (NuGet).

```csharp
using Aspose.Words;
using Aspose.Words.Saving;

class Program
{
    static void Main()
    {
        // Input: any DOC or DOCX file. Output: PDF.
        Document doc = new Document("input.docx");

        // Simple conversion (format inferred from extension)
        doc.Save("output.pdf");

        // Optional: explicit format and PDF options
        PdfSaveOptions options = new PdfSaveOptions();
        doc.Save("output-with-options.pdf", options);
    }
}
```

I haven't compiled or run this. I confirmed that the docs show `Document.Save` and `PdfSaveOptions` for PDF conversion, but I didn't check individual `PdfSaveOptions` members.

Docs:
- https://docs.aspose.com/words/net/convert-a-document-to-pdf/
- https://reference.aspose.com/words/net/aspose.words/document/save/
- https://reference.aspose.com/words/net/aspose.words.saving/pdfsaveoptions/
