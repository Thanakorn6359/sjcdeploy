from flask import render_template,request,url_for,redirect,Blueprint
import pyodbc
#import datetime
from datetime import  timedelta,datetime


do_status = Blueprint('do_status',__name__)
conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                        'Server=TICSERVER\SQLEXPRESS;'
                        'uid=sa;pwd=sjc@#2017;'
                        'Database=sjc_cp;'
                        'autocommit=True')


@do_status.route('/delivery_order')
def delivery_order():
    return render_template("delivery_order.html")


@do_status.route('/do')
def do():
    # with conn :
    #     cur = conn.cursor()
    #     sql = "select dn_number,"
    return render_template("do.html")

@do_status.route('/do_realtime')
def do_realtime():
    with conn :
        cur = conn.cursor()
        sql = "select a.dn_number,a.plant,a.item_line,a.item_code,a.item_name,a.do_qty,a.do_unit,b.picking_datetime," \
               "b.loading_datetime,b.dev_datetime,b.sold_to_name,b.ship_name ,b.truck_no,b.text_detail " \
               "from dn_i a , dn_h b where a.dn_number = b.dn_number and b.status <> '0' and a.status <> '0' " \
              "and cast(picking_datetime as date) = cast(getdate() as date) order by picking_datetime   "
        cur.execute(sql)
        row = cur.fetchall()
        for i in row :
            date_now = i[7].strftime('%d %B %Y')

            i[7] = (i[7].strftime('%H:%M:%S'))[:5]
            i[8] = (i[8].strftime('%H:%M:%S'))[:5]
            i[9] = (i[9].strftime('%H:%M:%S'))[:5]

        return render_template("do_realtime.html", data=row , datenow = date_now)

#------------------------------------------------------------------------------------------------------------

@do_status.route('/delivery_order_f201')
def delivery_order_f201():
    return render_template("delivery_order_f201.html")

@do_status.route('/do_realtime_f201')
def do_realtime_f201():
    with conn :
        cur = conn.cursor()
        sql = "select a.dn_number,a.plant,a.item_line,a.item_code,a.item_name,a.do_qty,a.do_unit,b.picking_datetime," \
               "b.loading_datetime,b.dev_datetime,b.sold_to_name,b.ship_name ,b.truck_no,b.text_detail " \
               "from dn_i a , dn_h b where a.dn_number = b.dn_number and b.status <> '0' and a.status <> '0' " \
              "and cast(picking_datetime as date) = cast(getdate() as date) and a.plant = 'f201'  order by picking_datetime  "
        cur.execute(sql)
        row = cur.fetchall()
        for i in row :
            date_now = i[7].strftime('%d %B %Y')

            i[7] = (i[7].strftime('%H:%M:%S'))[:5]
            i[8] = (i[8].strftime('%H:%M:%S'))[:5]
            i[9] = (i[9].strftime('%H:%M:%S'))[:5]

        return render_template("do_realtime_f201.html", data=row , datenow = date_now)

#------------------------------------------------------------------------------------------------------------

@do_status.route('/delivery_order_f202')
def delivery_order_f202():
    return render_template("delivery_order_f202.html")

@do_status.route('/do_realtime_f202')
def do_realtime_f202():
    with conn :
        cur = conn.cursor()
        sql = "select a.dn_number,a.plant,a.item_line,a.item_code,a.item_name,a.do_qty,a.do_unit,b.picking_datetime," \
               "b.loading_datetime,b.dev_datetime,b.sold_to_name,b.ship_name ,b.truck_no,b.text_detail " \
               "from dn_i a , dn_h b where a.dn_number = b.dn_number and b.status <> '0' and a.status <> '0' " \
              "and cast(picking_datetime as date) = cast(getdate() as date) and a.plant = 'f202'  order by picking_datetime  "
        cur.execute(sql)
        row = cur.fetchall()
        for i in row :
            date_now = i[7].strftime('%d %B %Y')

            i[7] = (i[7].strftime('%H:%M:%S'))[:5]
            i[8] = (i[8].strftime('%H:%M:%S'))[:5]
            i[9] = (i[9].strftime('%H:%M:%S'))[:5]

        return render_template("do_realtime_f202.html", data=row , datenow = date_now)

