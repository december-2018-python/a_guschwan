from flask import Flask, render_template, request, redirect, flash, session
app = Flask(__name__)
app.secret_key="slfsdjfalsdjfls"
@app.route('/')
def index():
    return render_template("dojo_survey.html")

@app.route('/result', methods=['POST'])
def survey():
    yname = request.form['yname']
    if len(request.form['yname']) < 1:
        flash("Name cannot be blank!", 'yname')
    location = request.form['location']
    language = request.form['language']
    if len(request.form['comment']) < 1:
        flash("Comment cannot be blank!", 'comment')
    if len(request.form['comment']) > 120:
        flash("Comment cannot be more that 120 characters.")
        comment = request.form['comment']
    if '_flashes' in session.keys():
        return redirect("/")
    else:
        return render_template("result.html", yname=yname, location=location, language=language, comment=comment)

@app.route('/danger', methods=['GET'])
def danger():
    print("a user tried to visit/danger")
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)