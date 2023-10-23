''' Import list '''
import os
import json
from jinja2 import Environment, FileSystemLoader
import markdown

environment = Environment(loader=FileSystemLoader("templates/"))

def get_article_list():
    ''' Return list of file paths to blog article markdown files '''
    folder_path = "./articles"
    directory_contents = os.listdir(folder_path)
    articles = [os.path.abspath(os.path.join(folder_path, file)) for file in directory_contents]
    return articles

def generate_article_data():
    '''
    Generate list of blog article data from markdown and
    it's included metadata.
    '''
    if os.path.exists("output/blog") is False:
        os.makedirs("output/blog")

    articles = get_article_list()
    template = environment.get_template("article.j2")
    return_list = []

    for article in articles:
        with open(article, mode="r", encoding="utf-8") as f:
            # Create instance of markdown class, generate content and metadata
            md = markdown.Markdown(extensions=['fenced_code', 'meta'])
            text = f.read()
            html = md.convert(text)
            return_list.append({
                "metadata": {
                    "name": os.path.basename(article).split(".")[0],
                    "date_created": md.Meta["date_created"][0],
                    "date_modified": md.Meta["date_modified"][0]
                },
                "content": template.render(article_content=html, not_root=True)
            })
    return return_list

def generate_articles(data):
    ''' Generate HTML files from parsed article data '''
    for item in data:
        with open(f"output/blog/{item['metadata']['name']}.html", mode="w", encoding="utf-8") as file:
            file.write(item['content'])

def init():
    ''' Entry point for script '''
    configuration = None
    articles = generate_article_data()
    with open("configuration.json", mode="r", encoding="utf-8") as file:
        configuration = json.load(file)
    if os.path.exists("output") is False:
        os.makedirs("output")

    for key, value in configuration["routes"].items():
        template = environment.get_template(value)
        content = ""
        if key == "blog":
            content = template.render(metadata=articles)
        elif key == "resume":
            content = template.render(resume_data=configuration["resume"], skills=configuration["skills"])
        else:
            content = template.render()
        with open(f"output/{key}.html", mode="w", encoding="utf-8") as file:
            file.write(content)
    generate_articles(articles)

if __name__ == "__main__":
    init()