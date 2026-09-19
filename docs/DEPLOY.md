# 🚀 Deploying for free (no credit card)

Total cost: **RM 0**. Every service below has a free tier that doesn't ask for a card.

| Piece | Free service | What it does |
|---|---|---|
| Web app (API + dashboard) | **Hugging Face Spaces** (Docker) | Public link for judges. Free CPU, stays up |
| AI | **Google Gemini API** free tier (AI Studio key) | Unclear emails, unknown labels, scanned PDFs |
| Database | **Supabase** free project | Saves human reviews + uploaded emails in the cloud |
| Code | GitHub | Repo judges read |

> The app also works with **no AI key and no database**: it falls back to rules only and saves reviews to a local file. So a missing key never breaks the demo.

---

## 1. Get a free Gemini key (5 min)
1. Go to <https://aistudio.google.com/apikey>, sign in with a Google account, **Create API key**.
2. Check which models are free today in AI Studio. Put the model name in `GEMINI_MODEL` (default `gemini-2.5-flash`).
3. Locally: `cp .env.example .env` and paste the key into `GEMINI_API_KEY`.

**Alternative (also free):** Groq (<https://console.groq.com>) with `LLM_PROVIDER=openai_compat`, `LLM_BASE_URL=https://api.groq.com/openai/v1`. Groq can't read scanned PDFs; Gemini can.

## 2. Create the free Supabase database (5 min)
1. <https://supabase.com> → New project (free).
2. SQL editor → paste and run [`supabase.sql`](supabase.sql).
3. Project Settings → API: copy the **Project URL** → `SUPABASE_URL` and the **service_role** key → `SUPABASE_KEY`.
   The key is only used on the server, never sent to the browser.

## 3. Pre-compute results (so the demo is instant and uses no AI quota)
```bash
python3 scripts/run_batch.py          # uses AI only where rules aren't sure
python3 scripts/score.py              # optional: saves accuracy numbers for the dashboard
```
Commit the updated `data/results.json`.

## 4. Deploy to Hugging Face Spaces (10 min)
1. <https://huggingface.co/new-space> → SDK: **Docker** → Blank → Public.
2. Space → Settings → **Variables and secrets**: add `GEMINI_API_KEY`, `LLM_PROVIDER=gemini`, `SUPABASE_URL`, `SUPABASE_KEY` as **secrets**.
3. Push this repo to the Space. The Space's `README.md` must start with:
   ```yaml
   ---
   title: ShipCheck
   emoji: 🚢
   colorFrom: blue
   colorTo: green
   sdk: docker
   app_port: 7860
   ---
   ```
   Easiest: keep GitHub as the main repo and push to the Space as a second remote:
   ```bash
   git remote add space https://huggingface.co/spaces/<user>/<space-name>
   git push space main
   ```
   (Add the YAML block above to the top of README.md first, or on a separate `hf` branch you push with `git push space hf:main`.)
4. The link is `https://<user>-<space-name>.hf.space`. **Open it in an incognito window** to check it works for judges.

**Backup host:** Render (<https://render.com>) → New Web Service → from GitHub → Docker. Free, but it sleeps after 15 min idle (~50 s to wake). Hugging Face is the better option for judging.

## 5. Before submitting
- [ ] Live link loads in incognito, and "Try your own email" works
- [ ] `/health` returns `{"ok": true, "emails": 520}`
- [ ] No keys in the repo (`git grep -n "AIza\|sk-\|service_role"` finds nothing)
