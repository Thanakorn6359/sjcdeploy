import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=SJCHSERVER\SJCSQLSERVER;'
                        'uid=sa;pwd=sjc@#2021;'
                        'Database=sale_order_qas')


cursor = conn.cursor()

with conn:
    cur = conn.cursor()
    sql = "select plant_id,so_date from s_order"
    cur.execute(sql)
    conn.commit()

cursor.execute('select plant_id,so_qty from s_order where so_date = (SELECT CAST(GETDATE() AS DATE))')
rows = cursor.fetchall()
for i in rows:
    print (i)