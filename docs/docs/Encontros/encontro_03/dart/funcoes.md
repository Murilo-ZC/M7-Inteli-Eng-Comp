---
sidebar_position: 5
title: Funções
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Funções

As funções são blocos de código que realizam uma tarefa específica. Elas são utilizadas para organizar o código e evitar a repetição de trechos de código. Em Dart, as funções são declaradas utilizando a palavra-chave `void` seguida do nome da função e dos parâmetros entre parênteses. Vamos ver um exemplo de uma função simples que imprime uma mensagem na tela:

```dart
void imprimirMensagem() {
    print('Olá, Mundo!');
}

void main() {
  imprimirMensagem();
}
```

As funcões podem receber parâmetros que são utilizados para passar informações para a função. Os parâmetros são declarados entre parênteses após o nome da função. Vamos ver um exemplo de uma função que recebe um parâmetro:

```dart
void imprimirMensagem(String mensagem) {
    print(mensagem);
}

void main() {
  imprimirMensagem('Olá, Mundo!');
}
```

As funções também podem retornar um valor utilizando a palavra-chave `return`. Vamos ver um exemplo de uma função que retorna um valor:

```dart
int somar(int a, int b) {
    return a + b;
}

void main() {
  int resultado = somar(10, 20);
  print(resultado);
}
```
É possivel também definir valores padrão para os parâmetros de uma função. Vamos ver um exemplo:

```dart
void imprimirMensagem(String mensagem, {String nome = 'Mundo'}) {
    print('$mensagem, $nome!');
}

void main() {
  imprimirMensagem('Olá');
  imprimirMensagem('Olá', nome: 'Dart');
}
```

Aqui temos um ponto importante sobre as funções em Dart. Elas são *first-class citizens*, o que significa que as funções podem ser atribuídas a variáveis, passadas como parâmetros para outras funções e retornadas de outras funções. Vamos ver um exemplo de como podemos atribuir uma função a uma variável:

```dart
void imprimirMensagem() {
    print('Olá, Mundo!');
}

void main() {
  var funcao = imprimirMensagem;
  funcao();
}
```

Neste exemplo, a função `imprimirMensagem` é atribuída à variável `funcao` e depois é chamada utilizando a variável.

As funções são uma parte fundamental da programação em Dart e são utilizadas para organizar o código e torná-lo mais legível e reutilizável.
Quando uma função tem apenas uma expressão, é possível utilizar a sintaxe de função de seta `=>`. Vamos ver um exemplo:

```dart
int somar(int a, int b) => a + b;

void main() {
  int resultado = somar(10, 20);
  print(resultado);
}
```

Neste exemplo, a função `somar` tem apenas uma expressão que retorna a soma dos parâmetros `a` e `b`. A sintaxe de função de seta `=>` é utilizada para definir a função de forma mais concisa.

## DartPad

<iframe  style={{
            display: 'block',
            margin: 'auto',
            width: '100%',
            height: '50vh',
            marginBottom: '24px'
        }}
        src="https://dartpad.dev/?id=56417c61d38592329bfe99b94d8e9867?theme=light"></iframe>