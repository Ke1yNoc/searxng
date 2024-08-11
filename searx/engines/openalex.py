import requests
from dateutil import parser
from json import loads
from urllib.parse import quote

# About information
about = {
    "website": 'https://openalex.org/',
    "wikidata_id": None,
    "official_api_documentation": 'https://docs.openalex.org/',
    "use_official_api": True,
    "require_api_key": False,
    "results": 'JSON',
}

# Base URL and search path
base_url = 'https://api.openalex.org/works'
search_string = '?search={query}'

def request(query, params):
    search_path = search_string.format(
        query=quote(query),
    )
    params['url'] = base_url + search_path
    return params

def response(resp):
    results = []
    data = resp.json()  # Directly use the JSON method of the response object
    docs = data.get('results', [])

    for current in docs:
        item = {}
        item['url'] = current.get('id')
        item['title'] = current.get('title')
        item['authors'] = [author['display_name'] for author in current.get('authors', [])]
        item['publishedDate'] = parser.parse(current.get('publication_date'))
        item['abstract'] = current.get('abstract', '')

        results.append(item)

    return results
