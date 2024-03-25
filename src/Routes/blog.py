from flask import Blueprint, request, render_template, redirect, url_for, session
import datetime
from Database.database import get_session
from Database.Models.post import Post

blog = Blueprint("blog", __name__)

@blog.after_request
def add_header(response):
    """
    Add an Access-Control-Allow-Origin header to the response.

    :param response: The Flask response object.
    """
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "content-type, authorization"
    return response


@blog.route("/forum", methods=["GET", "POST"])
def blogForum():
    if "username" not in session:
        return redirect("/auth/login")
    
    with get_session() as session:
        posts = (session.query(Post).all())
    username = session["username"]

    return render_template("/blog/forum.html", posts=posts, username=username)

@blog.route("/create_post", methods=["GET", "POST"])
def createPost():
    if "username" not in session:
        return redirect("/auth/login")
    if request.method == "POST":
        title = request.form.get('title')
        content = request.form.get('content')

        created_at_str = datetime.datetime.now().strftime("%Y-%m-%d")  # Format the current date as a string
        created_at = datetime.datetime.strptime(created_at_str, "%Y-%m-%d")  # Convert the string to a datetime object
        created_by = session["username"]
        post = Post(
                title=title, 
                content=content, 
                created_at=created_at, 
                created_by=created_by
            )
        with get_session() as session:
            session.add(post)
            session.commit()
    
        # Redirect or return a response indicating success
        return redirect("/forum")
    username = session["username"]
    return render_template("create_post.html", username=username)
