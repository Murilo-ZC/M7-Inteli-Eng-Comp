---
sidebar_position: 2
title: Relembrando a Ferramenta Docker e sua utilização
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Relembrando a Ferramenta Docker e sua utilização

Vamos relembrar alguns pontos importantes para utilização do Docker e aplicações conteinerizadas.

## Um pouco de contexto

Problemas comuns no desenvolvimento de soluções de software:
- Diferentes setup's de hardware e software;
- Diferentes conjuntos de requisitos para rodar uma aplicação;
- Demanda por isolamento entre aplicações;
- Necessidade de escala de partes da solução.

Quais são as possíveis soluções que temos para esse problema? Podemos utilizar máquinas virtuais!
Máquinas Virtuais (VMs) são ambientes computacionais simulados que funcionam como sistemas de computador completos, incluindo CPU, memória, disco e outros recursos. Elas são criadas e executadas em um servidor físico, permitindo que um único hardware execute vários sistemas operacionais e aplicativos independentes.

A virtualização é alcançada através de um software chamado hipervisor ou monitor de máquina virtual, que gerencia e aloca recursos entre as VMs. VMs oferecem isolamento, permitindo a execução segura de aplicativos e sistemas operacionais diferentes em uma mesma máquina física. São úteis para testes, desenvolvimento, consolidação de servidores, backup, recuperação de desastres e fornecimento rápido de ambientes replicáveis. Exemplos de tecnologias de virtualização incluem VMware, Microsoft Hyper-V, KVM (Kernel-based Virtual Machine) e VirtualBox.

<img src="https://cdn.ttgtmedia.com/rms/onlineimages/virtual_machines-h_half_column_mobile.png" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom: '24px' }}/>

A imagem acima apresenta o processo de utilização das máquinas virtuais. Um servidor físico possui um hardware e um sistema operacional próprio. Estes elementos possuem uma característica de ser chamados de `elementos de host`. Neste servidor, é instalado um software chamado de `hypervisor`, ele que vai permitir executar os sistemas convidados neste sistema nativo. Cada máquina virtual será criada como uma instância que deve possuir `Guest OS` e as aplicações que estão sendo executadas dentro dela.

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRNScWo5JpS77L3GWqtDobfEHru5DpjBcsDkuSqcjCxIg&s" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom: '24px' }}/>

Mas onde entram os containers nessa conversa?

Containers são como cestas de piquinique, tudo que precisamos para comer uma refeição está dentro dela, assim como tudo que precisamos para executar uma aplicação já está dentro dele. Para executar containers, é necessário um Container Engine sendo executado no sistema operacional host.

<img src="https://masterfromus.files.wordpress.com/2020/02/image-4.png?w=921" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom: '24px' }}/>

A partir de agora vamos iniciar a utilização do Docker.

## Utilizando Docker

Vamos executar um container de `hello-world` no docker. No terminal, executar o comando:

```sh
docker run hello-world
```

Vamos obter a seguinte resposta:

```sh
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
719385e32844: Pull complete 
Digest: sha256:926fac19d22aa2d60f1a276b66a20eb765fbeea2db5dbdaafeb456ad8ce81598
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

:::tip[O que aconteceu aqui?]

> Mas Murilo o que aconteceu aqui mesmo?

<img src="https://pa1.aminoapps.com/6925/606ef81cfe6a33308600d6a7444a8527a78dca27r1-288-216_00.gif" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom: '24px' }}/>

Vamos avaliar o que aconteceu aqui:

1. O comando `docker run hello-world` foi executado no terminal;
2. O Docker Client entrou em contato com o Docker Daemon;
3. O Docker Daemon procurou a imagem do `hello-world` e não encontrou. Ele baixou a imagem `hello-world` do Docker Hub;
4. O Docker Daemon criou um novo container a partir da imagem baixada e executou o comando que produziu a saída que estamos lendo;
5. O Docker Daemon enviou a saída para o Docker Client, que a enviou para o terminal.

Esse foi o processo de execução de um container no Docker. Vamos continuar com a execução de containers no Docker.

:::

Um detalhe importante é que um container apenas é executado enquanto o processo que ele está executando estiver em execução. Quando o processo termina, o container é encerrado. Para executar um container em modo interativo, é necessário utilizar o comando `docker run -it ubuntu bash`. Vamos executar este comando no terminal.

```sh
docker run -it ubuntu bash
```

O que vai acontecer agora é que a imagem do Ubuntu será baixada e um container será criado. O terminal será alterado para o terminal do container. Vamos executar o comando `ls` para listar os arquivos do container.

```sh
ls
```

Repare que os arquivos listados são os arquivos do container. Vamos executar o comando `exit` para sair do container.

```sh
exit
```

Agora o container foi encerrado e o terminal voltou ao terminal do host. Porque isso aconteceu? Porque o processo que estava sendo executado no container foi encerrado. E qual era o processo? O processo era o terminal bash. Quando o terminal bash foi encerrado, o container foi encerrado.

:::tip[O que aconteceu aqui?]

> Mas Murilo, calma ai! Como vou saber quais containers estão em execução?

<img src="https://pa1.aminoapps.com/6925/606ef81cfe6a33308600d6a7444a8527a78dca27r1-288-216_00.gif" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom: '24px' }}/>

Vamos verificar isso! Para verificar os containers em execução, é necessário executar o comando `docker container ps`. Vamos executar este comando no terminal.

```sh
docker container ps
```

Vamos obter a seguinte resposta:

```sh
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

