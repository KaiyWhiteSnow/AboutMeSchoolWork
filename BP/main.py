from flask import Flask, redirect

app = Flask(__name__)
app.secret_key = "change-me-to-something-random"

from Routes.auth import auth
app.register_blueprint(auth, url_prefix="/auth")
from Routes.main import main
app.register_blueprint(main, url_prefix="/main")

@app.route("/")
def defaultRoute():
    return redirect("/auth/login")