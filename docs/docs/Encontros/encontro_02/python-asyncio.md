---
sidebar_position: 4
title: Python AsyncIO
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Python AsyncIO

Legal, agora temos o conceito alinhado conosco, vamos falar sobre o AsyncIO do Python.

Ele é uma biblioteca padrão do Python que fornece suporte para escrever código assíncrono usando a sintaxe async/await. Foi introduzido na versão 3.4 do Python e é uma das maneiras mais fáceis de escrever código assíncrono.

:::tip[Para saber mais]

> Mas Murilo por que você está já está adicionando o material do para saber mais?

Porque eu quase esqueci na última seção, então para não esquecer, já estou adicionando aqui.

- [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)
- [Python Asyncio: The Complete Guide](https://superfastpython.com/python-asyncio/)
- [Coroutines and Tasks](https://docs.python.org/3/library/asyncio-task.html)

:::

Para os próximos exemplos, vamos discultir alguns conceitos de utilização do AsyncIO. Ele, por padrão vem na biblioteca padrão do Python, então não é necessário instalar nada. CONTUDO, é uma boa prática fazer a separação de um ambiente virtual para cada projeto, então vamos criar um ambiente virtual para o nosso projeto.

```bash
python3 -m venv env
source env/bin/activate
```

Ao longo dos exemplos, vamos precisar de bibliotecas adicionais, ai elas podem ser adicionadas neste ambiente virtual, mantendo nossa instalação limpa.

<img src="https://i.pinimg.com/originals/a6/b1/44/a6b144b6a9795f845c8638d842cfb815.gif" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom: '24px' }}/>

## Primeiro Código com AsyncIO

Primeiro programa:

```python
# O asyncio é uma biblioteca que permite a execução de tarefas assíncronas
# Ela é uma biblioteca padrão do Python 3.5 ou superior
import asyncio


# Para marcarmos uma função como assíncrona, utilizamos a palavra-chave async
async def print_com_delay(tempo, mensagem):
    # A função asyncio.sleep é uma função assíncrona que suspende a execução da função por um determinado tempo
    await asyncio.sleep(tempo)
    print(mensagem)


# Agora configuramos uma função principal que irá chamar a função assíncrona
async def main():
    # Adicionando um marcador para ver o tempo de execução da função
    print("Início da execução:", asyncio.get_event_loop().time())
    # Realiza uma chamada bloqueante para a função assíncrona
    await print_com_delay(1, "Olá")
    await print_com_delay(2, "Mundo")
    # Adicionando um marcador para ver o tempo de execução da função
    print("Fim da execução:", asyncio.get_event_loop().time())

  

# Para chamar a função principal, utilizamos o método que cria um evento de loop e executa a função principal
asyncio.run(main())
```

Quanto utilizamos a palavra chave `async` estamos definindo que aquela função é especial e pode ser iniciada e pausada pelo `event-loop`  do sistema. Quando utilizamos o operador `await` estamos esperando que a operação assíncrona termine para que a execução do código possa avançar. É uma chamada do tipo `bloqueante`.

A chamada `asyncio.run(main())` é o entry-point de chamada para o nosso sistema. É ele que permite nossa execução assíncrona.  O elemento fundamental para a execução do código assíncrono é o `event-loop`. Ele é fundamental para a coordenar a execução das tarefas sem bloquear o fluxo de execução principal do programa.

O `event-loop` é uma estrutura que continuamente monitora e processa eventos de diferentes fontes, como entradas, chamadas de rede ou mesmo eventos de temporizadores. Ele é o responsável por acionar os `handlers` ou `callbacks` específicos de cada evento. A chamada `asyncio.run` é responsável por fazer a criação do `event-loop` e executar a corrotina principal.

São responsabilidades do `event-loop`:
- Agendar e executar as tarefas assíncronas (corotinas)
- Lidar com operações de I/O
- Lidar com temporizações e timeouts
- Liberar eventos para a fonte correspondente (handler)

Outro exemplo de utilização:

```python
import asyncio

async def task(nome, tempo_delay):
    print(f"Task {nome} iniciada")
    await asyncio.sleep(tempo_delay)
    print(f"Task {nome} finalizada")
    return f"Task {nome} finalizada"

async def main():
    # Cria uma lista de tarefas
    tasks = [
        task("A", 1),
        task("B", 5),
        task("C", 3)
    ]

    # Envia todas as tarefas para execução
    # O método gather() aguarda todas as tarefas serem finalizadas
    # Ele também lança a execução de todas as tarefas
    results = await asyncio.gather(*tasks)
    print(results)

# Cria um novo evento de loop
asyncio.run(main())

```

