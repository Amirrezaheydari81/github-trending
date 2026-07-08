
from github import github_search


def most_starred():

    repos = github_search(
        "stars:>50000"
    )

    return repos



def trending_today():

    repos = github_search(
        "created:>2026-07-07",
        sort="stars"
    )

    return repos



def trending_week():

    repos = github_search(
        "pushed:>2026-07-01",
        sort="stars"
    )

    return repos



def trending_month():

    repos = github_search(
        "created:>2026-06-01",
        sort="stars"
    )

    return repos



def hidden_gems():

    repos = github_search(
        "stars:1000..10000",
        sort="stars"
    )

    return repos