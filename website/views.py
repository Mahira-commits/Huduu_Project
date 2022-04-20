from time import sleep
from flask import Blueprint, render_template, request, redirect, flash, jsonify, url_for
from flask_login import login_required, current_user
from sqlalchemy import null
from .models import User, Progress
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

#####booking
@views.route('/bookAppointmentStudent', methods = ['GET', 'POST'])
def bookAppointmentStudent():
    if request.method == 'POST':
        name, aus_id, counselor, phone, date, time= request.form['name'],request.form['aus_id'],request.form['counselor'], request.form['phone'], request.form['date'],request.form['time']
        #appointment1 = Appointments(name=name,aus_id=aus_id, counselor=counselor,  phone=phone, date=date,time=time)
        print(name, aus_id, counselor,phone, date, time)
        #db.session.add(appointment1)
        #db.session.commit()
        return render_template('confirmation.html')
        
    counselorNames=[]
    for x in User.query.all():
        if x.userType==1:
            counselorNames.append(x.name)
    print(counselorNames)
    return render_template('bookAppointmentStudent.html', label=counselorNames)

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
@views.route('/moodStudent',methods = ['POST', 'GET'])
def moodStudent():
    if request.method == 'POST':
        # inputting moods from user
        happy = request.form.get('happy')
        neutral = request.form.get('neutral')
        sad = request.form.get('sad')
        feeling = null

        if happy!=None:
            feeling=happy
        elif neutral!=None:
            feeling = neutral
        elif sad!=None:
            feeling = sad


        # inputting meals from user
        one = request.form.get('1')
        two = request.form.get('2')
        three = request.form.get('3')
        num_meals = null

        if one!=None:
            num_meals=one
        elif two!=None:
            num_meals=two
        elif three!=None:
            num_meals = three 

        # inputting sleep hours from user
        zero_three = request.form.get('0-3')
        four_six = request.form.get('4-6')
        seven_nine = request.form.get('7-9')
        ten = request.form.get('10')
        num_hrs = null

        if zero_three!=None:
            num_hrs=zero_three
        elif four_six!=None:
            num_hrs=four_six
        elif seven_nine!=None:
            num_hrs = seven_nine 
        elif ten!=None:
            num_hrs = ten 

        if num_hrs!=null and feeling !=null and num_meals != null:
            dummy = Progress(feeling=feeling,num_meals=num_meals,num_hrs=num_hrs)
            db.session.add(dummy)
            db.session.commit()

    return render_template('moodStudent.html')
    
@views.route('/myProgressStudent', methods = ['GET', 'POST'])
def myProgressStudent():
    mooddict = {}
    for dummy in Progress.query.all():
        feeling = dummy.feeling
        if feeling not in mooddict.keys():
            mooddict[feeling] = 0
    for dummy in Progress.query.all():
        feeling= dummy.feeling
        mooddict[feeling] = mooddict[feeling] + 1
    
    labels = list(mooddict.keys())
    values = list(mooddict.values())
    print(labels)
    print(values)
    return render_template('myProgressStudent.html', label = json.dumps(labels), value= json.dumps(values))