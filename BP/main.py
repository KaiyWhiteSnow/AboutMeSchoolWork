from flask import Flask, request, redirect, url_for, session, render_template

# Define a list of hardcoded users
users = {"Admin": "Heslo"}
sessionUser = "SysAdmin"


app = Flask(__name__)
app.secret_key = "key"

@app.route("/", methods=['GET', 'POST'])
def notHome():
    if "username" not in session:
        return render_template("index.html")
    else:
        return render_template("index.html", sessionUser=sessionUser)

@app.route("/index", methods=['GET', 'POST'])
def home():    
    return render_template("index.html")
    
    
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username and password match a hardcoded user
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return 'Invalid username or password. <a href="/login">Try again</a>'
    
    return render_template("login.html")

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


@app.route('/Sokkatto')
def Sokkatto():
    return render_template("sokkatto.html")

if __name__ == "__main__":
    app.run(debug=True)