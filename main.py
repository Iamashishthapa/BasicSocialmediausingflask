from flask import Flask,url_for,render_template,request,session,redirect

app = Flask(__name__)
app.secret_key="ashish"

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
            session["user"] = user
            return redirect(url_for("welcome",user=user))
        else:
            return render_template('signup.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/welcome",methods=['GET', 'POST'])
def welcome():
    if "user" in session:
        user = session["user"]
        return render_template('welcome.html',user=user)
    else:
        return redirect(url_for("signup"))

@app.route("/logout")
def logout():
    session.pop("user" , None)
    return redirect(url_for("login"))

if __name__ == '__main__':
    app.run(debug=True)

