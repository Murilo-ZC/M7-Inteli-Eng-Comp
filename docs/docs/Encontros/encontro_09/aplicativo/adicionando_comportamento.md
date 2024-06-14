---
sidebar_position: 4
title: Adicionando Comportamento
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Adicionando comportamento e estilo ao nosso teclado

Legal, observando algumas calculadoras, podemos perceber que ela possui um estilo diferente para cada botão. Vamos modificar esse comportamento na nossa aplicação. Para isso, vamos avaliar: Não podemos mais passar apenas a lista com os nomes dos botões, precisamos passar também o estilo de cada botão. Logo, nossa lista não terá mais apenas o nome do botão, mas sim um objeto com o nome e o estilo do botão.

```dart
// minha_calculadora.dart
import 'package:calculadora_app/display.dart';
import 'package:calculadora_app/keypad.dart';
import 'package:flutter/material.dart';

class MinhaCalculadora extends StatefulWidget {
  const MinhaCalculadora({super.key});

  @override
  State<MinhaCalculadora> createState() => _MinhaCalculadoraState();
}

class _MinhaCalculadoraState extends State<MinhaCalculadora> {
  String userData = '';
  String result = "";

  // Array com os botões da calculadora
  // A lista foi dividida em 4 linhas
  List<Map> buttons = [
    {'text': '7', 'backcolor': Colors.black, 'textcolor': Colors.white},
    {'text': '8', 'backcolor': Colors.black, 'textcolor': Colors.white},
    {'text': '9', 'backcolor': Colors.black, 'textcolor': Colors.white},
    {'text': '/', 'backcolor': Colors.orange, 'textcolor': Colors.white},
    {'text': '4', 'backcolor': Colors.black, 'textcolor': Colors.white},
    {'text': '5', 'backcolor': Colors.black, 'textcolor': Colors.white},
    {'text': '6', 'backcolor': Colors.black, 'textcolor': Colors.white},
    {'text': 'x', 'backcolor': Colors.orange, 'textcolor': Colors.white},
    {'text': '1', 'backcolor': Colors.black, 'textcolor': Colors.white},
    {'text': '2', 'backcolor': Colors.black, 'textcolor': Colors.white},
    {'text': '3', 'backcolor': Colors.black, 'textcolor': Colors.white},
    {'text': '-', 'backcolor': Colors.orange, 'textcolor': Colors.white},
    {'text': '.', 'backcolor': Colors.black, 'textcolor': Colors.white},
    {'text': '0', 'backcolor': Colors.black, 'textcolor': Colors.white},
    {'text': 'C', 'backcolor': Colors.red, 'textcolor': Colors.white},
    {'text': '+', 'backcolor': Colors.orange, 'textcolor': Colors.white},
    {'text': '=', 'backcolor': Colors.orange, 'textcolor': Colors.white},
    {'text': 'DEL', 'backcolor': Colors.red, 'textcolor': Colors.white},
    {'text': '⚙️', 'backcolor': Colors.blue, 'textcolor': Colors.white},
    {'text': '😁', 'backcolor': Colors.blue, 'textcolor': Colors.white},
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Calculadora Flutter'),
      ),
      backgroundColor: Colors.white38,
      body: Column(
        children: <Widget>[
          // Cria o campo para exibir os dados digitados
          Display(result: result, userData: userData),
          // Cria o campo para exibir as teclas para o usuário
          Keypad(buttons: buttons),
        ],
      ),
    );
  }
}

```

Pessoal algumas coisas para observar aqui. A primeira delas é que no lugar da lista de `Strings`, agora temos uma lista de `Map`. Cada item do `Map` possui o texto do botão e o estilo do botão. Um `Map` é uma coleção de chaves e valores, onde cada chave é única e cada chave mapeia para um valor. Similar a um dicionário em Python. O segundo ponto para se observar é que o nosso arquivo apresenta um erro agora. Isso ocorre porque nosso `Keypad` não está preparado para receber uma lista de `Map` e sim uma lista de `String`. Vamos corrigir isso agora.

```dart
// keypad.dart
import 'package:flutter/material.dart';

class Keypad extends StatelessWidget {
  const Keypad({
    super.key,
    required this.buttons,
  });

  final List<Map> buttons;

  @override
  Widget build(BuildContext context) {
    return Expanded(
      flex: 3,
      child: GridView.builder(
        itemCount: buttons.length,
        gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
          crossAxisCount: 4,
        ),
        itemBuilder: (BuildContext context, int index) {
          // Cria um botão
          return GestureDetector(
            onTap: (){},
            child: Padding(
              padding: const EdgeInsets.all(4.0),
              child: ClipRRect(
                borderRadius: BorderRadius.circular(16),
                child: Container(
                  color: buttons[index]['backcolor'],
                  child: Center(
                    child: Text(
                      buttons[index]['text'],
                      style: TextStyle(
                        color: buttons[index]['textcolor'],
                        fontSize: 25,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ),
                ),
              ),
            ),
          );
        },
      ),
    );
  }
}

```

