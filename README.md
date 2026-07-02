# 🐾 공냥 프롬프트 킷 VOL.2

**막연한 한마디를 gpt-image-2 완성 프롬프트로 컴파일하는 Claude Code 스킬.**

![공냥 프롬프트 킷 VOL.2 키비주얼](docs/main.png)

"포스터 하나 만들어줘" 수준의 요청을 받아, 바로 생성에 넣을 수 있는 완성 한국어 프로덕션 프롬프트를 만든다. 1,000장 규모의 라이브러리·화보·포스터·만화를 뽑으며 검증한 규칙을 스킬 하나로 정리했다. 위 키비주얼도 이 킷으로 컴파일한 프롬프트(C11 시네마틱 키아트)로 생성한 것이다.

> 인터랙티브 데모: **[kimsh-1.github.io/gongnyang-prompt-kit](https://kimsh-1.github.io/gongnyang-prompt-kit)**

## 빠른 시작

```bash
git clone https://github.com/kimsh-1/gongnyang-prompt-kit
ln -s "$PWD/gongnyang-prompt-kit/skills/image-prompt" ~/.claude/skills/image-prompt
```

Claude Code에서 "이미지 프롬프트 써줘", "화보 프롬프트", "키아트" 같은 트리거나 `/image-prompt`로 실행한다.

- 심볼릭 링크로 설치하면 레포 업데이트가 자동 반영된다. 복사로 설치했다면 업데이트마다 다시 복사해야 한다.
- 검증기 실행에는 Node.js가 필요하다.

## 무엇을 하나

![컴파일 데모 — 거친 요청 → 완성 프롬프트 → 검증기 통과](docs/hero.gif)

거친 요청 → 완성 프롬프트 → 검증기 통과. 이 세 단계가 스킬 안에서 끝난다.

| 입력 | 출력 |
|---|---|
| "봄밤 야시장 포스터 하나 만들어줘" | 장면·카메라·조명·팔레트(HEX)·텍스트 배치까지 지정된 완성 프롬프트 + `AR 4:5` |

이미지 생성 자체는 이 스킬의 범위 밖이다. 대량 생성·병렬 스폰은 [codex-fleet](https://github.com/kimsh-1/codex-fleet)의 `codex-imagegen` 스킬을 쓰고, 한 장이면 `codex`에 직접 넣는다. (생성까지 하려면 [Codex CLI](https://github.com/openai/codex) 로그인 + ChatGPT Plus/Pro가 필요하다.)

## 생성 예시 — 프롬프트가 이렇게 바뀝니다

같은 gpt-image-2다. **왼쪽은 사람이 친 한 줄을 그대로 넣은 결과, 오른쪽은 그 한 줄을 킷이 컴파일해서 넣은 결과** — 차이는 프롬프트뿐이다. 각 이미지 하단 칩에 실제 입력이 그대로 적혀 있고, 컴파일 프롬프트 전문은 비교마다 펼침으로 달았다. 전체 레코드는 [`examples/showcase.jsonl`](examples/showcase.jsonl).

#### `파도 타이포그래피 포스터` → T1 움직임 번역

| 스킬 없이 | 킷 컴파일 |
|---|---|
| ![스킬 없이 — 파도 타이포그래피 포스터](docs/showcase/SC26B.webp) | ![킷 컴파일 — T1 움직임 번역](docs/showcase/SC26.webp) |

<details>
<summary>컴파일 프롬프트 전문</summary>

```
타이포그래피 아트 포스터 — 파도의 에너지를 실은 한글 레터링이 유일한 피사체. Scene: 옅은 포말빛 필드 전면을 거대한 한글 레터링 '파도'가 채우는 구성. letterforms carrying the surge of a breaking wave: thick brush strokes swelling and curling upward with momentum, stroke tips bursting into fine white spray droplets, the baseline rolling like a swell, deep-sea ink gradating to foam white inside each stroke — the lettering is the only subject in the frame, all of the wave's energy living inside the strokes. Camera: 정면 평면 포스터 구성, 레터링이 프레임의 80%를 차지하는 과감한 스케일. Lighting: 균일한 인쇄 광, 획 안쪽에만 깊이감 있는 톤 변화. Color grading: deep sea ink #1D4E89, midnight undertone #101A2E, foam white #F5F8FA, 시안 스프레이 포인트 #5EEAD4. Texture/Medium: 두꺼운 스크린프린트 잉크 질감, 획 가장자리의 미세한 물보라 입자. Text-in-image: headline "파도" 화면 중앙(초대형 브러시 한글 레터링, 딥블루). All text appears once, perfectly legible — no duplicate text, no extra words, no invented glyphs, no watermark. AR 4:5
```

</details>

#### `야시장 타이포그래피 포스터, 힙하고 키치하게` → T3 의도 왜곡

| 스킬 없이 | 킷 컴파일 |
|---|---|
| ![스킬 없이 — 야시장 타이포그래피 포스터, 힙하고 키치하게](docs/showcase/SC27B.webp) | ![킷 컴파일 — T3 의도 왜곡](docs/showcase/SC27.webp) |

<details>
<summary>컴파일 프롬프트 전문</summary>

```
키치 네온 타이포그래피 포스터 — 의도적으로 왜곡된 한글 레터링이 주인공. Scene: 순흑에 가까운 밤 필드 중앙에 대형 한글 레터링 '야시장' — deliberately distorted lettering: each glyph sliced horizontally at its waist, the upper half shifted sideways like a mis-registered screen print, strokes stretched tall and slightly wobbling as if seen through hot night air, distortion stopping just before legibility breaks. 글자 주변에 네온 사인의 옅은 글로우와 작은 전구 점들이 흩어진 야시장 무드. Camera: 정면 평면 포스터 구성, 레터링이 프레임 70%를 차지. Lighting: 네온 글로우가 글자 획에서 배어나오는 self-lit lettering, 배경은 딥 섀도. Color grading: hot pink neon #F25C9B, electric mint offset layer #5EEAD4, warm bulb amber #F2B705, near-black night field #0B0D12. Texture/Medium: 네온 튜브의 유리 광택과 미세한 헤이즈, 스크린프린트 오프셋의 어긋난 잉크 레이어. Text-in-image: headline "야시장" 중앙(초대형 절단·오프셋 한글 레터링, 핑크+민트 이중 레이어). All text appears once, perfectly legible — no duplicate text, no extra words, no invented glyphs, no watermark. AR 4:5
```

</details>

#### `위스키 광고 포스터 고급스럽게` → M2 아르데코

| 스킬 없이 | 킷 컴파일 |
|---|---|
| ![스킬 없이 — 위스키 광고 포스터 고급스럽게](docs/showcase/SC28B.webp) | ![킷 컴파일 — M2 아르데코](docs/showcase/SC28.webp) |

<details>
<summary>컴파일 프롬프트 전문</summary>

```
위스키 브랜드 포스터 — 아르데코 재해석, 하이엔드 주류 광고 완성도. Scene: 딥네이비 필드 중앙에 각진 크리스탈 디캔터와 온더록 글래스 하나, 그 뒤로 방사형 선셋버스트 골드 라인과 계단형 대칭 프레임이 수직으로 상승하는 구성, 상단 타이틀 밴드. Art Deco geometry — radiating sunburst lines, stepped symmetric frame, vertical emphasis, gilded linework over deep navy, polished lacquer finish. Camera: 정면 대칭 포스터 구성, 중앙 정렬, 풀블리드. Lighting: 앰버 백글로우가 디캔터 유리를 투과하는 절제된 스펙큘러, 금박 라인에 raking light. Color grading: deep navy #101A2E, gold #C9A24B, cream #F3EEE2, amber liquid #B36A2E. Texture/Medium: 래커 마감 인쇄 톤, 금박 라인의 미세한 반짝임, 파인 그레인. Text-in-image: headline "밤의 황금기" 상단 밴드 중앙(아르데코 기하 세리프, 골드), caption "조용히 깊어지는 12년" 하단 중앙(가는 산세리프, 크림). All text appears once, perfectly legible — no duplicate text, no extra words, no invented glyphs, no watermark. AR 4:5
```

</details>

#### `록 페스티벌 포스터 멋지게` → M8 구성주의

| 스킬 없이 | 킷 컴파일 |
|---|---|
| ![스킬 없이 — 록 페스티벌 포스터 멋지게](docs/showcase/SC29B.webp) | ![킷 컴파일 — M8 구성주의](docs/showcase/SC29.webp) |

<details>
<summary>컴파일 프롬프트 전문</summary>

```
록 페스티벌 포스터 — 구성주의 재해석, 공연 인쇄물 완성도. Scene: 사선으로 화면을 가로지르는 적·흑 컬러 플레인, 그 교차점에 일렉 기타를 치켜든 연주자의 하이컨트라스트 포토몽타주 실루엣, 상단 대각 타이틀 밴드. constructivist poster dynamics — aggressive diagonal composition, angular planes slicing across the field, photomontage-style subject placement, kinetic propaganda energy. Camera: 정면 평면 포스터 구성, 대각 정렬, 풀블리드. Lighting: 플랫 인쇄 광, 실루엣 가장자리는 하드 컷. Color grading: vermilion red #B33A2B, ink black #111111, aged cream #E8DCC4. Texture/Medium: 거친 오프셋 인쇄 질감, 스텐실 에지, 종이 결. Text-in-image: headline "굉음" 상단 대각 밴드(초굵은 그로테스크 산세리프, 블랙), caption "6.21 한강 특설무대" 하단(콘덴스드 산세리프, 레드). All text appears once, perfectly legible — no duplicate text, no extra words, no invented glyphs, no watermark. AR 4:5
```

</details>

#### `향초 브랜드 포스터 예쁘게` → M7 아르누보

| 스킬 없이 | 킷 컴파일 |
|---|---|
| ![스킬 없이 — 향초 브랜드 포스터 예쁘게](docs/showcase/SC30B.webp) | ![킷 컴파일 — M7 아르누보](docs/showcase/SC30.webp) |

<details>
<summary>컴파일 프롬프트 전문</summary>

```
핸드메이드 향초 브랜드 포스터 — 아르누보 재해석, 부티크 인쇄물 완성도. Scene: 아이보리 필드 중앙에 유리컵 소이 캔들 하나, 촛불 주위를 식물 줄기 곡선과 금박 라인 장식 프레임이 유기적으로 감싸는 구성, 상단 타이틀 여백. Art Nouveau linework — flowing botanical curves framing the subject, hand-drawn organic ornament, lithograph texture. Camera: 정면 대칭 포스터 구성, 캔들 중앙, 풀블리드. Lighting: 촛불의 웜 글로우가 프레임 안쪽을 은은히 밝히는 부드러운 명암. Color grading: sage #7A8C5F, ivory #F3EEE2, gilded gold #C9A24B, deep brown #4A3B2A. Texture/Medium: 리소그래프 인쇄 질감, 손그림 라인의 미세한 흔들림, 무광 종이. Text-in-image: headline "숨" 상단 중앙(아르누보 곡선 세리프, 딥브라운), caption "손으로 붓는 소이 캔들" 하단 중앙(가는 산세리프, 세이지). All text appears once, perfectly legible — no duplicate text, no extra words, no invented glyphs, no watermark. AR 4:5
```

</details>

#### `일렉트로닉 파티 포스터 힙하게` → M9 사이키델릭

| 스킬 없이 | 킷 컴파일 |
|---|---|
| ![스킬 없이 — 일렉트로닉 파티 포스터 힙하게](docs/showcase/SC31B.webp) | ![킷 컴파일 — M9 사이키델릭](docs/showcase/SC31.webp) |

<details>
<summary>컴파일 프롬프트 전문</summary>

```
일렉트로닉 파티 포스터 — 70년대 사이키델릭 재해석, 공연 인쇄물 완성도. Scene: 소용돌이치는 동심원 물결이 화면 전체를 채우고, 그 리듬을 그대로 타고 흐르는 한글 레터링이 중앙에서 바깥으로 퍼지는 유동 구성. 70s psychedelic flow — melting liquid shapes and swirling rhythm, wavy concentric contours, vintage offset print grain. Camera: 정면 평면 포스터, 중앙 방사 구성, 풀블리드. Lighting: 플랫 인쇄 광, 고채도 색면 대비로 깊이를 만든다. Color grading: saturated clash of orange #E85D1F, purple #7B4EA3, green #3E8C4F, yellow #F2B705. Texture/Medium: 빈티지 오프셋 그레인, 살짝 어긋난 잉크 미스레지스트레이션. Text-in-image: headline "새벽" 중앙(물결치는 사이키델릭 한글 레터링, 오렌지), caption "자정부터 해 뜰 때까지" 하단(라운드 산세리프, 그린). All text appears once, perfectly legible — no duplicate text, no extra words, no invented glyphs, no watermark. AR 4:5
```

</details>

## 핵심 규칙

잘 나오게 하는 규칙이 아니라, **안 나오게 만드는 습관을 막는** 규칙이다.

| 규칙 | 이유 |
|---|---|
| **네거티브 기본 금지** | gpt-image-2는 "no crowd" 같은 장면 네거티브를 오히려 그 단어로 렌더한다. 장면 배제는 전부 긍정형 — "프레임 안엔 인물 한 명, 단독". |
| **예외는 화이트리스트 2종뿐** | Tier-1 텍스트 렌더 가드(`no duplicate text` 등 7종, 렌더 텍스트가 있을 때만) · Tier-2 화보 컴플라이언스 페어(명시 선언 시만). 나머지 부정문은 전부 검증기가 잡는다. |
| **앞 브래킷 금지** | size는 API 파라미터다. 프롬프트에는 끝에 `AR x:y` 토큰 하나만 둔다. |
| **글자 배치는 영역 문법** | "상단 1/3 타이틀 밴드", 롤 라벨(headline/subhead/callout), 따옴표 카피 고정. 밀집 텍스트는 quality high와 페어링. |
| **장비 스펙 → 결과 서술** | 모델은 `Canon R5 f/1.4`를 모른다. "shallow DoF, background falls off softly"처럼 결과로 쓴다. |
| **SD 품질태그·죽은 단어 금지** | `masterpiece, 8k`도, "예쁘게·고급스럽게·어워드 수준으로"도 노이즈다. 기준이 프롬프트 밖에 있으면 평균값만 나온다 — 수치·몸 반응·구체 예시로 환원한다. |
| **수치를 박는다** | HEX 팔레트, 켈빈, `key:fill 1:2` — 수치가 품질을 올린다. |
| **1행 = 1컷 = 1 호출** | 한 캔버스에 여러 컷을 그리드로 그리지 않는다. (카드뉴스처럼 그리드 자체가 산출물인 경우만 예외.) |

## 두 가지 포맷

| | Format A — 라벨 6섹션 | Format B — 화보 플랫 콤마형 |
|---|---|---|
| **구조** | Scene / Camera / Lighting / Color grading / Texture / Text-in-image | 피사체→얼굴→헤어→장르앵커→장면→의상→구도→조명→팔레트 `#HEX`→질감을 콤마로 잇는 한 문장 |
| **용도** | 포스터·키아트·인포그래픽·도감 등 구조물 전반 | 단독 인물 화보·에디토리얼 전용 |

## 카테고리 C1~C12

패션/화보 · 뷰티 · 한국어 포스터 · 제품 도감 · 캠페인 · 인포그래픽 · 카드뉴스 · 브랜딩 목업 · 3D 아이콘 · 만화/웹툰 · 시네마틱 키아트 · **프레젠테이션 덱(신규)**. 컷타입과 기본 AR은 `references/category-patterns.md`에 있다.

"있어보이게"는 감으로 조립하지 않는다 — `references/look-presets.md`의 **룩 프리셋 8종**(럭셔리 에디토리얼·시네마틱 그레이드·미니멀 프로덕트·스위스 타이포·다크 테크·레트로 인쇄·파스텔·골드 포일)에서 골라 드롭인한다.

시안을 여러 개 벌리거나 컨셉부터 잡을 땐 `references/concept-axes.md`의 **변수 축**을 쓴다 — 미학 사조 10종(바우하우스~와비사비, 조형언어 분해 드롭인), 몸 반응 번역("고급스럽게" 대신 "목소리를 낮추고 조용히 보게 되는"), 모순쌍 레이어 분리, 음악·장면→컬러 번역, 타이포 아트 4기법(위 [스킬 전후](#스킬-전후--같은-요청-같은-모델) 비교가 T1·T3 실물이다). 같은 피사체를 축 하나로 스윕하면 양산 컨셉 시안이 나온다.

## 검증기

작성한 프롬프트가 규칙을 지켰는지 자동으로 검사한다. 티어를 인지해서 화이트리스트 밖 네거티브만 잡는다.

```bash
node skills/image-prompt/scripts/check_prompt.mjs examples/poster.txt      # 텍스트 모드
node skills/image-prompt/scripts/check_prompt.mjs --tier 2 examples/hwabo_formatB.txt
node skills/image-prompt/scripts/check_prompt.mjs --jsonl examples/prompts.sample.jsonl
node skills/image-prompt/scripts/check_prompt.mjs --test                   # 회귀 셀프테스트
```

`{ok, format, tier, errors, warnings}` JSON을 반환한다. 화이트리스트 밖 네거티브·앞 브래킷·SD 폐기어휘·사이즈락 위반·슬롯 토큰 잔존은 `error`(긍정형 rewrite 힌트 포함), 빈 형용사·HEX 누락 등은 `warning`. 통과·실패 샘플은 `examples/`에 있다.

## 구조

![공냥 프롬프트 킷 구조 — 거친 요청 → 스킬 코어 → 레퍼런스 → 완성 프롬프트 → 검증기 → 이미지 생성](docs/architecture.png)

거친 요청이 스킬 코어와 레퍼런스를 거쳐 완성 프롬프트가 되고, 검증기를 통과해야 생성으로 넘어간다. (이 구조도 역시 이 킷으로 컴파일한 C6 인포그래픽 프롬프트로 생성했다.)

```
skills/image-prompt/
├─ SKILL.md                      # 코어 — 워크플로우·철칙·티어 네거티브·포맷 A/B·사이즈락·라우팅
├─ references/                   # 필요할 때만 읽는 깊은 내용
│  ├─ category-patterns.md       #   C1~C12 컷타입·기본 AR·만화 A/B·키아트·덱
│  ├─ look-presets.md            #   프리미엄 룩 프리셋 8종 드롭인
│  ├─ concept-axes.md            #   변수 축 — 사조 10종·몸 반응 번역·모순쌍·컬러 번역·타이포 아트
│  ├─ typography-layout.md       #   영역 문법·롤 라벨·폰트 어휘·정확 문자열·그리드
│  ├─ editorial-hwabo.md         #   화보 Format B·슬롯 12종·컴플라이언스 레인
│  ├─ jsonl-and-examples.md      #   jsonl 스키마·모델 팩트·codex 호출 골격
│  ├─ photo-vocab.md             #   카메라·조명·필름·구도·색 어휘 + 국문/영문 혼용
│  └─ style-taxonomy.md          #   패션 21종 + persona DNA + 마스터 템플릿
└─ scripts/
   ├─ check_prompt.mjs           # 티어 인식 검증기 (--jsonl/--tier/--api/--test)
   └─ fixtures/                  # 회귀 테스트 픽스처
```

SKILL.md에는 항상 로드되는 코어만 두고, 깊은 디테일은 `references/`로 분리했다(progressive disclosure).

## 라이선스

MIT
