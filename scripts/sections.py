"""
README Sections
"""

from github import github
from config import (
    TOP_REPOSITORIES,
    LANGUAGES,
    TOPICS
)


class Sections:

    # --------------------------
    # Main Sections
    # --------------------------

    def most_starred(self):
        return github.most_starred(TOP_REPOSITORIES)

    def trending_today(self):
        return github.trending_today(TOP_REPOSITORIES)

    def trending_week(self):
        return github.trending_week(TOP_REPOSITORIES)

    def trending_month(self):
        return github.trending_month(TOP_REPOSITORIES)

    def hidden_gems(self):
        return github.hidden_gems(TOP_REPOSITORIES)

    def latest_updated(self):
        return github.latest_updated(TOP_REPOSITORIES)

    def most_forked(self):
        return github.most_forked(TOP_REPOSITORIES)

    def awesome_lists(self):
        return github.awesome_lists(TOP_REPOSITORIES)

    # --------------------------
    # Languages
    # --------------------------

    def languages(self):

        data = {}

        for language in LANGUAGES:

            data[language] = github.language(
                language,
                limit=10
            )

        return data

    # --------------------------
    # Topics
    # --------------------------

    def topics(self):

        data = {}

        for topic in TOPICS:

            data[topic] = github.topic(
                topic,
                limit=10
            )

        return data

    # --------------------------
    # Dashboard
    # --------------------------

    def dashboard(self):

        return {
            "most_starred": len(self.most_starred()),
            "today": len(self.trending_today()),
            "week": len(self.trending_week()),
            "month": len(self.trending_month()),
            "languages": len(LANGUAGES),
            "topics": len(TOPICS)
        }


sections = Sections()