Agora nossa aplicação está pronta para receber os estilos dos botões. Vamos rodar nossa aplicação e ver como ela está ficando.

<img src={useBaseUrl("/img/calculadora-flutter/calc_03.png")} alt="Arquitetura Sincrona" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'24px' }} />

Um ponto bastante importante que cabe ressaltar no código acima: acessamos os valores do `Map` através da chave. Ou seja, para acessar o valor do texto do botão, utilizamos `buttons[index]['text']` e para acessar o valor do estilo do botão, utilizamos `buttons[index]['backcolor']` e `buttons[index]['textcolor']`. Outro ponto que vale ser chamada atenção é que agora o `TextStyle` do botão não é mais um valor fixo, mas sim um valor que é passado no `Map` de botões. Logo não podemos mais utilizar o modificador `const` para o `TextStyle`.


## Configurando o funcionamento do teclado

Legal, agora temos nossos botões customizados e configurados. Vamos agora adicionar mais um elemento para eles, a sua funcionalidade. Vamos adicionar a funcionalidade de cada botão. Para isso, vamos adicionar um método que irá tratar a ação de cada botão.  Vamos implementar nesse momento todas as funcionalidades com exceção da funcionalidade de "=". Já vamos verificar como realizar a sua implementação. Primeiro vamos modificar o nosso `Keypad` para adicionar a funcionalidade de cada botão.

```dart
// keypad.dart
import 'package:flutter/material.dart';

class Keypad extends StatelessWidget {
  const Keypad({
    super.key,
    required this.buttons,
  });

  final List<Map> buttons;

  @override
  Widget build(BuildContext context) {
    return Expanded(
      flex: 3,
      child: GridView.builder(
        itemCount: buttons.length,
        gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
          crossAxisCount: 4,
        ),
        itemBuilder: (BuildContext context, int index) {
          // Cria um botão
          return GestureDetector(
            onTap: buttons[index].containsKey("action")?buttons[index]["action"]:(){},
            child: Padding(
              padding: const EdgeInsets.all(4.0),
              child: ClipRRect(
                borderRadius: BorderRadius.circular(16),
                child: Container(
                  color: buttons[index]['backcolor'],
                  child: Center(
                    child: Text(
                      buttons[index]['text'],
                      style: TextStyle(
                        color: buttons[index]['textcolor'],
                        fontSize: 25,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ),
                ),
              ),
            ),
          );
        },
      ),
    );
  }
}


```

Aqui podemos verificar que o conteúdo da chave `action` do `Map` de botões é uma função que será executada quando o botão for pressionado. Se nenhuma função foi atribuida, a função padrão é executada. Vamos agora adicionar as funções para cada botão. Para isso vamos alterar nosso arquivo `minha_calculadora.dart`.

