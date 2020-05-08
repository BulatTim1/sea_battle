from flask import Flask
# from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_restful import Api

app = Flask(__name__)
app.config.from_object('config')
mail = Mail(app)
bs = Bootstrap(app)
api = Api(app)
# lm = LoginManager()
# lm.init_app(app)
# lm.login_view = 'login'
from app import views
