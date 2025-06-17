from flask import Blueprint, jsonify
from app.models.Usuario import Usuario

usuarios_bp = Blueprint('usuarios', __name__)
@usuarios_bp.routes('/')
def create():
    return