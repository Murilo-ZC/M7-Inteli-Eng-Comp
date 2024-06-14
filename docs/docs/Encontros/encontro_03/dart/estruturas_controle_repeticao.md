---
sidebar_position: 4
title: Estruturas de Controle e de Repetição
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Estruturas de Controle 

Em Dart, assim como em outras linguagens de programação, temos algumas estruturas de controle que nos permitem controlar o fluxo de execução do nosso programa. Vamos ver algumas dessas estruturas.

### if-else

A estrutura `if-else` é uma das estruturas de controle mais comuns em programação. Ela nos permite executar um bloco de código se uma condição for verdadeira e outro bloco de código se a condição for falsa. Vamos ver um exemplo:

```dart
void main() {
  int numero = 10;

  if (numero > 0) {
    print('O número é positivo');
  } else {
    print('O número é negativo');
  }
}
```

Neste exemplo, estamos verificando se o número é maior que zero. Se for, imprimimos a mensagem `O número é positivo`, caso contrário, imprimimos a mensagem `O número é negativo`.

### switch-case

A estrutura `switch-case` é utilizada quando queremos comparar uma variável com uma lista de valores possíveis. Vamos ver um exemplo:

```dart
void main() {
  String diaDaSemana = 'segunda';

  switch (diaDaSemana) {
    case 'segunda':
      print('Hoje é segunda-feira');
      break;
    case 'terça':
      print('Hoje é terça-feira');
      break;
    case 'quarta':
      print('Hoje é quarta-feira');
      break;
    case 'quinta':
      print('Hoje é quinta-feira');
      break;
    case 'sexta':
      print('Hoje é sexta-feira');
      break;
    case 'sábado':
      print('Hoje é sábado');
      break;
    case 'domingo':
      print('Hoje é domingo');
      break;
    default:
      print('Dia inválido');
  }
}
```

Neste exemplo, estamos verificando o valor da variável `diaDaSemana` e imprimindo uma mensagem de acordo com o dia da semana.

Uma outra implementação do código acima é utilizando um mapa:

```dart
void main() {
  String diaDaSemana = 'segunda';

  Map<String, String> diasDaSemana = {
    'segunda': 'Hoje é segunda-feira',
    'terça': 'Hoje é terça-feira',
    'quarta': 'Hoje é quarta-feira',
    'quinta': 'Hoje é quinta-feira',
    'sexta': 'Hoje é sexta-feira',
    'sábado': 'Hoje é sábado',
    'domingo': 'Hoje é domingo',
  };

  print(diasDaSemana[diaDaSemana] ?? 'Dia inválido');
}
```

Aqui vou aproveitar para já dar um gosto de um dos operadores que vamos ver mais a frente, o `??`. Ele é o operador de coalescência nula, que nos permite definir um valor padrão para uma variável caso ela seja nula. Quando tentamos acessar um valor em um mapa que não existe, o Dart retorna `null`. Com o operador `??`, podemos definir um valor padrão para esse caso.

:::tip[Continue a nadar!]

Em alguns momentos, algumas funcionalidades da linguagem podem não estar totalmente claras. Vamos continuar com o curso que vamos ver mais exemplos e vamos entender melhor essas funcionalidades. Lembre-se de testar o máximo que vocês puderem!

<img src="https://pa1.aminoapps.com/6513/28974ccdf6ee34f4bcb76b6a7712200b269480bd_00.gif" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom: '24px' }}/>

:::

## Estruturas de Repetição

As estruturas de repetição nos permitem executar um bloco de código várias vezes. Vamos ver algumas dessas estruturas.

### for

A estrutura `for` é utilizada quando sabemos exatamente quantas vezes queremos repetir um bloco de código. Vamos ver um exemplo:

```dart
void main() {
  for (int i = 0; i < 5; i++) {
    print('O valor de i é $i');
  }
}
```

Neste exemplo, estamos imprimindo o valor da variável `i` de 0 a 4. Observe que aqui utilizamos um recurso de Dart chamado interpolação de strings. Para fazer isso, utilizamos o símbolo `$` seguido da variável que queremos interpolar. Podemos interpolar não apenas o valor de uma variável, mas também o resultado de uma expressão.

Existem ainda outras formas de utilizar o `for`. Vamos ver um exemplo com uma lista:

```dart
void main() {
  List<int> numeros = [1, 2, 3, 4, 5];

  for (int numero in numeros) {
    print('O número é $numero');
  }
}
```

Neste exemplo, estamos percorrendo a lista `numeros` e imprimindo o valor de cada número.


### while

A estrutura `while` é utilizada quando não sabemos exatamente quantas vezes queremos repetir um bloco de código, mas sabemos a condição de parada. Vamos ver um exemplo:

```dart
void main() {
  int i = 0;

  while (i < 5) {
    print('O valor de i é $i');
    i++;
  }
}
```

Neste exemplo, estamos imprimindo o valor da variável `i` de 0 a 4.

### do-while

A estrutura `do-while` é semelhante à estrutura `while`, mas a condição é verificada após a execução do bloco de código. Isso garante que o bloco de código seja executado pelo menos uma vez. Vamos ver um exemplo:

```dart
void main() {
  int i = 0;

  do {
    print('O valor de i é $i');
    i++;
  } while (i < 5);
}
```

Neste exemplo, estamos imprimindo o valor da variável `i` de 0 a 4.


## DartPad

<iframe  style={{
            display: 'block',
            margin: 'auto',
            width: '100%',
            height: '50vh',
            marginBottom: '24px'
        }}
        src="https://dartpad.dev/?id=baf0feb2a2d43dac00103dbd75b0e3c8?theme=light"></iframe>

