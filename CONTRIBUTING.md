# Contributing to LLM Technical Reports

Thanks for your interest in contributing!

## How to Add a New Report

1. **Fork** this repository
2. **Edit** `README.md` — find the appropriate company section
3. **Add** your entry following this format:

```markdown
| YYYY-MM | Model Name | Type | [Title](URL) |
```

4. **Submit** a Pull Request

## Entry Types

- **Paper** — Published on arXiv or similar academic venues
- **Technical Report** — Official technical documentation from the company
- **System Card** — Safety and capability evaluation documents
- **Model Card** — Model specification and limitation documents
- **Blog** — Official company blog posts (when no paper exists)
- **GitHub** — Official repository (when no paper/blog exists)

## Rules

1. **Official sources only** — Link to the original publication (arXiv, company CDN, official blog)
2. **Chronological order** — New entries go at the bottom of each company section
3. **Date format** — Use `YYYY-MM`
4. **No PDFs** — We link, not download
5. **One row per model/version** — If a model has both a paper and system card, use separate rows

## Adding a New Company

If the company doesn't exist yet:

1. Add it to the Table of Contents
2. Create a new `## Company Name` section
3. Add the table header:

```markdown
| Date | Model | Type | Link |
|:-----|:------|:-----|:-----|
```

4. Add your entries

## Using with AI Assistants

This repo includes a **skill file** for AI coding assistants (Cursor, Copilot, CoPaw, etc.):

```
.cursor/skills/llm-tech-report-maintenance/SKILL.md
```

Load it as context when asking your AI to update this repo. It contains:
- Exact table schema and field definitions
- Step-by-step procedures for all operations
- Commit message conventions
- Guardrails (no PDF downloads, no content extraction, etc.)

## Questions?

Open an issue if you're unsure about anything!
