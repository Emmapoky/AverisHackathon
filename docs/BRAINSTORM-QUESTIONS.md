# 🧠 Brainstorm Questions

> Work through these as a team. Write answers right under each question.
> ⭐ = decide first · ✅ = answered at the opening ceremony (answer filled in) · 🆕 = new since the ceremony
> Context: [START-HERE.md](START-HERE.md) · Rules, rubric and deadlines: [HACKATHON-RULES.md](HACKATHON-RULES.md)
>
> 🚨 **Deadline: Mon 22 Sep, 12:00 PM.** Two workshop days (20th, 21st) are in between. Settle the ⭐ questions **tonight**.

---

## A. Framing & Goal

- [ ] ⭐ **What's our one-sentence pitch?** (e.g. "Zero missed doc checks, zero silent guesses.")
  - _Answer:_
- [ ] ⭐ **What's our angle for the 30 product/impact points?** Pick 1–2 standout ideas (see Parking Lot). We can't do everything in 2.5 days.
  - _Answer:_
- [ ] **Who is our user?** A doc-checker at APRIL handling **up to 2,000 emails a day**. What would make them trust the tool?
  - _Answer:_
- [x] ✅ **Solve the brief exactly, or build something more practical?**
  - _Answer:_ Either. "If you can propose a better solution, that will be great." Extending the data or the scope is welcome, as long as we still classify → understand intent → compare documents.
- [ ] **What's our "wow" moment in the 5-minute video?** Which 30 seconds will the judges remember?
  - _Answer:_

## B. Rules & Setup

- [x] ✅ **Can we use the Docker kit and scorer?**
  - _Answer:_ Yes. The organizers said to run the accuracy test through Docker. **Team rule:** measure with it, but don't tune on `ground_truth.json`.
- [x] ✅ **Are LLM APIs allowed? Any limits?**
  - _Answer:_ No limits. AI is actually **required** in the core functionality. Training our own model or calling external APIs are both fine; we just need to showcase whichever we choose.
- [x] ✅ **Is judging done on this same dataset?**
  - _Answer:_ Accuracy isn't a main criterion in the prelims. **The finals will run tests**, probably on unseen emails. So generalise and don't overfit.
