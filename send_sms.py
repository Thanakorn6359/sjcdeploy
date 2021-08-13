import pyodbc
from datetime import datetime,timedelta
import requests
import datetime
import os
import glob
import shutil
from time import strftime
import time




conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                        'Server=TICSERVER\SQLEXPRESS;'
                        'uid=sa;pwd=sjc@#2017;'
                        'Database=sjc_cp;'
                        'autocommit=True')

with conn :
    cur01 = conn.cursor()
    sql01 = "select dn_number,so_number,doc_date,dev_datetime,sold_to_code,sold_to_name,ship_code,ship_name,ship_phone " \
            "from dn_h where ship_phone <> '' and  left(ship_phone,2) not in ('03','02') " \
            "and cast(dev_datetime  as date ) = cast(getdate() as date) "
    cur01.execute(sql01)
    row01 = cur01.fetchall()
with conn:
    cur02 = conn.cursor()
    sql02 = "select dn_number,so_number from T_send_sms where cast(dev_datetime  as date ) = cast(getdate() as date)"
    cur02.execute(sql02)
    row02 = cur02.fetchall()
    a = []
    for t_sms in row02 :
        a.append(t_sms[0])
    #print(a)
    for i in row01 :
        #print(i[0].strip())
        if (i[0]).strip() in a :
            #print('in a')
            with conn :
                cur04 = conn.cursor()
                sql04 = "update T_send_sms set dn_number = ? , so_number = ?,doc_date=?,dev_datetime = ?,sold_to_code = ? " \
                        ",sold_to_name = ? ,ship_code = ?, ship_name = ? ,ship_phone = ? where dn_number = ? "
                cur04.execute(sql04,(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[0]))

        else :
            #print('not in a')
            with conn :
                cur03 = conn.cursor()
                sql03 = "insert into T_send_sms (dn_number,so_number,doc_date,dev_datetime,sold_to_code,sold_to_name," \
                        "ship_code,ship_name,ship_phone) values (?,?,?,?,?,?,?,?,?) "
                cur03.execute(sql03,(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]))

with conn :
    cur05 = conn.cursor()
    sql05 = "select dn_number, dev_datetime,ship_phone,status_sms,sold_to_code from T_send_sms " \
            "where cast(dev_datetime  as date ) = cast(getdate() as date)"
    cur05.execute(sql05)
    row05 = cur05.fetchall()
    for i in row05 :
        date = i[1].strftime("%Y-%m-%d")
        time = i[1].strftime("%H:%M:%S")
        # print(date)
        # print(time)
        r_number = (str(i[0])).strip()
        if time == '00:00:00' :
            print('00')
        if time != '00:00:00' and i[3] == '0':
            #print(i[1])
            now = datetime.datetime.now()
            nowp5 = now + timedelta(minutes=7.00)
            send_date = nowp5.strftime("%Y-%m-%d %H:%M:%S")
            print (nowp5)
            message = 'สินค้าของท่านกำลังเตรียมจัดส่ง คัดลอกเลขที่ใบจัดส่ง ' + r_number + ' นำไปเช็คสินค้าของท่านได้ที่ ' + 'https://lin.ee/812EP5G'
            phone = (str(i[2]))
            phone = phone.strip()
            phone2 = ''
            for p in phone:
                if p.isdigit():
                    phone2 += (str(p))
            phone2 = phone2.strip()
            print(phone2)
            phone2 = '0835405472'
            sender = 'SJCGROUP'

            print(send_date)
            print(message)
            print(phone2)


            # funcion send sms

            def send_sms(message, phone, sender, send_date):
                url = "https://portal-otp.smsmkt.com/api/send-message"
                headers = {
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                    "api_key": "ee6cced6efd7fc76b304af25c6d39a16",
                    "secret_key": "5vNqldMPdgmuVBcB",
                }
                payload = {
                    "message": message,
                    "phone": phone2,
                    "sender": sender,
                    "send_date": send_date,
                }
                response = requests.request("POST", url, json=payload, headers=headers)
                print(response.text)


            send_sms(message, phone, sender, send_date)
            send_datetime = datetime.datetime.strptime(send_date, '%Y-%m-%d %H:%M:%S')

            with conn:  # เมื่อส่งเสร็จ update status SMS เป็น 1
                cur06 = conn.cursor()
                sql06 = "update T_send_sms set status_sms ='1' ,datetime_sms = ? where dn_number = ? "
                cur06.execute(sql06, (send_datetime,i[0]))

