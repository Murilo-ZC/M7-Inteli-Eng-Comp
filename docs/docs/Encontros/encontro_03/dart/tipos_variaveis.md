---
sidebar_position: 3
title: Tipos de Variáveis
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Tipos de Variáveis

Dart é uma linguagem fortemente tipada, o que significa que todas as variáveis têm um tipo de dados associado a elas. Dart tem suporte para os seguintes tipos de dados:

- `int`: números inteiros
- `double`: números de ponto flutuante
- `String`: sequência de caracteres
- `bool`: valor booleano
- `List`: coleção de objetos
- `Map`: coleção de pares chave-valor

Aqui vale uma característica importante do Dart. Mesmo sendo uma linguagem fortemente tipada, o Dart permite que você defina o tipo de uma variável de forma explícita ou de forma implícita. Vamos ver um exemplo:

```dart
void main() {
  int numero = 10; // Tipo explícito
  var numero2 = 20; // Tipo implícito

  print(numero);
  print(numero2);
}
```

Neste exemplo, a variável `numero` é do tipo `int` e a variável `numero2` é do tipo `int` também, mas o tipo foi inferido pelo Dart.

Vamos ver agora como podemos trabalhar com cada um desses tipos de dados.

### Números

Dart suporta dois tipos de números:

- `int`: números inteiros
- `double`: números de ponto flutuante

Vamos ver um exemplo de como podemos trabalhar com esses tipos de dados:

```dart
void main() {
  int numeroInteiro = 10;
  double numeroDecimal = 10.5;

  print(numeroInteiro);
  print(numeroDecimal);
}
```

### Strings

Strings são usadas para representar texto. Em Dart, você pode criar strings usando aspas simples ou duplas. Vamos ver um exemplo:

```dart
void main() {
  String nome = 'Dart';
  String sobrenome = "Flutter";

  print(nome);
  print(sobrenome);
}
```

### Booleanos

O tipo `bool` é usado para representar valores booleanos. Um valor booleano pode ser `true` ou `false`. Vamos ver um exemplo:

```dart
void main() {
  bool isTrue = true;
  bool isFalse = false;

  print(isTrue);
  print(isFalse);
}
```

### Listas

Uma lista é uma coleção ordenada de objetos. Em Dart, você pode criar uma lista usando colchetes `[]`. Vamos ver um exemplo:

```dart
void main() {
  List<int> numeros = [1, 2, 3, 4, 5];

  print(numeros);

  // Adiciona mais um valor a lista
  numeros.add(6);

  print(numeros);

  // Remove o valor 3 da lista
  numeros.remove(3);

  print(numeros);

  // Acessa o valor na posição 2 da lista
  print(numeros[2]);

  // Tamanho da lista
  print(numeros.length);

  // Verifica se a lista está vazia
  print(numeros.isEmpty);

  // Verifica se um valor existe na lista
  print(numeros.contains(4));
}
```

Este código já merece um pouco mais de atenção. Aqui estamos criando uma lista de números inteiros. A lista é uma coleção de objetos, então podemos adicionar qualquer tipo de objeto a ela.

Quando que `numeros` será uma lista, nós estamos definindo o tipo de objeto que a lista pode receber. Neste caso, a lista `numeros` só pode receber números inteiros. Utilizamos o operador `<>` para definir o tipo de objeto que a lista pode receber.

Se tentarmos remover um valor que não existe na lista, o Dart não irá lançar uma exceção. Ele simplesmente não fará nada.

Vamos trabalhar com diversas listas ao longo do curso, tente ficar bastante familiarizado com elas.

### Mapas

Um mapa é uma coleção de pares chave-valor. Em Dart, você pode criar um mapa usando chaves `{}`. Vamos ver um exemplo:

```dart
void main() {
  Map<String, String> pessoa = {
    'nome': 'João',
    'sobrenome': 'Silva',
    'idade': '30',
  };

  print(pessoa);

  // Adiciona um novo par chave-valor ao mapa
  pessoa['email'] = 'email@email.com';

  print(pessoa);

}
```

Vamos avaliar o código anterior para compreender alguns detalhes de quando trabalhamos com mapas no Dart. Aqui estamos criando um mapa de strings. O mapa é uma coleção de pares chave-valor, então podemos adicionar qualquer tipo de objeto a ele. Como definimos que ele vai apenas trabalhar com strings, o Dart irá lançar um erro se tentarmos adicionar um valor que não seja uma string.

> Mas Murilo e se quisermos adicionar um valor que não seja uma string?

Nos casos que desejarmos adicionar outro valores que não são do mesmo tipo em um mapa, podemos utilizar o tipo `dynamic`. O tipo `dynamic` é um tipo especial que pode receber qualquer tipo de objeto. Vamos ver um exemplo:

```dart
void main() {
  Map<String, dynamic> pessoa = {
    'nome': 'João',
    'sobrenome': 'Silva',
    'idade': 30,
  };

  print(pessoa);
}
```

Neste exemplo, estamos criando um mapa de strings e dinâmicos. O mapa é uma coleção de pares chave-valor, então podemos adicionar qualquer tipo de objeto a ele. Como definimos que ele vai trabalhar com strings e dinâmicos, o Dart não irá lançar um erro se tentarmos adicionar um valor que não seja uma string.

## DartPad

<iframe  style={{
            display: 'block',
            margin: 'auto',
            width: '100%',
            height: '50vh',
            marginBottom: '24px'
        }}
        src="https://dartpad.dev/?id=4adb4b8ecd8d5641754c82a66cb233ea?theme=light"></iframe>

