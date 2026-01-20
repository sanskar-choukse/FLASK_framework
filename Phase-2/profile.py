from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def student_profile():
    return render_template(
        "profile.html",
        name="vire",
        is_topper=True,
        subject=["Maths","Science","Physics"]
    )
    
if __name__ == '__main__':
    app.run(debug=True)
        