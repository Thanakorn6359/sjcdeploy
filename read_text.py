import pyodbc
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

path = "D:\\interface\\DN\\inbound\\"
to_p =  "D:\\interface\\DN\\archive\\"
all_file = os.listdir("D:\\interface\\DN\\inbound\\")
#print(all_file)

def interface() :
    for i in all_file :
        p = i
        f = p.split(',')   # split เป็น List 1 data
        f = ''.join(f)    # แปลง list เป็น Str
        if (f[0:7]) == 'DO_CP_H' : # เช็คไฟล์ Do_heder
            data1 = (path + f)
            data2 = (to_p + f)
           # data1 = f.split(',')
            #print (data1)
            try : #อ่านตาม readlines ทีละบรรทัด
                file = open(data1, encoding="utf8")
                datas = file.readlines()
                file.close()
                #print (d)
                for i in datas:
                    do =  i.split("\t") #split ไฟล์ให้ Loop ออกมาทีละแถว
                    #print(do[0])
                    if (do[-1][1:2]) == "\n" : #ถ้าแถวสุดท้ายมี \n เอาออก
                        do[-1] = (do[-1][0])

                    if do[5] == '00000000':
                        do[5] = None
                    else :
                        do[5] = datetime.datetime.strptime((do[5]),'%Y%m%d')

                    if do[6] == '00000000':
                        do[6] = None
                    else:
                        do[6] = datetime.datetime.strptime((do[6] + do[7]),'%Y%m%d%H%M%S')

                    if do[8] == '00000000':
                        do[8] = None
                    else:
                        do[8] = datetime.datetime.strptime((do[8] + do[9]),'%Y%m%d%H%M%S')

                    if do[10] == '00000000':
                        do[10] = None
                    else:
                        do[10] = datetime.datetime.strptime((do[10] + do[11]),'%Y%m%d%H%M%S')

                    if do[12] == '00000000':
                        do[12] = None
                    else :
                        do[12] = datetime.datetime.strptime((do[12] + do[13]),'%Y%m%d%H%M%S')

                    if do[14] == '00000000':
                        do[14] = None
                    else:
                        do[14] = datetime.datetime.strptime((do[14] + do[15]),'%Y%m%d%H%M%S')

                    if do[31] == '00000000':
                        do[31] = None
                    else:
                        do[31] = datetime.datetime.strptime((do[31] + do[32]),'%Y%m%d%H%M%S')


                    do[34]    = (do[34] + do[35])
                    #print(do[34])
                    if do[34] == '00000000000000' :
                        do[34] = None
                    else :
                        do[34] = datetime.datetime.strptime((do[34]),'%Y%m%d%H%M%S')


                    print(do)
                    with conn:
                        cur = conn.cursor()
                        sql = "select * from dn_h where dn_number = ?"
                        cur.execute(sql,(do[0]))
                        rows = cur.fetchall()
                        if len(rows) == 0 :
                            with conn:
                                cur1 = conn.cursor()
                                sql1 = "insert into dn_h (dn_number,so_number,dev_type,dist_ch,division,doc_date,picking_datetime,	" \
                                       "trans_plan_datetime,loading_datetime,plan_gi_datetime,dev_datetime,sold_to_code,sold_to_name,ship_code,ship_name," \
                                       "ship_street,ship_city,ship_dataline,ship_phone,shipping_point,ship_cond,ship_type,sales_code,truck_no," \
                                       "text_detail,Create_user,create_datetime,change_user,change_datetime,LA,LO,status) " \
                                       "values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
                                cur1.execute(sql1, (do[0],do[1],do[2],do[3],do[4],do[5],do[6],do[8],do[10],do[12],do[14]
                                                    ,do[16],do[17],do[18],do[19],do[20],do[21],do[22],do[23],do[24],do[25],do[26]
                                                    ,do[27],do[28],do[29],do[30],do[31],do[33],do[34],do[36],do[37],do[38]))
                        else :
                            with conn:
                                cur2 = conn.cursor()
                                sql2 = "update dn_h set dn_number = ?,so_number = ?,dev_type = ?,dist_ch = ?,division = ?,doc_date = ?,picking_datetime= ?,	" \
                                       "trans_plan_datetime = ?,loading_datetime = ?,plan_gi_datetime =?,dev_datetime = ?,sold_to_code =?,sold_to_name =?,ship_code =?,ship_name =?," \
                                       "ship_street = ?,ship_city =?,ship_dataline =?,ship_phone =?,shipping_point =?,ship_cond =?,ship_type =?,sales_code =?,truck_no =?," \
                                       "text_detail =?,Create_user =?,create_datetime =?,change_user =?,change_datetime =?,LA =?,LO =?,status =?  where dn_number = ? "
                                cur2.execute(sql2, ( do[0],do[1],do[2],do[3],do[4],do[5],do[6],do[8],do[10],do[12],do[14]
                                                     ,do[16],do[17],do[18],do[19],do[20],do[21],do[22],do[23],do[24],do[25],do[26]
                                                     ,do[27],do[28],do[29],do[30],do[31],do[33],do[34],do[36],do[37],do[38],do[0] ))
            except FileNotFoundError :
                print ("no file")
            else :

                print ('interface ok :' + f)
                shutil.move(data1,data2)
            #print (data1)
            #print (data2)

        #dn_item ------------------------------------------------

        if (f[0:7]) == 'DO_CP_I' : # เช็คไฟล์ Do_ITEM
            data1 = (path + f)
            data2 = (to_p + f)
            try : #อ่านตาม readlines ทีละบรรทัด
                file = open(data1, encoding="utf8")
                datas = file.readlines()
                file.close()
                #print (d)
                for i in datas:
                    do =  i.split("\t") #split ไฟล์ให้ Loop ออกมาทีละแถว
                    if (do[-1][1:2]) == "\n" : #ถ้าแถวสุดท้ายมี \n เอาออก
                        do[-1] = (do[-1][0])
                    do[4] = (int(do[4][:-5]))
                    do[6] = (int(do[6][:-5]))
                    with conn:
                        cur = conn.cursor()
                        sql = "select * from dn_i where dn_number = ? and item_line = ?"
                        cur.execute(sql,(do[0],do[1]))
                        rows = cur.fetchall()
                        if len(rows) == 0 :
                            with conn:
                                cur1 = conn.cursor()
                                sql1 = "insert into dn_i (dn_number,item_line,item_code,item_name,so_qty,so_unit,do_qty" \
                                       ",do_unit,unit_weight,plant,sloc,status )" \
                                       "values (?,?,?,?,?,?,?,?,?,?,?,?)"
                                cur1.execute(sql1, (do[0],do[1],do[2],do[3],do[4],do[5],do[6],do[7],do[8],do[9],do[10],do[11]))
                        else :
                            with conn:
                                cur2 = conn.cursor()
                                sql2 = "update dn_i set dn_number =?,item_line = ?,item_code = ?,item_name = ?,so_qty =?" \
                                       ",so_unit = ? ,do_qty =?,do_unit =?,unit_weight =?,plant =?,sloc =?,status=? " \
                                       "where dn_number =? and item_line = ? "
                                cur2.execute(sql2, (do[0],do[1],do[2],do[3],do[4],do[5],do[6],do[7],do[8],do[9],do[10],do[11],do[0],do[1]))
            except FileNotFoundError :
                print ("no file")
            else :

                print ('interface ok :' + f)
                shutil.move(data1,data2)
            #print (data1)
            #print (data2)
        # else :
        #     print ('ไฟล์เสียชื่อไม่ตรง')



# loop file in dir


# i = 1
# while i > 0:
#     interface()
#     #print(i, end = ', ')
#     #i = i + 1
#     time.sleep(10)

interface ()