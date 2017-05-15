from jinja2 import Environment, FileSystemLoader, select_autoescape
import os
import shutil
import json


print("Starting Build Process...")
env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

if os.path.exists("options.json"):
    options_file = open("options.json", "r")
    options = json.load(options_file)
else:
    options = {}

# recreate output folder
try:
    shutil.rmtree("output")
except:
    pass

os.mkdir("output")

# copy assets
shutil.copytree("assets", "output")
shutil.copytree("extra", "output")

index_template = env.get_template("index.html")
rendered = index_template.render(options)
output_index = open("output/index.html", "w")
output_index.write(rendered)
output_index.close()
print("Build Done.")
