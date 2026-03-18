# Skill: LLM Tech Report Maintenance

> **For AI coding assistants (Cursor, Copilot, CoPaw, etc.).**
> Load this file as context when you need to add, update, or validate entries in this repo.

---

## 1. Repo Overview

```
llm-tech-report/
├── README.md            ← The only data file. All reports live here.
├── CONTRIBUTING.md      ← Human-readable contribution guide
├── LICENSE
└── .cursor/skills/…     ← This skill file
```

**Core rule: links only, never download PDFs, never read PDF content.**

---

## 2. README.md Schema

### 2.1 Company Section

Each company is an `## H2` heading. Inside it sits **one Markdown table**:

```markdown
## Company Name

| Date | Model | Type | Link |
|:-----|:------|:-----|:-----|
| YYYY-MM | Model Name | Type | [Display Text](URL) |
```

### 2.2 Field Definitions

| Field | Format | Example |
|-------|--------|---------|
| **Date** | `YYYY-MM` | `2025-01` |
| **Model** | Official model name / version | `DeepSeek-R1` |
| **Type** | One of the values below | `Paper` |
| **Link** | `[Display Text](URL)` | `[Technical Report](https://arxiv.org/abs/…)` |

### 2.3 Allowed Type Values

| Type | When to use |
|------|-------------|
| `Paper` | Peer-reviewed or arXiv publication |
| `Technical Report` | Official technical document (not peer-reviewed) |
| `System Card` | Safety / capability evaluation doc (OpenAI, Anthropic style) |
| `Model Card` | Model spec / limitations doc (Google, HuggingFace style) |
| `Blog` | Official company blog post (when no paper exists) |
| `GitHub` | Official repo (when no paper or blog exists) |

### 2.4 Link Priority

When multiple sources exist for the same model, prefer (highest → lowest):

1. **arXiv** (`arxiv.org/abs/…`) — most stable
2. **Official CDN** (`cdn.openai.com`, `assets.anthropic.com`, `storage.googleapis.com`)
3. **Official blog** (`openai.com/blog`, `qwen.ai/blog`)
4. **GitHub repo** (`github.com/org/repo`)
5. **Web Archive** (`web.archive.org`) — only when original is dead

If a model has **both** a paper and a system card, add **two separate rows**.

---

## 3. Operations

### 3.1 Add a Report to an Existing Company

```
Steps:
1. Read README.md
2. Find the company's H2 section
3. Confirm the model is NOT already listed (avoid duplicates)
4. Append a new row at the END of that company's table
5. Keep chronological order (oldest → newest)
6. Commit
```

**Example edit** — appending to DeepSeek:

```diff
  | 2025-12 | DeepSeek-V3.2 | Paper | [DeepSeek-V3.2](https://arxiv.org/abs/2512.02556) |
+ | 2026-05 | DeepSeek-V4 | Paper | [DeepSeek-V4](https://arxiv.org/abs/2605.XXXXX) |
```

### 3.2 Add a New Company

```
Steps:
1. Read README.md
2. Add entry to the Table of Contents section (keep logical grouping)
3. Insert a new H2 section at the appropriate position:
   - Western companies: after existing Western companies
   - Chinese companies: after existing Chinese companies
4. Use this template:

## Company Name

| Date | Model | Type | Link |
|:-----|:------|:-----|:-----|
| YYYY-MM | ModelName | Type | [Title](URL) |

5. Commit
```

### 3.3 Search & Verify a Report Link

```
Steps:
1. Search for the report:
   - arXiv: https://arxiv.org/search/?query=MODEL+NAME&searchtype=all
   - Google Scholar: https://scholar.google.com/
   - Company website / blog
2. Verify the link loads correctly (open & snapshot if using browser tool)
3. Extract: title, date, URL, type
4. Follow 3.1 or 3.2 to add
```

### 3.4 Batch Update

When adding multiple reports at once:

```
Steps:
1. Read full README.md
2. Collect all new entries, grouped by company
3. For each company, append rows to the existing table
4. Single commit with descriptive message
```

### 3.5 Fix a Broken Link

```
Steps:
1. Identify the broken row
2. Search for the new/correct URL (arXiv, official site, Web Archive)
3. Replace the URL in the Link column
4. Commit
```

---

## 4. Commit Message Convention

| Action | Format |
|--------|--------|
| Add report(s) | `add: MODEL_NAME from COMPANY` |
| Add company | `add: COMPANY section with N reports` |
| Fix link | `fix: update link for MODEL_NAME` |
| Batch update | `update: add N reports (COMPANY1, COMPANY2, …)` |
| Other | `chore: description` |

---

## 5. Current Company Directory

| Region | Companies |
|--------|-----------|
| 🇺🇸 US | OpenAI · Google/DeepMind · Anthropic · Meta · Microsoft/Phi · xAI · Cohere |
| 🇪🇺 EU | Mistral AI |
| 🇨🇳 CN | DeepSeek · Alibaba/Qwen · ByteDance · Zhipu AI · Moonshot/Kimi · Baidu/ERNIE · Tencent/Hunyuan · MiniMax · Baichuan · 01.AI/Yi · Meituan · StepFun · InclusionAI · Xiaomi/MiMo |

---

## 6. Guardrails

- ❌ Never download or store PDF files
- ❌ Never read/parse PDF content for summaries
- ✅ Always `read` before `edit` — never blindly overwrite
- ✅ Always check for duplicates before adding
- ✅ Keep entries sorted chronologically (oldest → newest) within each company
- ✅ Verify link accessibility when possible
