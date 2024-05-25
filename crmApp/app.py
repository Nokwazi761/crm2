# Imports
from flask import Flask
# import flask_login
from flask_sqlalchemy import SQLAlchemy
import app
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
# from crmApp.Forms import LoginForm, RegisterForm,TaskForm
# from crmApp.models import User
from werkzeug.utils import secure_filename

# SetUp
app = Flask(__name__)
app.config['SECRET_KEY']='NAMR'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///User.db'
db = SQLAlchemy(app)
# login_manager = flask_login.LoginManager()
# login_manager.init_app(app)


# Code
@app.route('/contact')
def contact():
    
    return render_template('contact.html')

@app.route('/about')
def about():
    
    return render_template('about.html')


@app.route('/')
def home():
    return render_template('index.html')


# @app.route('/Register',methods=['GET','POST'])
# def register():
#     form=RegisterForm()
#     if form.validate_on_submit():
#         user=User(name=form.name.data,surname=form.surname.data,phone_number=form.phonenumber.data,email =form.email.data,password=form.password.data)
#         db.session.add(user)
#         db.session.commit()      
#         flash('user added successful')
#         return redirect(url_for('login'))
#     return render_template('register.html',form=form) 

# @app.route('/login',methods=['GET','POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         user=User.query.filter_by(email=form.email.data).first()
#         if user:
#             login_user(user=user,remember=form.remember.data)
#             flash('You have been logged in!')
#             next_page = request.args.get('next')
#             return redirect(next_page) if next_page else redirect(url_for('landing'))
#         else:
#             flash('Login Unsuccessful. Please check username and password'+form.password.data)
#     return render_template('login.html',form=form)


# @app.route("/logout")
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('home'))

# @login_manager.unauthorized_handler
# def unauthorized_handler():
#     return 'Unauthorized', 401

# @app.route('/landing')
# @login_required
# def landing():
#     logged=current_user.name
#     return render_template('landing.html',logged=logged)

# @app.route('/upload',methods=['GET','POST'])
# @login_required
# def upload():
#     form=TaskForm()
#     if form.validate_on_submit():
#         subject=form.subject.data
#         f = form.tasksdocs.data
#         filename = secure_filename(f.file.filename)
#         form.tasksdocs.data.save('uploads/' + filename)
#         flash('Uploaded!')
#         return redirect(url_for('landing'))
#     return render_template('upload.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)
