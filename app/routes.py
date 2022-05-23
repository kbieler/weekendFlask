from app import app
from flask import render_template
import requests as r
from .templates.services import getEpisode, getImages, getChar


@app.route('/')
def home():
    challenge = 'Can a Foxes-90 cohort use Flask, API calls, and still remember HTML/CSS?'
    return render_template('index.html', challenge=challenge)

@app.route('/ricks')
def ricks():
    context = getEpisode()
    return render_template('ricks.html', **context)
   
@app.route('/about')
def about():
    contexts = getImages()
    return render_template('about.html', **contexts) 

@app.route('/schwifty')
def schwifty():
    return render_template('schwifty.html')

@app.route('/squanch.html')
def squanch():
    context = getChar()
    return render_template('squanch.html', **context)

@app.route('/go.html')
def go():
    return render_template('go.html')

@app.route('/yourself.html')
def yourself():
    context = getEpisode()
    return render_template('yourself.html', **context)