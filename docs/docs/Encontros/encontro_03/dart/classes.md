---
sidebar_position: 6
title: Classes
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Um pouco sobre Orientação a Objetos

A programação orientada a objetos é um paradigma de programação que utiliza objetos para representar dados e métodos para manipular esses dados. Os objetos são instâncias de classes, que são modelos que definem a estrutura e o comportamento dos objetos. As classes são compostas por atributos e métodos, que representam as características e o comportamento dos objetos, respectivamente.

O paradigma é fundamentado em quatro princípios básicos:

- **Abstração**: é a capacidade de representar objetos do mundo real em forma de classes, abstraindo as características e o comportamento dos objetos.
- **Encapsulamento**: é a capacidade de ocultar os detalhes de implementação dos objetos, expondo apenas a interface pública.
- **Herança**: é a capacidade de criar novas classes a partir de classes existentes, herdando os atributos e métodos da classe pai.
- **Polimorfismo**: é a capacidade de um objeto se comportar de diferentes formas, dependendo do contexto em que é utilizado.

Esses quatro pilares são fundamentais para a programação orientada a objetos e são utilizados para criar sistemas mais organizados, reutilizáveis e fáceis de manter.

Em Dart, assim como em outras linguagens de programação, podemos criar classes para representar objetos. Vamos ver como podemos criar uma classe em Dart.

## Classes em Dart

Em Dart, as classes são definidas utilizando a palavra-chave `class`, seguida do nome da classe e do corpo da classe entre chaves. Vamos ver um exemplo de uma classe simples em Dart:

```dart
class Pessoa {
  String nome;
  int idade;

  Pessoa(this.nome, this.idade);

  void imprimirDados() {
    print('Nome: $nome');
    print('Idade: $idade');
  }
}

void main() {
  Pessoa pessoa = Pessoa('João', 30);
  pessoa.imprimirDados();
}
```

Pessoal vamos analisar este exemplo de código. Primeiro definimos a classe `Pessoa` com dois atributos: `nome` e `idade`. Em seguida, definimos um construtor que recebe os valores dos atributos `nome` e `idade` e os atribui aos atributos da classe. Por fim, definimos um método `imprimirDados` que imprime os valores dos atributos `nome` e `idade`.

O `contrutor` de uma classe é um método especial que é chamado quando um objeto da classe é criado. Ele é utilizado para inicializar os atributos da classe com os valores passados como parâmetros. Em Dart, o construtor pode ser definido de duas formas: `construtor padrão` e `construtor nomeado`.

O `construtor padrão` é um construtor que não possui nome e é chamado quando um objeto da classe é criado sem passar nenhum parâmetro. Já o `construtor nomeado` é um construtor que possui um nome igual ao da classe e é chamado quando um objeto da classe é criado passando os parâmetros necessários.

Vamos ver um exemplo de um construtor nomeado:

```dart
class Pessoa {
  String nome;
  int idade;

  Pessoa({required this.nome, required this.idade});

  void imprimirDados() {
    print('Nome: $nome');
    print('Idade: $idade');
  }
}

void main() {
  Pessoa pessoa = Pessoa(nome: 'João', idade: 30);
  pessoa.imprimirDados();
}
```

Pessoal reparem na mudança entre essas duas formas de construtores. No primeiro exemplo, utilizamos o construtor padrão para inicializar os atributos da classe `Pessoa`. Já no segundo exemplo, utilizamos um construtor nomeado para inicializar os atributos da classe `Pessoa`. A principal diferença entre os dois construtores é a forma como os parâmetros são passados para a classe.

No segundo caso, repare também que utilizamos a palavra-chave `required` antes dos parâmetros do construtor. Essa palavra-chave é utilizada para indicar que os parâmetros são obrigatórios e devem ser passados ao criar um objeto da classe.

Os construtores podem possuir um corpo mais robusto. No exemplo abaixo, iniciamos nossa classe e já fazemos o inserção da data e hora que ela foi criada.

