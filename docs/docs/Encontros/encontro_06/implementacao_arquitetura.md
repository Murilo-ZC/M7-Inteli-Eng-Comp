---
sidebar_position: 5
title: Implementando Arquitetura
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Implementando Arquitetura de Microsserviços

Pessoas lindas do meu coração, aqui vamos gastar a ponta dos nossos dedos (ok exagerei mas foi para deixar tudo mais dramático) !!

Vamos implementar algumas arquiteturas de microsserviços, conforme os conceitos que discultimos anteriormente.

Nossa primeira arquitetura já está vindo!

:::warning[AGORA MUUUUITO SÉRIO, PRATIQUEM!]

Pessoal eu vou tentar ao máximo descrever todos os passos para realizarmos a implementação de diversas arquiteturas e serviços e padrões com vocês. Mas, eu apenas estou garantindo para vocês, se vocês não praticarem, não vai adiantar de nada.

<img src="https://external-preview.redd.it/eKcRAzHsHicyHykAqSJCpju139qFIRiPJt4v25TtMXA.jpg?auto=webp&s=6e59d055d1153e423a6c1735ebaa2d7c38a9c58b" style={{ display: 'block', marginLeft: 'auto', maxHeight: '65vh', marginRight: 'auto', marginBottom: '24px' }}/>


:::

---

## Arquitetura 01 - Comunicação Assíncrona com RabbitMQ

Pessoal, para iniciarmos nosso estudo, vamos implementar um sistema como descrito na imagem abaixo:

<img src={useBaseUrl("/img/microsservicos/arquitetura_01.png")} style={{ display: 'block', marginLeft: 'auto', maxHeight: '65vh', marginRight: 'auto', marginBottom: '24px' }}/>

O que está acontecendo aqui:

- Temos um `gateway`, implementado com o ***Nginx***, que recebe as requisições HTTP externa e as encaminha para o serviço adequado.
- Temos o nosso `Service01`, que é responsável por receber as requisições do `gateway` e encaminhar para o `RabbitMQ`. Ele recebe requisições do tipo `POST` e envia para o `RabbitMQ` a data e hora que a requisição ocorreu. Ele disponibiliza um endpoint `/ping` que recebe as requisições.
- Temos o nosso `Service02`, que é responsável por receber as mensagens do `RabbitMQ` e armazenar em um banco de dados em memória (isso mesmo é só uma lista de objetos em memória). Ele disponibiliza um endpoint `/pong` que recebe as requisições do tipo `GET` para retornar a lista de mensagens armazenadas.
- Por fim, temos nosso broker de mensagens, o `RabbitMQ`, que é responsável por receber as mensagens do `Service01` e encaminhar para o `Service02`.

### Verificando os requisitos

Legal, agora que falamos como nossa arquitetura funciona, vamos verificar os requisitos para implementar ela:

- [ ] Ter o ***Nginx*** instalado e configurado para encaminhar as requisições para o `Service01` e para o `Service02`.
- [ ] Ter o ***RabbitMQ*** instalado e configurado para receber as mensagens do `Service01` e encaminhar para o `Service02`.
- [ ] Ter o `Service01` implementado para receber as requisições do `gateway` e encaminhar para o `RabbitMQ`.
- [ ] Ter o `Service02` implementado para receber as mensagens do `RabbitMQ` e armazenar em um banco de dados em memória.

Assim que tivermos todo o nosso ***checklist*** preenchido, vamos ter nosso sistema funcionando 🐨🐳!!

Pensado de forma pedagógica, seria mais interessante colocarmos esses passos em ordem. Masssss, vamos utilizar a premissa de que o time deve escolher o que vai priorizar para implementar primeiro! Logo, vamos criar um diretório para que os arquivos de nossa solução possam ser organizados.

A minha sugestão de diretórios seria:

```bash
microsservicos/
├── Service01/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
├── Service02/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
├── nginx/
│   ├── nginx.conf
├── rabbitmq/
├── docker-compose.yml
```

:::tip[Calma, calma, calma!]

Não precisamos já criar toda nossa estrutura de arquivos. Vamos implementando conforme vamos avançando. Mas, é sempre bom ter uma ideia de como vamos organizar nossos arquivos.

:::

### Adicionando o Service01 e o docker-compose