Repare que temos os cabeçalhos das informações dos containers. Neste caso, não temos nenhum container em execução. Vamos executar o comando `docker container ps -a` para verificar todos os containers que foram executados.

```sh
docker container ps -a
```

Agora vamos obter a seguinte resposta:

```sh
CONTAINER ID   IMAGE         COMMAND    CREATED          STATUS                          PORTS     NAMES
95def145d17a   ubuntu        "bash"     2 minutes ago    Exited (0) About a minute ago             boring_hugle
20f0398d420f   hello-world   "/hello"   23 minutes ago   Exited (0) 23 minutes ago                 trusting_taussig
```

Agora pessoal, vamos ver algumas coisas importantes aqui. O comando `docker container ps -a` nos mostra todos os containers que foram executados. Repare que temos o `CONTAINER ID`, `IMAGE`, `COMMAND`, `CREATED`, `STATUS`, `PORTS` e `NAMES`. O `CONTAINER ID` é um identificador único para o container. O `IMAGE` é a imagem que foi utilizada para criar o container. O `COMMAND` é o comando que foi executado no container. O `CREATED` é o tempo que o container foi criado. O `STATUS` é o status atual do container. O `PORTS` são as portas que estão sendo utilizadas pelo container. O `NAMES` é o nome do container. Quando nenhum nome é atribuído ao container, o Docker atribui um nome aleatório.

Vamos continuar estudando!

:::

Agora vamos utilizar algumas opções do comando `docker run`. Vamos executar o comando `docker run -d -p 8080:80 nginx` para executar um container do Nginx em modo `detached` e mapear a porta `8080` do host para a porta `80` do container.

```sh
docker run -d -p 8080:80 nginx
```

Agora o que vai acontecer? Vamos conseguir acessar o Nginx no navegador? Vamos verificar isso! Vamos acessar o endereço `http://localhost:8080` no navegador.

<img src={useBaseUrl("/img/docker-base/tela-saida-nginx.png")} alt="Utilizando baseUrl" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'24px' }} />

Podemos conseguir acessar o Nginx no navegador. O que aconteceu aqui? O comando `docker run -d -p 8080:80 nginx` foi executado no terminal. O Docker Daemon procurou a imagem do Nginx e não encontrou. Ele baixou a imagem do Nginx do Docker Hub. O Docker Daemon criou um novo container a partir da imagem baixada e mapeou a porta `8080` do host para a porta `80` do container. O Nginx foi executado no container e o Nginx foi acessado no navegador.

:::tip[Onde será que estão essas imagens?]

<img src="https://pa1.aminoapps.com/6207/8a22f6d4b44447096b45b89b5416deb4780e9317_hq.gif" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom: '24px' }}/>

Temos uma pergunta importante a ser respondida. Onde estão as imagens que foram baixadas? As imagens que foram baixadas estão armazenadas no Docker Host. 

> Mas Murilo, como vou saber quais imagens estão armazenadas no Docker Host?

Você pode verificar as imagens que estão armazenadas no Docker Host utilizando o comando `docker image ls`. Vamos executar este comando no terminal. Vamos obter a seguinte saída:

```sh
REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
nginx         latest    2ac752d7aeb1   7 days ago      188MB
ubuntu        latest    7af9ba4f0a47   12 days ago     77.9MB
hello-world   latest    d2c94e258dcb   11 months ago   13.3kB
```

> Mas Murilo, onde é o Docker Host?

