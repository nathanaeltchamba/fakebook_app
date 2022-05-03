from flask import Config, Flask

app = Flask(__name__)
app.config.from_object(Config)

from app import routes, errors