# Key Operational Commands

Core maintenance and operational commands for managing OpenClaw gateways and environments.

## Gateway Management

| Command | Description |
| :--- | :--- |
| `pkill -9 -f openclaw-gateway` | Force stop a running gateway. |
| `nohup openclaw gateway run --bind loopback --port 18789 --force > /tmp/openclaw-gateway.log 2>&1 &` | Start a background gateway on a specific port. |
| `openclaw channels status --probe` | Verify channel connectivity and status. |
| `pnpm openclaw config set gateway.remote.url <url>` | Set the remote gateway URL. |

## Platform-Specific Tools

- **macOS Logs:** Use `scripts/clawlog.sh` to query unified logs for the OpenClaw subsystem (supports follow/tail/category filters).
- **Update CLI:** `sudo npm i -g openclaw@latest` (global install needs root on `/usr/lib/node_modules`).
- **Doctor:** Run `openclaw doctor` for rebrand/migration issues or legacy config/service warnings.

## Deployment & Sync

- **Signal/Fly Updates:** `fly ssh console -a flawd-bot -C "bash -lc 'cd /data/clawd/openclaw && git pull --rebase origin main'"`
- **Restart Machine:** `fly machines restart <machine-id> -a flawd-bot`.

## Batch Management & Academic Skills

| Command | Description |
| :--- | :--- |
| `ktu-tutor-view` | Check internals/attendance upload status for a KTU batch and show submission status by faculty. |
