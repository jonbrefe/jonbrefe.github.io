#!/usr/bin/env python3
"""Generate PNG favicon fallbacks from the terminal-glyph design.

Outputs apple-touch-icon.png (180x180) and favicon-32.png (32x32).
Run: python3 make_favicon.py
"""
import os
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
BG = (11, 15, 20)
BORDER = (34, 48, 59)
GREEN = (63, 185, 80)
GREEN_BRIGHT = (86, 211, 100)


def render(size, radius_ratio=0.19):
    scale = 8
    s = size * scale
    img = Image.new("RGB", (s, s), BG)
    d = ImageDraw.Draw(img)
    r = int(s * radius_ratio)
    d.rounded_rectangle([s * 0.05, s * 0.05, s * 0.95, s * 0.95],
                        radius=r, outline=BORDER, width=max(2, int(s * 0.03)))
    # chevron ">"
    w = max(3, int(s * 0.08))
    d.line([(s * 0.25, s * 0.34), (s * 0.44, s * 0.5), (s * 0.25, s * 0.66)],
           fill=GREEN, width=w, joint="curve")
    # underscore "_"
    d.rounded_rectangle([s * 0.5, s * 0.59, s * 0.75, s * 0.67],
                        radius=int(s * 0.03), fill=GREEN_BRIGHT)
    return img.resize((size, size), Image.LANCZOS)


for name, size in [("apple-touch-icon.png", 180), ("favicon-32.png", 32)]:
    render(size).save(os.path.join(HERE, name))
    print("wrote", name)