```dart
// minha_calculadora.dart
import 'package:calculadora_app/display.dart';
import 'package:calculadora_app/keypad.dart';
import 'package:flutter/material.dart';

class MinhaCalculadora extends StatefulWidget {
  const MinhaCalculadora({super.key});

  @override
  State<MinhaCalculadora> createState() => _MinhaCalculadoraState();
}

class _MinhaCalculadoraState extends State<MinhaCalculadora> {
  String userData = '0';
  String result = "";

  void appendUserData(String data) {
    setState(() {
      userData += data;
    });
  }

  void setUserData(String data){
    setState(() {
      userData = data;
    });
  }

  bool checkIfZero(){
    if (userData == '0'){
      return true;
    }
    return false;
  }

  bool checkIfContainsDot(){
    if (userData.contains('.')){
      return true;
    }
    return false;
  }

  void removeLast(){
    if (userData.length > 1){
      setState(() {
        userData = userData.substring(0, userData.length - 1);
      });
    } else {
      setState(() {
        userData = '0';
      });
    }
  }

  bool checkIfOperation(){
    if (userData[userData.length - 1] == '+' || userData[userData.length - 1] == '-' || userData[userData.length - 1] == 'x' || userData[userData.length - 1] == '/'){
      return true;
    }
    return false;
  }

  void setResult(String data){
    setState(() {
      result = data;
    });
  }
  // Array com os botões da calculadora
  // A lista foi dividida em 4 linhas
  List<Map> buttons = [];

  void init_list(){
    buttons = [
    {'text': '7', 'backcolor': Colors.black, 'textcolor': Colors.white, "action":(){if (checkIfZero()) setUserData('7'); else appendUserData('7');}},
    {'text': '8', 'backcolor': Colors.black, 'textcolor': Colors.white, "action":(){if (checkIfZero()) setUserData('8'); else appendUserData('8');}},
    {'text': '9', 'backcolor': Colors.black, 'textcolor': Colors.white, "action":(){if (checkIfZero()) setUserData('9'); else appendUserData('9');}},
    {'text': '/', 'backcolor': Colors.orange, 'textcolor': Colors.white, "action":(){if(!checkIfOperation()) appendUserData('/');}},
    {'text': '4', 'backcolor': Colors.black, 'textcolor': Colors.white, "action":(){if (checkIfZero()) setUserData('4'); else appendUserData('4');}},
    {'text': '5', 'backcolor': Colors.black, 'textcolor': Colors.white, "action":(){if (checkIfZero()) setUserData('5'); else appendUserData('5');}},
    {'text': '6', 'backcolor': Colors.black, 'textcolor': Colors.white, "action":(){if (checkIfZero()) setUserData('6'); else appendUserData('6');}},
    {'text': 'x', 'backcolor': Colors.orange, 'textcolor': Colors.white, "action":(){if(!checkIfOperation()) appendUserData('x');}},
    {'text': '1', 'backcolor': Colors.black, 'textcolor': Colors.white, "action":(){if (checkIfZero()) setUserData('1'); else appendUserData('1');}},
    {'text': '2', 'backcolor': Colors.black, 'textcolor': Colors.white, "action":(){if (checkIfZero()) setUserData('2'); else appendUserData('2');}},
    {'text': '3', 'backcolor': Colors.black, 'textcolor': Colors.white, "action":(){if (checkIfZero()) setUserData('3'); else appendUserData('3');}},
    {'text': '-', 'backcolor': Colors.orange, 'textcolor': Colors.white, "action":(){if(!checkIfOperation()) appendUserData('-');}},
    {'text': '.', 'backcolor': Colors.black, 'textcolor': Colors.white, "action":(){if (!checkIfContainsDot()) appendUserData('.');}},
    {'text': '0', 'backcolor': Colors.black, 'textcolor': Colors.white, "action":(){if (!checkIfZero()) appendUserData('0');}},
    {'text': 'C', 'backcolor': Colors.red, 'textcolor': Colors.white, "action":(){setUserData('0'); setResult("0");}},
    {'text': '+', 'backcolor': Colors.orange, 'textcolor': Colors.white, "action":(){if(!checkIfOperation()) appendUserData('+');}},
    {'text': '=', 'backcolor': Colors.orange, 'textcolor': Colors.white, },
    {'text': 'DEL', 'backcolor': Colors.red, 'textcolor': Colors.white, "action":(){removeLast();}},
    {'text': '⚙️', 'backcolor': Colors.blue, 'textcolor': Colors.white},
    {'text': '😁', 'backcolor': Colors.blue, 'textcolor': Colors.white},
  ];
  }

  @override
  Widget build(BuildContext context) {
    init_list();
    return Scaffold(
      appBar: AppBar(
        title: const Text('Calculadora Flutter'),
      ),
      backgroundColor: Colors.white38,
      body: Column(
        children: <Widget>[
          // Cria o campo para exibir os dados digitados
          Display(result: result, userData: userData),
          // Cria o campo para exibir as teclas para o usuário
          Keypad(buttons: buttons),
        ],
      ),
    );
  }
}

```

Pessoal reparem que aqui, estamos definindo várias coisas. Primeiro temos um conjunto de métodos auxiliares que são utilizados para diferentes funções. Vamos verificar elas:

- `appendUserData`: Adiciona um valor ao final do campo de dados do usuário.
- `setUserData`: Define um valor para o campo de dados do usuário.
- `checkIfZero`: Verifica se o campo de dados do usuário é igual a zero.
- `checkIfContainsDot`: Verifica se o campo de dados do usuário contém um ponto.
- `removeLast`: Remove o último valor do campo de dados do usuário.
- `checkIfOperation`: Verifica se o último valor do campo de dados do usuário é uma operação.
- `setResult`: Define um valor para o campo de resultado.

Além disso, temos o método `init_list` que é responsável por inicializar a lista de botões. Nesse método, definimos a lista de botões com o texto, cor de fundo, cor do texto e a ação de cada botão. A ação de cada botão é definida através da chave `action` do `Map` de botões. Se a chave `action` não for definida, a função padrão é executada. 

