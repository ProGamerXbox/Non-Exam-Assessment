from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os, sys
from routes import *

os.chdir(os.path.dirname(os.path.abspath(__file__)))
#print("Current working directory:", os.getcwd())

base_dir = os.path.abspath(os.path.dirname(__file__))
instance_path_relative = os.path.join(base_dir, 'instance')

app = Flask(__name__, instance_path=instance_path_relative, instance_relative_config=True)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'data.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'data.db')
db = SQLAlchemy(app)

#print("Database path:", os.path.join(app.instance_path, 'data.db'))

if __name__ == "__main__":
    app.run(debug=True)