from jinja2 import Environment, FileSystemLoader
from datetime import datetime
import os
import markdown

environment = Environment(loader=FileSystemLoader("templates/"))

# Main route configuration
configuration = {
    "index": "index.j2",
    "resume": "resume.j2",
    "blog": "blog.j2",
}

def retrieve_metadata():
    folder_path = "./articles"
    directory_contents = os.listdir(folder_path)
    metadata = []

    for file in directory_contents:
        article_path = os.path.abspath(os.path.join(folder_path, file))
        metadata.append({
            "name": os.path.splitext(file)[0],
            "date_created": datetime.fromtimestamp(os.path.getctime(article_path)).strftime("%d/%m/%Y"),
            "date_modified": datetime.fromtimestamp(os.path.getmtime(article_path)).strftime("%d/%m/%Y")
        })
    
    return metadata

def generate_articles(metadata):
    print("Generating blog and articles...")
    if os.path.exists("output/blog") is False:
        os.makedirs("output/blog")
        print("Blog folder generated...")

    template = environment.get_template("article.j2")

    for article in metadata:
        html = ''

        with open(f"articles/{article['name']}.md", 'r') as f:
            text = f.read()
            html = markdown.markdown(text)
            print(f"{html}")

        content = template.render(article_content=html, not_root=True)

        with open(f"output/blog/{article['name']}.html", mode="w", encoding="utf-8") as file:
            file.write(content)
            print(f"{article['name']}.html generated...")

    print("Articles generated...")


def init():
    print("Generating static site...")
    if os.path.exists("output") is False:
        os.makedirs("output")
        print("Output folder generated...")

    metadata = retrieve_metadata()

    for key, value in configuration.items():
        template = environment.get_template(value)
        content = ""
        if key == "blog":
            content = template.render(metadata=metadata)
        else:
            content = template.render()
        with open(f"output/{key}.html", mode="w", encoding="utf-8") as file:
            file.write(content)
            print(f"{key}.html generated...")
        
    generate_articles(metadata)

if __name__ == "__main__":
    init()