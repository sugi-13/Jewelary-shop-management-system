import sqlite3
from flask import Flask, render_template,url_for,Response
import os
import requests
import json
import datetime
from flask import Flask, jsonify, render_template, request, flash,session,redirect
from flask_session import Session
from flask_socketio import SocketIO, emit, join_room, leave_room, send
from PIL import Image

flag=0

app = Flask(__name__)
app.debug = True
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SESSION_PERMANENET"]=False
app.config["SESSION_TYPE"]="filesystem"
Session(app)
socketio = SocketIO(app, manage_session=False)

@app.route("/")
def home():
  return render_template("home.html")
@app.route("/aboutus")
def aboutus():
  return render_template("aboutus.html")
@app.route("/supplier")
def supplier():
  return render_template("supplier.html")
@app.route("/login")
def login():
  return render_template("login.html")
@app.route("/pdetail")
def pdetail():
  return render_template("pdetail.html")
@app.route("/pdetail2")
def pdetail2():
  return render_template("pdetail2.html")
@app.route("/pdetail3")
def pdetail3():
  return render_template("pdetail3.html")
@app.route("/pdetail4")
def pdetail4():
  return render_template("pdetail4.html")
@app.route("/pdetail5")
def pdetail5():
  return render_template("pdetail5.html")
@app.route("/pdetail6")
def pdetail6():
  return render_template("pdetail6.html")
@app.route("/cart")
def cart():
  return render_template("cart.html")
@app.route("/payment")
def payment():
  return render_template("payment.html")
@app.route("/signin")
def signin():
  return render_template("signin.html")
@app.route("/success")
def success():
  return render_template("success.html")
@app.route("/supdet")
def supdet():
  return render_template("supdet.html")

#creating database
conn = sqlite3.connect('JewelManagement.db',check_same_thread=False)
conn.row_factory = sqlite3.Row

def get_db_connection():
    conn = sqlite3.connect('JewelManagement.db')
    conn.row_factory = sqlite3.Row
    return conn



"""
def get_db_connection():
    conn = sqlite3.connect('db2.db')
    conn.row_factory = sqlite3.Row
    return conn
conn = get_db_connection()
        users = conn.execute('SELECT * FROM user').fetchall()
connection = sqlite3.connect('db2.db',check_same_thread=False)
"""

@app.route('/review',methods=["GET","POST"])
def review():
      name=(request.form.get("name"))
      email=(request.form.get("email"))
      message=(request.form.get("message"))
      if not name:
          return render_template("error.html")
      cur = conn.cursor()
      cur.execute("INSERT INTO aboutus(name,email,message)VALUES(?,?,?)",(name,email,message)) 
      conn.commit()
      conn.close()
      return render_template("aboutus.html")

@app.route('/log',methods=["GET","POST"])
def log():
  if request.method=="POST":
      session["lemail"]=request.form.get("lemail")
      session["lpassword"]=request.form.get("lpassword")
      conn = get_db_connection()
      users = conn.execute("SELECT * from users").fetchall()
      print(users)
      for user in users:
        print(user["semail"])
        print(session["lemail"])
        if(user["semail"] == session["lemail"]):
          global flag
          flag = 1
          if(user["scpassword"] == session["lpassword"]):
            flag = 1
          else :
            flag = 0
      print(flag)
      if(flag == 0):
        session["lemail"] = None
        session["lpassword"] = None
        return render_template("error2.html")
      conn.close()
      return redirect("/")
  return render_template("home.html")

@app.route('/sign',methods=["GET","POST"])
def sign():
  print("hi")
  susername=(request.form.get("susername"))
  semail=(request.form.get("semail"))
  spassword=(request.form.get("spassword"))
  scpassword=(request.form.get("scpassword"))
  print(susername)
  print(semail)
  print(scpassword)
  conn = sqlite3.connect('JewelManagement.db',check_same_thread=False)
  if not susername:
          return render_template("error.html")
  if(spassword != scpassword):
          return render_template("error2.html")
  cur = conn.cursor()
  cur.execute("INSERT INTO users(susername,semail,scpassword)VALUES(?,?,?)",(susername,semail,scpassword)) 
  conn.commit()
  conn.close()
  return render_template("login.html")

