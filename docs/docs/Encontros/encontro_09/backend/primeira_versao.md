---
sidebar_position: 2
title: Backend Simples
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Primeira Versão do Backend

Nossa primeira versão do backend é bastante simples. Ela possui um endpoint apenas e exibe o resultado de uma operação matemática. Ela vai receber a operação no corpo da requisição e retornar o resultado. Vamos para sua implementação.

## Criando ambiente de desenvolvimento

Pessoal vamos aqui criar nosso ambinte virtual para o desenvolvimento da nossa solução. Para isso, vamos utilizar o `venv` para criar um ambiente virtual para o nosso projeto.

```bash
python3 -m venv venv
```

Aqui temos um diretório chamado `venv` que é o nosso ambiente virtual. Para ativar ele, vamos utilizar o comando:

```bash
# No Linux/Mac
source venv/bin/activate
```

```bash
# No Windows
venv\Scripts\activate
```

## Instalando as dependências

Vamos adicionar agora as dependências do nosso projeto. Para isso, vamos criar um arquivo chamado `requirements.txt` e adicionar as dependências necessárias.

```bash
# requirements.txt
fastapi==0.111.0
plusminus==0.7.0
```

Na versão atual do FastAPI, o Uvicorn já é instalado por padrão. Mais informações [aqui](https://pypi.org/project/fastapi/).
O pacote `plusminus` é uma biblioteca que faz a operação matemática. Mais informações [aqui](https://pypi.org/project/plusminus/).

Lembrando que para instalar as dependencias, basta rodar o comando:

```bash
python3 -m pip install -r requirements.txt
```

Vamos criar a primeira versão do nosso backend.

:::danger[CUIDADO COM O STATEING DE ARQUIVOS]

Pessoal importante, o `.gitignore` é um arquivo que contém uma lista de arquivos e diretórios que o Git deve ignorar. Isso é importante para que não subamos arquivos desnecessários para o repositório. Por isso, é importante que vocês criem um arquivo `.gitignore` e adicionem o seguinte conteúdo:

```bash
/venv
```

:::


```python
# main.py

from fastapi import FastAPI
from pydantic import BaseModel

# Define a classe de modelo base utilizada
class Pedido(BaseModel):
    expressao:str

app = FastAPI()

@app.post("/evaluate")
async def evaluate(pedido: Pedido):
    # Esta versão ainda não utiliza a biblioteca plusminus para verificar a expressão
    # Ela faz a verificação apenas com a função eval do Python
    try:
        resultado = eval(pedido.expressao)
        return {"resultado": resultado}
    except Exception as e:
        return {"resultado": f"Erro na expressão informada: {e}"}
    
```

Agora vamos rodar o nosso backend. Para isso, vamos utilizar o comando:

```bash
fastapi dev main.py
```

Esse comando está utilizando a nova CLI do FastAPI para rodar o nosso backend. Mais informações [aqui](https://fastapi.tiangolo.com/fastapi-cli/). Nosso serviço está sendo executado apenas localmente em nossa máquina. Para testar ele, podemos utilizar o Insonmia, Postman ou o cURL. Vou colocar um exemplo com o cURL:

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/evaluate' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
    "expressao": "2+2"
}'
```

Pronto! Temos a primeira versão do nosso backend rodando! Agora vamos adicionar esse nosso backend para que possamos executar ele como um container Docker.

## Criando o Dockerfile

Vamos criar nosso Dockerfile para que possamos rodar nosso backend como um container Docker. Para isso, vamos criar um arquivo chamado `Dockerfile` e adicionar o seguinte conteúdo:

```Dockerfile
# Use the official Python image
# https://hub.docker.com/_/python
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Specify the command to run on container start
CMD [ "fastapi", "run", "main.py"]

```

Agora vamos criar a nossa imagem Docker. Para isso, vamos rodar o comando:

```bash
docker build -t backend-simples .
```

Agora podemos executar nosso conteiner. Para isso, vamos rodar o comando:

```bash
docker run -d -p 8000:8000 backend-simples
```

Boa! Agora temos nosso serviço básico rodando!! Vamos para a próxima etapa!

