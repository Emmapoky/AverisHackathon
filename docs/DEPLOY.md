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

**Free alternatives** if the balance runs out: Gemini free tier (also reads scanned PDFs; set `LLM_MIN_INTERVAL=4`) or Groq. See `.env.example`.

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
2. Space → Settings → **Variables and secrets**: add `DEEPSEEK_API_KEY`, `SUPABASE_URL`, `SUPABASE_KEY` as **secrets**, and `LLM_PROVIDER=deepseek` as a variable.
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
- [ ] No keys in the repo (`git grep -nE "sk-[a-z0-9]{20}|AIza"` finds nothing)
- [ ] DeepSeek balance alert is on, and the balance is above $1
