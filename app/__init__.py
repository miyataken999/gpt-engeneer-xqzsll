from flask import Flask
from app.views.home import home

app = Flask(__name__)

app.add_url_rule("/", view_func=home)