Vamos iniciar implementando o nosso `Service01`, o `RabbitMQ` e o docker-compose que vai ligar esses dois. Como só temos parte da nossa estrutura, vamos ver como ficou nossa estrutura de pastas:

```bash
microsservicos/
├── Service01/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
├── rabbitmq/
│   ├── .gitkeep
├── docker-compose.yml
├── .env
```

> Calma lá Murilo, tem arquivos novos ai pô!

Sim, sim, sim! Vamos criar um arquivo `.env` dentro da pasta `Service01` para armazenar as variáveis de ambiente que vamos utilizar em nosso serviço. Por que vamos fazer isso? Você pode se perguntar. Com as nossas variáveis de ambiente armazenadas em um arquivo `.env`, podemos utilizar o `docker-compose` para passar essas variáveis para o nosso container. Assim, não precisamos ficar alterando o código toda vez que precisamos mudar uma variável de ambiente.

Vamos escrever primeiro nosso serviço `Service01`. Ele é uma aplicação que utilizar o Flask e o Uvicorn como dependências. Vamos criar o arquivo `app.py` dentro da pasta `Service01` com o seguinte conteúdo:

```python
# Service01/app.py

from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
app = FastAPI()

class Message(BaseModel):
    date: datetime = None
    msg: str

messages = []

@app.post("/ping")
async def ping(msg: Message):
    msg.date=datetime.now()
    return {"message": f"Created at {msg.date}", "content": f"{msg.msg}"}

# Executa a aplicação com a informação de HOST e PORTA enviados por argumentos
if __name__ == "__main__":
    import uvicorn
    import os
    print(os.environ)
    if "SERVICE_01_HOST" in os.environ and "SERVICE_01_PORT" in os.environ:
        uvicorn.run(app, host=os.environ["SERVICE_01_HOST"], port=os.environ["SERVICE_01_PORT"])
    else:
        raise Exception("HOST and PORT must be defined in environment variables")

```

Agora, vamos criar o arquivo `Dockerfile` dentro da pasta `Service01` com o seguinte conteúdo:

```Dockerfile
# Service01/Dockerfile

FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

Por fim, vamos criar o arquivo `requirements.txt` dentro da pasta `Service01` com o seguinte conteúdo:

```txt
fastapi==0.68.1
uvicorn==0.15.0
```

Agora, vamos criar o arquivo `docker-compose.yml` na raiz do nosso projeto. Aqui teremos algumas diferenças, dentre elas, a utilização dos dados presentes no arquivo `.env` para passar as variáveis de ambiente para o nosso container. Vamos criar o arquivo `docker-compose.yml` com o seguinte conteúdo:

```yaml
# docker-compose.yml

version: '3.8'

services:
  service01:
    build:
      context: ./Service01
    ports:
      - "${SERVICE01_HOST_PORT}:${SERVICE_01_PORT}"
    environment:
      - SERVICE_01_HOST=${SERVICE_01_HOST}
      - SERVICE_01_PORT=${SERVICE_01_PORT}

