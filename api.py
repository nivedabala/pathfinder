from flask import Flask, request, render_template, redirect, url_for
import csv
import os

PICTURE_FOLDER = os.path.join('static', 'picture_photo')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PICTURE_FOLDER

#from pathplanner import Session

# @app.route('/', methods=['GET'])
# def api():
# return {
# 'userId':1,
# 'title': 'Flask React Application',
# 'completed': False
# }
@app.route('/')
def home():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'download.png')
    return render_template("home.html", user_image = full_filename)


@app.route("/questions", methods=['GET', 'POST'])
def questions():
    if request.method == 'POST':
        return redirect(url_for('home'))

    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'download.png')
    return render_template('questions.html', user_image = full_filename)


@app.route("/display", methods=['GET', 'POST'])
def display():
    
    if request.method == 'POST':
        distance = request.form['distance']
        sights = request.form.getlist('sight')
        #something = Session(sights, distance).main()


    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'download.png')
    return render_template('display.html', user_image = full_filename, distance = distance, sights=sights)


if __name__ == '__main__':
    app.run(debug=True, host='localhost',port=5001)
