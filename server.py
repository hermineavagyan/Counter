from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'counter key'

@app.route('/')
def add():
    if "count" not in session:
        session['count'] = 1
        print(session['count'])
    else:
        session['count'] +=1
        print(session['count'])
    return render_template("index.html")

@app.route('/userAdds', methods = ['POST'])
def userAdds():
    session['count'] += int(request.form['number'])
    return redirect('/')

@app.route('/addTwo')
def addTwo():
    if "count" not in session:
        session['count'] = 1
        print(session['count'])
    else:
        session['count'] +=1
        print(session['count'])
    return redirect('/')

@app.route('/addFixedNum', methods = ['POST'])
def addFixedNum():
    session['count'] +=4
    return redirect('/')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')


if __name__== "__main__":
    app.run(debug=True)