@app.route('/viewdet', methods=['POST', 'GET'])
def viewdet():
  conn = sqlite3.connect('JewelManagement.db',check_same_thread=False) 
  conn.row_factory = sqlite3.Row  
  cur = conn.cursor()  
  cur.execute("select * from supdet1")  
  rows = cur.fetchall()  
  for a in rows:
    print(a)
  return render_template("supdet.html",rows = rows)

@app.route('/viewdet2', methods=['POST', 'GET'])
def viewdet2():
  conn = sqlite3.connect('JewelManagement.db',check_same_thread=False) 
  conn.row_factory = sqlite3.Row  
  cur = conn.cursor()  
  cur.execute("select * from supdet2")  
  rows = cur.fetchall()  
  for a in rows:
    print(a)
  return render_template("supdet2.html",rows = rows)

@app.route('/viewdet3', methods=['POST', 'GET'])
def viewdet3():
  conn = sqlite3.connect('JewelManagement.db',check_same_thread=False) 
  conn.row_factory = sqlite3.Row  
  cur = conn.cursor()  
  cur.execute("select * from supdet3")  
  rows = cur.fetchall()  
  for a in rows:
    print(a)
  return render_template("supdet3.html",rows = rows)

@app.route('/viewdet4', methods=['POST', 'GET'])
def viewdet4():
  conn = sqlite3.connect('JewelManagement.db',check_same_thread=False) 
  conn.row_factory = sqlite3.Row  
  cur = conn.cursor()  
  cur.execute("select * from supdet4")  
  rows = cur.fetchall()  
  for a in rows:
    print(a)
  return render_template("supdet4.html",rows = rows)

@app.route("/logout",methods=['POST', 'GET'])
def logout():
    session.pop('lemail', None)
    return render_template("home.html")

@app.route('/pd',methods=['POST', 'GET'])
def pd():
  if 'lemail' not in session:
    return render_template("login.html")
  else:
    return render_template("cart.html")

@app.route('/viewpdt', methods=['POST', 'GET'])
def viewpdt():
  conn = sqlite3.connect('JewelManagement.db',check_same_thread=False) 
  conn.row_factory = sqlite3.Row  
  cur = conn.cursor()  
  cur.execute("select * from products")  
  rows = cur.fetchall()  
  return render_template("fromcart.html",rows = rows)

@app.route("/addToCart1", methods=['POST', 'GET'])
def addToCart1():
    if 'lemail' not in session:
        return render_template("login.html")
    else:
        pid = 1
        with sqlite3.connect('JewelManagement.db') as conn:
            cur = conn.cursor()
            cur.execute("SELECT susername FROM users WHERE semail = '" + session['lemail'] + "'")
            susername = cur.fetchone()[0]
            try:
                cur.execute("INSERT INTO cart (cname,pid) VALUES (?, ?)", (susername,pid))
                conn.commit()
                msg = "Added successfully"
            except:
                conn.rollback()
                msg = "Error occured"
        conn.close()
        return render_template("home.html")

@app.route("/addToCart2", methods=['POST', 'GET'])
def addToCart2():
    if 'lemail' not in session:
        return render_template("login.html")
    else:
        pid = 2
        with sqlite3.connect('JewelManagement.db') as conn:
            cur = conn.cursor()
            cur.execute("SELECT susername FROM users WHERE semail = '" + session['lemail'] + "'")
            susername = cur.fetchone()[0]
            try:
                cur.execute("INSERT INTO cart (cname,pid) VALUES (?, ?)", (susername,pid))
                conn.commit()
                msg = "Added successfully"
            except:
                conn.rollback()
                msg = "Error occured"
        conn.close()
        return render_template("home.html")

@app.route("/addToCart3", methods=['POST', 'GET'])
def addToCart3():
    if 'lemail' not in session:
        return render_template("login.html")
    else:
        pid = 3
        with sqlite3.connect('JewelManagement.db') as conn:
            cur = conn.cursor()
            cur.execute("SELECT susername FROM users WHERE semail = '" + session['lemail'] + "'")
            susername = cur.fetchone()[0]
            try:
                cur.execute("INSERT INTO cart (cname,pid) VALUES (?, ?)", (susername,pid))
                conn.commit()
                msg = "Added successfully"
            except:
                conn.rollback()
                msg = "Error occured"
        conn.close()
        return render_template("home.html")

