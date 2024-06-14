---
sidebar_position: 3
title: Maturidade de Richardson
---

## 1.Modelo de Maturidade de Richardson

O Modelo de Maturidade de Richardson é uma ferramenta útil para avaliar a conformidade de uma API com os princípios REST. Desenvolvido por Leonard Richardson, este modelo decompõe os elementos cruciais que definem uma API RESTful em quatro níveis de maturidade. Cada nível adiciona novos elementos sobre os anteriores, aumentando a aderência aos princípios REST. A ideia é que, ao seguir este modelo, desenvolvedores possam criar serviços web mais robustos, escaláveis e flexíveis.

## 2.Níveis do Modelo

### 2.1.Nível 0: POX (Plain Old XML)

O HTTP é utilizado apenas como meio de transporte. Neste nível, a API é basicamente apenas um mecanismo remoto de chamada de procedimento (RPC). Ou seja, não aproveita as características inerentes do protocolo HTTP além de simplesmente enviar e receber dados.

As mensagens são enviadas por XML ou qualquer outro formato, mas não usa recursos HTTP como HTTP verbs ou HTTP status codes. Em geral, todas as operações são realizadas geralmente via POST, sem diferenciar o tipo de ação realizada sobre o recurso.

A API neste nível geralmente expõe apenas um único URI que recebe todas as requisições, que são diferenciadas pelo corpo da requisição.

:::info[Qual a relevância?]

- `Facilidade de Implementação:` Muito fácil de implementar, especialmente para sistemas legados ou quando integrado a sistemas que não são baseados em web.

- `Principais Limitações:` Falta de escalabilidade, flexibilidade e dificuldades na manutenção, pois não utiliza a plena capacidade do HTTP.

:::

### 2.2.Nível 1: Recursos

No nível 1, o sistema começa a definir recursos com URIs dedicadas. Por exemplo, separando `/clientes` para acessos relacionados a clientes e `/pedidos` para pedidos. 

Geralmente, ainda usa POST para todas as operações, não diferenciando entre tipos de ação (criar, ler, atualizar, deletar). Por exemplo: 
- POST /clientes para criar um novo cliente; 
- POST /clientes/123 para atualizar o cliente com ID 123.

:::info[Qual a relevância?]

- `Organização Melhorada:` Facilita a organização da API e a compreensão dos tipos de entidades que a API manipula, melhorando um pouco a manutenibilidade.

- `Ainda Não É RESTful:` Não aproveita o protocolo HTTP para representar operações CRUD através de verbos como GET, PUT, e DELETE.

:::

### 2.3.Nível 2: Verbos HTTP

Este nível utiliza os verbos HTTP (GET, POST, PUT, DELETE) para definir ações sobre os recursos, alinhando melhor com os princípios REST. Em geral temos como operações padrão:
- `GET` para recuperar recursos.
- `POST` para criar novos recursos.
- `PUT` para atualizar recursos existentes.
- `DELETE` para remover recursos.

Como exemplo: 
- `GET /clientes/123` para obter informações do cliente 123;
- `DELETE /clientes/123` para deletar esse cliente.

Este nível também utiliza códigos de status HTTP para comunicar o resultado das operações ao cliente, como 200 OK, 201 Created, e 404 Not Found.


:::info[Qual a relevância?]

- `Aproveitamento do HTTP:` Utiliza o protocolo HTTP como foi destinado, o que facilita a interoperabilidade e a integração com outras interfaces web e clientes HTTP.

- `Melhor Feedback para o Cliente:` Os códigos de status informam os clientes sobre o sucesso ou falha das operações, permitindo reações apropriadas do lado do cliente.

:::

### 2.4.Nível 3: HATEOAS (Hypermedia as the Engine of Application State)

O último nível adiciona controles de hypermedia, que incluem links dentro das respostas que orientam o cliente sobre as ações possíveis subsequentes.

As respostas são auto-descritivas, com links para métodos relacionados (por exemplo, link para deletar um cliente na representação de um cliente). A aplicação do cliente muda de estado exclusivamente através das hyperlinks fornecidos dinamicamente pela aplicação do servidor.

Por exemplo, uma resposta para `GET /clientes/123` poderia incluir links para `PUT /clientes/123` e `DELETE /clientes/123`, e talvez links para recursos relacionados como `/clientes/123/pedidos`.

:::info[Qual a relevância?]

- `Descoberta Dinâmica:` Permite que os clientes da API descubram dinamicamente outras funcionalidades da API, reduzindo o acoplamento entre cliente e servidor e melhorando a escalabilidade e a flexibilidade da aplicação.

- `Verdadeiramente RESTful:` Alcançar este nível significa que a API é totalmente RESTful, aproveitando todos os benefícios do protocolo HTTP e seguindo os princípios de design REST de maneira completa.

:::

Sugestão de Material Complementar (créditos ao [rmnicola](https://github.com/rmnicola) por ter sugerido o vídeo):

<iframe width="600" height="480" max-width="80vw" src="https://www.youtube.com/embed/x7v6SNIgJpE?si=whTCgt28o5i5nqdY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style={{display: 'block', marginLeft: 'auto', maxHeight: '80vh', marginRight: 'auto', marginBottom: '16px'}}></iframe>

## 3. Considerações sobre o uso do Modelo

Este modelo não só ajuda a construir APIs que verdadeiramente aproveitam a arquitetura da Web mas também promove práticas que podem aumentar a flexibilidade, escalabilidade e a manutenibilidade da aplicação. APIs que alcançam o Nível 3 são consideradas verdadeiramente RESTful, pois utilizam a web (com seus hyperlinks e métodos HTTP) como plataforma de desenvolvimento de aplicações.

Ao projetar APIs RESTful, atingir o Nível 3 do Modelo de Maturidade de Richardson significa que a API está bem equipada para evoluir. Links e ações sugeridas nas respostas permitem que o cliente de API descubra dinamicamente outras ações possíveis, reduzindo o acoplamento entre cliente e servidor e facilitando mudanças e expansões futuras.

A aplicação desses princípios ajuda a garantir que a API pode ser usada de maneira intuitiva e eficaz, aproveitando plenamente os protocolos web existentes e a infraestrutura de internet. Em resumo, o Modelo de Maturidade de Richardson fornece um caminho claro para a evolução técnica das APIs.

Contudo, cabe destacar que o Modelo de Maturidade de Richardson é uma ferramenta útil para avaliar o quão bem uma API segue os princípios REST. No entanto, é importante lembrar que a aderência estrita a todos os níveis do modelo pode não ser necessária ou prática em todos os casos. A aplicação do modelo deve ser feita de forma consciente, considerando as necessidades e restrições específicas de cada projeto.