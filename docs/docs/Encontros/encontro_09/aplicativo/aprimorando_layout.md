---
sidebar_position: 3
title: Aprimorando o Layout
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Continuando a construção do aplicativo

Até aqui pessoal, nossa calculadora básica depende da inserção dos valores manualmente. Vimos que o usuário pode inserir um valor inválido e a aplicação não consegue tratar isso. Vamos modificar nosso layout agora. Vamos adicionar botões para que o usuário possa inserir os valores e as operações. Vamos adicionar botões para as operações de soma, subtração, multiplicação e divisão. Além de um botão que irá realizar a operação e outro que irá limpar a tela.

Vamos começar modificando o arquivo `main.dart`:

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Calculadora Flutter',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: const MinhaCalculadora(),
    );
  }
}

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
  List<String> buttons = [
    '7',
    '8',
    '9',
    '/',
    '4',
    '5',
    '6',
    'x',
    '1',
    '2',
    '3',
    '-',
    '.',
    '0',
    'C',
    '+',
    '=',
    'DEL',
    '⚙️',
    '😁',
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
          Expanded(
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
                  child: Text(
                    userData,
                    style: const TextStyle(
                      fontSize: 48,
                      color: Colors.white,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ),
              ],
            ),
          ),
          // Cria o campo para exibir as teclas para o usuário
          Expanded(
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
                        color: Colors.white70,
                        child: Center(
                          child: Text(
                            buttons[index],
                            style: const TextStyle(
                              color: Colors.black,
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
          ),
        ],
      ),
    );
  }
}

