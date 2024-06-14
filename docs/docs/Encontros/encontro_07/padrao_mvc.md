---
sidebar_position: 3
title: Padrão MVC
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Model View Controller (MVC)

O padrão de arquitetura Model View Controller (MVC) é um padrão de arquitetura de software que separa a aplicação em três componentes principais: Model, View e Controller. Cada um desses componentes tem responsabilidades específicas e interage entre si para criar uma aplicação. Ele foi proposto originalmente por Trygve Reenskaug em 1979 para a linguagem de programação Smalltalk-80. O padrão foi adotado por diversas linguagens de programação e frameworks, como Ruby on Rails, Django, Spring, entre outros.

<img src="https://miro.medium.com/v2/resize:fit:720/format:webp/0*ZqwogJDz1cA1sr-B.png" style={{ display: 'block', marginLeft: 'auto', maxHeight: '50vh', marginRight: 'auto', marginBottom: '24px' }}/>

Os três componentes do sistema (Model-View-Controller) estão interconectados, mas cada um deles com suas responsabilidades claramente definidas. Este padrão é amplamente utilizado no desenvolvimento de interfaces de usuário e aplicações web devido à sua eficiência na organização do código e na separação de responsabilidades, facilitando a manutenção e a escalabilidade. 

1. **Model**: Este componente representa a lógica de negócios e os dados subjacentes. O **model** gerencia o comportamento fundamental dos dados da aplicação, incluindo as regras, os métodos de manipulação de dados e o acesso ao banco de dados. Ele responde às solicitações, geralmente de um controlador, realiza os processamentos necessários e, em seguida, envia os dados de volta, podendo notificar a View de mudanças para atualização da interface.

2. **View**: A View é responsável pela apresentação dos dados ao usuário. Ela apenas exibe os dados que recebe do Model, sem realizar operações ou lógica de negócios. A View também escuta as mudanças nos dados para atualizar sua apresentação, caso algo no Model altere. Frequentemente, em aplicações web, as Views são implementadas como páginas HTML dinâmicas que são geradas e enviadas ao navegador do usuário.

3. **Controller**: O Controller atua como um intermediário entre o Model e a View. Ele recebe as entradas do usuário (por exemplo, cliques de mouse, interações de teclado) e interpreta essas entradas, muitas vezes através da alteração dos estados do Model ou através da solicitação de novas Views que refletem mudanças no Model. O Controller toma decisões, mas não manipula diretamente os dados nem a apresentação final; sua função é coordenar o processo.

A filosofia central do MVC é separar as funções de maneira que cada componente tenha responsabilidades distintas. Essa separação ajuda a manter o código mais organizado, facilita a manutenção e promove a reutilização de código. Além disso, permite que diferentes desenvolvedores trabalhem em componentes diferentes sem interferir uns nos outros, o que é particularmente útil em equipes grandes ou em projetos complexos. Esse padrão pode e muitas vezes é utilizado em conjunto com outros padrões de arquitetura, como o Observer, o Strategy e o Factory.

