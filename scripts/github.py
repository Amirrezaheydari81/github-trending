import requests
import os

TOKEN = os.getenv("GH_TOKEN")


def github_search(query, sort="stars", order="desc", limit=10):

    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }

    params = {
        "q": query,
        "sort": sort,
        "order": order,
        "per_page": limit
    }

    url = "https://api.github.com/search/repositories"

    response = requests.get(
        url,
        headers=headers,
        params=params
    )

    return response.json()["items"]