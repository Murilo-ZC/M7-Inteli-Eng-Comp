---
sidebar_position: 1
title: Arquitetura de Software
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Arquitetura de Software 

Podemos definir arquitetura de software como:

> Arquitetura de software refere-se ao conjunto de estruturas necessárias para racionalizar o desenvolvimento, a manutenção e a operação de um sistema de software. Ela envolve a definição de componentes de software, suas propriedades externas, e as relações entre eles.

Acho que é relevante verificarmos a definição de arquitetura de software, fornecida por [Martin Fowler](https://martinfowler.com), compartilhada por [Ralph Johnson](https://refactory.com/ralph-johnson/). Segundo ele, arquitetura de software é:

> "***Architecture is about the important stuff. Whatever that is***".

:::tip[Recomendação de leitura]

Recomendo a leitura do arquito de Martin Fowler sobre [Arquitetura de Software](https://martinfowler.com/architecture/).

:::

### Princípios de Arquitetura de Software

Aqui estão alguns princípios de arquitetura de software que você deve considerar ao projetar um sistema de software:

1. **Princípio da Responsabilidade Única (Single Responsibility Principle - SRP)**: Um módulo deve ter uma e apenas uma razão para mudar.

2. **Princípio Aberto/Fechado (Open/Closed Principle - OCP)**: Você deve ser capaz de estender um comportamento de uma classe sem modificá-lo.

3. **Princípio da Substituição de Liskov (Liskov Substitution Principle - LSP)**: As classes derivadas devem ser substituíveis por suas classes base.

4. **Princípio da Segregação de Interface (Interface Segregation Principle - ISP)**: Muitas interfaces específicas são melhores do que uma interface única.

5. **Princípio da Inversão de Dependência (Dependency Inversion Principle - DIP)**: Os módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de abstrações.

6. **Princípio da Convenção sobre Configuração (Convention Over Configuration)**: O desenvolvedor só precisa especificar aspectos da aplicação que não seguem a convenção.

7. **Princípio do Menor Conhecimento (Least Knowledge Principle - LKP)**: Um objeto deve conhecer o mínimo possível sobre outros objetos.

8. **Princípio do Encapsulamento**: Um objeto deve ser responsável por seu próprio estado e não deve permitir que outros objetos o modifiquem diretamente.

9. **Princípio do Acoplamento Fraco (Loose Coupling)**: Um objeto deve ser capaz de interagir com outro objeto sem saber muito sobre ele.

10. **Princípio da Coesão Forte (High Cohesion)**: Um objeto deve ter uma única responsabilidade.

Cada um destes princípios é importante para a arquitetura de software e deve ser considerado ao projetar um sistema de software. Muitas vezes não é possível seguir todos os princípios, mas é importante tentar seguir o máximo possível.

Outro fator importante é a escolha de um padrão de arquitetura de software. Existem vários padrões de arquitetura de software, como MVC, MVVM, MVP, entre outros. Cada padrão tem suas próprias vantagens e desvantagens, e a escolha de um padrão de arquitetura de software depende do sistema que você está desenvolvendo.

### Padrões de Arquitetura de Software

Aqui estão alguns padrões de arquitetura de software que você deve considerar ao projetar um sistema de software:

1. **Model-View-Controller (MVC)**: O padrão MVC é um padrão de arquitetura de software que divide um aplicativo em três componentes principais: Model, View e Controller.

2. **Model-View-ViewModel (MVVM)**: O padrão MVVM é um padrão de arquitetura de software que separa a lógica de apresentação da interface do usuário.

3. **Model-View-Presenter (MVP)**: O padrão MVP é um padrão de arquitetura de software que separa a lógica de apresentação da interface do usuário.

4. **Model-View-Adapter (MVA)**: O padrão MVA é um padrão de arquitetura de software que separa a lógica de apresentação da interface do usuário.

5. **Model-View-Service (MVS)**: O padrão MVS é um padrão de arquitetura de software que separa a lógica de apresentação da interface do usuário.

6. **Model-View-Interactor (MVI)**: O padrão MVI é um padrão de arquitetura de software que separa a lógica de apresentação da interface do usuário.

7. **Model-View-Intent (MVI)**: O padrão MVI é um padrão de arquitetura de software que separa a lógica de apresentação da interface do usuário.

8. **Model-View-Controller-Service (MVCS)**: O padrão MVCS é um padrão de arquitetura de software que separa a lógica de apresentação da interface do usuário.

9. **Model-View-Controller-Interactor (MVCI)**: O padrão MVCI é um padrão de arquitetura de software que separa a lógica de apresentação da interface do usuário.


Cada um destes padrões é importante para a arquitetura de software e deve ser considerado ao projetar um sistema de software. Muitas vezes não é possível seguir todos os padrões, mas é importante tentar seguir o máximo possível.

### Componentes de Arquitetura de Software

Os componentes são as estruturas básicas de um sistema de software. Eles são os blocos de construção do sistema e são responsáveis por realizar tarefas específicas. Aqui estão alguns componentes de arquitetura de software que você deve considerar ao projetar um sistema de software:


1. ***Componentes***: Os elementos básicos de uma arquitetura de software, como módulos, classes ou pacotes, que encapsulam um conjunto de funcionalidades relacionadas. Os componentes interagem entre si por meio de interfaces claramente definidas.

2. ***Conectores***: Mecanismos que facilitam a comunicação entre componentes. Incluem chamadas diretas de métodos, mensagens em filas, protocolos de rede e outros meios de interação entre os componentes.

3. ***Camadas***: Uma forma de organizar relacionamentos entre diferentes partes do sistema. Comum em muitas arquiteturas é a divisão em camada de apresentação, lógica de negócios e acesso a dados. Isso ajuda a separar responsabilidades e facilita a manutenção e escalabilidade.

4. ***Padrões de Arquitetura***: Modelos e práticas reconhecidos que são replicados para resolver problemas comuns de design de software, como MVC (Model-View-Controller), MVVM (Model-View-ViewModel) e Microservices.

5. ***Estilo Arquitetônico***: Define a estrutura geral do sistema. Estilos comuns incluem arquitetura em camadas, baseada em eventos, cliente-servidor e orientada a serviços (SOA).

6. ***Qualidade de Software***: Características que determinam o desempenho de um software, incluindo escalabilidade, confiabilidade, segurança e manutenabilidade. A arquitetura deve ser projetada de modo a otimizar essas qualidades.

7. ***Governança de Software***: Refere-se às políticas e práticas empregadas para garantir que a arquitetura do software cumpra os padrões e regulamentos necessários, mantendo a qualidade e a conformidade durante todo o ciclo de vida do desenvolvimento.

8. ***Gerenciamento de Dados***: Como os dados são armazenados, acessados e geridos dentro do sistema. Pode incluir a escolha de bancos de dados, estratégias de persistência de dados e políticas de backup.

9. ***Segurança***: Inclui as estratégias e ferramentas utilizadas para proteger o sistema de acessos não autorizados ou maliciosos. Elementos comuns incluem autenticação, autorização, criptografia e auditoria.

10. ***Integração e Middleware***: Componentes ou softwares que facilitam a integração e comunicação eficiente entre diferentes sistemas e aplicações. Middleware pode gerenciar e mediar a comunicação de dados entre diferentes processos e sistemas.

11. ***Adaptabilidade e Manutenibilidade***: A capacidade do sistema de se adaptar a mudanças de requisitos e o quão fácil é manter, corrigir e estender o sistema com o mínimo de esforço e custo.

12. ***Deploy e Provisionamento***: Métodos e processos utilizados para entregar o software ao ambiente de produção. Inclui automação de deploy, contêineres, e infraestrutura como código.