:::tip[Sugestão de Leitura]

 Pessoal vou deixar aqui uma sugestão de leitura bem interessante sobre a utilização e funcionamento do padrão MVC: [link](https://lucasbaradel.medium.com/mvc-o-que-significa-essa-sigla-e-suas-camadas-142615b78c81).

 E vou deixar mais dois vídeos que podem auxiliar a compreender o conceito:

<iframe style={{ display: 'block', marginLeft: 'auto', marginRight: 'auto', width: '40vw', height: '23vh', marginBottom: '24px' }} src="https://www.youtube.com/embed/ZW2JLtX4Dag?si=btqp6ZM08Esna-Vs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<iframe style={{ display: 'block', marginLeft: 'auto', marginRight: 'auto', width: '40vw', height: '23vh', marginBottom: '24px' }} src="https://www.youtube.com/embed/mMDt9g7bMjk?si=_Vi7WXmSUsNlwqaE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


:::

## Implementando o MVC em nosso aplicativo Hello World

Legal, estudamos até aqui o que é o MVC, como e porque ele foi criado. Mas vamos implementar agora?

<img src="https://d31xsmoz1lk3y3.cloudfront.net/big/2492186.jpg?v=1653857594" style={{ display: 'block', marginLeft: 'auto', maxHeight: '50vh', marginRight: 'auto', marginBottom: '24px' }}/>

Primeiro, vamos criar nossa aplicação. Vamos utilizar o padrão de criação de projetos do Flutter, que é o `flutter create`. Vamos criar um projeto chamado `hello_mvc`:

```bash
flutter create hello_mvc
```

Nesse momento, estamos com nosso código padrão que é apresentado para nós quando criamos um novo projeto com Flutter. Primeiro vamos remover os comentários para avaliarmos cada etapa do nosso código e verificar onde vamos levar cada uma delas.
    
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

Eu deixei apenas um comentário nessa primeira versão que é para possamos sempre lembrar, deixar essa virgula no final de um método, função ou atributo, faz com que o auto-formatador do Dart e do Flutter consiga formatar o código de maneira mais eficiente. Agora vamos analisar as partes do nosso código. Para o padrão MVC, devemos possuir primeiro onde armazenar esses elementos. Logo vamos criar três diretórios dentro da pasta `lib`: `model`, `view` e `controller`.

### Adicionando os diretórios Model, View e Controller

Agora vamos fazer nossa primeira modificação. Nossa aplicação controla o número de vezes que o usuário acionou o botão. Para isso, vamos criar um Model que vai armazenar esse valor. Vamos criar um arquivo chamado `counter_model.dart` dentro da pasta `model`:

```dart
class CounterModel {
  int _counter = 0;

  int get counter => _counter;

  void incrementCounter() {
    _counter++;
  }
}
```

Vamos avaliar essa classe. Ela possui um atributo `_counter` que é privado e um método `incrementCounter` que incrementa o valor do contador. Além disso, temos um getter `counter` que retorna o valor do contador. Vamos parar um momento para lembrar de alguns conceitos de Dart.

O primeiro deles, é que atributos e métodos privados são acessíveis apenas dentro da própria classe. Isso é feito para proteger o estado interno da classe e garantir que ele seja modificado apenas de maneira controlada. O segundo conceito é que Dart possui um sistema de tipagem forte, o que significa que cada variável possui um tipo específico e não pode ser alterado. Isso ajuda a evitar erros de programação e a melhorar a legibilidade do código. Para tornar um atriburo ou método privado, basta adicionar um `_` antes do nome.

Agora vamos avaliar o `getter`. Getters e setters são métodos especiais que permitem acessar e modificar os atributos de uma classe de maneira controlada. Eles são usados para garantir a coesão e o encapsulamento do código, evitando que os atributos sejam acessados diretamente. No caso do `getter`, ele é usado para acessar o valor de um atributo sem permitir que ele seja modificado. Para criar um `getter`, basta adicionar a palavra-chave `get` antes do nome do método. Vale destcar um ponto! Observando o código, é possível notar que o atributo `_counter` é privado, ou seja, ele não pode ser acessado diretamente de fora da classe. Para acessar o valor do contador, é necessário utilizar o getter `counter`. Esse é um exemplo de como o encapsulamento é utilizado para proteger o estado interno da classe e garantir que ele seja modificado apenas de maneira controlada.

Agora, vamos criar nosso controller. Ele será o responsável por gerenciar a interação entre o Model e a View. Vamos criar um arquivo chamado `counter_controller.dart` dentro da pasta `controller`:

```dart
import 'package:hello_mvc/model/counter_model.dart';

class CounterController {
  final CounterModel _model = CounterModel();

  int get counter => _model.counter;

  void incrementCounter() {
    _model.incrementCounter();
  }
}
```

Vamos avaliar essa classe. Ela possui um atributo `_model` do tipo `CounterModel` e dois métodos: `counter` e `incrementCounter`. O método `counter` retorna o valor do contador do Model, enquanto o método `incrementCounter` incrementa o contador. Temos diversos pontos de implementação similares ao Model, mas com algumas diferenças. A primeira é que o atributo `_model` é do tipo `CounterModel`, ou seja, ele armazena uma instância da classe `CounterModel`. Isso é feito para permitir que o Controller acesse e modifique o estado do Model. A segunda é que o método `counter` retorna o valor do contador do Model. Isso é feito para permitir que a View acesse o valor do contador sem modificar o estado interno do Model. A terceira é que o método `incrementCounter` chama o método `incrementCounter` do Model. Isso é feito para permitir que o Controller modifique o estado do Model de maneira controlada. Cabe destacar aqui que o nosso controller não muda o valor do contador diretamente, ele chama o método `incrementCounter` do Model para fazer isso. Isso é feito para garantir que a lógica de negócios seja centralizada no Model e que o Controller seja responsável apenas por coordenar a interação entre o Model e a View.

Agore vamos criar nossa View. Ela será responsável por exibir o valor do contador e permitir que o usuário o incremente. Vamos criar um arquivo chamado `counter_view.dart` dentro da pasta `view`:

```dart
import 'package:flutter/material.dart';
import 'package:hello_mvc/controller/counter_controller.dart';

class CounterView extends StatelessWidget {
  final CounterController _controller = CounterController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Flutter Demo Home Page'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            const Text(
              'You have pushed the button this many times:',
            ),
            Text(
              '${_controller.counter}',
              style: Theme.of(context).textTheme.headline4,
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          _controller.incrementCounter();
        },
        tooltip: 'Increment',
        child: const Icon(Icons.add),
      ),
    );
  }
}
```

Vamos analisar este código até aqui. A nossa view possui uma instância de um controller. É essa instância que vai permitir que a view acesse o valor do contador e o incremente. A view é responsável pelas interações com o contador e o usuário. Para isso, ela utiliza um Scaffold com um AppBar e um FloatingActionButton. O valor do contador é exibido em um Text com o estilo headline4. O FloatingActionButton chama o método incrementCounter do controller quando é pressionado. Isso é feito para garantir que a lógica de negócios seja centralizada no Model e que o Controller seja responsável apenas por coordenar a interação entre o Model e a View.

Vamos modificar agora nosso `main.dart` para utilizar a nossa View. Vamos importar o arquivo `counter_view.dart` e modificar o método `build` da classe `MyApp` para retornar a nossa View:

```dart
import 'package:flutter/material.dart';
import 'package:hello_mvc/view/counter_view.dart';

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
     home: CounterView(),
    );
  }
}

```

Agora, vamos rodar nossa aplicação e ver o resultado. Vamos rodar o comando `flutter run` no terminal e ver o que acontece. 

```bash
flutter run
```

:::tip[Vamos rodar nossa aplicação diversas vezes]

Pessoal, durante esse processo de refatoração, vamos rodar nossa aplicação diversas vezes. ë importante que ela mantenha um comportamento esperado. Vamos rodar nossa aplicação diversas vezes para garantir que ela está funcionando corretamente com as modificações que implementamos.

:::

Com nossa aplicação sendo executada, teremos a seguinte saída:

<img src={useBaseUrl("/img/flutter_mvc/app_rodando_primeira_refatorada.png")} style={{ display: 'block', marginLeft: 'auto', maxHeight: '50vh', marginRight: 'auto', marginBottom: '24px' }}/>

### Depurando a aplicação

Tudo funcionando de forma maravilhosa não? Na verdade não. Ao acionar o botão, o valor do contador não é incrementado. Mas será que nosso código efetivamente está mudando o valor do contador? Vamos verificar!

Vamos adicionar um `breakpoint` no método `incrementCounter` do nosso Model e rodar novamente nossa aplicação. No VS Code, basta clicar na linha que deseja adicionar o `breakpoint` e pressionar `F9`. Vamos rodar nossa aplicação novamente e verificar o que acontece.

<img src={useBaseUrl("/img/flutter_mvc/debuging.png")} style={{ display: 'block', marginLeft: 'auto', maxHeight: '50vh', marginRight: 'auto', marginBottom: '24px' }}/>

:::tip[Depurando nossa aplicação]

Em diversos momentos, vai ser necessário depurar nossa aplicação para verificar o comportamento de nosso código. Quando utilizamos o depurador, estamos interagindo com o código de maneira mais detalhada, permitindo que possamos verificar o estado das variáveis, a execução dos métodos e a interação entre os diferentes componentes da aplicação. Isso é particularmente útil para identificar e corrigir erros de programação, entender o fluxo de execução do código e testar diferentes cenários de uso.

A utilização do depurador fica mais simples com a repetição de uso. Vamos utilizar o depurador diversas vezes para verificar o comportamento de nosso código e garantir que ele está funcionando corretamente.

<img src="https://s2-techtudo.glbimg.com/RSnQ9K4uQ4Qc5Po18UkFdyn2lO4=/0x0:968x542/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_08fbf48bc0524877943fe86e43087e7a/internal_photos/bs/2019/3/1/p6RbwXTR2sEiLsscA5MA/captura-de-tela-2019-05-08-as-11.58.45.png
" style={{ display: 'block', marginLeft: 'auto', maxHeight: '50vh', marginRight: 'auto', marginBottom: '24px' }}/>

:::

Mas o que será que aconteceu que não conseguimos fazer a alteração então?

> Murilo, você comentou que widgets do tipo `Stateless` não podem ser alterados, certo? E o que acontece com o nosso `CounterView`? Ele é um widget do tipo `Stateless` ou `Stateful`?

Ahhh, muito bem lembrado! O nosso `CounterView` é um widget do tipo `Stateless`. Isso significa que ele não pode ser alterado após ser construído. Para resolver esse problema, vamos transformar o nosso `CounterView` em um widget do tipo `Stateful`. Vamos modificar o arquivo `counter_view.dart` para que ele seja um widget do tipo `Stateful`:

```dart
import 'package:flutter/material.dart';
import 'package:hello_mvc/controller/counter_controller.dart';

class CounterView extends StatefulWidget {
  @override
  _CounterViewState createState() => _CounterViewState();
}

class _CounterViewState extends State<CounterView> {
  final CounterController _controller = CounterController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Flutter Demo Home Page'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            const Text(
              'You have pushed the button this many times:',
            ),
            Text(
              '${_controller.counter}',
              style: Theme.of(context).textTheme.headline4,
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          setState(() {
            _controller.incrementCounter();
          });
        },
        tooltip: 'Increment',
        child: const Icon(Icons.add),
      ),
    );
  }
}
```

Vamos avaliar o código. O nosso `CounterView` agora é um widget do tipo `Stateful`. Isso significa que, podemos notificar que ele sofreu uma alteração para forçar sua nova renderização na tela. Para isso, ele utiliza um método `setState` que atualiza o estado do widget e chama o método `incrementCounter` do controller. Isso é feito para garantir que o valor do contador seja incrementado corretamente e que a interface seja atualizada de acordo. Vamos rodar nossa aplicação novamente e verificar o resultado.

Agora nossa aplicação funciona como esperado!!

### Continuando com a refatoração

Pessoal, vamos continuar só mais um pouco nossa refatoração aqui, acredito que ainda temos alguns pontos de melhoria para fazer. Primeiro deles, vamos criar mais uma diretório em `lib` chamado `widgets`. Ele vai ser responsável por armazenar os widgets que vamos utilizar em nossa aplicação. Qual a vantagem disso? A vantagem é que podemos reutilizar esses widgets em diferentes partes de nossa aplicação, facilitando a manutenção e a escalabilidade do código. 

Vamos avaliar a nossa classe `CounterView`. Ela possui um `Scaffold` com um `AppBar`, um `Text` e um `FloatingActionButton`. Vamos criar um widget para representar o `FloatingActionButton`. Vamos criar um arquivo chamado `counter_floating_action_button.dart` dentro da pasta `widgets`:

```dart
import 'package:flutter/material.dart';

class CounterFloatingActionButton extends StatelessWidget {
  final void Function() action;
  final String tooltip;
  final Icon icon;

  const CounterFloatingActionButton({Key? key, required this.action, this.tooltip = "Incremento", this.icon = const Icon(Icons.add)}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return FloatingActionButton(
      onPressed: action,
      tooltip: tooltip,
      child: icon,
    );
  }
}
```

Avaliando o código acima, nós temos:

1. Um widget chamado `CounterFloatingActionButton` que é do tipo `Stateless`. Ele possui três atributos: `action`, `tooltip` e `icon`. 
2. O atributo `action` é uma função que será chamada quando o botão for pressionado. 
3. O atributo `tooltip` é uma string que será exibida quando o usuário passar o mouse sobre o botão. 
4. O atributo `icon` é um ícone que será exibido no botão. 
5. O construtor do widget recebe esses três atributos e os utiliza para criar um `FloatingActionButton`. Isso é feito para permitir que o botão seja personalizado de acordo com as necessidades da aplicação.
6. O atributo `key` é utilizado para identificar o widget de maneira única. Ele é opcional e pode ser utilizado para facilitar a depuração e a manutenção do código.
7. O atribuito `action` é obrigatório e não pode ser nulo. Já os atributos `tooltip` e `icon` são opcionais e possuem valores padrão. Se nenhum valor for enviado, fica valendo o valor padrão.


Vamos alterar nosso código da `CounterView` para utilizar esse novo widget:

```dart
import 'package:flutter/material.dart';
import 'package:hello_mvc/controller/counter_controller.dart';
import 'package:hello_mvc/widgets/couunter_floating_action_button.dart';

class CounterView extends StatefulWidget {
  @override
  State<CounterView> createState() => _CounterViewState();
}

class _CounterViewState extends State<CounterView> {
  final CounterController _controller = CounterController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Flutter Demo Home Page'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            const Text(
              'You have pushed the button this many times:',
            ),
            Text(
              '${_controller.counter}',
              style: Theme.of(context).textTheme.headline4,
            ),
          ],
        ),
      ),
      floatingActionButton: CounterFloatingActionButton(
        action: (){
          setState(() {
            _controller.incrementCounter();
          });
        },
      )
    );
  }
}

```

Beleza, agora vamos ver se temos mais alguma oportunidade de ejetar widgets para fora de nossa `CounterView`. Vamos avaliar o nosso `Text` que exibe o valor do contador. Vamos criar um widget para representar esse `Text`. Vamos criar um arquivo chamado `counter_text.dart` dentro da pasta `widgets`:

```dart
import 'package:flutter/material.dart';

class CounterText extends StatelessWidget {
  final String text;
  final bool isBigger;

  const CounterText({Key? key, required this.text, this.isBigger = false}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Text(
      text,
      style: isBigger ? Theme.of(context).textTheme.headline4 : Theme.of(context).textTheme.headline5,
    );
  }
}
```

E ajustando o nosso `CounterView` para utilizar esse novo widget:

```dart
import 'package:flutter/material.dart';
import 'package:hello_mvc/controller/counter_controller.dart';
import 'package:hello_mvc/widgets/counter_floating_action_button.dart';
import 'package:hello_mvc/widgets/counter_text.dart';

class CounterView extends StatefulWidget {
  @override
  State<CounterView> createState() => _CounterViewState();
}

class _CounterViewState extends State<CounterView> {
  final CounterController _controller = CounterController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Flutter Demo Home Page'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            const CounterText(text: "Numero de Vezes que Foi Acionado"),
            CounterText(text: '${_controller.counter}', isBigger: true),
          ],
        ),
      ),
      floatingActionButton: CounterFloatingActionButton(
        action: (){
          setState(() {
            _controller.incrementCounter();
          });
        },
      )
    );
  }
}

```

Pessoal vou parar por aqui essa implementação, mas quero que vocês observem o que estamos fazendo. Estamos separando as responsabilidades de cada componente do MVC e criando widgets para representar cada parte da nossa aplicação. Isso é feito para facilitar a manutenção e a escalabilidade do código, permitindo que diferentes partes da aplicação sejam modificadas e reutilizadas de maneira independente. 

Podemos continuar com essa separação e criar o pacote `strings` para armazenar as strings que são exibidas na interface, o pacote `themes` para armazenar os temas da aplicação, o pacote `utils` para armazenar funções e classes utilitárias, entre outros. A ideia é que cada parte da aplicação seja organizada de maneira lógica e coesa, facilitando a compreensão e a manutenção do código.

Vamos tentar utilizar os conceitos de arquitetura MVC nos próximos códigos que vamos desenvolver.

Lembrem-se de antes de enviar código Flutter para os repositórios, utilizar a ferramenta `flutter clean` para limpar o cache e garantir que o código está sendo compilado corretamente.

