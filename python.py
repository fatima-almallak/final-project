from ast import Return
from genericpath import exists
from itertools import count
from sqlite3 import Cursor, connect
from tabnanny import check 
from flask import Flask, render_template, request, flash, abort, current_app, make_response
from werkzeug.utils import secure_filename
from gtts import gTTS
from flask import jsonify
import os
from playsound import playsound
from os import path
import webbrowser 
import speech_recognition as sr
import pymysql
import mysql.connector
connection=pymysql.connect(host="localhost",user="root",password="123456",database="mydb")
cursor = connection.cursor() 


app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/home")
def home():
    return render_template("home.html")    

@app.route("/login")
def login():
   return render_template("login.html")


@app.route("/loginforstudent",methods=['POST']  )
def loginforstudent():
 
         id=request.form.get("number")
         password=request.form.get("password")
         value = request.form.getlist('check') 
         b=int(id)
         if(value[0]=="notadmin"):
          q=("SELECT count(*) FROM  std_info WHERE password=(%s) and std_id=(%s)")
          v=(password,b) 
          cursor.execute(q,v)
          value3=cursor.fetchone()[0]
          if (value3 == 0):
            return render_template("login.html")
          else:
            q=("SELECT * FROM  std_info WHERE std_id=(%s)")
            v=(b)
            cursor.execute(q,v)
            data = cursor.fetchall()
            return render_template("afterLogin.html",value=data) 
         else:
            return render_template("login.html")
         
             

@app.route("/StudentSchedule")
def StudentSchedule():
   return render_template("StudentSchedule.html")


@app.route("/chgpass")
def chgpass():
   return render_template("chgpass.html")


@app.route("/StudentInfo")
def StudentInfo():
   return render_template("StudentInfo.html")   


@app.route("/StudentRegistration/<name>")
def StudentRegistration(name):
   q=("SELECT course.course_id,course.course_name,course.noOfHours FROM  course JOIN plan  on course.course_id=plan.course_id and dept_name=(%s)")
   v=(name)
   cursor.execute(q,v)
   data2 = cursor.fetchall()
   return render_template("StudentRegistration.html",value=data2,v=name)



@app.route("/CourseSchedule")
def CourseSchedule():
   return render_template("CourseSchedule.html")   



@app.route("/afterlogin")
def afterlogin():
    return render_template("afterlogin.html")  


if __name__=="__main__":
     app.run(port=8000)