```

Agora temos o seguinte layout na nossa aplicação:

<img src={useBaseUrl("/img/calculadora-flutter/calc_02.png")} alt="Arquitetura Sincrona" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'24px' }} />

Ahhhh agora estamos com um layout que parece mais com uma calculadora de celular. Mas ele ainda não faz nada e temos um monte de código novo para avaliar. Vamos lá??

A primeira coisa que chama atenção no nosso código está já no nosso `MyApp`. Estamos desativando o banner de debug da aplicação. Isso é importante para que a aplicação fique mais limpa e não tenha informações que não são necessárias para o usuário final. 

Bom agora vamos descer mais o nível nas modificações. Vamos analisar o que fizemos no `MinhaCalculadora`. Primeiro removemos a aplicação anterior e agora, no lugar dos campos de texto, temos um campo de texto para exibir o resultado da operação e outro para exibir os dados digitados pelo usuário. Esses valores ficaram armazenados nas variáveis `result` e `userData` respectivamente.

Além destes campos, nós também criamos uma lista de Strings com o texto de cada botão que estamos utilizando na nossa aplicação. Essa lista é utilizada para criar os botões da calculadora. Beleza, agora vamos para o método `build` da nossa aplicação.

Estamos setando a cor do fundo da nossa aplicação para `Colors.white38`. Esse valor pode ser diferente de acordo com o que você deseja. Apenas lembre-se de que a cor deve ser um valor hexadecimal. O `Colors.white38` é um valor hexadecimal que representa a cor branca com 38% de opacidade. Para escrever sua própria cor, utilize o método `Color.fromRGBO(255, 255, 255, 0.38)`.

Agora, no `body` da nossa aplicação, temos uma coluna com dois campos. O primeiro campo é um `Container` que exibe o resultado da operação. O segundo campo é um `Container` que exibe os dados digitados pelo usuário. Ambos os campos estão envolvidos pelo widget `Expanded`. Isso faz com que os campos ocupem o espaço disponível na tela. A propriedade `flex` do widget `Expanded` é utilizada para definir a proporção de espaço que cada campo irá ocupar. No nosso caso, o campo que exibe os dados digitados pelo usuário irá ocupar 3 vezes mais espaço que o campo que exibe o resultado da operação. O widget `Expanded` apenas pode ser utilizado dentro de um widget `Column` ou `Row`.

Para exibição dos dados informados pelo usuário, primeiro criamos um `Container` com um `padding` de 15 pixels em todas as direções. Dentro desse `Container`, criamos um `Text` que exibe o valor da variável `userData`. O `Text` possui um estilo que define o tamanho da fonte como 48, a cor do texto como branca e o peso da fonte como negrito. O mesmo é feito para o campo que exibe o resultado da operação, porém com um `padding` de 20 pixels e um tamanho de fonte de 24. Esses dois containers estão envolvidos por um `Column`.

Vamos agora para os botões onde o usuário informa os valores da aplicação. Para isso, vamos utilizar um `GridView`. O widget `GridView` é utilizado para exibir uma grade de widgets em uma lista de rolagem. Em geral, utilizamos ele quando queremos exibir uma lista de widgets em duas dimensões. No nosso caso, queremos exibir os botões da calculadora em uma grade de 4 colunas. Para isso, utilizamso o `GridView.builder` que é uma versão otimizada do `GridView` que cria os widgets sob demanda. Isso significa que ele só cria os widgets que estão visíveis na tela. Isso é importante para melhorar a performance da aplicação.

No `GridView.builder`, definimos o número de itens que serão exibidos na grade, o `gridDelegate` que define o layout da grade e o `itemBuilder` que define como cada item da grade será construído. No nosso caso, o `itemBuilder` é uma função que recebe o contexto e o índice do item e retorna um widget. Nessa função, criamos um `GestureDetector` que envolve um `Padding` que envolve um `ClipRRect` que envolve um `Container` que envolve um `Center` que envolve um `Text`. Ufa! Muitos widgets, não é mesmo? Vamos entender o que cada um faz.

O `GestureDetector` é utilizado para detectar gestos do usuário. No nosso caso, queremos detectar o toque do usuário em um botão. Para isso, utilizamos o `onTap` do `GestureDetector`. No nosso caso, o `onTap` está vazio, mas é aqui que iremos adicionar a lógica para cada botão. O `Padding` é utilizado para adicionar um preenchimento ao redor do widget. O `ClipRRect` é utilizado para recortar os cantos do widget. No nosso caso, estamos arredondando os cantos do botão. O `Container` é utilizado para adicionar um fundo ao widget. No nosso caso, estamos utilizando a cor branca com 70% de opacidade. O `Center` é utilizado para centralizar o widget filho. No nosso caso, o widget filho é um `Text` que exibe o texto do botão. O `Text` é utilizado para exibir um texto na tela. No nosso caso, o texto é o valor do botão. O `Text` possui um estilo que define o tamanho da fonte como 25, a cor do texto como preta e o peso da fonte como negrito.

Caramba! Muita coisa mesmo para compreender. POR ISSO ESTAMOS FAZENDO UM APP QUE É CONHECIDO DE TODOS COMO FUNCIONA!!!!!!

Antes de avançarmos em adicionar o funcionamento do nossa aplicativo, vamos refletir um pouco: esse código, que só tem a estrutura dos nossos componentes. Está començando a ficar um pouco grande. Será que não podemos dividi-lo em partes menores? Sim ou Com certeza?

<img src="https://media3.giphy.com/media/kWqBN1d6bQsXysO5Pv/giphy.gif" alt="Arquitetura Sincrona" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'24px' }} />

## Refatorando nossa aplicação

Vamos dividir nosso código em partes menores. Vamos criar um arquivo para cada parte da nossa aplicação. Primeiro vamos criar o arquivo `minha_calculadora.dart` e mover a classe `MinhaCalculadora` para esse arquivo.

:::tip[Onde Criar os Arquivos?]

Pessoal se você já sente-se seguro com a separação por estrutura e responsabilidade que fizemos com o MVC, já pode e deve seguir ele. Senão eu sugiro fortemente que vocês me sigam aqui e por enquanto fiquem com seus widgets dentro do diretório `lib` apenas.

:::

```dart
// minha_calculadora.dart
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
  List<String> buttons = [
    '7',
    '8',
    '9',
    '/',
    '4',
    '5',
    '6',
    'x',
    '1',
    '2',
    '3',
    '-',
    '.',
    '0',
    'C',
    '+',
    '=',
    'DEL',
    '⚙️',
    '😁',
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
          Expanded(
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
                  child: Text(
                    userData,
                    style: const TextStyle(
                      fontSize: 48,
                      color: Colors.white,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ),
              ],
            ),
          ),
          // Cria o campo para exibir as teclas para o usuário
          Expanded(
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
                        color: Colors.white70,
                        child: Center(
                          child: Text(
                            buttons[index],
                            style: const TextStyle(
                              color: Colors.black,
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
          ),
        ],
      ),
    );
  }
}