O Docker Host é o sistema operacional onde o Docker está sendo executado. No nosso caso, o Docker Host é o sistema operacional Ubuntu.
Outro ponto bastante importante, pode ser que você queira remover uma imagem que não está sendo utilizada. Para remover uma imagem, é necessário executar o comando `docker image rm <IMAGE_ID>`. Vamos remover a imagem do Nginx. Para isso, vamos executar o comando `docker image rm 2ac752d7aeb1`.

Ao tentar executar esse comando, você vai obter a seguinte resposta:

```sh
Error response from daemon: conflict: unable to delete 2ac752d7aeb1 (cannot be forced) - image is being used by running container e9e805427010
```

Por que isso aconteceu? Isso aconteceu porque a imagem do Nginx está sendo utilizada por um container. Para remover a imagem, é necessário remover o container que está utilizando a imagem. Vamos remover o container que está utilizando a imagem do Nginx. Quando as imagens não estão sendo utilizadas, podemos remover as imagens sem problemas. Basta baixar elas novamente quando for necessário.

:::

Agora vamos parar a execução do container do Nginx. Para parar a execução de um container, é necessário executar o comando `docker container stop <CONTAINER_ID>`. Vamos parar a execução do container do Nginx. 

```sh
docker container ls
docker container stop <ID_DO_CONTAINER_NGINX>
```

Agora vamos executar um container de Nginx, fornecendo uma página HTML para ele. Vamos fazer isso de algumas formas diferentes. Vamos criar um arquivo chamado `index.html` com o seguinte conteúdo:

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Teste de Página HTML</title>
</head>
<body>
    <h1>Teste de Página HTML</h1>
    <p>Esta é uma página HTML de teste.</p>
</body>
</html>
```

Vamos executar o comando `docker run -d -p 8080:80 -v $(pwd)/index.html:/usr/share/nginx/html/index.html nginx` para executar um container do Nginx em modo `detached`, mapear a porta `8080` do host para a porta `80` do container e fornecer a página HTML para o Nginx.

```sh
docker run -d -p 8080:80 -v $(pwd)/index.html:/usr/share/nginx/html/index.html nginx
```

Observe que quando acessamos o endereço `http://localhost:8080` no navegador, a página HTML que fornecemos é exibida.

<img src={useBaseUrl("/img/docker-base/server-personalizado-01.png")} alt="Utilizando baseUrl" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'24px' }} />

Vamos fazer uma modificação no código HTML e vamos recarregar a página no navegador.

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Teste de Página HTML</title>
</head>
<body>
    <h1>Teste de Página HTML</h1>
    <p>Esta é uma página HTML de teste.</p>
    <img src="https://www.icegif.com/wp-content/uploads/2021/11/icegif-110.gif" />
</body>
</html>
```

Agora, vamos apenas recarregar a página no navegador. O que aconteceu?

<img src={useBaseUrl("/img/docker-base/server-personalizado-02.png")} alt="Utilizando baseUrl" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'24px' }} />

Repare que a aplicação não parou de ser executada. O que aconteceu foi que o Nginx recarregou a página HTML que fornecemos. Isso é uma das vantagens de utilizar containers. Mas como isso aconteceu? Nós ligamos um volume do host para o container. O volume é um diretório ou arquivo que é montado no container. Quando o arquivo é modificado no host, o arquivo é modificado no container. Isso é uma das vantagens de utilizar volumes.

:::tip[O que é um volume?]

<img src="https://orig00.deviantart.net/5462/f/2016/314/1/4/porygon_flip_by_cortoony-danyc80.gif" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom: '24px' }}/>

Os volumes são uma forma de persistir dados em containers. Eles são diretórios ou arquivos que são montados no container. Quando um volume é montado no container, o diretório ou arquivo é acessível no container. 

Os volumes são utilizados para persistir dados em containers. Eles são utilizados para armazenar dados que precisam ser persistidos, como arquivos de configuração, arquivos de log, arquivos de banco de dados, entre outros. 

Os volumes são utilizados para armazenar dados que precisam ser compartilhados entre containers. Os volumes são utilizados para armazenar dados que precisam ser acessados por múltiplos containers. Os volumes são utilizados para armazenar dados que precisam ser acessados por containers que estão sendo executados em diferentes hosts.

:::

> Mas Murilo, e quando eu preciso publicar uma imagem em produção?

Em geral, mantemos os volumes de dados separados dos containers. Isso é feito para garantir que os dados sejam mantidos mesmo que o container seja removido. Para publicar uma imagem em produção, é necessário criar um Dockerfile. O Dockerfile é um arquivo que contém as instruções para criar uma imagem. O Dockerfile contém as instruções para instalar as dependências, copiar os arquivos, configurar o ambiente, entre outras coisas. O Dockerfile é utilizado para criar uma imagem que pode ser executada em produção.

Vamos criar um Dockerfile para publicar a página HTML em produção. Vamos criar um arquivo chamado `Dockerfile` com o seguinte conteúdo:

```Dockerfile
FROM nginx:latest

