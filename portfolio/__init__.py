from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
<<<<<<< HEAD
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:new_password@localhost/vue'
=======
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost/vue'
>>>>>>> 13854cdbacaf913f48b45ede5bae576870a8a0db
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from portfolio import routes
