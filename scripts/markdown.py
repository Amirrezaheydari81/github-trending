"""
Markdown Generator
"""

from datetime import datetime


class MarkdownBuilder:

    def __init__(self):
        self.lines = []

    # --------------------------
    # Helpers
    # --------------------------

    def add(self, text=""):
        self.lines.append(text)

    def hr(self):
        self.lines.append("---")

    def h1(self, text):
        self.lines.append(f"# {text}")

    def h2(self, text):
        self.lines.append(f"## {text}")

    def h3(self, text):
        self.lines.append(f"### {text}")

    # --------------------------
    # Header
    # --------------------------

    def header(self):

        self.h1("🚀 گیت‌هاب ترند | GitHub Trending Repositories")

        self.add()

        self.add("> بزرگ‌ترین آرشیو خودکار ریپازیتوری‌های محبوب GitHub")
        self.add("> ")
        self.add("> ⭐ بروزرسانی خودکار")
        self.add("> 🔥 ترندهای امروز، هفته و ماه")
        self.add("> 🤖 هوش مصنوعی، Python، React، Docker و ...")

        self.add()

        self.add("آخرین بروزرسانی:")

        self.add(
            f"**{datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}**"
        )

        self.hr()

    # --------------------------
    # Introduction
    # --------------------------

    def intro(self):

        self.h2("درباره پروژه")

        self.add()

        self.add(
            "این مخزن هر روز به‌صورت خودکار محبوب‌ترین "
            "ریپازیتوری‌های GitHub را جمع‌آوری می‌کند."
        )

        self.add()

        self.add(
            "اگر به دنبال پروژه‌های متن‌باز، "
            "هوش مصنوعی، توسعه وب، DevOps، "
            "Python، React، Docker و سایر تکنولوژی‌ها هستید، "
            "این صفحه هر روز بروزرسانی می‌شود."
        )

        self.hr()

    # --------------------------
    # TOC
    # --------------------------

    def toc(self):

        self.h2("فهرست")

        items = [
            "⭐ پرستاره‌ترین پروژه‌ها",
            "🔥 ترند امروز",
            "📈 ترند هفته",
            "🚀 ترند ماه",
            "💎 Hidden Gems",
            "🐍 Python",
            "⚛ React",
            "🟨 JavaScript",
            "🔷 TypeScript",
            "🐳 Docker",
            "🤖 AI"
        ]

        self.add()

        for item in items:
            self.add(f"- {item}")

        self.hr()

    # --------------------------
    # Section
    # --------------------------

    def section(self, title):

        self.h2(title)

        self.add()

        self.add("| پروژه | ⭐ | زبان |")

        self.add("|-------|------|------|")

    # --------------------------
    # Repository
    # --------------------------

    def repository(self, repo):

        language = repo["language"] or "-"

        self.add(
            f"| "
            f"[{repo['full_name']}]({repo['html_url']}) "
            f"| ⭐ {repo['stargazers_count']} "
            f"| {language} |"
        )

    # --------------------------
    # End Section
    # --------------------------

    def end_section(self):

        self.add()

        self.hr()

    # --------------------------
    # Footer
    # --------------------------

    def footer(self):

        self.h2("درباره این پروژه")

        self.add()

        self.add(
            "این ریپازیتوری توسط GitHub Actions "
            "به صورت خودکار بروزرسانی می‌شود."
        )

        self.add()

        self.add(
            "تمام اطلاعات از GitHub API دریافت می‌شوند."
        )

        self.add()

        self.hr()

        self.add(
            "⭐ اگر این پروژه برایتان مفید بود، "
            "فراموش نکنید به آن Star بدهید."
        )

    # --------------------------
    # Build
    # --------------------------

    def build(self):

        return "\n".join(self.lines)