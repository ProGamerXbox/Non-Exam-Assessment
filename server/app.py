from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)  # Add this field


    def __repr__(self):
        return '<User %r>' % self.username



@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not password:  # Check if the password is empty
            error = "Password cannot be empty."
            users = User.query.order_by(User.date_created).all()  # Reload the existing users
            return render_template('index.html', users=users, error=error)

        new_user = User(username=username, password=password)

        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding the user (Could be that you have the same username as someone else)'

    else:
        users = User.query.order_by(User.date_created).all()  # Now works since date_created exists
        return render_template('index.html', users=users)


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
    user = User.query.get_or_404(id)

    if request.method == 'POST':
        user.content = request.form['user']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your username'

    else:
        return render_template('update.html', user=user)


if __name__ == "__main__":
    app.run(debug=True)