COPY index.html /usr/share/nginx/html/index.html
```

Agora vamos construir uma imagem a partir do Dockerfile. Para construir uma imagem a partir de um Dockerfile, é necessário executar o comando `docker build -t <NOME_DA_IMAGEM> .`. Vamos construir uma imagem a partir do Dockerfile.

```sh
docker build -t meu-nginx .
```

Agora vamos executar um container a partir da imagem que construímos. Vamos executar o comando `docker run -d -p 8080:80 meu-nginx` para executar um container a partir da imagem que construímos.

```sh
docker run -d -p 8080:80 meu-nginx
```

Agora vamos acessar o endereço `http://localhost:8080` no navegador. A página HTML que fornecemos é exibida. A imagem que construímos pode ser utilizada em produção. Quando alguma modificação é feita no código HTML, é necessário construir uma nova imagem e executar um novo container.

:::tip[O que é um Dockerfile?]

<img src="https://64.media.tumblr.com/f575f13ebd2a66e30615c7c4115bc21c/tumblr_oboyc1iMXf1v6bs4yo1_500.gif" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom: '24px' }}/>

Um arquivo Dockerfile é um arquivo de texto que contém as instruções para construir uma imagem. O Dockerfile é utilizado para criar uma imagem que pode ser executada em produção. O Dockerfile contém as instruções para instalar as dependências, copiar os arquivos, configurar o ambiente, entre outras coisas.

Construímos os nossos containers a partir de imagens. As imagens são arquivos que contêm o sistema operacional, as bibliotecas, os binários e os arquivos necessários para executar uma aplicação. As imagens são criadas a partir de um Dockerfile. O Dockerfile é um arquivo de texto que contém as instruções para construir uma imagem.

Nossas imagens são construídas a partir dos Dockerfiles.

Mais informações podem ser encontradas na [documentação oficial do Docker](https://docs.docker.com/engine/reference/builder/). E também na documentação do [Dockerfile](https://docs.docker.com/reference/dockerfile/).

:::

Legal até aqui avançamos bastante no desenvolvimento utilizando Docker. Vamos continuar estudando mais sobre Docker e containers.

---

## Docker Compose

Em diversas aplicações que vamos desenvolver, vai ser necessário utilizar mais de um container. Para facilitar a execução de múltiplos containers, o Docker Compose é uma ferramenta que permite definir e executar aplicações multi-container. 

O Docker Compose é utilizado para definir os serviços, as redes e os volumes que compõem a aplicação. O Docker Compose é utilizado para executar os containers da aplicação.

Vamos lançar um serviço que utiliza o Postgres e o Adminer. Para isso, vamos criar um arquivo chamado `docker-compose.yml` com o seguinte conteúdo:

```yml
# Use postgres/example user/password credentials
version: '3.9'

services:

  db:
    image: postgres
    restart: always
    # set shared memory limit when using docker-compose
    shm_size: 128mb
    # or set shared memory limit when deploy via swarm stack
    #volumes:
    #  - type: tmpfs
    #    target: /dev/shm
    #    tmpfs:
    #      size: 134217728 # 128*2^20 bytes = 128Mb
    environment:
      POSTGRES_PASSWORD: example

  adminer:
    image: adminer
    restart: always
    ports:
      - 8080:8080
```

Para executar os containers, é necessário executar o comando `docker-compose up -d`. Vamos executar este comando no terminal.

```sh
docker-compose up -d
```

Agora vamos acessar o endereço `http://localhost:8080` no navegador. O Adminer é exibido. O Adminer é um cliente de banco de dados que permite gerenciar os bancos de dados.

:::tip[O que é está acontecendo aqui?]

<img src="https://64.media.tumblr.com/f575f13ebd2a66e30615c7c4115bc21c/tumblr_oboyc1iMXf1v6bs4yo1_500.gif" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom: '24px' }}/>

Vamos avaliar o que aconteceu aqui:

