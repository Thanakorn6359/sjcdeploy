# -*- coding: utf-8 -*-
import pyodbc
from flask import Flask,request,abort
import os
import json
import requests
#from OpenSSL import SSL
#print (SSL._CERTIFICATE_PATH_LOCATIONS)



conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                        'Server=TICSERVER\SQLEXPRESS;'
                        'uid=sa;pwd=sjc@#2017;'
                        'Database=sjc_cp;'
                        'autocommit=True')


#------------ end import zone -----------

app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def webhook():
    if request.method == 'POST':
        payload = request.json
        Reply_token = payload['events'][0]['replyToken']
        print(Reply_token)
        message = payload['events'][0]['message']['text']
        #message = message[0:10]
        print(message)
        if len(message) == 10:
            with conn :
                cur01 = conn.cursor()
                sql01 = "select item_line,item_name,do_qty,do_unit,(select sold_to_name " \
                        "from dn_h where dn_number= dn_i.dn_number)  from dn_i where dn_number = ?"
                cur01.execute(sql01,message)
                row01 = cur01.fetchall()

                n = 1
                a = []
                for i in row01 :
                    a.append( (str(n)) + '.' + ' ' +  (str(i[1])).strip() + ' ' +  (str(i[2])).strip() + ' ' + (str(i[3])).strip() + '\n')
                    soldto = i[4]
                    n += 1
                header = 'ลูกค้า '+ soldto + 'สินค้าที่จะจัดส่งให้วันนี้\n'
                footer = 'โปรดเตรียมสถานที่ลงสินค้าให้พร้อม เพื่อความรวดเร็วในการลงสินค้า นะ แบระ ~~~~'
                str1 = ''.join(a)
                data = header + '\n' + str1 + '\n' + footer


                Reply_messasge = data
                ReplyMessage(Reply_token,Reply_messasge,
                'BOElfOP7qJrEo4e4geMTQF74M7A/Gn4fRWcwYXKKPxDFFHSKUcQCyoQR5s8NwSo0maBuQ6ydMpcLCmY9ITc0/3KErdBqwnbvpN4kQAgMno7ej08nmO98wGeHN6V57NNDFHf8pZCXdd4EpWALwEmH9wdB04t89/1O/w1cDnyilFU=') #ใส่ Channel access token
        else :
            Reply_messasge = 'ใส่เลขที่ใบส่งสินค้าได้เลย แบระๆๆ แล้วมาดูกันว่าวันนี้สินค้าที่ต้องได้รับมีอะไรบ้าง'
            ReplyMessage(Reply_token, Reply_messasge,
                         'BOElfOP7qJrEo4e4geMTQF74M7A/Gn4fRWcwYXKKPxDFFHSKUcQCyoQR5s8NwSo0maBuQ6ydMpcLCmY9ITc0/3KErdBqwnbvpN4kQAgMno7ej08nmO98wGeHN6V57NNDFHf8pZCXdd4EpWALwEmH9wdB04t89/1O/w1cDnyilFU=')  # ใส่ Channel access token

        return request.json, 200
    else :
        abort(400)
def ReplyMessage(Reply_token, TextMessage, Line_Acees_Token):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    Authorization = 'Bearer {}'.format(Line_Acees_Token)
    print(Authorization)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization':Authorization
                 }
    data = {
        "replyToken":Reply_token,
        "messages":[{
                    "type":"text",
                    "text":TextMessage
                }]
             }
    data = json.dumps(data)
    r = requests.post(LINE_API, headers=headers, data=data)
    return 200






















# def hello():
#     return "Hello World!"
#
# #------------insert new code below --------
# @app.route('/webhook' , methods = ['POST'])
# def webhook():
#     new_event = request.json
#     event_reply = new_event['events'][0]['replyToken']
#     sendtext(event_reply)
#     return '',200
#
# def sendtext(event_reply):
#     token = 'xBQnQTfLOseB4Zg6az/7EZPoQOSerMqYXeGcKqR9htItgZBgXZHdSP//Ek5ugB2AmaBuQ6ydMpcLCmY9ITc0/3KErdBqwnbvpN4kQAgMno6KcxbYWvLD6CYtCUtaJ+2VG31hWuQTK5r5MdhGDNIq9AdB04t89/1O/w1cDnyilFU=' #edit token here
#     reply_url = 'https://api.line.me/v2/bot/message/reply'
#     Authorization = 'Bearer {}'.format(token)
#     headers = {'Content-Type':'application/json; charset=UTF-8','Authorization':Authorization}
#     data = json.dumps({"replyToken":event_reply,"messages":[{"type":"text","text":"ได้หมด"}]})
#     r = requests.post(reply_url, headers=headers, data=data)
#
# #------------ end edit zone  --------
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=int(os.environ.get('PORT','5100')))
    #app.run(host='192.168.100.10', debug=True, ssl_context='adhoc' , port=int(os.environ.get('PORT','5100')))
