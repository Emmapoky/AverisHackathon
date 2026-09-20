# Erwyna — live demo script

Every click, in order, with the exact words. **[ACTION]** is what you do,
**"SAY"** is what you say while doing it.

Measured, not estimated — these are real word counts at presenting pace plus
click time:

| Version | Use it for | Length |
|---|---|---|
| **Video cut** (below) | the 5-minute video, slide 10 | **20 sec** |
| **Short run** — the ⏩ sections | a quick walkthrough if asked | 90 sec |
| **Full run** — every section | the Friday pitch, where you have time | **3 min 50** |

The full run is too long for the video. Don't try to squeeze it in — use the
video cut for the recording, and keep the full run for Friday.

---

## VIDEO CUT — 20 seconds, use this one for the recording

**[ACTION]** Inbox on screen. Type `26067` in the search box, click the result.

> "Five hundred and twenty emails, already sorted. Here's one it caught — the
> Shipping Instruction says EAST BRIGHT FZ-LLC, the draft Bill of Lading says
> UAB NOVAKOPA. Different company."

**[ACTION]** Click the **Consignee** row so the evidence line opens.

> "And it shows the exact line it came from. Forty-six out of forty-six caught,
> zero false alarms."

**[ACTION]** Click **Needs a person** in the sidebar, hold for one second.

> "And when it isn't sure, it asks."

---

**Before you start**
- Open `http://localhost:8000` in a clean window. Browser at 100% zoom, no
  bookmarks bar, no other tabs.
- Have the **Inbox** tab selected and the page scrolled to the top.
- Check the sidebar bottom-left says `AI · deepseek-flash`. If it says
  *Rules only*, your keys aren't loaded — the demo still works, but skip the
  sentence about the second opinion.
- **Do not click "Yes, this is right" if you are demoing the Vercel link** —
  without Supabase connected it returns an error. On localhost it is fine.

---

## 1 · The inbox ⏩

**[ACTION]** Just sit on the Inbox screen for a beat. Don't click yet.

> "This is the shared inbox — five hundred and twenty real emails, already
> sorted. Every one has a label: check BL, new SI, invoice, general, spam. That
> sorting happened in about a second."

**[ACTION]** Point at the five cards along the top.

> "Five hundred and twenty sorted. A hundred and nine BL checks done.
> Forty-six mistakes caught. Twenty waiting for a person. About forty-four hours
> of staff time saved."

---

## 2 · A caught mistake ⏩

**[ACTION]** In the search box, type `26067`. One email appears. Click it —
*REQUEST BL DRAFT _ PO 26067_ COATED IVORY BOARD*.

> "Here's one it caught."

**[ACTION]** Point at the red banner.

> "Two fields don't match: consignee and notify party."

**[ACTION]** Point at the two red rows in the comparison table.

> "The Shipping Instruction says EAST BRIGHT FZ-LLC. The draft Bill of Lading
> says UAB NOVAKOPA. That's a completely different company — that BL would have
> shipped to the wrong consignee."

---

## 3 · Show the evidence ⏩

**[ACTION]** Click directly on the **Consignee** row. A grey evidence row opens
underneath it.

> "And it shows its working. That's the exact line, quoted from each document.
> Nobody has to take the system's word for it — you can check it in two seconds."

*(⏩ For the video, stop here and go to section 8.)*

---

## 4 · Where the AI helped

**[ACTION]** Scroll down to the **Where the AI helped** panel.

> "The rules found this mismatch, not the AI. But because we're about to tell a
> customer their document is wrong, the AI reads both documents again,
> independently, as a second reviewer."

**[ACTION]** Point at the green line and read the AI's sentence.

> "It agrees — and it says why, in plain English. It agreed with the rules
> forty-six times out of forty-six. If it ever disagrees, that's a flag for a
> human, not an automatic override. The decision always stays with the code."

---

## 5 · The step-by-step trace

**[ACTION]** Scroll to **What the system did**.

> "Every email keeps a trace: how it was sorted, how each document was read,
> what was compared, and how long each step took. If anyone asks why an email
> was handled a certain way, the answer is right here."

---

## 6 · The AI doing what rules can't

**[ACTION]** Scroll back up. Click the **✦ AI stepped in** chip in the filters.

> "These are the forty-nine emails where the AI did something the rules
> couldn't."

**[ACTION]** Type `25041` in the search box and click the result
(*PAPERONE DIGITAL COPIER PAPER*).

**[ACTION]** Scroll to **Attachments** and point at the **read by AI** tag.

> "Both attachments here are scanned images. There is no text in them at all —
> no rule and no text model can read these. Gemini reads them visually. And
> notice it still went to a person to confirm, because a scan is exactly where
> you don't want a machine to have the last word."

**[ACTION]** Click the **✦ AI stepped in** chip again to turn the filter off.

---

## 7 · When it isn't sure

**[ACTION]** Click **Needs a person** in the left sidebar.

> "Twenty emails are waiting for a human — five with the wrong document
> attached, five missing a file, five unreadable scans, and five with a blank
> field. Each one says why it stopped, and what it needs."

**[ACTION]** Click any row in the queue.

> "A reviewer confirms or corrects it, and that decision is saved. The system
> never guesses on these — that's the whole point."

---

## 8 · Close ⏩

**[ACTION]** Click **Inbox** to return to the full list.

> "Five hundred and twenty emails, a hundred percent sorted correctly,
> forty-six out of forty-six mistakes caught, zero false alarms. That's
> ShipCheck."

---

## If something goes wrong

- **Page won't load** → the server stopped. `bash scripts/start.sh` in a
  terminal, then reload.
- **Sidebar says "Rules only"** → keys aren't loaded. Everything still works;
  just skip section 4.
- **A button errors on the Vercel link** → you're on the hosted version without
  Supabase. Switch to `localhost:8000` and carry on.
- **Asked "what if the AI is wrong?"** → "It can't be, on the decision. The
  comparison is deterministic code. The AI only sorts unclear emails, reads
  scans, and gives a second opinion we show but never act on automatically."
- **Asked "does this only work on your test data?"** → "We wrote a hundred
  tests using emails and documents that appear nowhere in the sample set —
  Malay, Chinese, Spanish, Vietnamese, European number formats, pounds versus
  tonnes. Four real bugs came out of that, and we fixed all four."
