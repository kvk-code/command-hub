---
name: visual-analysis
description: Analyze images with strong visual grounding using the best available vision-capable model. Use when examining documents, forms, handwriting, charts, signatures, or any image requiring detailed visual inspection. Triggers on phrases like "analyze image", "check signatures", "read form", "examine document", "what's in this image", "visual analysis".
---

# Visual Analysis

When analyzing images that require detailed visual inspection, always use the **best available vision-capable model**.

## Core Principle

Model capabilities evolve. Always use the model with the strongest visual inference from the current available set. As of 2026-03-24, the ranking is:

1. **Qwen 3.5 Plus** (`bailian/qwen3.5-plus`) — Best for handwriting, signatures, fine details
2. **Opus 4.6** (`github-copilot/claude-opus-4.6`) — Strong visual grounding, good for complex reasoning
3. Other models — Verify visual capability before use

## Model Selection (Current)

| Task | Best Model | Why |
|------|------------|-----|
| Document/forms with handwriting | **Qwen 3.5 Plus** | Best for distinguishing marks from empty space |
| Complex visual reasoning | **Opus 4.6** or **Qwen 3.5 Plus** | Both have strong grounding |
| Charts and graphs | Either | Both handle well |
| Text extraction from images | **Qwen 3.5 Plus** | Good OCR-like capability |
| Document verification (stamps, watermarks, fonts) | **Qwen 3.5 Plus** | Fine detail detection |

## Models to AVOID for Visual Tasks

These models have **weak visual grounding** and may hallucinate:
- GLM-5 (`bailian/glm-5`) — Weak vision, hallucinates details that aren't there
- GPT-4.1 (`github-copilot/gpt-4.1`) — Weaker on fine visual details
- Haiku 4.5 (`github-copilot/claude-haiku-4.5`) — Not designed for complex visual analysis

They tend to describe what "should" be there rather than what's actually visible.

## Usage Pattern

Spawn a subagent with the appropriate vision model:

```
sessions_spawn(
    task="Analyze image at /path/to/image.jpg for [specific task]",
    runtime="subagent",
    model="bailian/qwen3.5-plus"
)
```

## Analysis Guidelines

When analyzing visual documents:

1. **Be explicit about what to look for** — "Check each row's signature column for handwritten marks"
2. **Request row-by-row analysis** — For tables/forms, ask for each row individually
3. **Set expectations** — "Expected approximately 10-15 signatures"
4. **Verify with context** — Cross-reference with known data when possible

## Common Failure Modes

| Failure | Cause | Fix |
|---------|-------|-----|
| "All cells have signatures" | Model can't distinguish empty vs filled | Use Qwen 3.5 or Opus 4.6 |
| "I see text here" when blank | Hallucination from weak visual model | Switch models |
| Missing fine details | Model not designed for visual tasks | Use vision-capable model |

## Example Prompt

```
Analyze this attendance form image and identify which students have ACTUAL SIGNATURES.

Image: /path/to/form.jpg

For EACH ROW:
1. Read the roll number and name
2. Look at the signature column — is there a handwritten mark?
3. Only mark YES if there is clearly a signature visible

Output: Roll No | Name | Has Signature (YES/NO)

Expected: approximately 10-15 signatures total.
```