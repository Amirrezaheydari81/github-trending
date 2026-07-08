"""
Update README
"""

from markdown import MarkdownBuilder
from sections import sections
from config import README_FILE


builder = MarkdownBuilder()

# -------------------------------------
# Header
# -------------------------------------

builder.header()

builder.intro()

builder.toc()

# -------------------------------------
# Most Starred
# -------------------------------------

builder.section("⭐ پرستاره‌ترین ریپازیتوری‌های GitHub")

for repo in sections.most_starred():
    builder.repository(repo)

builder.end_section()

# -------------------------------------
# Trending Today
# -------------------------------------

builder.section("🔥 ترند امروز")

for repo in sections.trending_today():
    builder.repository(repo)

builder.end_section()

# -------------------------------------
# Trending Week
# -------------------------------------

builder.section("📈 ترند هفته")

for repo in sections.trending_week():
    builder.repository(repo)

builder.end_section()

# -------------------------------------
# Trending Month
# -------------------------------------

builder.section("🚀 ترند ماه")

for repo in sections.trending_month():
    builder.repository(repo)

builder.end_section()

# -------------------------------------
# Hidden Gems
# -------------------------------------

builder.section("💎 Hidden Gems")

for repo in sections.hidden_gems():
    builder.repository(repo)

builder.end_section()

# -------------------------------------
# Languages
# -------------------------------------

languages = sections.languages()

for language, repos in languages.items():

    builder.section(f"🐍 {language}")

    for repo in repos:

        builder.repository(repo)

    builder.end_section()

# -------------------------------------
# Topics
# -------------------------------------

topics = sections.topics()

for topic, repos in topics.items():

    builder.section(f"🏷 {topic.upper()}")

    for repo in repos:

        builder.repository(repo)

    builder.end_section()

# -------------------------------------
# Footer
# -------------------------------------

builder.footer()

# -------------------------------------
# Save
# -------------------------------------

with open(
    README_FILE,
    "w",
    encoding="utf-8"
) as f:

    f.write(builder.build())

print("README updated successfully ✅")