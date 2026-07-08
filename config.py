"""
GitHub Trending Config
"""

from datetime import datetime, timedelta

# تعداد پروژه‌های هر بخش
TOP_REPOSITORIES = 20

# حداقل ستاره برای Most Starred
MIN_STARS = 50000

# Hidden Gems
HIDDEN_GEMS_MIN = 500
HIDDEN_GEMS_MAX = 5000

# زبان‌ها
LANGUAGES = [
    "Python",
    "JavaScript",
    "TypeScript",
    "Go",
    "Rust",
    "PHP",
    "Java",
    "C++",
    "C#",
    "Swift",
    "Kotlin",
    "Dart",
]

# دسته‌بندی‌ها (GitHub Topics)
TOPICS = [
    "ai",
    "llm",
    "react",
    "vue",
    "angular",
    "nextjs",
    "nodejs",
    "docker",
    "kubernetes",
    "flutter",
    "security",
    "linux",
    "devops",
    "automation",
]

TODAY = datetime.utcnow()

YESTERDAY = TODAY - timedelta(days=1)

LAST_WEEK = TODAY - timedelta(days=7)

LAST_MONTH = TODAY - timedelta(days=30)

DATE_FORMAT = "%Y-%m-%d"

README_FILE = "README.md"