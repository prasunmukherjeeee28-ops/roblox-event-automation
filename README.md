# Hollow Jack Monitor (research scaffold)

A phone-friendly project for researching Slap Battles public-server discovery and Discord notifications.

## Current capabilities
- Discover public server instances for a configured Roblox place using Roblox's public server-list endpoint.
- Print server Job IDs and player counts for manual use.
- Send a Discord webhook test message when `DISCORD_WEBHOOK_URL` is configured as an environment variable.

## Important limitation
The public server list does **not** expose live objects or event state inside each server. This scaffold does not detect Hollow Jack's grave and does not claim to scan grave spawns globally. A reliable detector needs an authorized source of confirmed spawn observations.

## Run
Requires Python 3.10+; no third-party packages are needed.

```bash
export ROBLOX_PLACE_ID="YOUR_PLACE_ID"
python server_discovery.py
```

Optional webhook test:

```bash
export DISCORD_WEBHOOK_URL="YOUR_DISCORD_WEBHOOK_URL"
python webhook_test.py
```

Keep webhook URLs private. Never commit them to GitHub.

## Files
- `server_discovery.py` — public server-list discovery only.
- `webhook_test.py` — sends a harmless test message to your own Discord webhook.
- `main.lua` and `interface.lua` — reserved Lua templates; not used by the Python scaffold yet.