## Síntaxe Async/Await

O `async/await` foi adicionado no Python 3.5.
As corrotinas são funções especiais que podem ter sua execução suspensa e resumida, possibilitando sua execução concorrente.
A palavra chave `await` serve para aguarda o fim da execução de uma operação assíncrona. Quando desejamos aguardar a execução de mais de uma corrotina de forma simultânea, nós devemos utilizar o `asyncio.gather()`.
A partir da versão 3.8 do Python, o conceito de `Native Coroutine` foi implementado. Elas utilizam uma versão dedicada do opcode do await, resultando em um desempenho melhor e e redução do overhead de execução do código. A sintaxe `async/await` permanece a mesma, mas a sua implementação foi melhorada.
As `Async Comprehensions` permitem utilizar o recurso de list comprehensions para criar listas utilizando o retorno de corrotinas. O mesmo pode ser utilizado com a criação de dicionários e sets.

```python
# Utiliza o recurso de list comprehension para criar uma lista de tarefas utilizando um gerado assíncrono
import asyncio

async def quadrado_assincrono(n):
    await asyncio.sleep(1)
    return n * n

async def main():
    numeros = [1, 2, 4, 8, 16, 32]
    numeros_quadrados = [await quadrado_assincrono(numero) for numero in numeros]
    print(numeros_quadrados)

    # Versão otimizada com o método gather
    numeros_quadrados = await asyncio.gather(*[quadrado_assincrono(numero) for numero in numeros])
    print(numeros_quadrados)
    
if __name__ == "__main__":
    asyncio.run(main())
```

Chamando corotinas simples:

```python
# Agendando e executando uma corotina simples

import asyncio

async def corotina(nome, delay):
    print(f"Corotina {nome} iniciada - {asyncio.get_event_loop().time()}")
    await asyncio.sleep(delay)
    print(f"Corotina {nome} finalizada - {asyncio.get_event_loop().time()}")
    

async def main():
    # Prepara as corotinas utilizando o método create_task
    # O método create_task() cria uma tarefa para execução de uma corotina, mas não a executa. A execução é feita pelo loop de eventos.
    corotina1 = asyncio.create_task(corotina("A", 1))
    corotina2 = asyncio.create_task(corotina("B", 2))

    # Aguarda a execução das corotinas, mas não bloqueia a execução
    await corotina1
    await corotina2

# Cria um novo evento de loop
if __name__ == "__main__":
    asyncio.run(main())
```

> ***IMPORTANTE:*** existe uma diferença entre chamar e aguardar uma corotina e criar uma task com ela utilizando o `asyncio.create_task()`. Quando apenas chamamos as corotinas, elas são executadas conforme a execução dos pontos anteriores do programa vai terminando (o await fica com um comportamento `bloqueante`). Quando invocamos elas criando corotinas (não apenas as funções assíncronas puras), o `await` não é bloqueante.


```python
# Agendando e executando uma corotina simples

import asyncio

async def corotina(nome, delay):
    print(f"Corotina {nome} iniciada - {asyncio.get_event_loop().time()}")
    await asyncio.sleep(delay)
    print(f"Corotina {nome} finalizada - {asyncio.get_event_loop().time()}")
    

async def main():
    # Prepara as corotinas utilizando o método create_task
    # O método create_task() cria uma tarefa para execução de uma corotina, mas não a executa. A execução é feita pelo loop de eventos.
    corotina1 = asyncio.create_task(corotina("A", 1))
    corotina2 = asyncio.create_task(corotina("B", 2))

    # Aguarda a execução das corotinas, mas não bloqueia a execução
    await corotina1
    await corotina2

    # Chamada do exemplo anterior, mas sem a criação de tarefas
    corotina3 = corotina("C", 3)
    corotina4 = corotina("D", 4)
    await corotina3
    await corotina4
    

# Cria um novo evento de loop
if __name__ == "__main__":
    asyncio.run(main())
```

Saída da execução do código:

```sh
> python corotina-simples.py
Corotina A iniciada - 428855.359
Corotina B iniciada - 428855.359
Corotina A finalizada - 428856.359
Corotina B finalizada - 428857.375
Corotina C iniciada - 428857.375
Corotina C finalizada - 428860.375
Corotina D iniciada - 428860.375
Corotina D finalizada - 428864.39
```

Podemos criar nosso próprio `event-loop` e controlar sua execução:

