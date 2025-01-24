# filepath: /c:/Users/jlrbk/Documents/desarrollin/FP2/Desarrollo Entorno Servidor/Segundo Trimestre/RouteSesionSecurity/src/app.py
from flask import Flask, render_template, redirect, url_for, request, flash
from config import config
from flask_mysqldb import MySQL
from models.ModelUser import ModelUser
from models.entities.User import User
from flask_login import LoginManager, login_user

app = Flask(__name__)

db = MySQL(app)
loginManager= LoginManager(app)





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
        print(username, password)
        user = User(0, username, password)
        
        print(user)
        logged_user = ModelUser.login(db, user)
        loginManager(logged_user)
        print(logged_user)
        
        if logged_user:
            if logged_user.password:
                return redirect(url_for("home"))
            else:
                flash("password incorrect")
                return render_template('auth/login.html')
        else:
            flash("user not found")
            return render_template('auth/login.html')
    return render_template('auth/login.html')
        
@app.route("/home")
def home():
    return render_template("home.html")
    
    

if __name__ == "__main__":
    app.config.from_object(config['development'])
    app.run()