```dart
import 'dart:core';

class Pessoa {
  String nome;
  int idade;
  DateTime? dataCriacao;

  Pessoa({required this.nome, required this.idade}){
    dataCriacao = DateTime.now();
  }
      

  void imprimirDados() {
    print('Nome: $nome');
    print('Idade: $idade');
    print('Data de Criação: $dataCriacao');
  }
}

void main() {
  Pessoa pessoa = Pessoa(nome: 'João', idade: 30);
  pessoa.imprimirDados();
}
```

Aqui temos alguns pontos diferentes do que estavamos fazendo. O primeiro é a importação da biblioteca `dart:core`. Essa biblioteca é a biblioteca padrão do Dart e contém as classes e funções básicas da linguagem. Neste caso, estamos importando a classe `DateTime`, que é utilizada para representar datas e horas. Além disso, estamos utilizando a classe `DateTime` para criar um objeto `dataCriacao` e atribuir a ele a data e hora em que o objeto da classe `Pessoa` foi criado. Para isso, utilizamos o método `now()` da classe `DateTime`, que retorna a data e hora atual.

Ainda neste ponto, gostaria de chamar a atenção para o uso do `?` após o tipo `DateTime`. Esse operador é chamado de `operador de nulabilidade` e é utilizado para indicar que o valor da variável pode ser nulo. No Dart, todas as variáveis são não nulas por padrão, o que significa que elas não podem receber o valor `null`. No entanto, podemos utilizar o operador `?` para indicar que uma variável pode ser nula.

> Mas Murilo por que precisamos disso?

Em Dart, o operador `?` é utilizado para indicar que uma variável pode ser nula. Isso é útil quando queremos indicar que uma variável pode não ter um valor definido. Por exemplo, se quisermos representar uma data de criação que pode não ter sido definida, podemos utilizar o operador `?` para indicar que o valor da variável pode ser nulo.

## Herança

A herança é um dos pilares da programação orientada a objetos e é utilizada para criar novas classes a partir de classes existentes, herdando os atributos e métodos da classe pai. Em Dart, a herança é feita utilizando a palavra-chave `extends`. Vamos ver um exemplo de herança em Dart:

```dart
class Animal {
  String nome;

  Animal(this.nome);

  void emitirSom() {
    print('O animal está emitindo um som');
  }
}

class Cachorro extends Animal {
  Cachorro(String nome) : super(nome);

  void latir() {
    print('O cachorro está latindo');
  }
}

void main() {
  Cachorro cachorro = Cachorro('Rex');
  cachorro.emitirSom();
  cachorro.latir();
}
```

Repare que aqui temos bastante coisa acontecendo também:

1. Criamos uma classe `Animal` com um atributo `nome` e um método `emitirSom`.
2. Criamos uma classe `Cachorro` que herda da classe `Animal` utilizando a palavra-chave `extends`. A classe `Cachorro` possui um método `latir` que imprime a mensagem `O cachorro está latindo`.
3. No método `main`, criamos um objeto da classe `Cachorro` chamado `cachorro` e chamamos os métodos `emitirSom` e `latir` do objeto.

Neste exemplo, a classe `Cachorro` herda da classe `Animal` e possui um método `latir` que é específico para a classe `Cachorro`. O método `emitirSom` é herdado da classe `Animal` e pode ser chamado a partir de um objeto da classe `Cachorro`.

Estamos criando uma relação de herança entre as classes `Animal` e `Cachorro`. A classe `Cachorro` herda os atributos e métodos da classe `Animal` e pode adicionar novos atributos e métodos específicos para a classe `Cachorro`. Essa relação é do tipo `é um`, o que significa que um cachorro é um animal.

Dart também possui o conceito de `métodos e atributos estáticos`. Os métodos e atributos estáticos pertencem à classe em vez de pertencerem a uma instância da classe. Isso significa que eles podem ser acessados diretamente a partir da classe, sem a necessidade de criar um objeto da classe. Vamos ver um exemplo de um método estático em Dart:

