
# haridha — cotton tote website (static + GitHub Pages)

This bundle contains a minimal, elegant website for **haridha** with:
- **Home**, **Products** (loaded from `products.json`), and **About** pages (SPA)
- Lightweight CSS, responsive layout, and local placeholder images (SVG)

## Update prices or images
1. Open `products.json`
2. Edit `price` (number only) and `img` path (e.g., `assets/products/your-image.jpg`)
3. Drop your images into `assets/products/`
4. Refresh the site

> Tip: Use WebP/JPG around 1200×1000 px. Keep names in lowercase-hyphen style, e.g., `market-olive.webp`.

## Run locally
To avoid browser CORS blocking `fetch('products.json')`, serve files via a tiny local server:
```bash
python -m http.server 8000
# then open http://localhost:8000
```

## Publish to GitHub Pages
1. Create a new public repo, e.g., `haridha-site`
2. Upload **all files and folders** in this zip
3. In GitHub → **Settings → Pages**
   - **Source**: Deploy from branch
   - **Branch**: `main` (root)
4. Your site will be live at: `https://<username>.github.io/haridha-site/`

(If you name the repo `<username>.github.io`, it will publish at the root domain.)

## Change navigation labels or copy
Edit `index.html` — look for the **About** and **Home** sections and tweak the copy.

---
© haridha
