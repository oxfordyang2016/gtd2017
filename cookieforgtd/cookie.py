

#reference url https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-one
#when u run app.py in macos ,u may meet the problem https://stackoverflow.com/questions/24001147/python-bind-socket-error-errno-13-permission-denied
import os,time,json
#import datetime
from dateutil import parser
from datetime import datetime
from flask import Flask, request,jsonify,redirect, url_for
from flask import render_template,make_response
from flask.ext.sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


def checkcookie_time(request):
    useremail = request.cookies.get('email')
    logintime = request.cookies.get('logintime')
    #i use the https://stackoverflow.com/questions/466345/converting-string-into-datetime to parser time string
    logintime = parser.parse(logintime)
    now = datetime.now()
    #comupte interval senconds
    #https://stackoverflow.com/questions/4362491/how-do-i-check-the-difference-in-seconds-between-two-dates
    allseconds = (now-logintime).total_seconds()
    return allseconds


def checkcookie(request):
    useremail = request.cookies.get('email')
    logintime = request.cookies.get('logintime')
    #i use the https://stackoverflow.com/questions/466345/converting-string-into-datetime to parser time string
    logintime = parser.parse(logintime)
    now = datetime.now()
    #comupte interval senconds
    #https://stackoverflow.com/questions/4362491/how-do-i-check-the-difference-in-seconds-between-two-dates
    allseconds = (now-logintime).total_seconds()
    print(allseconds,'login time interval')
    if allseconds<50000:
        return True
    else:
        return False


def getcookieinfo(request):
    '''
    this fucntion is used to get all cookie info
    '''
    useremail = request.cookies.get('email')
    logintime = request.cookies.get('logintime')
    clienttype = request.cookies.get('client')
    #i use the https://stackoverflow.com/questions/466345/converting-string-into-datetime to parser time string
    return [useremail,logintime,clienttype]
