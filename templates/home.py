import os


def home():
    home_template = open(f"{os.getcwd()}/templates/html/home.html")
    html_template = home_template.read()
    home_template.close()
    return html_template
