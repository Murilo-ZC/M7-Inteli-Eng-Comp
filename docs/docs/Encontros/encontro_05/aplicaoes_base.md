---
sidebar_position: 3
title: Aplicações que Serão Testadas
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Aplicações que Serão Testadas

Nesta seção pessoal, vamos avaliar as aplicações que serão testadas durante nosso estudo sobre os testes de carga. Elas são aplicações construídas com alguns frameworks de Python e todas estão dockerizadas  🐳.

Peço que vocês dediquem uma quantidade de tempo para verificar como elas foram desenvolvidas e quais são as diferenças entre elas. Todos os códigos fonte estão disponíveis no [repositório do GitHub](https://github.com/Murilo-ZC/M10-Inteli-Eng-Comp/tree/main/src/encontro05).

### Aplicações

Aqui temos um breve descritivo de cada uma das aplicações que serão testadas.

#### Aplicação 1 - Flask com SQLite

Essa aplicação foi construída com o framework Flask e utiliza o banco de dados SQLite. Ela é uma aplicação simples que permite a criação de usuários e a listagem de todos os usuários cadastrados.

O CRUD foi implementado utilizando a biblioteca `sqlite3` do Python e comandos SQL. A aplicação foi dockerizada e está pronta para ser executada. O link para ela pode ser visto [aqui](https://github.com/Murilo-ZC/M10-Inteli-Eng-Comp/tree/main/src/encontro05/aplicacao01).

Um ponto importante para se observar, essa implementação foi deployada com o servidor built-in do Flask, o que não é recomendado para ambientes de produção.

#### Aplicação 2 - Flask com SQLite e Servidor Gunicorn

Está aplicação é igual a anterior, mas utilizando o servidor Gunicorn para servir a aplicação. O Gunicorn é um servidor HTTP WSGI para Python que é amplamente utilizado para servir aplicações web Python em produção.

:::tip[WSGI]

A Interface Gateway de Servidor Web (WSGI) é uma especificação para a comunicação entre servidores web e aplicações web Python. Ela define um contrato entre servidores web e aplicações web Python, permitindo que diferentes servidores web e aplicações web Python se comuniquem de forma eficiente.

Para saber mais sobre o WSGI, acesse a [documentação oficial](https://www.python.org/dev/peps/pep-3333/).
E para saber mais sobre o Gunicorn, acesse a [documentação oficial](https://gunicorn.org/) e sua implementação com o [Flask](https://flask.palletsprojects.com/en/3.0.x/deploying/gunicorn/).
:::

Você pode acessar o código fonte [aqui](https://github.com/Murilo-ZC/M10-Inteli-Eng-Comp/tree/main/src/encontro05/aplicacao02).

#### Aplicação 3 - FastAPI com SQLite

Agora pessoal, vamos para uma aplicação construída com o framework FastAPI. O FastAPI é um framework moderno e rápido para construir APIs web com Python 3.6+ baseado em anotações de tipo.

Vamos utilizar a mesma base de código da aplicação 1, mas agora com o FastAPI. O link para o código fonte pode ser acessado [aqui](https://github.com/Murilo-ZC/M10-Inteli-Eng-Comp/tree/main/src/encontro05/aplicacao03).

:::tip[Uvicorn vs Gunicorn]

O Uvicorn é um servidor ASGI que é amplamente utilizado para servir aplicações web Python em produção. Ele é o servidor recomendado para servir aplicações FastAPI. Já o Gunicorn é um servidor WSGI que é amplamente utilizado para servir aplicações web Python em produção. Ele é o servidor recomendado para servir aplicações Flask.

:::

:::tip[ASGI]

A Interface Gateway de Servidor Assíncrono (ASGI) é uma especificação para a comunicação entre servidores web e aplicativos web Python assíncronos. Ela define um contrato entre servidores web e aplicativos web Python assíncronos, permitindo que diferentes servidores web e aplicativos web Python assíncronos se comuniquem de forma eficiente.

Para saber mais sobre o ASGI, acesse a [documentação oficial](https://asgi.readthedocs.io/en/latest/).
E para saber mais sobre o Uvicorn, acesse a [documentação oficial](https://www.uvicorn.org/).

:::

## Considerações 

Pessoal ainda podemos criar diferentes aplicações para testar. Essas são apenas algumas aplicações base que utilizam diferentes frameworks de Python.

:::danger[IMPORTANTE]

Pessoal, repare que, mesmo com frameworks diferentes, as aplicações tem as demais características iguais. Isso é proposital para que possamos avaliar o desempenho de cada framework. Quando iniciarmos as trocas de pontos das tecnologias, devemos lembrar que elas podem impactar na performance da aplicação.

Se estamos comparando apenas os frameworks, devemos manter as demais características iguais.

:::