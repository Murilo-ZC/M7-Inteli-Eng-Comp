---
sidebar_position: 4
title: Implementações
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Implementações de Microsserviços

Pessoal até aqui tudo muito bom, tudo muito bonito, conseguimos discutir diversos pontos conceituais sobre a aplicação de microsserviços. Agora como implementamos?

<img src="https://media.tenor.com/Rc1GWDr71WIAAAAM/psyduck.gif" alt="Arquitetura Sincrona" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'16px' }} />

Pessoal vamos avaliar algumas formas de realizar essas implementações. Vale lembrar que existem diversas formas de implementar microsserviços, e a escolha da melhor abordagem depende do contexto e dos requisitos do projeto. 

### Hello World Microsserviços

Vamos criar três serviços e acessar eles através de um gateway.

:::danger[Novos Conceitos]

Pessoal vamos discultir diversos novos conceitos aqui. Fiquem tranquilos e vamos em conjunto avaliando eles.

<img src="https://i.pinimg.com/originals/08/5f/c9/085fc978dac75ac1a7146a78d9badd39.gif" alt="Arquitetura Sincrona" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'16px' }} />

:::

Vamos criar um diretório chamado `hello-world-microservices` e dentro dele vamos criar três diretórios: `service1`, `service2` e `service3`. Todo esse material estará no repositório do módulo.

```bash
mkdir hello-world-microservices
cd hello-world-microservices
mkdir service1
mkdir service2
mkdir service3
```

Para cada um dos serviços, vamos criar um arquivo Python para implementar um servidor HTTP simples que responde a uma solicitação GET com uma mensagem de "Olá, Mundo!" e o nome do serviço. Vamos utilizar o FastAPI para criar os servidores.

```python
# service1/server.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/service1")
async def read_root():
    return {"message": "Hello, World! from service1"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
```

O código será o mesmo para os outros serviços, apenas mudando o nome do serviço. Vale destacar que vamos utilizar o `uvicorn` para rodar os servidores. Por hora, vamos rodar cada um dos serviços em uma porta diferente, utilizando a porta `8001` para o `service1`, a porta `8002` para o `service2` e a porta `8003` para o `service3`.


Vamos ajustar o arquivo de `requirements.txt` para cada um dos serviços.

```bash
fastapi
uvicorn
```

:::tip[Cuidado com versões]
Vamos tomar cuidado com as versões das bibliotecas que estamos utilizando. Sempre é interessante deixar essas versões especificadas. Vamos alterar o arquivo `requirements.txt` para cada um dos serviços.
:::

Novo arquivo `requirements.txt` para o `service1` (depois da bronca).

```bash
fastapi==0.110.3
uvicorn==0.29.0
```

Agora, antes de rodarmos nossos serviços, vamos criar um dockerfile para cada um dos serviços.

```dockerfile
# service1/Dockerfile

FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "server.py"]
```

Agora vamos construir nossa imagem e rodar nosso container.

```bash
docker build -t service1 .
docker run -d -p 8001:8001 service1
```

Vamos ter o nosso serviço rodando e agora é possível acessar ele através do endereço `http://localhost:8001/service1`.

Vamos fazer o mesmo para os outros serviços.

:::warning[Sério Mesmo?]

Poxa Murilo vamos ter que fazer isso para todos os serviços? Não tem uma forma mais fácil?

:::

Ahhhh tem sim, vamos utilizar o `docker-compose` para facilitar nossa vida.

Vamos construir um arquivo `docker-compose.yml` na raiz do nosso projeto. A funcionalidade dele vai ser construir e rodar todos os nossos serviços.

```yaml
version: '3'

services:
  service1:
    build: ./service1
    ports:
      - "8001:8001"
  service2:
    build: ./service2
    ports:
      - "8002:8002"
  service3:
    build: ./service3
    ports:
      - "8003:8003"
```

O que está acontecendo neste `docker-compose` é que estamos construindo e rodando os nossos serviços. Vamos rodar o comando `docker-compose up` na raiz do nosso projeto.

```bash
docker-compose up
```

Legal agora todos os nossos serviços estão rodando e podemos acessar eles através dos endereços `http://localhost:8001/service1`, `http://localhost:8002/service2` e `http://localhost:8003/service3`.

### Gateway

Pessoal, vamos analisar uma coisa aqui. Nós temos três serviços rodando e cada um deles em uma porta diferente. Como podemos acessar todos esses serviços através de um único ponto de entrada?

> Murilo como assim? É só utilizar o endereço e a porta de cada um dos serviços.

Sim, você está correto, mas imagine que você tenha um serviço que chama outros serviços e você quer que ele seja o único ponto de entrada para acessar todos os outros serviços. Ainda temos outro problema aqui, quando a nossa quantidade de serviços aumentar vamos ter que ficar atualizando o nosso cliente para acessar os novos serviços. Isso não parece ser uma boa prática. Para resolver este tipo de problema, podemos utilizar um gateway.

:::tip[Gateway]

