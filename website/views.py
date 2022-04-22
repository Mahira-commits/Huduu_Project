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
    adham = User(username="Adham123", password="Adham123", name="Adham Galal", email="adham@gmail.com", id=77846, phone="0509876543", userType=0)
    lolya = User(username="Lolya123", password="Lolya123", name="Lolya Younes", email="lolya@gmail.com", id=88888, phone="0501122334", userType=0)
    mahira = User(username="Mahira123", password="Mahira123", name="Mahira Pathan", email="mahira@gmail.com", id=85003, phone="0501383252", userType=0)
    #counselors
    yara = User(username="Yara123", password="Yara123", name="Yara Aljabi", email="yara@gmail.com", id=1111, phone="0501234566", userType=1)
    razan = User(username="Rewan123", password="Rewan123", name="Rewan Reda", email="razan@gmail.com", id=2222, phone="0502222222", userType=1)
    rawan = User(username="Lamees123", password="Lamees123", name="Lamees Mamoun", email="Lamees@gmail.com", id=3333, phone="0502631008", userType=1)
    abdulrahman = User(username="Abdul123", password="Abdul123", name="Abdelrahman Tolba", email="abdul@gmail.com", id=4444, phone="0502631009", userType=1)

    #manually adding appointments
    app1 = Appointments(name="Meriam Mkadmi", studentID=83776, counselor=1111,  phone="0562401285", date="30/04/2022",time="8:00 A.M. - 9:00 A.M.", message="I have problems with anxiety and depression and would like your consultation")
    app2 = Appointments(name="Meriam Mkadmi", studentID=83776, counselor=2222,  phone="0562401285", date="29/04/2022",time="8:00 A.M. - 9:00 A.M.", message="I find it hard to communicate with others and would like to seek help")
    app3 = Appointments(name="Isra Hasan", studentID=85609, counselor=2222,  phone="0501234567", date="25/05/2022",time="9:00 A.M. - 10:00 A.M.", message="I am stressed and feel under a lot of pressure")
    app4 = Appointments(name="Isra Hasan", studentID=85609, counselor=4444,  phone="0501234567", date="26/06/2022",time="9:00 A.M. - 10:00 A.M.", message="I find it hard ton conentrate on my studies due to stress and would like some help")

    #manually adding student tips
    tip1=StudentTips(studentId=85609, counselorId=1111,message="Don’t take your thoughts so seriously.")
    tip2=StudentTips(studentId=83776, counselorId=2222,message="Learn self care and focus on yourself.")
    tip3=StudentTips(studentId=83776, counselorId=2222,message="Do your best to remain a willing, accepting, and teachable person.")
    tip4=StudentTips(studentId=83776, counselorId=3333,message="Remove the word should from your vocabulary as much as possible.")

    db.session.add(meriam)
    db.session.add(isra)
    db.session.add(adham)
    db.session.add(lolya)
    db.session.add(mahira)
    db.session.add(yara)
    db.session.add(razan)
    db.session.add(rawan)
    db.session.add(abdulrahman)
    db.session.add(app1)
    db.session.add(app2)
    db.session.add(app3)
    db.session.add(app4)
    db.session.add(tip1)
    db.session.add(tip2)
    db.session.add(tip3)
    db.session.add(tip4)
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
        
        feeling = request.form.get('btn')
        meal = request.form.get('btn2')
        rest = request.form.get('btn3')

        if feeling != None:
            dummy = Progress(studentID=int(current_user.id), type="mood", value=feeling)
            db.session.add(dummy)
            db.session.commit()
        if meal != None:
            dummy = Progress(studentID=int(current_user.id), type="meal", value=meal)
            db.session.add(dummy)
            db.session.commit()
        if rest != None:
            dummy = Progress(studentID=int(current_user.id), type="rest", value=rest)
            db.session.add(dummy)
            db.session.commit()

    return render_template('moodStudent.html')


@views.route('/myProgressStudent',methods = ['POST', 'GET'])
def myProgressStudent():
    return redirect(url_for('views.tempMood'))


@views.route('/tempMood',methods = ['POST', 'GET'])
def tempMood():
    if request.method == 'POST':
        moodHappy = Progress.query.filter_by(studentID=current_user.id, value="happy").count()
        moodNeutral = Progress.query.filter_by(studentID=current_user.id, value="neutral").count()
        moodSad = Progress.query.filter_by(studentID=current_user.id, value="sad").count()
        lstMood = ["happy", "neutral", "sad"]
        valMood = [moodHappy, moodNeutral, moodSad]

        mealOne = Progress.query.filter_by(studentID=current_user.id, value="1").count()
        mealTwo = Progress.query.filter_by(studentID=current_user.id, value="2").count()
        mealThree = Progress.query.filter_by(studentID=current_user.id, value="3").count()
        lstMeal = ["1", "2", "3"]
        valMeal = [mealOne, mealTwo, mealThree]

        rest03 = Progress.query.filter_by(studentID=current_user.id, value="1-3").count()
        rest46 = Progress.query.filter_by(studentID=current_user.id, value="4-6").count()
        rest79 = Progress.query.filter_by(studentID=current_user.id, value="7-9").count()
        rest10 = Progress.query.filter_by(studentID=current_user.id, value="10").count()
        lstRest = ["0-3", "4-6", "7-9", "10"]
        valRest = [rest03, rest46, rest79, rest10]

    return render_template('myProgressStudent.html',
    lstMood = json.dumps(lstMood),
    valMood= json.dumps(valMood),
    lstMeal = json.dumps(lstMeal),
    valMeal= json.dumps(valMeal),
    lstRest = json.dumps(lstRest),
    valRest= json.dumps(valRest))