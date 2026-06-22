# jsonl 스키마 · 완성 예제 · codex 호출 골격

> 라이브러리/배치로 뽑을 때 읽는다. 단발 프롬프트만 쓸 땐 SKILL.md §2만으로 충분.

## 1. prompts.jsonl 스키마 (1줄 = 1프롬프트 JSON)

```jsonc
{
  "id": "C1-LEVITATION-001",     // 고유키 C{n}-{CUT}-{NNN}
  "category": "C1", "cut_type": "levitation_catalog", "title": "...",
  "palette": ["#F7F4EC", "#B76E79"],
  "ar": "3:4", "size": "1024x1536",      // size=API 파라미터, ar=프롬프트 끝 토큰
  "quality": "medium",                    // 시드 medium → 최종 high. auto 금지
  "output_format": "webp", "output_compression": 82,   // 텍스트 많으면 88
  "full_prompt": "<순수 서술 ... 끝에 AR 3:4>",
  "labels": ["TRENCH COAT"], "korean_copy": "오늘 더 따뜻해요",
  "status": "draft",   // draft→queued→generated→approved|rejected→retry
  "qa": {"goal_fit": 0, "text_accuracy": 0, "material_realism": 0, "layout": 0},
  "output_path": "04_output/webp/C1/....webp",
  "teaching_point": "..."   // 교육용일 때만, 20~80자
}
```
- 합격선: qa 4항목 평균 ≥4 **AND** `text_accuracy ≥ 4`.
- `full_prompt`는 러너가 그대로 소비 — **끝에 AR만**, 앞 브래킷·Negative 없음.

## 2. 완성 예시 (C3 한국어 포스터, "포스터 하나 만들어줘" → 컴파일 결과)

```text
한국어 이벤트 포스터, 상업 인쇄 완성도.
Scene: 화면 상단 1/3에 굵은 세리프 메인 타이틀, 중앙에 달과 야시장 일러스트, 하단은 카피용 여백. 정돈된 매거진 레이아웃.
Camera: 정면 평면 구성, 중앙 대칭 정렬, 풀블리드.
Lighting: 부드러운 소프트박스 균등광, 옅은 콘택트 섀도로 깊이.
Color grading: 딥네이비 #0F1D30 배경, 크림 #F7F4EC 타이틀, 로즈골드 #B76E79 액센트는 달 테두리에만.
Texture/Medium: 매트 아트지 질감, 미세 그레인, 인쇄 톤.
Text-in-image: "봄밤 야시장" 상단 중앙(굵은 세리프), "4.20 SAT 6PM" 하단(콘덴스드 산세리프). 모든 텍스트는 한 번씩만, 완벽히 또렷하게.
AR 4:5
```
이걸 담은 jsonl 1줄:
```json
{"id":"C3-EVENT-001","category":"C3","cut_type":"event_promo","title":"봄밤 야시장","palette":["#0F1D30","#F7F4EC","#B76E79"],"ar":"4:5","size":"1024x1536","quality":"high","output_format":"webp","output_compression":88,"full_prompt":"한국어 이벤트 포스터, 상업 인쇄 완성도. Scene: ... AR 4:5","korean_copy":"봄밤 야시장","status":"draft","qa":{"goal_fit":0,"text_accuracy":0,"material_realism":0,"layout":0},"output_path":"out/C3-EVENT-001.webp"}
```
> `full_prompt`만 떼어 `node scripts/check_prompt.mjs`에 넣으면 `ok:true`여야 한다.

## 3. AUTHORING_GUIDE 8섹션 변형 (라이브러리/교육용)

기본 6섹션과 별개 체계. 챕터 단위로 변수 통제할 때:
§1 목적·용도 / §2 핵심 브리프·장면 / §3 필수 요소(엔티티 속성) / §4 맥락·환경 / §5 구도·공간 / §6 빛·색·재질·매체 / §7 제약(영어 키워드 2~3) / §8 출력(`{ar} · {size} · PNG`).
- `sections_present`로 쓸 섹션만 렌더. 챕터 내 §1·§2·§7은 전 행 동일, 변수는 §5 또는 §6 한 곳만.
- `teaching_point` 20~80자(교육용).

## 4. codex 호출 골격

배치는 챕터 단위(한 세션 N=8~20개), `codex exec --sandbox workspace-write`. full_prompt 끝에 붙인다:
```
TASK: Use the image_generation tool to create the image described above.
After generation, copy the output file to this exact path: {output_path}.
Reply only with the saved file path.
```
- codex는 **복사만**(중간 요약 금지), 이미지당 `SAVED: <path>` 1줄, 실패 `FAILED: <id> <reason>`, 끝에 `DONE chapter={slug} success=N failures=N`.
- 대량 생성·병렬 스폰은 **[codex-imagegen]** 스킬.
