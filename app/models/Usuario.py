
from app import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    nome = db.Column(db.String(255), nullable=False)
    senha = db.Column(db.String(255))



from datetime import datetime

class Usuario:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

class Mensagem:
    def __init__(self, id, conteudo, autor_id, data_hora=None):
        self.id = id
        self.conteudo = conteudo
        self.autor_id = autor_id
        self.data_hora = data_hora if data_hora else datetime.now()

    def __repr__(self):
        return f"Mensagem(id={self.id}, autor_id={self.autor_id}, data_hora={self.data_hora}, conteúdo='{self.conteudo}')"

# Exemplo de uso
usuario1 = Usuario(id=1, nome="Alice")
mensagem1 = Mensagem(id=101, conteudo="Olá, mundo!", autor_id=usuario1.id)

print(mensagem1)
# Mensagem(id=101, autor_id=1, data_hora=2024-06-18 14:30:00.123456, conteúdo='Olá, mundo!')

# Criando outra mensagem com data e hora customizadas
from datetime import datetime, timedelta

data_especifica = datetime(2024, 6, 17, 10, 0, 0)
mensagem2 = Mensagem(id=102, conteudo="Outra mensagem", autor_id=usuario1.id, data_hora=data_especifica)
print(mensagem2)
# Mensagem(id=102, autor_id=1, data_hora=2024-06-17 10:00:00, conteúdo='Outra mensagem')

from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulação de um banco de dados
mensagens = []
proximo_id_mensagem = 1

@app.route('/mensagens', methods=['POST'])
def criar_mensagem():
    global proximo_id_mensagem
    dados_da_mensagem = request.get_json()

    # Aqui, você verifica se o usuário está sendo fornecido na requisição
    # Se não estiver, define o usuário como 1 por padrão.
    usuario_id = dados_da_mensagem.get('usuario_id', 1)
    
    nova_mensagem = {
        'id': proximo_id_mensagem,
        'texto': dados_da_mensagem['texto'],
        'usuario_id': usuario_id,
    }

    mensagens.append(nova_mensagem)
    proximo_id_mensagem += 1

    return jsonify(nova_mensagem), 201

@app.route('/mensagens', methods=['GET'])
def listar_mensagens():
    return jsonify(mensagens)


if __name__ == '__main__':
    app.run(debug=True)