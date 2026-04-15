#aqui vai o modelo de bando de dados a ser criado
from datetime import datetime
from app.database.db import db

class contact(db.Model):
    __tablename__ = "contacts"

    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    mensagem = db.Column(db.Text, nullable=False)

    data_envio = db.Column(
        db.datetime,
        default=datetime.utcnow(),
        nullable=False
    )
    def __repr__(self):
        return f"<contato {self.id} - {self.nome}>"
