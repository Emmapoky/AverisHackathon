# 🚢 SDOC Hackathon: Start Here

> **One-line goal:** Read a shipping inbox, sort every email into the right bucket, and for "check these docs" emails compare the Shipping Instruction (SI) against the draft Bill of Lading (BL). Flag exactly which fields differ, and hand anything we can't decide to a human.

> 🚨 **Preliminary deadline: Mon 22 Sep, 12:00 PM (Google Form).** Required: working prototype · 5-min demo video · public GitHub repo · live demo link · slides. **AI and cloud must both be meaningfully used.** Full details in [HACKATHON-RULES.md](HACKATHON-RULES.md).

---

## 1. The problem in plain English

A shipping ops team gets one inbox with everything mixed together: doc-check requests, requests for new SIs, invoice questions, general updates and spam.

When someone asks for a **doc check**, staff compare two documents by hand:

- **SI (Shipping Instruction):** what the customer *wants*. **This is the source of truth.**
- **BL (draft Bill of Lading):** what the carrier *drafted*. Errors here have to be caught before it's finalised.

Why it hurts today:
1. **Emails get missed.** A doc request buried in the inbox never gets checked.
2. **Manual comparison is slow and error-prone.** Checking names, ports, counts and weights over and over leads to mistakes.
3. **Same info, different labels.** `Port of Loading` vs `Load Port`, `Consignee` vs `To the Order of`, `Gross Weight (KG)` vs `Gross Wt (kgs)`.

---

## 2. What our system must do

| #   | Capability       | What it means                                                                              |
| --- | ---------------- | ------------------------------------------------------------------------------------------ |
| 1   | **Classify**     | Put every email into one of 5 categories (below)                                           |
| 2   | **Extract**      | For doc-check emails, pull the 7 fields from the SI and the BL                             |
| 3   | **Compare**      | Show mismatched fields side by side (e.g. `SI: 3 / BL: 4`)                                 |
| 4   | **Ask for help** | If we can't decide, escalate to a human with the reason and evidence. Never guess silently |

### The 5 categories
`BL_COMPARISON` · `SI_REQUEST` · `INVOICE_QUERY` · `GENERAL` · `SPAM`

### The 7 fields to compare
`shipper` · `consignee` · `notify_party` · `port_of_loading` · `port_of_discharge` · `container_count` · `gross_weight_kg`

### The 3 possible outcomes for a doc-check email
| status         | meaning                                                                                                    |
| -------------- | ---------------------------------------------------------------------------------------------------------- |
| `OK`           | All 7 fields match. Report "No mismatch detected."                                                         |
| `MISMATCH`     | 1 or more fields differ. List exactly which ones                                                           |
| `NEEDS_REVIEW` | We *can't* decide. Give a reason: `wrong_doc_type` · `missing_attachment` · `unreadable` · `missing_value` |

> ⚠️ A blank field or an unreadable scan is **not** a mismatch. It's `NEEDS_REVIEW`.

---

## 3. How the self-scorer grades accuracy

> ℹ️ This is the **Docker self-evaluation**, not the judging rubric. Judges score out of 100 (70 technical, 30 product/impact): see [HACKATHON-RULES.md](HACKATHON-RULES.md). Accuracy isn't a main criterion in the prelims, but it's our best evidence for "technical feasibility & validation" (15 pts), and the finals will run tests.

```
final_score = 50% end-to-end + 30% classification (macro-F1) + 20% defect detection (F1)
```

- **End-to-end (50%, the big one):** for each email with a real defect, did we (a) classify it as `BL_COMPARISON` **and** (b) flag the **exact** set of wrong fields? Getting one field too many or too few scores zero for that email.
- **Classification macro-F1 (30%):** all 5 categories count *equally*, so the small ones (Spam, General) matter as much as the big ones.
- **Defect F1 (20%):** did we correctly say defect / no defect? False alarms hurt here.
- **Reliability (separate diagnostic):** did we escalate the 20 "can't decide" cases? This isn't in the final number, but the brief says it's where you **stand out**.
- Optional hidden field: the scorer tracks `decided_by` (e.g. `"rule"` vs `"llm"`) if we include it, which is a nice transparency point for judges.

**Implication:** accuracy on the field-level comparison is worth the most. False alarms ("crying wolf") are penalised.

---

## 4. The data at a glance

