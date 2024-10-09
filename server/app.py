from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)  # Add this field

    def __repr__(self):
        return '<User %r>' % self.username



@app.route('/', methods=['POST', 'GET'])
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username_register']
        password = request.form['password_register']

        user = User.query.filter_by(username=username, password=password).first()
        if user:
            return redirect('/')
        else:
            error = "Invalid username or password"
            return render_template('index.html', error=error)

    return redirect('/')


@app.route('/delete/<int:id>')
def delete(id):
    user_to_delete = User.query.get_or_404(id)

    try:
        db.session.delete(user_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    user_to_update = User.query.get_or_404(id)

    if request.method == 'POST':
        user_to_update.username = request.form['username']  # Correctly update the username

        try:
            db.session.commit()
            return redirect('/')
        except:
            return f'There was an issue updating your username'

    else:
        return render_template('update.html', user=user_to_update)


if __name__ == "__main__":
    app.run(debug=True)