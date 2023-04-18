from flask import Flask, request, redirect, url_for, session, render_template


# Define a list of hardcoded users
users = {"Admin": "Heslo"}
sessionUser = "SysAdmin"


app = Flask(__name__)
app.secret_key = "key"

#In case I forget, this is for initial page but is exactly the same as index which everything will redirect to
@app.route("/", methods=['GET', 'POST'])
def notHome():
    if "username" not in session:
        return render_template("index.html")
    else:
        return render_template("index.html", sessionUser=sessionUser)

@app.route("/index", methods=['GET', 'POST'])
def home():    
    return render_template("index.html")

# TODO: Fucking database
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Write user information to a text file
        with open('users.txt', 'a') as file:
            file.write(f'{username},{password}\n')

        # Redirect to login page
        return redirect('/login')

    return render_template('register.html')

#Normal login, checks 
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        with open('users.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                user, pwd = line.strip().split(',')
                if user == username and pwd == password:
                    # User found, redirect to home page or appropriate page
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

if __name__ == "__main__":
    app.run(debug=True)