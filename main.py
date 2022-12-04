import jinja2

print("This is a test of python!")

environment = jinja2.Environment()
template = environment.from_string("Hello, {{ name }}!")
test = template.render(name="World")
print(test)
