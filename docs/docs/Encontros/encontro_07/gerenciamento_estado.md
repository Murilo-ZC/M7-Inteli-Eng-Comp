---
sidebar_position: 4
title: Gerenciamento de Estado 
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Definição de Estado em uma aplicação

Antes de iniciarmos a discussão sobre gerenciamento de estado, é importante entendermos o que é estado em uma aplicação. O estado de uma aplicação é a representação de todos os dados que a aplicação precisa para funcionar. Esses dados podem ser informações de usuário, configurações, dados de um formulário, etc.

De forma geral, o estado de uma aplicação é composto por:

- **Estado Local**: Dados que são utilizados apenas em um componente específico.

- **Estado Aplicação**: Dados que são utilizados por toda a aplicação.

O estado é importante para que a aplicação possa reagir a eventos e interações do usuário, como cliques, digitação, etc. Por exemplo, ao clicar em um botão, a aplicação pode alterar o estado para exibir uma mensagem de sucesso.

Até aqui, refletimos a mudança de estado da aplicação utilizando a função `setState` do Flutter. No entanto, conforme a aplicação cresce, o gerenciamento de estado pode se tornar complexo e difícil de manter. Para resolver esse problema, existem diversas bibliotecas e padrões que auxiliam no gerenciamento de estado.

A figura abaixo ilustra o problema de gerenciamento de estado em uma aplicação. Reparem que a figura ilustra um problema de gerenciamento de estado em uma aplicação que possui diversos componentes que compartilham o mesmo estado. Nela, as cores são adicionadas ao estado e compartilhadas entre os componentes.

<img src="https://docs.flutter.dev/assets/images/docs/development/data-and-backend/state-mgmt/state-management-explainer.gif" style={{ display: 'block', marginLeft: 'auto', maxHeight: '50vh', marginRight: 'auto', marginBottom: '24px' }}/>


## Padrão do Flutter para Gerenciamento de Estado

Seguindo a documentação oficial do [Flutter](https://docs.flutter.dev/data-and-backend/state-mgmt/intro), temos algumas sugestões para a construção de nossas aplicações.

A primeira delas é que devemos conhecer a diferença entre o estado local (local state) e o estado global (app state). O estado local é o estado que é utilizado apenas em um componente específico, enquanto o estado global é o estado que é utilizado por toda a aplicação. 

O estado local diz respeito do estado de um ***widget*** apenas. Ele pode ser resolvido utilizando um `StatefulWidget` e o método `setState`. Já o estado global é o estado que é compartilhado entre diversos ***widgets***. Para resolver esse problema, o Flutter sugere o uso de alguma técnica que possibilite a comunicação entre os ***widgets***.

A figura abaixo traz uma ilustração que nos permite diferenciar de qual tipo de estado estamos analisando. Repare que a fonte inicial é o dado. A sua disponibilização é que vai determinar se o estado é local ou global

<img src="https://docs.flutter.dev/assets/images/docs/development/data-and-backend/state-mgmt/ephemeral-vs-app-state.png" style={{ display: 'block', marginLeft: 'auto', maxHeight: '50vh', marginRight: 'auto', marginBottom: '24px' }}/>


Por padrão, o Flutter sugere que utilizemos o `Provider` para gerenciar o estado da aplicação. O `Provider` é uma biblioteca que permite a injeção de dependências e o gerenciamento de estado de forma simples e eficiente. Contudo, o `Provider` não é a única opção para gerenciar o estado de uma aplicação. Outras opções são o `Bloc`, `Riverpod`, `GetX`, `MobX`, entre outros.

Vamos, ao longo do módulo, estudar alguns dos gerenciadores de estado disponíveis para o Flutter. Contudo, é importante que vocês saibam que a escolha do gerenciador de estado depende do contexto da aplicação e do conhecimento da equipe de desenvolvimento.

Para nosso estudo inicial, vamos utilizar o `MobX` para gerenciar o estado da aplicação. O `MobX` é uma biblioteca que permite a criação de observáveis e reações de forma simples e eficiente. A documentação do `MobX` pode ser encontrada [aqui](https://pub.dev/packages/mobx).

## Considerações Finais

Vamos realizar agora a implementação do `MobX` em nossa aplicação. Para isso, vamos construir uma aplicação que simula um sistema de vendas. Vamos exibir algumas listas para o usuário e ele vai adicionar os elementos destas listas em um carrinho de compras. Nossa aplicação vai exibir o total da compra e a quantidade de itens no carrinho. Esse carrinho poderá ser limpo a qualquer momento.

Vamos realizar essa implementação utilizando o `MobX` e o padrão `MVC`. Vamos lá?

:::warning[Implementem!!]

Pessoal, a próxima implementação é um tanto quando mais trabalhosa. Contudo, é importante que vocês implementem para fixar o conteúdo. A prática é fundamental para a evolução de vocês como pessoas desenvolvedoras, engenheiras e arquitetas de solução.

Minha singela sugestão é que vocês façam uma avaliação sobre a atividade e o seu momento de estudo. Se você considerou muito simples a implementação apresentada, tente modificar a ferramenta de gerenciamento de estado. Se você considerou média a dificuldade de implementação pelo acompanhamento que vem fazendo dela, primeiro faça a implementação como fizemos e depois comece a modificar as funcionalidades implementadas. Se você achou muito difícil mesmo fazer essa implementação, sugiro você dar uma olhada nas versões anteriores de código que implementamos. Tente fazer pequenas modificações. Quebre propositalmente o funcionamento do código e tente fazer ele voltar a funcionar. 

De novo, a prática vai fazer vocês conseguirem evoluir. Então, mãos à obra!

:::