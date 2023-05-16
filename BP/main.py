from flask import Flask, request, redirect, url_for, session, render_template
import hashlib

app = Flask(__name__)
app.secret_key = "key"

#In case I forget, this is for initial page but is exactly the same as index which everything will redirect to
@app.route("/", methods=['GET', 'POST'])
def notHome():
    if "username" not in session:
        return redirect('/login')
    else:
        return redirect('/index')
    
@app.route("/index", methods=['GET', 'POST'])
def home():    
    return render_template("index.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        hashPass = password
        hashUser = username
        HP = hashlib.md5(hashPass.encode())
        HU = hashlib.md5(hashUser.encode())

        # Write user information to a text file
        with open('users.txt', 'a') as file:
            file.write(f'{HU.hexdigest()},{HP.hexdigest()}\n')

        # Redirect to login page
        return redirect('/login')

    return render_template('register.html')

#Normal login, checks 
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Hash username and password using MD5 algorithm
        hashPass = hashlib.md5(password.encode()).hexdigest()
        hashUser = hashlib.md5(username.encode()).hexdigest()

        with open('users.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                user, pwd = line.strip().split(',')
                if user == hashUser and pwd == hashPass:
                    # User found, store username in session and redirect to home page
                    session["username"] = username
                    return redirect('/index')

        # User not found, show error message
        error = "Invalid username or password. Please try again."
        return render_template('login.html', error=error)

    return render_template('login.html')

@app.route('/logout')
def logout():
    # Remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('login'))  # Update to redirect to 'login' route

@app.route('/StoryOfKaiy')
def StoryOfKaiy():
    return render_template("StoryOfKaiy.html")

@app.route('/Art')
def Art():
    return render_template("Art.html")


@app.route('/sokkatto')
def sokkatto():
    return render_template("sokkatto.html")
