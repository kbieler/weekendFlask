from app import app
from flask import render_template
import requests as r
from .templates.services import getEpisode


@app.route('/')
def home():
    challenge = 'Can a Foxes-90 cohort use Flask, API calls, and still remember HTML/CSS?'
    return render_template('index.html', challenge=challenge)

@app.route('/ricks')
def ricks():
    context = getEpisode()
    return render_template('ricks.html', **context)
   