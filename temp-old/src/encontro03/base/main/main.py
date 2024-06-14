import uvicorn
from fastapi import FastAPI
from main.models import PostSchema

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
@app.post("/posts", tags=["posts"])
def add_post(post: PostSchema):
    # Ajusta o id do post
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {"data": "Post adicionado com sucesso"}