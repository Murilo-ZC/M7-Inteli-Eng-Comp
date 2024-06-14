---
sidebar_position: 2
title: Criando o Projeto
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Criando o Projeto

Aqui voc6es já conseguem ver que o projeto pode ser criado utilizando a extensão do VS Code ou ainda utilizando o terminal. Vamos utilizar o terminal para criar o projeto.

```bash
flutter create calculadora_app
```

Pronto, agora temos o diretório da nossa solução. Todo o projeto Flutter depende da sua estrutura de diretórios e arquivos. É importante que ela seja mantida para que o Flutter consiga compilar e rodar o projeto. 

:::danger[CUIDADO COM O GITIGNORE]

O arquivo `.gitignore` é um arquivo que contém as pastas e arquivos que não devem ser versionados no Git. Ele é muito importante para manter o repositório limpo e organizado. Lembrando que o Flutter cria um arquivo `.gitignore` por padrão, então não se preocupe com isso. Agora se já existe um arquivo `.gitignore` no seu projeto, verifique se ele contém as pastas e arquivos do Flutter. Se por acaso o diretório `lib` estiver lá, remova-o.

:::

Temos nesse momento nossa aplicação padrão que o Flutter nos entrega. Vamos modificar o arquivo `main.dart` para que ele fique da seguinte forma:

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
      title: 'Calculadora Flutter',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: const MinhaCalculadora(),
    );
  }
}


class MinhaCalculadora extends StatelessWidget {
  const MinhaCalculadora({super.key});

  @override
  Widget build(BuildContext context) {
    return const Placeholder();
  }
}

```

Devemos ter a aplicação rodando e exeibindo apenas uma tela com um `Placeholder`. Agora vamos modificar nossa aplicação para adicionar uma carinha da nossa calculadora. Vamos implementar primeiro o seguinte layout.

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
  final TextEditingController _valor1 = TextEditingController();
  final TextEditingController _valor2 = TextEditingController();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Calculadora Flutter'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Padding(
              padding: const EdgeInsets.symmetric(horizontal:8.0),
              child: TextField(
                controller: _valor1,
                keyboardType: TextInputType.number,
                decoration: const InputDecoration(
                  border: OutlineInputBorder(),
                  labelText: 'Valor 1',
                ),
              ),
            ),
            Padding(
              padding: const EdgeInsets.symmetric(horizontal:8.0, vertical: 8.0),
              child: TextField(
                controller: _valor2,
                keyboardType: TextInputType.number,
                decoration: const InputDecoration(
                  border: OutlineInputBorder(),
                  labelText: 'Valor 2',
                ),
              ),
            ),
            ElevatedButton(
              onPressed: () {
                var valor1 = double.parse(_valor1.text);
                var valor2 = double.parse(_valor2.text);
                var resultado = valor1 + valor2;
                showDialog(
                  context: context,
                  builder: (context) {
                    return AlertDialog(
                      content: Text('Resultado: $resultado'),
                    );
                  },
                );
              },
              child: const Text('Somar'),
            ),
          ],
        ),
      ),
    );
  }
}

```

Uoooouuu, muita coisa mudou não? Vamos ver cada um destes pontos e ver o que está acontecendo agora. Primeiro, nossa calculadora deve ter ficado com esse formato:

<img src={useBaseUrl("/img/calculadora-flutter/calc_01.png")} alt="Arquitetura Sincrona" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'24px' }} />

Legal, agora vamos compreender o que aconteceu. Primeiro, nosso `MinhaCalculadora` agora é um `StatefulWidget`. Isso porque precisamos de um estado para armazenar os valores dos campos de texto. Para isso, criamos dois `TextEditingController` que são responsáveis por armazenar os valores dos campos de texto. Como uma vez instanciados, essa referência deles não é alterada, podemos criar eles como atributos do tipo `final`.

:::tip[TextEditingController]

São controladores de texto que são utilizados para controlar o conteúdo de um campo de texto. Eles são responsáveis por armazenar o valor do campo de texto e também por atualizar o campo de texto com o valor que ele armazena. Como eles precisam ser atualizados, eles são armazenados no estado do widget.

:::

Depois, temos o método `build` que é responsável por construir a interface do widget. Nesse método, temos um `Scaffold` que é um widget que nos permite criar uma tela com uma barra de aplicativo e um corpo. No corpo, temos um `Center` que centraliza os elementos filhos. E dentro do `Center`, temos um `Column` que é um widget que nos permite empilhar os elementos filhos verticalmente.

Até aqui, sem muita diferença do que já vinhamos fazendo. Vamos só compreender agora como alocamos esses elementos filhos dentro desta coluna. Nosso objetivo é possuir três elementos dentro desta coluna:

