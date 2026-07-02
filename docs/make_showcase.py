#!/usr/bin/env python3
"""docs/showcase/*.webp — 쇼케이스 갤러리 베이커.
생성 원본 PNG에 '거친 입력 한마디' 칩(좌하단)과 카테고리 배지(우하단)를 구워
최대 1024px webp로 저장한다. 사용: python3 docs/make_showcase.py <원본PNG디렉토리>
"""
import json, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
SRC = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "showcase" / "src"
OUT = HERE / "showcase"
MAL  = "/mnt/c/Windows/Fonts/malgun.ttf"
MALB = "/mnt/c/Windows/Fonts/malgunbd.ttf"
INK, MINT, GOLD, PILL = (238,241,247), (94,234,212), (244,207,122), (11,13,18)

def chip(d, xy, text, font, fg, anchor_right=False, img_w=0):
    pad_x, pad_y = int(font.size*0.55), int(font.size*0.38)
    w = d.textlength(text, font=font)
    x, y = xy
    if anchor_right:
        x = x - (w + pad_x*2)
    box = [x, y, x + w + pad_x*2, y + font.size + pad_y*2]
    d.rounded_rectangle(box, radius=int(font.size*0.55), fill=(*PILL, 208), outline=(255,255,255,38), width=1)
    d.text((x+pad_x, y+pad_y), text, font=font, fill=fg)
    return box

for e in json.load(open(HERE / "showcase" / "manifest.json")):
    src = SRC / f"{e['id']}.png"
    if not src.exists():
        print(f"skip {e['id']} (no source)"); continue
    im = Image.open(src).convert("RGB")
    if max(im.size) > 1024:
        r = 1024 / max(im.size)
        im = im.resize((round(im.width*r), round(im.height*r)), Image.LANCZOS)
    ov = Image.new("RGBA", im.size, (0,0,0,0))
    d = ImageDraw.Draw(ov)
    fs = max(15, im.width // 30)
    f_chip  = ImageFont.truetype(MALB, fs)
    f_badge = ImageFont.truetype(MAL, int(fs*0.78))
    margin = int(im.width * 0.035)
    ch = fs + int(f_chip.size*0.38)*2
    chip(d, (margin, im.height - margin - ch), f"“{e['rough']}”", f_chip, MINT)
    bh = int(fs*0.78) + int(f_badge.size*0.38)*2
    chip(d, (im.width - margin, im.height - margin - bh), e["badge"], f_badge, GOLD, anchor_right=True)
    im = Image.alpha_composite(im.convert("RGBA"), ov).convert("RGB")
    im.save(OUT / f"{e['id']}.webp", quality=84, method=6)
    print(f"baked {e['id']}.webp {im.size}")
print("done")
