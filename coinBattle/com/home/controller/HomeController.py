from flask import Flask, Blueprint, render_template

bp = Blueprint("HomeController", __name__)

@bp.route("/")
@bp.route("/index")
def index():
    return render_template("index.html")