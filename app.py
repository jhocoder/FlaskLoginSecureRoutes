from flask import Flask, render_template, redirect, url_for, request, flash
from config import config
from flask_mysqldb import MySQL
from models.ModelUser import ModelUser
from models.entities.User import User
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_object(config['development'])
crsf = CSRFProtect(app)

db = MySQL(app)
loginManager = LoginManager(app)

@loginManager.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        user = User(0, username, password)
        logged_user = ModelUser.login(db, user)
        
        if logged_user:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for("home"))
            else:
                flash("password incorrect")
                return render_template('auth/login.html')
        else:
            flash("user not found")
            return render_template('auth/login.html')
    else:
        if current_user.is_authenticated:
            print("AUTENTICADO CON SESION")
            print(current_user.username)
            print(current_user.fullname)
            print(current_user.get_by_id())
            return redirect(url_for("home"))
    return render_template('auth/login.html')

@app.route("/home")
@login_required
def home():
    print(current_user)
    return render_template("home.html", current_user=current_user)

@app.route("/protected")
@login_required
def protected():
    return "<h1>Protected Route</h1>"

def status_401(error):
    return redirect(url_for("login"))

def status_404(error):
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.config.from_object(config['development'])
    crsf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()
    
    
    # CSRF ATAQIE