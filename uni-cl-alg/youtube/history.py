import json

history_detailed = {}
with open("history_detailed.json", "r") as f:
    history_detailed = json.load(f)

history = {
    "columns": [
        "comment_count",
        "duration",
        "view_count",
        "timestamp",
        "like_count",
        "channel",
        "channel_follower_count"
    ]
}
history["index"] = list(history_detailed.keys())
history["data"] = list(history_detailed.values())

with open("history.json", "w") as f:
    json.dump(history, f, indent=2)

