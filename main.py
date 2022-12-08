from jinja2 import Environment, FileSystemLoader
import os

print("Generating static site...")

configuration = {
    "index": "index.j2",
    "resume": "resume.j2",
    "blog": "blog.j2",
}

if os.path.exists("output") is False:
    print("output folder generated")
    os.makedirs("output")

environment = Environment(loader=FileSystemLoader("templates/"))

for key, value in configuration.items():
    print("key", key)
    print("Value", value)
    template = environment.get_template(value)
    content = template.render()
    with open(f"output/{key}.html", mode="w", encoding="utf-8") as file:
        file.write(content)
        print("File created!")
print("Static site generated!")