1. O arquivo `docker-compose.yml` foi criado com as definições dos serviços `db` e `adminer`;
2. Definimos a versão do Docker Compose;
3. Definimos os serviços `db` e `adminer`;
4. O serviço `db` utiliza a imagem do Postgres e define a senha do Postgres;
5. Estabelecemos o comportamento de reinicialização do container. Quando definimos ele para `always`, o container será reiniciado sempre que ele for encerrado;
6. Definimos o tamanho do shared memory limit para o container;
7. O serviço `adminer` utiliza a imagem do Adminer e define a porta `8080` do host para a porta `8080` do container;
8. O comando `docker-compose up -d` foi executado no terminal;
9. O Docker Compose criou os containers `db` e `adminer` a partir das imagens do Postgres e do Adminer;
10. O Adminer foi acessado no navegador.

Aqui foi aberta a porta `8080` do host para a porta `8080` do container. 

:::

Agora como temos o acesso ao `Adminer`. O uusário padrão da imagem do Postgres é `postgres` e a senha é `example`. Vamos acessar o Adminer e vamos preencher os campos de conexão com o banco de dados.

<img src={useBaseUrl("/img/docker-base/postgres-01.png")} alt="Utilizando baseUrl" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'24px' }} />

Agora vamos verificar se conseguimos acessar o banco de dados utilizando uma aplicação externa. Podemos utilizar o DBeaver para acessar o banco de dados. Vamos acessar o DBeaver e vamos criar uma nova conexão com o banco de dados.

:::danger[Atenção]

ESSA ETAPA É APENAS PARA FAZER UMA DEMONSTRAÇÃO! NÃO É NECESSÁRIO FAZER ISSO!

<img src="https://i.gifer.com/embedded/download/X2gn.gif" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom: '24px' }}/>

:::

Vamos obter o seguinte erro:

<img src={useBaseUrl("/img/docker-base/postgres-02.png")} alt="Utilizando baseUrl" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'24px' }} />

> Mas Murilo isso não faz sentido! O que aconteceu aqui? Nós estamos conectados com o banco de dados no Adminer, mas não conseguimos conectar com o banco de dados no DBeaver. O que aconteceu?

O que aconteceu foi que o banco de dados está sendo executado em um container. O banco de dados está sendo executado em um container e a porta `5432` do host não está mapeada para a porta `5432` do container. Para acessar o banco de dados no DBeaver, é necessário mapear a porta `5432` do host para a porta `5432` do container. Vamos fazer isso alterando o nosso arquivo `docker-compose.yml`.

```yml
# Use postgres/example user/password credentials
version: '3.9'

services:

  db:
    image: postgres
    restart: always
    # set shared memory limit when using docker-compose
    shm_size: 128mb
    # or set shared memory limit when deploy via swarm stack
    #volumes:
    #  - type: tmpfs
    #    target: /dev/shm
    #    tmpfs:
    #      size: 134217728 # 128*2^20 bytes = 128Mb
    ports:
      - "5432:5432"
    environment:
      POSTGRES_PASSWORD: example

  adminer:
    image: adminer
    restart: always
    ports:
      - 8080:8080
```

Vamos derrubar os containers e subir novamente.

```sh
docker-compose down
docker-compose up -d
```

Agora podemos ver o resultado da tentativa de conexão com o DBeaver:

<img src={useBaseUrl("/img/docker-base/postgres-03.png")} alt="Utilizando baseUrl" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'24px' }} />

Agora conseguimos acessar o banco de dados no DBeaver. O que aconteceu aqui foi que a porta `5432` do host foi mapeada para a porta `5432` do container. 

Pessoal até aqui avançamos bastante no desenvolvimento utilizando Docker. Vamos continuar estudando mais sobre Docker e containers, mas agora limitando os recursos disponíveis para nossa aplicação.

Primeiro vamos criar uma aplicação em Flask que conecta com nosso banco de dados Postgres. Nossa aplicação vai ser simples, ela vai enviar os dados que estamos recebendo para o banco e devolver todos os dados que estão no banco. Portanto ela possui apenas duas rotas.

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:example@db:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_USERNAME'] = 'postgres'
app.config['SQLALCHEMY_PASSWORD'] = 'example'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return '<User %r>' % self.name

@app.route('/users', methods=['POST'])
def create_user():
    name = request.json['name']
    user = User(name=name)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created'}), 201

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'name': user.name, 'created_at': user.created_at} for user in users]), 200

if __name__ == '__main__':
      app.app_context().push()
      db.create_all()
      app.run(host='0.0.0.0', port=5000, threaded=False)