```

Por fim, vamos criar o arquivo `.env` dentro da pasta `Service01` com o seguinte conteúdo:

```env
SERVICE_01_HOST=0.0.0.0
SERVICE_01_PORT=8001
SERVICE01_HOST_PORT=8000
```

> Murilo, eita nóis, tem muita coisa nova ai!

<img src="https://pbs.twimg.com/media/Ei8Gep-XYAADnPO.jpg" style={{ display: 'block', marginLeft: 'auto', maxHeight: '65vh', marginRight: 'auto', marginBottom: '24px' }}/>

Calma, calma, calma! Vamos entender o que fizemos:

- Arquivo `app.py`:
    - Criamos uma aplicação `FastAPI` que possui um endpoint `/ping` que recebe uma mensagem e retorna a data e hora que a mensagem foi recebida.
    - Utilizamos o `pydantic` para definir o modelo da mensagem que será recebida. Assim, podemos definir qual o formato da mensagem que será recebida. Se o JSON enviado não estiver no formato esperado, o `FastAPI` retorna um erro.
    - Para receber as variáveis de ambiente `SERVICE_01_HOST` e `SERVICE_01_PORT`, utilizamos a biblioteca `os`. Com o `os.environ`, conseguimos acessar as variáveis de ambiente do sistema operacional. No nosso caso, as variáveis de ambiente são passadas pelo `docker-compose` e ficam acessíveis para a aplicação.
    - Utilizamos o `uvicorn` para executar a aplicação. O `uvicorn` é um servidor ASGI que permite executar aplicações `FastAPI`.

- Arquivo `Dockerfile`:
    - Utilizamos a imagem `python:3.8-slim` como base para a nossa aplicação. Essa imagem já possui o Python 3.8 instalado e é uma versão mais leve da imagem `python:3.8`.
    - Definimos o diretório de trabalho como `/app`.
    - Copiamos o arquivo `requirements.txt` para o diretório `/app`.
    - Instalamos as dependências do arquivo `requirements.txt` com o comando `pip install -r requirements.txt`.
    - Copiamos todos os arquivos do diretório atual para o diretório `/app`.
    - Definimos o comando que será executado quando o container for iniciado. Neste caso, executamos o arquivo `app.py`.

- Arquivo `.env`:
    - Definimos as variáveis de ambiente `SERVICE_01_HOST`, `SERVICE_01_PORT` e `SERVICE01_HOST_PORT`. Essas variáveis de ambiente são utilizadas para definir o host, a porta e a porta de exposição do serviço `Service01`.

- Arquivo `docker-compose.yml`:
    - Definimos a versão do `docker-compose` como `3.8`.
    - Criamos um serviço chamado `service01` que utiliza o `Dockerfile` presente no diretório `Service01` para construir a imagem do serviço.
    - Mapeamos a porta `${SERVICE01_HOST_PORT}` do host para a porta `${SERVICE_01_PORT}` do container. Assim, podemos acessar o serviço `Service01` na porta definida em `SERVICE01_HOST_PORT`.
    - Passamos as variáveis de ambiente `SERVICE_01_HOST` e `SERVICE_01_PORT` para o container. Essas variáveis de ambiente são definidas no arquivo `.env` e são utilizadas pela aplicação `Service01`.

Pessoal, vocês virão a beleza desse processo? Se nós alterarmos o nosso arquivo `.env`, não precisamos alterar o nosso código. Isso é muito legal, pois podemos alterar as variáveis de ambiente sem precisar alterar o código da aplicação. Isso facilita a configuração e o gerenciamento das variáveis de ambiente.

<img src="https://i.gifer.com/A5OX.gif" style={{ display: 'block', marginLeft: 'auto', maxHeight: '65vh', marginRight: 'auto', marginBottom: '24px' }}/>

:::danger[Cuidado com apenas o resultado pronto]

Pessoal eu queria muito dizer para vocês que foi super fácil, sem problemas, que passar mantega no pão foi mais dificil. Mas, ao menos para mim, não foi assim que eu implementei esses passos. Eu tive que pesquisar, errar, testar, errar, corrigir, errar, errar, erarrr, errrarrrr e até que enfim conseguir implementar a solução da maneira que eu gostaria de apresentar para vocês.

Então, não se preocupem se vocês não conseguirem implementar de primeira. O importante é tentar, errar, corrigir e tentar de novo. A prática leva a perfeição. As 32x que eu tive que remover a imagem desse Service01 que o digam.

:::

Beleza, mas agora vamos lá, ainda não devemos comemorar!! Faltam muitas coisas aqui para terminarmos nosso primeiro passo! Vamos adicionar o RabbitMQ nessa brincadeira!

### Adicionando o RabbitMQ

Vamos utilizar a imagem oficial do RabbitMQ, disponível no [DockerHub](https://hub.docker.com/_/rabbitmq). Essa imagem vai ser adicionada no nosso arquivo `docker-compose.yml` para que o `docker-compose` possa baixar e executar o RabbitMQ. Além disso, vamos configurar dentro do nosso arquivo de `.env` uma variável para definir o nosso usuário e a senha do RabbitMQ.

Vamos adicionar as variáveis de ambiente no arquivo `.env`:

```env
# Configurações do Service01

SERVICE_01_HOST=0.0.0.0
SERVICE_01_PORT=8001
SERVICE01_HOST_PORT=8000

# Configurando o RabbitMQ

