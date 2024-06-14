---
sidebar_position: 5
title: Conversando com o Backend
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Comunicação com o Backend

Pessoal para essa etapa do nosso projeto, vamos trabalhar com a comunicação entre o aplicativo e o backend. Essa implementação precisa do uso de uma biblioteca chamada `http` que é responsável por fazer requisições HTTP. Mas não apenas isso, também vamos precisar do nosso backend funcionando. Pode ser a `versão 1` do nosso backend, que é a mais simples e que já está disponível no repositório do projeto.

:::note[Checkpoint do Aplicativo]

Pessoal existem duas versões do aplicativo no repositório. Durante o encontro, vamos continuar com a versão `checkpoint` que é a versão do aplicativo desenvolvida até esse momento.

:::

## Requisições HTTP

Para fazer requisições HTTP no Flutter, vamos utilizar a biblioteca `http`. Para adicionar essa biblioteca ao nosso projeto, vamos adicionar a seguinte dependência no arquivo `pubspec.yaml`:

```yaml
dependencies:
  flutter:
    sdk: flutter
  http: ^1.2.1
```
Agora vamos fazer uma requisição HTTP para o nosso backend. Para isso, vamos configurar a ação do botão '😁' para que ele faça a operação do botão `=`, mas enviando ela para o servidor. Primeiro vamos fazer com que nosso aplicativo envie os dados para o nosso servidor e receba a resposta dele para ser exibida na tela. Nesse primeiro momento, o endereço do servidor estará fixo no nosso aplicativo, vamos ajustar isso ainda nessa interação.

Vamos alterar o arquivo `minha_calculadora.dart` para que ele faça a requisição HTTP. Primeiro vamos importar a biblioteca `http`:

```dart
import 'dart:convert';

import 'package:calculadora_app/display.dart';
import 'package:calculadora_app/keypad.dart';
import 'package:flutter/material.dart';
import 'package:math_expressions/math_expressions.dart';
import 'package:http/http.dart' as http;

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

  Future<String> avaliarExpressaoServidor() async{
    String finaluserinput = userData;
    finaluserinput = finaluserinput.replaceAll('x', '*');
    print(jsonEncode({"expressao":finaluserinput}));
    // Realiza a requisição utilizando o http
    // O servidor deve estar rodando para que a requisição funcione
    var resultado = await http.post(Uri.parse("http://192.168.0.248:8000/evaluate"), headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
    }, body: jsonEncode(<String, String>{"expressao":finaluserinput}));
    print(resultado.body);
    var saida = jsonDecode(resultado.body) as Map;
    return saida["resultado"].toString();
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
    {'text': '😁', 'backcolor': Colors.blue, 'textcolor': Colors.white, "action":()async{setResult(await avaliarExpressaoServidor()); setUserData("0");}},
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

Vamos avaliar o que está acontecendo aqui:

1. Adicionamos a importação da biblioteca `http` no início do arquivo.
2. Adicionamos um método chamado `avaliarExpressaoServidor` que é responsável por fazer a requisição HTTP para o nosso servidor. Esse método é assíncrono, ou seja, ele não trava a execução do aplicativo enquanto espera a resposta do servidor.
3. Adicionamos ao botão '😁' na lista de botões, a responsabilidade por chamar o método `avaliarExpressaoServidor` quando ele é pressionado.
4. Adicionamos a importação da biblioteca `dart:convert` para que possamos usar o método `jsonEncode` e `jsonDecode` para transformar os dados em JSON.

Vamos avaliar em especial o método `avaliarExpressaoServidor`:

```dart
Future<String> avaliarExpressaoServidor() async{
    String finaluserinput = userData;
    finaluserinput = finaluserinput.replaceAll('x', '*');
    print(jsonEncode({"expressao":finaluserinput}));
    // Realiza a requisição utilizando o http
    // O servidor deve estar rodando para que a requisição funcione
    var resultado = await http.post(Uri.parse("http://192.168.0.248:8000/evaluate"), headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
    }, body: jsonEncode(<String, String>{"expressao":finaluserinput}));
    print(resultado.body);
    var saida = jsonDecode(resultado.body) as Map;
    return saida["resultado"].toString();
  }
