from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import json
from datetime import datetime
from portfolio import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
<<<<<<< HEAD
    password = db.Column(db.String(100), nullable=False)

    def __str__(self):
        return f"User('{self.username}', '{self.email}', '{self.password}', '{self.image_file}')"
=======
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(20), nullable=False)

    def __str__(self):
        return f"User('{self.username}', '{self.email}', '{self.password}')"

class Rider(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contact_number = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    vehicle_type = db.Column(db.String(50), nullable=False)
    vehicle_registration = db.Column(db.String(50), unique=True, nullable=False)
    area_of_operation = db.Column(db.String(100), nullable=False)
    availability = db.Column(db.Boolean, default=True)
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"Rider('{self.name}', '{self.contact_number}', '{self.vehicle_type}', '{self.area_of_operation}', '{self.availability}')"
>>>>>>> 13854cdbacaf913f48b45ede5bae576870a8a0db
