from flask import Flask, request
import mysql.connector

app = Flask(__name__)
print(__name__)
if __name__ == '__main__':
    print("************")
    app.run(host='0.0.0.0', port=8080, debug=True)

try:
    con = mysql.connector.connect(host="mydatabase.c284m4zoh3wq.ap-south-1.rds.amazonaws.com",user="admin",password="sagar123",database="myapp")
    con.autocommit=True
    cur = con.cursor(dictionary=True)
except:
    print('An exception occurred')

@app.route("/")
def home():
    return "Hello"

@app.route("/getrecords")
def get_records():
    try:
        cur.execute("select * from users")
        result = cur.fetchall()
    except:
        return "Internal Error"
    
    if len(result)>0:
        return {"payload":result}
    else:
        return "No Data Found"

@app.route("/addrecord", methods=["post"])
def add_record():
    try:
        data = request.form
        cur.execute(f"INSERT INTO users(name, email, password) VALUES('{data['name']}', '{data['email']}', '{data['password']}')")
        return "Record Added"
    except:
        return "Internal Error"
    

