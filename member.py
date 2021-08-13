from flask import Blueprint,render_template,request,url_for,session,redirect
import pyodbc

member = Blueprint('member',__name__)


@member.route("/register")
def register():
    return render_template("register.html")

@member.route("/login")
def login():
    return  render_template('login.html')

@member.route("/logoff")
def logoff():
    session.clear()
    print (session)
    return  render_template('login.html')

@member.route("/checklogin/",methods=['GET','POST'])
def checklogin():
    if request.method == "POST" :
        id_p1 = request.form["ID"]
        password1 = request.form["password"]
        id_p2 = request.form["ID"]
        password2 = request.form["password"]
        with conn :
            cur1 = conn.cursor()
            sql1 = "select * from member_user where id= ? and password= ? and status = '1'"
            cur1.execute(sql1,id_p1,password1)
            rows1 = cur1.fetchall()

        with conn:
            cur2 = conn.cursor()
            sql2 = "select * from member_user where id= ? and password= ? and status = '0'"
            cur2.execute(sql2,id_p2,password2)
            rows2 = cur2.fetchall()
            if len(rows1) > 0  and len(rows2) < 1:
                session['username'] = id_p1
                session['fname'] = rows1[0][1]
                session['lname'] = rows1[0][2]
                session['depart'] = rows1[0][5]
                print (session['depart'])
                session.permanet = True
                return render_template('index.html')
            if len(rows1) == 0  and len(rows2) > 0 :
                return "User โดน Lock โปรดติดต่อฝ่าย IT"
            else :
                return "Username หรือ รหัสผ่านไม่ถูกต้อง"

@member.route("/create_member/",methods=['GET','POST'])
def create_member():
    if request.method == "POST":
        id_p = request.form['ID']
        f_name = request.form['firstname']
        l_name = request.form['lastname']
        sex = request.form['sex']
        co_name = request.form['company']
        de_name = request.form['department']
        posit = request.form['position']
        telephone = request.form['telephone']
        email = request.form['email']
        password = request.form['inputPassword6']
        with conn :
            cur = conn.cursor()
            sql1 = " select * from member_user where id = ? "
            cur.execute(sql1, (id_p))
            rows1 = cur.fetchall()
            if len(rows1) > 0 :
                return "ขอภัย รหัสนี้ได้ลงทะเบียนไว้แล้ว "
            if len(rows1) < 1 :
                with  conn :
                    cur = conn.cursor()
                    sql = "insert into member_user  (id,firstname,lastname,sex,companyname,department," \
                          "telephone,position,email,password,status) VALUES (?,?,?,?,?,?,?,?,?,?,1) "
                    cur.execute(sql,[id_p, f_name, l_name, sex, co_name, de_name, telephone,
                                 posit, email, password])
                return render_template("register.html")
            else :
                return  "Error โปรดติดต่อ ฝ่าย IT"

@member.route("/memberuser")
def memberuser():
    if "username" not in session:
        return render_template("login.html")
    else :
        return render_template('memberuser.html')

@member.route("/showdatamember")
def showdatamember():
    return  'Ok'


@member.route("/edit_user")
def edit_user():
    if "username" not in session:
        return render_template("login.html")
    else :
        with conn :
            cur = conn.cursor()
            sql1 = " select * from member_user where id = ? "
            cur.execute(sql1, (session['username']))
            rows1 = cur.fetchall()
            print (rows1)
            return render_template('edit_user.html',datas = rows1)

@member.route("/edit_user_member")
def edit_user_member():
    if "username" not in session:
        return render_template("login.html")
    else :
        with conn :
            cur = conn.cursor()
            sql1 = " select * from member_user where id = ? "
            cur.execute(sql1, (session['username']))
            rows1 = cur.fetchall()
            print (rows1)
            return render_template('edit_user_member.html',datas = rows1)

@member.route("/editmember",methods=['GET','POST'])
def editmember():
    if "username" not in session:
        return render_template("login.html")
    if request.method == "POST":
        id_p = request.form['ID']
        f_name = request.form['firstname']
        l_name = request.form['lastname']
        sex = request.form['sex']
        co_name = request.form['company']
        de_name = request.form['department']
        posit = request.form['position']
        telephone = request.form['telephone']
        email = request.form['email']
        password = request.form['inputPassword6']
        with conn :
            cur = conn.cursor()
            sql1 = "update member_user set  firstname = ? ,lastname = ?,sex = ?,companyname = ?,department = ?," \
                          "position = ?,telephone = ?,email = ?,password = ? where id = ? "
            cur.execute(sql1, (f_name,l_name,sex,co_name,de_name,posit,telephone,email,password,id_p))
        with conn:
            cur2 = conn.cursor()
            sql2 = " select * from member_user where id = ? "
            cur2.execute(sql2, (id_p))
            rows1 = cur2.fetchall()
            return render_template('edit_user.html',datas = rows1)

#edite_member_list
@member.route("/edit_member",methods=['GET','POST'])
def edit_member():
    if "username" not in session:
        return render_template("login.html")
    if request.method == "POST":
        id_p = request.form['ID']
        f_name = request.form['firstname']
        l_name = request.form['lastname']
        sex = request.form['sex']
        co_name = request.form['company']
        de_name = request.form['department']
        posit = request.form['position']
        telephone = request.form['telephone']
        email = request.form['email']
        password = request.form['inputPassword6']
        with conn :
            cur = conn.cursor()
            sql1 = "update member_user set  firstname = ? ,lastname = ?,sex = ?,companyname = ?,department = ?," \
                          "position = ?,telephone = ?,email = ?,password = ? where id = ? "
            cur.execute(sql1, (f_name,l_name,sex,co_name,de_name,posit,telephone,email,password,id_p))
        with conn:
            cur2 = conn.cursor()
            sql2 = " select * from member_user"
            cur2.execute(sql2)
            rows1 = cur2.fetchall()
            return render_template('member_list.html',datas = rows1)


@member.route("/member_list_select")
def member_list_select():
    return render_template('member_list_select.html')

@member.route("/member_list")
def member_list():
    if "username" not in session:
        return render_template("login.html")
    else :
        with conn :
            cur = conn.cursor()
            sql1 = " select * from member_user "
            cur.execute(sql1)
            rows1 = cur.fetchall()
            print (rows1)
            return render_template('member_list.html',datas = rows1)

@member.route("/delete_member/<string:ID>",methods=['GET','POST'])
def delete_member(ID):
    if "username" not in session:
        return render_template("login.html")
    if request.method == "GET":
        with conn:
            cur = conn.cursor()
            sql1 = "delete member_user where id = ? "
            cur.execute(sql1,(ID))
            conn.commit()

            sql2 = " select * from member_user "
            cur.execute(sql2)
            rows1 = cur.fetchall()

            return render_template('member_list.html',datas = rows1)
