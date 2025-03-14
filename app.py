from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Configura o caminho para o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dados.db'
db = SQLAlchemy(app)

# Define o modelo de dados
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Usuario {self.nome}>"

# Cria o banco de dados
@app.before_first_request
def criar_db():
    db.create_all()

# Rota para o formulário
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome_usuario = request.form['nome']
        email_usuario = request.form['email']
        novo_usuario = Usuario(nome=nome_usuario, email=email_usuario)
        db.session.add(novo_usuario)
        db.session.commit()
        return redirect('/')
    return render_template('formulario.html')

if __name__ == "__main__":
    app.run(debug=True)
