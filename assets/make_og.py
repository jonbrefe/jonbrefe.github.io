#!/usr/bin/env python3
"""Generate the social preview banner (og:image) for the site.

Outputs a 1200x630 PNG matching the terminal / phosphor theme.
Run: python3 make_og.py
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "og-image.png")

W, H = 1200, 630
BG = (11, 15, 20)
GRID = (28, 42, 53)
GREEN = (63, 185, 80)
GREEN_BRIGHT = (86, 211, 100)
AMBER = (227, 179, 65)
CYAN = (57, 197, 207)
MUTED = (147, 166, 180)
TEXT = (215, 224, 232)

MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
MONO_B = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# Faint engineering grid
step = 44
for x in range(0, W, step):
    d.line([(x, 0), (x, H)], fill=GRID, width=1)
for y in range(0, H, step):
    d.line([(0, y), (W, y)], fill=GRID, width=1)

# Left accent bar
d.rectangle([0, 0, 10, H], fill=GREEN)

PAD = 80
f_prompt = ImageFont.truetype(MONO, 30)
f_name = ImageFont.truetype(MONO_B, 78)
f_tag = ImageFont.truetype(MONO, 30)
f_chip = ImageFont.truetype(MONO, 26)
f_url = ImageFont.truetype(MONO_B, 30)

# Prompt line
y = 120
d.text((PAD, y), "jonathan@tux", font=f_prompt, fill=GREEN)
w1 = d.textlength("jonathan@tux", font=f_prompt)
d.text((PAD + w1, y), ":", font=f_prompt, fill=MUTED)
w2 = d.textlength("jonathan@tux:", font=f_prompt)
d.text((PAD + w2, y), "~", font=f_prompt, fill=CYAN)
w3 = d.textlength("jonathan@tux:~", font=f_prompt)
d.text((PAD + w3, y), "$ whoami", font=f_prompt, fill=MUTED)

# Name
y += 60
d.text((PAD, y), "Jonathan Brenes", font=f_name, fill=TEXT)
y += 88
d.text((PAD, y), "Fernández", font=f_name, fill=TEXT)

# Tagline
y += 118
d.text((PAD, y), "Senior Technical Support Engineer", font=f_tag, fill=AMBER)
y += 40
d.text((PAD, y), "Azure Linux Escalation · Open Source · Automation", font=f_tag, fill=AMBER)

# Chips
y += 70
chips = ["25+ yrs Linux", "Azure Linux", "OSS contributor", "AI-augmented"]
x = PAD
for c in chips:
    tw = d.textlength(c, font=f_chip)
    pad_x, pad_y = 16, 10
    box = [x, y, x + tw + pad_x * 2, y + 26 + pad_y * 2]
    d.rounded_rectangle(box, radius=18, outline=GRID, width=2, fill=(19, 26, 34))
    d.text((x + pad_x, y + pad_y), c, font=f_chip, fill=CYAN)
    x = box[2] + 14

# URL bottom-right
url = "jonathan.brenes.info"
uw = d.textlength(url, font=f_url)
d.text((W - PAD - uw, H - 70), url, font=f_url, fill=GREEN_BRIGHT)

img.save(OUT)
print("wrote", OUT, img.size)
