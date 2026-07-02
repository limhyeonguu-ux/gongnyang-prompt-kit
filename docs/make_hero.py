#!/usr/bin/env python3
"""docs/hero.gif — 공냥 프롬프트 킷 VOL.2 컴파일 데모.
3막: 거친 요청 타이핑 → 완성 프롬프트 컴파일(Tier-1 가드) → 검증기 통과.
의존성: Pillow + Malgun(한글) + D2Coding(한글 모노).
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 640
BG, PANEL, PAN2, LINE = (11,13,18), (19,22,31), (23,27,38), (36,41,56)
INK, DIM, MINT, GOLD = (238,241,247), (139,147,167), (94,234,212), (244,207,122)

MAL  = "/mnt/c/Windows/Fonts/malgun.ttf"
MALB = "/mnt/c/Windows/Fonts/malgunbd.ttf"
D2   = "/home/seunghyeong/.fonts/d2coding/D2Coding-Ver1.3.2-20180524.ttf"
f_word = ImageFont.truetype(MALB, 28)
f_vol  = ImageFont.truetype(D2, 17)
f_tag  = ImageFont.truetype(MAL, 15)
f_sm   = ImageFont.truetype(MAL, 15)
f_rough= ImageFont.truetype(MALB, 28)
f_code = ImageFont.truetype(D2, 18)
f_chk  = ImageFont.truetype(D2, 17)
f_arr  = ImageFont.truetype(D2, 40)

def rr(d, box, r, **kw): d.rounded_rectangle(box, radius=r, **kw)

def cat_mark(d, cx, cy, s, col):
    d.polygon([(cx-s,cy-s*0.2),(cx-s*0.55,cy-s*1.05),(cx-s*0.15,cy-s*0.35)], outline=col, width=3)
    d.polygon([(cx+s,cy-s*0.2),(cx+s*0.55,cy-s*1.05),(cx+s*0.15,cy-s*0.35)], outline=col, width=3)
    d.ellipse([cx-s,cy-s*0.5,cx+s,cy+s*0.9], outline=col, width=3)
    d.ellipse([cx-s*0.42-2,cy+s*0.05-2,cx-s*0.42+2,cy+s*0.05+2], fill=col)
    d.ellipse([cx+s*0.42-2,cy+s*0.05-2,cx+s*0.42+2,cy+s*0.05+2], fill=col)

# ── 1막: 거친 요청 ──
ROUGH_LINES = ['"봄밤 야시장', '포스터 하나', '만들어줘"']
ROUGH_TOTAL = sum(len(l) for l in ROUGH_LINES)

# ── 2막: 완성 프롬프트 (글자, 색) 토큰 + 줄바꿈 마커 ──
LINES = [
    ("Scene: ", "상단 1/3 굵은 세리프 타이틀, 중앙 달·야시장 일러스트, 하단 카피 여백.", MINT),
    ("Camera: ", "정면 중앙 정렬, 풀블리드.", MINT),
    ("Lighting: ", "부드러운 소프트박스 균등광, 옅은 콘택트 섀도.", MINT),
    ("Color: ", "#0F1D30 · #F7F4EC · #B76E79.", MINT),
    ("Text: ", '"봄밤 야시장" 상단 타이틀, 한 번씩만 또렷하게.', MINT),
    ("Guard: ", "All text appears once, perfectly legible.", MINT),
    ("AR 4:5", "", GOLD),
]
tokens = []
for lbl, body, col in LINES:
    for ch in lbl: tokens.append((ch, col))
    for ch in body: tokens.append((ch, INK if body else col))
    tokens.append(("\n", None))
TOTAL = sum(1 for c,_ in tokens if c != "\n")

CARD_L, CARD_R = 578, 1240
TX0, TXMAX = 604, 1212
LINE_H = 29

def draw_rough(d, n, cursor):
    """1막 — 거친 요청을 n글자까지 타이핑."""
    drawn = 0; last = None
    for i, ln in enumerate(ROUGH_LINES):
        take = max(0, min(len(ln), n - drawn))
        if take:
            seg = ln[:take]
            x, y = 64, 216 + i*50
            d.text((x, y), seg, font=f_rough, fill=INK)
            last = (x + d.textlength(seg, font=f_rough), y)
        drawn += len(ln)
        if drawn >= n: break
    if cursor and last:
        d.rectangle([last[0]+4, last[1]+6, last[0]+16, last[1]+38], fill=GOLD)

def draw_tokens(d, n, cursor):
    """2막 — 완성 프롬프트를 n글자까지 타이핑. 폭 넘으면 자동 줄바꿈."""
    x, y = TX0, 194
    drawn = 0; last = (x, y)
    for ch, col in tokens:
        if ch == "\n":
            x = TX0; y += LINE_H; continue
        if drawn >= n: break
        w = f_code.getbbox(ch)[2]
        if x + w > TXMAX:
            x = TX0; y += LINE_H
        d.text((x, y), ch, font=f_code, fill=col)
        x += w; drawn += 1; last = (x, y)
    if cursor:
        d.text((last[0]+2, last[1]), "▌", font=f_code, fill=MINT)

CHK_CMD = "$ node scripts/check_prompt.mjs prompt.txt"
CHK_OUT = '{ "ok": true, "format": "A", "tier": 1, "errors": [] }'

P0, P1, P2, P3 = 12, 42, 8, 14           # 거친요청 / 컴파일 / 검증 / 홀드
FRAMES = P0 + P1 + P2 + P3
frames = []
for fi in range(FRAMES):
    img = Image.new("RGB", (W, H), BG)
    ov = Image.new("RGBA", (W, H), (0,0,0,0)); do = ImageDraw.Draw(ov)
    do.ellipse([850,-180,1500,360], fill=(94,234,212,16))
    do.ellipse([-260,120,360,620], fill=(244,207,122,10))
    img = Image.alpha_composite(img.convert("RGBA"), ov).convert("RGB")
    d = ImageDraw.Draw(img)

    # 헤더 — VOL.2 배지
    cat_mark(d, 52, 44, 16, MINT)
    d.text((78, 30), "공냥 프롬프트 킷", font=f_word, fill=INK)
    bw = d.textlength("VOL.2", font=f_vol)
    bx = 78 + d.textlength("공냥 프롬프트 킷", font=f_word) + 14
    rr(d, [bx, 33, bx+bw+16, 59], 7, outline=GOLD, width=1)
    d.text((bx+8, 37), "VOL.2", font=f_vol, fill=GOLD)
    rt = "Claude Code Skill · gpt-image-2"
    d.text((W-40-d.textlength(rt, font=f_sm), 40), rt, font=f_sm, fill=DIM)
    d.line([(40,84),(W-40,84)], fill=LINE, width=1)

    # 좌 카드 — 거친 요청
    rr(d, [40,110,520,440], 16, fill=PANEL, outline=LINE, width=1)
    d.text((64,132), "거친 요청", font=f_tag, fill=DIM)
    rough_n = min(ROUGH_TOTAL, int(ROUGH_TOTAL*(fi+1)/P0)) if fi < P0 else ROUGH_TOTAL
    draw_rough(d, rough_n, cursor=(fi < P0))

    # 화살표 — 컴파일 중에만 펄스
    if fi >= P0:
        puls = 0.55 + 0.45*abs(((fi%18)/18)*2-1)
        acol = tuple(int(MINT[k]*puls + DIM[k]*(1-puls)) for k in range(3))
        d.text((540, 258), "→", font=f_arr, fill=acol)

    # 우 카드 — 완성 프롬프트
    rr(d, [CARD_L,110,CARD_R,440], 16, fill=PAN2, outline=LINE, width=1)
    d.text((604,132), "완성 프롬프트 · C3 한국어 포스터 · Tier-1", font=f_tag, fill=DIM)
    if fi >= P0:
        k = fi - P0
        n = TOTAL if k >= P1 else int(TOTAL*(k+1)/P1)
        blink = (k < P1) or ((fi//3) % 2 == 0)
        draw_tokens(d, n, cursor=blink)

    # 하단 스트립 — 검증기
    rr(d, [40,464,CARD_R,600], 16, fill=PANEL, outline=LINE, width=1)
    d.text((64,484), "티어 인식 검증기", font=f_tag, fill=DIM)
    if fi >= P0 + P1:
        k = fi - P0 - P1
        cmd_n = min(len(CHK_CMD), int(len(CHK_CMD)*(k+1)/P2)) if k < P2 else len(CHK_CMD)
        d.text((64, 516), CHK_CMD[:cmd_n], font=f_chk, fill=DIM)
        if k >= P2:
            d.text((64, 548), CHK_OUT, font=f_chk, fill=MINT)
            pw = d.textlength("PASS", font=f_chk)
            px = CARD_R - 40 - pw - 18
            rr(d, [px, 542, px+pw+18, 572], 8, outline=MINT, width=1)
            d.text((px+9, 547), "PASS", font=f_chk, fill=MINT)

    frames.append(img.convert("P", palette=Image.ADAPTIVE, colors=96))

frames[0].save("docs/hero.gif", save_all=True, append_images=frames[1:],
               duration=90, loop=0, optimize=True, disposal=2)
print("wrote docs/hero.gif frames=", len(frames))
