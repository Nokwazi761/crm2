# Imports
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from secrets import token_hex

# SetUp
app = Flask(__name__)
app.config['SECRET_KEY'] = token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///User.db'
db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    surname = db.Column(db.String(20), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    gender = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)

    def __init__(self, name, surname, phone_number, email, password, gender):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.email = email
        self.gender = gender
        self.password = password

# Routes
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/')
@app.route('/index')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return redirect(url_for('calendar'))

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        phone_number = request.form['phone_number']
        gender = request.form['gender']
        email = request.form['email']
        password = request.form['password']
        user = User(name=name, surname=surname, phone_number=phone_number, email=email, password=password, gender=gender)
        db.session.add(user)
        db.session.commit()
        flash('User added successfully')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and user.password == password:
            return redirect(url_for('home'))  # Redirect to home page on successful login
        else:
            flash('Login Unsuccessful. Please check username and password')
    return render_template('login.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
