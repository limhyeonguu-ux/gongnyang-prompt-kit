# 사진 어휘 풀 — 결과 기반 토큰 (photo-vocab)

> gpt-image-2는 **장비명을 모른다.** 아래 축에서 고를 때도 카메라/조명 장비를 그대로 박지 말고 **결과(빛·심도·질감·색)로 환원**해서 쓴다. 모든 표현은 긍정형 서술. 부정문(`no ~`)·SD 품질태그·가중치 문법은 쓰지 않는다.

## 1. 심도·렌즈 character (결과로)
- 광각 느낌: "wide field of view, environment fully visible, mild edge stretch, deep focus front-to-back".
- 표준: "natural perspective, balanced compression, subject and setting in proportion".
- 망원/압축: "compressed perspective, flattened planes, subject lifted from a soft background".
- 얕은 심도: "shallow depth of field, background falls off softly into creamy blur".
- 빈티지 보케: "swirly painterly bokeh, gentle vintage rendering" (Helios 룩을 결과로).
- 아나모픽: "wide cinematic frame, horizontal flares, oval highlights".

## 2. 조명 (방향·질·결과)
- 패턴: Rembrandt(뺨 삼각 하이라이트) / butterfly(코밑 나비 그림자) / split(반쪽광) / clamshell(위아래 부드러운 균등광).
- 질: "soft diffuse wraparound light, gentle gradient shadows" ↔ "hard directional light, crisp sharp-edged shadows".
- 비율: `key:fill 1:1`(평탄) / `1:2`(자연) / `1:3`(드라마틱) — 결과로 "moderate shadow contrast" 식 병기.
- 보조: "cool rim light separating the edge", "warm practical glow", "window light from camera left".
- 시간광: golden hour 따뜻한 저각광 / blue hour 차분한 한기 / 정오 톱라이트.

## 3. 색·그레이딩 (HEX·켈빈·룩)
- 팔레트는 항상 **HEX 3~5개**. 색온도는 켈빈 또는 "warm 3200K-feel / neutral / cool".
- 조화: 보색(complementary) / 유사(analogous) / 삼색(triadic).
- 룩: teal & orange, bleach bypass(저채도 고대비), desaturated muted, warm filmic roll-off.
- 필름 시뮬레이션은 **결과**로: Portra 룩 = "warm skin, soft pastel midtones, gentle highlight roll-off"; Tri-X = "high-contrast monochrome, visible grain"; CineStill 800T = "tungsten night palette, soft red halation around highlights".

## 4. 필름/매체 3파트 (패션·필름 룩)
`[필름 emulation] — [스킨], [섀도], [하이라이트]. [매거진/매체] characteristic roll-off`
예: "Kodak Portra 400 emulation — warm luminous skin, soft green-leaning shadows, creamy highlights. Editorial magazine roll-off."

## 5. 구도·시지각
- 분할: rule of thirds, golden ratio, centered iconic.
- 여백: 카피용 여백 확보(매거진 여백), Ma(여백의 호흡).
- 유도: leading lines, 시선 궤적, 삼각 안정.
- 샷 사이즈: ECU(극클로즈업) → CU → MS(미디엄) → FS(전신) → EWS(원경).
- 앵글: eye-level / low(우러름) / high(내려봄) / over-the-shoulder / dutch(기울임).
- 거리: 카메라-피사체 거리를 **미터로** 명시.

## 6. 재질·후처리 (결과)
- 표면이 빛에 어떻게 반응하는지 결과로: "matte buttery surface", "wet specular highlights", "translucent subsurface glow".
- 마감: subtle film grain, gentle vignette, halation around bright edges, clean unbranded finish(워터마크·로고 빼고 싶을 때 — 긍정형으로 "clean, brand-free, copy-free").
- 피부: "natural skin texture, visible pores, fine peach fuzz" (이상적·플라스틱 피부 대신).

## 7. 장르 즉시조합 (각 결과 토큰 묶음)
- 패션 에디토리얼: soft diffuse key + neutral palette + shallow DoF + magazine margins.
- 네온 누아르: practical neon glow, teal&orange, wet reflective street, low-angle dutch.
- 스트리트 다큐: available light, slightly desaturated, candid framing, deep focus.
- 제품 히어로: clean softbox gradient, single hero spotlight, cool rim, HEX 배경.
- 한국 웹툰: soft cel shading, glossy K-beauty finish, dewy highlights, vertical scroll.

> 인물 신원은 고정 디테일로(ethnicity+age → hair → eye(쌍꺼풀·홍채색) → beauty mark → lip finish → outfit(소재+HEX) → 배경 HEX → 카메라 거리). 챕터 내 신원 드리프트 0. 실재 인물·상표 대신 가상 페르소나/브랜드.
