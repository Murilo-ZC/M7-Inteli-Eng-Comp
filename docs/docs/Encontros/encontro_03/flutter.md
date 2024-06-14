---
sidebar_position: 4
title: Framework Flutter
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Introdução ao Flutter

Até que enfim! Chegamos no ponto que nos interessa mais! Vamos falar sobre o Flutter!

Vamos criar nossa primeira aplicação com o Flutter. Para isso, vamos seguir os seguintes passos:

1. Instalar o Flutter ✅
2. Configurar as ferramentas ✅
3. Criar o nosso primeiro projeto ❕
4. Executar o nosso projeto ❕

Vamos seguir com o passo 3 e 4!

Primeiro vamos abrir o VS Code para criar o nosso projeto. Vamos clicar em `View` -> `Command Palette` e digitar `Flutter: New Project`. Vamos escolher a opção `Application` e vamos escolher o local onde vamos salvar o nosso projeto. Ao concluir a criação do projeto, vamos ter uma tela parecida com essa:

<img src={useBaseUrl("/img/ola-flutter/criando-projeto.png")} alt="Arquitetura Sincrona" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'24px' }} />

Agora vamos avaliar algumas coisas importantes para nosso desenvolvimento. O primeiro ponto a se observar é que nosso código fonte reside na pasta `lib/main.dart`. Vamos abrir esse arquivo e vamos ver o seguintimo código:

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
      title: 'Flutter Demo',
      theme: ThemeData(
        // This is the theme of your application.
        //
        // TRY THIS: Try running your application with "flutter run". You'll see
        // the application has a purple toolbar. Then, without quitting the app,
        // try changing the seedColor in the colorScheme below to Colors.green
        // and then invoke "hot reload" (save your changes or press the "hot
        // reload" button in a Flutter-supported IDE, or press "r" if you used
        // the command line to start the app).
        //
        // Notice that the counter didn't reset back to zero; the application
        // state is not lost during the reload. To reset the state, use hot
        // restart instead.
        //
        // This works for code too, not just values: Most code changes can be
        // tested with just a hot reload.
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: const MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  // This widget is the home page of your application. It is stateful, meaning
  // that it has a State object (defined below) that contains fields that affect
  // how it looks.

  // This class is the configuration for the state. It holds the values (in this
  // case the title) provided by the parent (in this case the App widget) and
  // used by the build method of the State. Fields in a Widget subclass are
  // always marked "final".

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      // This call to setState tells the Flutter framework that something has
      // changed in this State, which causes it to rerun the build method below
      // so that the display can reflect the updated values. If we changed
      // _counter without calling setState(), then the build method would not be
      // called again, and so nothing would appear to happen.
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    // This method is rerun every time setState is called, for instance as done
    // by the _incrementCounter method above.
    //
    // The Flutter framework has been optimized to make rerunning build methods
    // fast, so that you can just rebuild anything that needs updating rather
    // than having to individually change instances of widgets.
    return Scaffold(
      appBar: AppBar(
        // TRY THIS: Try changing the color here to a specific color (to
        // Colors.amber, perhaps?) and trigger a hot reload to see the AppBar
        // change color while the other colors stay the same.
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        // Here we take the value from the MyHomePage object that was created by
        // the App.build method, and use it to set our appbar title.
        title: Text(widget.title),
      ),
      body: Center(
        // Center is a layout widget. It takes a single child and positions it
        // in the middle of the parent.
        child: Column(
          // Column is also a layout widget. It takes a list of children and
          // arranges them vertically. By default, it sizes itself to fit its
          // children horizontally, and tries to be as tall as its parent.
          //
          // Column has various properties to control how it sizes itself and
          // how it positions its children. Here we use mainAxisAlignment to
          // center the children vertically; the main axis here is the vertical
          // axis because Columns are vertical (the cross axis would be
          // horizontal).
          //
          // TRY THIS: Invoke "debug painting" (choose the "Toggle Debug Paint"
          // action in the IDE, or press "p" in the console), to see the
          // wireframe for each widget.
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            const Text(
              'You have pushed the button this many times:',
            ),
            Text(
              '$_counter',
              style: Theme.of(context).textTheme.headlineMedium,
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
        tooltip: 'Increment',
        child: const Icon(Icons.add),
      ), // This trailing comma makes auto-formatting nicer for build methods.
    );
  }
}

```

Temos uma quantidade bastante grande de código aqui, mas boa parte dele são comentários para descrever algumas configurações. Vamos primeiro remover os comentários para deixar o código mais limpo. Vamos remover os comentários e vamos ter o seguinte código:

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: const MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            const Text(
              'You have pushed the button this many times:',
            ),
            Text(
              '$_counter',
              style: Theme.of(context).textTheme.headlineMedium,
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
        tooltip: 'Increment',
        child: const Icon(Icons.add),
      ), // This trailing comma makes auto-formatting nicer for build methods.
    );
  }
}

```

Já temos um código mais palatável. Antes de analisarmos esse código, vamos colocar ele para rodar no nosso emulador. No canto inferior direito do VS Code, temos a opção de escolher o dispositivo que vamos utilizar para rodar o nosso aplicativo. Vamos escolher o dispositivo e vamos clicar no botão `Run and Debug`. Vamos ver o nosso aplicativo rodando no emulador.

<img src={useBaseUrl("/img/ola-flutter/primeiro-app.png")} alt="Arquitetura Sincrona" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'24px' }} />

