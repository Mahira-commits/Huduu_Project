##from flask import Flask, render_template, request, url_for, redirect, flash
##from flask_sqlalchemy import SQLAlchemy
##from datetime import date, time, datetime
from website import db
from  website import create_app
from flask import Flask

##from flask_bcrypt import check_password_hash, login_user
##app = Flask(__name__)
app=create_app()

'''
@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    return render_template('contact.html')
'''
'''
@app.route('/user/<un>', methods = ['GET', 'POST'])
def profile(un):
    u = User.query.filter_by(username=un).one()
    return render_template('profile.html', user=u)

@app.route('/delete/<int:id>')
def deletion(id):
    user1 = Student.query.get(id)
    db.session.delete(user1)
    db.session.commit()
    return redirect(url_for('users'))

'''
from website.models import dummyTest
if __name__ == '__main__':
    ##db.create_all()

    ## db.session.add(user1)
    ##db.session.commit()
    app.run(debug=True)

    #done InshaAllah
    
    
    