```

1. Primeiro, pegamos a expressão que o usuário digitou e substituímos o caractere `x` por `*` para que a expressão seja válida para o servidor.
2. Fazemos um print na console, apenas para verificarmos como essa requisição estará recebendo seus dados.
3. Fazemos a requisição HTTP para o servidor, passando a expressão digitada pelo usuário no corpo da requisição. Reparem que aqui, configuramos o endereço do servidor como `http://192.168.0.248:8000/evaluate`. Este endereço é o IP do meu computador em minha rede local. Por default, o emulador não consegue acessar o `localhost` da máquina que está rodando o emulador, por isso, precisamos usar o IP da máquina. Se você estiver rodando o servidor em outra máquina, você precisa substituir esse endereço pelo IP da máquina que está rodando o servidor. 
4. Ajustamos os `headers` da requisição para que o servidor saiba que estamos enviando um JSON. Observe que, no Dart, precisamos definir os tipos dos dados que estamos enviando, por isso, usamos `<String, String>`.
5. Assim como no `header`, precisamos enviar o corpo da requisição como um JSON, por isso, usamos o método `jsonEncode` para transformar o mapa em JSON.
6. Aguardamos o resultado da requisição e fazemos um print no console para verificarmos o que o servidor nos respondeu.
7. Transformamos o resultado da requisição em um mapa e retornamos o valor da chave `resultado` como uma `String`.

Pessoal, reparem que até aqui temos vários pontos que podemos melhorar nossa aplicação. E já vamos implementar algumas destas melhorias. Vamos começar com o endereço do servidor.

## Configurando o Endereço do Servidor

Para configurar o endereço do servidor, vamos criar uma outra tela. Essa tela vai ser responsável por receber o endereço do servidor e salvar ele no aplicativo. Essa configuração ficará guardada no nosso aplicativo, mesmo quando ele for fechado. Para isso, vamos fazer uso do `SharedPreferences`. Vamos adicionar a dependência do `shared_preferences` no nosso arquivo `pubspec.yaml`:

O `shared_preferences` é uma biblioteca que permite salvar dados no dispositivo do usuário. Ela é bastante interessante para salvar configurações do aplicativo, como o endereço do servidor. Dentro de cada sistema operacional, ela salva esses dados de uma forma diferente, mas para o desenvolvedor, é transparente. Para saber mais sobre o `shared_preferences`, você pode acessar a [documentação oficial](https://docs.flutter.dev/cookbook/persistence/key-value).

```yaml
flutter pub add shared_preferences
```

Agora já conseguimos utilizar o `shared_preferences` no nosso aplicativo. Vamos criar uma nova tela chamada `ConfiguracaoServidor` que vai ser responsável por receber o endereço do servidor. Vamos criar um novo arquivo chamado `configuracao_servidor.dart`:

```dart
// configuracao_servidor.dart
import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';

class configuracao_servidor extends StatefulWidget {
  const configuracao_servidor({super.key});

  @override
  State<configuracao_servidor> createState() => _configuracao_servidorState();
}

class _configuracao_servidorState extends State<configuracao_servidor> {
  final TextEditingController _controller = TextEditingController();
  String _url = '';

  Future<void> recuperarUrl() async{
    // Recupera a instância do SharedPreferences
    final prefs = await SharedPreferences.getInstance();
    // Recupera o valor da chave 'serverUrl'
    _url = prefs.getString('serverUrl') ?? '';
    setState(() {
      _controller.text = _url;
    });
  }

  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    recuperarUrl();
  }
  @override
  Widget build(BuildContext context) {
    return  Scaffold(
      appBar: AppBar(
        title: const Text('Configuração do Servidor'),
      ),
      body: Container(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            TextField(
              controller: _controller,
              decoration: const InputDecoration(
                labelText: 'URL do Servidor',
              ),
            ),
            ElevatedButton(
              onPressed: () async {
                // Salva a URL no SharedPreferences
                final prefs = await SharedPreferences.getInstance();
                _url = _controller.text;
                prefs.setString('serverUrl', _url);
                // Exibe um SnackBar
                ScaffoldMessenger.of(context).showSnackBar(
                  const SnackBar(
                    content: Text('URL do servidor salva com sucesso!'),
                  ),
                );
              },
              child: const Text('Salvar'),
            ),
          ],
        ),
      )
    );
  }
}
```

Vamos observar o que foi feito aqui:

1. Importamos a biblioteca `shared_preferences` no início do arquivo.
2. Criamos uma classe chamada `configuracao_servidor` que é um `StatefulWidget`.
3. Criamos um `TextEditingController` chamado `_controller` que vai ser responsável por controlar o campo de texto que vai receber o endereço do servidor.
4. Criamos uma variável chamada `_url` que vai guardar o endereço do servidor.
5. Criamos o método `recuperarUrl` que é responsável por recuperar o endereço do servidor salvo no `SharedPreferences`.
6. No método `initState`, chamamos o método `recuperarUrl` para recuperar o endereço do servidor salvo no `SharedPreferences`.
7. No método `build`, criamos um `Scaffold` que é a estrutura da tela.
8. Adicionamos um `TextField` que é o campo de texto que vai receber o endereço do servidor.
9. Adicionamos um `ElevatedButton` que é o botão que vai salvar o endereço do servidor no `SharedPreferences`.
10. No `onPressed` do botão, salvamos o endereço do servidor no `SharedPreferences` e exibimos um `SnackBar` informando que o endereço foi salvo com sucesso.

Agora temos dois desafios:

1. Ligar essa configuração com nossa aplicação;
2. Fazer com que o endereço do servidor seja dinâmico.

Para implementar ambos, vamos modificar o código presente no arquivo `minha_calculadora.dart`:

```dart
import 'dart:convert';

import 'package:calculadora_app/configuracao_servidor.dart';
import 'package:calculadora_app/display.dart';
import 'package:calculadora_app/keypad.dart';
import 'package:flutter/material.dart';
import 'package:math_expressions/math_expressions.dart';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';

class MinhaCalculadora extends StatefulWidget {
  const MinhaCalculadora({super.key});

  @override
  State<MinhaCalculadora> createState() => _MinhaCalculadoraState();
}

class _MinhaCalculadoraState extends State<MinhaCalculadora> {
  String userData = '0';
  String result = "";
  String serverUrl = '';

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

  Future<void> getServerUrl() async{
    // Recupera a instância do SharedPreferences
    final prefs = await SharedPreferences.getInstance();
    // Recupera o valor da chave 'serverUrl'
    serverUrl = prefs.getString('serverUrl') ?? '';
  }

  void showSnackBar(String message){
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text(message),
      ),
    );
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

  Future<String> avaliarExpressaoServidor() async{
    String finaluserinput = userData;
    finaluserinput = finaluserinput.replaceAll('x', '*');
    print(jsonEncode({"expressao":finaluserinput}));
    // Realiza a requisição utilizando o http
    // Pega a URL do servidor do SharedPreferences
    await getServerUrl();
    if (serverUrl == ''){
      showSnackBar('URL do servidor não configurada!');
      return '';
    }
    // O servidor deve estar rodando para que a requisição funcione
    var resultado = await http.post(Uri.parse(serverUrl), headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
    }, body: jsonEncode(<String, String>{"expressao":finaluserinput}));
    print(resultado.body);
    var saida = jsonDecode(resultado.body) as Map;
    return saida["resultado"].toString();
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
    {'text': '⚙️', 'backcolor': Colors.blue, 'textcolor': Colors.white, "action":(){
      Navigator.push(context, MaterialPageRoute(builder:(context) => const configuracao_servidor()));
    }},
    {'text': '😁', 'backcolor': Colors.blue, 'textcolor': Colors.white, "action":()async{setResult(await avaliarExpressaoServidor()); setUserData("0");}},
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

Pontos que mais merecem destaque:

1. Adicionamos a importação da tela `configuracao_servidor.dart` no início do arquivo.
2. Adicionamos a variável `serverUrl` que vai guardar o endereço do servidor.
3. Adicionamos o método `getServerUrl` que é responsável por recuperar o endereço do servidor salvo no `SharedPreferences`. Esse método é assíncrono, pois ele precisa aguardar a resposta do `SharedPreferences`.
4. Adicionamos o método `showSnackBar` que é responsável por exibir um `SnackBar` na tela. Esse método é chamado quando o endereço do servidor não está configurado.
5. No método `avaliarExpressaoServidor`, chamamos o método `getServerUrl` para recuperar o endereço do servidor. Se o endereço não estiver configurado, exibimos um `SnackBar` informando ao usuário que o endereço do servidor não está configurado.
6. No botão de configuração, adicionamos a ação de navegar para a tela de configuração do servidor. Para isso, usamos o método `Navigator.push` que é responsável por navegar para outra tela. Nesse caso, estamos navegando para a tela `configuracao_servidor`.


Pessoal, dessa forma, conseguimos configurar nossa aplicação para que ela consiga buscar de forma dinâmica o endereço do nosso servidor. Não apenas isso, adicionamos a nossa aplicação a capacidade de armaezar esse endereço, mesmo quando o aplicativo for fechado. Isso é muito importante para que o usuário não precise configurar o endereço do servidor toda vez que ele abrir o aplicativo.

Testem as aplicações de vocês, verifiquem cada passo e vejam se tudo está funcionando corretamente. Se tiverem dúvidas, não deixem de perguntar. Vamos fazer algumas consolidações em nossa próximas instrução! Certifiquem-se de que todo o conteúdo foi compreendido e que a aplicação está funcionando corretamente. Até a próxima instrução!