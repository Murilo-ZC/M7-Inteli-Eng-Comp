---
sidebar_position: 3
title: Adicionando Cache no Backend
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## O conceito de Cache

Primeiro vamos analisar um conceito importante: o cache. O cache é uma técnica de armazenamento temporário de dados que são frequentemente acessados. Ele é utilizado para melhorar a performance e a eficiência de um sistema.

<img src="https://process.filestackapi.com/cache=expiry:max/enVkn7RtRvinRJnZxst2" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom: '24px' }}/>

O que temos na imagem é a descrição do processo de cache. Quando um cliente faz uma requisição para o servidor, o servidor verifica se a resposta para essa requisição está no cache. Se estiver, o servidor retorna a resposta do cache para o cliente. Se não estiver, o servidor processa a requisição e armazena a resposta no cache.

Essa abordagem traz uma série de benefícios, como a redução do tempo de resposta, a diminuição do tráfego de rede e a economia de recursos do servidor. O serviço de cache é muito utilizado em aplicações que precisam de alta performance e escalabilidade.

Diversos serviços podem ser utilizados para implementar o cache em uma aplicação. Vamos utilizar o Redis, um banco de dados em memória que é muito utilizado para cache e armazenamento de dados temporários. Extremamente importante ressaltar, o Redis tem muitas outras funcionalidades também, como armazenamento de dados em memória, suporte a estruturas de dados complexas, entre outras.

## Adicionando o Redis ao nosso projeto

