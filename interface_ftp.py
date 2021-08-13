from flask import Flask, render_template,request,url_for,redirect,Blueprint
import pyodbc
import datetime
from datetime import  timedelta

app = Flask(__name__)
interface_ftp = Blueprint('interface_ftp',__name__)


conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                        'Server=TICSERVER\SQLEXPRESS;'
                        'uid=sa;pwd=sjc@#2017;'
                        'Database=sjc_cp;'
                        'autocommit=True')