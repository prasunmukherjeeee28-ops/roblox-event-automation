"""Send a harmless test message to your own Discord webhook."""
import json
import os
import sys
import urllib.request


def main() -> int:
    url = os.environ.get("DISCORD_WEBHOOK_URL", "").strip()
    if not url.startswith("https://discord.com/api/webhooks/") and not url.startswith("https://discordapp.com/api/webhooks/"):
        print("Set DISCORD_WEBHOOK_URL to your own Discord webhook URL.", file=sys.stderr)
        return 2

    body = json.dumps({
        "content": "✅ Hollow Jack Monitor webhook test — notifications are connected."
    }).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=body,
        headers={"Content-Type": "application/json", "User-Agent": "HollowJackMonitor/0.1"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            if response.status in (200, 204):
                print("Webhook test delivered.")
                return 0
            print(f"Unexpected response: HTTP {response.status}", file=sys.stderr)
            return 1
    except Exception as exc:
        print(f"Webhook test failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