RABBITMQ_DEFAULT_USER=inteli
RABBITMQ_DEFAULT_PASS=inteli_secret
RABBITMQ_HOST=rabbitmq
RABBITMQ_PORT=5672
RABBITMQ_QUEUE=mensagens_async
```

Agora vamos adicionar o serviço do RabbitMQ no nosso arquivo `docker-compose.yml`:

```yaml
# docker-compose.yml

version: '3.8'

services:
  service01:
    build:
      context: ./Service01
    ports:
      - "${SERVICE01_HOST_PORT}:${SERVICE_01_PORT}"
    env_file:
      - .env
    depends_on:
      - rabbitmq

  rabbitmq:
    image: rabbitmq:3.12.14-management-alpine
    ports:
      - "5672:5672"
      - "15672:15672"
    environment:
      - RABBITMQ_DEFAULT_USER=${RABBITMQ_DEFAULT_USER}
      - RABBITMQ_DEFAULT_PASS=${RABBITMQ_DEFAULT_PASS}
```

Quando utilizamos a versão `management-alpine` da imagem do RabbitMQ, temos acesso a uma interface web que nos permite visualizar as filas, as trocas e os usuários do RabbitMQ. Essa interface é muito útil para debugar e monitorar o RabbitMQ. Para acessar a interface web, basta acessar o endereço [`http://localhost:15672`](http://localhost:15672/) no navegador e informar o usuário e a senha configurados no arquivo `.env`.

Pessoal reparem que adicionamos a variável `depends_on` no serviço `service01`. Essa variável indica que o serviço `service01` depende do serviço `rabbitmq`. Com isso, o `docker-compose` garante que o serviço `rabbitmq` seja iniciado antes do serviço `service01`. Isso é importante, pois o `service01` precisa do `rabbitmq` para enviar as mensagens.

Outro ponto importante, o `env_file` no serviço `service01` indica que as variáveis de ambiente do arquivo `.env` serão passadas para o container do serviço `service01`. Assim, as variáveis de ambiente definidas no arquivo `.env` ficam acessíveis para a aplicação `Service01`.

E boa!!! Temos nosso RabbitMQ funcionando, mas ainda não temos a comunicação entre o Service01 e o RabbitMQ. Vamos implementar essa comunicação agora!

### Comunicação entre Service01 e RabbitMQ

