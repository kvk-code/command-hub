---
name: gpt-researcher
description: Autonomous deep research agent that generates detailed reports on any topic. Uses GPT Researcher Reborn to search the web, synthesize sources, and produce comprehensive reports in multiple formats. Supports multi-query research, configurable LLM backends (Alibaba Coding Plan, OpenAI, Anthropic), multiple output formats (markdown, PDF, DOCX, JSON), tone customization, and Telegram streaming. Use when user asks for in-depth research, literature reviews, market analysis, or detailed investigation of any topic.
---

# GPT Researcher Reborn

Enhanced autonomous research agent with multi-format output, configurable models, and Telegram integration.

## Invocation

### CLI (Recommended)
```bash
/data/.openclaw/bin/gpt-researcher-reborn "your research query" --format markdown --tone analytical --model qwen3.5-plus --verbose
```

### Options
| Option | Values | Description |
|--------|-------------|-------------|
| `--type` | research, resource, outline, detailed, deep | Report type |
| `--format` | markdown, pdf, docx, json | Output format |
| `--source` | web, local, hybrid | Source type |
| `--tone` | objective, analytical, formal, casual, etc. | Writing tone |
| `--model` | qwen3.5-plus, glm-5, qwen3-max, etc. | Override model |
| `--output` | path | Save to specific file |
| `--verbose` | - | Show progress updates |
| `--telegram` | chat_id | Stream updates to Telegram |

### Python (Direct)
```python
import asyncio
from gpt_researcher import GPTResearcher

async def research(query: str):
    r = GPTResearcher(
        query=query,
        report_type="research_report",
        report_format="markdown",
        verbose=True,
    )
    await r.conduct_research()
    return await r.write_report()

report = asyncio.run(research("your topic"))
```

## Configuration

Environment: `/data/.openclaw/config/gpt-researcher.env`
- **LLM**: Alibaba Coding Plan (`sk-sp-` key)
- **Endpoint**: `coding-intl.dashscope.aliyuncs.com/v1`
- **Default Model**: `glm-5`
- **Embeddings**: Local HuggingFace `all-MiniLM-L6-v2`
- **Retriever**: Tavily (web search)

## Available Models (Coding Plan)

| Model | ID | Best For |
|-------|-----|----------|
| GLM-5 | `glm-5` | General research, balanced speed/quality |
| Qwen 3.5 Plus | `qwen3.5-plus` | Fast, good for quick research |
| Qwen3 Max | `qwen3-max-2026-01-23` | Deep analysis, best quality |
| Qwen3 Coder Plus | `qwen3-coder-plus` | Technical/code research |
| Kimi K2.5 | `kimi-k2.5` | Long-context research |
| MiniMax M2.5 | `MiniMax-M2.5` | Creative writing tone |

Override via `--model` flag or set `SMART_LLM=openai:qwen3.5-plus` in env.

## Output Formats

| Format | Extension | Use Case |
|--------|-----------|----------|
| Markdown | `.md` | Default, easy to read/edit |
| PDF | `.pdf` | Professional sharing |
| DOCX | `.docx` | Microsoft Word integration |
| JSON | `.json` | Structured data extraction |

## Report Types

| Type | Description |
|------|-------------|
| `research` | Comprehensive research report |
| `resource` | Focused on listing resources |
| `outline` | Structured outline |
| `detailed` | In-depth deep analysis |
| `deep` | Deep research mode (extensive) |

## Writing Tones

Available tones: `objective`, `formal`, `analytical`, `persuasive`, `informative`, `explanatory`, `descriptive`, `critical`, `comparative`, `speculative`, `reflective`, `narrative`, `humorous`, `optimistic`, `pessimistic`, `simple`, `casual`

Example: `--tone analytical` for critical evaluation style.

## Telegram Integration

Stream research progress to Telegram group/chat:
```bash
/data/.openclaw/bin/gpt-researcher-reborn "topic" --telegram -1003806395134 --verbose
```

Updates sent at key milestones: start, sources gathered, writing, complete.

## Key Constraints

- **Coding Plan**: No embedding API → uses local HuggingFace
- **Coding Plan**: No image generation
- **User-Agent header**: Required (`OpenClaw/2026.3.23`)
- **Endpoint**: Must use `coding-intl.dashscope.aliyuncs.com/v1`

## Examples

### Quick Research
```bash
/data/.openclaw/bin/gpt-researcher-reborn "What is RAG in AI?" --model qwen3.5-plus
```

### Deep Analysis Report
```bash
/data/.openclaw/bin/gpt-researcher-reborn "State of quantum computing 2026" --type deep --format pdf --tone formal
```

### Technical Research
```bash
/data/.openclaw/bin/gpt-researcher-reborn "How to implement LangGraph agents" --model qwen3-coder-plus --tone explanatory
```

### JSON Output (for data processing)
```bash
/data/.openclaw/bin/gpt-researcher-reborn "AI agent frameworks comparison" --format json
```

## Installation Location

- **CLI**: `/data/.openclaw/bin/gpt-researcher-reborn`
- **Config**: `/data/.openclaw/config/gpt-researcher.env`
- **Package**: `/data/.local/lib/python3.13/site-packages/gpt_researcher/`
- **Skill**: `/data/.openclaw/shared/command-hub/skills/gpt-researcher/`