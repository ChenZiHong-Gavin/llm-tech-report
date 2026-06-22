# AGENTS.md

Guidance for AI coding agents (Codex, etc.) working in the **llm-tech-report** repo.

## Project

A curated index of LLM technical reports, papers, and model/system cards.

```
llm-tech-report/
├── README.md            ← The only data file. All reports live here.
├── README_CN.md         ← Chinese mirror of README.md — keep in sync.
├── CONTRIBUTING.md       ← Human-readable contribution guide
├── LICENSE
└── .claude/skills/…      ← Detailed skill docs (maintenance + logo-generation)
```

**Core rule: links only — never download PDFs, never read/parse PDF content.**

There are two kinds of task: **(A) maintaining the report data** and **(B) regenerating the logo**.

---

## A. Report maintenance

`README.md` holds one Markdown table per company under an `## H2` heading:

```markdown
## Company Name

| Date | Model | Type | Link |
|:-----|:------|:-----|:-----|
| YYYY-MM | Model Name | Type | [Display Text](URL) |
```

### Field definitions
- **Date** — `YYYY-MM` (e.g. `2025-01`)
- **Model** — official model name / version (e.g. `DeepSeek-R1`)
- **Type** — one of the allowed values below
- **Link** — `[Display Text](URL)`

### Allowed `Type` values
- `Paper` — peer-reviewed or arXiv publication
- `Technical Report` — official technical document (not peer-reviewed)
- `System Card` — safety / capability evaluation doc (OpenAI, Anthropic style)
- `Model Card` — model spec / limitations doc (Google, HuggingFace style)
- `Blog` — official company blog post (when no paper exists)
- `GitHub` — official repo (when no paper or blog exists)

### Link priority (highest → lowest)
1. **arXiv** (`arxiv.org/abs/…`) — most stable
2. **Official CDN** (`cdn.openai.com`, `assets.anthropic.com`, `storage.googleapis.com`)
3. **Official blog** (`openai.com/blog`, `qwen.ai/blog`)
4. **GitHub repo** (`github.com/org/repo`)
5. **Web Archive** (`web.archive.org`) — only when the original is dead

If a model has **both** a paper and a system card, add **two separate rows**.

### Operations

**Add a report to an existing company**
1. Read README.md
2. Find the company's H2 section
3. Confirm the model is NOT already listed (avoid duplicates)
4. Append a new row at the END of that company's table
5. Keep chronological order (oldest → newest)
6. Mirror the edit into `README_CN.md`, then commit

**Add a new company**
1. Add an entry to the Table of Contents (keep logical grouping)
2. Insert a new H2 section at the right position (Western companies after Western, Chinese after Chinese)
3. Use the table template above
4. Mirror into `README_CN.md`, then commit

**Search & verify a link**
1. Search arXiv (`https://arxiv.org/search/`), Google Scholar, or the company site/blog
2. Verify the link loads correctly
3. Extract title, date, URL, type, then add per the operations above

**Batch update** — collect new entries grouped by company, append per company, single descriptive commit.

**Fix a broken link** — find the correct URL (arXiv, official site, Web Archive), replace the URL in the Link column, commit.

### Commit message convention
- Add report(s): `add: MODEL_NAME from COMPANY`
- Add company: `add: COMPANY section with N reports`
- Fix link: `fix: update link for MODEL_NAME`
- Batch update: `update: add N reports (COMPANY1, COMPANY2, …)`
- Other: `chore: description`

### Guardrails
- ❌ Never download or store PDF files
- ❌ Never read/parse PDF content for summaries
- ✅ Always read before edit — never blindly overwrite
- ✅ Always check for duplicates before adding
- ✅ Keep entries sorted chronologically (oldest → newest) within each company
- ✅ Keep `README.md` and `README_CN.md` in sync
- ✅ Verify link accessibility when possible

---

## B. Logo generation

Generates the timeline `logo.png` (repo root): all model names stacked above/below a time axis with automatic overlap avoidance.

```
.claude/skills/logo-generation/
└── scripts/
    ├── generate.py   # entry point: config + invoke
    ├── models.py     # data: all (year, name, company) entries
    └── draw.py       # drawing: timeline + anti-overlap algorithm
```

**Dependencies:** `pip install matplotlib numpy`

**Run (from repo root):**
```bash
python .claude/skills/logo-generation/scripts/generate.py
```
Output: `logo.png` (~400 KB, 20×8 in, 300 DPI).

**Add a model** — edit `scripts/models.py`, add to `MODELS`:
```python
(2025.50, "ModelName", "CompanyKey"),
```
- year = `YYYY + MM/12` (2025-06 → `2025.50`)
- name = keep short (`DS-R1`, not `DeepSeek-R1`)
- company = must exist in the `COLORS` dict in `generate.py`

No manual sorting needed — the script sorts by time.

**Add a company** — add `"NewCo": "#hex"` to `COLORS` in `generate.py`; add the name to the `legend` list in `draw.py` if it should appear in the legend.

**Adjust landmarks** — edit the `LANDMARKS` set in `generate.py` (landmark font 7.5 pt, normal 5.8 pt).

**Notes:** keep names short; 2023–2025 is densest (nudge the year decimal to de-cluster); past ~150 models, raise `FIG_H` or lower `y_step`; avoid very dark colors; re-run and eyeball after any data change.
