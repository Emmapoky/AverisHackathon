# 📋 Hackathon Rules, Deadlines & Judging

> Pulled from the opening ceremony on 18 Sep 2026 ([full transcript](brief/Opening-Ceremony-Transcript-2026-09-18.md)). The captions garble the names ("Aberest / Everest / Aries / Everis"), so **check the official name in the rules doc or Discord before it goes on our slides.**
> 💬 **Discord is the main channel** for announcements and questions. Join it if you haven't.

---

## ⏰ Timeline

| Date                              | What                                              | Notes                                                                                   |
| --------------------------------- | ------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Thu 18 Sep                        | Opening ceremony (virtual)                        | ✅ done                                                                                  |
| **Sat 20 Sep**                    | Workshop 1 (Shik & Darren)                        | Block time for it                                                                       |
| **Sun 21 Sep**                    | Workshop 2 (host-company speakers)                | Block time for it                                                                       |
| **🚨 Mon 22 Sep, 12:00 PM sharp** | **Preliminary submission deadline** (Google Form) | Aim to submit by Sunday night                                                           |
| Wed 24 Sep                        | Top 10 finalists announced                        | Each finalist gets a dedicated mentor                                                   |
| Fri 26 Sep                        | **Final pitch day, in person**                    | 10 min pitch + demo, 5 min Q&A, awards right after. **Every team member must be there** |

Final venue (as captioned): *"Mes University Malaysia Panda Sunre in Sububanga"*. Probably Monash University Malaysia, Bandar Sunway, Subang Jaya. Confirm on Discord.

🏆 **Prizes:** 1st RM 5,000 · 2nd RM 3,000 · 3rd RM 1,000

---

## 🚦 Hard requirements (lose marks without these)

1. **AI must be *meaningfully* part of the core functionality** (not a bolt-on).
2. **Cloud infrastructure must be *meaningfully* used.** The organizers said leaving this out *"may significantly reduce your score"*. Free tiers are fine (Vercel, Cloudflare, free AWS/GCP/Azure tiers, etc.). Docker / docker compose is fine for scaffolding.
3. **A working prototype** is required for the preliminary round.
4. **No tech-stack restrictions**, but they want thought given to **scalability, maintainability and extensibility** (could this keep going after the hackathon?).

---

## 📦 Submission checklist (Google Form, closes 22 Sep 12:00 PM)

- [ ] **Project description:** name, purpose, and the problem statement we're solving
- [ ] **Demo video, 5 min max:** YouTube *unlisted or public* (not private) or Google Drive set to *"anyone with the link can view"*
  - Must cover: team intro · project · problem · tech stack · **live working prototype** · impact
  - ⚠️ **-1 mark for every 30 seconds over.** Rehearse, and aim for 4:30.
- [ ] **GitHub repo link** with a clear **README and setup instructions** (the dataset is synthetic and **can be public**)
- [ ] **Live prototype / demo link:** public, and **working for the whole judging period** (so no laptop-hosted demos, and watch out for free-tier sleep or cold starts)
- [ ] **Slide deck or docs link** (no page limit) covering: technical architecture · implementation details · challenges faced · future roadmap

---

## 🧮 Judging rubric (100 points)

### Technical: 70
| Criterion | Pts | What it means for us |
|---|---|---|
| **Working core prototype** | **25** | Classify → extract → compare → escalate, working live on the hosted link |
| System design & architecture | 15 | A clean pipeline diagram; explain each choice |
| Technology integration | 15 | AI and cloud woven in meaningfully, not just ticked off |
| Technical feasibility & validation | 15 | **Show accuracy numbers** (the Docker self-scorer counts), plus tests and edge cases |

### Product & Impact: 30
| Criterion | Pts | What it means for us |
|---|---|---|
| Understanding of the problem | 10 | 2,000 emails/day, mislabelled fields, BL amendment cost |
| Innovativeness | 10 | What we do that others won't (HITL loop? multilingual? confidence scores?) |
| Practical value & potential | 10 | Could the ops team actually use this tomorrow? |

> 💡 The self-scoring leaderboard is **not** the preliminary judging criterion. Accuracy *is* evidence for "validation", and the organizers said the **final** round will "run some kind of test", probably on emails we haven't seen. So build something that generalises; don't overfit to the 520.

---

## 🗣️ Q&A answers from the ceremony

| Question | Answer |
|---|---|
| Any limit on AI use? | **None.** Use it to brainstorm, build, and as part of the product. |
| Is there a set workflow to follow? | No. Design our own, including **agentic / agent-to-agent** approaches. |
| Can we change or extend the data? | **Yes**, they'd appreciate it, as long as it still does classify → understand intent → compare documents. |
| Budget for cloud or AI? | Don't worry about budget; use free options. |
| API key for Docker? | There isn't one. Docker just serves the data over an API; reading files directly is fine too. |
| Fixed output format or scoring? | Accuracy **isn't a main criterion in the prelims**; the **finals will run tests**. |
| Tested on unseen emails? | Implied for the finals. |
| Languages? | The sample is English, but real mail could be **Malay, Indonesian or Mandarin**. Handling these is a bonus. |
| How do we show accuracy? | Run the **Docker accuracy test against the generated ground truth**, or show accuracy in the UI. Our choice. |
| Is a UI important? | Any UI is fine (chat, web dashboard…). **Justify the pros and cons** in the pitch. |
| How do judges get to the data in a live demo? | Docker compose it in, or embed the data directly. |
| Solve the brief exactly, or build something more practical? | Either. "If you can propose a better solution, that will be great." |
| Train our own ML or call APIs? | Either. **Showcase whichever you pick** in the prototype and slides. |
| Can the dataset go in a public repo? | **Yes**, it's synthetic. |
| Is there an HS code field involved? | Unanswered. Ask on Discord. (HS code = customs tariff code. It's in the SIs, but it's **not** one of the 7 compared fields.) |

### Extra problem context from Sergio (the host company's engineer)
- The real team gets **up to 2,000 emails a day**. This is our impact number.
- The information to extract may be **in the email body *or* in attachments**.
- Intent types he mentioned: invoice question, spam, SI-related, **draft BL**, **BL confirmation**.
- Different terms appear because **the BL is prepared by the shipping line**, not the shipper.
- When the system can't classify, extract or compare, it should **ask the shipping docs team for clarification**. Human-in-the-loop is central to the brief.