Agora sim! Temos o nosso primeiro aplicativo rodando no emulador! 🎉

Vamos avaliar agora o que aconteceu e como o nosso código gerou nosso aplicativo.

1. `void main()`: é a função principal do nosso aplicativo. Ela é a primeira função que é executada quando o aplicativo é iniciado. Nela, estamos chamando a função `runApp` e passando o widget `MyApp` para ser o widget principal do nosso aplicativo.
2. `MyApp`:
    - `build`: é o método que constrói o widget. Neste método, estamos retornando um `MaterialApp` que é o widget principal do nosso aplicativo. Neste widget, estamos definindo o título do nosso aplicativo e o tema que vamos utilizar. Além disso, estamos definindo o widget que vai ser a nossa tela inicial. 
3. `MyHomePage`:
    - `build`: é o método que constrói o widget. Neste método, estamos retornando um `Scaffold` que é o widget que define a estrutura básica de uma tela. Neste widget, estamos definindo a barra superior do aplicativo, o corpo da tela e o botão flutuante. 
    - `_incrementCounter`: é o método que incrementa o contador. Neste método, estamos chamando o método `setState` para atualizar o estado do widget. Quando o estado do widget é atualizado, o Flutter chama o método `build` para atualizar a interface do usuário.
    - `_counter`: é a variável que armazena o valor do contador.
    - `title`: é o título da tela.

Agora que temos o nosso aplicativo rodando, vamos fazer algumas alterações para ver como o Flutter trabalha com o *hot reload*. Vamos alterar o título do aplicativo e vamos ver como o Flutter atualiza a interface do usuário sem precisar reiniciar o aplicativo. Vamos alterar o título do aplicativo para `Meu Primeiro App` e vamos ver o resultado.

<img src="https://64.media.tumblr.com/8da1013538407144535de1803a82cf4d/tumblr_p5z64pm3Ga1tpvtc4o2_r2_500.gif" alt="Arquitetura Sincrona" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'24px' }} />

Pessoal até aqui discultimos alguns conceitos básicos do Flutter. Vamos agora verificar como adicionar novos recursos ao nosso aplicativo.

---

### Adicionando recursos ao aplicativo

Pessoal, vamos editar nosso aplicativo padrão para adicionar algumas funcionalidades nele:

- Adicionar imagens (mídia) no app;
- Adicionar um botão para mudar de tela;
- Adicionar um campo de texto para o usuário digitar algo;
- Adicionar um botão para enviar para realizar uma consulta a uma API.

Primeiro, vamos editar a estrutura do nosso arquivo `lib/main.dart`:

```dart
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: const MinhaPrimeiraTela(),
    );
  }
}

class MinhaPrimeiraTela extends StatelessWidget {
  const MinhaPrimeiraTela({super.key});

  @override
  Widget build(BuildContext context) {
    return  Container();
  }
}
```

