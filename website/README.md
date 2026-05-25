
# haridha — cotton tote website (static + GitHub Pages)

This bundle contains a minimal homepage for **haridha** with the full tote collection on `index.html`.
- Collection, About, and Contact sections all live on the homepage
- Product listings are generated from images in `assets/images/tote_bags_catlog`

## Add new images
1. Add the new image file to `assets/images/tote_bags_catlog/`
2. Commit and push the change to GitHub
3. GitHub Actions will automatically regenerate `products.json`
4. The homepage will update with the new image

> Tip: Use WebP/JPG around 1200×1000 px and keep file names clean.

## Run locally
To regenerate the data locally before testing:
```powershell
cd website
pwsh .\generate-products.ps1
```
Then serve the site locally, for example:
```bash
python -m http.server 8000
```
Open `http://localhost:8000/website/index.html`.

## Publish to GitHub Pages
1. Push the repository to your GitHub `main` branch
2. In GitHub → **Settings → Pages**
   - **Source**: Deploy from branch
   - **Branch**: `main`
3. The site will live from `index.html`

---
© haridha
