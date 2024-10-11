import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():

    # working directory
    os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

    app = Flask(__name__,
        template_folder=os.path.join(os.path.dirname(__file__), '../templates'),
        static_folder=os.path.join(os.path.dirname(__file__), '../static'))

    # Configurations
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'data.db')
    #app.config['SECRET_KEY'] = 'your-secret-key'

    db.init_app(app)

    # Import blueprints or routes
    from .routes import main  # Import the main blueprint
    app.register_blueprint(main)  # Register the blueprint

    return app
