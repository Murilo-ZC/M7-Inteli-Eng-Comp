---
sidebar_position: 3
title: Processos
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Processos

Processos são a unidade de execução de um sistema operacional. Cada processo tem seu próprio espaço de endereçamento, registradores, contador de programa e pilha. Isso significa que cada processo é isolado dos demais, não podendo acessar diretamente a memória ou recursos de outros processos.

Quando estamos utilizando processos, cada processo é independente e não compartilha recursos com outros processos. Isso significa que, se um processo falhar, os demais processos não são afetados. No entanto, a criação e gerenciamento de processos é mais custosa em termos de recursos do sistema, pois cada processo requer seu próprio espaço de endereçamento e recursos.

<img src="https://upload.wikimedia.org/wikipedia/commons/2/25/Concepts-_Program_vs._Process_vs._Thread.jpg" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom: '24px' }}/>

### Criando Processos em Python

Vamos criar nosso primeiro processo em Python. Para isso, vamos utilizar o módulo `multiprocessing`, que nos permite criar e gerenciar processos em Python.

```python
# Exemplo de uso de processos em Python

import os
import time
import multiprocessing

# Função que será executada em um processo
def funcao_processo():
    print(f'Processo {os.getpid()} iniciado')
    time.sleep(2)
    print(f'Processo {os.getpid()} finalizado')


if __name__ == '__main__':
    print(f'Processo principal {os.getpid()} inicializado')

    # Criação de um processo
    processo = multiprocessing.Process(target=funcao_processo)
    processo.start()

    print(f'Processo principal {os.getpid()} finalizado')

    # Aguarda o término do processo
    processo.join()

```

Neste exemplo, criamos uma função `funcao_processo` que imprime o ID do processo, dorme por 2 segundos e imprime novamente o ID do processo. Em seguida, criamos um processo `processo` que executa a função `funcao_processo` e o iniciamos com `processo.start()`. Por fim, aguardamos o término do processo com `processo.join()`.

Aqui temos um ponto importante: o `if __name__ == '__main__':`. Esse trecho de código é necessário para garantir que o código dentro dele seja executado apenas no processo principal. Isso é importante para evitar que o código seja executado nos processos filhos, o que pode causar problemas de concorrência. Mais detalhes podem ser encontrados na [documentação oficial do Python](https://docs.python.org/3/library/multiprocessing.html#multiprocessing-programming).

### Compartilhamento de Recursos

Uma das vantagens de utilizar processos é que eles são isolados uns dos outros, o que significa que cada processo tem seu próprio espaço de endereçamento e recursos. No entanto, em alguns casos, pode ser necessário compartilhar recursos entre processos. Para isso, o módulo `multiprocessing` fornece mecanismos para compartilhar recursos entre processos, como `Queue`, `Pipe` e `Value`.

Vamos verificar um exemplo de como compartilhar recursos entre processos utilizando `Queue`:

```python
# Exemplo de compartilhamento de recursos entre processos em Python

import os
import time
import multiprocessing

# Função que será executada em um processo
def funcao_processo(queue):
    print(f'Processo {os.getpid()} iniciado')
    time.sleep(2)
    queue.put(f'Mensagem do processo {os.getpid()}')
    print(f'Processo {os.getpid()} finalizado')


if __name__ == '__main__':
    print(f'Processo principal {os.getpid()} inicializado')

    # Criação de uma fila para compartilhar recursos
    queue = multiprocessing.Queue()

    # Criação de um processo
    processo = multiprocessing.Process(target=funcao_processo, args=(queue,))
    processo.start()

    # Aguarda o término do processo
    processo.join()

    # Lê a mensagem da fila
    mensagem = queue.get()
    print(f'Mensagem lida: {mensagem}')

    print(f'Processo principal {os.getpid()} finalizado')
```

O que está acontecendo neste código:

1. Criamos uma função `funcao_processo` que recebe uma `queue` como argumento, dorme por 2 segundos e coloca uma mensagem na `queue`.
2. Criamos uma `queue` para compartilhar recursos entre processos.
3. Criamos um processo `processo` que executa a função `funcao_processo` e o iniciamos com `processo.start()`.
4. Aguardamos o término do processo com `processo.join()`.
5. Lemos a mensagem da `queue` com `queue.get()`.
6. Imprimimos a mensagem lida.

Utilizando `Queue`, podemos compartilhar recursos entre processos de forma segura e eficiente. Vamos verificar como podemos fazer diferentes processos compartilharem informações entre si.

```python
# Exemplo de compartilhamento de recursos entre processos em Python

import os
import time
import multiprocessing

# Função que será executada em um processo
def funcao_processo(queue):
    print(f'Processo {os.getpid()} iniciado')
    time.sleep(2)
    queue.put(f'Mensagem do processo {os.getpid()}')
    print(f'Processo {os.getpid()} finalizado')


# Função que aguarda existir mensagens em uma fila
def aguardar_mensagens(queue):
    print(f'Processo {os.getpid()} iniciado')
    mensagem = queue.get()
    print(f'Mensagem lida: {mensagem}')
    print(f'Processo {os.getpid()} finalizado')

if __name__ == '__main__':
    print(f'Processo principal {os.getpid()} inicializado')

    # Criação de uma fila
    queue = multiprocessing.Queue()

    # Criação de um processo
    processo = multiprocessing.Process(target=funcao_processo, args=(queue,))
    processo.start()

    # Criação de um segundo processo
    processo2 = multiprocessing.Process(target=aguardar_mensagens, args=(queue,))
    processo2.start()

    print(f'Processo principal {os.getpid()} finalizado')

    # Aguarda o término dos processos
    processo.join()
    processo2.join()
```

Avaliando o código acima, temos:

1. Criamos uma função `aguardar_mensagens` que recebe uma `queue` como argumento, aguarda existir mensagens na `queue` e imprime a mensagem lida.
2. Criamos um processo `processo2` que executa a função `aguardar_mensagens` e o iniciamos com `processo2.start()`.
3. Aguardamos o término dos processos com `processo.join()` e `processo2.join()`.
4. Imprimimos a mensagem lida.

Dessa forma, podemos fazer diferentes processos compartilharem informações entre si de forma segura e eficiente.

### Conclusão

Processos são uma forma de executar tarefas de forma isolada e independente em um sistema operacional. Cada processo tem seu próprio espaço de endereçamento e recursos, o que garante que um processo não afete os demais. No entanto, a criação e gerenciamento de processos é mais custosa em termos de recursos do sistema, pois cada processo requer seu próprio espaço de endereçamento e recursos.