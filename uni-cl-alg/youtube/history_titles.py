import json
import requests

history = {}
with open('history.json', 'r') as f:
    history = json.load(f)

id_index = {}
for i in range(len(history['index'])):
    id_index[history['index'][i]] = i

video_ids = ','.join(history['index'])
url = f'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_ids}&key={api_key}'

response = requests.get(url)

data = response.json()

print(data)

for item in data['items']:
    index = id_index[item['id']]
    history['data'][index][0].append(item['snippet']['title'])

history['columns'].append('title')

with open('history.json', 'w') as f:
    json.dump(history, f)
