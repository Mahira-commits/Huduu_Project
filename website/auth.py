#from asyncio.windows_events import NULL
#sfrom django.forms import NullBooleanField
from flask import Blueprint, render_template, request, flash, redirect, url_for
from sqlalchemy import null
from .models import User,dummyTest
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth=Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if request.form.get('Student'):
            username, password, name,id, email, phone, userType  = request.form['username'],request.form['password'],request.form['name'], request.form['aus_id'], request.form['email'],request.form['phone'], 0
            user1 = User(username=username,password=password, name=name,  id=id, email=email,phone=phone,userType=userType)
            print(username, password, name,id, email, phone, userType )
            db.session.add(user1)
            db.session.commit()
            return redirect(url_for('auth.login')) 
        if request.form.get('Counsellor'):
            username, password, name,id, email, phone, userType  = request.form['username'],request.form['password'],request.form['name'], request.form['aus_id'], request.form['email'],request.form['phone'], 1
            user1 = User(username=username,password=password, name=name,  id=id, email=email,phone=phone,userType=userType)
            db.session.add(user1)
            db.session.commit()
            return redirect(url_for('auth.login')) 
    return render_template('register.html')


@auth.route('/login',methods = ['POST', 'GET'])
def login():
    
    if request.method == 'POST':
      username = request.form.get('username')
      password = request.form.get('password')
      u=User.query.filter_by(username=username).first()
      if u:
        if u.password==password: 
              flash('Logged in successfully!', category='success')
              ##login_user(user, remember=True)
              if u.userType == 0:
                return redirect(url_for('views.indexStudent'))
              if u.userType == 1:
                return redirect(url_for('views.indexCounselor'))
        else: 
            flash('Failed to login', category='error')
    return render_template('login.html')
'''
@auth.route('/moodStudent#',methods = ['POST', 'GET'])
def moodvalid():
    
    if request.method == 'POST':
        happy = request.form.get('happy')
        neutral = request.form.get('neutral')
        sad = request.form.get('sad')
        feeling = null
        if happy!=null:
            feeling =happy
        if neutral!=null:
            feeling = neutral
        if sad!=null:
            feeling = sad  
        print("feeling from post form is:",feeling)
        dummy = dummyTest(feeling=feeling,num_meals='3',num_hrs ='4-6')
        print(dummy)
    else: 
        flash('Failed to login', category='error')
    return redirect(url_for('views.charts'))
    '''