Pessoal repare que aqui, temos um novo widget chamado `MinhaPrimeiraTela`. Atualmente, ele está retornando um `Container`. Vamos alterar esse widget para retornar um `Scaffold` com uma imagem e um botão. Vamos alterar o código para o seguinte:

```dart
//Código anterior omitido

class MinhaPrimeiraTela extends StatelessWidget {
  const MinhaPrimeiraTela({super.key});

  @override
  Widget build(BuildContext context) {
    return  Scaffold(
      appBar: AppBar(
        title: const Text('Minha primeira tela'),
      ),
      body: const Center(
        child: Text('Olá, mundo!'),
      ),
    );
  }
}
```
O que fizemos de alteração aqui pessoal? Adicionamos um elemento estruturante na nossa aplicação, o `Scaffold`. O `Scaffold` é um widget que define a estrutura básica de uma tela. Ele possui várias propriedades que permitem personalizar a aparência da tela, como a barra superior, o corpo da tela e o botão flutuante. No nosso caso, estamos definindo a barra superior com o título `Minha primeira tela` e o corpo da tela com o texto `Olá, mundo!`.

Pessoal como recurso de imagem, vamos utilizar duas fotos disponíveis no [pexels](https://www.pexels.com/pt-br/) e [unslapsh](https://unsplash.com/pt-br). Vamos utilizar elas da seguinte maneira:

- Recurso online: https://images.pexels.com/photos/8364804/pexels-photo-8364804.jpeg
- Recurso offline: https://unsplash.com/pt-br/fotografias/cao-branco-e-marrom-de-pelagem-curta-no-tapete-marrom-nvuzRUquElY

Para adicionar a imagem vinda de uma URL, vamos utilizar o widget `Image.network`. Vamos adicionar a imagem no nosso aplicativo. Vamos alterar o código para o seguinte:

```dart
//Código anterior omitido

class MinhaPrimeiraTela extends StatelessWidget {
  const MinhaPrimeiraTela({super.key});

  @override
  Widget build(BuildContext context) {
    return  Scaffold(
      appBar: AppBar(
        title: const Text('Minha primeira tela'),
      ),
      body: Column(
        children:  <Widget>[
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Image.network('https://images.pexels.com/photos/8364804/pexels-photo-8364804.jpeg',
              width: 300,
              height: 300,
              fit: BoxFit.cover,
            ),
          ),
        ],
      )
    );
  }
}
```

Vamos avaliar o que fizemos aqui:

- Adicionamos um novo widget `Column` para organizar os widgets em uma coluna. O `Column` é um widget que organiza os widgets em uma coluna vertical. Ele possui várias propriedades que permitem personalizar a aparência da coluna, como o alinhamento dos widgets e o espaçamento entre eles.
- Adicionamos um novo widget `Padding` para adicionar um espaçamento ao redor da imagem. O `Padding` é um widget que adiciona um espaçamento ao redor de um widget filho. Ele possui várias propriedades que permitem personalizar o espaçamento, como a quantidade de espaçamento e a cor do espaçamento.
- Adicionamos um novo widget `Image.network` para exibir a imagem. O `Image.network` é um widget que exibe uma imagem vinda de uma URL. Ele possui várias propriedades que permitem personalizar a aparência da imagem, como a largura, a altura e o ajuste da imagem.

Agora vamos adicionar o recurso da imagem dentro da nossa aplicação. Primeiro vamos adicionar a imagem no nosso projeto. Vamos criar uma pasta chamada `assets` na raiz do nosso projeto e vamos adicionar a imagem `cao.jpg` nessa pasta. Vamos alterar o arquivo `pubspec.yaml` para adicionar a imagem no nosso projeto. Vamos adicionar o seguinte código:

```yaml
# Código anterior omitido
flutter:
  assets:
    - assets/cao.jpg

# Código posterior omitido
```

Quando realizamos alguma mudança no arquivo `pubspec.yaml`, precisamos rodar o comando `flutter pub get` para que as mudanças sejam aplicadas. O plugin do Flutter no VS Code já faz isso automaticamente para nós. Agora que adicionamos a imagem no nosso projeto, vamos alterar o código para adicionar a imagem no nosso aplicativo. Vamos alterar o código para o seguinte:

```dart
//Código anterior omitido

class MinhaPrimeiraTela extends StatelessWidget {
  const MinhaPrimeiraTela({super.key});

  @override
  Widget build(BuildContext context) {
    return  Scaffold(
      appBar: AppBar(
        title: const Text('Minha primeira tela'),
      ),
      body: Column(
        children:  <Widget>[
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Image.network('https://images.pexels.com/photos/8364804/pexels-photo-8364804.jpeg',
              width: 300,
              height: 300,
              fit: BoxFit.cover,
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Image.asset('assests/cao.jpg',
              width: 300,
              height: 300,
              fit: BoxFit.cover,
            ),
          ),
        ],
      )
    );
  }
}
```

:::note[Alterações no pubspec.yaml]

Pessoal, sempre que alguma alteração é feita no arquivo `pubspec.yaml`, é necessário rodar o comando `flutter pub get` para que as mudanças sejam aplicadas. O plugin do Flutter no VS Code já faz isso automaticamente para nós.

Além disso, para que as alterações possam ser refletidas no aplicativo, é necessário fechar o aplicativo e abri-lo novamente. Isso é necessário porque o Flutter não recarrega automaticamente os recursos do aplicativo quando eles são alterados.

:::

### Mudando de tela no aplicativo

Agora vamos adicionar um botão para mudar de tela. Vamos adicionar um novo widget `ElevatedButton` para adicionar um botão na tela. Vamos alterar o código para o seguinte:

```dart
//Código anterior omitido

class MinhaPrimeiraTela extends StatelessWidget {
  const MinhaPrimeiraTela({super.key});

  @override
  Widget build(BuildContext context) {
    return  Scaffold(
      appBar: AppBar(
        title: const Text('Minha primeira tela'),
      ),
      body: Column(
        children:  <Widget>[
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Image.network('https://images.pexels.com/photos/8364804/pexels-photo-8364804.jpeg',
              width: 300,
              height: 300,
              fit: BoxFit.cover,
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Image.asset('assets/cao.jpg',
              width: 300,
              height: 300,
              fit: BoxFit.cover,
            ),
          ),
          const ElevatedButton(onPressed: null, child: Text("Mudar de Tela"))
        ],
      )
    );
  }
}
```

Por hora, nosso botão aparece desabilitado, pois não definimos o que ele deve fazer. Vamos criar um novo arquivo com o nome `segunda_tela.dart` e vamos adicionar o seguinte código:

```dart
import 'package:flutter/material.dart';

class MinhaSegundaTela extends StatelessWidget {
  const MinhaSegundaTela({super.key});

  @override
  Widget build(BuildContext context) {
    return const Placeholder();
  }
}
```

Vamos adicionar agora a funcionalidade de trocar da primeira para a segunda tela. Vamos alterar o código da nossa primeira tela para o seguinte:

```dart

import 'package:flutter/material.dart';
import 'package:ola_mundo/segunda_tela.dart';

// Código anterior omitido

class MinhaPrimeiraTela extends StatelessWidget {
  const MinhaPrimeiraTela({super.key});

  @override
  Widget build(BuildContext context) {
    return  Scaffold(
      appBar: AppBar(
        title: const Text('Minha primeira tela'),
      ),
      body: Column(
        children:  <Widget>[
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Image.network('https://images.pexels.com/photos/8364804/pexels-photo-8364804.jpeg',
              width: 300,
              height: 300,
              fit: BoxFit.cover,
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Image.asset('assets/cao.jpg',
              width: 300,
              height: 300,
              fit: BoxFit.cover,
            ),
          ),
          ElevatedButton(onPressed: 
          (){
            Navigator.push(context, MaterialPageRoute(builder: (context) => const MinhaSegundaTela()));
          }, child: Text("Mudar de Tela")),
        ],
      )
    );
  }
}
```

O que está acontecendo aqui:

- Estamos utilizando o widget `Navigator` para navegar entre as telas. O `Navigator` é um widget que gerencia a pilha de telas do aplicativo. Ele possui vários métodos que permitem navegar entre as telas, como o método `push` que empilha uma nova tela na pilha de telas e o método `pop` que desempilha a tela atual da pilha de telas.
- Estamos utilizando o widget `MaterialPageRoute` para definir a rota da tela. O `MaterialPageRoute` é um widget que define a rota de uma tela. Ele possui várias propriedades que permitem personalizar a rota, como o construtor que recebe uma função que retorna a tela a ser exibida e a propriedade `builder` que recebe uma função que retorna a tela a ser exibida.

Agora conseguimos sair da primeira tela para a segunda! Utilizando o botão de retornar, conseguimos voltar para a primeira tela. 

### Adicionando um campo de texto e um botão de envio de requisição

Pessoal aqui vou colocar um pouco de código para trabalhar com dois pontos na segunda tela:
- Adicionar um campo de texto para o usuário digitar algo;
- Adicionar um botão para enviar para realizar uma consulta a uma API.

Vamos adicionar um novo widget `TextField` para adicionar um campo de texto na tela. Vamos alterar o código da nossa segunda tela para o seguinte:

```dart
import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';

class MinhaSegundaTela extends StatefulWidget {
  const MinhaSegundaTela({super.key});

  @override
  State<MinhaSegundaTela> createState() => _MinhaSegundaTelaState();
}

class _MinhaSegundaTelaState extends State<MinhaSegundaTela> {
  TextEditingController _controller = TextEditingController();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Minha segunda tela'),
      ),
      body: Column(
        children: <Widget>[
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: TextField(
              controller: _controller,
              decoration: const InputDecoration(
                border: OutlineInputBorder(),
                labelText: 'Digite seu nome',
              ),
            ),
          ),
          ElevatedButton(
            onPressed: () {
              print(_controller.text);
            },
            child: const Text("Consultar"),
          ),
        ],
      ),
    );
  }
}
```

Pessoal tivemos algumas alterações aqui. Vamos avaliar o que fizemos:

- Trocamos o widget `StatelessWidget` para `StatefulWidget`. O `StatefulWidget` é um widget que possui um estado mutável. Ele possui um método `createState` que retorna um objeto que gerencia o estado do widget.
- Adicionamos um novo widget `TextField` para adicionar um campo de texto na tela. O `TextField` é um widget que permite ao usuário digitar texto. Ele possui várias propriedades que permitem personalizar o campo de texto, como o controlador que gerencia o texto digitado e a decoração que define a aparência do campo de texto.
- Adicionamos um novo widget `ElevatedButton` para adicionar um botão na tela. O `ElevatedButton` é um widget que exibe um botão elevado. Ele possui várias propriedades que permitem personalizar o botão, como o texto que é exibido no botão e a ação que é executada quando o botão é pressionado.
- Adicionamos um novo objeto `TextEditingController` para gerenciar o texto digitado no campo de texto. O `TextEditingController` é um objeto que gerencia o texto digitado em um campo de texto. Ele possui vários métodos que permitem acessar e modificar o texto digitado, como o método `text` que retorna o texto digitado e o método `clear` que limpa o texto digitado.

Agora conseguimos digitar algo no campo de texto e ao pressionar o botão, conseguimos ver o que foi digitado no console.

Pessoal, até aqui discutimos alguns conceitos básicos do Flutter. Vamos agora verificar como adicionar novos recursos ao nosso aplicativo. Para realizar requisições HTTP, vamos utilizar a biblioteca [`http`](https://pub.dev/packages/http). Vamos adicionar a biblioteca no nosso arquivo `pubspec.yaml`. Vamos adicionar o seguinte código:

```yaml
# Código anterior omitido
dependencies:
  http: ^1.2.1
# Código posterior omitido
```

Quando realizamos alguma mudança no arquivo `pubspec.yaml`, precisamos rodar o comando `flutter pub get` para que as mudanças sejam aplicadas. O plugin do Flutter no VS Code já faz isso automaticamente para nós. Agora que adicionamos a biblioteca no nosso projeto, vamos alterar o código da nossa segunda tela para realizar uma requisição HTTP.

Vamos iniciar as requisições para a API do [Viacep](https://viacep.com.br/). Vamos enviar um CEP e exibir os dados na tela! Vamos alterar o código para o seguinte:

```dart
import 'package:flutter/material.dart';
import 'dart:convert';
import 'package:http/http.dart' as http;

class MinhaSegundaTela extends StatefulWidget {
  const MinhaSegundaTela({super.key});

  @override
  State<MinhaSegundaTela> createState() => _MinhaSegundaTelaState();
}

class _MinhaSegundaTelaState extends State<MinhaSegundaTela> {
  TextEditingController _controller = TextEditingController();
  String _saida = '';
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Minha segunda tela'),
      ),
      body: Column(
        children: <Widget>[
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: TextField(
              controller: _controller,
              decoration: const InputDecoration(
                border: OutlineInputBorder(),
                labelText: 'Digite seu nome',
              ),
            ),
          ),
          ElevatedButton(
            onPressed: () async {
              var resposta = await http.get(Uri.parse('https://viacep.com.br/ws/${_controller.text}/json/'));
              // Para trabalhar com a saída como JSON/Map
              // var resposta_processada = jsonDecode(resposta.body);
              setState(() {
                _saida = resposta.body;
              });
            },
            child: const Text("Consultar"),
          ),
          Text(_saida),
        ],
      ),
    );
  }
}
```

Pessoal bastante coisa mudou aqui, vamos avaliar algumas delas:
- Adicionamos um novo objeto `String` chamado `_saida` para armazenar a saída da requisição HTTP. O `_saida` é um objeto que armazena a saída da requisição HTTP. Ele é atualizado quando a requisição é concluída e a interface do usuário é atualizada para exibir a saída.
- Adicionamos um novo método `onPressed` para realizar a requisição HTTP. O `onPressed` é um método que é executado quando o botão é pressionado. Ele realiza a requisição HTTP para a API do [Viacep](https://viacep.com.br/) e atualiza a saída da requisição.
- Adicionamos um novo widget `Text` para exibir a saída da requisição. O `Text` é um widget que exibe texto na tela. Ele possui várias propriedades que permitem personalizar o texto, como o estilo do texto e a cor do texto.
- Adicionamos o modificador `async` para o método `onPressed`. O modificador `async` é um modificador que permite que o método seja assíncrono. Ele permite que o método
- Adicionamos o método `await` para a requisição HTTP. O método `await` é um método que espera a conclusão de uma operação assíncrona. Ele permite que o método aguarde a conclusão da requisição HTTP antes de continuar a execução.
- Adicionamos o método `setState` para atualizar a interface do usuário. O método `setState` é um método que atualiza o estado do widget. Ele permite que o widget seja reconstruído com o novo estado e a nova interface do usuário seja exibida.
- Adicionamos o método `jsonDecode` para processar a saída da requisição HTTP. O método `jsonDecode` é um método que converte a saída da requisição HTTP em um objeto JSON/Map. Ele permite que a saída da requisição seja processada e exibida na tela.
- Incluímos as bibliotecas `dart:convert` e `http` para trabalhar com a requisição HTTP. A biblioteca `dart:convert` é uma biblioteca que fornece funções para codificar e decodificar objetos JSON. A biblioteca `http` é uma biblioteca que fornece funções para realizar requisições HTTP.

Gente, falamos de BASTANTE coisa aqui! Vamos agora ver como o Flutter trabalha com o *hot reload* e como podemos utilizar isso para desenvolver nossos aplicativos de forma mais rápida e eficiente.

Boa codificação para vocês! 💻🤖📱

<img src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/cf207f31-d831-4ae4-bddb-3c93f061b34c/d9w7fob-20833e13-52c5-40cb-9222-2d4e68298e59.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2NmMjA3ZjMxLWQ4MzEtNGFlNC1iZGRiLTNjOTNmMDYxYjM0Y1wvZDl3N2ZvYi0yMDgzM2UxMy01MmM1LTQwY2ItOTIyMi0yZDRlNjgyOThlNTkuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.GXBQKmgRiCBhpotUCwTOT37jDSLi_h7GLSK3lRO1jRE" alt="Arquitetura Sincrona" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'24px' }} />