Para enviar mensagens para o RabbitMQ, vamos utilizar a biblioteca `pika`. Essa biblioteca é uma implementação do protocolo AMQP (Advanced Message Queuing Protocol) para Python. Com o `pika`, podemos enviar e receber mensagens do RabbitMQ de forma assíncrona. Mais informações sobre a biblioteca, podemos acessar a [documentação oficial](https://pika.readthedocs.io/en/stable/).

Para isso, vamos ter que fazer algumas modificações no nosso arquivo `app.py` do `Service01`. Vamos adicionar a comunicação com o RabbitMQ para enviar as mensagens recebidas no endpoint `/ping`. Vamos modificar também o arquivo `requirements.txt` para adicionar a dependência do `pika`.

```txt
fastapi==0.68.1
uvicorn==0.15.0
pika==1.2.0
```

:::danger[Mudança na estrutura da imagem]

Pessoal, aqui chegamos em um ponto importante. Nós vamos ter que modificar a estrutura da nossa imagem do `Service01` para que ele consiga se comunicar com o RabbitMQ. Vamos adicionar a comunicação com o RabbitMQ no arquivo `app.py`. Vamos precisar informar que o docker precisa reconstruir a imagem do `Service01` para que ele possa adicionar a dependência do `pika`.

Vamos excluir nossas imagens  Excluir nossa imagem antiga e criar uma nova imagem com o comando `docker-compose up --build`.


:::

Vamos modificar o arquivo `app.py` do `Service01` para adicionar a comunicação com o RabbitMQ:

```python

# Service01/app.py

# Adicionando a funcionalidade de enviar mensagens com data e hora para o broker do RabbitMQ

from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import pika

app = FastAPI()

class Message(BaseModel):
    date: datetime = None
    msg: str

# Cria uma função que faz o envio das mensagens para o RabbitMQ
def send_message_rabbitmq(msg: Message):
    # Verifica se as variáveis de ambiente estão definidas
    if "RABBITMQ_HOST" not in os.environ or "RABBITMQ_PORT" not in os.environ:
        raise Exception("RABBITMQ_HOST and RABBITMQ_PORT must be defined in environment variables")

    credentials = pika.PlainCredentials(os.environ["RABBITMQ_DEFAULT_USER"], os.environ["RABBITMQ_DEFAULT_PASS"])
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        os.environ["RABBITMQ_HOST"]
        , os.environ["RABBITMQ_PORT"]
        , '/'
        , credentials))
    channel = connection.channel()
    channel.queue_declare(queue=os.environ["RABBITMQ_QUEUE"])
    channel.basic_publish(exchange='', routing_key=os.environ["RABBITMQ_QUEUE"], body=f"{msg.date} - {msg.msg}")
    connection.close()

@app.post("/ping")
async def ping(msg: Message):
    msg.date=datetime.now()
    send_message_rabbitmq(msg)
    return {"message": f"Created at {msg.date}", "content": f"{msg.msg}"}

# Executa a aplicação com a informação de HOST e PORTA enviados por argumentos
if __name__ == "__main__":
    import uvicorn
    import os
    print(os.environ)
    if "SERVICE_01_HOST" in os.environ and "SERVICE_01_PORT" in os.environ:
        uvicorn.run(app, host=os.environ["SERVICE_01_HOST"], port=os.environ["SERVICE_01_PORT"])
    else:
        raise Exception("HOST and PORT must be defined in environment variables")

```

E pronto, agora temos nosso `Service01` enviando mensagens para o RabbitMQ. Vamos testar se a comunicação está funcionando corretamente. Para isso, vamos iniciar o RabbitMQ e o Service01 com o comando `docker-compose up`. Em seguida, vamos acessar o endpoint `/ping` do Service01 para enviar uma mensagem para o RabbitMQ.

Estamos avançando!! Como está nosso estado atual:

- [ ] Ter o ***Nginx*** instalado e configurado para encaminhar as requisições para o `Service01` e para o `Service02`.
- [x] Ter o ***RabbitMQ*** instalado e configurado para receber as mensagens do `Service01` e encaminhar para o `Service02`.
- [x] Ter o `Service01` implementado para receber as requisições do `gateway` e encaminhar para o `RabbitMQ`.
- [ ] Ter o `Service02` implementado para receber as mensagens do `RabbitMQ` e armazenar em um banco de dados em memória.

Vamos agora configurar o `Service02` para receber as mensagens do RabbitMQ e armazenar em um banco de dados em memória.

### Adicionando o Service02

Agora vamos construir nosso segundo serviço. Vamos criar a estrutura de pastas para o `Service02` e adicionar o arquivo `app.py`. Os arquivos `Dockerfile` e `requirements.txt` serão os mesmos do `Service01`. Vamos criar o arquivo `app.py` dentro da pasta `Service02` com o seguinte conteúdo:

```python
# Serviço 2 - recebe as mensagens via RabbitMQ e as armazena em um banco de dados em memória

from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import pika
import os

app = FastAPI()
banco_em_memoria = []

class Message(BaseModel):
    date: datetime = None
    msg: str

# Cria uma função que recebe as mensagens para o RabbitMQ
def receive_message_rabbitmq():
    # Verifica se as variáveis de ambiente estão definidas
    if "RABBITMQ_HOST" not in os.environ or "RABBITMQ_PORT" not in os.environ:
        raise Exception("RABBITMQ_HOST and RABBITMQ_PORT must be defined in environment variables")

    credentials = pika.PlainCredentials(os.environ["RABBITMQ_DEFAULT_USER"], os.environ["RABBITMQ_DEFAULT_PASS"])
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        os.environ["RABBITMQ_HOST"]
        , os.environ["RABBITMQ_PORT"]
        , '/'
        , credentials))
    channel = connection.channel()
    channel.queue_declare(queue=os.environ["RABBITMQ_QUEUE"], durable=True)
    channel.basic_consume(queue=os.environ["RABBITMQ_QUEUE"], on_message_callback=callback, auto_ack=True)
    channel.start_consuming()

def callback(ch, method, properties, body):
    print(f" [x] Received {body}")
    banco_em_memoria.append(body)

@app.get("/messages")
async def get_messages():
    return banco_em_memoria

# Executa a aplicação com a informação de HOST e PORTA enviados por argumentos
if __name__ == "__main__":
    import uvicorn
    import os
    print(os.environ)
    if "SERVICE_02_HOST" in os.environ and "SERVICE_02_PORT" in os.environ:
        receive_message_rabbitmq()
        uvicorn.run(app, host=os.environ["SERVICE_02_HOST"], port=os.environ["SERVICE_02_PORT"])
    else:
        raise Exception("HOST and PORT must be defined in environment variables")

```

Agora vamos compreender o que está acontecendo aqui:

- Criamos uma aplicação `FastAPI` que possui um endpoint `/messages` que retorna a lista de mensagens armazenadas em um banco de dados em memória.
- Criamos uma lista `banco_em_memoria` que armazena as mensagens recebidas do RabbitMQ.
- Criamos uma função `receive_message_rabbitmq` que recebe as mensagens do RabbitMQ e armazena no banco de dados em memória.
- Criamos uma função `callback` que é chamada quando uma mensagem é recebida do RabbitMQ. Essa função adiciona a mensagem no banco de dados em memória.
- Criamos um endpoint `/messages` que retorna a lista de mensagens armazenadas no banco de dados em memória.

Agora vamos ajustar o arquivo `.env` para adicionar as variáveis de ambiente do `Service02`:

```env
# Configurações do Service01

SERVICE_01_HOST=0.0.0.0
SERVICE_01_PORT=8001
SERVICE01_HOST_PORT=8000

# Configurando o RabbitMQ

RABBITMQ_DEFAULT_USER=inteli
RABBITMQ_DEFAULT_PASS=inteli_secret
RABBITMQ_HOST=rabbitmq
RABBITMQ_PORT=5672
RABBITMQ_QUEUE=mensagens_async

# Configurações do Service02

SERVICE_02_HOST=0.0.0.0
SERVICE_02_PORT=8000
SERVICE02_HOST_PORT=8002
```

Agora vamos adicionar o serviço `service02` no nosso arquivo `docker-compose.yml`:

```yaml
# docker-compose.yml

version: '3.8'

services:
  service01:
    build:
      context: ./Service01
    ports:
      - "${SERVICE01_HOST_PORT}:${SERVICE_01_PORT}"
    env_file:
      - .env
    depends_on:
      - rabbitmq

  rabbitmq:
    image: rabbitmq:3.12.14-management-alpine
    ports:
      - "5672:5672"
      - "15672:15672"
    environment:
      - RABBITMQ_DEFAULT_USER=${RABBITMQ_DEFAULT_USER}
      - RABBITMQ_DEFAULT_PASS=${RABBITMQ_DEFAULT_PASS}

  service02:
    build:
      context: ./Service02
    ports:
      - "${SERVICE02_HOST_PORT}:${SERVICE_02_PORT}"
    env_file:
      - .env
    depends_on:
      - rabbitmq
```

Pronto, agora temos o nosso `Service02` implementado e configurado no `docker-compose`. Vamos testar se a comunicação entre o `Service01` e o `Service02` está funcionando corretamente. Para isso, vamos iniciar o RabbitMQ, o Service01 e o Service02 com o comando `docker-compose up`. Em seguida, vamos acessar o endpoint `/ping` do Service01 para enviar uma mensagem para o RabbitMQ. Por fim, vamos acessar o endpoint `/messages` do Service02 para verificar se a mensagem foi armazenada corretamente.

Espera um pouco, temos um problema aqui. O `Service02` não está recebendo as mensagens do RabbitMQ. Isso ocorre porque o `Service02` não está executando a função `receive_message_rabbitmq`. Para corrigir isso, vamos modificar o arquivo `app.py` do `Service02` para executar a função `receive_message_rabbitmq` quando o serviço for iniciado.

Massss antes de continuarmos, vamos entender o que está acontecendo. A biblioteca `pika` é uma biblioteca síncrona, ou seja, ela bloqueia a execução do programa enquanto aguarda a chegada de mensagens. Para resolver esse problema, precisamos utilizar algum recurso que permita a execução da função `receive_message_rabbitmq` em ***PARALELO*** com a execução da aplicação. Eles precisam compartilhar o mesmo contexto de execução, mas precisam ser executados em ***PARALELO***.

Mesmo processo, execução em paralelo, lembra algo? Em especial algo que falamos que se inicia com a letra ***T***. Sim, sim, sim, ***THREADS***. Vamos utilizar ***THREADS*** para executar a função `receive_message_rabbitmq` em ***PARALELO*** com a execução da aplicação.

Vamos alterar o código do nosso `Service02` para adicionar a execução da função `receive_message_rabbitmq` em ***THREADS***:

```python
# Serviço 2 - recebe as mensagens via RabbitMQ e as armazena em um banco de dados em memória

from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import threading
import pika
import os
# Ajuste para tentar reconectar ao RabbitMQ
from pika.connection import Parameters
Parameters.DEFAULT_CONNECTION_ATTEMPTS = 10



app = FastAPI()
banco_em_memoria = []

class Message(BaseModel):
    date: datetime = None
    msg: str

# Função de callback utilizada
def callback(ch, method, properties, body):
    print(f" [x] Received {body}")
    banco_em_memoria.append(body)

# Cria uma função que recebe as mensagens para o RabbitMQ
def receive_message_rabbitmq():
    # Verifica se as variáveis de ambiente estão definidas
    if "RABBITMQ_HOST" not in os.environ or "RABBITMQ_PORT" not in os.environ:
        raise Exception("RABBITMQ_HOST and RABBITMQ_PORT must be defined in environment variables")

    credentials = pika.PlainCredentials(os.environ["RABBITMQ_DEFAULT_USER"], os.environ["RABBITMQ_DEFAULT_PASS"])
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        os.environ["RABBITMQ_HOST"]
        , os.environ["RABBITMQ_PORT"]
        , '/'
        , credentials))
    channel = connection.channel()
    channel.queue_declare(queue=os.environ["RABBITMQ_QUEUE"])
    channel.basic_consume(queue=os.environ["RABBITMQ_QUEUE"], on_message_callback=callback)
    channel.start_consuming()


@app.get("/messages")
async def get_messages():
    return banco_em_memoria

# Executa a aplicação com a informação de HOST e PORTA enviados por argumentos
if __name__ == "__main__":
    import uvicorn
    import os
    print(os.environ)
    if "SERVICE_02_HOST" in os.environ and "SERVICE_02_PORT" in os.environ:
        try:    
            # Cria uma thread para receber as mensagens do RabbitMQ
            thread = threading.Thread(target=receive_message_rabbitmq)
            thread.start()
            uvicorn.run(app, host=os.environ["SERVICE_02_HOST"], port=os.environ["SERVICE_02_PORT"])
        except Exception as e:
            print(f"Finalizando a execução da thread: {e}")
            thread.stop()
    else:
        raise Exception("HOST and PORT must be defined in environment variables")


```

Pessoal agora sim, temos o nosso `Service02` recebendo as mensagens do RabbitMQ e armazenando em um banco de dados em memória. Vamos testar se a comunicação entre o `Service01` e o `Service02` está funcionando corretamente. Para isso, vamos iniciar o RabbitMQ, o Service01 e o Service02 com o comando `docker-compose up`. Em seguida, vamos acessar o endpoint `/ping` do Service01 para enviar uma mensagem para o RabbitMQ. Por fim, vamos acessar o endpoint `/messages` do Service02 para verificar se a mensagem foi armazenada corretamente.

Aeeee temos quase tudo completo agora:

- [ ] Ter o ***Nginx*** instalado e configurado para encaminhar as requisições para o `Service01` e para o `Service02`.
- [x] Ter o ***RabbitMQ*** instalado e configurado para receber as mensagens do `Service01` e encaminhar para o `Service02`.
- [x] Ter o `Service01` implementado para receber as requisições do `gateway` e encaminhar para o `RabbitMQ`.
- [x] Ter o `Service02` implementado para receber as mensagens do `RabbitMQ` e armazenar em um banco de dados em memória.

Vamos lá pessoal só mais um pouco!!
Vamos adicionar o ***Nginx*** para encaminhar as requisições para o `Service01` e para o `Service02`.

### Adicionando o Nginx

Vamos utilizar a imagem oficial do Nginx, disponível no [DockerHub](https://hub.docker.com/_/nginx). Essa imagem vai ser adicionada no nosso arquivo `docker-compose.yml` para que o `docker-compose` possa baixar e executar o Nginx. Além disso, vamos configurar o Nginx para encaminhar as requisições para o `Service01` e para o `Service02`.

Primeiro vamos ajustar nosso arquivo de `nginx.conf` para configurar o Nginx para encaminhar as requisições para o `Service01` e para o `Service02`. Vamos criar o arquivo `nginx.conf` dentro da pasta `nginx` com o seguinte conteúdo:

```nginx
# gateway/nginx.conf

worker_processes 1;

events { worker_connections 1024; }

http {
    sendfile on;

    upstream Service01 {
        server Service01:8001;
    }

    upstream Service02 {
        server Service02:8002;
    }


    server {
        listen 80;

        location /ping {
            proxy_pass http://Service01;
        }

        location /messages {
            proxy_pass http://Service02;
        }

    }
}
```

Observem o que está acontecendo aqui:

- Definimos o número de processos do Nginx como 1.
- Definimos o número de conexões por processo como 1024.
- Configuramos o Nginx para encaminhar as requisições para o `Service01` na porta 8001.
- Configuramos o Nginx para encaminhar as requisições para o `Service02` na porta 8002.
- Criamos um servidor que escuta na porta 80.
- Configuramos o Nginx para encaminhar as requisições para o `Service01` no endpoint `/ping`.
- Configuramos o Nginx para encaminhar as requisições para o `Service02` no endpoint `/messages`.

Agora vamos ajustar o arquivo `docker-compose.yml` para adicionar o serviço `nginx`:

```yaml
# docker-compose.yml

version: '3.8'

services:
  service01:
    build:
      context: ./Service01
    ports:
      - "${SERVICE01_HOST_PORT}:${SERVICE_01_PORT}"
    env_file:
      - .env
    depends_on:
      - rabbitmq


  rabbitmq:
    image: rabbitmq:3.12.14-management-alpine
    ports:
      - "5672:5672"
      - "15672:15672"
    environment:
      - RABBITMQ_DEFAULT_USER=${RABBITMQ_DEFAULT_USER}
      - RABBITMQ_DEFAULT_PASS=${RABBITMQ_DEFAULT_PASS}


  service02:
    build:
      context: ./Service02
    ports:
      - "${SERVICE02_HOST_PORT}:${SERVICE_02_PORT}"
    env_file:
      - .env
    depends_on:
      - rabbitmq
    restart: on-failure

  gateway:
    build: ./nginx
    ports:
      - "8000:80"
```

Agora pessoal, para subir nossa aplicação, vamos executar o comando `docker-compose up`. Em seguida, vamos acessar o endpoint `/ping` do Nginx para enviar uma mensagem para o RabbitMQ. Por fim, vamos acessar o endpoint `/messages` do Nginx para verificar se a mensagem foi armazenada corretamente.

Enfim!!! Temos nosso sistema funcionando 🐨🐳!! Parabéns a todos que chegaram até aqui. Agora, vamos comemorar e descansar um pouco.

Pessoal, eu queria muito me vangloriar e dizer que nós estudamos o comportamento das Threads para utilizar exatamente aqui, quando precisamos delas. Contudo, eu não fiz isso de forma proposital. 

Contudo, queria chamar a atenção de vocês para a importância de compreender alguns comportamentos e conceitos que são base para a construção das nossas soluções. A utilização de Threads é um desses conceitos que são muito importantes para a construção de sistemas distribuídos e escaláveis. Então, não deixem de estudar e compreender esses conceitos, pois eles são fundamentais para a construção de sistemas robustos e escaláveis.

Gostaria de deixar como pensamento final para vocês:

```quote
“A wildfire destroys everything in its path. 
It will be the same with your powers unless you learn to control them.” 
— Giovanni
```

<img src="https://blogger.googleusercontent.com/img/a/AVvXsEgd6-b9tfTF0rXsofi5GG4f2nJvkZyWijBxKtTA8bSxOHNjgPY-vH3TsSSPKP-iRlrEOz2N_penVxMN0s7ImUTPEJ9D9ivnUnvpfzu4fAYZ-iLZvO4E2_IESZ4rodtgIKnCIlHovso7vtsCYup_4RHPWnTlMASK5XWNL9j3YNw3nJNpXLptdrpC7WpD=w1600" style={{ display: 'block', marginLeft: 'auto', maxHeight: '65vh', marginRight: 'auto', marginBottom: '24px' }}/>
