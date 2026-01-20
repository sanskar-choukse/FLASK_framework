from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/sample', methods=['POST'])
def login():
    username = request.form.get('username')      #use of request for read usernae,
    password = request.form.get('password')      #use of request for read password,

    # """if username == 'sanskar' and password == 'sanskar@123':        #if morethan 1 credential so we will use of dictionary
    #     return render_template('welcome.html', name=username)"""
    
    valid_user={
        'admin':'123',
        'sanskar':'sanskar@123',
        'rajat':'raj',
        'shyam':'radha'
    }
    
    if username in valid_user and password == valid_user[username]:
        return render_template('welcome_login_page.html',name=username)
    else:
        return 'Invalid username or password'

if __name__ == '__main__':
    app.run(debug=True)
