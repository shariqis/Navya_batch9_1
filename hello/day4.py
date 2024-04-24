from flask import *
from flask_mail import *

app=Flask(__name__)

app.secret_key="abc"

@app.route('/',methods=['GET','POST'])
def index():
    
    if request.method=="GET":
        return render_template('mydp.html')
    else:
        er="hhhhhhhhhhhhhhhhhhhhh"
        f=request.files['dp']
        f.save(f.filename)
        a=1
        if a==1:
            flash('successfully saved')
        else:
            flash('error')     
        return render_template('mydp.html',error=er)
        # return 'success'



app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']="dummymailid"
app.config['MAIL_PASSWORD']=''
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True

mail=Mail(app)

@app.route('/sm')
def smail():
    msg=Message('subject',sender='dummymilid',recipients=['to address'])
    msg.body='hi my first message in flask'
    msg.send()
    return 'success'
    



if __name__=="__main__":
    app.run(debug=True)