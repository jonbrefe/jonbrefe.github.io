# Personal website — jonathan.brenes.info

Static, single-page personal site for Jonathan Brenes Fernández. Plain HTML/CSS, no build step, terminal-inspired theme.

## Structure

```
index.html    # the page
styles.css    # styling (terminal / phosphor theme)
CNAME         # custom domain
assets/
  grid.svg           # background texture
  resume-master.docx # downloadable résumé
.nojekyll     # serve files as-is
```

## Run locally

```bash
python3 -m http.server 8080
# open http://localhost:8080
```