Pessoal conseguimos utilizar o Redis de diversas formas diferentes, mas para o nosso projeto vamos utilizar o Redis como um serviço de cache. Sua utilização pode acontecer por uma instalação local, serviço de cloud ou ainda utilizando um container Docker. Vamos trabalhar com a última opção. A imagem que vamos utilizar é a oficial do Redis, disponível no [Docker Hub](https://hub.docker.com/_/redis).

Vamos adicionar o Redis ao nosso projeto utilizando o Docker. Primeiro, vamos criar um arquivo chamado `docker-compose.yml` na raiz do nosso projeto. Adicione o seguint: 

```yaml

version: '3.8'

services:
  redis:
    image: redis
    container_name: redis
    ports:
      - "6379:6379"
  backend:
    build: .
    container_name: backend
    ports:
      - "8000:8000"
    restart: on-failure
    depends_on:
      - redis

```

Pessoal o que vai acontecer aqui, vamos iniciar nosso backend e também vamos iniciar o Redis. O Redis vai estar disponível na porta 6379 e o backend na porta 8000. O backend vai depender do Redis, ou seja, o Redis vai ser iniciado antes do backend. Por hora, ainda não estamos utilizando o Redis no nosso backend, mas vamos fazer isso agora.

## Utilizando o Redis

Pessoal aqui vai ser uma seção de utilização do Redis, para compreender como ele pode ser utilizado. Se vocês quiserem apenas ver a implementação do cache, podem pular para a próxima seção. O que é necessário fazer aqui é adicionar a dependência do Redis ao nosso projeto. Para isso, vamos instalar o pacote `redis` no arquivo `requirements.txt`. 

```bash
fastapi==0.111.0
plusminus==0.7.0
redis==5.0.4
```

### Utilizando o Redis por linha de comando

- TODO

### Utilizando o Redis com Python

- TODO

## Implementando o Cache no Backend

Agora vamos para nossa implementação de cache no backend. Vamos adicionar o Redis ao nosso projeto e utilizar o cache para armazenar os resultados das requisições. Primeiro, vamos adicionar o Redis ao nosso projeto. Para isso, vamos criar um arquivo chamado `cache.py` na pasta `backend` e adicionar o seguinte código:

```python
import redis

redis_client = redis.Redis(host='redis', port=6379, db=0)
```

O que foi realizado aqui:

1. Importamos a biblioteca `redis`.
2. Criamos uma instância do cliente do Redis, passando o host e a porta do Redis.

Vamos utilizar agora o Redis para armazenar os resultados das requisições. Vamos adicionar o cache na rota de listagem de produtos. Para isso, vamos modificar o arquivo `main.py` na pasta `backend` e adicionar o seguinte código:

```python
# main.py

from fastapi import FastAPI
from pydantic import BaseModel
from cache import redis_client

# Define a classe de modelo base utilizada
class Pedido(BaseModel):
    expressao:str

app = FastAPI()

@app.post("/evaluate")
async def evaluate(pedido: Pedido):
    # Verifica se a requisição já foi feita
    resultado = redis_client.get(pedido.expressao)
    if resultado:
        return {"resultado": resultado.decode()}
    
    # Calcula o resultado da expressão
    try:
        resultado = eval(pedido.expressao)
        # Armazena o resultado no cache
        redis_client.set(pedido.expressao, resultado)
        return {"resultado": resultado}
    except Exception as e:
        # Em caso de erro, retorna uma mensagem de erro, mas armazena ela no cache também
        redis_client.set(pedido.expressao, f"Erro na expressão informada: {e}")
        return {"resultado": f"Erro na expressão informada: {e}"}
    
```

O que foi realizado aqui:

1. Importamos a biblioteca `redis`.
2. Criamos uma instância do cliente do Redis, passando o host e a porta do Redis.
3. Modificamos a rota de listagem de requisições para verificar se ela já foi feita. Se sim, retorna o resultado do cache. Se não, calcula o resultado da expressão e armazena no cache.

Agora, vamos testar a nossa aplicação. Para isso, vamos iniciar o nosso projeto utilizando o Docker. Abra o terminal na raiz do projeto e execute o seguinte comando:

```bash
docker-compose up --build
```

Agora, abra o navegador e acesse a URL `http://localhost:8000/docs`. Você verá a documentação da nossa API. Vamos testar a nossa rota de listagem de produtos. Clique no botão `Try it out` e insira a expressão `2+2`. Clique em `Execute` e veja o resultado. Agora, insira a expressão `2+2` novamente e clique em `Execute`. Você verá que o resultado foi retornado do cache.

Para verificar se o cache está funcionando, abra o terminal e execute o seguinte comando:

```bash
docker exec -it redis redis-cli
```

Agora para pegar todos os valores armazenados no cache, execute o seguinte comando:

```bash
keys "*"
```

Você vai conseguir ver os dados que foram armazenados no cache.

> Mas Murilo, esse cache não vai ficar ai enquanto os servidor estiver rodando? E se eu quiser limpar o cache? Ou ainda se eu quiser invalidar o cache após um valor específico de tempo?

Vamos lá pessoal, essas são perguntas muito importantes. O Redis tem uma série de funcionalidades que podem ser utilizadas para manipular o cache. Vamos ver algumas delas:

### Expiração do Cache

Para definir um tempo de expiração para um valor no cache, podemos utilizar o comando `EXPIRE`. Vamos adicionar um tempo de expiração de 10 segundos para os valores armazenados no cache. Para isso, vamos o arquivo fonte da nossa aplicação e adicionar o seguinte código:

```python
# main.py

from fastapi import FastAPI
from pydantic import BaseModel
from cache import redis_client

# Define a classe de modelo base utilizada
class Pedido(BaseModel):
    expressao:str

app = FastAPI()

@app.post("/evaluate")
async def evaluate(pedido: Pedido):
    # Verifica se a requisição já foi feita
    resultado = redis_client.get(pedido.expressao)
    if resultado:
        return {"resultado": resultado.decode()}
    
    # Calcula o resultado da expressão
    try:
        resultado = eval(pedido.expressao)
        # Armazena o resultado no cache com tempo de expiração de 10 segundos
        redis_client.setex(pedido.expressao, resultado, 10)
        return {"resultado": resultado}
    except Exception as e:
        # Em caso de erro, retorna uma mensagem de erro, mas armazena ela no cache também
        redis_client.setex(pedido.expressao, f"Erro na expressão informada: {e}", 10)
        return {"resultado": f"Erro na expressão informada: {e}"}
    
```

O que aconteceu aqui foi que utilizamos o método `setex` do Redis para armazenar o valor no cache com um tempo de expiração de 10 segundos. Dessa forma, o valor será automaticamente removido do cache após 10 segundos. Essa funcionalidade é muito útil para armazenar valores temporários no cache. Ela evita a necessidade de limpar o cache manualmente e garante que os valores antigos sejam removidos automaticamente.

Agora se for necessário limpar todo o cache, podemos utilizar o comando `FLUSHALL`. Para isso, execute o seguinte comando no terminal:

```bash
# Para conectar no container do Redis
docker exec -it redis redis-cli

# Para limpar o cache
FLUSHALL
```

Pessoal espero que assim vocês consigam compreender como o cache pode ser utilizado e como ele pode ser manipulado. O Redis é uma ferramenta muito poderosa e versátil, que pode ser utilizada de diversas formas. Nesse encontro, utilizamos o Redis como um serviço de cache, mas ele pode ser utilizado para muitas outras finalidades, como armazenamento de dados em memória, suporte a estruturas de dados complexas, entre outras.


