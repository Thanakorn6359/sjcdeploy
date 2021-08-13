from flask import render_template,request,url_for,redirect,Blueprint
import pyodbc
#import datetime
import time
import  datetime


do_report = Blueprint('do_report',__name__)
conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                        'Server=TICSERVER\SQLEXPRESS;'
                        'uid=sa;pwd=sjc@#2017;'
                        'Database=sjc_cp;'
                        'autocommit=True')


@do_report.route('/do_report01')
def do_report01():
    return render_template("do_report01.html")

@do_report.route('/do_report01data' ,methods=['GET','POST'])
def do_report01data():
    date = request.form['f_order_date1']
    date_i = datetime.datetime.strptime(date, '%Y-%m-%d')
    date_r = datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%d/%m/%Y')
    plant = request.form['p_id']
    # print (plant)
    with conn :
        cur = conn.cursor()
        if len(plant) < 1 :
            sql = 'select  a.plant,a.dn_number,b.picking_datetime,b.loading_datetime,b.dev_datetime,a.item_line,' \
                  'a.item_name,a.so_qty,a.do_qty,a.do_unit,b.sold_to_name,b.ship_name,b.truck_no,b.text_detail,' \
                  'b.sales_code,b.ship_phone from dn_i a , dn_h b where  a.dn_number = b.dn_number ' \
                  'and cast(b.picking_datetime as date) = ? order by b.picking_datetime,a.dn_number,a.item_line    '
            cur.execute(sql,(date_i))
        else :
            sql = 'select  a.plant,a.dn_number,b.picking_datetime,b.loading_datetime,b.dev_datetime,a.item_line,' \
                  'a.item_name,a.so_qty,a.do_qty,a.do_unit,b.sold_to_name,b.ship_name,b.truck_no,b.text_detail,' \
                  'b.sales_code,b.ship_phone from dn_i a , dn_h b where  a.dn_number = b.dn_number and a.plant = ? ' \
                  'and cast(b.picking_datetime as date) = ? order by b.picking_datetime,a.dn_number,a.item_line    '
            cur.execute(sql,(plant,date_i))
        row = cur.fetchall()
        for i in row :
            i[2] = (i[2].strftime('%d-%m-%Y %H:%M:%S'))
            i[3] = (i[3].strftime('%d-%m-%Y %H:%M:%S'))
            i[4] = (i[4].strftime('%d-%m-%Y %H:%M:%S'))

        return render_template("do_report01data.html", rows = row , plant = plant , date_r = date_r, f_date1 = date)