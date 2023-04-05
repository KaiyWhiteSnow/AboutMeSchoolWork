from flask import Flask, request, redirect, url_for, session, render_template

# Define a list of hardcoded users
users = {"SysAdmin": "Password"}
username = "SysAdmin"

app = Flask(__name__)
app.secret_key = 'mysecretkey'  # Set a secret key for session management

@app.route('/')
def index():
    # Check if the user is already logged in
    if "username" in session:
        return render_template("index.html", username=username)
    else:
        return render_template("login.html")
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Check if the user is already logged in
    if 'username' in session:
        return render_template("index.html")

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
    
if __name__ == "__main__":
    app.run(debug=True)