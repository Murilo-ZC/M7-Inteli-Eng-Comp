# Desenvolvimento em Aula Encontro 10

Ao longo deste encontro, vamos desenvolver uma aplicação que remove o fundo de uma imagem e faz a sua combinação com a imagem de fundo, também enviada pelo usuário.

As tecnologias utilizadas para sua construção serão:
- AWS SQS
- RabbitMQ
- OpenCV, Pillow e REMBG (Python)
- Python
- Docker
- Celery
- FastAPI
- HTMX | Reflex

## 1. Configuração do ambiente e aplicação monolítica

A aplicação será desenvolvida em dois cenários distintos, o de uma aplicação monolítica e uma aplicação com serviços rodando em segundo plano.
Vamos trabalhar primeiro com uma aplicação monolítica, para depois separar as funcionalidades em segundo plano.

Nosso arquivo ***requirements.txt*** deve conter as seguintes dependências, para a aplicação monolítica:

```txt
fastapi
uvicorn
rembg
pillow
python-multipart
```

Nossa aplicação Python deve conter o seguinte código:

```python
from PIL import Image
from rembg import remove
from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse

NO_BG_IMAGE_NAME = "no-bg.png"

def remove_br(image):
    try:
        bytes_data = Image.open(image)
        output = remove(bytes_data)
        Image.frombytes("RGBA", output.size, output.tobytes()).save(NO_BG_IMAGE_NAME)
        return True
    except Exception as e:
        print(e)
        return False

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/remove_bg")
async def remove_bg(image:UploadFile = None):
    if not image:
        return {"message": "No image"}
    if remove_br(image.file):
        return FileResponse(NO_BG_IMAGE_NAME)
    return {"message": "Error"}
```

Vamos chamar nosso código de ***backend.py***. Para executar a aplicação, basta executar o seguinte comando:

```bash
python -m uvicorn backend:app 
```

Para testar nossa aplicação, vamos fazer uma requisição do tipo POST, enviando uma imagem para o endpoint */remove_bg*. Podemos fazer isso utilizando o [Postman](https://www.postman.com/), o [Insomnia](https://insomnia.rest/) ou o plugin [Thunder Client](https://www.thunderclient.com/).

<img src="./media/requisicao_thunder_client.png" width=100% flex=center>

Agora vamos criar uma outra rota que recebe a imagem de fundo e faz a combinação com a imagem sem fundo. 

```python
from PIL import Image
from rembg import remove
from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse

NO_BG_IMAGE_NAME = "no-bg.png"

def remove_br(image):
    try:
        bytes_data = Image.open(image)
        output = remove(bytes_data)
        Image.frombytes("RGBA", output.size, output.tobytes()).save(NO_BG_IMAGE_NAME)
        return True
    except Exception as e:
        print(e)
        return False

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/remove_bg")
async def remove_bg(image:UploadFile = None):
    if not image:
        return {"message": "No image"}
    if remove_br(image.file):
        return FileResponse(NO_BG_IMAGE_NAME)
    return {"message": "Error"}

@app.post("/combine_bg")
async def combine_bg(image:UploadFile = None, background:UploadFile = None):
    if not image or not background:
        return {"message": "No image or no background"}
    if remove_br(image.file):
        try:
            bytes_data = Image.open(NO_BG_IMAGE_NAME)
            bg = Image.open(background.file)
            bg.paste(bytes_data, (bg.width//2, bg.height//2), bytes_data)
            bg.save(NO_BG_IMAGE_NAME, "JPEG", optimize=True,)
            return FileResponse(NO_BG_IMAGE_NAME)
        except Exception as e:
            print(e)
            return {"message": "Error"}
    return {"message": "Error"}
```

Agora temos uma segunda rota que além de remover o fundo de uma imagem, faz sua junção com outra imagem de fundo.

<img src="./media/requisicao_thunder_client_com_bg.png" width=100% flex=center>

Se prestarmos atenção no tempo que a requisição levou para ser concluída, podemos ver que ela levou quase 3 segundos, isso considerando que toda a aplicação está sendo executada localmente. Quando realizamos o deploy de uma aplicação, o tempo de resposta dela pode comprometer a experiência do usuário. Para resolver esse problema, podemos utilizar o Celery para executar as tarefas em segundo plano.


## 2. Refatorando para utilizar o Celery e o RabbitMQ

Vamos criar agora um diretório chamado ***segundo-plano*** e dentro dele vamos iniciar uma nova aplicação. Não esqueça de parar o ***venv*** criado na aplicação monolítica.

```bash
mkdir segundo-plano
cd segundo-plano
python -m venv .
source bin/activate
```

A princípio vamos utilizar a mesma aplicação base que a aplicação monolítica, mas vamos refatorar o código para que ele possa ser executado. O arquivo de requerimentos fica um pouco diferente.

```txt
fastapi
uvicorn
rembg
pillow
python-multipart
celery
```

Vamos criar um arquivo chamado de ***celery_config.py***, que vai conter a configuração do Celery.

```python
from celery import Celery
import os

app = Celery('celery_base',
             broker='amqp://usuario:senha@rabbitmq:5672/vhost',
             include=['task'])
```

Agora vamos criar um arquivo chamado ***task.py***, que vai conter a tarefa que será executada em segundo plano.

```python
from celery_config import app
import time


@app.task
def sample_task():
    for i in range(10):
        time.sleep(5)
    print("Task Completed")

#TODO adicionar o restante
```

Agora vamos executar um container com o RabbitMQ, para que possamos utilizar o Celery.

```bash
docker run -d --hostname my-rabbit --name some-rabbit -e RABBITMQ_DEFAULT_USER=usuario -e RABBITMQ_DEFAULT_PASS=senha -e RABBITMQ_DEFAULT_VHOST=vhost -p 5672:5672 -p 8080:8080 rabbitmq:3-management
```

É possível ver o funcionamento do RabbitMQ acessando o endereço [http://localhost:8080](http://localhost:8080). As credenciais de acesso são as mesmas que foram configuradas no container.