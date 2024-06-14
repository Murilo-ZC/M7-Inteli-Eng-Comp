---
sidebar_position: 4
title: Implementando RPC
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Implementando RPC

O RPC (Remote Procedure Call) é um padrão de comunicação entre processos que permite que um programa solicite a execução de um procedimento em um processo remoto. O RPC é amplamente utilizado em sistemas distribuídos para facilitar a comunicação entre serviços. Legal, mas agora, como vamos implementar ele?

Primeiro vamos criar um projeto para fazer essa implementação. Para isso, vamos utilizar o Flask para criar uma API RESTful e o gRPC para implementar o RPC. Vamos lá!

Vamos fazer a implementação proposta por [Barkhayot - Building a Flask API Gateway for gRPC Microservices: A Practical Guide](https://medium.com/@coderviewer/building-a-flask-api-gateway-for-grpc-microservices-a-practical-guide-f912aed73b94), com algumas modificações.

### Criando o Projeto

Primeiro vamos criar um `venv` para nosso projeto:

```bash
python3 -m venv venv
source venv/bin/activate
```

Legal, agora com o nosso ambiente criado, vamos instalar o FastAPI e o gRPC:

```bash
python3 -m pip install flask grpcio grpcio-tools
```

Pronto, temos nossas depencias instaladas, vamos para nossa aplicação.

### Criando a descrição 

Primeiro vamos criar um arquivo `proto` com a descrição dos elementos que serão serializados. 

:::note[O que é um arquivo `.proto`?]

Um arquivo `proto` é um arquivo de definição de protocolo que descreve a estrutura dos dados que serão serializados e desserializados. O arquivo `proto` é utilizado pelo gRPC para gerar o código necessário para serializar e desserializar os dados.

Como ele é agnóstico a linguagem, podemos utilizar o mesmo arquivo `proto` para gerar o código em Python e em outras linguagens.

Mais detalhes sobre o protocolo podem ser encontrados na [documentação oficial do gRPC](https://grpc.io/docs/what-is-grpc/introduction/).

:::

Nosso arquivo `proto` vai descrever a instância de um livro, com os campos `id`, `title` e `author`. Vamos criar o arquivo `books.proto`:

```protobuf
syntax = "proto3";

package bookstore;

service BookService {
  rpc GetBooks (GetBooksRequest) returns (GetBooksResponse);
}

message GetBooksRequest {
}

message GetBooksResponse {
  repeated Book books = 1;
}

message Book {
  string id = 1;
  string title = 2;
  string author = 3;
}
```

Vamos compreender o que está acontecendo nesse arquivo:

- `syntax = "proto3";`: indica que estamos utilizando a versão 3 do protocolo.
- `package bookstore;`: define o pacote do arquivo.
- `service BookService { ... }`: define o serviço `BookService` com o método `GetBooks`.
- `message GetBooksRequest { }`: define a mensagem de requisição para o método `GetBooks`. Nessa implementação, não temos parâmetros na requisição.
- `message GetBooksResponse { }`: define a mensagem de resposta para o método `GetBooks`. Aqui, temos um campo `books` que é uma lista de `Book`. O campo `books` é marcado com o número `1`.
- `message Book { ... }`: define a mensagem `Book` com os campos `id`, `title` e `author`. Cada campo é marcado com um número único. Esse número é utilizado pelo gRPC para serializar e desserializar os dados. Ele é importante para garantir que os dados sejam serializados e desserializados corretamente. É definido como um número inteiro positivo.

### Gerando o Código

Agora precisamos gerar o código Python a partir do arquivo `proto`. Para isso, vamos utilizar o comando `protoc` com o plugin do gRPC para Python.

No terminal, vamos executar o seguinte comando:

```bash
python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. books.proto
```

O que aconteceu aqui:

- `-I.`: indica o diretório onde o arquivo `proto` está localizado.
- `--python_out=.`: indica o diretório onde o código Python será gerado.
- `--grpc_python_out=.`: indica o diretório onde o código gRPC Python será gerado.
- `books.proto`: indica o arquivo `proto` que será utilizado para gerar o código.

Após a execução do comando, serão gerados dois arquivos: `books_pb2.py` e `books_pb2_grpc.py`. O arquivo `books_pb2.py` contém as definições das mensagens e o arquivo `books_pb2_grpc.py` contém as definições do serviço.

### Implementando o Serviço

Vamos agora criar nosso servidor gRPC. Para isso, vamos criar um arquivo `server.py` com o seguinte conteúdo:

```python
# books_server.py

import grpc
from concurrent import futures
import books_pb2
import books_pb2_grpc

class BookService(books_pb2_grpc.BookServiceServicer):
    def GetBooks(self, request, context):
        # Simulate fetching books from a database or external service
        books = [
            books_pb2.Book(id="1", title="Book 1", author="Author 1"),
            books_pb2.Book(id="2", title="Book 2", author="Author 2"),
            # Add more books as needed
        ]

        return books_pb2.GetBooksResponse(books=books)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    books_pb2_grpc.add_BookServiceServicer_to_server(BookService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC Server started. Listening on port 50051...")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
```

O que está acontecendo aqui:

- `BookService`: é a classe que implementa o serviço `BookService`. Ela possui um método `GetBooks` que retorna uma lista de livros.
- `serve`: é a função que inicia o servidor gRPC. Ela cria um servidor gRPC, adiciona o serviço `BookService` ao servidor, inicia o servidor na porta `50051` e aguarda a execução.

### Criando a interface HTTP com o Flask

Agora vamos criar uma interface HTTP com o Flask para acessar o serviço gRPC. Vamos criar um arquivo `gateway.py` com o seguinte conteúdo:

```python
# gateway.py
from flask import Flask, jsonify
import grpc
import books_pb2
import books_pb2_grpc

app = Flask(__name__)

@app.route('/api/books', methods=['GET'])
def get_books():
    try:
        # Make gRPC call to the BookService
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = books_pb2_grpc.BookServiceStub(channel)
            grpc_request = books_pb2.GetBooksRequest()
            grpc_response = stub.GetBooks(grpc_request)

        # Process gRPC response and return to the Flask app
        books_data = [{'id': book.id, 'title': book.title, 'author': book.author} for book in grpc_response.books]
        return jsonify({'books': books_data})
    except Exception as e:
        return jsonify({'message': f"Error: {e}"})
if __name__ == '__main__':
    app.run(debug=True)
```

O que está acontecendo aqui:

- `get_books`: é a função que faz a chamada gRPC para o serviço `BookService` e retorna os dados para a aplicação FastAPI.
- `with grpc.insecure_channel('localhost:50051') as channel:` : cria um canal gRPC para se comunicar com o servidor gRPC. Depois do canal criado, é possível criar um stub para chamar o serviço `BookService`. Um `stub` é um objeto que permite chamar os métodos do serviço gRPC.
- `app`: é a instância do FastAPI que define a rota `/api/books` para acessar a função `get_books`.

Agora vamos iniciar o servidor gRPC e o servidor FastAPI (sim são dois servidores rodando simultaneamente). Para isso, abra dois terminais e execute os seguintes comandos:

```bash
python3 server.py
```

```bash
python3 gateway.py
```

Agora se você acessar `http://localhost:5000/api/books` no seu navegador, você deve ver a lista de livros retornada pelo serviço gRPC.

Essa é uma primeira implementação de RPC utilizando gRPC e Flask. Existem muitas outras possibilidades e configurações que podem ser feitas para melhorar a implementação e a performance do serviço. Fique à vontade para explorar mais sobre o gRPC e Flask e experimentar diferentes configurações e implementações.
