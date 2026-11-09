# Per-image review checklist

Review each screenshot card as an independent unit. Record PASS only when every applicable item passes.

## Screenshot fidelity

- The card uses the intended source screenshot.
- The complete screenshot is visible without distortion or cropping.
- For smartphone manuals, the source was captured at the target smartphone viewport and follows the SKILL.md “Capture smartphone screens” rules, including the enlargement policy.
- Every tap box surrounds the exact control; confirmation boxes identify the values or text being checked.
- Swipe steps use arrows pointing in the direction of finger movement, with the step badge at the start. A revealed button has its own tap box.
- Every numbered operation or confirmation maps to the same number on the image; preparation and off-screen follow-up are outside the numbered sequence.
- Menu overview rows and their matching screenshot controls share the same numbers.
- Boxes, arrows, labels, and badges remain aligned after browser resizing.
- Text in the screenshot remains legible at practical zoom.

## Explanation quality

- The title identifies the visible screen or task.
- The meaning describes what the screen does without inventing hidden behavior.
- The use case helps the intended reader decide when to use it.
- Steps follow the actual visible control sequence; no hidden or previous-screen control is marked as visible.
- Menu explanations separate the home overview from individual icon/name/function rows.
- Control icons match the actual UI and sit beside the relevant names.
- Small detail references navigate to the correct section; printed page references match the checked final output.
- Cautions cover permissions, deletion, billing, sharing, privacy, and prerequisites when applicable.
- Wording preserves meaningful distinctions between similar screens or states.

## Evidence

- Visible claims are traceable to the screenshot.
- Non-visible or current-behavior claims are supported by a primary source.
- The cited page directly supports the claim.
- Captured UI state and current documentation are distinguished when they differ.
- Uncertainty is explicit; proposals and inferences are not phrased as confirmed behavior.

## Safety and usability

- Sensitive content is absent, redacted, or clearly bounded to local-only use.
- Alt text is useful and does not expose private information.
- The card works with keyboard navigation and increased browser zoom.
- The mobile layout stacks without overlap or horizontal scrolling.
- Destructive actions are not presented as harmless or reversible without evidence.

## Review loop

For each image, maintain a short record in working notes:

```text
image: 01.png
cycle: 1
status: FAIL
reasons: callout 2 is offset; billing availability lacks a primary source
correction: adjusted x/width; replaced unsupported statement with sourced limitation
```

Run at most three cycles per image. Report unresolved FAIL items rather than silently accepting them.

