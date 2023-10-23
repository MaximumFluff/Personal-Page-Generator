from jinja2 import Environment, FileSystemLoader
from datetime import datetime
import os
import markdown

environment = Environment(loader=FileSystemLoader("templates/"))

# Skills config
skills = [
    "HTML",
    "CSS",
    "JavaScript",
    "TypeScript",
    "Node.js",
    "Express.js",
    "React.js",
    "React Native",
    "Redux",
    "SQL",
    "Python",
    "Heroku",
    "Markdown"
]

# Main route configuration
configuration = {
    "index": "index.j2",
    "resume": "resume.j2",
    "blog": "blog.j2",
}

# Resume configuration
resume = [
    {
        "company": "Kesko",
        "location": "Helsinki, FIN",
        "time": "May 2023 - Present",
        "title": "Full Stack Developer",
        "image_url": "images/kesko.jpg",
        "image_alt": "Kesko logo",
        "description": "Working as part of Team Sweden I help improve and maintain K-Rauta.se"
    },
    {
        "company": "eMabler",
        "location": "Helsinki, FIN",
        "time": "February 2022 - April 2023",
        "title": "Software Developer",
        "image_url": "images/emabler.jpg",
        "image_alt": "eMabler logo",
        "description": "For all product UI's I maintained, implemented redesigns and added new features based on customer feedback.\n\nI also worked on bugfixes for both ends of the stack, new features for the C# backend and creating internal documentation for new features and architecture choices"
    },
    {
        "company": "Veikkaus",
        "location": "Helsinki, FIN",
        "time": "September 2019 - February 2022",
        "title": "Junior Developer",
        "image_url": "images/veikkaus.jpg",
        "image_alt": "Veikkaus logo",
        "description": "Worked in the front-end team working on re-implementing the app in React Native. Responsibilities included implementing redesigns of the UI and creating native versions of various games based on their web counterparts."
    },
    {
        "company": "Industry62",
        "location": "Helsinki, FIN",
        "time": "January 2019 - May 2019",
        "title": "Software Developer",
        "image_url": "images/industry62.jpg",
        "image_alt": "Industry62 logo",
        "description": "As part of Industry62 my main task involved front-end programming work for a pair of React Native mobile apps designed to deliver digital health services for pregnant women in Africa.\n\nYou can read more about the project here: https://www.industry62.com/case-stories/2019/5/8/myhealthhand"
    }
]

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
            html = markdown.markdown(text, extensions=['fenced_code'])

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
        elif key == "resume":
            content = template.render(resume_data=resume, skills=skills)
        else:
            content = template.render()
        with open(f"output/{key}.html", mode="w", encoding="utf-8") as file:
            file.write(content)
            print(f"{key}.html generated...")
        
    generate_articles(metadata)

if __name__ == "__main__":
    init()