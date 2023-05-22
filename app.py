from flask import Flask, request
import mysql.connector
app = Flask(__name__)

con = mysql.connector.connect(host="mydb.c284m4zoh3wq.ap-south-1.rds.amazonaws.com",user="admin",password="sagar123",database="myapp")
con.autocommit=True
cur = con.cursor(dictionary=True)

@app.route("/")
def home():
    return "Hello"

@app.route("/getrecords")
def get_records():
    cur.execute("select * from users")
    result = cur.fetchall()
    if len(result)>0:
        return {"payload":result}
    else:
        return "No Data Found"

@app.route("/addrecord", methods=["post"])
def add_record():
    data = request.form
    print(data)
    cur.execute(f"INSERT INTO users(name, email, password) VALUES('{data['name']}', '{data['email']}', '{data['password']}')")
    return "Record Added"

