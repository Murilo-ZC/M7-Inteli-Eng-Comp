# Instruções Gerais para o Encontro:

Ao longo deste encontro, vamos utilizar um conjunto de containers para apresentar nosso banco de dados Postgres.
Primeiro, executar o arquivo docker-compose:

```yaml
# Use postgres/example user/password credentials
version: '3.1'

services:

  db:
    image: postgres
    restart: always
    environment:
      POSTGRES_PASSWORD: senha
      POSTGRES_USER: postgres
      POSTGRES_DB: postgres
    ports:
      - 5432:5432

  adminer:
    image: adminer
    restart: always
    ports:
      - 8080:8080
    depends_on:
      - db
```

Para iniciar o conjunto de container (pela primeira vez), utilizar o comando:

```bash
docker-compose up
```

Isso vai lançar os containers do Postgres e do Adminer. Para acessar o Adminer, no navegador, ir para url: http://localhost:8080.

<p align="center">
  <img src="./static/adminer.png" width="100%" height="auto" title="Tela de Login Inicial do Adminer">
</p>

