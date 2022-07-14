from flask_login import UserMixin
from app import db

class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuarios'
    cedula = db.Column(db.Integer, primary_key=True)
    id = cedula
    nombre = db.Column(db.String(50))
    rol = db.Column(db.String(45))
    contra = db.Column(db.String)
    estado = db.Column(db.String(25))