```python
# Programa para lidar com a execução de multiplas corotinas
import asyncio

async def corotina(nome_arquivo):
    print(f"Corotina {nome_arquivo} iniciada - {asyncio.get_event_loop().time()}")
    await asyncio.sleep(2)
    print(f"Corotina {nome_arquivo} finalizada - {asyncio.get_event_loop().time()}")
    return f"Corotina {nome_arquivo} finalizada"

async def main():
    # Cria uma lista com os nomes dos arquivos
    arquivos = ["arquivo1.txt", "arquivo2.txt", "arquivo3.txt", "arquivo4.txt"]
    chamada_download = [corotina(arquivo) for arquivo in arquivos]
    # # Esse método está deprecado, mas ainda é utilizado para aguardar a execução de todas as corotinas
    # # Utiliza o método wait() para aguardar a execução de todas as corotinas
    # finalizada, pendente = await asyncio.wait(chamada_download, return_when=asyncio.ALL_COMPLETED)

    # # Exibe o resultado da execução
    # for corotina_finalizada in finalizada:
    #     print(corotina_finalizada.result())
    
    # Versão não deprecada
    # Utiliza o método gather() para aguardar a execução de todas as corotinas
    resultados = await asyncio.gather(*chamada_download)
    for resultado in resultados:
        print(resultado)

if __name__ == "__main__":
    asyncio.run(main())
```

## Gerenciamento de Tasks com AsyncIO

As Tasks são os blocos de construção para executar e gerenciar as operações utilizando o AsyncIO. As Tasks são um wrapper adicionado nas corotinas para trazer mais funcionalidades de controle a elas.

```python
# Lidando com o gerenciamento de tasks no Python com Asyncio

import asyncio

# Cria uma rotina
async def rotina(delay):
    print(f"Rotina iniciada - {asyncio.get_event_loop().time()}")
    await asyncio.sleep(delay)
    print(f"Rotina finalizada - {asyncio.get_event_loop().time()}")
    return f"Rotina finalizada"

# Cria a função principal
async def main():
    # Cria duas tarefas para serem executadas
    tarefa1 = asyncio.create_task(rotina(1))
    tarefa2 = asyncio.create_task(rotina(2))

    await asyncio.sleep(1)

    # Cancela a execução da tarefa 2
    tarefa2.cancel()

    # Aguarda a execução das tarefas
    await asyncio.gather(tarefa1, tarefa2, return_exceptions=True)

# Cria o evento de loop
if __name__ == "__main__":
    asyncio.run(main())
```

É possível verificar o estado de uma task. É importante notar algumas coisas:
- Erros e exceções nas corotinas devem ser tratados dentro do event loop.
- Se o result() de uma task for acessado antes dela terminar, vai resultar no lançamento de uma exceção.

```python
# Verifica o estado de uma task

import asyncio

async def corotina1(nome):
    await asyncio.sleep(3)
    return nome

async def corotina2(nome):
    # Corotina que lança uma exceção
    await asyncio.sleep(5)
    raise ValueError("Erro na corotina")
    return nome

# Função principal
async def main():
    try:
        # Cria as tasks
        task1 = asyncio.create_task(corotina1("A"))
        task2 = asyncio.create_task(corotina2("B"))

        # Aguarda a execução das tasks
        await asyncio.sleep(1)

        # Verifica o estado das tasks - verificando se elas estão terminadas
        print(task1.done())
        print(task2.done())

        # Exibe o estado atual das tasks
        print(task1._state)
        print(task2._state)

        # Aguarda a execução das tasks
        await asyncio.gather(task1, task2, return_exceptions=True)

        # Verifica o estado das tasks
        print(task1.done())
        print(task2.done())

        # Exibe o resultado das tasks
        print(task1.result())
        print(task2.result())
    except ValueError as e:
        print(f"Erro: {e}")

# Cria um novo evento de loop
if __name__ == "__main__":
    asyncio.run(main())
```

Uma comparação de tempo interessante:

```python
import asyncio

async def compute():
    return sum(i * i for i in range (10000000))

async def main():
    print(asyncio.get_event_loop().time())
    result1 = await compute()
    print(asyncio.get_event_loop().time())
    result2 = sum(i * i for i in range (10000000))
    print(asyncio.get_event_loop().time())

    print(result1, result2)

if __name__ == "__main__":
    asyncio.run(main())
```

## Trabalhando com AsyncIO para Requisições de Rede

