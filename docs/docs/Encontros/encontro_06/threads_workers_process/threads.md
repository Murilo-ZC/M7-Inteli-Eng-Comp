---
sidebar_position: 2
title: Threads
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Threads

Threads são a menor unidade de processamento que um sistema operacional pode agendar. Um processo pode ter vários threads, cada um com seu próprio contador de programa, registradores e pilha, mas compartilhando o mesmo espaço de endereço. Threads são úteis para melhorar a performance de aplicações, pois permitem que um processo execute várias tarefas simultaneamente.

<img src="https://media4.giphy.com/media/UiH6lsIgUhZU7uNKFR/200w.gif?cid=6c09b9526b7d15ezf4qco8bbm7a7i6b5v2rfgalkmikoexm1&ep=v1_gifs_search&rid=200w.gif&ct=g" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom: '24px' }}/>

> Murilo, mas o que é um thread?

Um thread é um fluxo de execução dentro de um processo. Cada thread tem seu próprio contador de programa, registradores e pilha, mas compartilha o mesmo espaço de endereço com outros threads do mesmo processo. Isso significa que os threads podem acessar as mesmas variáveis e recursos do processo, mas têm seu próprio estado de execução.

<img src="https://av-eks-lekhak.s3.amazonaws.com/media/__sized__/article_images/thread2_H7Y4wjm-thumbnail_webp-600x300.webp" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom: '24px' }}/>


### Talk is cheap, show me the code!

Vamos ver um exemplo de como criar um thread em Python. Vamos avaliar um pouco como funciona a criação de threads e como podemos utilizá-las.

```python
# Hello World em Python com Threads

import threading
import time

# Cria o comportamento de uma thread
def hello():
    print("Hello World!")
    time.sleep(3)

# Realiza a criação de uma thread
t = threading.Thread(target=hello)

# Inicia a thread
t.start()

# Espera a thread terminar
t.join()

print("Fim do programa")
```

Neste exemplo, criamos uma função `hello` que imprime "Hello World!" e dorme por 3 segundos. Em seguida, criamos uma thread `t` que executa a função `hello` e a iniciamos com `t.start()`. Por fim, esperamos a thread terminar com `t.join()` e imprimimos "Fim do programa".


<img src="https://math.hws.edu/javanotes/c12/threads-vs-subroutines.png" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom: '24px' }}/>


> Pô Murilo! Mais não vi nada de mais nesse exemplo. O que tem de especial nisso?

Calma, jovem treinador e treinadora! O exemplo é simples, mas ilustra bem como criar e utilizar threads em Python. Threads são úteis para executar tarefas em paralelo e melhorar a performance de aplicações. Em aplicações mais complexas, é comum utilizar threads para realizar operações de I/O, como leitura e escrita em arquivos, conexões de rede e acesso a banco de dados.

Vamos modificar o exemplo para tornar ele um pouco mais interessante.

```python
# Hello World em Python com Threads

import threading
import time

# Cria o comportamento de uma thread
def hello():
    print("Hello World!")
    time.sleep(3)

# Cria um conjunto de threads
threads = []

# Realiza a criação de uma thread
for i in range(10):
    threads.append(threading.Thread(target=hello))

# Inicia as threads
for t in threads:
    t.start()

# Espera as threads terminar
for t in threads:
    t.join()

print("Fim do programa")

```

Neste exemplo, criamos uma lista `threads` e criamos 10 threads que executam a função `hello`. Em seguida, iniciamos todas as threads com `t.start()` e esperamos todas as threads terminarem com `t.join()`. Dessa forma, podemos executar a função `hello` 10 vezes em paralelo.

Repare que, ao utilizar threads, podemos executar várias tarefas simultaneamente e melhorar a performance de nossa aplicação. No entanto, é importante ter cuidado ao utilizar threads, pois elas compartilham o mesmo espaço de endereço e podem causar problemas de concorrência se não forem utilizadas corretamente.

> Legal, mas da para utilizar threads para fazer alguma outra coisa?

Sim, jovem treinador e treinadora! Threads são úteis para realizar operações de I/O, como leitura e escrita em arquivos, conexões de rede e acesso a banco de dados, lembra!??. Vamos utilizar threads para realizar uma operação de I/O em Python.

```python
# Exemplo de uso de threads em Python para realizar download de arquivos
import threading
import requests

def download_arquivo(url):
    print('Baixando arquivo: ', url)
    # Realiza o download do arquivo utilizando o pacote requests
    response = requests.get(url)
    # Salva o arquivo
    with open(url.split('/')[-1], 'wb') as f:
        f.write(response.content)
    print('Download finalizado: ', url)

# Cria um conjunto de imagens para fazer o download
imagens = [
    'https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/025.png',
    'https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/001.png',
    'https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/004.png',
    'https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/009.png',
    'https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/150.png',
]

# Cria uma thread para cada imagem
threads = []

for imagem in imagens:
    t = threading.Thread(target=download_arquivo, args=(imagem,))
    t.start()
    threads.append(t)

# Espera todas as threads terminarem
for t in threads:
    t.join()

print('Download de todas as imagens finalizado')
```

:::tip[O pacote requests]

Pessoal, é necessário instalar o pacote `requests` para realizar o download dos arquivos. Para instalar o pacote, execute o comando `pip install requests`. CONTUDO!!! Lembrem de utilizar um ambiente virtual para instalar as dependências do projeto.

:::

Reparem que, neste exemplo, criamos uma função `download_arquivo` que realiza o download de um arquivo a partir de uma URL. Em seguida, criamos uma lista `imagens` com URLs de imagens de Pokémon e criamos uma thread para cada imagem que executa a função `download_arquivo`. Dessa forma, podemos realizar o download de várias imagens simultaneamente e melhorar a performance da aplicação.

As threads possuem um ciclo de vida e podem ser iniciadas, pausadas, retomadas e finalizadas. É importante ter cuidado ao utilizar threads, pois elas compartilham o mesmo espaço de endereço e podem causar problemas de concorrência se não forem utilizadas corretamente.


<img src="https://media.geeksforgeeks.org/wp-content/uploads/20240318155846/Lifecycle-and-States-of-a-Thread-in-Java-1.png" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom: '24px' }}/>

### Threads em Python

Python possui um módulo `threading` que permite a criação e utilização de threads. O módulo `threading` fornece uma interface de alto nível para a criação e gerenciamento de threads em Python. Com o módulo `threading`, podemos criar threads, iniciar threads, esperar threads terminarem e realizar outras operações com threads. A documentação oficial do módulo `threading` pode ser encontrada [aqui](https://docs.python.org/3/library/threading.html).

Para aprofundamento sobre threads em Python, recomendo a leitura da documentação oficial do módulo `threading` e do artigo [An Intro to Threading in Python](https://realpython.com/intro-to-python-threading/).
