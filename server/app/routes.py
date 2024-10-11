from flask import render_template, request, redirect
from . import db  # Import the database instance
from .models import User
from flask import Blueprint

# Create a Blueprint for the app
main = Blueprint('main', __name__)

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username_register = request.form['username']
        password_register = request.form['password']

        new_user = User(username=username_register, password=password_register)

        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect('/')  # Redirect to the home page after registration
        except:
            return 'There was an issue adding the user'
    return render_template('register.html')

@main.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        username_register = request.form['username']
        password_register = request.form['password']

        if not password_register:  # Check if the password is empty
            error = "Password cannot be empty."
            data = User.query.order_by(User.date_created).all()  # Reload the existing users
            return render_template('index.html', data=data, error=error)

        new_user = User(username=username_register, password=password_register)

        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding the user (Could be that you have the same username as someone else)'

    else:
        data = User.query.order_by(User.date_created).all()  # Now works since date_created exists
        return render_template('index.html', data=data)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username, password=password).first()
        if user:
            return redirect('/')
        else:
            error = "Invalid username or password"
            return render_template('index.html', error=error)

    return redirect('/')
