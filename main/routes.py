from flask import url_for,render_template,request,session,redirect,flash
from main import app
from main.models import  User, Post
from main import db

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/signup",methods=['GET', 'POST'])
def signup():
    if "user" in session:
        user = session["user"]
        return redirect(url_for("welcome",user=user))
    else:
        if request.method == "POST":
            user = request.form['suser']
            email =request.form['semail']
            password =request.form['spw']
            session["user"] = user
            usr=User(user,email,password)
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
            email = request.form['lemail']
            password = request.form['lpw']
            found_email = User.query.filter_by(email=email).first()
            if found_email:
                if password == found_email.password:
                    user = found_email.name
                    session["user"] = user
                    #session["email"]=found_user.email
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
        posted = Post.query.order_by(Post.date_posted.desc()).all()
        return render_template('welcome.html',user=user,posted=posted)
    else:
        return redirect(url_for("signup"))

@app.route("/post/new",methods=['GET', 'POST'])
def newpost():
    if "user" in session:
        if request.method == "POST":
            title = request.form['title']
            content =request.form['content']
            post = Post(title=title,content=content,author=session["user"])
            db.session.add(post)
            db.session.commit()
            return redirect(url_for("welcome",user=session["user"]))
        return render_template("newpost.html")
    else:
        return f"Please Login!"


@app.route("/logout")
def logout():
    session.pop("user" , None)
    return redirect(url_for("login"))

@app.route("/display",)
def display():
    user = User.query.all()
    return render_template("display.html",user=user)
