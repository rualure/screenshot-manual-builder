---
name: screenshot-manual-builder
description: "Create or revise a source-checked HTML操作マニュアル from supplied screenshots, including numbered callouts and per-image review."
---

# Screenshot Manual Builder

Create a trustworthy visual manual from screenshots. Treat the screenshots as evidence of the visible UI, and primary documentation as evidence of behavior that is not visible.

## Establish the task

Identify these inputs from the request and workspace:

- screenshot directory
- manual subject and intended reader
- output HTML path or filename
- whether the result must be a single self-contained HTML file
- required source sites, language, tone, branding, and publication boundary

Default to a Japanese, self-contained HTML file in the current workspace when the user does not specify otherwise. Infer the subject from the screenshots and nearby files when safe. Ask only when a missing choice would materially change the manual.

Treat screenshot count, filenames, visible account names, dates, and app versions as per-run data. Do not hardcode values from an earlier manual.

Use HTML for the first review unless the user specifies another format. When the user asks to review HTML first, defer PDF creation or updates until requested.

## Protect evidence and privacy

- Preserve every source screenshot unchanged.
- Do not place generated files inside the source screenshot directory unless requested.
- Detect passwords, tokens, billing data, personal messages, medical data, account identifiers, device names, and other private content before building the manual.
- Never repeat sensitive content in prose or generated metadata. Use neutral placeholders when the workflow shape needs it.
- For a local-only manual, include a visible warning when screenshots may contain private information.
- Before any publication or external sharing, require redacted screenshots or explicit approval for the exact visible content. Saving and technical validation do not authorize publication.

## Orchestrate the work

For a multi-image manual, use independent roles when subagents are available:

1. Assign research and screenshot inventory to a research role.
2. Assign manifest and HTML production to one implementation owner.
3. Assign per-image review to an independent reviewer.
4. Assign final reader-flow testing to a user-perspective tester.
5. Keep the primary agent responsible for scope, evidence, correction routing, and final acceptance.

Do not claim a requested model or effort level was used when the environment cannot select it. Use the closest available role and disclose the mismatch. If subagents are unavailable, run the same gates serially and say that the review was not independent.

## Inventory and inspect every screenshot

1. Enumerate supported images with a natural numeric sort; ignore hidden metadata files such as `.DS_Store`.
2. Record the source filename, pixel dimensions, visible page or dialog, and likely manual section.
3. Create a contact sheet only for orientation. Inspect every image individually at original resolution before describing or annotating it.
4. Identify the exact existing control, label, or region that each callout explains. Do not substitute a nearby element.
5. Preserve meaningful duplicates when they show different states, selections, permissions, or outcomes.

## Capture smartphone screens

For smartphone manuals, capture the actual UI at a smartphone viewport matching the target device. If no device size is specified, use 390 × 844 CSS pixels as a starting point and record the viewport used. Capture at that size rather than resizing a desktop screenshot into a phone shape.

Present the complete smartphone screenshot at its original aspect ratio with numbered annotations and adjacent explanations. Do not add separate enlarged crops or duplicate zoomed images unless the user explicitly requests them. Check readability in the rendered HTML and, when requested, the exported PDF; adjust the layout or explanation when needed.

## Research behavior

- Use current primary or official documentation for behavior, availability, permissions, shortcuts, billing, deletion, sharing, and other consequential claims.
- Distinguish what is directly visible, what official documentation states, and what is an inference.
- Add source URLs to the manifest and final HTML. Put the most relevant source near the related card when practical.
- If current documentation contradicts a screenshot, describe the screenshot as the captured state and flag the current difference. Do not silently rewrite the screenshot evidence.

## Explain controls and gestures

Read [references/visual-operation-guide.md](references/visual-operation-guide.md) when writing or revising menu explanations, operation steps, icons, cross-references, or numbered annotations. Match every numbered step to its visible target; show taps with red boxes and swipes with directional arrows. Apply these rules to every affected item, not just the example the user pointed out.

## Write the manual manifest

Read [references/manifest-schema.md](references/manifest-schema.md) and create a JSON manifest in the output workspace. Use one item per screenshot unless the user explicitly requests a different mapping.

For every item, write:

- concise title
- what the screen or setting means
- when to use it
- ordered operation steps when applicable
- cautions, prerequisites, or destructive effects
- numbered annotations with labels and percentage coordinates
- source links supporting non-visible behavior

Use the screenshot's intrinsic pixel dimensions to calculate annotation percentages. Keep boxes tight around the actual target with a small margin. Number callouts to match the corresponding operation or confirmation step exactly. Keep preparation and off-screen follow-up outside that numbered sequence.

## Build the HTML

Use [scripts/build_manual.py](scripts/build_manual.py) with [assets/manual-template.html](assets/manual-template.html) as a starting point:

```bash
python3 scripts/build_manual.py MANIFEST.json --output MANUAL.html
```

The bundled builder currently renders rectangle annotations and plain-text steps. Adapt the project generator/template for directional arrows, inline icons, menu rows, and separate preparation/follow-up text before claiming those features are implemented. Keep the changes in the reproducible generator so rebuilding preserves them.

The builder embeds screenshots as data URLs by default, producing a portable single file. The layout must keep the screenshot on the left and explanation on the right on wide screens, then stack them on narrow screens. Preserve the complete screenshot with `object-fit: contain`; never crop controls to make the layout fit.

Keep the visual design restrained: white grouped surfaces, royal-blue hierarchy, subtle borders and shadows, and red only for numbered annotation targets or warnings. Use semantic headings, useful alt text, keyboard-focus styles, a table of contents, print styles, and no required animation.

## Audit each image

Read [references/review-checklist.md](references/review-checklist.md). Review every screenshot card separately after rendering the actual HTML.

For each card:

1. Compare the rendered screenshot and callouts against the source image, including each step number, exact target, and gesture direction.
2. Check every explanation against visible evidence and cited primary sources.
3. Mark PASS or FAIL with specific reasons.
4. Correct only failed cards and render again.
5. Repeat for at most three review cycles per image.

Do not hide unresolved failures after the third cycle. Report the affected image, what remains uncertain, and what evidence or user decision is needed.

## Test the reader flow

- Open the generated HTML in a real browser.
- Click several table-of-contents links, including the first and last.
- Verify desktop two-column layout and narrow mobile stacking.
- Verify tap boxes and gesture arrows track their intended targets after resizing, and that their numbers match the steps.
- Follow detail links to confirm that they reach the intended section. Use actual exported page numbers only when a paginated output exists and has been checked.
- Verify text remains readable at increased browser zoom.
- Verify local assets and source links resolve as intended.
- Verify the HTML contains the expected number of screenshot cards and embedded images.
- Check print preview when the user requests printable output.

Do not call the manual complete based only on source inspection. Validate the rendered result. Do not publish unless the user explicitly requests publication.

## Deliver

Provide a clickable link to the final HTML and summarize:

- screenshot count and sections covered
- source and privacy status
- browser checks performed
- per-image audit result and any unresolved items
- whether the artifact is local-only, saved, technically validated, or published

