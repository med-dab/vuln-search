from flask import Flask, render_template, request, flash
from scraper import search_surface_web, search_dark_web
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "change-this-key"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Simple in-memory user store
users = {"admin": generate_password_hash("admin123")}

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    if user_id in users:
        return User(user_id)
    return None

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and check_password_hash(users[username], password):
            login_user(User(username))
            return render_template('index.html', results=[], user=current_user)
        else:
            flash("Invalid login")
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out")
    return render_template('login.html')

@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    results = []
    if request.method == 'POST':
        equipment = request.form['equipment'].strip()
        if equipment:
            surface = search_surface_web(equipment)
            dark = search_dark_web(equipment)
            results = surface + dark
        else:
            flash("Enter equipment or software name")
    return render_template('index.html', results=results, user=current_user)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