- [x] ✅ **What do we submit?**
  - _Answer:_ Description, a ≤5-min video, a GitHub repo with README, a live public demo link, and slides/docs. See [HACKATHON-RULES.md](HACKATHON-RULES.md#-submission-checklist-google-form-closes-22-sep-1200-pm).
- [x] ✅ **How is it judged?**
  - _Answer:_ 70 technical (prototype 25 · architecture 15 · tech integration 15 · feasibility & validation 15) + 30 product (problem understanding 10 · innovation 10 · practical value 10).
- [ ] 🆕 **Ask on Discord:** the official event/company name for our slides, and whether "cloud" means the *app* has to run in the cloud or whether a cloud AI API counts.
  - _Answer:_

## C. Classification

- [ ] ⭐ **Rules, LLM, or hybrid?** Subject lines are heavily coded (`TO CONFIRM DOCS`, `REQUEST BL DRAFT`, `SI - ...`, `BILLING`). Idea: cheap rules first, LLM for ambiguous cases, and log `decided_by`. This counts as "AI meaningfully in the core" *and* is cheap and explainable.
  - _Answer:_
- [ ] **Which signal wins: subject, body, sender, or attachments?** What if they disagree (misleading subject)?
  - _Answer:_
- [ ] **How do we avoid being fooled by forwarded threads, signatures and "external sender" banners?**
  - _Answer:_
- [ ] **How do we tell BL_COMPARISON from SI_REQUEST when the body contains SI details** (`email_110`)?
  - _Answer:_
- [ ] 🆕 **Do we go beyond the 5 categories?** Sergio mentioned "draft BL" vs "BL confirmation" as separate intents. Sub-intents could be a nice extra, as long as we still output the 5 required categories.
  - _Answer:_
- [ ] **Doc-check request with no attachments ("please send the draft BL"):** do we report `OK`, or `NEEDS_REVIEW / missing_attachment`? Either way, the UI should show it as "waiting for BL".
  - _Answer:_

## D. Extraction

- [ ] ⭐ **One extractor for all formats, or convert everything to text first** and then run one field-mapper (LLM with a JSON schema)?
  - _Answer:_
- [ ] **How do we map label synonyms to the 7 fields?** A synonym table, an LLM, or both (table first, LLM fallback)?
  - _Answer:_
- [ ] **PDF tables, bilingual Word BLs, Excel SIs:** which libraries? (`pdfplumber`, `python-docx`, `openpyxl`)
  - _Answer:_
- [ ] **Scanned or image-only PDFs:** OCR, vision LLM, or detect and escalate?
  - _Answer:_
- [ ] 🆕 **Info in the email body, not just attachments.** Sergio said the fields can live in either. Do we extract from bodies too (e.g. SIs pasted into emails)?
  - _Answer:_
- [ ] **Multi-line fields** (consignee plus address): compare the name only, or name and address?
  - _Answer:_
- [ ] **How do we detect a wrong doc type** (invoice or packing list sent instead of a BL)?
  - _Answer:_

## E. Comparison

- [ ] ⭐ **What counts as "the same"?** Case, punctuation, `CO., LTD` vs `CO LTD`, `21,577 KG` vs `21577`, `1 x 40'HC` vs `1`, port name vs UN/LOCODE (`MYPKG`).
  - _Answer:_
- [ ] **Number normalisation:** container count from `15 x 20'GP` or `2x40HC + 1x20GP`; KG vs MT.
  - _Answer:_
- [ ] **Avoid over-flagging:** formatting noise must never become a MISMATCH. What's our false-alarm guard?
  - _Answer:_
- [ ] **Confidence score per field?** What threshold sends a field to review instead of MISMATCH?
  - _Answer:_
- [ ] **How do we display it?** Side-by-side `SI: 3 / BL: 4`, highlighted in the source doc?
  - _Answer:_

## F. Human-in-the-Loop & Reliability (central to the brief)

- [ ] ⭐ **When exactly do we escalate?** Unreadable, missing value (`???`, `____`, `TBA`), wrong doc type, missing attachment, low confidence, can't classify…
  - _Answer:_
- [ ] **What does the reviewer see?** Email, both docs, highlighted fields, our reason, and the evidence snippet.
  - _Answer:_
- [ ] **How does the reviewer confirm or correct,** and how does the report update?
  - _Answer:_
- [ ] **Processing failures:** show them visibly and allow retry. Don't crash the batch.
  - _Answer:_
- [ ] **Do corrections feed back** into rules or prompts (a learning loop)? Good for innovation points.
  - _Answer:_
- [ ] **How do we avoid escalating too much?**
  - _Answer:_

## G. Product, UI & Demo

- [x] ✅ **Does the UI matter? Chat or dashboard?**
  - _Answer:_ Any UI is fine. We **must justify the pros and cons** in the pitch.
- [ ] ⭐ **So which one?** Web dashboard (inbox → triage → review queue), chat assistant, Outlook-style mock, or a dashboard with a chat side-panel?
  - _Answer:_
- [x] ✅ **How do we show accuracy?**
  - _Answer:_ Run the Docker test, **or show it in the UI**. Idea: a live "accuracy" panel that scores the run against the self-scorer.
- [ ] **What does the report look like** per email and for the whole inbox?
  - _Answer:_
- [ ] **Business case numbers:** 2,000 emails/day × minutes saved; cost of a wrong BL (amendment fees, delays, demurrage).
  - _Answer:_
- [ ] **Real-world integration story:** Outlook / Microsoft Graph, shared mailbox, ticketing. This goes in the "future roadmap" slide.
  - _Answer:_

## H. 🆕 Cloud & Deployment (mandatory: lose marks without it)

- [ ] ⭐ **Where does it run?** Needs a **public link that stays up through judging**. Options: Render / Railway / Fly.io (Docker), Vercel + serverless API, Cloudflare Workers, Google Cloud Run, AWS free tier…
  - _Answer:_
- [ ] ⭐ **What makes our cloud use "meaningful"** rather than just hosting? Ideas: cloud LLM API, object storage for attachments (S3 / R2), a queue for processing emails, a cloud DB for review decisions, serverless workers that scale with inbox volume.
  - _Answer:_
- [ ] **How does the demo get its data?** Embed the 520 emails in the deployment, or docker-compose the organizers' server alongside ours. (Both approved.)
  - _Answer:_
- [ ] **Free-tier gotchas:** cold starts or sleeping instances during judging, LLM rate limits, API keys kept out of the public repo.
  - _Answer:_
- [ ] **Cost of processing 520 emails with the LLM:** can we pre-compute and cache results so the live demo is instant?
  - _Answer:_

## I. Tech & Team

- [x] ✅ **Any stack restrictions?**
  - _Answer:_ None. But they'll judge scalability, maintainability and extensibility.
- [ ] ⭐ **Our stack:** Python backend (FastAPI?) + UI (Streamlit for speed, or Next.js / React for polish)?
  - _Answer:_
- [ ] ⭐ **Which LLM?** Cost, latency, JSON-mode reliability, vision for scans.
  - _Answer:_
- [ ] ⭐ **Who owns what?** Classifier · Extractors · Comparator · Review UI · Cloud/deploy · Video + slides
  - _Answer:_

    | Member | Owns | Backup for |
    |---|---|---|
    | Erwyna | | |
    | Nandhini | | |
    | Charvhi | | |
    | Riely | | |
    | Taabish | | |
- [ ] **How do we test fast?** A scoring loop after every change, plus a small hand-checked set of tricky emails.
  - _Answer:_
- [ ] **What do we cut if time runs out?**
  - _Answer:_

## J. Stretch Ideas (only if the core is solid)

- [ ] 🆕 **Multilingual:** Malay, Indonesian or Mandarin emails. The organizers flagged this as realistic. A few translated test emails would make a quick, impressive demo.
  - _Answer:_
- [ ] **Agentic / agent-to-agent design** (explicitly welcomed): e.g. a Triage agent → Extraction agent → Verifier agent → Escalation agent.
  - _Answer:_
- [ ] **Auto-drafted reply** to the carrier listing the BL corrections needed.
  - _Answer:_
- [ ] **HS code** check (asked at the ceremony, unanswered; ask on Discord first).
  - _Answer:_

## K. Risks & Unknowns

- [ ] Finals test data may be different (real `.msg` emails, new label variants). How robust are we?
  - _Answer:_
- [ ] LLM API down or slow during judging: is there a cached or offline fallback?
  - _Answer:_
- [ ] Final pitch (26 Sep) needs **every member there in person** (Erwyna, Nandhini, Charvhi, Riely, Taabish). Can everyone make it?
  - _Answer:_
- [ ] Assumptions to write down ("if your decision is reasonable, record the reason").
  - _Answer:_

---

## 🗓️ Suggested 2.5-Day Plan

| When | Goal |
|---|---|
| **Fri 19 Sep (tonight)** | Answer the ⭐ questions · split roles · repo created · baseline script on .txt pairs + first self-score |
| **Sat 20 Sep** (+ Workshop 1) | pdf/docx/xlsx extraction · LLM hybrid classifier · escalation rules · **deploy a skeleton to the cloud early** |
| **Sun 21 Sep** (+ Workshop 2) | Review UI / HITL flow · accuracy panel · polish · README · slides · **record the video Sunday night** |
| **Mon 22 Sep, by 10 AM** | Final checks: live link works in incognito, video is unlisted/public, repo is public → **submit before 12:00** |

## 🗳️ Decisions Log

| # | Decision | Why | Who / When |
|---|---|---|---|
| 1 | Use the Docker scorer to measure, never tune on the ground truth | Finals test unseen data | Team, 19 Sep |
| 2 | | | |
| 3 | | | |

## 💡 Idea Parking Lot
_Drop half-formed ideas here. Sort them later._

- "Inbox Zero for shipping docs": a triage dashboard with a review queue
- Confidence-scored field comparison with source-evidence highlights
- Reviewer corrections become new synonym rules (a learning loop)
-
