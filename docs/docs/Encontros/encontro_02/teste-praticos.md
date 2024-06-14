---
sidebar_position: 5
title: Testes de Implementação
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Testes de Implementação

<!-- <img src="https://i.pinimg.com/originals/6f/f6/ec/6ff6ec2ae7b80e0ad31702464217de49.gif" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom: '24px' }}/> -->

Vamos agora fazer alguns testes práticos para verificar como podemos utilizar algumas bibliotecas e frameworks para testar comportamentos da nossa aplicação em uma aplicação síncrona e assíncrona.

:::tip[docker-compose]

<img src="https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/v1/attachments/delivery/asset/36eb05f369f0f8a30a5c7f7468790b41-1667993704/kerrholden/create-your-own-pokemon-gif.gif" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom: '24px' }}/>

Para todos os nossos testes, os ambientes de desenvolvimento e produção serão executados em containers Docker. Para isso, utilizaremos o arquivo `docker-compose.yml` que está disponível no repositório do projeto. Vou utilizar o mapeamento de volume para alterar nossos códigos fontes e testes sem a necessidade de recriar os containers.

:::

### Testes Síncronos

Primeiro vamos avaliar nosso sistema de forma síncrona. Para isso, vamos utilizar a seguinte arquitetura:

<img src={useBaseUrl("/img/arquiteturas/arquitetura-sinc-inicial.png")} alt="Arquitetura Sincrona" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'24px' }} />

Neste sistema, vamos iniciar a sua construção com o arquivo YAML que vai definir a estrutura do nosso sistema. Vamos criar um arquivo chamado `docker-compose.yml` na raiz do nosso projeto com o seguinte conteúdo:

Sugestão:

```yaml
# Use postgres/example user/password credentials
version: '3.9'

services:
  api:
    image: python:3.9
    working_dir: /app
    volumes:
      - pip39:/usr/local/lib/python3.9/site-packages
      - .:/app
    ports:
      - "5005:5000"
    command: python app.py
    restart: on-failure
    deploy:
      resources:
        limits:
          memory: 256M
    depends_on:
      - requirements

  requirements:
    image: python:3.9-slim-buster
    working_dir: /app
    volumes:
      - pip39:/usr/local/lib/python3.9/site-packages
      - .:/app
    command: pip install -r requirements.txt


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
    deploy:
      resources:
        limits:
          memory: 256M

  adminer:
    image: adminer
    restart: always
    ports:
      - 8080:8080
    deploy:
      resources:
        limits:
          memory: 256M

volumes:
  pip39:

```