# -*- coding: utf-8 -*-
from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Database config and connection
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)


class Plane(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    body = db.Column(db.Text)
    image_url = db.Column(db.String(255))


# seed_planes = [
#         Plane({'title': 'Lockheed C-5 Galaxy', 'body': 'As the Air Force’s largest and only strategic airlifter, the C-5 Galaxy can carry more cargo farther distances than any other aircraft. With a payload of six Mine Resistant Ambush Protected vehicles (MRAPs) or up to five helicopters, the C-5 can haul twice as much cargo as any other airlifter.', 'image_url': 'http://www.lockheedmartin.com/content/dam/lockheed/data/aero/photos/c-5/C5%20Homepage%201.jpg'}),
#         Plane({'title': 'Airbus A340', 'body': 'The Airbus A340 is a long-range, four-engine, wide-body commercial passenger jet airliner developed and produced by the European aerospace company Airbus. The A340 was assembled in Toulouse, France.', 'image_url': ''}),
#         Plane({'title': 'Boeing C-17 Globemaster', 'body': 'A high-wing, four-engine, T-tailed military transport aircraft, the multi-service C-17 can carry large equipment, supplies and troops directly to small airfields in harsh terrain anywhere in the world. The massive, sturdy, long-haul aircraft tackles distance, destination and heavy, oversized payloads in unpredictable conditions. It has delivered cargo in every worldwide operation since the 1990s. Boeing builds and maintains the aircraft for nine countries worldwide.', 'image_url': 'http://www.boeing.com/resources/boeingdotcom/defense/c-17_globemaster_iii/images/c_17_hero_lrg_01_1280x720.jpg'})
# ]

# db.session.bulk_save_objects(seed_planes)

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

        return redirect('/jets')


@app.route('/jets', methods=['GET'])
def show_planes():
    planes = Plane.query.all()
    return render_template('planes.html', planes = planes)


@app.route('/delete/<int:id>', methods=['POST'])
def delete_plane(id):
    if request.method == 'POST':
        plane = Plane.query.filter_by(id=id).first()
        print plane
        db.session.delete(plane)
        db.session.commit()
        return redirect('/jets')


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_plane(id):
    if request.method == 'GET':
        plane = Plane.query.filter_by(id=id).first()
        return render_template('edit_plane.html', plane = plane)
    else:
        plane = Plane.query.filter_by(id=id).first()
        plane.title = request.form['title']
        plane.body = request.form['body']
        plane.image_url = request.form['image_url']
        db.session.commit()

        return redirect('/jets')


if __name__ == "__main__":
    app.run(debug=True)
