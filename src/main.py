from flask import Flask, redirect, render_template

from Routes.auth import session

app = Flask(__name__)
app.secret_key = "change-me-to-something-random"

from Routes.auth import auth
app.register_blueprint(auth, url_prefix="/auth")
from Routes.blog import blog
app.register_blueprint(blog, url_prefix="/blog")

@app.route("/")
def defaultRoute():
    if "username" not in session:
        return redirect("/auth/login")
    return render_template("index.html")
