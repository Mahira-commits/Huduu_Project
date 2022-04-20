from time import sleep
from flask import Blueprint, render_template, request, redirect, flash, jsonify, url_for
from flask_login import login_required, current_user
from sqlalchemy import null
from .models import User,dummyTest, Appointments, StudentTips, BroadcastTips
from . import db
import json

views=Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('index.html')
@views.route('/indexStudent')
def indexStudent():
    return render_template('indexStudent.html')
@views.route('/indexCounselor')
def indexCounselor():
    return render_template('indexCounselor.html')
@views.route('/contact', methods = ['GET', 'POST'])
def contact():
    return render_template('contact.html')

@views.route('/moodStudent', methods = ['GET', 'POST'])
def moodStudent():
    return render_template('moodStudent.html')

@views.route('/about', methods = ['GET', 'POST'])
def about():
    return render_template('about.html')

@views.route('/aboutCounselor', methods = ['GET', 'POST'])
def aboutCounselor():
    return render_template('aboutCounselor.html')

@views.route('/aboutStudent', methods = ['GET', 'POST'])
def aboutStudent():
    return render_template('aboutStudent.html')

@views.route('/addTipCounselor', methods = ['GET', 'POST'])
def addTipCounselor():
    return render_template('addTipCounselor.html')

@views.route('/appointmentCounselor', methods = ['GET', 'POST'])
def appointmentCounselor():
    return render_template('appointmentCounselor.html')

@views.route('/confirmation', methods = ['GET', 'POST'])
def confirmation():
    return render_template('confirmation.html')

@views.route('/contactCounselor', methods = ['GET', 'POST'])
def contactCounselor():
    return render_template('contactCounselor.html')

@views.route('/contactStudent', methods = ['GET', 'POST'])
def contactStudent():
    return render_template('contactStudent.html')
'''
@views.route('/register', methods = ['GET', 'POST'])
def register():
    return render_template('register.html')
'''
@views.route('/viewAppointmentStudent', methods = ['GET', 'POST'])
def viewAppointmentStudent():
    return render_template('viewAppointmentStudent.html')

@views.route('/viewTipsCounselor', methods = ['GET', 'POST'])
def viewTipsCounselor():
    return render_template('viewTipsCounselor.html')

@views.route('/charts', methods = ['GET', 'POST'])
def charts():
    mooddict = {}

    for dummy in dummyTest.query.all():
        feeling= dummy.feeling
        if feeling not in mooddict.keys():
            mooddict[feeling]=0
    for dummy in dummyTest.query.all():
        feeling= dummy.feeling
        mooddict[feeling] = mooddict[feeling]+1
    
    labels = list(mooddict.keys())
    values = list(mooddict.values())
    print(labels)
    print(values)
    return render_template('charts.html', label = json.dumps(labels), value= json.dumps(values))
'''
auth.route('/register', methods=['GET', 'POST'])
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
    '''
#####adding counsellors names to drop down 
@views.route('/retrieve', methods = ['GET', 'POST'])
def retrieve():
    counselorNames=[]
    for x in User.query.all():
        if x.userType==1:
            counselorNames.append(x.name)
    print(counselorNames)
    return render_template('bookAppointmentStudent.html', label=counselorNames)

@views.route('/bookAppointmentStudent', methods = ['GET', 'POST'])
def bookAppointmentStudent():
    return render_template('bookAppointmentStudent.html')

#####booking
@views.route('/bookAppointmentStudent2', methods = ['GET', 'POST'])
def bookAppointmentStudent2():
    #if request.method == 'POST':
        name, aus_id, counselor, phone, date, time= request.form['name'],request.form['aus_id'],request.form['counselor'], request.form['phone'], request.form['date'],request.form['time']
        appointment1 = Appointments(name=name,aus_id=aus_id, counselor=counselor,  phone=phone, date=date,time=time)
        print(name, aus_id , counselor,phone, date, time)
        db.session.add(appointment1)
        db.session.commit()
        return render_template('bookAppointmentStudent2.html')
   

'''
#Adding dummy records to test on
stat1 = dummyTest(feeling='happy',num_meals='1',num_hrs ='0-3')
    stat2 = dummyTest(feeling='neutral',num_meals='3',num_hrs ='4-6')
    stat3 = dummyTest(feeling='neutral',num_meals='2',num_hrs ='7-9')
    print(stat1)
    print(stat2)
    print(stat3)
    db.session.add(stat1)
    db.session.add(stat2)
    db.session.add(stat3)
    db.session.commit()
    print(dummyTest.query.all())
    print(dummyTest.query.filter_by(feeling='neutral').all())
'''
@views.route('/test.html',methods = ['POST', 'GET'])
def moodvalid():
    
    if request.method == 'POST':
        happy = request.form.get('happy')
        print("happy is",happy)
        neutral = request.form.get('neutral')
        print("neutral is",neutral)
        sad = request.form.get('sad')
        print("sad is",sad)
        feeling = null
        if happy!=None:
            feeling=happy
        elif neutral!=None:
            feeling = neutral
        elif sad!=None:
            feeling = sad  
        print("feeling from post form is:",feeling)
        dummy = dummyTest(feeling=feeling,num_meals='3',num_hrs ='4-6')
        db.session.add(dummy)
        db.session.commit()
        print(dummy.feeling)
    return redirect(url_for('views.charts'))
    