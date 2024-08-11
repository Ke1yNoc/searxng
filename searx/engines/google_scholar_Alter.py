import requests
import json
from dateutil import parser

headers = {
    'X-API-KEY': '543783e821c757e49a6bb042bb88c3fe9931af9e',
    'Content-Type': 'application/json'
}

url = "https://google.serper.dev/scholar"

params = {
    'url': url,
    'headers': headers
}

def request(query, params):
    payload = json.dumps({
        "q": query
    })
    params['payload'] = payload
    return params

def response(resp):
    results = []
    try:
        data = resp.json()
        docs = data.get('organic', [])

        for current in docs:
            item = {}
            item['title'] = current.get('title')
            item['url'] = current.get('link')
            item['publicationInfo'] = current.get('publicationInfo')
            item['snippet'] = current.get('snippet')
            item['publishedDate'] = parser.parse(f"{current.get('year')}-01-01") if current.get('year') else None
            item['citedBy'] = current.get('citedBy', 0)

            results.append(item)
    except json.JSONDecodeError as e:
        print("Failed to decode JSON response:", e)
        print("Response content:", resp.text)

    return results