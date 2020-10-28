from flask import Flask, render_template, request, redirect, url_for, session
from flask import Blueprint
# app = Flask(__name__)
# app.secret_key = 'you-will-never-ever-ever-guess'

# defining a route
server_bp = Blueprint('login', __name__)
@server_bp.route("/", methods=['GET', 'POST'])
def login_page():
    error = None
    if request.method == 'POST':
        #session.pop('user', None)
        if request.form['username']!= 'diabetes' and request.form['password'] != 'test':
            error = 'Invalid Credentials. Please try again.'
        # else:
        #     #session['user'] =request.form['username']
        #     return redirect(url_for("login.home"))
    return render_template('login_page.html', error=error)


# @server_bp.route("/home", methods=['GET', 'POST'])
# def home():
#     return "<h1>request received </h1>"

#
# if __name__ == "__main__":
#     app.run(debug=True)
