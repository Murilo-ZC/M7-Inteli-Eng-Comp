# Descrição das ferramentas utilizadas no Encontro:

Ao longo do encontro, vamos utilizar um conjunto de ferramentas em Python e com alguns containers padronizados. Para a plena utilização destas ferramentas, segue uma descrição de como iniciar cada uma delas.

## Container do Banco de Dados Postgres

Como nosso armazenamento de dados, vamos utilizar um banco de dados Postgres.
Dentro do diretório `database` está o arquivo fonte para a construção da imagem do banco de dados.

```Dockerfile
FROM postgres:latest
ENV POSTGRES_PASSWORD=yourpassword
ENV POSTGRES_USER=postgres
ENV POSTGRES_DB=postgres
```

Este `Dockerfile` vai configurar a imagem padrão do [Postgres](https://hub.docker.com/_/postgres) para funcionar com o usuário `postgres`, com a senha `yourpassword` e com o banco de dados `postgres`. 

Para compilar a imagem, utilizar a seguinte sequencia de comandos:

```bash
# Entrando no diretório do Dockerfile
cd database
# Criando a imagem
docker build -t banco-db-img .
# Executando a imagem e conectando nela
docker run --name banco-db -p 5432:5432 -d banco-db-img
```

Para verificar se o container está funcionando, conectar nele como DBeaver ou outra ferramenta de manipulação de SGBD.