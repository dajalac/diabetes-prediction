from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'you-will-never-ever-ever-guess'

# defining a route

@app.route("/", methods=['GET', 'POST'])
def login_page():
    error = None
    if request.method == 'POST':
        #session.pop('user', None)
        if request.form['username']!= 'diabetes' and request.form['password'] != 'test':
            error = 'Invalid Credentials. Please try again.'
        else:
            #session['user'] =request.form['username']
            return redirect(url_for("home"))
    return render_template('login_page.html', error=error)


@app.route("/home", methods=['GET', 'POST'])
def home():
    return "<h1>request received </h1>"


if __name__ == "__main__":
    app.run(debug=True)