| Fact                          | Number                                                                                              |
| ----------------------------- | --------------------------------------------------------------------------------------------------- |
| Emails                        | **520** (500 main + 20 hard edge cases, `email_501` to `email_520`)                                 |
| Expected mix (main set)       | ~200 BL_COMPARISON · 125 SI_REQUEST · 75 INVOICE_QUERY · 60 GENERAL · 40 SPAM                       |
| Emails with 0 attachments     | 394 (includes "please send the draft BL" doc requests, which are still BL_COMPARISON)               |
| Emails with an SI+BL pair     | 124                                                                                                 |
| Emails with only 1 attachment | 2                                                                                                   |
| Attachment formats            | 94 txt+txt · 13 pdf+pdf · 8 xlsx+docx · 7 xlsx+xlsx · 2 txt+pdf                                     |
| Defect rate                   | ~50% of pairs have 1–2 planted mismatches (±1 container, ±500–2000 kg, a different real port, etc.) |

**Traps to watch for:**
- Coded subject lines like `AIE - POD - CARRIER(BL#) - OC - INV - CUSTOMER - TERM`
- Forwarded threads, signatures and "external sender" banners in the body
- `SI_REQUEST` emails can contain SI-looking text in the body (see `email_110`) but have **no attachments**
- Edge cases: the "BL" is actually an invoice or packing list, scans with no text layer, 0-byte files, broken PDFs, and SI fields left as `???`, `____`, or `TBA`

---

## 5. Folder map

```
AverisHackathon/                ← git repo (github.com/Emmapoky/AverisHackathon)
├── README.md                   ← project README (team, setup; judges read this)
├── docs/
│   ├── START-HERE.md           ← you are here
│   ├── HACKATHON-RULES.md      ← deadlines, submission checklist, rubric, Q&A
│   ├── BRAINSTORM-QUESTIONS.md ← work through this as a team
│   ├── IDEA-CANVAS.md          ← fill in once we pick a direction
│   └── brief/                  ← use-case PDF + opening-ceremony transcript
├── data/                       ← ✅ PARTICIPANT DATA: build against this
│   ├── inbox/                  520 email JSONs
│   ├── attachments/            SI/BL files (txt/pdf/docx/xlsx)
│   ├── loader.py               helper: Inbox("data")
│   ├── sample_submission.json  required output shape
│   └── README.md
├── src/                        ← our code
├── tests/
└── _local/scoring-server/      ← 🔒 NOT in git: Docker self-scorer (contains the answer key)
```

### 🔒 About `_local/scoring-server`
This is technically the organizer kit: it includes `data_v2/ground_truth.json` and the generator scripts that show how defects are planted. At the opening ceremony the organizers confirmed that teams **can run the accuracy test through Docker**, so using the `/submit` scorer is fine.

It's **git-ignored** so the answer key never lands on GitHub. Teammates can get it from the organizers' Google Drive zip (`sdoc-hackathon-docker.zip`) and unzip it into `_local/scoring-server/`.

**Team rule:** use the scorer to *measure* accuracy, but **don't hand-tune against `ground_truth.json` or the generator code**. The finals will test on emails we haven't seen, so overfitting to these 520 will backfire.

---

## 6. Quick start

```bash
cd ~/AverisHackathon/data
python3 loader.py .                       # smoke test: "520 emails from ."
cat inbox/email_001.json                  # a doc-check request
cat attachments/email_001_SI.txt attachments/email_001_BL.txt
```

Run the self-scoring server (needs Docker Desktop running):
```bash
cd ~/AverisHackathon/_local/scoring-server && docker compose up --build
```
Then, in Python:
```python
from loader import Inbox
inbox = Inbox("http://localhost:8080")
print(inbox.submit(submission)["final_score"])
```

Python libraries we'll likely need for the binary attachments: `pip3 install pdfplumber python-docx openpyxl` (plus an OCR engine or vision LLM for the scanned edge cases).

---

## 7. Two stages of ambition

| Basic (everyone does this) | Advanced (where we stand out) |
|---|---|
| Classify emails | PDF + Word + Excel attachments with tables |
| Extract from plain text | Scanned / image-only PDFs (OCR or vision LLM) |
| Compare 7 fields | Messy labels, misleading subjects, missing attachments |
| Report mismatches | **Human-in-the-loop review UI**: person confirms or corrects, report updates, visible failures and retries |

➡️ **Next step:** open [BRAINSTORM-QUESTIONS.md](BRAINSTORM-QUESTIONS.md).
