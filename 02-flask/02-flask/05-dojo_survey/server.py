from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("dojo_survey.html")

@app.route('/result', methods=['POST'])
def survey():
    yname = request.form['yname']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    return render_template("result.html", yname=yname, location=location, language=language, comment=comment)

@app.route('/danger', methods=['GET'])
def danger():
    print("a user tried to visit/danger")
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)