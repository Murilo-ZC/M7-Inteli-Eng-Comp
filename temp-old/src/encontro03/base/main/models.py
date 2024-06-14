from pydantic import BaseModel, Field

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