> Shotto Matte Murilo!! Por que não mantivemos a lista de botões como uma variável de estado que é definida como anteriormente?

O que acontece pessoal, agora como as ações dos botões são definidas através de funções, não podemos mais definir a lista de botões como uma variável de estado. Isso porque a lista de botões é definida antes da criação do widget. Assim, quando tentamos acessar um membro do widget, ele ainda não foi criado. 

Vamos rodar nossa aplicação e verificar como ela está ficando.

<img src={useBaseUrl("/img/calculadora-flutter/calc_04.png")} alt="Arquitetura Sincrona" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'24px' }} />

> Calma ai Murilo! Dessa forma, quando digitarmos um número muito grande, ele vai sair da tela. Como podemos resolver isso?

Vamos alterar nosso `Display` para que ele possa exibir o texto de forma que ele não saia da tela. Vamos alterar o arquivo `display.dart`.

```dart
// display.dart
import 'package:flutter/material.dart';

class Display extends StatelessWidget {
  const Display({
    super.key,
    required this.result,
    required this.userData,
  });

  final String result;
  final String userData;

  @override
  Widget build(BuildContext context) {
    return Expanded(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        children: [
          Container(
            padding: const EdgeInsets.all(20),
            alignment: Alignment.centerRight,
            child: Text(
              result,
              style: const TextStyle(
                fontSize: 24,
                color: Colors.white,
              ),
            ),
          ),
          Container(
            padding: const EdgeInsets.all(15),
            alignment: Alignment.centerRight,
            child: FittedBox(
              child: Text(
                userData != "" ? userData : "0",
                style: const TextStyle(
                  fontSize: 48,
                  color: Colors.white,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}

```

Nós utilizamos o `FittedBox` para que o texto se ajuste ao tamanho da tela. Aqui uma nota importante, se o tamanho do texto for nulo, ele será substituído por "0". Esse comportamento é importante pois se o campo de texto ficar com tamanho vazio, o `FittedBox` não irá funcionar.

## Adicionando o comportamento do botão `=`

