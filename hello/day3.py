from flask import *

app=Flask(__name__)
app.secret_key="aa"

@app.route('/GstudReg',methods=['GET'])
def mygetmthd():
    name=request.args.get('fname')
    email=request.args.get('em')
    ph=request.args.get('ph')
    print(name,email,ph)
    return 'Success'


@app.route('/PstudReg',methods=['POST'])
def mypostmthd():
    name=request.form['fname']
    email=request.form['em']
    ph=request.form['ph']
    print(name,email,ph)
    return 'Success POST METHOd'

@app.route('/n')
def reg():
    return render_template('d2.html')

@app.route('/succ',methods=['POST','GET'])
def get_data():
    if request.method=="POST":
        data=request.form
        return data
    else:
        return render_template('d2.html')
    
@app.route('/sc')
def set_cook():
    res=make_response("<h1> Cookie is set </h1>")
    res.set_cookie('fname','ammu')  
    return res

@app.route('/gc')
def get_cook():
    name=request.cookies.get('fname')  
    return name

@app.route('/ss')
def set_sess():
    res=make_response('session is set')
    
    session['phon']=9999
    return res

@app.route('/gs')
def get_sess():
    if "phon" in session:
        return str( session['phon'])
    
if __name__=="__main__":
    app.run(debug=True)