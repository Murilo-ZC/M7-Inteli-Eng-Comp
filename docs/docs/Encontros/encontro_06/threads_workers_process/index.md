---
sidebar_position: 1
title: Threads, Workers e Processos
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Sistema Operacional

Um sistema operacional é um software que gerencia os recursos de hardware e software de um computador. Ele fornece uma interface entre o hardware e os programas de aplicação, permitindo que os usuários interajam com o computador e executem tarefas de forma eficiente.

### Boot do Sistema Operacional

Quando um sistema operacional é inicializado, ele cria um processo chamado de processo de inicialização. Este processo é responsável por iniciar todos os outros processos e threads que serão executados no sistema. O boot do sistema operacional é um processo complexo que envolve a execução de vários programas e scripts, como o carregamento do kernel, a inicialização dos drivers de hardware e a configuração do ambiente de execução.

<img src={useBaseUrl("/img/threads_workers_process/Bootloader-Flowchart.png")} style={{ display: 'block', marginLeft: 'auto', maxHeight: '60vh', marginRight: 'auto', marginBottom: '24px' }}/>

No processo de boot do sistema operacional, primeiro são carregados os drivers básicos do sistema de arquivos. Com eles, é possível utilizar ler e escrever no disco. Em seguida, o kernel é carregado na memória e inicializado. O kernel é o núcleo do sistema operacional, responsável por gerenciar os recursos do sistema, como a memória, o processador e os dispositivos de entrada e saída. Por fim, o kernel inicia o processo de inicialização, que é responsável por iniciar todos os outros processos e threads do sistema.

Agora que entendemos o processo de boot do sistema operacional, vamos falar um pouco mais sobre threads.

### Como o sistema operacional realiza uma ação?

A execução de uma tarefa por um sistema operacional é um processo que envolve várias etapas, desde o início da tarefa até a sua conclusão.

1. **Início da Tarefa**:
   Uma tarefa geralmente começa quando um usuário ou um sistema inicia um programa. Isso pode ser feito clicando em um ícone, executando um comando em um terminal, ou por meio de uma tarefa programada.

2. **Criação do Processo**:
   Quando um programa é iniciado, o sistema operacional cria um novo processo. Este processo inclui um espaço de endereço (memória alocada para o programa), os códigos executáveis do programa, e os dados associados a ele. O sistema operacional também aloca recursos necessários, como handles de arquivos e conexões de rede.

3. **Carregamento do Programa**:
   O sistema operacional carrega o código executável do programa do disco para a memória. Isso inclui ler o código binário do programa (como um arquivo .exe no Windows ou um arquivo binário no Linux) e os dados necessários para a execução.

4. **Criação de Threads**:
   Dentro de cada processo, o sistema operacional pode criar uma ou mais threads. Cada thread representa um caminho de execução independente dentro do processo. A criação de múltiplas threads permite que o processo realize multitarefa dentro de si mesmo, executando várias operações em paralelo ou de forma concorrente.

5. **Escalonamento**:
   O scheduler do sistema operacional é responsável por determinar qual thread de qual processo será executada em um determinado momento. O escalonamento é baseado em vários fatores, como prioridade da thread, justiça (fairness), e políticas específicas do sistema operacional.

6. **Execução**:
   Uma vez que uma thread é selecionada pelo scheduler, ela recebe tempo de CPU para executar suas instruções. Se o processo estiver em um sistema com múltiplos núcleos, várias threads podem ser executadas realmente em paralelo. Caso contrário, o sistema operacional simula paralelismo alternando rapidamente entre as threads (multithreading).

7. **Interrupções e Chamadas de Sistema**:
   Durante a execução, o processo pode precisar de recursos adicionais do sistema operacional, como ler um arquivo ou enviar dados pela rede. Essas operações são realizadas através de chamadas de sistema, que são interfaces fornecidas pelo sistema operacional para realizar tarefas que envolvem recursos do sistema.

8. **Terminação**:
   Uma tarefa é concluída quando a thread principal do processo termina sua execução, seja terminando naturalmente após executar todas as suas instruções, seja por ser terminada por uma chamada de sistema ou devido a um erro. Quando uma tarefa termina, o sistema operacional limpa os recursos usados, fecha handles de arquivo e libera a memória utilizada pelo processo.

Essas etapas compõem o ciclo de vida básico de uma tarefa em um sistema operacional, permitindo que os computadores executem múltiplas tarefas de forma eficiente e controlada.

### Paralelismo e Concorrência

O paralelismo e a concorrência são conceitos fundamentais em sistemas operacionais e programação de computadores. Eles descrevem a capacidade de um sistema de executar múltiplas tarefas simultaneamente e de forma eficiente.

- **Paralelismo**:
  O paralelismo refere-se à capacidade de um sistema de executar múltiplas tarefas ao mesmo tempo, aproveitando os recursos de hardware disponíveis. Isso pode ser feito em sistemas com múltiplos núcleos de processamento, onde cada núcleo pode executar uma tarefa separada de forma independente.


- **Concorrência**:
   A concorrência refere-se à capacidade de um sistema de gerenciar múltiplas tarefas de forma eficiente, mesmo que elas não sejam executadas simultaneamente. Isso pode ser feito através de técnicas como multitarefa, multithreading e programação assíncrona, que permitem que várias tarefas sejam executadas de forma concorrente, alternando rapidamente entre elas.


<img src="https://miro.medium.com/v2/resize:fit:962/format:webp/0*gNXjJonOTkqPDaIw.gif" style={{ display: 'block', marginLeft: 'auto', maxHeight: '60vh', marginRight: 'auto', marginBottom: '24px' }}/>

<img src="https://miro.medium.com/v2/resize:fit:962/format:webp/1*o9s_kvTIVFbP8NanzqvBsA.gif" style={{ display: 'block', marginLeft: 'auto', maxHeight: '60vh', marginRight: 'auto', marginBottom: '24px' }}/>
