# Personal résumé website

Static, single-page résumé site for Jonathan Brenes Fernández. Plain HTML/CSS, no build step.

## Structure

```
site/
  index.html        # the page
  styles.css        # styling (dark theme)
  assets/
    resume-master.docx   # downloadable résumé
  .nojekyll         # tells GitHub Pages to serve files as-is
```

## Preview locally

```bash
cd site
python3 -m http.server 8080
# open http://localhost:8080
```

## Before publishing — quick edits

In `index.html`:
- Replace the GitHub link (`https://github.com/`) with your profile.
- In the **Open Source & Projects** section, replace each `href="#"` with the real repo URL.
- Confirm the LinkedIn vanity URL.

## Deploy to GitHub Pages

1. Create a public repo (e.g. `jbrenes.github.io` for a user site, or any repo for a project site).
2. Put the contents of this `site/` folder at the repo root (or in `/docs`).
3. Push to `main`.
4. Repo → Settings → Pages → Source: `main` branch, root (or `/docs`).
5. Your site goes live at `https://<username>.github.io/` (user site) or
   `https://<username>.github.io/<repo>/` (project site).

For a custom domain, add a `CNAME` file with your domain and configure DNS.

## Updating the résumé download

The DOCX in `assets/` is copied from `../output/resume-master.docx`.
After regenerating that file, copy it again:

```bash
cp ../output/resume-master.docx assets/resume-master.docx
```
