---
sidebar_position: 6
title: MobX e Exemplo de Implementação
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Definição do Problema

Nosso problema é um recorte de aplicação que vai contemplar alguns pontos importantes:

- Utilização da arquitetura MVC;
- Utilização de listas para exibir os produtos;
- Adição de produtos ao carrinho de compras;
- Exibição do total da compra.

Para resolver esse problema, vamos utilizar o MobX. O MobX é uma biblioteca que permite a criação de observáveis e reações de forma simples e eficiente. A documentação do MobX pode ser encontrada [aqui](https://pub.dev/packages/mobx).

Agora vamos para nossa aplicação!!

## Criando o projeto base

Vamos criar um projeto base para a nossa aplicação. Para isso, vamos utilizar o comando `flutter create mobx_carrinho`.

```bash
flutter create mobx_carrinho
```

O MobX não é um pacote oficial do Flutter, então precisamos adicionar o pacote ao nosso arquivo `pubspec.yaml`. Isso pode ser realizado editando o arquivo, ou utilizando o comando `flutter pub add mobx`. Além dele, vamos adicionar o pacote `flutter_mobx` que é uma extensão do MobX para o Flutter.

```bash
flutter pub add mobx
flutter pub add flutter_mobx
flutter pub add build_runner
flutter pub add mobx_codegen
```

Agora vamos construir nossa aplicação. Primeiro, vamos criar a estrutura de pastas do nosso projeto. Vamos criar as pastas `models`, `controllers` e `views`. De acordo com o avanço da aplicação, vamos criando os arquivos necessários. Agora, dentro do nosso diretório de `views`, vamos criar um outro diretório com o nome de `screens`. Esse diretório vai conter as telas da nossa aplicação. A princípio, nossa aplicação vai ter duas telas: a tela de listagem de produtos e a tela de carrinho de compras.

## Criando a ProductListScreen

Vamos criar os arquivos `product_list_screen.dart` e `cart_screen.dart` dentro do diretório `screens`. Vamos começar a escrever o código da nossa `product_list_screen.dart`.

```dart
// product_view.dart
// Arquivo de tela de visualização de lista de produtos

import 'package:flutter/material.dart';
import 'package:flutter_mobx/flutter_mobx.dart';
import 'package:mobx_carrinho/controllers/cart_controller.dart';
import 'package:mobx_carrinho/controllers/product_controller.dart';
import 'package:mobx_carrinho/models/product_model.dart';

class ProductView extends StatelessWidget {
  final ProductController productController;
  final CartController cartController;

  ProductView({required this.productController, required this.cartController});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Produtos'),
        actions: [
          IconButton(
            icon: Icon(Icons.shopping_cart),
            onPressed: () {
              Navigator.pushNamed(context, '/cart');
            },
          ),
        ],
      ),
      body: Observer(
        builder: (_) {
          return ListView.builder(
            itemCount: productController.products.length,
            itemBuilder: (context, index) {
              Product product = productController.products[index];
              return ListTile(
                title: Text(product.name),
                subtitle: Text('R\$ ${product.price.toStringAsFixed(2)}'),
                trailing: IconButton(
                  icon: Icon(Icons.add_shopping_cart),
                  onPressed: () {
                    cartController.addProduct(product);
                  },
                ),
              );
            },
          );
        },
      ),
    );
  }
}
```

Ao observar nossa aplicação, estamos utilizando o Scaffold para construir a tela. No corpo da tela, estamos utilizando um `ListView.builder` para exibir a lista de produtos. O `ListView.builder` é um widget que constrói os itens da lista sob demanda. Isso significa que ele só constrói os itens que estão visíveis na tela. Isso é importante para otimizar a performance da aplicação. Se diversos itens fossem construídos ao mesmo tempo, a aplicação poderia ficar lenta. Desta forma, mesmo que a lista tenha milhares de itens, o `ListView.builder` só vai construir os itens que estão visíveis na tela.

> Mas Murilo e quando os itens saem da tela de visão do usuário? Eles são destruídos?

Sim, eles são destruídos. O `ListView.builder` é um widget que constrói os itens sob demanda. Quando um item sai da tela de visão do usuário, ele é destruído. Quando o usuário rola a tela para cima ou para baixo, o `ListView.builder` constrói os itens que estão visíveis na tela.

## Implementando o modelo de produto

Não vamos conseguir executar nosso projeto ainda. Não temos implementado nossos modelos e controladores. Vamos implementar nosso modelo de produto. Ele já vai ser implementado com o `MobX`. Ele vai ser responsável por gerenciar o estado dos produtos. Por hora, para simular o carregamento dos produtos, vamos criar um método `loadProducts` que vai adicionar alguns produtos na lista de JSON, previamente definida nos assets da aplicação. 

:::tip[Dependências do MobX]

Pessoal, não esqueçam de adicionar as dependências do MobX no arquivo `pubspec.yaml`. Vamos adicionar o pacote `mobx` e o pacote `flutter_mobx`.

```bash

flutter pub add mobx
flutter pub add flutter_mobx

```

:::

```dart
// product_model.dart

// product_model.dart
// Arquivo de modelo de produto. Carrega os dados dos produtos de um arquivo JSON dos assets.

import 'dart:convert';

import 'package:flutter/services.dart';

class Product {
  final String name;
  final double price;

  Product({required this.name, required this.price});

  static Future<List<Product>> loadProducts() async {
    String productsJson = await rootBundle.loadString('assets/products.json');
    List<dynamic> productsList = jsonDecode(productsJson);

    return productsList
        .map((product) => Product(name: product['name'], price: product['price']))
        .toList();
  }
}
```

Agora vamos adicionar alguns produtos dentro deste nosso arquivo JSON. Vamos criar um arquivo `products.json` dentro do diretório `assets`. Vamos adicionar o seguinte conteúdo:

```json
[
  {
    "name": "Camiseta",
    "price": 29.99
  },
  {
    "name": "Calça",
    "price": 59.99
  },
  {
    "name": "Tênis",
    "price": 99.99
  },
  {
    "name": "Boné",
    "price": 19.99
  }
]
```

Adicionar o nosso recurso no arquivo `pubspec.yaml`:

```yaml
flutter:
  assets:
    - assets/products.json
```

Legal, agora temos nossa lista de produtos carregada. Vamos implementar o controlador de produtos. Ele vai ser responsável por gerenciar o estado dos produtos. Vamos implementar o método `loadProducts` que vai carregar os produtos do arquivo JSON e adicionar na lista de produtos.

## Implementando o controlador de produtos

```dart
// product_controller.dart
// Arquivo de controlador de produto. Carrega os produtos do modelo e os mantém em uma lista observável.

import 'package:mobx/mobx.dart';
import 'package:mobx_carrinho/models/product_model.dart';

part 'product_controller.g.dart';

class ProductController = _ProductControllerBase with _$ProductController;

abstract class _ProductControllerBase with Store {
  @observable
  ObservableList<Product> products = ObservableList<Product>();

  @action
  void loadProducts() {
    Product.loadProducts().then((value) => products = value.asObservable());
  }
}
```

Agora vamos criar o arquivo `product_controller.g.dart` que vai ser gerado pelo MobX. Ele vai conter o código gerado pelo MobX para o controlador de produtos.

```bash
flutter pub run build_runner build
```

Vamos avaliar a classe `product_controller.dart`:

- A classe `ProductController` é uma classe que vai gerenciar o estado dos produtos. Ela é uma classe que vai ser observável. Isso significa que ela vai notificar os observadores quando o estado dos produtos mudar. Para isso, ela utiliza o decorator `@observable` para marcar a lista de produtos como observável.

- A classe `ProductController` possui um método `loadProducts` que vai carregar os produtos do arquivo JSON e adicionar na lista de produtos. Para isso, ela utiliza o decorator `@action` para marcar o método `loadProducts` como uma ação. Isso significa que o método `loadProducts` vai modificar o estado dos produtos.

Vamos implementar a lógica do nosso carrinho de compras. Vamos criar o arquivo `cart_controller.dart` que vai ser responsável por gerenciar o estado do carrinho de compras. Vamos implementar o método `addProduct` que vai adicionar um produto ao carrinho de compras.

## Implementando o controlador de carrinho

```dart
// cart_controller.dart
// Arquivo de controlador de carrinho. Mantém a lista de produtos adicionados ao carrinho e o valor total.

import 'package:mobx/mobx.dart';
import 'package:mobx_carrinho/models/product_model.dart';

part 'cart_controller.g.dart';

class CartController = _CartControllerBase with _$CartController;

abstract class _CartControllerBase with Store {
  @observable
  ObservableList<Product> products = ObservableList<Product>();

  @computed
  double get totalValue => products.fold(0, (total, product) => total + product.price);

  @action
  void addProduct(Product product) {
    products.add(product);
  }

  @action
  void removeProduct(Product product) {
    products.remove(product);
  }
}
```

Essa classe é mais complexa, vamos analisar ela com calma:

- A classe `CartController` é uma classe que vai gerenciar o estado do carrinho de compras. Ela é uma classe que vai ser observável. Isso significa que ela vai notificar os observadores quando o estado do carrinho de compras mudar. Para isso, ela utiliza o decorator `@observable` para marcar a lista de produtos como observável.

- A classe `CartController` possui um método `addProduct` que vai adicionar um produto ao carrinho de compras. Para isso, ela utiliza o decorator `@action` para marcar o método `addProduct` como uma ação. Isso significa que o método `addProduct` vai modificar o estado do carrinho de compras.

- A classe `CartController` possui um método `removeProduct` que vai remover um produto do carrinho de compras. Para isso, ela utiliza o decorator `@action` para marcar o método `removeProduct` como uma ação. Isso significa que o método `removeProduct` vai modificar o estado do carrinho de compras.

- A classe `CartController` possui um método `totalValue` que vai calcular o valor total do carrinho de compras. Para isso, ela utiliza o decorator `@computed` para marcar o método `totalValue` como um cálculo. Isso significa que o método `totalValue` vai calcular o valor total do carrinho de compras. Essa atualização vai ser feita automaticamente pelo MobX, toda vez que um produto for adicionado ou removido do carrinho de compras. O método `fold` é um método que vai acumular o valor total do carrinho de compras.

Vamos gerar o arquivo `cart_controller.g.dart` que vai ser gerado pelo MobX. Ele vai conter o código gerado pelo MobX para o controlador de carrinho de compras.

```bash
flutter pub run build_runner build
```

Agora vamos criar a tela de carrinho de compras. Vamos criar o arquivo `cart_screen.dart` dentro do diretório `screens`. Vamos começar a escrever o código da nossa `cart_screen.dart`.

## Implementando a tela de carrinho de compras

```dart
// cart_screen.dart
// cart_screen.dart
// Tela de carrinho de compras. Exibe os produtos adicionados ao carrinho e o valor total.

import 'package:flutter/material.dart';
import 'package:flutter_mobx/flutter_mobx.dart';
import 'package:mobx_carrinho/controllers/cart_controller.dart';
import 'package:mobx_carrinho/models/product_model.dart';

class CartScreen extends StatelessWidget {
  final CartController cartController;

  CartScreen({required this.cartController});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Carrinho'),
      ),
      body: Observer(
        builder: (_) {
          return ListView.builder(
            itemCount: cartController.products.length,
            itemBuilder: (context, index) {
              Product product = cartController.products[index];
              return ListTile(
                title: Text(product.name),
                subtitle: Text('R\$ ${product.price.toStringAsFixed(2)}'),
                trailing: IconButton(
                  icon: Icon(Icons.remove_shopping_cart),
                  onPressed: () {
                    cartController.removeProduct(product);
                  },
                ),
              );
            },
          );
        },
      ),
      bottomNavigationBar: BottomAppBar(
        child: Padding(
          padding: const EdgeInsets.all(8.0),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Text('Total: R\$ ${cartController.totalValue.toStringAsFixed(2)}'),
              ElevatedButton(
                onPressed: () {
                  cartController.products.clear();
                },
                child: Text('Limpar carrinho'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
```

Agora vamos criar o arquivo `main.dart` que vai ser o ponto de entrada da nossa aplicação. 

## Ajustando o ponto de entrada da aplicação

Vamos começar a escrever o código:

```dart
// main.dart

import 'package:flutter/material.dart';
import 'package:mobx_carrinho/controllers/cart_controller.dart';
import 'package:mobx_carrinho/controllers/product_controller.dart';
import 'package:mobx_carrinho/views/screens/cart_screen.dart';
import 'package:mobx_carrinho/views/screens/product_view.dart';

void main() {
  final productController = ProductController();
  final cartController = CartController();

  WidgetsFlutterBinding.ensureInitialized();
  productController.loadProducts();

  runApp(MyApp(productController: productController, cartController: cartController));
}

class MyApp extends StatelessWidget {
  final ProductController productController;
  final CartController cartController;

  MyApp({required this.productController, required this.cartController});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'MobX Carrinho',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      initialRoute: '/',
      routes: {
        '/': (context) => ProductView(productController: productController, cartController: cartController),
        '/cart': (context) => CartScreen(cartController: cartController),
      },
    );
  }
}
```

Pessoal agora vamos avaliar o que está acontecendo aqui:

- O método `main` é o ponto de entrada da nossa aplicação. Ele é o método que vai ser chamado quando a aplicação for iniciada. No método `main`, estamos criando uma instância do `ProductController` e do `CartController`. Estamos carregando os produtos no `ProductController` e passando os controladores para a nossa aplicação.

- A classe `MyApp` é a nossa aplicação. Ela é uma classe que herda de `StatelessWidget`. Ela é a classe que vai construir a nossa aplicação. No método `build`, estamos construindo a nossa aplicação. Estamos criando uma instância do `MaterialApp` e passando os controladores para as telas da nossa aplicação.

- Na inicialização da nossa aplicação, utilizamos o método `WidgetsFlutterBinding.ensureInitialized()` para garantir que os controladores de produtos e carrinho sejam carregados antes da aplicação ser construída. Isso é importante para garantir que os produtos sejam carregados antes da aplicação ser construída.

Pessoal, passamos por uma aplicação bastante tensa aqui. Vocês vão reparar que ela tem um detalhe de funcionamento que eu vou deixar para vocês tentarem corrigir (a resposta estará escondida aqui embaixo).

Analisem a aplicação com calma. Estudem os pontos de implementação e comparem com a implementação anterior. Você vão ver que utilizamos os mesmos conceitos, aplicados com alguma variação.

Pessoal espero que vocês estejam gostando do conteúdo e conseguindo imaginar como aplicar esses conceitos em suas aplicações. Vamos continuar estudando e praticando. A prática é fundamental para a evolução de vocês como pessoas desenvolvedoras, engenheiras e arquitetas de solução.

<img src="https://static1.cbrimages.com/wordpress/wp-content/uploads/2023/03/pokemon_horizons_introdduces_captain_pikachu.jpg" style={{ display: 'block', marginLeft: 'auto', maxHeight: '50vh', marginRight: 'auto', marginBottom: '24px' }}/>

## Solução do Problema

<details> 
        <summary mdxType="summary"> Solução Proposta para o Carrinho não Atualizar de Forma Automática</summary>

Pessoal se rodaram tudo até aqui, perceberam que o carrinho está funcionando, mas é preciso sair da tela e voltar para que o valor total possa ser atualizado. Isso acontece porque o MobX não consegue observar a mudança de estado do carrinho de compras. Para resolver esse problema, vamos atualizar a classe `cart_screen` para que ela possa adicionar um `Observer` no elemento `Text` que é responsável por exibir o valor total.

```dart
// cart_screen.dart
// Tela de carrinho de compras. Exibe os produtos adicionados ao carrinho e o valor total.

import 'package:flutter/material.dart';
import 'package:flutter_mobx/flutter_mobx.dart';
import 'package:mobx_carrinho/controllers/cart_controller.dart';
import 'package:mobx_carrinho/models/product_model.dart';

class CartScreen extends StatelessWidget {
  final CartController cartController;

  CartScreen({required this.cartController});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Carrinho'),
      ),
      body: Observer(
        builder: (_) {
          return ListView.builder(
            itemCount: cartController.products.length,
            itemBuilder: (context, index) {
              Product product = cartController.products[index];
              return ListTile(
                title: Text(product.name),
                subtitle: Text('R\$ ${product.price.toStringAsFixed(2)}'),
                trailing: IconButton(
                  icon: Icon(Icons.remove_shopping_cart),
                  onPressed: () {
                    cartController.removeProduct(product);
                  },
                ),
              );
            },
          );
        },
      ),
      bottomNavigationBar: BottomAppBar(
        child: Padding(
          padding: const EdgeInsets.all(8.0),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Observer(builder: (_) {
                return Text('Total: R\$ ${cartController.totalValue.toStringAsFixed(2)}');
              }),
              ElevatedButton(
                onPressed: () {
                  cartController.products.clear();
                },
                child: Text('Limpar carrinho'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
```

O Observer é um widget que vai observar as mudanças de estado do carrinho de compras. Ele é um widget que vai notificar os observadores quando o estado do carrinho de compras mudar. Para isso, ele utiliza o método `builder` para construir o widget. O método `builder` é um método que vai construir o widget toda vez que o estado do carrinho de compras mudar. Isso significa que o valor total do carrinho de compras vai ser atualizado automaticamente toda vez que um produto for adicionado ou removido do carrinho de compras.

</details> 