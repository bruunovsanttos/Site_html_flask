from flask import Blueprint, request, redirect, url_for, flash
from app.database.db import db
from app.models.contact import Contact

contato_bp = Blueprint("contact", __name__)


@contato_bp.route("/contato", methods=["POST"])
def receber_contato():

    nome = request.form.get("nome")
    telefone = request.form.get("telefone")
    email = request.form.get("email")
    mensagem = request.form.get("mensagem")


    if not nome or not telefone or not email or not mensagem:
        return "Preencha todos os campos obrigatórios!", 400


    novo_contato = Contact(
        nome=nome,
        telefone=telefone,
        email=email,
        mensagem=mensagem
    )


    db.session.add(novo_contato)
    db.session.commit()


    flash("Mensagem enviada com sucesso!", "sucesso")

    # redireciona para o home do site apos a mensagem
    return redirect(url_for("main.home"))