# 🐾 ゴンニャン・プロンプトキット VOL.2

**曖昧なひと言を、そのまま生成に使える gpt-image-2 プロンプトへコンパイルする Claude Code スキル。**

<samp>[한국어](README.md) · [English](README.en.md) · **日本語**</samp>

[![License: MIT](https://img.shields.io/badge/License-MIT-black.svg)](LICENSE) &nbsp;![Claude Code Skill](https://img.shields.io/badge/Claude_Code-Skill-d97757) &nbsp;![target: gpt-image-2](https://img.shields.io/badge/target-gpt--image--2-1E4D40) &nbsp;![library: C1-C12 + P1-P8](https://img.shields.io/badge/library-C1--C12_+_P1--P8-C19A6B)

![ゴンニャン・プロンプトキット VOL.2 キービジュアル](docs/main.png)

「ポスターを1枚作って」程度のリクエストを受け取り、そのまま生成に投入できる完成度の韓国語プロダクションプロンプトを返す。ルールは約1,000枚規模のライブラリ（エディトリアル・ポスター・漫画）を作りながら検証し、ひとつのスキルにまとめた。上のキービジュアルも、このキットがコンパイルしたプロンプト（C11 シネマティック・キーアート）から生成したものだ。

> インタラクティブ・デモ：**[kimsh-1.github.io/gongnyang-prompt-kit](https://kimsh-1.github.io/gongnyang-prompt-kit)**

## クイックスタート

```bash
git clone https://github.com/kimsh-1/gongnyang-prompt-kit
ln -s "$PWD/gongnyang-prompt-kit/skills/image-prompt" ~/.claude/skills/image-prompt
```

Claude Code で「画像プロンプトを書いて」「エディトリアル・プロンプト」「キーアート」などのトリガー、または `/image-prompt` で実行する。

- シンボリックリンクで導入すればリポジトリの更新が自動反映される。コピーで導入した場合は更新のたびに再コピーが必要。
- バリデーターの実行には Node.js が必要。

## 何をするか

![コンパイル・デモ — 曖昧なリクエスト → 完成プロンプト → バリデーター通過](docs/hero.gif)

曖昧なリクエスト → 完成プロンプト → バリデーター通過。この3ステップがスキルの中で完結する。

| 入力 | 出力 |
|---|---|
| 「春の夜の夜市ポスターを1枚」 | シーン・カメラ・照明・パレット（HEX）・テキスト配置まで指定された完成プロンプト + `AR 4:5` |

画像生成そのものはこのスキルの範囲外。大量生成・並列スポーンは [codex-fleet](https://github.com/kimsh-1/codex-fleet) の `codex-imagegen` スキルを、1枚なら `codex` に直接投入する。（生成には [Codex CLI](https://github.com/openai/codex) のログイン + ChatGPT Plus/Pro が必要。）

## ビフォー / アフター — 同じリクエスト、同じモデル

違いは**プロンプトだけ**。左は人間のひと言をそのまま投入した結果、右は同じひと言をキットがコンパイルして投入した結果 — 同じ gpt-image-2 だ。キットが出力するのは**韓国語**のプロダクションプロンプト（韓国語レンダリングを第一に設計）なので、以下のコンパイル済みプロンプトは生成そのままの韓国語で示す。コンパイル済みプロンプトの全セットは [`examples/showcase.jsonl`](examples/showcase.jsonl) にある。

<details>
<summary>フラッグシップ — <code>かっこいい画像を1枚</code> → C11 シネマティック・キーアート（コンパイル済みプロンプト全文）</summary>

| スキルなし | キット・コンパイル |
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

以下の各ペアは同じひと言。左は素のまま、右はキット・コンパイル：

| リクエスト → プレイブック | スキルなし | キット・コンパイル |
|---|---|---|
| `ファッション・スプレッド` → C1 エディトリアル | ![](docs/showcase/SC01B.webp) | ![](docs/showcase/SC01.webp) |
| `リップバーム広告カット` → C2 ビューティ | ![](docs/showcase/SC02B.webp) | ![](docs/showcase/SC02.webp) |
| `ジャズバーのポスター` → C3 韓国語ポスター | ![](docs/showcase/SC03B.webp) | ![](docs/showcase/SC03.webp) |
| `イヤホン分解図鑑` → C4 プロダクト図鑑 | ![](docs/showcase/SC04B.webp) | ![](docs/showcase/SC04.webp) |
| `香水キャンペーン` → C5 キャンペーン | ![](docs/showcase/SC05B.webp) | ![](docs/showcase/SC05.webp) |
| `コーヒーのインフォグラフィック` → C6 インフォグラフィック | ![](docs/showcase/SC06B.webp) | ![](docs/showcase/SC06.webp) |
| `節約カードニュース` → C7 カードニュース | ![](docs/showcase/SC07B.webp) | ![](docs/showcase/SC07.webp) |
| `グラノーラのパッケージ` → C8 ブランディング・モックアップ | ![](docs/showcase/SC08B.webp) | ![](docs/showcase/SC08.webp) |
| `ロケットの3Dアイコン` → C9 3Dアイコン | ![](docs/showcase/SC09B.webp) | ![](docs/showcase/SC09.webp) |
| `猫の4コマ漫画` → C10 漫画 | ![](docs/showcase/SC10B.webp) | ![](docs/showcase/SC10.webp) |
| `SFキーアート` → C11 キーアート | ![](docs/showcase/SC11B.webp) | ![](docs/showcase/SC11.webp) |
| `高級腕時計` → L1 ラグジュアリー・エディトリアル | ![](docs/showcase/SC13B.webp) | ![](docs/showcase/SC13.webp) |
| `ダッシュボード・ヒーロー` → L5 ダークテック | ![](docs/showcase/SC17B.webp) | ![](docs/showcase/SC17.webp) |
| `年末の招待状` → L8 ゴールドフォイル | ![](docs/showcase/SC20B.webp) | ![](docs/showcase/SC20.webp) |
| `波のタイポグラフィ・ポスター` → T1 動きの翻訳 | ![](docs/showcase/SC26B.webp) | ![](docs/showcase/SC26.webp) |
| `夜市ポスター、ヒップでキッチュに` → T3 意図的な歪み | ![](docs/showcase/SC27B.webp) | ![](docs/showcase/SC27.webp) |
| `ウイスキー広告、高級に` → M2 アールデコ | ![](docs/showcase/SC28B.webp) | ![](docs/showcase/SC28.webp) |
| `ロックフェスのポスター` → M8 構成主義 | ![](docs/showcase/SC29B.webp) | ![](docs/showcase/SC29.webp) |
| `キャンドル・ブランドのポスター` → M7 アールヌーヴォー | ![](docs/showcase/SC30B.webp) | ![](docs/showcase/SC30.webp) |
| `エレクトロニック・パーティのポスター` → M9 サイケデリック | ![](docs/showcase/SC31B.webp) | ![](docs/showcase/SC31.webp) |

## プレゼン・デッキ／複雑な図表（C6·C12）— 40カット・ギャラリー

ポスターやエディトリアルだけでなく、**発表スライドや複雑な概念図**もこのキットでコンパイルする。「gpt-image-2 は図表を描けない」という通念を40カットで反証した — シーケンス図、多対多ネットワーク、フィードバックループ、そして**1スライドあたり韓国語400〜800文字の超高密度テキスト**まで。

| 超高密度テキスト（Transformer, 約700字） | キャッシュ戦略5種の比較表（約700字） |
|---|---|
| ![Transformer 超高密度スライド](examples/diagram-gallery/dense-16x9/DN-TRANSFORMER-001.png) | ![分散キャッシュ比較](examples/diagram-gallery/dense-16x9/DN-CACHE-008.png) |
| **TCP シーケンス図（ライフライン・交差メッセージ）** | **21:9 データスライド（目盛り・値ラベル）** |
| ![TCP 3-way ハンドシェイク](examples/diagram-gallery/complex-16x9/CX-TCP-002.png) | ![四半期成長レポート](examples/diagram-gallery/deck-21x9/D12-DATA-007.png) |

**40カット全ギャラリー → [`examples/diagram-gallery/`](examples/diagram-gallery/)**（インフォグラフィック・21:9デッキ・複雑な概念図・超高密度テキスト 各10カット + 元プロンプト jsonl）。

図表を開く3つのレバー：

- **テキスト精度の第一レバーはキャンバスの縦の高さ。** 21:9（codex 経路で縦 約810px）は400字で文字が小さくなる。16:9（約950px）・2:3 で縦を確保すれば700〜800字も鮮明。codex 経路は大きなキャンバス要求を長辺 約1900px に正規化するため、精度はアスペクト比の選択で稼ぐ。
- **フリーライト・ゾーンが密度の主武器。** クリティカルなラベルだけを引用符で固定し、本文は `genuine Korean sentences, fully written in real hangul` に委任すれば、モデルが概念的に正しい説明を自ら埋める（B木のキー分配・Raft ログインデックスまで論理整合）。
- **シーケンス・多対多・フィードバックも正面突破できる。** ボトルネックはモデルの能力ではなく、ノード・接続・方向を文でどれだけ具体的に指定するかだ。

> 💡 超高密度テキストのスライドは縦の高いアスペクト比（16:9 · 2:3）で最も安定する。タイトルや主要数値などクリティカルなコピーは引用符で固定し、本文の密度はフリーライト・ゾーンに委任して、必要なカットだけ取り直す。

## 販促グラフィック（P1–P8）— デザイナー・ポスターの文法

情報系SNSカードのカードニュース感ではなく、**実際のデザイナーが作った販促物**のトーンでレンダリングするレイヤー。デザイナーのリファレンス14枚から蒸留した8つのレイアウト文法（P1–P8）— 文字が装飾ではなく被写体と物理的に絡み合う構造 + 2〜3色のハードロック + 印刷仕上げのデバイス（バーコード・トンボ・エディション番号）。ルックプリセット（L）と直交し、互いに掛け合わせ（クロスブリード）できる。詳細は [`skills/image-prompt/references/promo-router.md`](skills/image-prompt/references/promo-router.md)（パターン別ドロップインは [`references/promo/`](skills/image-prompt/references/promo/)）。

### 基本パターン（P1–P8）

| P1 タイポマスク・文字の中の写真 | P2 タイポ環境・アイソメトリック地形 | P3 オーバーサイズ・クロップ + オクルージョン |
|---|---|---|
| ![P1 type-mask — seoul](docs/showcase/PR01.webp) | ![P2 type-environment — RUN isometric](docs/showcase/PR02.webp) | ![P3 occlusion — BREW](docs/showcase/PR03.webp) |
| **P5 メタUI・選択ボックス** | **P6 ストリート・コラージュ** | **P8 モノクローム・ステージング** |
| ![P5 meta UI — FORME selection box](docs/showcase/PR04.webp) | ![P6 street collage — street pop](docs/showcase/PR05.webp) | ![P8 monochrome staging — silver](docs/showcase/PR06.webp) |

### クロスブリード・韓国語ベース

パターンを2〜3個掛け合わせ、韓国語ヘッドラインで立てたセット。

| オクルージョン × 影のナラティブ（C11）・「집」 | マスキング × タイポ環境・「폭풍」 | 光の柱 × ステージング・「고요」 |
|---|---|---|
| ![집 — 立体1文字の影が夜景スカイラインに](docs/showcase/PR07.webp) | ![폭풍 — 文字の中に嵐雲、隙間から稲妻](docs/showcase/PR08.webp) | ![고요 — 文字の隙間からアンバーの光柱がウイスキーに落ちる](docs/showcase/PR09.webp) |
| **マスキング × 選択・「소리」** | **回転軸 × マスキング・「바다」** | **文字＝本棚・「책방」** |
| ![소리 — ハーフトーンの群衆、1文字だけカラー選択](docs/showcase/PR10.webp) | ![바다 — 縦マスキング + 90度回転写真](docs/showcase/PR11.webp) | ![책방 — 2文字が実際の本棚家具](docs/showcase/PR12.webp) |

韓国語ヘッドラインは**マスキング・押し出しともに2文字が安全圏**（3文字以上は画が潰れやすい）、オクルージョンは `reads behind it` の一文で成立する。

## タイポグラフィポスター（TP1〜TP14）— 文字がそのままイメージになる

「これ、文字で作ったの？」を狙うタイポグラフィポスターの文法14種。文字の中に風景をマスキングし（TP1）、一語をトンネルとして無限に反復して空間を作り（TP2）、文字を建築として積み（TP3）、ランプの影と水面の反射が文字を書き（TP4）、ガラス・クローム・風船の実物で削り出し（TP7〜TP9）、室内空間に分節塗装したペイントがただ一つの視点でのみ単語へ合体し（TP13）、数千の微細な文字が肖像を描く（TP14）。ルーター表からパターンを1つ選び、ファイルを1つだけロードする → [`skills/image-prompt/references/typo-poster-router.md`](skills/image-prompt/references/typo-poster-router.md)

| TP1・フォトマスキング（SEOUL） | TP2・テキストトンネル（무한／無限） | TP3・タイプ建築（BUILD·WERK） |
|---|---|---|
| ![TP1 photo masking — SEOUL](docs/showcase/TP01.webp) | ![TP2 text tunnel — 무한](docs/showcase/TP02.webp) | ![TP3 type architecture — BUILD WERK](docs/showcase/TP03.webp) |
| **TP4・光学現象（쉼／休息）** | **TP5・物性破壊（해체／解体）** | **TP6・スイス・キネティック（will kern for food）** |
| ![TP4 optical — 쉼 shadow](docs/showcase/TP04.webp) | ![TP5 material breakdown — 해체](docs/showcase/TP05.webp) | ![TP6 swiss kinetic — will kern for food](docs/showcase/TP06.webp) |
| **TP7・素材彫刻（얼음／氷）** | **TP8・リキッドクローム（녹아／溶けて）** | **TP9・インフレータブル（몰랑／ぷにぷに）** |
| ![TP7 material sculpting — 얼음](docs/showcase/TP07.webp) | ![TP8 liquid chrome — 녹아](docs/showcase/TP08.webp) | ![TP9 inflatable — 몰랑](docs/showcase/TP09.webp) |
| **TP10・オプアート・パターン（진동／振動）** | **TP11・アシッド・グラフィックス（광란／狂乱）** | **TP12・フューチャー・ミディーバル（심판／審判）** |
| ![TP10 op-art — 진동](docs/showcase/TP10.webp) | ![TP11 acid — 광란](docs/showcase/TP11.webp) | ![TP12 future medieval — 심판](docs/showcase/TP12.webp) |
| **TP13・アナモルフィック錯視（LOOK）** | **TP14・ミクログラフィ（고요／静けさ）** | |
| ![TP13 anamorphic — LOOK](docs/showcase/TP13.webp) | ![TP14 micrography — 고요](docs/showcase/TP14.webp) | |

韓国語のヒーロー語がほとんどのパターンでそのまま成立する — クロームドリップの「녹아」、風船の「몰랑」、オプアートの「진동」、影の「쉼」、宮書体の刃「심판」、微細文字の肖像「고요」まで。全カットのコンパイル・レコードは [`examples/typo-poster.jsonl`](examples/typo-poster.jsonl)。

## ホンデ・インディーのムードライン（L9）— ホンデ病ギャラリー

「かっこいい」という感覚を勘ではなく**8つの生成エンジン**に分解したホンデ・インディーのムードライン（ルックプリセット L9）。一語を世界へ開くタイポグラフィ（A）、芸術運動の再解釈（B）、コラージュ（C）、フィルム写真（D）、Riso ジン・ポスター（E）、ミクストメディア（F）、静物（G）、そしてオブジェの落とす影がシネマティックな場面へにじむ**影のナラティブ（H）** — 同じムードを8通りに引き出す。影のナラティブはスキルの `shadow_narrative`（C11）文法と直結する。

| H・影のナラティブ（フィルムカメラ） | A・語の世界（夜明け） | D・フィルム（夜） |
|---|---|---|
| ![shadow narrative — film camera](docs/showcase/HD01.webp) | ![word-world — dawn](docs/showcase/HD02.webp) | ![film — night](docs/showcase/HD03.webp) |
| **B・芸術運動（サイケデリック）** | **E・Riso ジン（ポスター）** | **C・コラージュ（メンフィス）** |
| ![movement — psychedelic](docs/showcase/HD04.webp) | ![Riso zine — poster](docs/showcase/HD05.webp) | ![collage — Memphis](docs/showcase/HD06.webp) |
| **G・静物（わびさび）** | **F・ミクストメディア（顔モンタージュ）** | **D・フィルム（屋台）** |
| ![still life — wabi-sabi](docs/showcase/HD07.webp) | ![mixed media — face montage](docs/showcase/HD08.webp) | ![film — pojangmacha](docs/showcase/HD09.webp) |
| **H・影のナラティブ（ウイスキーグラス）** | **A・語の世界（夏の夜）** | **D・フィルム（地下クラブ）** |
| ![shadow narrative — whiskey glass](docs/showcase/HD10.webp) | ![word-world — summer night](docs/showcase/HD11.webp) | ![film — basement club](docs/showcase/HD12.webp) |

韓国語コピーは全カットでクリーンにレンダリングされる — 影のナラティブ（H）は、オブジェから影へ物語が開くシネマティック・キーアートで3語の韓国語スローガンまで正確だ。ルックプリセットのドロップインは [`skills/image-prompt/references/look-presets.md`](skills/image-prompt/references/look-presets.md)。

## コアルール

うまく出すためのルールではなく、**うまく出ないクセを止める**ルールだ。

| ルール | 理由 |
|---|---|
| **ネガティブは既定で禁止** | gpt-image-2 は "no crowd" のようなシーンネガティブを、まさにその単語でレンダリングする。シーンの除外はすべて肯定形で — 「フレーム内に人物1人、単独」。 |
| **例外はホワイトリスト2種のみ** | Tier-1 テキストレンダー・ガード（`no duplicate text` など7種、レンダーテキストがある時のみ）・Tier-2 エディトリアル・コンプライアンス・ペア（明示宣言時のみ）。それ以外の否定文はすべてバリデーターが捕捉する。 |
| **先頭ブラケット禁止** | サイズは API パラメータ。プロンプトには末尾に `AR x:y` トークンを1つだけ置く。 |
| **文字配置はゾーン文法** | 「上部1/3のタイトルバンド」、ロールラベル（headline/subhead/callout）、引用符でコピーを固定。高密度テキストは quality high とペアリング。 |
| **機材スペック → 結果の記述** | モデルは `Canon R5 f/1.4` を知らない。「shallow DoF, background falls off softly」のように結果で書く。 |
| **SD 品質タグ・死語禁止** | `masterpiece, 8k` もノイズ、「きれいに・高級に・アワード級に」もノイズ。基準がプロンプトの外にあると平均値しか出ない — 数値・身体反応・具体例に還元する。 |
| **数値を打ち込む** | HEX パレット、ケルビン、`key:fill 1:2` — 数値が品質を上げる。 |
| **1行 = 1カット = 1コール** | 1つのキャンバスに複数カットをグリッドで描かない。（カードニュースのようにグリッド自体が成果物の場合のみ例外。） |

## 2つのフォーマット

| | Format A — ラベル付き6セクション | Format B — エディトリアル・フラットコンマ |
|---|---|---|
| **構造** | Scene / Camera / Lighting / Color grading / Texture / Text-in-image | 被写体→顔→髪→ジャンルアンカー→シーン→衣装→構図→照明→パレット `#HEX`→質感 をコンマで繋いだ一文 |
| **用途** | ポスター・キーアート・インフォグラフィック・図鑑など構造物全般 | 単独人物のエディトリアル専用 |

## カテゴリ C1–C12

ファッション/エディトリアル・ビューティ・韓国語ポスター・プロダクト図鑑・キャンペーン・インフォグラフィック・カードニュース・ブランディング・モックアップ・3Dアイコン・漫画/ウェブトゥーン・シネマティック・キーアート・**プレゼンデッキ（新規）**。カットタイプと既定 AR は `references/category-patterns.md` にある。

「高級に見せる」は勘で組まない — `references/look-presets.md` の**ルックプリセット9種**（ラグジュアリー・エディトリアル・シネマティック・グレード・ミニマル・プロダクト・スイス・タイポグラフィ・ダークテック・レトロ印刷・パステル・ゴールドフォイル・ホンデ・インディー）から選んでドロップインする。

複数の案を広げる、あるいは概念から立てるときは `references/concept-axes.md` の**変数軸**を使う — 美学運動10種（バウハウス〜わびさび、造形言語に分解したドロップイン）、身体反応の翻訳（「高級に」ではなく「声を落として静かに見てしまう」）、矛盾ペアのレイヤー分離、音楽・場面→色の翻訳、タイポグラフィ・アート4技法（上の[ビフォー/アフター](#ビフォー--アフター--同じリクエスト同じモデル)の T1・T3 が実物）。同じ被写体を1軸でスイープすれば量産コンセプト案になる。

## バリデーター

書いたプロンプトがルールを守ったかを自動で検査する。ティアを認識し、ホワイトリスト外のネガティブだけを捕捉する。

```bash
node skills/image-prompt/scripts/check_prompt.mjs examples/poster.txt      # テキストモード
node skills/image-prompt/scripts/check_prompt.mjs --tier 2 examples/hwabo_formatB.txt
node skills/image-prompt/scripts/check_prompt.mjs --jsonl examples/prompts.sample.jsonl
node skills/image-prompt/scripts/check_prompt.mjs --test                   # 回帰セルフテスト
```

`{ok, format, tier, errors, warnings}` の JSON を返す。ホワイトリスト外のネガティブ・先頭ブラケット・SD 廃語・サイズロック違反・スロットトークンの残存は `error`（肯定形リライトのヒント付き）、空の形容詞・HEX 欠落などは `warning`。通過・失敗サンプルは `examples/` にある。

## 構造

![キット構造 — 曖昧なリクエスト → スキルコア → リファレンス → 完成プロンプト → バリデーター → 画像生成](docs/architecture.png)

曖昧なリクエストがスキルコアとリファレンスを経て完成プロンプトになり、バリデーターを通過して初めて生成へ進む。（この構造図もこのキットでコンパイルした C6 インフォグラフィック・プロンプトから生成した。）

```
skills/image-prompt/
├─ SKILL.md                      # コア — ワークフロー・鉄則・ティアネガティブ・フォーマット A/B・サイズロック・ルーティング
├─ references/                   # 必要な時だけ読む深い内容
│  ├─ category-patterns.md       #   C1–C12 カットタイプ・既定 AR・漫画 A/B・キーアート・デッキ
│  ├─ look-presets.md            #   プレミアム・ルックプリセット9種のドロップイン
│  ├─ promo-router.md            #   販促文法ルーター（P1–P8）+ 仕上げデバイス + クロスブリード
│  ├─ concept-axes.md            #   変数軸 — 運動10種・身体反応の翻訳・色の翻訳・タイポグラフィアート
│  ├─ typography-layout.md       #   ゾーン文法・ロールラベル・フォント語彙・正確な文字列・グリッド
│  ├─ editorial-hwabo.md         #   エディトリアル Format B・12スロット・コンプライアンス・レーン
│  ├─ jsonl-and-examples.md      #   jsonl スキーマ・モデルファクト・codex コール骨格
│  ├─ photo-vocab.md             #   カメラ・照明・フィルム・構図・色の語彙
│  └─ style-taxonomy.md          #   ファッション21種 + ペルソナ DNA + マスターテンプレート
└─ scripts/
   ├─ check_prompt.mjs           # ティア認識バリデーター（--jsonl/--tier/--api/--test）
   └─ fixtures/                  # 回帰テスト・フィクスチャ
```

SKILL.md には常時ロードされるコアのみを置き、深い詳細は `references/` に分離した（プログレッシブ・ディスクロージャー）。

## ライセンス

MIT
