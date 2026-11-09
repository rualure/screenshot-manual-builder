# Visual operation explanations

## Home and menu introduction

Separate the home screen overview from the menu explanation. Explain what appears on the home screen, then list each menu button in its own row: actual icon and label on the left, a short explanation of what it does on the right.

Use the app's real icon assets or verified source SVG/glyphs; compare them with the captured UI. Keep icons next to quoted control names in operation prose when that helps readers locate the control. Preserve the visible label and avoid substituting emoji or a similar-looking unrelated icon. Embed assets in a self-contained HTML deliverable. Decorative icons beside an existing text label should not duplicate screen-reader text.

Give each menu row a small detail reference. In HTML, use a stable section link such as “詳しくは 02 →”. In paginated output, use “詳しくは p.5” only after checking the final page. Keep document item numbers distinct from screenshot operation numbers. Do not invent page numbers for HTML.

Describe the feature's purpose, then its current availability when relevant. For example, a public-material catalogue can be described as a place to find and add published materials, followed by the currently available provider or price scope. Keep future capabilities conditional and out of instructions for current operations. Product-specific facts belong in that manual, not in this skill.

## Match every step and target

For each screenshot, write the actions and confirmations actually visible there. Use the same numbered badges in the steps and on the image: step 1 maps to marker 1, step 2 to marker 2. The first annotation must identify the first numbered target, rather than an arbitrary region of interest.

- Taps: draw a tight red box around the exact button, icon, tab, input, or selectable row. When a step offers alternatives, identify the actual choice controls, not the surrounding panel.
- Confirmations: box the precise value, heading, or text being checked; phrase the step as a confirmation so it does not imply that a non-interactive region is tappable.
- Preparation: explain how to reach the captured state before the numbered sequence. A button from a previous screen must not be represented by a box on a different current-screen control.
- Follow-up: put results, scrolling to another state, and later operations after the numbered sequence, with a link to the relevant screenshot when available.
- Hidden targets: use another captured state or explicitly tell the reader how to reveal the control. Never draw a target over navigation that obscures it, blurred dialog backgrounds, or a nearby unrelated element.

For a menu overview, number the menu rows and matching image controls together; it is a control legend rather than a sequence of taps. Keep every screenshot marker explained, without unexplained gaps or a number outside the corresponding sequence.

## Show motion with arrows

Represent a swipe with a directional arrow over the surface the finger moves across. Point the arrow in the direction of finger movement, rather than the resulting panel movement. Attach the step badge at the start and add a short label such as “左へスワイプ” or “右へスワイプ”. Do not use a rectangular target box as the sole depiction of a swipe.

If swiping reveals a button, show the swipe arrow as step 1 and a separate tight tap box as step 2. Keep the arrow, badge, and label clear of the button and important text. A white outline can keep a colored arrow readable on both light and dark screenshots. Anchor arrows in image-relative coordinates so resizing preserves alignment.

Preserve the full smartphone screenshot without enlarged crops. Small inline control icons are identification aids, not enlarged duplicate screenshots.

## Verify the rendered explanation

Inspect every affected source screenshot individually, then compare the generated cards with the source. Check the full numbered sequence, exact tap target, finger direction, and absence of annotations on hidden controls. A check of number sets alone does not prove that the boxes surround the correct targets.

Render at desktop and target mobile widths. Check markers, arrowheads, badges, labels, wrapping, image loading, and overflow. Click detail links. When the user asks for all items to be checked, cover the entire manual rather than a sample; distinguish individual inspection from contact-sheet and programmatic checks in the work record. Do not call unseen cards visually verified.