```

Agora vamos criar o arquivo `app.dart` e mover a classe `MyApp` para esse arquivo.

```dart
// app.dart
import 'package:calculadora_app/minha_calculadora.dart';
import 'package:flutter/material.dart';

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Calculadora Flutter',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: const MinhaCalculadora(),
    );
  }
}
```

Por fim, vamos ajustar nossa `main.dart` para importar os arquivos que criamos.

```dart
// main.dart
import 'package:calculadora_app/app.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}
```

Pessoal, de imediato, o que é possível perceber aqui: nossos arquivos estão mais organizados e mais fáceis de serem lidos. Isso é muito importante, em especial quando a complexidade da aplicação vai aumentando. Vamos continuar com nossa lógica de dividir nossa aplicação em blocos menores de código, agora observando nosso arquivo `minha_calculadora.dart`. Observando ele, podemos ver que temos dois blocos que fazem a construção do nosso corpo da aplicação. Vamos separar esses blocos em arquivos diferentes. Vamos ter o `display.dart` e o `keypad.dart`. Vamos primeiro analisar o `display.dart`:

:::tip[Extraindo Widgets]

Pessoal enquanto estamos desenvolvendo nossa aplicação é comum que a gente vá criando os widgets e os colocando no mesmo arquivo. Isso é normal e não tem problema. Mas quando a aplicação começa a crescer, é importante que a gente comece a separar esses widgets em arquivos diferentes. Agora, esse processo pode ser um tanto quando `trick` e podemos acabar quebrando a aplicação ou extraindo o código incorreto. Para evitar esse problema, podemos utilizar a ferramenta de refatoração do VSCode. Para isso, selecione o código que deseja extrair e clique com o botão direito do mouse. No menu que aparecer, clique em `Refactor` e depois em `Extract Widget`. O VSCode irá criar um novo arquivo com o código selecionado.

<img src={useBaseUrl("/img/calculadora-flutter/extrair_widgets.png")} alt="Arquitetura Sincrona" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'24px' }} />

:::

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
            child: Text(
              userData,
              style: const TextStyle(
                fontSize: 48,
                color: Colors.white,
                fontWeight: FontWeight.bold,
              ),
            ),
          ),
        ],
      ),
    );
  }
}

```

Repare que ao extrairmos nosso widget, ele ficou mais limpo e mais fácil de ser lido. Mas não é só isso não é mesmo? Observe que ele foi criado com um construtor que recebe os valores `result` e `userData`. Isso é importante para que possamos passar esses valores para o widget. Vamos agora extrair o nosso teclado da calculadora. Vamos criar o arquivo `keypad.dart`:

```dart
// keypad.dart
import 'package:flutter/material.dart';

class Keypad extends StatelessWidget {
  const Keypad({
    super.key,
    required this.buttons,
  });

  final List<String> buttons;

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
                  color: Colors.white70,
                  child: Center(
                    child: Text(
                      buttons[index],
                      style: const TextStyle(
                        color: Colors.black,
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

Da mesma forma que aconteceu com o `display.dart`, o `keypad.dart` também recebe um construtor que recebe a lista de botões que serão exibidos na calculadora. Agora vamos ajustar o nosso arquivo `minha_calculadora.dart` para utilizar esses widgets:

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
  List<String> buttons = [
    '7',
    '8',
    '9',
    '/',
    '4',
    '5',
    '6',
    'x',
    '1',
    '2',
    '3',
    '-',
    '.',
    '0',
    'C',
    '+',
    '=',
    'DEL',
    '⚙️',
    '😁',
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

Ahhh nossa aplicação agora ficou bem mais simples de ser lida e entendida. Isso é muito importante!!
Pessoal, agora vamos observar mais um ponto que conseguimos ajustar aqui. Além de enviarmos qual o texto de cada botão vamos enviar, seria interessante passar mais algumas informações, como a cor do fundo do botão e qual a função ele desempenha. Vamos fazer esse ajuste na nossa próxima seção!