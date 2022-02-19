from flask import Flask,render_template,request,redirect,url_for
import sqlite3
app = Flask(__name__)

# c.execute('create table student_info(name text,course text,fees integer)')


@app.route("/", methods = ["GET","POST"])

def index():
    msg=''
    row=''
    if (request.method == "POST"):
        name = request.form['name']
        course = request.form['course']
        fees = request.form['fees']
        conn = sqlite3.connect('student.db')

        c = conn.cursor()
        c.execute("insert into student_info values('"+name+"','"+course+"',"+fees+")")

        # c.execute('select * from student_info')
        # row = c.fetchall()

        conn.commit()
        conn.close()
        msg='The record is inserted'
    return render_template('index.html',msg=msg,row=row)
@app.route("/display")
def display():
    row=""
    conn = sqlite3.connect("student.db")
    c = conn.cursor()
    c.execute('select * from student_info')
    row = c.fetchall()
    conn.commit()
    conn.close()
    return render_template("index.html",row=row)

@app.route("/delete/<string:name>/")
def delete(name):
    name = name
    conn = sqlite3.connect("student.db")
    c = conn.cursor()
    c.execute("delete from student_info where name = '"+name+"'")
    conn.commit()
    conn.close()
    return render_template("delete.html",name=name)

@app.route("/edit/<string:name>/")
def edit(name):
    name = name
    conn = sqlite3.connect("student.db")
    c = conn.cursor()
    c.execute("select * from student_info where name = '"+name+"'")
    row = c.fetchall()
    conn.commit()
    conn.close()
    return render_template("edit.html", name=name, row=row)
   
if __name__ == '__main__':
    app.run(debug='True')