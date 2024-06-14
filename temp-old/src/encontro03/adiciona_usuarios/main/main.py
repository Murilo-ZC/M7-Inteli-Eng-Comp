import uvicorn
from fastapi import FastAPI, Body, Depends
from main.models import PostSchema, UserSchema, LoginUserSchema
from main.auth.jwt_handler import signJWT
from main.auth.jwt_bearer import jwtBearer

# Cria a referência com os dados da aplicação
posts = [
    {
        "id": 1,
        "title": "Primeiro Post",
        "content": "Conteúdo do primeiro post 😒",
    },
    {
        "id": 2,
        "title": "Segundo Post",
        "content": "Conteúdo do segundo post 👌",
    }
]

users = []

# Cria a base para a aplicação
app = FastAPI()

@app.get("/", tags=["tests"])
def ola():
    return {"message": "Olá Mundo!"}

# Retorna todos os posts
@app.get("/posts", tags=["posts"])
def get_posts():
    return {"data": posts}

# Retorna um post por id
@app.get("/posts/{post_id}", tags=["posts"])
def get_post_by_id(post_id: int):
    if post_id > len(posts):
        return {"error": "Post não encontrado"}
    for post in posts:
        if post["id"] == post_id:
            return {"data": post}
        
# Recebe um post e adiciona na lista
@app.post("/posts", dependencies=[Depends(jwtBearer())], tags=["posts"])
def add_post(post: PostSchema):
    # Ajusta o id do post
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {"data": "Post adicionado com sucesso"}

# Recebe uma requisição do POST para criar um usuário
@app.post("/user/signup", tags=["user"])
def user_signup(user: UserSchema = Body(default= None)):
    users.append(user)
    return signJWT(user.email)

# Função que verifica os dados do usuário
def check_user(data: LoginUserSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False

# Recebe uma requisição do POST para logar um usuário
@app.post("/user/login", tags=["user"])
def user_login(user: UserSchema = Body(default= None)):
    if check_user(user):
        return signJWT(user.email)
    return {"error": "Dados inválidos"}
