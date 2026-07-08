from sections import *


def markdown(title, repos):

    text = f"\n## {title}\n\n"

    text += "| Repository | Stars | Language |\n"
    text += "|---|---|---|\n"


    for repo in repos:

        text += (
            f"| [{repo['full_name']}]"
            f"({repo['html_url']}) "
            f"| ⭐ {repo['stargazers_count']} "
            f"| {repo['language']} |\n"
        )

    return text



content = """

# GitHub Repository Explorer

Updated Daily 🚀

"""


content += markdown(
    "⭐ Most Starred",
    most_starred()
)


content += markdown(
    "🔥 Trending Today",
    trending_today()
)


content += markdown(
    "📈 Trending This Week",
    trending_week()
)


content += markdown(
    "🚀 Trending This Month",
    trending_month()
)


content += markdown(
    "💎 Hidden Gems",
    hidden_gems()
)



with open(
    "README.md",
    "w",
    encoding="utf8"
) as f:

    f.write(content)


print("README Updated")