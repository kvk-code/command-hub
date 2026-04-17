---
description: "AI-powered web search via Tavily MCP with advanced filtering, topic selection, and content extraction. Use when the user asks to search the web, find information, research a topic, or extract content from URLs."
---

# Tavily Web Search Skill

AI-powered web search for research, news, and content extraction. Use when the user asks to search the web, find information, research a topic, or extract content from URLs.

## Why Tavily MCP Over Direct Search

**MCP-based search is superior to direct search APIs for several reasons:**

1. **AI-Optimized Results** — Tavily is designed specifically for AI agents. Results are cleaned, deduplicated, and formatted for LLM consumption. No HTML soup, no boilerplate.

2. **Search Depth Control** — `basic` for fast results, `advanced` for highest relevance with deeper crawling. Direct APIs like DuckDuckGo or Brave don't offer this granularity.

3. **Topic Filtering** — Filter by `general`, `news`, or `finance` to get domain-specific results. Critical for research workflows.

4. **Time-Based Filtering** — `day`, `week`, `month`, `year` filters for recency. Essential for news and current events.

5. **Domain Control** — `include_domains` and `exclude_domains` for targeted searches. Search only trusted sources.

6. **Content Extraction** — `tavily_extract` provides clean content extraction from URLs. One tool, two capabilities.

7. **AI-Generated Answers** — Optional `include_answer` parameter generates a synthesized answer from search results.

8. **Rate Limit Friendly** — Built for production AI workloads with proper rate limiting and retry logic.

## Available Tools

### `web_search` (Generic)

Simple, provider-backed search. Uses Tavily under the hood.

```
query: string — Search query
count: number — Number of results (1-10)
```

**Use when:** Simple searches, quick lookups, no special filtering needed.

### `tavily_search` (Native)

Advanced Tavily search with full control.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `query` | string | required | Search query (keep under 400 chars) |
| `search_depth` | string | `"basic"` | `"basic"` (fast) or `"advanced"` (deep) |
| `topic` | string | `"general"` | `"general"`, `"news"`, or `"finance"` |
| `max_results` | number | 5 | Number of results (1-20) |
| `include_answer` | boolean | false | Include AI-generated answer summary |
| `time_range` | string | null | `"day"`, `"week"`, `"month"`, `"year"` |
| `include_domains` | string[] | null | Restrict to these domains |
| `exclude_domains` | string[] | null | Exclude these domains |

**Use when:** Research tasks, news monitoring, domain-specific searches, need recency filtering.

### `tavily_extract` (Native)

Extract clean content from URLs.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `urls` | string[] | required | URLs to extract (1-20) |
| `query` | string | null | Rerank chunks by relevance to query |
| `extract_depth` | string | `"basic"` | `"basic"` or `"advanced"` (JS-heavy pages) |
| `chunks_per_source` | number | 1 | Chunks per URL (1-5, requires query) |
| `include_images` | boolean | false | Include image URLs |

**Use when:** Extracting article content, processing URLs shared by users, building research summaries.

## Search Depth Guide

| Depth | When to Use |
|-------|-------------|
| `basic` | Quick searches, real-time needs, most use cases |
| `advanced` | Deep research, academic topics, comprehensive coverage |

## Topic Guide

| Topic | When to Use |
|-------|-------------|
| `general` | Default, works for most searches |
| `news` | Current events, press coverage, announcements |
| `finance` | Market data, company financials, economic news |

## Time Range Guide

| Range | When to Use |
|-------|-------------|
| `day` | Breaking news, today's events |
| `week` | Recent developments, weekly roundups |
| `month` | Monthly reports, trend analysis |
| `year` | Annual context, historical comparison |

## Examples

### Quick Search (Generic)
```
User: "What's the latest on the AI Act?"
→ Use web_search with query "AI Act latest news" count 5
```

### Research with Advanced Controls
```
User: "Research recent developments in quantum computing from academic sources"
→ Use tavily_search with:
   query: "quantum computing developments"
   search_depth: "advanced"
   topic: "general"
   time_range: "month"
   max_results: 10
```

### News Monitoring
```
User: "What's happening with OpenAI this week?"
→ Use tavily_search with:
   query: "OpenAI"
   topic: "news"
   time_range: "week"
   max_results: 10
```

### Domain-Filtered Search
```
User: "Find research papers on transformers from arxiv"
→ Use tavily_search with:
   query: "transformer architecture research"
   include_domains: ["arxiv.org"]
   search_depth: "advanced"
```

### Content Extraction
```
User: "Summarize this article: https://example.com/article"
→ Use tavily_extract with:
   urls: ["https://example.com/article"]
```

### Competitive Intelligence
```
User: "What's Anthropic up to? Check their blog and news"
→ Use tavily_search with:
   query: "Anthropic announcements"
   include_domains: ["anthropic.com", "techcrunch.com"]
   topic: "news"
   time_range: "month"
```

## Best Practices

1. **Start with `web_search`** for simple queries — it's faster and sufficient for most cases.

2. **Use `tavily_search`** when you need:
   - Topic filtering (news/finance)
   - Time-based filtering
   - Domain restrictions
   - AI-generated answer summaries
   - More than 10 results

3. **Use `search_depth: "advanced"` sparingly** — it's slower but more comprehensive for deep research.

4. **Combine search + extract** for research workflows:
   - Search to find relevant URLs
   - Extract to get full content
   - Synthesize a comprehensive answer

5. **Use `include_answer: true`** when you want a quick synthesized answer alongside results.

## Configuration

Tavily is configured at the OpenClaw level:

```json
{
  "plugins": {
    "entries": {
      "tavily": {
        "enabled": true,
        "config": {
          "webSearch": {
            "apiKey": "tvly-..."
          }
        }
      }
    }
  },
  "tools": {
    "web": {
      "search": {
        "provider": "tavily",
        "enabled": true
      }
    }
  }
}
```

## Rate Limits

- Free tier: 1,000 searches/month
- Pro tier: Higher limits available
- Built-in rate limiting and retries

## Error Handling

If Tavily fails, the system will fall back to `web_search` with DuckDuckGo. For critical searches, consider retrying with `search_depth: "basic"` if `advanced` times out.
