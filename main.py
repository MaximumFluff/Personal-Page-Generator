""" Import list """
import json
import os
from datetime import datetime

import markdown
from jinja2 import Environment, FileSystemLoader

environment = Environment(loader=FileSystemLoader("templates/"))


def init():
    """Entry point for script, render the base routes"""
    configuration = import_json()
    articles = generate_article_data()

    for key, value in configuration["routes"].items():
        template = environment.get_template(value)
        content = ""
        if key == "blog":
            content = template.render(metadata=articles)
        elif key == "resume":
            content = template.render(
                resume_data=configuration["resume"], skills=configuration["skills"]
            )
        else:
            content = template.render()
        with open(f"public/{key}.html", mode="w", encoding="utf-8") as file:
            file.write(content)
    generate_articles(articles)


def get_article_list():
    """Return list of file paths to blog article markdown files"""
    folder_path = "./articles"
    directory_contents = os.listdir(folder_path)
    return [
        os.path.abspath(os.path.join(folder_path, file)) for file in directory_contents
    ]


def generate_article_data():
    """
    Generate list of blog article data from markdown and included metadata
    """
    articles = get_article_list()
    template = environment.get_template("article.j2")
    return_list = []

    for article in articles:
        with open(article, mode="r", encoding="utf-8") as file:
            # Create instance of markdown class, generate content and metadata
            md = markdown.Markdown(extensions=["codehilite", "fenced_code", "meta"])
            text = file.read()
            html = md.convert(text)
            return_list.append(
                {
                    "file_name": os.path.basename(article).split(".")[0],
                    "article_name": md.Meta["article_name"][0],  # type: ignore
                    "date_created": md.Meta["date_created"][0],  # type: ignore
                    "content": template.render(
                        article_name=md.Meta["article_name"][0],  # type: ignore
                        date_created=md.Meta["date_created"][0],  # type: ignore
                        date_modified=md.Meta.get("date_modified")[0]  # type: ignore
                        if md.Meta.get("date_modified")  # type: ignore
                        else "",
                        article_content=html,
                        not_root=True,
                    ),
                }
            )
    # Sort list by article creation date from latest to oldest
    return sorted(
        return_list,
        key=lambda x: datetime.strptime(x["date_created"], "%d/%m/%Y"),
        reverse=True,
    )


def generate_articles(data):
    """Generate HTML files from parsed article data"""
    for item in data:
        with open(
            f"public/blog/{item['file_name']}.html", mode="w", encoding="utf-8"
        ) as file:
            file.write(item["content"])


def import_json():
    """Import and parse JSON data configuration file"""
    with open("configuration.json", mode="r", encoding="utf-8") as file:
        return json.load(file)


if __name__ == "__main__":
    init()
