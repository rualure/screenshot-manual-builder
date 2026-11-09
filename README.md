# Screenshot Manual Builder

スクリーンショットを根拠に、番号付き注釈と操作説明を備えたHTMLマニュアルを作成するCodexスキルです。

## 主な方針

- 元画像の縦横比と画面全体を保持
- 操作番号と注釈を対応させ、タップ位置・確認対象を明示
- スワイプは指を動かす方向の矢印で説明
- PCでは画像と説明を横並び、スマートフォンでは縦並び
- 各画面の目視確認、公式情報との照合、ブラウザ検証

## インストール

このリポジトリをCodexのスキルディレクトリへ配置します。

```sh
git clone https://github.com/rualure/screenshot-manual-builder.git ~/.codex/skills/screenshot-manual-builder
```

すでに同名ディレクトリがある場合は、内容を確認してから導入してください。

## 使い方

Codexで次のように依頼します。

```text
$screenshot-manual-builder を使って、指定フォルダのスクリーンショットからHTML操作マニュアルを作成してください。
```

Python 3.9以上があれば、同梱のビルダーを単独でも実行できます（外部Pythonパッケージ不要）。

```sh
python3 scripts/build_manual.py MANIFEST.json --output MANUAL.html
```

マニフェストの書式は [references/manifest-schema.md](references/manifest-schema.md) を参照してください。画像はHTMLに埋め込まれます。

## 同梱ビルダーの対応範囲

標準ビルダーは矩形注釈と平文の手順を描画します。スワイプ矢印、実UIアイコン、メニュー一覧、準備・後続操作の分離は、スキルの指針に従って利用先の生成スクリプトとテンプレートを拡張してください。

詳細な制作・確認手順は [SKILL.md](SKILL.md) を参照してください。