#------------------------------------------------------------------------------------------------------------

@do_status.route('/delivery_order_f203')
def delivery_order_f203():
    return render_template("delivery_order_f203.html")

@do_status.route('/do_realtime_f203')
def do_realtime_f203():
    with conn :
        cur = conn.cursor()
        sql = "select a.dn_number,a.plant,a.item_line,a.item_code,a.item_name,a.do_qty,a.do_unit,b.picking_datetime," \
               "b.loading_datetime,b.dev_datetime,b.sold_to_name,b.ship_name ,b.truck_no,b.text_detail " \
               "from dn_i a , dn_h b where a.dn_number = b.dn_number and b.status <> '0' and a.status <> '0' " \
              "and cast(picking_datetime as date) = cast(getdate() as date) and a.plant = 'f203'  order by picking_datetime  "
        cur.execute(sql)
        row = cur.fetchall()
        for i in row :
            date_now = i[7].strftime('%d %B %Y')

            i[7] = (i[7].strftime('%H:%M:%S'))[:5]
            i[8] = (i[8].strftime('%H:%M:%S'))[:5]
            i[9] = (i[9].strftime('%H:%M:%S'))[:5]

        return render_template("do_realtime_f203.html", data=row , datenow = date_now)

#------------------------------------------------------------------------------------------------------------

@do_status.route('/delivery_order_f204')
def delivery_order_f204():
    return render_template("delivery_order_f204.html")

@do_status.route('/do_realtime_f204')
def do_realtime_f204():
    with conn :
        cur = conn.cursor()
        sql = "select a.dn_number,a.plant,a.item_line,a.item_code,a.item_name,a.do_qty,a.do_unit,b.picking_datetime," \
               "b.loading_datetime,b.dev_datetime,b.sold_to_name,b.ship_name ,b.truck_no,b.text_detail " \
               "from dn_i a , dn_h b where a.dn_number = b.dn_number and b.status <> '0' and a.status <> '0' " \
              "and cast(picking_datetime as date) = cast(getdate() as date) and a.plant = 'f204'  order by picking_datetime  "
        cur.execute(sql)
        row = cur.fetchall()
        for i in row :
            date_now = i[7].strftime('%d %B %Y')

            i[7] = (i[7].strftime('%H:%M:%S'))[:5]
            i[8] = (i[8].strftime('%H:%M:%S'))[:5]
            i[9] = (i[9].strftime('%H:%M:%S'))[:5]

        return render_template("do_realtime_f204.html", data=row , datenow = date_now)

#------------------------------------------------------------------------------------------------------------

@do_status.route('/delivery_order_f205')
def delivery_order_f205():
    return render_template("delivery_order_f205.html")

@do_status.route('/do_realtime_f205')
def do_realtime_f205():
    with conn :
        cur = conn.cursor()
        sql = "select a.dn_number,a.plant,a.item_line,a.item_code,a.item_name,a.do_qty,a.do_unit,b.picking_datetime," \
               "b.loading_datetime,b.dev_datetime,b.sold_to_name,b.ship_name ,b.truck_no,b.text_detail " \
               "from dn_i a , dn_h b where a.dn_number = b.dn_number and b.status <> '0' and a.status <> '0' " \
              "and cast(picking_datetime as date) = cast(getdate() as date) and a.plant = 'f205'  order by picking_datetime  "
        cur.execute(sql)
        row = cur.fetchall()
        for i in row :
            date_now = i[7].strftime('%d %B %Y')

            i[7] = (i[7].strftime('%H:%M:%S'))[:5]
            i[8] = (i[8].strftime('%H:%M:%S'))[:5]
            i[9] = (i[9].strftime('%H:%M:%S'))[:5]

        return render_template("do_realtime_f205.html", data=row , datenow = date_now)