```

Vamos primeiro compreender o que nossa aplicação está fazendo:

1. Estamos criando uma aplicação em Flask;
2. Estamos configurando a conexão com o banco de dados Postgres;
3. Configuramos a rota para conectar com o banco de dados e criar um usuário;
4. Configuramos o SQLAlchemy para não rastrear as modificações;
5. Estamos criando uma tabela `User` no banco de dados;
6. Estamos criando duas rotas: uma para criar um usuário e outra para listar todos os usuários;
7. Estamos criando um usuário no banco de dados quando a rota `POST /users` é acessada;
8. Estamos listando todos os usuários do banco de dados quando a rota `GET /users` é acessada.

Para nossa aplicação ser executada, é necessário instalar as dependências. Para instalar as dependências, é necessário criar um arquivo chamado `requirements.txt` com o seguinte conteúdo:

```txt
Flask==2.2
Werkzeug==2.2.2
Flask-SQLAlchemy==3.0.3
psycopg2-binary==2.9.1
```

Agora vamos criar um arquivo chamado `Dockerfile` com o seguinte conteúdo:

```Dockerfile
FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

Agora vamos construir o arquivo `docker-compose.yml` com o seguinte conteúdo:

```yml
version: '3.9'

services:

  db:
    image: postgres
    restart: always
    ports:
      - "5432:5432"
    environment:
      POSTGRES_PASSWORD: example

  app:
    build: .
    restart: always
    ports:
      - "5000:5000"
    depends_on:
      - db
```

Vamos agora iniciar o processo.

```sh
docker-compose up
```

Pessoal deixamos o console preso a aplicação para conseguirmos ver o que está acontecendo. Vamos utilizar o Insomnia para testar nossa aplicação. Vamos criar um novo usuário utilizando a rota `POST /users`. Podemos verificar o resultado da requisição e a inserção do usuário no banco de dados, verificando a rota `GET /users`.

:::danger[Atenção]

<img src="https://i.pinimg.com/originals/8b/30/e1/8b30e1297f11091203561dd1fe0ce5bb.gif" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom: '24px' }}/>

> Murilo, o que está acontecendo aqui?

Pessoal vamos analisar por partes, fizemos bastante coisa aqui e temos várias coisas acontecendo ao mesmo tempo.

1. Criamos uma aplicação em Flask que se conecta com o banco de dados Postgres;
2. Configuramos a conexão com o banco de dados Postgres;
3. Configuramos a rota para criar um usuário no banco de dados;
4. Configuramos a rota para listar todos os usuários do banco de dados;
5. Criamos um Dockerfile para construir a imagem da aplicação;
6. Criamos um arquivo `requirements.txt` com as dependências da aplicação;
7. Criamos um arquivo `docker-compose.yml` com as definições dos serviços `db` e `app`;
8. Criamos um serviço `db` que utiliza a imagem do Postgres e mapeia a porta `5432` do host para a porta `5432` do container;
9. Criamos um serviço `app` que constrói a imagem da aplicação e mapeia a porta `5000` do host para a porta `5000` do container;
10. O Docker Compose criou os containers `db` e `app` a partir das imagens do Postgres e da aplicação;
11. A aplicação foi executada no container `app`;
12. A aplicação foi acessada no pelo Insomnia;
13. Um usuário foi criado no banco de dados;
14. O usuário foi listado no banco de dados.

Nosso sistema neste momento está funcionando corretamente. Utilizando 2 containers, um para o banco de dados e outro para a aplicação. Vamos manter esse sistema ativo até o momento.

:::

Agora vamos estrangular nossa aplicação para ver o comportamento do sistema. Vamos limitar a quantidade de memória e cpu disponível para a aplicação. Vamos alterar o arquivo `docker-compose.yml` para limitar a quantidade de memória e cpu disponível para a aplicação.

```yml
version: '3.9'

services:

  db:
    image: postgres
    restart: always
    ports:
      - "5432:5432"
    environment:
      POSTGRES_PASSWORD: example
   resources:
      limits:
        # Segura que esse limite não está funcionando no nosso note
        #cpus: '0.5'
        memory: 128M

  app:
    build: .
    restart: always
    ports:
      - "5000:5000"
    depends_on:
      - db
    deploy:
      resources:
        limits:
          # Segura que esse limite não está funcionando no nosso note
          #cpus: '0.5'
          memory: 128M
```

Agora vamos reiniciar os containers.

```sh
docker-compose down
docker-compose up
```
