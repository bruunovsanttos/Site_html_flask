from flask import Blueprint, render_template

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def home():
    return render_template("index.html")

@main_bp.route("/projetos")
def projetos():
    return render_template("project.html")

@main_bp.route("/contato")
def contato():
    return render_template("contact.html")