---
sidebar_position: 3
title: Aplicação de Estudo
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Construção da Aplicação para Análise

Pessoal, vamos construir aqui a base para nossa aplicação de estudo. 
Nossa aplicação vai possuir duas funcionalidades principais:
- Um agendador de notificações locais;
- Um removedor de fundo em imagens.

Essas duas funcionalidades serão implementadas ao longo do material e do encontro.
O projeto será implementado utilizando a estrutura MVC (Model-View-Controller) e o padrão de projeto Observer.

## Criando o Projeto

Vamos criar um projeto Flutter utilizando o comando abaixo:

```bash
flutter create --org com.adalove --project-name encontro_08 .
```

Repare que aqui criamos nosso projeto de uma forma diferente do que fizemos até aqui. Nós definimos o nome do projeto como `encontro_08` e a organização como `com.adalove`. Isso é importante para que possamos manter a organização dos nossos projetos. Existem outros parâmetros que podem ser passados para o comando `flutter create`, mas esses são os mais importantes para nós. Para conhecer mais sobre eles, acesse a [documentação oficial](https://docs.flutter.dev/reference/flutter-cli).

Importante, quando utilizamos a anotação `.` no final do comando, estamos dizendo para o Flutter criar o projeto no diretório atual. Isso é importante!!

## Estrutura do Projeto

Vamos criar primeiro um diretório para armazenar os `assets` da nossa aplicação. Não esqueça de criar ele na raiz do projeto e adicionar ele no arquivo `pubspec.yaml`:

```yaml
flutter:
  assets:
    - assets/
```

Agora vamos criar no nosso diretório `lib` os diretórios `models`, `views` e `controllers`. Dentro do diretório `views`, vamos construir nosso widget de home.

## Home

Nossa página `Home` vai ser responsável por exibir as funcionalidades da nossa aplicação. Vamos criar um widget que vai exibir um botão para acessar a funcionalidade de agendamento de notificações locais e um botão para acessar a funcionalidade de remoção de fundo de imagens.

```dart
// home.dart
import 'package:flutter/material.dart';

class Home extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.blue[400],
      appBar: AppBar(
        title: const Text('Seletor de Funcionalidades'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text("Agendamento de Notificações",
            style: TextStyle(color: Colors.white, fontSize: 24),),
            IconButton(
              onPressed: () {
                // Navegar para a tela de agendamento de notificações locais
              },
              icon: ClipRRect(
                borderRadius: BorderRadius.circular(20.0),
                child: Image.asset('assets/tomato.png',
                  width: 200,
                  height: 200,
                  fit: BoxFit.contain,),
              ),
            ),
            const SizedBox(height: 20),
            const Text("Remover de Fundo de Imagens",
            style: TextStyle(color: Colors.white, fontSize: 24),
            ),
            IconButton(
              onPressed: () {
                // Navegar para a tela de remoção de fundo de imagens
              },
              icon: ClipRRect(
                borderRadius: BorderRadius.circular(20.0),
                child: Image.asset('assets/shiba01.png',
                  width: 200,
                  height: 200,
                  fit: BoxFit.contain,),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
```

Vamos atualizar o arquivo `main.dart` para exibir a nossa página `Home`:

```dart
// main.dart
import 'package:encontro_08/views/home.dart';
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
      title: 'Encontro 08',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        useMaterial3: true,
      ),
      initialRoute: '/home',
      routes: {
        '/home': (context) => Home(),
        // '/local_notifications': (context) => const LocalNotifications(),
        // '/remove_background': (context) => const RemoveBackground(),
      },
    );
  }
}

```

Pessoal, até aqui, temos nossa aplicação com uma página apenas e dois botões. Vamos implementar as funcionalidades de agendamento de notificações locais e remoção de fundo de imagens ao longo do material.

Primeiro vamos implementar as mudanças de tela. Cada uma das novas telas estará implementada com suas funcionalidades básicas. Sem estar funcionando ainda, mas com a estrutura básica.

## Agendamento de Notificações Locais

Vamos primeiro criar a tela de agendamento de notificações locais. Vamos criar um novo arquivo chamado `local_notifications.dart` dentro do diretório `views`.

```dart
// local_notifications.dart
// Construção de uma tela que permite realizar agendamentos de tempo para notificações locais.

import 'package:flutter/material.dart';

class LocalNotifications extends StatefulWidget {
  const LocalNotifications({Key? key}) : super(key: key);

  @override
  State<LocalNotifications> createState() => _LocalNotificationsState();
}

class _LocalNotificationsState extends State<LocalNotifications> {
  TextEditingController _timeController = TextEditingController();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.blue[400],
      appBar: AppBar(
        title: const Text('Agendamento de Notificações'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text(
              "Agendamento de Notificações",
              style: TextStyle(color: Colors.white, fontSize: 24),
            ),
            Padding(
              padding: const EdgeInsets.all(8.0),
              child: TextField(
                keyboardType: TextInputType.number,
                controller: _timeController,
                decoration: const InputDecoration(
                  hintText: 'Digite o tempo em segundos',
                ),
              ),
            ),
            IconButton(
              onPressed: () {
                // Navegar para a tela de agendamento de notificações locais
              },
              icon: ClipRRect(
                borderRadius: BorderRadius.circular(20.0),
                child: Image.asset(
                  'assets/tomato.png',
                  width: 100,
                  height: 100,
                  fit: BoxFit.contain,
                ),
              ),
            ),
            
           
          ],
        ),
      ),
    );
  }
}
```

É importante adicionarmos essa rota no arquivo `main.dart`:

```dart
//Código Anterior
routes: {
        '/home': (context) => Home(),
        '/local_notifications': (context) => const LocalNotifications(),
        // '/remove_background': (context) => const RemoveBackground(),
      },
```

Legal, agora vamos adicionar a tela que está faltando aqui. Vamos criar a tela de remoção de fundo de imagens. Importante, repare que ainda existem dependências que devem ser adicionadas para que essa funcionalidade funcione. Nosso objetivo hoje é que vocês possam fazer essas adições ao material.

## Remoção de Fundo de Imagens

Vamos iniciar a criação dessa tela. Vamos criar um novo arquivo chamado `remove_background.dart` dentro do diretório `views`.

```dart
// remove_background.dart
// Tela da aplicação que permite o usuário escolher uma imagem, tirar ela com a camera. Enviar essa imagem para o servidor, remover o background e exibir a imagem sem o background. O usuário poderá compartilhar a imagem sem o background.

import 'package:flutter/material.dart';

class RemoveBackground extends StatelessWidget {
  const RemoveBackground({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.blue[400],
      appBar: AppBar(
        title: const Text('Remover de Fundo de Imagens'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text(
              "Remover de Fundo de Imagens",
              style: TextStyle(color: Colors.white, fontSize: 24),
            ),
            
          ],
        ),
      ),
    );
  }
}
```

E vamos ajustar o arquivo `main.dart` para adicionar essa rota:

```dart
//Código Anterior
routes: {
        '/home': (context) => Home(),
        '/local_notifications': (context) => const LocalNotifications(),
        '/remove_background': (context) => const RemoveBackground(),
      },
```

Além de adicionar as rotas, modificar o arquivo `home.dart` para navegar para essas telas:

```dart
// home.dart
import 'package:flutter/material.dart';

class Home extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.blue[400],
      appBar: AppBar(
        title: const Text('Seletor de Funcionalidades'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text("Agendamento de Notificações",
            style: TextStyle(color: Colors.white, fontSize: 24),),
            IconButton(
              onPressed: () {
                // Navegar para a tela de agendamento de notificações locais
                Navigator.pushNamed(context, '/local_notifications');
              },
              icon: ClipRRect(
                borderRadius: BorderRadius.circular(20.0),
                child: Image.asset('assets/tomato.png',
                  width: 200,
                  height: 200,
                  fit: BoxFit.contain,),
              ),
            ),
            const SizedBox(height: 20),
            const Text("Remover de Fundo de Imagens",
            style: TextStyle(color: Colors.white, fontSize: 24),
            ),
            IconButton(
              onPressed: () {
                // Navegar para a tela de remoção de fundo de imagens
                Navigator.pushNamed(context, '/remove_background');
              },
              icon: ClipRRect(
                borderRadius: BorderRadius.circular(20.0),
                child: Image.asset('assets/shiba01.png',
                  width: 200,
                  height: 200,
                  fit: BoxFit.contain,),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
```

Pessoal com isso temos a estrutura básica da nossa aplicação para o encontro de hoje. Vamos implementar as funcionalidades de agendamento de notificações locais e remoção de fundo de imagens ao longo do material.
