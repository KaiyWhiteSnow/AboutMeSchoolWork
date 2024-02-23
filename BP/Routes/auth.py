from flask import Blueprint, request, render_template, redirect, url_for, session

from Hash.hash import BetterHash

auth = Blueprint("auth", __name__)

@auth.after_request
def add_header(response):
    """
    Add an Access-Control-Allow-Origin header to the response.

    :param response: The Flask response object.
    """
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "content-type, authorization"
    return response

@auth.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
            
        better_hash_instance = BetterHash()  # Create an instance of BetterHash
        check = better_hash_instance.checkHash(username=username, password=password)
        if check == 1:
            # Authentication successful, set session variable
            session['username'] = username
            return redirect(url_for("main.home")) 
        else: 
            return "Wrong name or password"
            
    return render_template("index.html")
            
@auth.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        passwordCheck = request.form['passwordCheck']
        
        if password != passwordCheck:
            return "Passwords do not match"
        
        better_hash_instance = BetterHash()  # Create an instance of BetterHash
        better_hash_instance.createUser(username=username, password=password)
        
        return redirect("/auth/login")
    return render_template("register.html")