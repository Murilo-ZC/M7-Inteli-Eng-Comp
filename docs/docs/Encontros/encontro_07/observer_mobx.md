---
sidebar_position: 5
title: Padrão Observer e MobX 
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Introdução ao Conceito de Observabilidade

Observabilidade é um conceito multifacetado na computação. Em sua essência, observabilidade é a capacidade de observar ou monitorar o estado interno de um sistema. Em sistemas de software, a observabilidade é a capacidade de observar o estado interno de um sistema em execução. A observabilidade é uma propriedade de um sistema que permite que seus estados internos sejam observados e compreendidos de forma clara e precisa.

Pessoal sugiro fortemente a leitura do capítulo 1 do livro [Observability Engineering](https://www.oreilly.com/library/view/observability-engineering/9781492076438/ch01.html) para entender melhor o conceito de observabilidade. 

## Padrão Observer

Implementar a observabilidade em um sistema é uma tarefa que já foi demandada por muitos desenvolvedores. Toda vez que temos uma tarefa sendo implementada diversas vezes, é sinal de que talvez tenhamos um padrão de projeto. O padrão Observer é um padrão de projeto de software que define uma dependência um-para-muitos entre objetos, de modo que quando um objeto muda de estado, todos os seus dependentes são notificados e atualizados automaticamente.

O padrão Observer é um dos padrões de projeto mais utilizados no desenvolvimento de software. Ele é utilizado para implementar a comunicação entre objetos em um sistema. O padrão Observer é composto por três elementos principais: o sujeito, o observador e a notificação. O sujeito é o objeto que é observado. O observador é o objeto que observa o sujeito. A notificação é o mecanismo que o sujeito utiliza para notificar os observadores de que houve uma mudança de estado.

Vamos verificar duas referências aqui sobre o padrão Observer:

<iframe style={{ display: 'block', marginLeft: 'auto', marginRight: 'auto', width: '40vw', height: '23vh', marginBottom: '24px' }} src="https://www.youtube.com/embed/-oLDJ2dbadA?si=PMWBtLRZYc0SfLOw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<iframe style={{ display: 'block', marginLeft: 'auto', marginRight: 'auto', width: '40vw', height: '23vh', marginBottom: '24px' }} src="https://www.youtube.com/embed/REqVImw8Wgo?si=EdWIjx7bIXddPyHt" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<iframe style={{ display: 'block', marginLeft: 'auto', marginRight: 'auto', width: '40vw', height: '23vh', marginBottom: '24px' }} src="https://www.youtube.com/embed/ioYkXh8NhKc?si=1yAmDTQEAlWcvmax" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<details> 
        <summary mdxType="summary"> Se quiser estudar mais padrões de projeto?</summary>

        <iframe style={{ display: 'block', marginLeft: 'auto', marginRight: 'auto', width: '40vw', height: '23vh', marginBottom: '24px' }} src="https://www.youtube.com/embed/tv-_1er1mWI?si=1N_CcNnKDAat11RQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

        <iframe style={{ display: 'block', marginLeft: 'auto', marginRight: 'auto', width: '40vw', height: '23vh', marginBottom: '24px' }} src="https://www.youtube.com/embed/tAuRQs_d9F8?si=3ryyoNujajHsPu2t" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

        <iframe style={{ display: 'block', marginLeft: 'auto', marginRight: 'auto', width: '40vw', height: '23vh', marginBottom: '24px' }} src="https://www.youtube.com/embed/NU_1StN5Tkk?si=ya-JWmiLCbLgFz2q" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

</details> 

## MobX

Legal, agora que já discutimos o padrão Observer, vamos falar sobre o MobX. O MobX é uma biblioteca que permite a criação de observáveis e reações de forma simples e eficiente. O MobX é uma biblioteca de gerenciamento de estado que foi inspirada no padrão Observer. A documentação do MobX pode ser encontrada [aqui](https://pub.dev/packages/mobx).

O MobX foi construído utilizando a seguinte filosofia: "Torne o que é observável, reaja a isso e torne isso observável". 

<img src="https://github.com/mobxjs/mobx.dart/raw/master/docs/src/images/mobx-triad.png" style={{ display: 'block', marginLeft: 'auto', maxHeight: '50vh', marginRight: 'auto', marginBottom: '24px' }}/>

O que está figura diz para nós? Na verdade bastante sobre o funcionamento do MobX. Quando uma variável é observável, ela pode ser observada por outras variáveis. Quando uma variável observável é alterada, as variáveis que a observam são notificadas e reagem a essa mudança. Essa é a essencia do MobX.

## Implementando o MobX

Vamos criar um exemplo básico de modificação do MobX. Para isso, vamos primeiro criar um projeto base para a nossa aplicação. Para isso, vamos utilizar o comando `flutter create mobx_example`.

```bash
flutter create mobx_example
```

Agora vamos adicionar as dependências do MobX e do Flutter MobX. Para isso, vamos utilizar o comando `flutter pub add mobx` e `flutter pub add flutter_mobx`.

```bash
flutter pub add mobx
flutter pub add flutter_mobx
```

Agora vamos construir nossa aplicação. Primeiro, vamos criar a estrutura de pastas do nosso projeto. Vamos criar as pastas `models`, `controllers` e `views`. De acordo com o avanço da aplicação, vamos criando os arquivos necessários. Agora, dentro do nosso diretório de `views`, vamos criar um outro diretório com o nome de `screens`. Esse diretório vai conter as telas da nossa aplicação. Nossa aplicação vai possuir apenas duas telas: a tela que exibe a quantidade de vezes que um botão foi clicado e a tela que permite clicar no botão.

> Murilo, que exemplo mais besta é esse?

Eu sei que esse exemplo é simples pessoal, mas tem vários conceitos do MobX que precisamos compreender antes de avançar na construção de soluções mais robustas. Vamos absorver esses conceitos e avançar para soluções mais complexas.

Vamos criar os arquivos `clicks_screen.dart` e `action_screen.dart` dentro do diretório `screens`. Vamos começar a escrever o código da nossa `clicks_screen.dart`.

```dart
// clicks_screen.dart
// Tela que vai exibir a quantidade total de clicks que foram acionados no projeto

import 'package:flutter/material.dart';
import 'package:flutter_mobx/flutter_mobx.dart';
import 'package:mobx_example/controllers/clicks_controller.dart';

class ClicksScreen extends StatelessWidget {
  final ClicksController controller;

  const ClicksScreen({Key? key, required this.controller}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Clicks"),
      ),
      body: Center(
        child: Observer(
          builder: (_) {
            return Text(
              "Total de clicks: ${controller.totalClicks}",
              style: TextStyle(fontSize: 24),
            );
          },
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: (){
          Navigator.pushNamed(context, "/action");
        },
        tooltip: "Trocar de Tela",
        child: const Icon(Icons.arrow_circle_right_outlined),
      )
    );
  }
}
``` 

Vamos avaliar o código anterior:

1. Importamos o pacote `flutter_mobx` para utilizar o `Observer` que é um widget que observa um `Observable` e automaticamente reconstrói o widget quando o `Observable` muda. Importante: essa reconstrução acontece mesmo se o `Observable` for alterado em outro lugar da aplicação e em um `StatelessWidget`.
2. Importamos o `ClicksController` que é o controlador que vai gerenciar o estado da nossa aplicação.
3. Criamos a classe `ClicksScreen` que é um `StatelessWidget` que vai exibir a quantidade total de clicks que foram acionados no projeto.
4. Criamos o método `build` que é o método que vai construir a nossa tela. Dentro dele, temos:
    - Um `Scaffold` que é o widget que implementa o layout básico de uma tela. Ele possui uma `AppBar` que é a barra superior da tela e um `body` que é o corpo da tela.
    - No corpo da tela, temos um `Center` que é um widget que centraliza o seu filho na tela. Dentro dele, temos um `Observer` que é um widget que observa um `Observable` e automaticamente reconstrói o widget quando o `Observable` muda. Dentro do `Observer`, temos um `Text` que é um widget que exibe um texto na tela. O texto exibido é a quantidade total de clicks que foram acionados no projeto.
    - No `floatingActionButton`, temos um `FloatingActionButton` que é um botão flutuante que vai permitir a navegação para a próxima tela.

:::warning[Nossa aplicação ainda não está pronta!]

Nunca é demais avisar, nossa aplicação ainda não pode ser executada sem esses arquivos faltantes!

:::

Agora vamos criar o nosso `ClicksController`. Vamos criar o arquivo `clicks_controller.dart` dentro do diretório `controllers`.

```dart
// clicks_controller.dart
// Controller que vai gerenciar a quantidade total de clicks que foram acionados no projeto

import 'package:mobx/mobx.dart';

part 'clicks_controller.g.dart';

class ClicksController = _ClicksControllerBase with _$ClicksController;

abstract class _ClicksControllerBase with Store {
  @observable
  int totalClicks = 0;

  @action
  void incrementClicks() {
    totalClicks++;
  }
}


```

Vamos avaliar o código anterior:

1. Importamos o pacote `mobx` para utilizar os decoradores `observable` e `action`.
2. Importamos o arquivo `clicks_controller.g.dart` que é o arquivo gerado pelo MobX que contém a implementação dos métodos `incrementClicks` e `totalClicks`.
3. Criamos a classe `ClicksController` que é uma classe que vai gerenciar a quantidade total de clicks que foram acionados no projeto.
4. Criamos a classe `_ClicksControllerBase` que é uma classe abstrata que contém os métodos e atributos que vão ser utilizados pelo `ClicksController`.
5. Criamos o atributo `totalClicks` que é um inteiro que vai armazenar a quantidade total de clicks que foram acionados no projeto.
6. Criamos o método `incrementClicks` que é um método que incrementa a quantidade total de clicks que foram acionados no projeto.

:::danger[Atenção!]

Espera um pouco Murilo, como essa `part 'clicks_controller.g.dart';` foi parar aí?

Quando utilizamos o MobX, nós utilizamos alguns decoradores para indicar que um atributo ou método é observável ou uma ação. O MobX utiliza um gerador de código para gerar o código que vai ser utilizado para observar e reagir a mudanças no estado da aplicação. Para isso, precisamos adicionar a dependência `build_runner` e a dependência `mobx_codegen` ao nosso projeto. Para isso, vamos utilizar o comando:

```bash
flutter pub add build_runner
flutter pub add mobx_codegen
```

Mas espera denovo! Nós vamos ter que criar esse arquivo `clicks_controller.g.dart`? Não! O MobX vai criar esse arquivo para nós. Para isso, primeiro vamos navegar até a raiz do nosso projeto e executar o comando:

```bash
flutter packages pub run build_runner build
```

NÃO VAMOS ALTERAR NENHUM ARQUIVO GERADO PELO MOBX! Eles são gerados automaticamente e qualquer alteração neles pode causar problemas na aplicação. Quando alguma alteração for realizada nos arquivos que utilizam MobX, precisamos executar o comando acima para que os arquivos gerados sejam atualizados.

:::

Agora vamos criar o nosso `ActionScreen`. Vamos criar o arquivo `action_screen.dart` dentro do diretório `screens`.

```dart
// action_screen.dart
// Tela que vai alterar o valor de totalClicks

import 'package:flutter/material.dart';
import 'package:mobx_example/controllers/click_action_controller.dart'; 

class ActionScreen extends StatelessWidget {
  final ClickActionController controller;

  const ActionScreen({Key? key, required this.controller}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Action"),
      ),
      body: Center(
        child: Column(children: [
          const Text(
            "Pressione o botão para incrementar o total de clicks",
            style: TextStyle(fontSize: 24),
          ),
          OutlinedButton(
              onPressed: controller.incrementClicks,
              child:
                  const Text("Incrementar Clicks", style: TextStyle(fontSize: 24))),
        ]),
      ),
    );
  }
}


```

Vamos avaliar o código anterior:

1. Importamos o pacote `flutter/material.dart` para utilizar os widgets do Material Design.
2. Importamos o `ClicksController` que é o controlador que vai gerenciar o estado da nossa aplicação.
3. Criamos a classe `ActionScreen` que é um `StatelessWidget` que vai alterar o valor de `totalClicks`.

Agora vamos criar o nosso `ClickActionController`. Vamos criar o arquivo `click_action_controller.dart` dentro do diretório `controllers`.

```dart
// click_action_controller.dart
// Controller que vai gerenciar a ação de incrementar o total de clicks

import 'package:mobx/mobx.dart';
import 'package:mobx_example/controllers/clicks_controller.dart';

part 'click_action_controller.g.dart';

class ClickActionController = _ClickActionControllerBase with _$ClickActionController;

abstract class _ClickActionControllerBase with Store {
  final ClicksController clicksController;

  _ClickActionControllerBase(this.clicksController);

  @action
  void incrementClicks() {
    clicksController.incrementClicks();
  }
}

```

Vamos avaliar o código anterior:

1. Importamos o pacote `mobx` para utilizar o decorador `action`.
2. Importamos o arquivo `clicks_controller.dart` que é o controlador que vai gerenciar a quantidade total de clicks que foram acionados no projeto.
3. Importamos o arquivo `click_action_controller.g.dart` que é o arquivo gerado pelo MobX que contém a implementação do método `incrementClicks`.
4. Criamos a classe `ClickActionController` que é uma classe que vai gerenciar a ação de incrementar o total de clicks.
5. Criamos a classe `_ClickActionController` que é uma classe abstrata que contém os métodos e atributos que vão ser utilizados pelo `ClickActionController`.
6. Criamos o atributo `clicksController` que é um `ClicksController` que vai gerenciar a quantidade total de clicks que foram acionados no projeto.
7. Criamos o método `incrementClicks` que é um método que incrementa a quantidade total de clicks que foram acionados no projeto.

Agora vamos criar o arquivo `click_action_controller.g.dart` dentro do diretório `controllers`. Para isso, vamos utilizar o comando:

```bash
flutter packages pub run build_runner build
```

:::tip[Store]

Murilo eu já havia reparado antes, mas o que é esse `Store` que aparece nas classes que utilizam MobX?

O `Store` é uma classe que contém os `Observables` e `Actions` que vão ser utilizados por um controlador. O MobX utiliza o `Store` para gerenciar o estado da aplicação. Cada `Store` pode ser visto como um módulo da aplicação que contém os `Observables` e `Actions` que vão ser utilizados por um controlador.

:::

Agora vamos criar o arquivo `main.dart` dentro do diretório `lib`.

```dart
// main.dart
// Arquivo principal da aplicação

import 'package:flutter/material.dart';
import 'package:mobx_example/controllers/click_action_controller.dart';
import 'package:mobx_example/controllers/clicks_controller.dart';
import 'package:mobx_example/views/screens/action_screen.dart';
import 'package:mobx_example/views/screens/clicks_screen.dart';

void main() {
  final ClicksController clicksController = ClicksController();
  final ClickActionController actionController = ClickActionController(clicksController);

  runApp(MyApp(clicksController: clicksController, actionController: actionController));
}

class MyApp extends StatelessWidget {
  final ClicksController clicksController;
  final ClickActionController actionController;

  const MyApp({Key? key, required this.clicksController, required this.actionController}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'MobX Example',
      initialRoute: "/clicks",
      routes: {
        "/clicks": (context) => ClicksScreen(controller: clicksController),
        "/action": (context) => ActionScreen(controller: actionController),
      },
    );
  }
}

```
Agora vamos compreender esse código:

1. Na nossa função `main`, criamos uma instância do `ClicksController` e do `ClickActionController`. Elas são responsáveis por gerenciar o estado da nossa aplicação.
2. Criamos a classe `MyApp` que é um `StatelessWidget` que vai construir a nossa aplicação. Dentro dela, temos:
    - Um `MaterialApp` que é o widget que implementa o layout básico de uma aplicação. Ele possui um `title` que é o título da aplicação, um `initialRoute` que é a rota inicial da aplicação e um `routes` que é um mapa de rotas que a aplicação pode acessar.
    - No `routes`, temos duas rotas: a rota `/clicks` que vai exibir a quantidade total de clicks que foram acionados no projeto e a rota `/action` que vai permitir a ação de incrementar o total de clicks.
    - Quando damos nome a uma rota, podemos acessá-la utilizando o método `Navigator.pushNamed(context, "/nome_da_rota")`.

Agora podemos executar nosso programa e vamos ver que nosso App tem duas telas. A primeira tela exibe a quantidade total de clicks que foram acionados no projeto e a segunda tela permite a ação de incrementar o total de clicks.

Pessoal, observem que o MobX faz muitas automações para nós. Ele é uma biblioteca que facilita a implementação de observáveis e reações em uma aplicação. Com o MobX, podemos criar aplicações mais reativas e responsivas de forma simples e eficiente.

Minha sugestão para vocês nesse momento: façam modificações nesse código!

- Modifiquem a quantidade de clicks que são incrementados a cada clique;
- Modifiquem a mensagem que é exibida na tela;
- Adicionem outras telas e ações..

Utilizar o MobX é uma tarefa que demanda prática. Então, mãos à obra!

