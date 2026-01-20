from flask import Flask,render_template,request,redirect,url_for,flash

app=Flask(__name__)
app.secret_key="My-secret-key"  #use of secret key when we use of session and flash  

@app.route("/",methods=['GET','POST'])
def form():
    if request.method == 'POST':
        name=request.form.get("name")   
        if not name:
            flash("Name can't be empty")
            return redirect(url_for("form"))
        flash(f"Thanks {name}, Your feedback was saved")
        return redirect(url_for("thankyou"))
    
    return render_template("form.html")


@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")


if __name__ == '__main__':
    app.run(debug=True)
    
    