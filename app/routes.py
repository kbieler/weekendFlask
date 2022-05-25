from app import app
import requests as r
from .templates.services import getEpisode, getImages, getChar
from flask_login import login_required
from flask import Blueprint, render_template, request, redirect, url_for, flash


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
@login_required
def schwifty():
    return render_template('schwifty.html')

@app.route('/squanch.html')
@login_required
def squanch():
    context = getChar()    
    return render_template('squanch.html', **context)

@app.route('/go.html')
@login_required
def go():
    return render_template('go.html')

@app.route('/yourself.html')
@login_required
def yourself():
    context = getEpisode()
    return render_template('yourself.html', **context)