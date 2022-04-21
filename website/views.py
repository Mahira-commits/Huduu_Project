from time import sleep
from flask import Blueprint, render_template, request, redirect, flash, jsonify, url_for
from flask_login import login_required, current_user
from sqlalchemy import null
from .models import User, Progress, Appointments, StudentTips
from . import db
import json

views=Blueprint('views', __name__)

@views.route('/')
def index():
    db.drop_all()
    db.create_all()

    #manually adding users
    meriam = User(username="Meriam123", password="Meriam123", name="Meriam Mkadmi", email="meriam@gmail.com", id=83776, phone="0562401285", userType=0)
    isra = User(username="Isra123", password="Isra123", name="Isra Hasan", email="isra@gmail.com", id=85609, phone="0501234567", userType=0)
    adham = User(username="Adham123", password="Adham123", name="Adham Galal", email="adham@gmail.com", id=77846, phone="0509876543", userType=1)
    lolya = User(username="Lolya123", password="Lolya123", name="Lolya Younes", email="lolya@gmail.com", id=88888, phone="0501122334", userType=1)
    
    #manually adding appointments
    app1 = Appointments(name="Meriam Mkadmi", studentID=83776, counselor=77846,  phone="0562401285", date="21/04/2022",time="8:00 A.M. - 9:00 A.M.", message="Help1")
    app2 = Appointments(name="Meriam Mkadmi", studentID=83776, counselor=88888,  phone="0562401285", date="22/04/2022",time="8:00 A.M. - 9:00 A.M.", message="Help2")
    app3 = Appointments(name="Isra Hasan", studentID=85609, counselor=88888,  phone="0501234567", date="22/05/2022",time="9:00 A.M. - 10:00 A.M.", message="Help2")
    app4 = Appointments(name="Isra Hasan", studentID=85609, counselor=77846,  phone="0501234567", date="22/06/2022",time="9:00 A.M. - 10:00 A.M.", message="Help2")


    
    db.session.add(meriam)
    db.session.add(isra)
    db.session.add(adham)
    db.session.add(lolya)
    db.session.add(app1)
    db.session.add(app2)
    db.session.add(app3)
    db.session.add(app4)


    db.session.commit()

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

#####booking
@views.route('/bookAppointmentStudent', methods = ['GET', 'POST'])
def bookAppointmentStudent():
    if request.method == 'POST':
        name, aus_id, counselor, phone, date, time, message= request.form['name'],request.form['aus_id'],request.form['counselor'], request.form['phone'], request.form['date'],request.form['time'],request.form['message']
        counselorID=User.query.filter_by(name=counselor).first().id
        appointment1 = Appointments(name=name, studentID=int(aus_id), counselor=counselorID,  phone=phone, date=date,time=time, message=message)
        print(name, aus_id, counselor,phone, date, time)
        db.session.add(appointment1)
        db.session.commit()
        return render_template('confirmation.html')
        
    counselorNames=[]
    for x in User.query.all():
        if x.userType==1:
            counselorNames.append(x.name)
    print(counselorNames)
    return render_template('bookAppointmentStudent.html', label=counselorNames)

####view the booking for students
@views.route('/viewAppointmentStudent', methods = ['GET', 'POST'])
def viewAppointmentStudent():
    ap=Appointments.query.filter_by(studentID=current_user.id).all()
    namesC=[]
    for i in range(len(ap)):
        counselorName=(User.query.filter_by(id=ap[i].counselor).first()).name
        namesC.append(counselorName)

    return render_template('viewAppointmentStudent.html', ap=ap, namesC=namesC)
######counselor viewing their appointments
@views.route('/viewAppointmentCounselor', methods = ['GET', 'POST'])
def appointmentCounselor():
    ap=Appointments.query.filter_by(counselor=current_user.id).all()
    namesS=[]
    for i in range(len(ap)):
        studentName=(User.query.filter_by(id=ap[i].studentID).first()).name
        namesS.append(studentName)

    return render_template('viewAppointmentCounselor.html', ap=ap, namesS=namesS)
    ##return render_template('appointmentCounselor.html')

####deleting the appointment s
    
@views.route('/deleteAppointment', methods = ['GET', 'POST'])
def deleteAppointment():
    if request.method == 'POST':
        id= request.form['delete']
        print(id)
        appointment = Appointments.query.get(id)
        db.session.delete(appointment)
        db.session.commit()
        return redirect(url_for('views.viewAppointmentStudent'))
    return render_template('viewAppointmentStudent.html')


@views.route('/editFields', methods = ['GET', 'POST'])
def editFields():
    if request.method == 'POST':
        id= request.form['edit']
        print(id)
        appointment = Appointments.query.get(id)
        counselorNames=[]
        counselorIDs=[]
        cslID = appointment.counselor
        cslName = (User.query.filter_by(id=cslID)).first().name

        lstTimes = ["8:00 A.M. - 9:00 A.M.", "9:00 A.M. - 10:00 A.M.", "10:00 A.M. - 11:00 A.M.", "11:00 A.M. - 12:00 P.M.", "12:00 P.M. - 1:00 P.M.", "1:00 P.M. - 2:00 P.M.", "2:00 P.M. - 3:00 P.M.", "3:00 P.M. - 4:00 P.M.", "4:00 P.M. - 5:00 P.M."]

        if appointment.time in lstTimes:
            lstTimes.remove(appointment.time)
        print(lstTimes)

        for x in User.query.all():
            if x.userType==1:
                if x.name != cslName:
                    counselorNames.append(x.name)
                    counselorIDs.append(x.id)
        
        print(counselorNames)
        print(cslName)
    return render_template('editFields.html', counselorNames=counselorNames, counselorIDs=counselorIDs, cslName=cslName, cslID=cslID, appointment=appointment, id=id, lstTimes=lstTimes)

@views.route('/editAppointment', methods = ['GET', 'POST'])
def editAppointment():
    if request.method == 'POST':
        print("inside edit Appointment ")
        id, counselor, date, time, message= request.form['id'],request.form['counselor'], request.form['date'],request.form['time'], request.form['message']
        print(id,counselor,date,time,message)
        appointment = Appointments.query.get(id)
        appointment.counselor=counselor
        appointment.date=date
        appointment.time=time
        appointment.message=message
        print(appointment.counselor, appointment.date, appointment.time, appointment.message)
        db.session.commit()
    return redirect(url_for('views.viewAppointmentStudent'))

####add tips by counselor
@views.route('/addTipCounselor', methods = ['GET', 'POST'])
def addTipCounselor():
    if request.method == 'POST':
        studentId, message=request.form['studentId'], request.form['message']
        
        counselorId=current_user.id 
        tip1 = StudentTips(studentId = studentId, counselorId=counselorId, message=message)
        print(studentId,counselorId, message)
        db.session.add(tip1)
        db.session.commit()

    return render_template('addTipCounselor.html')
@views.route('/viewTipsStudent', methods = ['GET', 'POST'])
def viewTipsStudent():
    ap=StudentTips.query.filter_by(studentId=current_user.id).all()
    namesC=[]
    namesS=[]
    for i in range(len(ap)):
        counselorName=(User.query.filter_by(id=ap[i].counselorId).first()).name
        studentName=(User.query.filter_by(id=ap[i].studentId).first()).name
        namesC.append(counselorName)
        namesS.append(studentName)
    return render_template('viewTipsStudent.html', ap=ap, namesC=namesC, namesS=namesS)
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
            dummy = Progress(feeling=feeling,num_meals="3",num_hrs="4-6")
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