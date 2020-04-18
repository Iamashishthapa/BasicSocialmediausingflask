from flask import Flask,url_for,render_template,request,session,redirect,flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 

app = Flask(__name__)
app.secret_key="ashish123"
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class users(db.Model):
    _id = db.Column("id",db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    
    def __init__(self,name,email,password):
        self.name=name
        self.email=email 
        self.password=password

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/signup",methods=['GET', 'POST'])
def signup():
    if "user" in session:
        user=session["user"]
        return redirect(url_for("welcome",user=user))
    else:
        if request.method == "POST":
            user = request.form['user']
            email =request.form['email']
            password =request.form['pw']
            session["user"] = user
            usr=users(user,email,password)
            db.session.add(usr)
            db.session.commit()
            return redirect(url_for("welcome",user=user))
        else:
            return render_template('signup.html')

@app.route("/login",methods=['GET', 'POST'])
def login():
    if "user" in session:
        user = session["user"]
        return redirect(url_for("welcome",user=user))
    else:
        if request.method == "POST":
            user = request.form['user']
            password = request.form['pw']
            found_user = users.query.filter_by(name=user).first()
            if found_user:
                if password == found_user.password:
                    session["user"] = user
                    # session["email"]=found_user.email
                    return redirect(url_for('welcome',user=user))
                else:
                    flash("Wrong Password","info")
            else: 
                flash("User Not found","info")
                return redirect(url_for('signup'))  
        return render_template("login.html")

@app.route("/welcome",methods=['GET', 'POST'])
def welcome():
    if "user" in session:
        user = session["user"]
        if request.method == "POST":
            email=request.form["email"]
            session.email=email
            found_user= users.query.filter_by(name=user).first()
            found_user.email=email
        return render_template('welcome.html',user=user)
    else:
        return redirect(url_for("signup"))

@app.route("/logout")
def logout():
    session.pop("user" , None)
    return redirect(url_for("login"))

@app.route("/display")
def display():
    user = users.query.all()
    return render_template("display.html",user=user)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

