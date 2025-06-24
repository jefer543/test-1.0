from flask import Blueprint, jsonify
from app.models.Usuario import Usuario

usuarios_bp = Blueprint('usuarios', __name__)
from flask import Blueprint, request, jsonify, abort
from models import User, db  # supondo que User e db estão no models.py
from schemas import user_schema  # Marshmallow Schema para User

users_bp = Blueprint('users', __name__, url_prefix='/users')

# Rota para listar todos os usuários
@users_bp.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200

# Rota para obter um usuário por ID
@users_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict()), 200

# Rota para criar um novo usuário
@users_bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        abort(400, description="Campos 'name' e 'email' são obrigatórios.")

    new_user = User(name=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user.to_dict()), 201

# Rota para atualizar um usuário existente
@users_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json()

    updated_data = user_schema.load(
        data,
        instance=user,
        partial=True  # permite atualização parcial
    )

    db.session.commit()
    return jsonify(user_schema.dump(updated_data)), 200

# Rota para deletar um usuário
@users_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return '', 204