Utilizando os conceitos presentes no AsyncIO, é possível construir aplicações cliente-servidor que conseguem lidar com uma quantidade muito mais elevada de requisições, melhorando a utilização dos recursos disponíveis.
O AsyncIO aceita conexões seguras de SSL/TLS.
Exemplo de servidor assíncrono:

```python
# Construção de um servidor assincrono utilizando apenas o Asyncio
import asyncio

# Definição do método que será chamado para lidar com clientes
async def handle_client(reader, writer):
    # Os elementos reader e writer são objetos que permitem a leitura e escrita de dados
    # O método read() é utilizado para ler dados do cliente
    # O valor informado é a quantidade de bytes que serão lidos
    data = await reader.read(1024)
    message = data.decode()
    print(f"Dados Recebido: {message}")

    resposta = "Ola Cliente!"
    writer.write(resposta.encode())
    # O método drain() é utilizado para garantir que todos os dados foram escritos
    await writer.drain()
    print("Fechando Conexão")
    writer.close()
    await writer.wait_closed()

# Criação do servidor
async def main():
    # Cria uma instância de servidor que escuta na porta 8888
    server = await asyncio.start_server(
        handle_client, 'localhost', 8888)
    
    # Cria um loop para aguardar a conexão de clientes
    # A criação com o método async with garante que o servidor será fechado corretamente
    async with server:
        # Inicia o servidor
        await server.serve_forever()

# Inicia o servidor
if __name__ == "__main__":
    asyncio.run(main())
```

Exemplo de um cliente para conectar nesse servidor assíncrono:

```python
import asyncio

async def connect_to_server():
    reader, writer = await asyncio.open_connection('localhost', 8888)
    message = "oi tudo bem ai?"
    writer.write(message.encode())
    await writer.drain()
    data = await reader.read(1024)
    print(f"Resposta do servidor: {data.decode()}")
    writer.close()
    await writer.wait_closed()

if __name__ == "__main__":
    asyncio.run(connect_to_server())
```

É possível utilizar o AsyncIO para manipular bases de dados também. Utilizando drivers assíncronos, é possível realizar consultas e chamadas as bases de dados de forma concorrente.
Alguns drivers assíncronos:
- AsyncPG (for PostgreSQL)
- Motor (for MongoDB)
- Aio_pika (for RabbitMQ)
- Asyncio Redis (for Redis)
- aiosqlite (for sqlite)


Exemplo de execução de código utilizando o aisqlite. Primeiro é necessário instalar a dependencia.

```sh
python -m pip install aiosqlite
```

E o código para manipular os dados:

```python
import asyncio
import aiosqlite

# Cria uma corotina para criar as tabelas
async def criar_tabelas(db_name, table_name):
    async with aiosqlite.connect(db_name) as db:
        await db.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY, mensagem TEXT)")
        await db.commit()

# Insere alguns dados aleatórios em uma tabela
async def inserir_dados(db_name, table_name):
    async with aiosqlite.connect(db_name) as db:
        for i in range(10):
            await db.execute(f"INSERT INTO {table_name} (mensagem) VALUES ('Mensagem {i}')")
        await db.commit()

# Pega dados que estão na tabela
async def pegar_dados(db_name, table_name):
    async with aiosqlite.connect(db_name) as db:
        async with db.execute(f"SELECT * FROM {table_name}") as cursor:
            return [row async for row in cursor]

# Função principal
async def main():
    db_name = "banco.db"
    table_name = "mensagens"
    await criar_tabelas(db_name, table_name)
    await inserir_dados(db_name, table_name)
    dados = await pegar_dados(db_name, table_name)
    print(dados)

# Roda a função principal
if __name__ == "__main__":
    asyncio.run(main())
```

Em algumas situações, vai ser necessário utilizar código assíncrono com código síncrono.  É possível realizar a troca de informações entre estes dois sistemas. Esse comportamento é especialmente necessário quando algumas bibliotecas ou trechos do código que serão utilizados são síncronos.
Primeiro instalando a dependência da biblioteca `requests`:

```sh
python -m pip install requests
```

```python
# Exemplo de utilização de código sincrono em conjunto com código assincrono
import asyncio
import requests

# Cria uma corotina que fica como uma ponte entre código assincrono e código sincrono
async def fetch_url(url):
    # Pega o loop de eventos
    loop = asyncio.get_event_loop()
    # Roda a função requests.get de forma sincrona, mas em uma thread separada
    return await loop.run_in_executor(None, requests.get, url)

# Função principal
async def main():
    url = "https://www.google.com"
    # Os parênteses são necessários para pegar o texto da resposta.
    # Eles garantem que a função fetch_url seja chamada primeiro.
    data = (await fetch_url(url)).text
    print(data)

# Roda a função principal
if __name__ == "__main__":
    asyncio.run(main())
```

