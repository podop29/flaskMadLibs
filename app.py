from flask import Flask, request, render_template
from stories import *


app = Flask(__name__)


@app.route('/')
def home():
    prompt = story.prompts
    return render_template('home.html', prompts = prompt)


@app.route('/story')
def showStory():
    text = story.generate(request.args)
    return render_template('story.html', text=text)

