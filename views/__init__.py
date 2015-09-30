from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.haml')


@app.route('/about')
def about():
    return render_template('about.haml')


@app.route('/skills')
def skills():
    return render_template('skills.haml')


@app.route('/work')
def work():
    return render_template('work.haml')


@app.route('/education')
def education():
    return render_template('education.haml')


@app.route('/contact')
def contact():
    return render_template('contact.haml')