#------------------------------------------------------------------------------------------------------------

@do_status.route('/delivery_order_f206')
def delivery_order_f206():
    return render_template("delivery_order_f206.html")

@do_status.route('/do_realtime_f206')
def do_realtime_f206():
    with conn :
        cur = conn.cursor()
        sql = "select a.dn_number,a.plant,a.item_line,a.item_code,a.item_name,a.do_qty,a.do_unit,b.picking_datetime," \
               "b.loading_datetime,b.dev_datetime,b.sold_to_name,b.ship_name ,b.truck_no,b.text_detail " \
               "from dn_i a , dn_h b where a.dn_number = b.dn_number and b.status <> '0' and a.status <> '0' " \
              "and cast(picking_datetime as date) = cast(getdate() as date) and a.plant = 'f206'  order by picking_datetime  "
        cur.execute(sql)
        row = cur.fetchall()
        for i in row :
            date_now = i[7].strftime('%d %B %Y')

            i[7] = (i[7].strftime('%H:%M:%S'))[:5]
            i[8] = (i[8].strftime('%H:%M:%S'))[:5]
            i[9] = (i[9].strftime('%H:%M:%S'))[:5]

        return render_template("do_realtime_f206.html", data=row , datenow = date_now)

    # ------------------------------------------------------------------------------------------------------------


@do_status.route('/delivery_order_f221')
def delivery_order_f221():
    return render_template("delivery_order_f221.html")


@do_status.route('/do_realtime_f221')
def do_realtime_f221():
    with conn:
        cur = conn.cursor()
        sql = "select a.dn_number,a.plant,a.item_line,a.item_code,a.item_name,a.do_qty,a.do_unit,b.picking_datetime," \
              "b.loading_datetime,b.dev_datetime,b.sold_to_name,b.ship_name ,b.truck_no,b.text_detail " \
              "from dn_i a , dn_h b where a.dn_number = b.dn_number and b.status <> '0' and a.status <> '0' " \
              "and cast(picking_datetime as date) = cast(getdate() as date) and a.plant = 'f221'  order by picking_datetime  "
        cur.execute(sql)
        row = cur.fetchall()
        for i in row:
            date_now = i[7].strftime('%d %B %Y')

            i[7] = (i[7].strftime('%H:%M:%S'))[:5]
            i[8] = (i[8].strftime('%H:%M:%S'))[:5]
            i[9] = (i[9].strftime('%H:%M:%S'))[:5]

        return render_template("do_realtime_f221.html", data=row, datenow=date_now)

#------------------------------------------------------------------------------------------------------------

@do_status.route('/delivery_order_f241')
def delivery_order_f241():
    return render_template("delivery_order_f241.html")

@do_status.route('/do_realtime_f241')
def do_realtime_f241():
    with conn :
        cur = conn.cursor()
        sql = "select a.dn_number,a.plant,a.item_line,a.item_code,a.item_name,a.do_qty,a.do_unit,b.picking_datetime," \
               "b.loading_datetime,b.dev_datetime,b.sold_to_name,b.ship_name ,b.truck_no,b.text_detail " \
               "from dn_i a , dn_h b where a.dn_number = b.dn_number and b.status <> '0' and a.status <> '0' " \
              "and cast(picking_datetime as date) = cast(getdate() as date) and a.plant = 'f241'  order by picking_datetime  "
        cur.execute(sql)
        row = cur.fetchall()
        for i in row :
            date_now = i[7].strftime('%d %B %Y')

            i[7] = (i[7].strftime('%H:%M:%S'))[:5]
            i[8] = (i[8].strftime('%H:%M:%S'))[:5]
            i[9] = (i[9].strftime('%H:%M:%S'))[:5]

        return render_template("do_realtime_f241.html", data=row , datenow = date_now)