- Um campo de texto para o valor 1
- Um campo de texto para o valor 2
- Um botão para somar os valores

Legal, agora se apenas adicionar os elementos, eles serão dispostos exatamente nesse formato. Para evitar que o campo de texto invada o botão e as laterais da nossa aplicação, vamos utilizar o `Padding` para adicionar um espaçamento entre os elementos.

:::tip[Padding]

O `Padding` é um widget que adiciona um espaçamento ao redor de um widget filho. Ele é muito útil para adicionar um espaçamento entre os elementos da interface. Ele pode ser configurado de diversas formas distintas, como espaçamento horizontal, vertical, entre outros. Maiores informações podem ser encontradas [aqui](https://api.flutter.dev/flutter/widgets/Padding-class.html).

:::

:::warning[A importância da documentação]

Pessoal, denovo acredito que sim vocês já estão familiarizados com esse conceito. Mas acredito que nunca é demais reforçar a importância de investir "horas sentado na frente do computador, testando/estudando/implementando". Pessoal o tempo é um fator extremamente importante durante o processo de aprendizado. Então, não tenham medo de investir tempo na documentação do Flutter. Ela é muito rica e pode te ajudar a compreender melhor os conceitos e a implementar as soluções de forma mais eficiente.

> Mas Murilo, não é para utilizar as ferramentas de geração de código?

Pessoal, essa resposta é mais longa que apenas um comentário aqui. Porque ela é um sim e não na minha opinião. Acredito que sim, voc6es devem utilizar essas ferramentas de geração de código. Mas, não, ela não pode ser a fonte de verdade (do inglês `source off truth`) para a tomada de decisões. Se você utilizou a ferramenta para gerar um código, você deve compreender o que foi gerado e como ele funciona. Busque na documentação o que foi gerado e tente compreender como ele funciona. Altere o código, quebre ele e conserte depois. Isso é muito importante para o aprendizado.

Recomendo fortemente que vocês assistam o vídeo abaixo:

<iframe width="560" height="315" src="https://www.youtube.com/embed/DZkbDCSdC1Q?si=kNGWOSOXX2XZshDj" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

:::

Agora, temos nossos campos de texto, os `TextFields`. Eles são muito úteis para capturar a entrada do usuário. Eles possuem diversos atributos que podem ser configurados, como o `controller` que é o controlador de texto que vimos anteriormente, o `keyboardType` que é o tipo de teclado que será exibido para o usuário, o `decoration` que é a decoração do campo de texto, entre outros.

Além dele, temos nosso botão de somar. Ele é um `ElevatedButton` que é um botão que possui uma elevação. Ele possui um atributo `onPressed` que é uma função que será executada quando o botão for pressionado e um atributo `child` que é o widget que será exibido dentro do botão. Repare que em nossa função, o que estamos fazendo é converter os valores dos campos de texto para `double`, somar eles e exibir o resultado em um `AlertDialog`.

Pessoal no nosso aplicativo, quando pressionamos o botão de somar, ele exibe um `AlertDialog` com o resultado da soma dos valores dos campos de texto. Contudo, apenas se o usuário formatou da maneira correta os valores. Se ele colocar um valor que não é um número, o aplicativo irá quebrar. Isso é um problema que precisamos resolver. Vamos ver como podemos resolver isso.

```dart
//Código anterior suprimido

ElevatedButton(
              onPressed: () {
                try {
                  var valor1 = double.parse(_valor1.text);
                  var valor2 = double.parse(_valor2.text);
                  var resultado = valor1 + valor2;
                  showDialog(
                    context: context,
                    builder: (context) {
                      return AlertDialog(
                        content: Text('Resultado: $resultado'),
                      );
                    },
                  );
                } on Exception catch (e) {
                  showDialog(
                    context: context,
                    builder: (context) {
                      return AlertDialog(
                        content: Text('Algo deu errado: $e'),
                      );
                    },
                  );
                }
              },
              child: const Text('Somar'),
            ),

//Código posterior suprimido
```
O que fizemos aqui foi adicionar um bloco `try-catch` para capturar a exceção que é lançada quando o valor não pode ser convertido para `double`. Se a exceção for lançada, exibimos um `AlertDialog` com a mensagem de erro. Isso é muito importante para garantir que o aplicativo não quebre quando o usuário inserir um valor inválido.

Pessoal até aqui temos uma calculadora básica que soma dois valores. Como desafio, sugiro que vocês tentem implementar as demais operações (subtração, multiplicação e divisão). Agora vamos alterar o layout da nossa calculadora para que ela fique mais similar as calculadoras que temos em nossos smartphones.
