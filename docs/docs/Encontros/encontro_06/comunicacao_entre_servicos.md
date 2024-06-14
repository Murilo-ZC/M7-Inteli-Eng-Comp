---
sidebar_position: 3
title: Comunicação Entre Serviços
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Comunicação Entre Serviços

A comunicação entre serviços é um dos principais desafios no desenvolvimento de arquiteturas de software distribuídas. Existem várias formas de implementar a comunicação entre serviços, cada uma com suas vantagens e desvantagens.  Vamos avaliar algumas delas.

<img src="https://dz2cdn1.dzone.com/storage/temp/7542942-screen-shot-2017-12-14-at-42543-pm.png" style={{ display: 'block', marginLeft: 'auto', maxHeight: '65vh', marginRight: 'auto', marginBottom: '24px' }}/>


### Comunicação Síncrona

A comunicação síncrona é o tipo mais comum de comunicação entre serviços. Nesse modelo, um serviço faz uma chamada a outro serviço e aguarda a resposta antes de continuar a execução. Isso é útil quando o serviço depende da resposta do outro para continuar a execução.

Para implementar a comunicação síncrona, podemos utilizar protocolos como HTTP, gRPC, ou WebSockets. Vamos avaliar cada um deles.

#### HTTP

O protocolo HTTP é amplamente utilizado para comunicação entre serviços. Ele é simples, flexível e suportado por praticamente todas as linguagens de programação e plataformas. No entanto, o HTTP é baseado em texto e pode ser lento para comunicações de alta performance.

É comum utilizar o HTTP para implementar APIs RESTful, que são endpoints que respondem a requisições HTTP com dados em formato JSON ou XML. APIs RESTful são fáceis de implementar e entender, mas podem ser limitadas em termos de desempenho e flexibilidade.

<img src="https://learn.microsoft.com/pt-br/dotnet/architecture/microservices/architect-microservice-container-applications/media/communication-in-microservice-architecture/request-response-comms-live-queries-updates.png" style={{ display: 'block', marginLeft: 'auto', maxHeight: '65vh', marginRight: 'auto', marginBottom: '24px' }}/>

Como principais vantagens do HTTP, temos:

- **Simplicidade**: O HTTP é fácil de entender e implementar.
- **Flexibilidade**: O HTTP suporta vários métodos de requisição, como GET, POST, PUT e DELETE.
- **Suporte**: O HTTP é suportado por praticamente todas as linguagens de programação e plataformas.

Como desvantagens do HTTP, temos:

- **Desempenho**: O HTTP pode ser lento para comunicações de alta performance.
- **Latência**: APIs RESTful podem trazer latência aos serviços.

#### gRPC - Google Remote Procedure Call

O gRPC é um framework de comunicação de alto desempenho desenvolvido pelo Google. Ele utiliza o protocolo HTTP/2 para comunicação entre serviços e suporta vários tipos de dados, como JSON, Protocol Buffers e gRPC-Web.

O gRPC é baseado em chamadas de procedimento remoto (RPC), onde um serviço faz uma chamada a outro serviço e aguarda a resposta. O gRPC suporta streaming bidirecional, o que permite que os serviços enviem e recebam dados de forma assíncrona.

<img src="https://miro.medium.com/max/1400/1*HRO6F1VnuK_3YOo_oPgxvg.png" style={{ display: 'block', marginLeft: 'auto', maxHeight: '65vh', marginRight: 'auto', marginBottom: '24px' }}/>

---

### Comunicação Assíncrona

A comunicação assíncrona é um modelo de comunicação onde um serviço envia uma mensagem a outro serviço e não aguarda a resposta imediata. Isso é útil quando o serviço não depende da resposta do outro para continuar a execução.

Em geral, a comunicação assíncrona é mais eficiente e escalável do que a comunicação síncrona, pois permite que os serviços continuem a execução sem aguardar a resposta do outro serviço.

Sua implementação pode ser feita utilizando sistemas de mensageria, como RabbitMQ, Kafka, ou Amazon SQS. Vamos avaliar a implementação do RabbitMQ.

<img src="https://miro.medium.com/v2/resize:fit:1400/1*0C3Fdogb7BNuoCZ0sId7Yg.png" style={{ display: 'block', marginLeft: 'auto', maxHeight: '65vh', marginRight: 'auto', marginBottom: '24px' }}/>

