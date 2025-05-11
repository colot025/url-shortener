from flask import Flask
from .extensions import db, migrate
from .routes import shortener

# initialize flask application
def create_app(config_file='settings.py', config_dict=None):
    app = Flask(__name__)

    #app.config.from_pyfile(config_file)
    if config_dict:
        app.config.update(config_dict)  # Load configuration from the dictionary
    else:
        app.config.from_pyfile(config_file)  # Load configuration from the file

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(shortener)

    return app