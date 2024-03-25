from flask import Blueprint, request, jsonify, render_template, redirect, url_for, session

main = Blueprint("main", __name__)

@main.after_request
def add_header(response):
    """
    Add an Access-Control-Allow-Origin header to the response.

    :param response: The Flask response object.
    """
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "content-type, authorization"
    return response

@main.route("/home", methods=["GET", "POST"])
def home():
    return render_template("home.html")