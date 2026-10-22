# Contract — hours, session plans and increasing difficulty

| Field | Value |
|---|---|
| ID | `hours-and-progression` |
| Scope | Every science module (`courses/*/index.qmd` minus `specs/non-science-pages.md`) + home page programme table |
| Source of hours | SynapseS 2026–2027 sheet quoted in each module's own fiche; when a sheet publishes no volume, the plan says “assumed” and why |
| Gate | `python3 tools/check_progression.py` (also run by `tools/check_gates.py`) |

## Why

1. Students asked for notes whose **amount matches the official volume** (36 h for an M1 course, 12 h for a refresher, ~24 h for an M2 course). Measured before this contract: refreshers carried 730–940 prose words per contact hour, regular M1 courses 85–200, two P2 courses fewer than 100 — the 12 h refreshers held about five times more than a 12 h course can cover.
2. Chapters must go **from easy to hard**: a reader following the page in order never meets a harder chapter before an easier one it does not depend on, and the exercises are graded.
3. The SynapseS sheets do not publish a session-by-session programme, so the mapping of chapters onto hours is ours and is labelled as a proposal.

## Rules

### R1 — Session plan (`### Session plan {#sessions}`)

Placed in the introduction, after *Course outline* and before *How to study this module*. It opens with one bold line

```
**36 h in class = 12 sessions of 3 h.**
```

(or `**24 h in class (assumed) = 8 sessions of 3 h.**` when the sheet is silent; the off-curriculum NN refresher uses `h of guided self-study`), followed by one sentence naming the source of the volume and saying that the session split is a proposal. Then a pipe table:

| Session | Hours | Level | Content | Practice |
|---|---|---|---|---|
| 1 | 3 h | 1 | ch. 0 Review …; ch. 1.1–1.2 … | Ex. 1–2 |

- **Hours** sum exactly to the bold total.
- **Level** is `1` (foundations: reviews, definitions, first worked examples), `2` (core: the main theorems and algorithms of the course) or `3` (advanced: proof-heavy material, recent research, open problems). It **never decreases** from one row to the next.
- **Content** cites chapters as `ch. N` (sections allowed: `ch. 2.1–2.3`). The first chapter cited in each row never goes back: sessions follow the page order.
- After the table, one line `**Self-study, outside the N h** (about K h in total): ch. 8 … (≈ 2 h) · …` lists every chapter not taught in class, each with a time estimate. Research-of-the-instructor chapters and “going further” chapters go here unless the course is a research seminar.
- Every numbered chapter appears in the table or in the self-study line.

### R2 — Volume calibration

Prose words (code and math stripped) of the chapters cited in the table, divided by the in-class hours, lie in **[100, 320] words per hour**. Above the band, move whole chapters (or the end of a chapter, as its own subsection pointer) to self-study; below the band, the module is too thin for its hours and must gain worked examples or explanations.

### R3 — Chapter order = difficulty order

Chapters are numbered in page order (`## N. Title {#chN}`, consecutive). A chapter that is clearly easier than one before it, and does not depend on it, moves up; research notes move to the end. Renumbering updates every reference: contents list, headings and ids, `Definition N.k` labels, `ch. N` / `section N.k` / `theorem N.k` mentions, the official-correspondence table, the outline, exercises and links from other modules (`grep -rn "<module>/index.html#ch"`).

### R4 — Graded exercises

Each exercise title starts with its level: `1.  **★ Closed-form ridge.**` (★ apply the course, ★★ combine or prove a short result, ★★★ open-ended or research-flavoured). Exercises are sorted by non-decreasing level; references to exercise numbers are updated.

### R5 — Readability fixes found on the way

- Each chapter opens with one or two plain sentences saying what problem it solves before the first definition.
- Symbols are defined before they are used; a forward reference never carries a needed definition.
- Conversion artefacts are fixed: `\|x\|` used for an absolute value becomes `|x|` (keep `\|` for norms), stray `\\)` or doubled backslashes inside math are removed.

## Proof

- `python3 tools/check_progression.py` exits 0.
- `python3 tools/check_gates.py` exits 0.
- Pages re-rendered with `python3 tools/render.py <module>` (Quarto 1.7.32).
