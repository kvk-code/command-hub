# OpenClaw ACP Bridge

The OpenClaw ACP (Agent Client Protocol) bridge exposes an ACP agent over stdio and forwards prompts to a running OpenClaw Gateway over WebSocket.

## Bridge Commands

Use ACP when an IDE or tooling speaks Agent Client Protocol and you want it to drive a OpenClaw Gateway session.

### Selecting Agents
ACP does not pick agents directly. It routes by the Gateway session key. Use agent-scoped session keys to target a specific agent:

```bash
openclaw acp --session agent:main:main
openclaw acp --session agent:design:main
openclaw acp --session agent:qa:bug-123
```

### Gateway Discovery
`openclaw acp` resolves the Gateway URL and auth from CLI flags or config:
- `--url` / `--token` / `--password` take precedence.
- Otherwise use configured `gateway.remote.*` settings.

## Session Mapping

By default each ACP session is mapped to a dedicated Gateway session key:
- `acp:<uuid>` unless overridden.

### Metadata Overrides (Per-Session)
```json
{
  "_meta": {
    "sessionKey": "agent:main:main",
    "sessionLabel": "support inbox",
    "resetSession": true,
    "requireExisting": false
  }
}
```

## Prompt Translation

- `text` and `resource` blocks become prompt text.
- `resource_link` with image mime types become attachments.
- The working directory can be prefixed into the prompt (default on, can be disabled with `--no-prefix-cwd`).
- Gateway streaming events are translated into ACP `message` and `tool_call` updates.
