import json

liked_fetched = {}
with open("liked_fetched.json", "r") as f:
    liked_fetched = json.load(f)

liked = {
    "columns": [
        "title",
        "videoOwnerChannelTitle"
    ],
    "index": [],
    "data": []
}

for item in liked_fetched["items"]:
    snippet = item["snippet"]
    id = snippet["resourceId"]["videoId"]
    try:
        title = snippet["title"]
        channel = snippet["videoOwnerChannelTitle"]
        liked["data"].append([title, channel])
    except:
        liked["data"].append(["", ""])
    liked["index"].append(id)

with open("liked.json", "w") as f:
    json.dump(liked, f, indent=2)

