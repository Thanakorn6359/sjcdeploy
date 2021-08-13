from flask import Flask, render_template,request,url_for,redirect
import pyodbc
import datetime
from datetime import  timedelta
from member import *
from interface_ftp import *
from do_status import *
from do_report import *

app = Flask(__name__)

app.secret_key= "thanakorn"
app.permanent_session_lifetime = timedelta(days=1)
app.register_blueprint(member)
app.register_blueprint(do_status)
app.register_blueprint(do_report)



conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                        'Server=TICSERVER\SQLEXPRESS;'
                        'uid=sa;pwd=sjc@#2017;'
                        'Database=sjc_cp;'
                        'autocommit=True')

@app.route('/')
def index():
    return render_template("index.html")


#-------------------------------------------

if __name__ == '__main__':
    app.run(debug=True, host='192.168.100.10',port=5000)
    app.run(debug=True, host='172.21.0.74',port=5000)
