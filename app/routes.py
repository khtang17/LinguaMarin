from app import app

from flask import render_template, request, url_for, redirect, flash


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/children')
def children():
    return render_template("children.html")

@app.route('/adults')
def adults():
    return render_template("adults.html")

@app.route('/resources')
def resources():
    return render_template("resources.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/job')
def job():
    return render_template("job.html")