```dart
class Calculadora {
  static int somar(int a, int b) {
    return a + b;
  }
}

void main() {
  int resultado = Calculadora.somar(10, 20);
  print(resultado);
}
```

Neste exemplo, criamos uma classe `Calculadora` com um método estático `somar` que recebe dois números inteiros `a` e `b` e retorna a soma dos dois números. O método `somar` é estático, o que significa que ele pode ser chamado diretamente a partir da classe `Calculadora`, sem a necessidade de criar um objeto da classe.

Os métodos e atributos estáticos são úteis quando queremos criar métodos e atributos que pertencem à classe em vez de pertencerem a uma instância da classe. Eles são utilizados para representar comportamentos e características que são comuns a todas as instâncias da classe.

## Polimorfismo

O polimorfismo é um dos pilares da programação orientada a objetos e é utilizado para criar objetos que se comportam de diferentes formas, dependendo do contexto em que são utilizados. Em Dart, o polimorfismo é feito através de classes abstratas e interfaces. Vamos ver um exemplo de polimorfismo em Dart:

```dart
abstract class Animal {
  void emitirSom();
}

class Cachorro extends Animal {
  @override
  void emitirSom() {
    print('O cachorro está latindo');
  }
}

class Gato extends Animal {
  @override
  void emitirSom() {
    print('O gato está miando');
  }
}

void main() {
  List<Animal> animais = [Cachorro(), Gato()];

  for (Animal animal in animais) {
    animal.emitirSom();
  }
}
```

Neste exemplo, criamos uma classe abstrata `Animal` com um método abstrato `emitirSom`. Uma classe abstrata é uma classe que não pode ser instanciada diretamente e é utilizada como um modelo para outras classes. As classes `Cachorro` e `Gato` herdam da classe `Animal` e implementam o método `emitirSom` de acordo com o comportamento específico de cada animal.

No método `main`, criamos uma lista de animais que contém um cachorro e um gato. Em seguida, percorremos a lista de animais e chamamos o método `emitirSom` de cada animal. Como o método `emitirSom` é abstrato na classe `Animal`, ele é implementado de forma diferente em cada classe que herda da classe `Animal`, permitindo que os animais emitam sons diferentes.

O polimorfismo é utilizado para criar objetos que se comportam de diferentes formas, dependendo do contexto em que são utilizados. Ele é útil quando queremos representar objetos que compartilham um comportamento comum, mas que se comportam de forma diferente em determinadas situações.

Já as interfaces podem ser utilizadas para definir um contrato que as classes devem seguir. Uma interface é um conjunto de métodos que as classes devem implementar para cumprir o contrato. Vamos ver um exemplo de interface em Dart:

```dart
abstract class Animal {
  void emitirSom();
}

abstract class Voador {
  void voar();
}

class Passaro extends Animal implements Voador {
  @override
  void emitirSom() {
    print('O pássaro está cantando');
  }

  @override
  void voar() {
    print('O pássaro está voando');
  }
}

void main() {
  Passaro passaro = Passaro();
  passaro.emitirSom();
  passaro.voar();
}
```

Neste exemplo, criamos uma interface `Voador` com um método `voar` e uma classe `Passaro` que implementa a interface `Voador`. A classe `Passaro` herda da classe `Animal` e implementa os métodos `emitirSom` e `voar` de acordo com o comportamento específico de um pássaro. Repare que as interfaces são utilizadas para definir um contrato que as classes devem seguir. A classe `Passaro` implementa a interface `Voador` e deve implementar o método `voar` para cumprir o contrato da interface.

As interfaces em Dart são declaradas como classes abstratas com métodos abstratos. As classes que implementam a interface devem implementar todos os métodos da interface para cumprir o contrato da interface. As interfaces estabelecem um contrato entre as classes e garantem que as classes sigam um padrão de implementação.


## DartPad

<iframe  style={{
            display: 'block',
            margin: 'auto',
            width: '100%',
            height: '50vh',
            marginBottom: '24px'
        }}
        src="https://dartpad.dev/?id=7a69fbbae158a336e25b376393d01a2a?theme=light"></iframe>
