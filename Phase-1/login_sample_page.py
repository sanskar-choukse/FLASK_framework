from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == 'admin' and password == '112233':
            return "Login successful"
        else:
            return "Invalid Credentials"
    return render_template('login_simple_page.html')    
     
if __name__== '__main__':
    app.run(debug=True)     