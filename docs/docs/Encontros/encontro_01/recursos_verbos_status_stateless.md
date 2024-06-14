---
sidebar_position: 2
title: Recursos, verbos, status code e stateless
---

## 1. Definições

O `REST` é uma sigla para `Representational State Transfer`. Trata-se de um estilo arquitetônico para sistemas distribuídos e é frequentemente usado para desenvolver serviços web. O conceito foi introduzido e definido em 2000 por Roy Fielding em sua tese de [doutorado](https://ics.uci.edu/~fielding/pubs/dissertation/fielding_dissertation.pdf).

REST não é um protocolo ou padrão, mas sim um conjunto de princípios arquitetônicos. Quando um serviço web é descrito como "RESTful", significa que ele adota esses princípios. 

### 1.1 Backend REST

Um Backend REST refere-se à parte do servidor em uma aplicação web ou sistema de software onde a lógica de negócios é processada. É o local onde as operações CRUD (Criar, Ler, Atualizar, Deletar) são executadas, dados são processados e mantidos, e onde se define a lógica de integração com outros serviços ou bancos de dados. Este back-end é acessado por meio de uma API RESTful que expõe interfaces específicas para as funções que o frontend ou outros clientes podem utilizar.

Em outras palavras, podemos dizer que um backend REST refere-se a toda a infraestrutura de servidor que implementa a lógica de negócios e manipulação de dados de uma aplicação. O back-end REST lida com a interação direta com o banco de dados, execução de lógica de negócios, autenticação de usuários, autorização de acessos, e também serve como a plataforma sobre a qual os serviços REST são construídos. O objetivo principal é garantir que as operações de dados sejam realizadas de forma segura, eficiente e de acordo com as regras de negócio.

### 1.2 Web Service REST

Um Web Service REST, por sua vez, é um serviço específico disponibilizado através de uma API web que adere aos princípios REST. Ele permite a comunicação e interação entre diferentes softwares na internet. Cada Web Service REST é projetado para realizar tarefas específicas e é acessado por meio de URLs. Usam verbos HTTP para indicar ações e podem retornar dados em vários formatos, como JSON ou XML.

É uma interface exposta pelo back-end que permite a interação e comunicação entre diferentes sistemas (ou entre cliente e servidor) através da web utilizando o protocolo HTTP. Este serviço define um conjunto de operações que podem ser realizadas (como obter dados, atualizar informações, etc.) e é acessível através de URIs específicas. Cada Web Service REST é projetado para executar tarefas bem definidas e é projetado para ser stateless (já vamos falar desse ponto), seguindo os princípios REST.

## 2. Diferenças

Podemos citar como diferenças entre um back-end REST e um Web Service REST:

### 2.1 Escopo

- `Backend REST`: Refere-se a toda a parte do servidor em um sistema que processa lógica, manipula dados, e se integra com outros serviços. Serve como a espinha dorsal de uma aplicação, gerenciando a lógica de negócios, persistência de dados, segurança, e manipulação de todas as operações de back-end necessárias para suportar as funcionalidades da aplicação.

- `Web Service REST`: É uma parte do back-end que é especificamente projetada para ser uma interface entre diferentes sistemas, permitindo-lhes interagir e funcionar juntos. Atua como um ponto de comunicação ou interface que expõe funcionalidades específicas do back-end para serem usadas por outros sistemas ou clientes, permitindo assim a interoperabilidade entre diferentes tecnologias ou domínios.

### 2.2 Uso

- `Backend REST`: Utilizado para desenvolver a lógica interna do sistema e garantir que os dados dos usuários sejam manipulados corretamente. Inclui o servidor de aplicação, o servidor de banco de dados, implementações de lógica de negócios, gerenciamento de sessão (apesar do stateless), e segurança (autenticação e autorização). 

<details> 
<summary mdxType="summary">Exemplo de Utilização</summary>

***Tecnologias Usadas:*** Python e Django.

***Banco de Dados:*** PostgreSQL.

***Funções Implementadas:***

- Autenticação de usuários.
- Manipulação de sessões de usuário (apesar do princípio stateless, o back-end pode usar sessões para outros propósitos internos que não afetam a comunicação REST).
- Operações CRUD para tarefas no banco de dados.
- Lógica para atribuição de tarefas a usuários.

</details>



- `Web Service REST`: Usado para permitir a integração e comunicação externa entre diferentes sistemas, tanto internos quanto externos. Compreende as APIs específicas que são expostas para acessar recursos do servidor, utilizando métodos HTTP (GET, POST, PUT, DELETE) para manipular esses recursos representados geralmente em formatos como JSON ou XML.

<details> 
<summary mdxType="summary">Exemplo de Utilização</summary>

Web Service REST:

Endpoint `/tasks`:
- GET: Retorna todas as tarefas do usuário autenticado.
- POST: Permite criar uma nova tarefa com os dados fornecidos no corpo da requisição.

Endpoint `/tasks/[task_id]`:
- GET: Retorna detalhes de uma tarefa específica.
- PUT: Atualiza a tarefa com os novos dados fornecidos.
- DELETE: Remove a tarefa especificada.

</details>

### 2.3 Fluxo de Comunicação

1. Cliente (Front-end) faz uma requisição HTTP para o Web Service REST.
2. Web Service REST interpreta a requisição, realiza autenticação e autorização usando os métodos definidos no back-end REST.
3. Backend REST executa as operações necessárias (e.g., buscar dados do banco, atualizar um registro).
4. Web Service REST retorna a resposta para o cliente, como um status HTTP e dados (se necessário) em formato JSON.

## 3. Recursos, Verbos, Status Code e Stateless

### 3.1 Recursos

Em REST, "recursos" são representações de uma entidade específica ou um conjunto de entidades que são acessíveis pela API. Por exemplo, em um aplicativo de blog, os recursos podem incluir artigos, autores e comentários, cada um acessível via URIs (Uniform Resource Identifiers).

### 3.2 Verbos

Os verbos HTTP são métodos usados para realizar ações nos recursos. Os principais incluem:

- **GET:** Recuperar dados do servidor (por exemplo, listar usuários).
- **POST:** Criar um novo recurso (por exemplo, adicionar um novo usuário).
- **PUT:** Atualizar um recurso existente.
- **DELETE:** Remover um recurso.
- **PATCH:** Atualizar parcialmente um recurso.

### 3.3 Status Codes

Os códigos de status HTTP fornecem informações sobre o resultado de uma requisição feita ao servidor. Os mais comuns em APIs REST são:

- **200 OK**: A requisição foi bem-sucedida.
- **201 Created**: Um novo recurso foi criado.
- **400 Bad Request**: A requisição não foi processada devido a erro do cliente.
- **404 Not Found**: O recurso solicitado não foi encontrado.
- **500 Internal Server Error**: Erro genérico quando o servidor falha.

Para ver todos os códigos de status HTTP, consulte a [documentação oficial](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status).

:::danger[Versão Pets]
- https://http.cat/
- https://httpstatusdogs.com/
:::

## 3.4 Stateless:

O princípio de ser stateless significa que cada requisição da API deve conter todas as informações necessárias para ser entendida e processada, sem que o servidor precise lembrar de estados anteriores. Isso simplifica a arquitetura do servidor e aumenta a escalabilidade, pois não é necessário manter um estado ou contexto entre as requisições.