"""
GitHub API Client
"""

from datetime import datetime, timedelta
import os
import time
import requests

BASE_URL = "https://api.github.com"

TOKEN = os.getenv("GH_TOKEN")

HEADERS = {
    "Accept": "application/vnd.github+json",
    "User-Agent": "GitHub-Trending-Bot/1.0"
}

if TOKEN:
    HEADERS["Authorization"] = f"Bearer {TOKEN}"


class GitHub:

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(HEADERS)

    # -----------------------------

    def _request(self, endpoint, params=None):

        url = f"{BASE_URL}/{endpoint}"

        for attempt in range(3):

            try:

                response = self.session.get(
                    url,
                    params=params,
                    timeout=30
                )

                # Rate Limit
                if response.status_code == 403:

                    remain = response.headers.get(
                        "X-RateLimit-Remaining"
                    )

                    if remain == "0":

                        reset = int(
                            response.headers.get(
                                "X-RateLimit-Reset",
                                time.time() + 60
                            )
                        )

                        sleep = reset - int(time.time()) + 5

                        print(
                            f"Rate limit reached. Waiting {sleep}s..."
                        )

                        time.sleep(max(sleep, 5))

                        continue

                response.raise_for_status()

                return response.json()

            except requests.RequestException as e:

                print(e)

                time.sleep(2)

        return {}

    # -----------------------------

    def search(
        self,
        query,
        sort="stars",
        order="desc",
        limit=20
    ):

        data = self._request(
            "search/repositories",
            {
                "q": query,
                "sort": sort,
                "order": order,
                "per_page": limit
            }
        )

        return data.get("items", [])

    # -----------------------------

    def repository(self, full_name):

        return self._request(
            f"repos/{full_name}"
        )

    # -----------------------------

    def language(self, language, limit=20):

        return self.search(
            f"language:{language}",
            limit=limit
        )

    # -----------------------------

    def topic(self, topic, limit=20):

        return self.search(
            f"topic:{topic}",
            limit=limit
        )

    # -----------------------------

    def most_starred(self, limit=20):

        return self.search(
            "stars:>50000",
            limit=limit
        )

    # -----------------------------

    def trending_today(self, limit=20):

        today = (
            datetime.utcnow() -
            timedelta(days=1)
        ).strftime("%Y-%m-%d")

        return self.search(
            f"created:>{today}",
            limit=limit
        )

    # -----------------------------

    def trending_week(self, limit=20):

        week = (
            datetime.utcnow() -
            timedelta(days=7)
        ).strftime("%Y-%m-%d")

        return self.search(
            f"created:>{week}",
            limit=limit
        )

    # -----------------------------

    def trending_month(self, limit=20):

        month = (
            datetime.utcnow() -
            timedelta(days=30)
        ).strftime("%Y-%m-%d")

        return self.search(
            f"created:>{month}",
            limit=limit
        )

    # -----------------------------

    def hidden_gems(self, limit=20):

        return self.search(
            "stars:500..5000",
            limit=limit
        )

    # -----------------------------

    def latest_updated(self, limit=20):

        return self.search(
            "stars:>100",
            sort="updated",
            limit=limit
        )

    # -----------------------------

    def most_forked(self, limit=20):

        return self.search(
            "forks:>1000",
            sort="forks",
            limit=limit
        )

    # -----------------------------

    def awesome_lists(self, limit=20):

        return self.search(
            "awesome in:name",
            limit=limit
        )


github = GitHub()