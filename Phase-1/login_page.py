from flask import Flask,request,redirect,url_for,session,Response

app=Flask(__name__)
app.secret_key = "something"  #use of secret_key when we store data in session



@app.route("/",methods=["GET","POST"])
def login():
    if request.method == "POST":
        username=request.form.get("username")
        password=request.form.get("password")
        
        if  username == "admin" and password == "123":
            session['user'] = username
            return redirect(url_for("welcome"))
        else:
            return Response("Invalid answer",mimetype="Text/plain")     
        
    return '''
        <h2>Login Page</h2>
        <form method="POST">
        <label>username:</lable>
        <input type="text" name="username"><br>
        <label>password:</lable>
        <input type="text" name="password"><br>
        <input type="submit" value="login"><br>
        </from>
        '''
#welcome
@app.route("/welcome")      #if user data store in session
def welcome():
    if "user" in session:
        return f'''<h2>welcome,{session["user"]}</h2>
        <a href="{url_for("logout")}">Logout</a>
    '''        
    return redirect(url_for("login"))    
        
@app.route("/logout")
def logout():
    session.pop('user',None)        # session["user"]=username, session data delete when you will logout 
    return redirect(url_for("login"))
    return redirect(url_for("login"))

#  use for run a file :python filesname.py
if __name__ == "__main__":
    app.run(debug=True)
         
        
        
        
        
        
        
        
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == '1234':
            return "Login Successful ✅"
        else:
            return "Invalid Credentials ❌"

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
        