from flask import Flask,request


app=Flask(__name__)


@app.route("/")
def home():
    return "hello user! this is my first flask practices"

@app.route("/about")
def about():
    return "This is about us page"

@app.route("/contact")
def contact():
    return "this is contact us page"

# from flask import request

@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        return "you sent the data"
    else:
        return "you are only viewing the form"
     
if __name__ == "__main__":
    app.run(debug=True)

