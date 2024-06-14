---
sidebar_position: 6
title: Documentando de uma API REST - OPEN API e Swagger
---

# Documentando de uma API REST - OPEN API e Swagger

## O que é OpenAPI?

O Swagger é uma ferramenta de código aberto que ajuda os desenvolvedores a projetar, criar, documentar e consumir serviços da Web RESTful. Ele fornece uma interface gráfica que facilita a documentação de APIs RESTful. O Swagger é uma especificação de API para descrever APIs RESTful expressas usando JSON. O Swagger é usado junto com um conjunto de ferramentas de software de código aberto para projetar, construir, documentar e usar APIs RESTful.

Ele foi criado pela SmartBear Software em 2011 e foi adotado pela OpenAPI Initiative em 2015. O padrão OpenAPI é agnóstico de linguagem de programação e é suportado por várias ferramentas de software de código aberto, incluindo o Swagger. Diversas APIs documentadas com o Swagger são listadas no portal [SwaggerHub](https://app.swaggerhub.com/home).


<details>
    <summary>Tem vídeo?</summary>
    <iframe width="600" height="480" max-width="80vw" src="https://www.youtube.com/embed/3nl9AzttzBQ?si=UDuMd64vQn2u2wSI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style={{display: 'block', marginLeft: 'auto', maxHeight: '80vh', marginRight: 'auto', marginBottom: '16px'}}></iframe>

</details>

Uma grande vantagem do uso do Swagger é que ele permite criar a documentação antes mesmo de implementar a API. Isso é possível porque o Swagger é uma especificação de API que descreve a estrutura de uma API RESTful. A especificação é escrita em JSON ou YAML e é usada para descrever a estrutura de uma API RESTful. A especificação é usada para gerar a documentação da API, que é exibida em um formato legível por humanos. A documentação da API é usada para ajudar os desenvolvedores a entender como usar a API e para ajudar os consumidores da API a entender como a API funciona.

Para realizar a documentação da API, podemos utilizar o Swagger Editor, que é uma ferramenta de código aberto que permite escrever e visualizar a especificação da API em tempo real. O link para acessar o editor pode ser visto aqui: [Swagger Editor](https://editor.swagger.io/).

## Implementando o Swagger

Vamos primeiro implementar o seguinte código da API:

```yaml
openapi: 3.0.0
info:
  title: API de Gerenciamento de Usuários
  description: Esta é uma API simples para criar, consultar e deletar usuários.
  version: "1.0.0"
servers:
  - url: 'https://api.seusite.com'
    description: API de Produção

paths:
  /criar:
    post:
      summary: Cria um novo usuário
      operationId: criarUsuario
      tags:
        - Usuários
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - nome
                - email
              properties:
                nome:
                  type: string
                  example: João da Silva
                email:
                  type: string
                  example: joao.silva@example.com
      responses:
        '201':
          description: Usuário criado com sucesso
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                    example: '123'
        '400':
          description: Informação insuficiente para criar o usuário
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorModel'
        '405':
          description: Método não permitido
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorModel'

  /consultar/{id}:
    get:
      summary: Consulta um usuário pelo ID
      operationId: consultarUsuario
      tags:
        - Usuários
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Dados do usuário
          content:
            application/json:
              schema:
                type: object
                properties:
                  nome:
                    type: string
                    example: João da Silva
                  email:
                    type: string
                    example: joao.silva@example.com
        '404':
          description: Usuário não encontrado
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorModel'
        '405':
          description: Método não permitido
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorModel'

  /deletar/{id}:
    delete:
      summary: Deleta um usuário pelo ID
      operationId: deletarUsuario
      tags:
        - Usuários
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Usuário deletado com sucesso
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: string
                    example: 'ok'
        '404':
          description: Usuário não encontrado
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorModel'
        '405':
          description: Método não permitido
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorModel'

components:
  schemas:
    ErrorModel:
      type: object
      properties:
        mensagem:
          type: string
          example: 'Método não permitido'

```

Repare que desta forma, nós conseguimos criar a documentação e já estabelecer como nossa API vai se comportar, mesmo sem ter implementado ela. Isso é muito útil para que possamos ter uma visão geral de como utilizar a API para fazer integrações.

Para observar:

- Qual o grau de maturidade da API?
- Quais são os endpoints disponíveis?
- Quais são os métodos disponíveis?
