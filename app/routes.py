from app import app

from flask import render_template, request, url_for, redirect, flash

#English - default routes
@app.route('/')
@app.route('/home')
def home():
    return render_template("en/home.html")

@app.route('/children')
def children():
    return render_template("en/children.html")

@app.route('/adults')
def adults():
    return render_template("en/adults.html")

@app.route('/resources')
def resources():
    return render_template("en/resources.html")

@app.route('/contact')
def contact():
    return render_template("en/contact.html")

@app.route('/job')
def job():
    return render_template("en/job.html")

@app.route('/whygerman')
def whygerman():
    return render_template("en/whygerman.html")

@app.route('/aboutus')
def aboutus():
    return render_template("en/aboutus.html")



#German routes
@app.route('/home/de')
def home_de():
    return render_template("german/home_de.html")

@app.route('/children/de')
def children_de():
    return render_template("german/children_de.html")

@app.route('/adults/de')
def adults_de():
    return render_template("german/adults_de.html")

@app.route('/resources/de')
def resources_de():
    return render_template("german/resources_de.html")

@app.route('/contact/de')
def contact_de():
    return render_template("german/contact_de.html")

@app.route('/job/de')
def job_de():
    return render_template("german/job_de.html")

@app.route('/whygerman/de')
def whygerman_de():
    return render_template("german/whygerman_de.html")

@app.route('/aboutus/de')
def aboutus_de():
    return render_template("german/aboutus_de.html")


#French routes
@app.route('/home/fr')
def home_fr():
    return render_template("french/home_fr.html")

@app.route('/children/fr')
def children_fr():
    return render_template("french/children_fr.html")

@app.route('/adults/fr')
def adults_fr():
    return render_template("french/adults_fr.html")

@app.route('/resources/fr')
def resources_fr():
    return render_template("french/resources_fr.html")

@app.route('/contact/fr')
def contact_fr():
    return render_template("french/contact_fr.html")

@app.route('/job/fr')
def job_fr():
    return render_template("french/job_fr.html")

@app.route('/whygerman/fr')
def whygerman_fr():
    return render_template("french/whygerman_fr.html")

@app.route('/aboutus/fr')
def aboutus_fr():
    return render_template("french/aboutus_fr.html")