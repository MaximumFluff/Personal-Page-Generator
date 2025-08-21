# Personal Page

This is a personal project to create my own simple blog utilizing Python and Markdown as a simple static site generator.

Code is linted and formatted using Ruff.

## How to run

This project is configured using the `uv` package manager for python

* Install `uv` from [here](https://docs.astral.sh/uv/)

* Inside the project folder, run `uv run main.py` in the terminal

## Folder structure

|Folder|Description|
|----|----|
|/output|Contains images and the generated HTML files|
|/templates|Contains Jinja2 template files|
|/articles|Contains markdown files for blog posts|

## Libraries used

- Jinja2
- Python Markdown

## TODO

- [ ] Reconfigure configuration.json to markdown files instead?
- [x] Handle missing metadata params in markdown files
- [x] Export all configuration variables to JSON files
- [x] Create function for generating configuration information from JSON
- [x] Clean up code, organize functions better for readability
- [x] Add configuration data for CSS values to facilitate easy theme changes
- [x] Change logic for created_by, updated_by for articles (Markdown metadata?)
- [ ] Type annotations?
- [ ] Fix folder structure
