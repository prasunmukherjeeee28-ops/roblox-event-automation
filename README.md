# Hollow Jack Monitor — research scaffold

A small, phone-friendly Python project for researching Roblox public-server discovery and Discord notifications.

## What works now
- Lists public server IDs and player counts for a Roblox place.
- Sends a harmless test message to a Discord webhook you control.
- Keeps secrets out of source code by reading the webhook URL from an environment variable.

## What does not work yet
This project **does not detect Hollow Jack's grave**. Roblox's public server-list endpoint returns server metadata; it does not expose live objects or event state inside each server. Listing Job IDs is not proof that the grave has spawned.

A real cross-server notifier needs a reliable, authorized source of confirmed spawn observations. Do not treat a server as a hit unless the spawn is actually verified.

## Files
- `server_discovery.py` — lists public servers for a configured place.
- `webhook_test.py` — tests delivery to your own Discord webhook.
- `config.example.json` — non-secret example configuration.
- `.gitignore` — avoids committing local secrets and Python cache files.

## Setup
Python 3.10+ is required. No third-party packages are needed.

Set your place ID as an environment variable:

```bash
export ROBLOX_PLACE_ID="YOUR_NUMERIC_PLACE_ID"
python server_discovery.py
```

To test a Discord webhook, set its URL only in your local environment:

```bash
export DISCORD_WEBHOOK_URL="YOUR_DISCORD_WEBHOOK_URL"
python webhook_test.py
```

Never paste a real webhook URL into source code, screenshots, issues, or commits. If one is exposed, delete/regenerate it in Discord.

## Next development milestone
Find and verify an authorized, dependable source of grave-spawn observations before implementing any event alerting. Until then, this repository intentionally reports server discovery only.