@app.route("/addToCart4", methods=['POST', 'GET'])
def addToCart4():
    if 'lemail' not in session:
        return render_template("login.html")
    else:
        pid = 4
        with sqlite3.connect('JewelManagement.db') as conn:
            cur = conn.cursor()
            cur.execute("SELECT susername FROM users WHERE semail = '" + session['lemail'] + "'")
            susername = cur.fetchone()[0]
            try:
                cur.execute("INSERT INTO cart (cname,pid) VALUES (?, ?)", (susername,pid))
                conn.commit()
                msg = "Added successfully"
            except:
                conn.rollback()
                msg = "Error occured"
        conn.close()
        return render_template("home.html")

@app.route("/addToCart5", methods=['POST', 'GET'])
def addToCart5():
    if 'lemail' not in session:
        return render_template("login.html")
    else:
        pid = 5
        with sqlite3.connect('JewelManagement.db') as conn:
            cur = conn.cursor()
            cur.execute("SELECT susername FROM users WHERE semail = '" + session['lemail'] + "'")
            susername = cur.fetchone()[0]
            try:
                cur.execute("INSERT INTO cart (cname,pid) VALUES (?, ?)", (susername,pid))
                conn.commit()
                msg = "Added successfully"
            except:
                conn.rollback()
                msg = "Error occured"
        conn.close()
        return render_template("home.html")

@app.route("/addToCart6", methods=['POST', 'GET'])
def addToCart6():
    if 'lemail' not in session:
        return render_template("login.html")
    else:
        pid = 6
        with sqlite3.connect('JewelManagement.db') as conn:
            cur = conn.cursor()
            cur.execute("SELECT susername FROM users WHERE semail = '" + session['lemail'] + "'")
            susername = cur.fetchone()[0]
            try:
                cur.execute("INSERT INTO cart (cname,pid) VALUES (?, ?)", (susername,pid))
                conn.commit()
                msg = "Added successfully"
            except:
                conn.rollback()
                msg = "Error occured"
        conn.close()
        return render_template("home.html")

@app.route("/newcart", methods=['POST', 'GET'])
def newcart():
    email = session['lemail']
    conn = sqlite3.connect('JewelManagement.db',check_same_thread=False)
    conn.row_factory = sqlite3.Row 
    cur = conn.cursor()
    cur.execute("SELECT susername FROM users WHERE semail = '" + email + "'")
    susername = (cur.fetchone()[0])
    cur.execute("SELECT cname FROM cart")
    cname = (cur.fetchone()[0])
    if(cname == susername):
      cur.execute("SELECT products.pid, products.pname, products.pprice FROM products, cart WHERE products.pid = cart.pid")
      products = cur.fetchall()
      totalPrice = 0
      for row in products:
        print(row)
        totalPrice += row[2]
    else :
      return render_template("login.html")
    return render_template("newcart.html",rows = products,t = totalPrice)

@app.route("/removeFromCart",methods=['POST', 'GET'])
def removeFromCart():
    if 'lemail' not in session:
        return render_template("login.html")
    email = session['lemail']
    with sqlite3.connect('JewelManagement.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT susername FROM users WHERE semail = '" + email + "'")
        susername = cur.fetchone()[0]
        cur.execute("DELETE FROM cart WHERE pid = 3 or pid = 2")
        conn.commit()
    conn.close()
    return render_template("home.html")

@app.route("/gotopayment",methods=['POST', 'GET'])
def gotopayment():
  total = (request.form.get("total"))
  print(total)
  return render_template("payment.html",total=total)

@app.route('/paydetails',methods=["GET","POST"])
def paydetails():
      username=(request.form.get("username"))
      cardname=(request.form.get("cardname"))
      cardnumber=(request.form.get("cardnumber"))
      exp=(request.form.get("exp"))
      cvv=(request.form.get("cvv"))
      address=(request.form.get("address"))
      city=(request.form.get("city"))
      state=(request.form.get("state"))
      zipcode=(request.form.get("zipcode"))
      if not username:
          return render_template("error.html")
      conn = sqlite3.connect('JewelManagement.db',check_same_thread=False)
      cur = conn.cursor()
      cur.execute("INSERT INTO paydetails(username,cardname,cardnumber,exp,cvv,address,city,state,zipcode)VALUES(?,?,?,?,?,?,?,?,?)",(username,cardname,cardnumber,exp,cvv,address,city,state,zipcode)) 
      conn.commit()
      conn.close()
      return render_template("success.html")