Agora vamos lá, nosso botão `=`. Para implementarmos seu funcionamento, vamos utilizar a biblioteca `math_expressions`. Essa biblioteca nos permite avaliar expressões matemáticas. Vamos adicionar essa biblioteca ao nosso arquivo `pubspec.yaml`. Para mais detalhes sobre ela, acesse [aqui](https://pub.dev/packages/math_expressions).

```yaml
#Conteúdo do arquivo pubspec.yaml	
dependencies:
  math_expressions: ^2.5.0
```

Ou ainda podemos adicionar ela pelo terminal:
    
```bash

flutter pub add math_expressions

```

Legal, agora vamos implementar a funcionalidade do botão `=`. Vamos alterar o arquivo `minha_calculadora.dart`.

```dart
// minha_calculadora.dart
import 'package:calculadora_app/display.dart';
import 'package:calculadora_app/keypad.dart';
import 'package:flutter/material.dart';
import 'package:math_expressions/math_expressions.dart';

class MinhaCalculadora extends StatefulWidget {
  const MinhaCalculadora({super.key});

  @override
  State<MinhaCalculadora> createState() => _MinhaCalculadoraState();
}

class _MinhaCalculadoraState extends State<MinhaCalculadora> {
  String userData = '0';
  String result = "";

  void appendUserData(String data) {
    setState(() {
      userData += data;
    });
  }

  void setUserData(String data){
    setState(() {
      userData = data;
    });
  }

  bool checkIfZero(){
    if (userData == '0'){
      return true;
    }
    return false;
  }

  bool checkIfContainsDot(){
    if (userData.contains('.')){
      return true;
    }
    return false;
  }

  void removeLast(){
    if (userData.length > 1){
      setState(() {
        userData = userData.substring(0, userData.length - 1);
      });
    } else {
      setState(() {
        userData = '0';
      });
    }
  }

  bool checkIfOperation(){
    if (userData[userData.length - 1] == '+' || userData[userData.length - 1] == '-' || userData[userData.length - 1] == 'x' || userData[userData.length - 1] == '/'){
      return true;
    }
    return false;
  }

  void setResult(String data){
    setState(() {
      result = data;
    });
  }

  String avaliarExpressao(){
    String finaluserinput = userData;
    finaluserinput = finaluserinput.replaceAll('x', '*');
 
    Parser p = Parser();
    Expression exp = p.parse(finaluserinput);
    ContextModel cm = ContextModel();
    double eval = exp.evaluate(EvaluationType.REAL, cm);
    return eval.toString();
  }
  // Array com os botões da calculadora
  // A lista foi dividida em 4 linhas
  List<Map> buttons = [];

  void init_list(){
    buttons = [
    {'text': '7', 'backcolor': Colors.black, 'textcolor': Colors.white, "action":(){if (checkIfZero()) setUserData('7'); else appendUserData('7');}},
    {'text': '8', 'backcolor': Colors.black, 'textcolor': Colors.white, "action":(){if (checkIfZero()) setUserData('8'); else appendUserData('8');}},
    {'text': '9', 'backcolor': Colors.black, 'textcolor': Colors.white, "action":(){if (checkIfZero()) setUserData('9'); else appendUserData('9');}},
    {'text': '/', 'backcolor': Colors.orange, 'textcolor': Colors.white, "action":(){if(!checkIfOperation()) appendUserData('/');}},
    {'text': '4', 'backcolor': Colors.black, 'textcolor': Colors.white, "action":(){if (checkIfZero()) setUserData('4'); else appendUserData('4');}},
    {'text': '5', 'backcolor': Colors.black, 'textcolor': Colors.white, "action":(){if (checkIfZero()) setUserData('5'); else appendUserData('5');}},
    {'text': '6', 'backcolor': Colors.black, 'textcolor': Colors.white, "action":(){if (checkIfZero()) setUserData('6'); else appendUserData('6');}},
    {'text': 'x', 'backcolor': Colors.orange, 'textcolor': Colors.white, "action":(){if(!checkIfOperation()) appendUserData('x');}},
    {'text': '1', 'backcolor': Colors.black, 'textcolor': Colors.white, "action":(){if (checkIfZero()) setUserData('1'); else appendUserData('1');}},
    {'text': '2', 'backcolor': Colors.black, 'textcolor': Colors.white, "action":(){if (checkIfZero()) setUserData('2'); else appendUserData('2');}},
    {'text': '3', 'backcolor': Colors.black, 'textcolor': Colors.white, "action":(){if (checkIfZero()) setUserData('3'); else appendUserData('3');}},
    {'text': '-', 'backcolor': Colors.orange, 'textcolor': Colors.white, "action":(){if(!checkIfOperation()) appendUserData('-');}},
    {'text': '.', 'backcolor': Colors.black, 'textcolor': Colors.white, "action":(){if (!checkIfContainsDot()) appendUserData('.');}},
    {'text': '0', 'backcolor': Colors.black, 'textcolor': Colors.white, "action":(){if (!checkIfZero()) appendUserData('0');}},
    {'text': 'C', 'backcolor': Colors.red, 'textcolor': Colors.white, "action":(){setUserData('0'); setResult("0");}},
    {'text': '+', 'backcolor': Colors.orange, 'textcolor': Colors.white, "action":(){if(!checkIfOperation()) appendUserData('+');}},
    {'text': '=', 'backcolor': Colors.orange, 'textcolor': Colors.white, "action": (){setResult(avaliarExpressao()); setUserData("0");}},
    {'text': 'DEL', 'backcolor': Colors.red, 'textcolor': Colors.white, "action":(){removeLast();}},
    {'text': '⚙️', 'backcolor': Colors.blue, 'textcolor': Colors.white},
    {'text': '😁', 'backcolor': Colors.blue, 'textcolor': Colors.white},
  ];
  }

  @override
  Widget build(BuildContext context) {
    init_list();
    return Scaffold(
      appBar: AppBar(
        title: const Text('Calculadora Flutter'),
      ),
      backgroundColor: Colors.white38,
      body: Column(
        children: <Widget>[
          // Cria o campo para exibir os dados digitados
          Display(result: result, userData: userData),
          // Cria o campo para exibir as teclas para o usuário
          Keypad(buttons: buttons),
        ],
      ),
    );
  }
}


```

Podemos ver o resultado da nossa aplicação.

<img src={useBaseUrl("/img/calculadora-flutter/calc_05.png")} alt="Arquitetura Sincrona" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'24px' }} />

Pessoal apenas para avaliarmos como o `=` está funcionando, vamos avaliar o método `avaliarExpressao`:

- Primeiro, substituímos o `x` por `*` para que a expressão seja válida.
- Em seguida, criamos um `Parser` e passamos a expressão para ele. O `Parser` é responsável por analisar a expressão matemática. 
- Criamos uma expressão a partir do `Parser` e passamos a expressão para o `ContextModel`. O `ContextModel` é responsável por avaliar a expressão.
- Por fim, avaliamos a expressão e retornamos o resultado.

Legal, até aqui temos nossa aplicação funcionando localmente. Vamos adicionar a ela a capacidade de conversar com nosso backend agora. Vamos lá!