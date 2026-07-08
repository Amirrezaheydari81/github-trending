import os
import requests

TOKEN = os.getenv("GH_TOKEN")

def github_search(query, sort="stars", order="desc", limit=10):
    url = "https://api.github.com/search/repositories"

    headers = {
        "Accept": "application/vnd.github+json"
    }

    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"

    params = {
        "q": query,
        "sort": sort,
        "order": order,
        "per_page": limit
    }

    response = requests.get(url, headers=headers, params=params)

    print("Status:", response.status_code)
    print("Response:", response.text)

    response.raise_for_status()

    data = response.json()

    return data.get("items", [])
