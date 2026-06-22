#!/usr/bin/env node
// image-prompt 룰 검증기 — 네거티브/앞브래킷/SD폐기어휘/가중치/슬래시플래그 탐지.
// 사용: node scripts/check_prompt.mjs <file>   또는   echo "<prompt>" | node scripts/check_prompt.mjs
import { readFileSync } from "node:fs";

const inputPath = process.argv[2];
let prompt;
try {
  prompt = inputPath ? readFileSync(inputPath, "utf8") : readFileSync(0, "utf8");
} catch (e) {
  console.log(JSON.stringify({ ok: false, errors: [`입력을 읽지 못함: ${e.message}`], warnings: [] }, null, 2));
  process.exit(1);
}
prompt = prompt.replace(/^﻿/, ""); // BOM 제거

const errors = [];
const warnings = [];
const has = (pattern) => pattern.test(prompt);
const head = prompt.trimStart().slice(0, 80); // "앞머리" 판정용

// ── 필수 구성 ─────────────────────────────────────────────
if (!/AR\s+\d+\s*:\s*\d+\s*$/i.test(prompt.trim())) {
  errors.push("끝에 `AR 3:4` 형태의 종횡비 토큰이 없음(반드시 프롬프트 맨 끝).");
}
if (prompt.trim().length < 220) {
  warnings.push("프롬프트가 짧음 — 프로덕션 프롬프트는 구체 시각 명세가 더 필요.");
}
if (!has(/(Scene:|한국|포스터|카드뉴스|도감|목업|아이콘|웹툰|만화|제품|패션|뷰티|인포그래픽)/)) {
  errors.push("첫 절에 매체/카테고리(결과물 장르)가 드러나지 않음.");
}
if (!has(/(Camera:|정면|톱다운|아이레벨|eye-level|로우앵글|클로즈업|와이드|중앙|레이아웃|컷|거터|읽힘)/)) {
  errors.push("카메라·구도·레이아웃 언어가 없음.");
}
if (!has(/(Lighting:|조명|키라이트|소프트박스|자연광|림라이트|그림자|컨택트 섀도|반사)/)) {
  errors.push("명시적 조명 지시가 없음.");
}
if (!has(/#[0-9A-Fa-f]{6}/)) {
  warnings.push("HEX 팔레트 없음 — 가능하면 핵심색 2~3개를 HEX로.");
}
if (!has(/(Texture\/Medium:|재질|질감|광택|종이|실크|리넨|유리|포일|베벨|셀 쉐이딩|스크린톤|수채|잉킹)/)) {
  errors.push("재질·질감·매체 디테일이 없음.");
}

// ── 텍스트 가독/반복 가드 ─────────────────────────────────
const textHeavy = has(/(Text-in-image:|텍스트|한글|타이틀|부제|라벨|말풍선|내레이션|SFX|카피|문구|")/);
if (textHeavy && !has(/(또렷|가독|한 번씩만|1~2개만|legible|appears once)/)) {
  warnings.push("텍스트가 있는데 가독성/반복 가드가 없음 (예: \"모든 텍스트는 한 번씩만, 또렷하게\").");
}

// ── 네거티브 절대 금지 (사용자 철칙) ──────────────────────
if (has(/\bNegative\s*:/i)) {
  errors.push("`Negative:` 섹션 금지 — 전부 긍정형 서술로.");
}
// 'negative space'(디자인 여백 용어)는 허용하므로 제거 후 검사
const noNeg = prompt.replace(/negative\s+space/gi, "");
const engNeg = noNeg.match(/\b(no|without|avoid|exclude|never|free of|devoid of|do not|don't)\s+[A-Za-z]/gi);
if (engNeg) {
  const uniq = [...new Set(engNeg.map((s) => s.toLowerCase().trim()))].slice(0, 5);
  errors.push(`영어 부정문 금지(${uniq.join(", ")}…) — 빼고 싶은 건 긍정형으로(예: "no text"→"텍스트 없음", "no watermark"→"브랜드 없는 클린 마감").`);
}

// ── 앞머리 [AR x:y SIZE wxh] 브래킷 금지 (맨 앞만 검사) ───
if (/^\[[^\]\n]*(\d+\s*:\s*\d+|SIZE|size)[^\]\n]*\]/.test(head)) {
  errors.push("앞머리 `[AR x:y SIZE wxh]` 브래킷 금지 — size는 API 파라미터, 프롬프트엔 끝의 `AR x:y`만.");
}

// ── SD-era 폐기 어휘 / 가중치 / 슬래시 플래그 ──────────────
const banned = prompt.match(/\b(masterpiece|best[ _]quality|(?:4|8)k|uhd|trending on artstation|ultra[- ]?detailed|hyper[- ]?detailed|highly detailed|intricate details?|sharp focus|award[- ]winning|raw photo)\b/gi);
if (banned) {
  errors.push(`SD 품질태그 폐기 어휘: ${[...new Set(banned.map((s) => s.toLowerCase()))].join(", ")}.`);
}
// 가중치 (word:1.3) — 소수점 가중치만 잡아 정상 괄호 (항목: 3개)는 통과
if (has(/\([^()]*:\s*[01]?\.\d+\s*\)/)) {
  errors.push("가중치 문법 `(word:1.3)` 금지.");
}
if (has(/--(ar|v|no|style|niji)\b/)) {
  errors.push("Midjourney식 슬래시 플래그(`--ar/--v/--no`) 금지.");
}
if (has(/(^|\n)\s*§|§\s*\d/)) {
  warnings.push("본문에 `§` 기호 사용 — 헤더 `# 1.` 형식만 허용.");
}

// ── 빈 형용사 ─────────────────────────────────────────────
const filler = prompt.match(/(멋지게|감성적으로|고급스럽게|예쁘게|beautifully|stunning|atmospheric|perfect|professional)\b/gi);
if (filler) {
  warnings.push(`빈 형용사(구체 명세로 대체): ${[...new Set(filler.map((s) => s.toLowerCase()))].join(", ")}.`);
}

const ok = errors.length === 0;
console.log(JSON.stringify({ ok, errors, warnings }, null, 2));
process.exitCode = ok ? 0 : 1;