Pessoal sugiro fortemente a leitura do artigo: [O padrão de gateway de API versus a comunicação direta cliente-microsserviço](https://learn.microsoft.com/pt-pt/dotnet/architecture/microservices/architect-microservice-container-applications/direct-client-to-microservice-communication-versus-the-api-gateway-pattern).

Além dele, vamos utilizar essa referência de [API Gateway](https://microservices.io/patterns/apigateway.html).

<iframe width="560" height="315" src="https://www.youtube.com/embed/-IBZGS_UXhU?si=KwzQCCPPvWEW_dxB" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'24px' }}></iframe>

:::

Vamos realizar a implementação do nosso gateway. Vamos criar um novo diretório chamado `gateway` e dentro dele vamos copiar os arquivos `Dockerfile`, `server.py` e `requirements.txt` dos nossos serviços.

Agora vamos configurar nosso gateway. Para isso vamos utilizar o `Nginx` para fazer o roteamento das requisições para os nossos serviços.

:::tip[O que é o Nginx?]

O Nginx é um servidor web de código aberto que também pode ser usado como um proxy reverso, balanceador de carga, cache HTTP e muito mais. Ele é conhecido por sua alta performance, estabilidade, recursos ricos e baixo uso de recursos.

:::

Vamos construir o nosso `Dockerfile` para o gateway.

```dockerfile
# gateway/Dockerfile

FROM nginx:1.19.0

COPY nginx.conf /etc/nginx/nginx.conf
```

Repare que estamos fazendo levando o arquivo `nginx.conf` para o diretório `/etc/nginx/nginx.conf` do container. Dentro do arquivo `nginx.conf` vamos configurar o nosso gateway.

```nginx
# gateway/nginx.conf

worker_processes 1;

events { worker_connections 1024; }

http {
    sendfile on;

    upstream service1 {
        server service1:8001;
    }

    upstream service2 {
        server service2:8002;
    }

    upstream service3 {
        server service3:8003;
    }

    server {
        listen 80;

        location /service1 {
            proxy_pass http://service1;
        }

        location /service2 {
            proxy_pass http://service2;
        }

        location /service3 {
            proxy_pass http://service3;
        }
    }
}
```

Vamos compreender o que está acontecendo aqui:

- Estamos configurando o `Nginx` para escutar na porta `80`.
- Estamos configurando o `Nginx` para fazer o roteamento das requisições para os serviços `service1`, `service2` e `service3`.

Agora vamos construir a nossa imagem e rodar o nosso container.

```bash
docker build -t gateway .
docker run -d -p 8000:80 gateway
```

Agora podemos acessar todos os nossos serviços através do endereço `http://localhost:8000/service1`, `http://localhost:8000/service2` e `http://localhost:8000/service3`.

Vamos adicionar nosso serviço no nosso arquivo `docker-compose.yml`.

```yaml
version: '3'

services:
  service1:
    build: ./service1
    ports:
      - "8001:8001"
  service2:
    build: ./service2
    ports:
      - "8002:8002"
  service3:
    build: ./service3
    ports:
      - "8003:8003"
  gateway:
    build: ./gateway
    ports:
      - "8000:80"
```

Pessoal reparem no que aconteceu aqui. Nós temos um gateway que é o único ponto de entrada para acessar todos os nossos serviços. Isso é muito interessante, pois podemos adicionar novos serviços sem precisar atualizar o nosso cliente.

### Ponto de Discussão

Pessoal, vamos avaliar um ponto que vale a nossa atenção: considerando a abordagem e as definições que discultimos até aqui, se um microsserviço é uma entindade de software independente, como ficam os bancos de dados?

> Murilo, cada microsserviço tem o seu próprio banco de dados?

Essa resposta é mais complexa do que parece. Vamos avaliar algumas abordagens:

1. **Banco de Dados Compartilhado**: Todos os microsserviços compartilham o mesmo banco de dados. Isso pode simplificar a implementação, mas pode levar a problemas de escalabilidade e acoplamento.

2. **Banco de Dados por Microsserviço**: Cada microsserviço tem seu próprio banco de dados. Isso pode aumentar a complexidade, mas também pode melhorar a escalabilidade e a autonomia dos serviços.

3. **Banco de Dados por Domínio**: Os microsserviços são agrupados em domínios e cada domínio tem seu próprio banco de dados. Isso pode ser uma abordagem intermediária que combina os benefícios das duas abordagens anteriores.

4. **Banco de Dados por Tabela**: Cada microsserviço tem seu próprio esquema de banco de dados, mas compartilha o mesmo banco de dados físico. Isso pode ser uma abordagem eficiente em termos de recursos, mas pode levar a problemas de acoplamento e desempenho.

Aqui pessoal não existe uma resposta certa ou errada, a escolha da melhor abordagem depende do contexto e dos requisitos do projeto. 

:::tip[Referência]

Sugiro que vocês leiam esses dois artigos para entender melhor sobre o assunto:

- [Pattern: Database per service](https://microservices.io/patterns/data/database-per-service.html)
- [Database Design in a Microservices Architecture](https://www.baeldung.com/cs/microservices-db-design)

:::

### Sugestão de atividade

Até aqui, desenvolvemos diversos monolitos com nossas aplicações. Vamos realizar agora uma mudança nessa arquitetura e vamos implementar ela utilizando microsserviços.




