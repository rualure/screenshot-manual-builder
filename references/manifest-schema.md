# Manual manifest

Use UTF-8 JSON. Paths are resolved relative to the manifest file unless absolute.

## Shape

```json
{
  "title": "製品設定マニュアル",
  "lead": "画面を見ながら設定内容を確認するためのガイド",
  "language": "ja",
  "privacy_notice": "共有前に個人情報が写っていないか確認してください。",
  "sections": [
    {
      "title": "基本設定",
      "items": [
        {
          "id": "general-theme",
          "number": "01",
          "title": "テーマを変更する",
          "image": "screenshots/01.png",
          "alt": "設定画面のテーマ選択欄",
          "meaning": "画面の表示テーマを選びます。",
          "use_when": "明るさや見やすさを変更したいとき。",
          "steps": [
            "テーマを選択します。"
          ],
          "cautions": [
            "組織設定によって選択肢が異なる場合があります。"
          ],
          "annotations": [
            {
              "number": 1,
              "label": "テーマ選択",
              "x": 55.2,
              "y": 18.4,
              "width": 31.0,
              "height": 8.6
            }
          ],
          "sources": [
            {
              "label": "公式設定リファレンス",
              "url": "https://example.com/official-settings"
            }
          ]
        }
      ]
    }
  ],
  "sources": [
    {
      "label": "公式ドキュメント",
      "url": "https://example.com/official-docs"
    }
  ]
}
```

## Coordinate rules

- Express `x`, `y`, `width`, and `height` as percentages from `0` to `100`.
- Measure `x` and `y` from the source image's top-left corner.
- Compute `x = left_px / image_width * 100` and equivalent values for the other fields.
- Include a small margin around the target, but do not cover unrelated controls.
- Keep all rectangles inside the image bounds: `x + width <= 100` and `y + height <= 100`.

## Content rules

- Keep `id` unique and stable; use lowercase ASCII letters, digits, and hyphens.
- Keep `number` presentation-friendly and unique, such as `01`, `02`, and `03`.
- Use `steps` for operations or explicit confirmations visible in the captured screen. For informational screens, an empty list is valid. Keep preparation and off-screen follow-up outside the numbered sequence.
- Each step number must match its annotation number. Follow the visual-operation guide linked from SKILL.md for icon rows, detail references, and swipe arrows. The current builder supports rectangle annotations only; extend the project renderer explicitly for gestures rather than adding unsupported fields and assuming they render.
- Use `cautions` for prerequisites, permissions, destructive effects, irreversible actions, plan limitations, privacy, and version differences.
- Add item-level `sources` for claims specific to a screen. Use top-level `sources` for references applying to the entire manual.
- Do not place secrets or personal data in any field.

