from pydantic import BaseModel, Field, EmailStr

class PostSchema(BaseModel):
    id : int = Field(default=None, gt=0)
    title: str = Field(default=None)
    content: str = Field(default=None)
    # Configuração criada para documentação do modelo
    class Config:
        schema_extra = {
            "post_teste" : {
                "title": "Post Teste",
                "content": "Conteúdo do post teste"
            }
        }

# Classe para representar os usuários do sistema
class UserSchema(BaseModel):
    fullname : str = Field(default=None)
    email : EmailStr = Field(default=None)
    password : str = Field(default=None)
    class Config:
        schema_extra = {
            "schema_user" : {
                "fullname": "Teste",
                "email": "teste@mail.com",
                "password":"123"
            }
        }
# Classe para o login dos usuários
class LoginUserSchema(BaseModel):
    email : EmailStr = Field(default=None)
    password : str = Field(default=None)
    class Config:
        schema_extra = {
            "user_teste" : {
                "email": "teste@mail.com",
                "password":"123"
            }
        }