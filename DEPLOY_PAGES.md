# Cloudflare Pages deploy - medicons gallery (static, no build)

Site root files served: `index.html`, `svg/`, `CATALOG.md`, `README.md`, `_headers`.
Do NOT deploy repo root directly (ships `sources/`, `preview/`, `react/`, `metadata/`, `.git` ~23M).

## 1. Auth

```bash
wrangler login
wrangler whoami   # must show account before deploying
```

Non-interactive CI alternative:

```bash
export CLOUDFLARE_API_TOKEN=<token>   # Pages:Edit + Zone:Read for frontendx.dev
export CLOUDFLARE_ACCOUNT_ID=<account-id>
```

## 2. Deploy (direct upload, no build)

```bash
rm -rf .pages-staging && mkdir -p .pages-staging
cp index.html CATALOG.md README.md _headers .pages-staging/
cp -r svg .pages-staging/
wrangler pages deploy .pages-staging --project-name=medicons
# first run creates the Pages project; note the <branch>.medicons.pages.dev URL
rm -rf .pages-staging
```

## 3. Custom domain medicons.frontendx.dev

No `wrangler pages domain add` subcommand exists in wrangler 4.136.2
(verified: `wrangler pages --help` lists only dev/functions/project/deployment/deploy/secret/download).
Add the domain via dashboard or API:

Dashboard: Cloudflare dashboard > Workers & Pages > medicons > Custom domains >
Set up a custom domain > `medicons.frontendx.dev` > Activate.

API alternative (needs Zone:Edit on frontendx.dev):

```bash
ACCOUNT_ID=<account-id>
PROJECT=medicons
curl -X POST "https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/pages/projects/$PROJECT/domains" \
  -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  -H "Content-Type: application/json" \
  --data '{"name":"medicons.frontendx.dev"}'
```

## 4. DNS note for frontendx.dev zone

- Zone on Cloudflare: adding the custom domain auto-creates the CNAME
  `medicons.frontendx.dev -> medicons.pages.dev`. No manual record needed.
- Zone off Cloudflare (external DNS): create manually:
  `CNAME medicons -> medicons.pages.dev` (or the branch deploy hostname shown
  after deploy). Then activate the custom domain in the Pages dashboard.
- TLS is provisioned automatically; wait for status Active before use.
