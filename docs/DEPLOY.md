# 🚀 Deploying (free hosting + our DeepSeek key)

Hosting and database are **free, no card**. The only paid piece is the DeepSeek API the team already topped up ($1.99 covers thousands of calls; 12 test requests cost < $0.01).

| Piece | Free service | What it does |
|---|---|---|
| Web app (API + dashboard) | **Hugging Face Spaces** (Docker) | Public link for judges. Free CPU, stays up |
| AI | **DeepSeek API** (`deepseek-chat`, team account) | Unclear emails, unknown labels. Scanned PDFs go to a person |
| Database | **Supabase** free project | Saves human reviews + uploaded emails in the cloud |
| Code | GitHub | Repo judges read |

> The app also works with **no AI key and no database**: it falls back to rules only and saves reviews to a local file. So a missing key never breaks the demo.

---

## 1. DeepSeek API key (2 min)
1. Nandhini (account owner): <https://platform.deepseek.com/api_keys> → **Create new API key** → name it e.g. `shipcheck-demo`.
2. Share it privately with whoever deploys (not in the repo, Discord or WhatsApp group). Locally: `cp .env.example .env` and paste it into `DEEPSEEK_API_KEY`.
3. In DeepSeek → Usage → **turn on the balance alert** (it's currently disabled) so the key doesn't run dry during judging. If it does run out, the app falls back to rules only instead of breaking.
4. Test it: `python3 scripts/run_batch.py --only email_001` → the first line should say `AI: deepseek-chat (deepseek)`.

**Scanned PDFs (optional, free):** DeepSeek can't read scans. Get a free Gemini key at <https://aistudio.google.com/apikey> (no card) and add `GEMINI_API_KEY=...` to `.env`. Gemini then reads scans only; DeepSeek does everything else. The deploy script uploads it as a secret too.

**If the DeepSeek balance runs out:** remove `DEEPSEEK_API_KEY` and Gemini takes over everything (set `LLM_MIN_INTERVAL=4` for its rate limit).

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

## 4. Deploy to Hugging Face Spaces (10 min, one command)
1. Make a free account at <https://huggingface.co/join>.
2. Create a token: <https://huggingface.co/settings/tokens> → **Create new token** → type **Write** → copy it (`hf_...`).
3. Put both keys in your local `.env` (never commit it):
   ```
   DEEPSEEK_API_KEY=sk-...
   HF_TOKEN=hf_...
   ```
4. Deploy:
   ```bash
   python3 scripts/deploy_hf.py --dry-run     # check the file list first
   python3 scripts/deploy_hf.py               # creates <you>/shipcheck and uploads
   ```
   It creates the Space, saves the DeepSeek key as a **Space secret** (read from `.env`, not typed anywhere else), uploads the app and dataset, and adds the Space header to the Space's README only. Plain `git push` to a Space fails on the PDF/Word/Excel files unless you set up git-lfs; this script avoids that.
5. Wait 3–5 min for the build (watch the **Logs** tab on the Space page). Your link: `https://<user>-shipcheck.hf.space`.
6. **Open it in an incognito window** to check it works for judges.
7. After code changes, run `python3 scripts/deploy_hf.py` again to update.

**Adding or changing the key by hand instead:** Space page → **Settings** → **Variables and secrets** → **New secret** → name `DEEPSEEK_API_KEY`, value `sk-...` → Save. Add a **New variable** `LLM_PROVIDER` = `deepseek`. The Space restarts by itself.

**Backup host:** Render (<https://render.com>) → New Web Service → from GitHub → Docker. Free, but it sleeps after 15 min idle (~50 s to wake). Hugging Face is the better option for judging.

## 5. Before submitting
- [ ] Live link loads in incognito, and "Try your own email" works
- [ ] `/health` returns `{"ok": true, "emails": 520}`
- [ ] No keys in the repo (`git grep -nE "sk-[a-z0-9]{20}|AIza"` finds nothing)
- [ ] DeepSeek balance alert is on, and the balance is above $1
