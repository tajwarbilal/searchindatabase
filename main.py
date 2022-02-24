from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'hellothisisbryanproject'  # secret key is used to define the secret data

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # sqlalchemy .db location (for sqlite)
# sqlalchemy track modifications in sqlalchemy
SQLALCHEMY_TRACK_MODIFICATIONS = True


# Database table
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), unique=True)


# This will create table in database
db.create_all()
db.session.commit()

# I am creating five record from the below lines
new_user = User(name='Tajwar')
db.session.add(new_user)
db.session.commit()

new_user = User(name='Bilal')
db.session.add(new_user)
db.session.commit()

new_user = User(name='Python')
db.session.add(new_user)
db.session.commit()

new_user = User(name='Gujjar')
db.session.add(new_user)
db.session.commit()

new_user = User(name='Developer')
db.session.add(new_user)
db.session.commit()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        name = request.form.get('search')
        check_data = User.query.all()

        count = 0  # count is used to check how many records are against one search
        send_data = list()  # created a temporary search
        for i in check_data:
            if i.name == name: # the condition will check how many records are against the search
                send_data.append(i.name)
                count = count + 1

    return render_template('search.html', send_data=send_data, count=count)


if __name__ == '__main__':
    app.run(debug=True)