Utilizar o método `run_in_executor` previne que o `event-loop`possa ser bloqueado durante a execução do código.

## Aplicando Testes com AsyncIO

É possível escrever código de testes para as aplicações assíncronas também. Para tal, vai ser necessário utilizar as bibliotecas `pytest` e `pytest-asyncio`.

```sh
python -m pip install pytest pytest-asyncio
```

O código da função:

```python
# Exemplo de teste de função assíncrona com pytest
import asyncio

async def fetch_data():
    await asyncio.sleep(2)
    return 'data'
```

O código do teste:

```python
# Cria o teste para a função fetch_data
import pytest
from exemplo_teste_assincrono import fetch_data

# Marca a função como de teste e com comportamento assincrono
@pytest.mark.asyncio
async def test_fetch_data():
    data = await fetch_data()
    assert data == 'data', "Resultado esperado não foi retornado."
```

Para executar os códigos de teste:

```sh
python -m pytest teste-exemplo-teste-assincrono.py
```

## Projetos Assíncronos

Para trabalhar com requisições HTTP de forma assíncrona, uma biblioteca que pode ser utilizada é a `aiohttp`. Ela pode ser instalada com:

```sh
python -m pip install aiohttp
```

E um exemplo de código:

```python
import asyncio
import aiohttp

# Cria a função que irá fazer a requisição
async def fetch( url):
    # Cria uma sessão. Ela representa uma conexão com o servidor
    async with aiohttp.ClientSession() as session:
        # Faz a requisição
        async with session.get(url) as response:
            # Lê o conteúdo da resposta
            # Neste exemplo, o conteúdo está sendo retornado como texto
            return await response.text()
        
# Cria a função principal
async def main():
    url = 'https://www.uol.com.br'
    html = await fetch(url)
    print(html)


# Cria o event-loop
if __name__ == '__main__':
    asyncio.run(main())
```

É possível realizar um conjunto de requisições de forma assíncrona utilizando a biblioteca.

```python
import asyncio
import aiohttp

# Cria a função que irá fazer a requisição
async def fetch( url):
    # Cria uma sessão. Ela representa uma conexão com o servidor
    async with aiohttp.ClientSession() as session:
        # Faz a requisição
        async with session.get(url) as response:
            # Lê o conteúdo da resposta
            # Neste exemplo, o conteúdo está sendo retornado como texto
            return await response.text()
        
# Cria a função principal
async def main():
    urls = ['https://www.uol.com.br', 'https://www.globo.com', 'https://www.terra.com.br']
    # Cria uma lista de tarefas
    tasks = [asyncio.create_task(fetch(url)) for url in urls]
    html = await asyncio.gather(*tasks)
    print(html)


# Cria o event-loop
if __name__ == '__main__':
    asyncio.run(main())
```

É possível adicionar um controle de número de retentativas que a função vai fazer se não for possível receber os dados de resposta quando uma requisição é realizada.

```python
import asyncio
import aiohttp

# Cria a função que irá fazer a requisição
async def fetch( url, max_tries=3):
    # Tenta fazer a requisição até 3 vezes
    tentativa = 0
    while tentativa < max_tries:
        try:
            # Cria uma sessão. Ela representa uma conexão com o servidor
            async with aiohttp.ClientSession() as session:
                # Faz a requisição
                async with session.get(url) as response:
                    # Lê o conteúdo da resposta
                    # Neste exemplo, o conteúdo está sendo retornado como texto
                    return await response.text()
        except aiohttp.ClientError as e:
            tentativa += 1
            # Espera 1 segundo antes de tentar novamente
            await asyncio.sleep(1)
        return None
    
# Cria a função principal
async def main():
    urls = ['https://www.uol.com.br', 'https://ww.globo.com', 'https://www.terra.com.br']
    # Cria uma lista de tarefas
    tasks = [asyncio.create_task(fetch(url)) for url in urls]
    htmls = await asyncio.gather(*tasks)
    # Verifica os retornos
    for html in htmls:
        if html:
            print('Resultado obtido com sucesso')
        else:
            print('Erro ao acessar a URL')


# Cria o event-loop
if __name__ == '__main__':
    asyncio.run(main())
```

