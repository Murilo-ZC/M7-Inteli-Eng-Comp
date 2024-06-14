---
sidebar_position: 7
title: Atividade Ponderada
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Atividade Ponderada - Construção de Aplicativo Híbrido com Flutter

Atividade Ponderada que consiste em construir uma aplicação Flutter. Essa aplicação deve ser realizada em sala de aula seguindo as orientações da Instrução. A entrega da atividade deve acontecer pelo Github. A aplicação deve ser desenvolvida utilizando o backend fornecido em sala de aula. O protocolo para comunicação com o backend também será disponibilizado durante a instrução.

O backend para está atividade deve, OBRIGATORIAMENTE, ser desenvolvido em Microsserviços. A aplicação deve ser desenvolvida utilizando o Flutter. Minha sugestão é que o backend seja desenvolvido em Python.

A aplicação deve estar conteinerizada e deve ser entregue com o Dockerfile e o docker-compose.yml. O repositório da aplicação deve ser entregue com o README.md contendo as instruções para execução da aplicação.

### Barema de Correção

Como barema de correção da atividade, serão considerados os seguintes aspectos:

| Faixa de Nota   | Conceito | Descrição  |
|:----------:|:----------|-------:|
| 0 - 2      | Não Iníciou        | O desenvolvimento do projeto não foi totalmente iniciado. Ele se resumiu a utilizar os templates iniciais. Não existe nenhuma integração entre as partes do sistema|
| 2.1 - 4    | Entrega Incompleta          | As aplicações, aplicativo e backend foram iniciadas. Elas não estão integradas. A aplicação mobile não segue nenhum padrão dos abordados nos encontros. A aplicação do backend não foi implementada utilizando microsserviços e/ou não está containerizada.|
| 4.1 - 6   | Atende Parcialmente          | O aplicativo foi desenvolvido e está parcialmente integrado com o backend. O backend foi desenvolvido utilizando uma arquitetura monolítica e não está com todas as suas funcionalidades desenvolvidas. A integração não foi totalmente realizada.|
| 6.1 - 9   | Atendeu os requisitos          | O aplicativo foi desenvolvido e está integrado com o backend. O backend foi desenvolvido utilizando uma arquitetura de microsserviços e está com todas as suas funcionalidades desenvolvidas. A integração foi totalmente realizada. |
| 9.1 - 10   | Supera os requisitos apresentados          |  aplicativo foi desenvolvido e está integrado com o backend. O backend foi desenvolvido utilizando uma arquitetura de microsserviços e está com todas as suas funcionalidades desenvolvidas. A integração foi totalmente realizada. O aplicativo foi construído utilizando as práticas de desenvolvimento de software apresentadas em aula e outras práticas de mercado. O backend foi construido e documentado para que mais funcionalidades possam ser adicionadas nele sem grandes complicações. |

---

- Checkpoint: Domingo (19/05/2024 - 23h59)
  - Aplicativo Flutter com tela de login (sem autenticação de rotas, necessáriamente), cadastro de usuário e tela para captura de imagens.
  - Backend em Microsserviços que realiza o cadastro de usuários e faz o log das ações que o usuário realiza no aplicativo (por hora só login e criação de conta).

- Entrega: Domingo (26/05/2024 - 23h59)
  - Aplicativo Flutter enviando as imagens para o processamento;
  - Backend em Microsserviços que recebe as imagens e as processa, retornando o resultado para o aplicativo;
  - Backend em Microsserviços que realiza o log das ações que o usuário realiza no aplicativo (por hora só login, criação de conta e envio de imagens);
  - Serviço de notificação que envia uma notificação para o usuário quando o processamento da imagem termina.