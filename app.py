from flask import Flask
import mysql.connector
app = Flask(__name__)

con = mysql.connector.connect(host="mydb.c284m4zoh3wq.ap-south-1.rds.amazonaws.com",user="admin",password="sagar123",database="myapp")
con.autocommit=True
cur = con.cursor(dictionary=True)

@app.get("/")
def home():
    return "Hello"

@app.get("/getrecords")
def get_records():
    cur.execute("select * from users")
    result = cur.fetchall()
    if len(result)>0:
        return {"payload":result}
    else:
        return "No Data Found"
