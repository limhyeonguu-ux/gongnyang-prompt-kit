# 🐾 Gongnyang Prompt Kit VOL.2

**A Claude Code skill that compiles a vague one-liner into a production-ready gpt-image-2 prompt.**

<samp>[한국어](README.md) · **English** · [日本語](README.ja.md)</samp>

[![License: MIT](https://img.shields.io/badge/License-MIT-black.svg)](LICENSE) &nbsp;![Claude Code Skill](https://img.shields.io/badge/Claude_Code-Skill-d97757) &nbsp;![target: gpt-image-2](https://img.shields.io/badge/target-gpt--image--2-1E4D40) &nbsp;![library: C1-C12 + P1-P8](https://img.shields.io/badge/library-C1--C12_+_P1--P8-C19A6B)

![Gongnyang Prompt Kit VOL.2 key visual](docs/main.png)

It takes a request as loose as "make me a poster" and returns a complete, ready-to-generate Korean production prompt. The rules were hardened while producing a ~1,000-image library of editorial spreads, posters, and comics — all distilled into a single skill. The key visual above was itself generated from a prompt this kit compiled (C11 cinematic key art).

> Interactive demo: **[kimsh-1.github.io/gongnyang-prompt-kit](https://kimsh-1.github.io/gongnyang-prompt-kit)**

## Quick start

```bash
git clone https://github.com/kimsh-1/gongnyang-prompt-kit
ln -s "$PWD/gongnyang-prompt-kit/skills/image-prompt" ~/.claude/skills/image-prompt
```

In Claude Code, run it with triggers like "write an image prompt", "editorial spread prompt", "key art", or `/image-prompt`.

- Install with a symlink and repo updates apply automatically. If you copy it instead, re-copy on every update.
- The validator requires Node.js.

## What it does

![Compile demo — loose request → complete prompt → validator pass](docs/hero.gif)

Loose request → complete prompt → validator pass. All three steps happen inside the skill.

| Input | Output |
|---|---|
| "make me a spring-night night-market poster" | A complete prompt specifying scene, camera, lighting, palette (HEX), and text placement + `AR 4:5` |

Image generation itself is out of scope. For bulk generation and parallel spawning, use the `codex-imagegen` skill in [codex-fleet](https://github.com/kimsh-1/codex-fleet); for a single image, feed the prompt straight to `codex`. (Generating requires a [Codex CLI](https://github.com/openai/codex) login + ChatGPT Plus/Pro.)

## Before / After — same request, same model

The **only** difference is the prompt. Left is a human's one-liner fed as-is; right is that same one-liner after the kit compiles it — same gpt-image-2. The kit outputs **Korean** production prompts (its target is Korean-first rendering), so the compiled prompt below is shown in Korean, exactly as generated. The full set of compiled prompts lives in [`examples/showcase.jsonl`](examples/showcase.jsonl).

<details>
<summary>Flagship — <code>make me a badass image</code> → C11 cinematic key art (full compiled prompt)</summary>

| Without the skill | Kit-compiled |
|---|---|
| ![without](docs/showcase/SC32B.webp) | ![C11 cinematic key art](docs/showcase/SC32.webp) |

```
시네마틱 키아트 — 새벽 구름바다 위로 도약하는 거대 고래.
Scene: 해 뜨기 직전의 구름 바다, 그 위로 거대한 혹등고래 한 마리가 구름 물보라를 흩뿌리며 도약하는 순간, 아래 절벽 끝에 작은 관측자 실루엣 한 명, 상단 하늘 밴드는 비워둔 클린 영역.
Camera: 초광각 vista, 로우 앵글, 인물 대비 압도적 스케일 대비, deep aerial perspective.
Lighting: 지평선의 골드 백라이트가 고래의 림을 태우고, 구름 틈으로 volumetric 광선이 쏟아진다.
Color grading: 새벽 인디고 #1B2440, 골드 #E8B168, 페일 로즈 #E8C4C4.
Texture/Medium: cinematic grain, 옅은 안개 드리프트.
AR 16:9
```

</details>

Every pair below is the same one-liner, left raw vs. right kit-compiled:

| Request → Playbook | Without skill | Kit-compiled |
|---|---|---|
| `fashion spread` → C1 editorial | ![](docs/showcase/SC01B.webp) | ![](docs/showcase/SC01.webp) |
| `lip-balm ad shot` → C2 beauty | ![](docs/showcase/SC02B.webp) | ![](docs/showcase/SC02.webp) |
| `jazz-bar poster` → C3 Korean poster | ![](docs/showcase/SC03B.webp) | ![](docs/showcase/SC03.webp) |
| `earbud exploded diagram` → C4 product atlas | ![](docs/showcase/SC04B.webp) | ![](docs/showcase/SC04.webp) |
| `perfume campaign` → C5 campaign | ![](docs/showcase/SC05B.webp) | ![](docs/showcase/SC05.webp) |
| `coffee infographic` → C6 infographic | ![](docs/showcase/SC06B.webp) | ![](docs/showcase/SC06.webp) |
| `savings card-news` → C7 card-news | ![](docs/showcase/SC07B.webp) | ![](docs/showcase/SC07.webp) |
| `granola package` → C8 branding mockup | ![](docs/showcase/SC08B.webp) | ![](docs/showcase/SC08.webp) |
| `rocket 3D icon` → C9 3D icon | ![](docs/showcase/SC09B.webp) | ![](docs/showcase/SC09.webp) |
| `cat 4-panel comic` → C10 comic | ![](docs/showcase/SC10B.webp) | ![](docs/showcase/SC10.webp) |
| `sci-fi key art` → C11 key art | ![](docs/showcase/SC11B.webp) | ![](docs/showcase/SC11.webp) |
| `luxury watch` → L1 luxury editorial | ![](docs/showcase/SC13B.webp) | ![](docs/showcase/SC13.webp) |
| `dashboard hero` → L5 dark tech | ![](docs/showcase/SC17B.webp) | ![](docs/showcase/SC17.webp) |
| `year-end invitation` → L8 gold foil | ![](docs/showcase/SC20B.webp) | ![](docs/showcase/SC20.webp) |
| `wave typography poster` → T1 motion translation | ![](docs/showcase/SC26B.webp) | ![](docs/showcase/SC26.webp) |
| `night-market poster, hip & kitsch` → T3 intentional distortion | ![](docs/showcase/SC27B.webp) | ![](docs/showcase/SC27.webp) |
| `whiskey ad, make it luxe` → M2 art deco | ![](docs/showcase/SC28B.webp) | ![](docs/showcase/SC28.webp) |
| `rock festival poster` → M8 constructivism | ![](docs/showcase/SC29B.webp) | ![](docs/showcase/SC29.webp) |
| `scented-candle poster` → M7 art nouveau | ![](docs/showcase/SC30B.webp) | ![](docs/showcase/SC30.webp) |
| `electronic party poster` → M9 psychedelic | ![](docs/showcase/SC31B.webp) | ![](docs/showcase/SC31.webp) |

## Presentation decks & complex diagrams (C6·C12) — 40-cut gallery

Not just posters and spreads — **presentation slides and complex conceptual diagrams** compile through this kit too. The "gpt-image-2 can't draw diagrams" assumption is disproven across 40 cuts — sequence diagrams, many-to-many networks, feedback loops, and even **400–800 characters of ultra-dense rendered Korean per slide**.

| Ultra-dense text (Transformer, ~700 chars) | Cache-strategy comparison table (~700 chars) |
|---|---|
| ![Transformer ultra-dense slide](examples/diagram-gallery/dense-16x9/DN-TRANSFORMER-001.png) | ![Distributed cache comparison](examples/diagram-gallery/dense-16x9/DN-CACHE-008.png) |
| **TCP sequence diagram (lifelines, crossing messages)** | **21:9 data slide (ticks, value labels)** |
| ![TCP 3-way handshake sequence](examples/diagram-gallery/complex-16x9/CX-TCP-002.png) | ![Quarterly growth report data slide](examples/diagram-gallery/deck-21x9/D12-DATA-007.png) |

**Full 40-cut gallery → [`examples/diagram-gallery/`](examples/diagram-gallery/)** (infographic · 21:9 deck · complex concept map · ultra-dense text, 10 each + source prompt jsonl).

Three levers that unlock diagrams:

- **The primary lever for text accuracy is canvas height.** 21:9 (codex path ~810px tall) shrinks glyphs at 400 chars. Secure height with 16:9 (~950px) or 2:3 and 700–800 chars stay crisp. The codex path normalizes large canvas requests to a ~1900px long edge, so accuracy is won through aspect-ratio choice.
- **The free-write zone is the key density weapon.** Pin only the critical labels in quotes and delegate body copy to `genuine Korean sentences, fully written in real hangul`; the model fills in conceptually correct explanations on its own (logically consistent down to B-tree key distribution and Raft log indices).
- **Sequences, many-to-many, and feedback all go through the front door.** The bottleneck isn't model capability — it's how concretely you specify nodes, links, and direction in sentences.

> 💡 Ultra-dense text slides are most stable at tall aspect ratios (16:9 · 2:3). Pin critical copy like titles and key figures in quotes, delegate body density to the free-write zone, and re-roll only the cuts you need.

## Promo graphics (P1–P8) — designer poster grammar

A layer that renders in the tone of **real designer-made promotional material**, not the card-news look of an informational SNS card. Eight layout grammars (P1–P8) distilled from 14 designer references — structures where type is not decoration but physically entangled with the subject, plus a 2–3 color hard-lock and print-finish devices (barcode, crop marks, edition number). Orthogonal to the look presets (L) and cross-breedable with them. Details in [`skills/image-prompt/references/promo-router.md`](skills/image-prompt/references/promo-router.md) (per-pattern drop-ins in [`references/promo/`](skills/image-prompt/references/promo/)).

### Base patterns (P1–P8)

| P1 Type-mask · photo inside the letters | P2 Type-environment · isometric terrain | P3 Oversize crop + occlusion |
|---|---|---|
| ![P1 type-mask — seoul](docs/showcase/PR01.webp) | ![P2 type-environment — RUN isometric](docs/showcase/PR02.webp) | ![P3 occlusion — BREW](docs/showcase/PR03.webp) |
| **P5 Meta UI · selection box** | **P6 Street collage** | **P8 Monochrome staging** |
| ![P5 meta UI — FORME selection box](docs/showcase/PR04.webp) | ![P6 street collage — street pop](docs/showcase/PR05.webp) | ![P8 monochrome staging — silver](docs/showcase/PR06.webp) |

### Cross-breeds · Korean base

Patterns cross-bred 2–3 at a time and anchored with a Korean headline.

| Occlusion × shadow narrative (C11) · "집" | Masking × type-environment · "폭풍" | Light shaft × staging · "고요" |
|---|---|---|
| ![집 — a 3D single glyph's shadow becomes a night skyline](docs/showcase/PR07.webp) | ![폭풍 — storm clouds inside the letters, lightning through the gaps](docs/showcase/PR08.webp) | ![고요 — an amber light shaft falls through the letters onto whiskey](docs/showcase/PR09.webp) |
| **Masking × selection · "소리"** | **Rotation axis × masking · "바다"** | **Letters = bookshelf · "책방"** |
| ![소리 — halftone crowd, one glyph in color selection](docs/showcase/PR10.webp) | ![바다 — vertical masking + 90° rotated photo](docs/showcase/PR11.webp) | ![책방 — two glyphs are actual bookshelf furniture](docs/showcase/PR12.webp) |

Korean headlines stay safe at **2 characters for both masking and extrusion** (3+ tends to smear the strokes); occlusion holds together with a single `reads behind it` sentence.

## Typography Posters (TP1–TP14) — Type as Image

Fourteen typography-poster grammars built to trigger "wait, that's made out of letters?" Landscape masked inside the glyphs (TP1), a single word tunneled into infinite repetition to build space (TP2), letters stacked into architecture (TP3), lamp shadows and water reflections that write the letters (TP4), forms carved from real glass, chrome, and balloons (TP7–TP9), segmented paint across an interior space that snaps into a word from one single viewpoint only (TP13), and thousands of micro-letters drawing a portrait (TP14). Pick one pattern from the router table and load a single file → [`skills/image-prompt/references/typo-poster-router.md`](skills/image-prompt/references/typo-poster-router.md)

| TP1 · Photo masking (SEOUL) | TP2 · Text tunnel (무한, mu-han, infinite) | TP3 · Type architecture (BUILD·WERK) |
|---|---|---|
| ![TP1 photo masking — SEOUL](docs/showcase/TP01.webp) | ![TP2 text tunnel — 무한](docs/showcase/TP02.webp) | ![TP3 type architecture — BUILD WERK](docs/showcase/TP03.webp) |
| **TP4 · Optical phenomenon (쉼, swim, rest)** | **TP5 · Material destruction (해체, hae-che, deconstruct)** | **TP6 · Swiss kinetic (will kern for food)** |
| ![TP4 optical phenomenon — 쉼 shadow](docs/showcase/TP04.webp) | ![TP5 material destruction — 해체](docs/showcase/TP05.webp) | ![TP6 Swiss kinetic — will kern for food](docs/showcase/TP06.webp) |
| **TP7 · Material sculpting (얼음, eol-eum, ice)** | **TP8 · Liquid chrome (녹아, nok-a, melt)** | **TP9 · Inflatable (몰랑, mol-lang, squishy)** |
| ![TP7 material sculpting — 얼음](docs/showcase/TP07.webp) | ![TP8 liquid chrome — 녹아](docs/showcase/TP08.webp) | ![TP9 inflatable — 몰랑](docs/showcase/TP09.webp) |
| **TP10 · Op-art pattern (진동, jin-dong, vibration)** | **TP11 · Acid graphics (광란, gwang-ran, frenzy)** | **TP12 · Future medieval (심판, sim-pan, judgment)** |
| ![TP10 op-art pattern — 진동](docs/showcase/TP10.webp) | ![TP11 acid — 광란](docs/showcase/TP11.webp) | ![TP12 future medieval — 심판](docs/showcase/TP12.webp) |
| **TP13 · Anamorphic illusion (LOOK)** | **TP14 · Micrography (고요, go-yo, stillness)** | |
| ![TP13 anamorphic — LOOK](docs/showcase/TP13.webp) | ![TP14 micrography — 고요](docs/showcase/TP14.webp) | |

Korean hero words hold up across most of the patterns as-is — chrome drip "녹아" (nok-a, melt), balloon "몰랑" (mol-lang, squishy), op-art "진동" (jin-dong, vibration), shadow "쉼" (swim, rest), blade-serif "심판" (sim-pan, judgment), all the way to the micro-letter portrait "고요" (go-yo, stillness). Compile records for every cut are in [`examples/typo-poster.jsonl`](examples/typo-poster.jsonl).

## Hongdae indie mood line (L9) — the Hongdae-byeong gallery

A Hongdae indie mood line (look preset L9) that decomposes the "looks-cool" feeling into **8 generation engines** rather than gut feel. Typography that opens a word into a world (A), art-movement reinterpretation (B), collage (C), film photography (D), Riso zine poster (E), mixed media (F), still life (G), and **shadow narrative (H)** — where an object's cast shadow bleeds into a cinematic scene. The same mood, drawn eight ways. Shadow narrative connects directly to the skill's `shadow_narrative` (C11) grammar.

| H · Shadow narrative (film camera) | A · Word-world (dawn) | D · Film (night) |
|---|---|---|
| ![shadow narrative — film camera](docs/showcase/HD01.webp) | ![word-world — dawn](docs/showcase/HD02.webp) | ![film — night](docs/showcase/HD03.webp) |
| **B · Movement (psychedelic)** | **E · Riso zine (poster)** | **C · Collage (Memphis)** |
| ![movement — psychedelic](docs/showcase/HD04.webp) | ![Riso zine — poster](docs/showcase/HD05.webp) | ![collage — Memphis](docs/showcase/HD06.webp) |
| **G · Still life (wabi-sabi)** | **F · Mixed media (face montage)** | **D · Film (pojangmacha)** |
| ![still life — wabi-sabi](docs/showcase/HD07.webp) | ![mixed media — face montage](docs/showcase/HD08.webp) | ![film — pojangmacha](docs/showcase/HD09.webp) |
| **H · Shadow narrative (whiskey glass)** | **A · Word-world (summer night)** | **D · Film (basement club)** |
| ![shadow narrative — whiskey glass](docs/showcase/HD10.webp) | ![word-world — summer night](docs/showcase/HD11.webp) | ![film — basement club](docs/showcase/HD12.webp) |

Korean copy renders cleanly across every cut — shadow narrative (H) nails even a 3-word Korean slogan in cinematic key art where the story opens from object to shadow. Look-preset drop-ins are in [`skills/image-prompt/references/look-presets.md`](skills/image-prompt/references/look-presets.md).

## Core rules

Not rules for making it come out well, but rules that **block the habits that make it come out badly**.

| Rule | Why |
|---|---|
| **No negatives by default** | gpt-image-2 renders scene negatives like "no crowd" using that very word. Express all scene exclusions positively — "one person in frame, alone". |
| **Only two whitelisted exceptions** | Tier-1 text-render guards (`no duplicate text`, etc. — 7 of them, only when there is rendered text) · Tier-2 editorial-compliance pair (only when explicitly declared). Every other negation gets caught by the validator. |
| **No leading brackets** | Size is an API parameter. The prompt carries only a single trailing `AR x:y` token. |
| **Text placement is a zone grammar** | "top-third title band", role labels (headline/subhead/callout), pinned quoted copy. Dense text pairs with quality high. |
| **Gear specs → result description** | The model doesn't know `Canon R5 f/1.4`. Write the result: "shallow DoF, background falls off softly". |
| **No SD quality tags or dead words** | `masterpiece, 8k` is noise, and so is "make it pretty / luxe / award-winning". If the standard lives outside the prompt, you only get the average — reduce it to numbers, bodily responses, concrete examples. |
| **Pin numbers** | HEX palettes, Kelvin, `key:fill 1:2` — numbers raise quality. |
| **1 line = 1 cut = 1 call** | Don't grid multiple cuts onto one canvas. (Exception: when the grid itself is the deliverable, like card-news.) |

## Two formats

| | Format A — 6 labeled sections | Format B — editorial flat-comma |
|---|---|---|
| **Structure** | Scene / Camera / Lighting / Color grading / Texture / Text-in-image | subject→face→hair→genre anchor→scene→wardrobe→composition→lighting→palette `#HEX`→texture, chained into one comma sentence |
| **Use** | Posters, key art, infographics, atlases — structural work in general | solo-figure editorial spreads only |

## Categories C1–C12

Fashion/editorial · beauty · Korean poster · product atlas · campaign · infographic · card-news · branding mockup · 3D icon · comic/webtoon · cinematic key art · **presentation deck (new)**. Cut types and default AR are in `references/category-patterns.md`.

"Make it look premium" isn't assembled by feel — pick from the **9 look presets** in `references/look-presets.md` (luxury editorial · cinematic grade · minimal product · Swiss typography · dark tech · retro print · pastel · gold foil · Hongdae indie) and drop them in.

To fan out multiple concepts or start from a concept, use the **variable axes** in `references/concept-axes.md` — 10 aesthetic movements (Bauhaus to wabi-sabi, decomposed into formal-language drop-ins), bodily-response translation ("make it luxe" → "makes you lower your voice and watch quietly"), contradiction-pair layer separation, music/scene→color translation, and 4 typographic-art techniques (the T1·T3 pairs in the [before/after](#before--after--same-request-same-model) above are the real thing). Sweep the same subject across one axis and you get mass-producible concept variants.

## Validator

Checks automatically whether a written prompt kept the rules. It is tier-aware and catches only negatives outside the whitelist.

```bash
node skills/image-prompt/scripts/check_prompt.mjs examples/poster.txt      # text mode
node skills/image-prompt/scripts/check_prompt.mjs --tier 2 examples/hwabo_formatB.txt
node skills/image-prompt/scripts/check_prompt.mjs --jsonl examples/prompts.sample.jsonl
node skills/image-prompt/scripts/check_prompt.mjs --test                   # regression self-test
```

Returns `{ok, format, tier, errors, warnings}` JSON. Negatives outside the whitelist, leading brackets, SD dead-vocabulary, size-lock violations, and residual slot tokens are `error` (with a positive-rewrite hint); empty adjectives, missing HEX, etc. are `warning`. Passing and failing samples are in `examples/`.

## Structure

![Kit structure — loose request → skill core → references → complete prompt → validator → image generation](docs/architecture.png)

A loose request passes through the skill core and references to become a complete prompt, and must clear the validator before generation. (This diagram was also generated from a C6 infographic prompt compiled by this kit.)

```
skills/image-prompt/
├─ SKILL.md                      # core — workflow, iron rules, tier negatives, format A/B, size-lock, routing
├─ references/                   # deep content, read only when needed
│  ├─ category-patterns.md       #   C1–C12 cut types, default AR, comic A/B, key art, deck
│  ├─ look-presets.md            #   9 premium look-preset drop-ins
│  ├─ promo-router.md            #   promo grammar router (P1–P8) + finishing devices + cross-breed
│  ├─ concept-axes.md            #   variable axes — 10 movements, bodily-response translation, color translation, typographic art
│  ├─ typography-layout.md       #   zone grammar, role labels, font vocabulary, exact strings, grid
│  ├─ editorial-hwabo.md         #   editorial Format B, 12 slots, compliance lane
│  ├─ jsonl-and-examples.md      #   jsonl schema, model facts, codex call skeleton
│  ├─ photo-vocab.md             #   camera, lighting, film, composition, color vocabulary
│  └─ style-taxonomy.md          #   21 fashion genres + persona DNA + master template
└─ scripts/
   ├─ check_prompt.mjs           # tier-aware validator (--jsonl/--tier/--api/--test)
   └─ fixtures/                  # regression test fixtures
```

SKILL.md keeps only the always-loaded core; deep detail is split into `references/` (progressive disclosure).

## License

MIT
