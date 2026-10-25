"""List public Roblox servers for a configured place.

This only discovers public server IDs; it cannot see whether a grave or other
in-game object exists inside any server.
"""
import json
import os
import sys
import urllib.parse
import urllib.request

API = "https://games.roblox.com/v1/games/{place_id}/servers/Public"


def fetch_page(place_id: str, cursor: str | None = None) -> dict:
    params = {"sortOrder": "Asc", "limit": "100"}
    if cursor:
        params["cursor"] = cursor
    url = API.format(place_id=urllib.parse.quote(place_id)) + "?" + urllib.parse.urlencode(params)
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "HollowJackMonitor/0.1 (public server discovery)"},
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.load(response)


def main() -> int:
    place_id = os.environ.get("ROBLOX_PLACE_ID", "").strip()
    if not place_id.isdigit():
        print("Set ROBLOX_PLACE_ID to the numeric Roblox place ID.", file=sys.stderr)
        return 2

    cursor = None
    pages = 0
    total = 0
    try:
        while pages < 3:  # conservative starter limit; increase only if needed
            payload = fetch_page(place_id, cursor)
            servers = payload.get("data", [])
            for server in servers:
                job_id = server.get("id")
                playing = server.get("playing", "?")
                capacity = server.get("maxPlayers", "?")
                if job_id:
                    print(f"Job ID: {job_id} | players: {playing}/{capacity}")
                    total += 1
            pages += 1
            cursor = payload.get("nextPageCursor")
            if not cursor:
                break
        print(f"\nListed {total} public server(s) across {pages} page(s).")
        print("These results do not indicate whether Hollow Jack's grave has spawned.")
        return 0
    except Exception as exc:
        print(f"Server-list request failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
