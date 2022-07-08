from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Instancia o App
app = FastAPI()

# Rota Raiz
@app.get("/")
def raiz():
    return {"Ola": "Mundo"}

# Criar model para os usuários
class Usuario(BaseModel):
    id: int
    email: str
    senha: str

# Criar base de dados
base_de_dados = [
    Usuario(id=1, email="lrgamito@dmn.com.br", senha="teste123"),
    Usuario(id=2, email="lrgamito2@dmn.com.br", senha="teste1234")
]

# Rota Get All
@app.get("/usuarios")
def get_todos_os_usuarios():
    return base_de_dados

def verifica_usuario(id_usuario):
    for usuario in base_de_dados:
        if(usuario.id == id_usuario):
            return usuario

# Rota Get Id
@app.get("/usuarios/{id_usuario}")
def get_usuario_usando_id(id_usuario: int):
    
    usuario_verificado = verifica_usuario(id_usuario)
    
    if(usuario_verificado is None ):
        raise HTTPException(status_code=404, detail="404 - Usuário não encontrado")   
    
    return usuario_verificado
    
# Rota insere usuarios
@app.post("/usuarios")
def insere_usuario(usuario: Usuario):
    
    mensagem = ""
    usuario_verificado = verifica_usuario(usuario.id)
    
    if(usuario_verificado is None):
        base_de_dados.append(usuario)
        mensagem = {"Mensagem":"Usuário Cadastrado"}
    else: 
        mensagem = {"Mensagem":"Usuário já existe"}
    
    return mensagem
    
