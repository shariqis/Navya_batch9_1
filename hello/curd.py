from flask import *
import sqlite3

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def stud_reg():
    if request.method=="POST":
        n=request.form['fname']
        p=request.form['ph']
        e=request.form['em']
        with sqlite3.connect("stud.db") as con:
            cur=con.cursor()
            cur.execute("""
            insert into student (name,email,phone) values 
            (?,?,?)""", (n,e,p))
            con.commit()
        return 'success'
    else:
        return render_template('studreg.html')

@app.route('/Sview')
def stuView():
    con=sqlite3.connect('stud.db')
    con.row_factory=sqlite3.Row
    cur=con.cursor()
    cur.execute("select * from student")
    rows=cur.fetchall()
    
    return render_template('stud_view.html',data=rows)

@app.route('/sd/<int:id>')
def Sdel(id):
    print(id)
    with sqlite3.connect("stud.db") as con:
        cur=con.cursor()
        cur.execute("delete from student where id=?",(id,))
        con.commit()
    return 'Successfully Deleted' 

if __name__=="__main__":
    app.run(debug=True)