from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from jinja2 import Template
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)

class Plane(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    body = db.Column(db.Text)
    image_url = db.Column(db.String(255))

    def __repr__(self):
        return self.title

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/jets/add', methods=['GET', 'POST'])

def create_plane():
    if request.method == 'GET':
        return render_template('add_plane.html')
    else:
        title = request.form['title']
        body = request.form['body']
        image_url = request.form['image_url']

        plane = Plane(title=title, body=body, image_url=image_url)

        db.session.add(plane)
        db.session.commit()

        return redirect('/')

def delete_plane():
    db.session.delete(plane)
    db.session.commit()
    return redirect('/')

@app.route('/jets', methods=['GET'])
def show_planes():
    planes = Plane.query.all()
    return render_template('planes.html', planes = planes)

if __name__ == "__main__":
    app.run(debug=True)
