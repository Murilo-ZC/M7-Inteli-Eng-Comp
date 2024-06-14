---
sidebar_position: 3
title: Sistemas Sincronos e Assincronos
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Antes de iniciarmos nossos estudos, precisamos compreender alguns conceitos e como eles são relevantes no desenvolvimento de nossas soluções. Por diversas vezes, misturamos alguns deles, ou até utilizamos o nome de um quando estamos falando de outro. Por isso, vamos entender o que são sistemas síncronos e assíncronos.

Afinal, o que são sistemas síncronos e assíncronos?

## Sistemas Síncronos

Sistemas síncronos são aqueles em que as operações ocorrem em resposta direta a um estímulo e com requisitos estritos de tempo. Em uma execução síncrona, cada passo ou tarefa aguarda a conclusão da anterior antes de começar, e muitas vezes isso é controlado por sincronização explícita, como semáforos ou bloqueios. Isso garante que as operações ocorram de forma sequencial e ordenada. 

Aqui estão alguns aspectos importantes dos sistemas síncronos:

- **Coordenação de tempo:** Em sistemas síncronos, as operações dependem de sinais ou eventos que ocorrem em intervalos específicos e previsíveis. Isso significa que a comunicação entre diferentes componentes do sistema é feita de forma que todos os elementos "esperem" ou se sincronizem uns com os outros baseados em relógios ou cronômetros.
- **Previsibilidade:** Devido à necessidade de operações ocorrerem em tempos específicos, esses sistemas são altamente previsíveis, o que é crucial em aplicações onde a temporização é essencial, como sistemas de controle industrial, telecomunicações ou sistemas embutidos em tempo real.
- **Bloqueios e espera ativa:** Em muitos sistemas síncronos, um processo pode bloquear ou entrar em um estado de espera ativa até que um evento específico ocorra, o que pode incluir a chegada de dados ou um sinal de outro processo. Este mecanismo de sincronização ajuda a manter a ordem e a coordenação dentro do sistema.
- **Facilidade de teste e depuração:** A natureza previsível e ordenada dos sistemas síncronos facilita o teste e a depuração, pois o comportamento do sistema em diferentes momentos é mais fácil de ser previsto e analisado.

Embora haja vantagens, os sistemas síncronos podem ser menos eficientes em termos de uso de recursos, pois podem exigir que os processos esperem por eventos externos, o que pode levar a um desperdício de ciclos de CPU, especialmente se a espera ativa for utilizada.

Na figura abaixo, é possível visualizar um exemplo de sistema síncrono, onde as operações ocorrem em resposta a um estímulo e de forma sequencial. Uma operação aguarda a conclusão da anterior antes de começar.

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSD4QU4e1T-SszRZ0cDoKZWwIWpHj2u99yagdE8DjdmQ2MM3uJU4QFv7nqHoEe6SGGCpw&usqp=CAU" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom: '24px' }}/>

:::danger[Sistemas Síncronos são ruins?]	

<img src="https://i.pinimg.com/originals/e0/75/7e/e0757e7cbb89daada00a1bef54e9cf58.gif" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom: '24px' }}/>

Não seria adequado afirmar genericamente que sistemas síncronos são ruins, pois a escolha entre sistemas síncronos e assíncronos depende amplamente das necessidades específicas e do contexto de cada aplicação. Ambos os tipos de sistemas têm suas vantagens e desvantagens, e a adequação depende do que é necessário para o sistema em questão.

- Vantagens dos Sistemas Síncronos:
    - Previsibilidade: Devido à natureza ordenada e cronometrada, sistemas síncronos são altamente previsíveis, o que facilita a depuração e o teste.
    - Facilidade de entendimento: A lógica de controle em sistemas síncronos pode ser mais fácil de entender e seguir, pois as ações ocorrem em uma sequência fixa e bem definida.
    - Consistência e integridade de dados: Em ambientes onde a ordem e a integridade dos dados são críticas, como sistemas de banco de dados transacionais, a execução síncrona pode garantir que as operações sejam completadas de maneira segura e ordenada.

- Desvantagens dos Sistemas Síncronos:
    - Ineficiência de recursos: Sistemas síncronos podem levar à ineficiência, especialmente se os processos passarem muito tempo esperando por outros processos ou eventos, resultando em ociosidade de recursos.
    - Escalabilidade limitada: Em alguns casos, a necessidade de sincronização estrita pode limitar a escalabilidade do sistema, pois adicionar mais processos ou usuários pode aumentar a complexidade e o overhead de sincronização.
    - Menos flexíveis: Em ambientes dinâmicos ou com cargas de trabalho variáveis, sistemas síncronos podem não se adaptar tão bem quanto os sistemas assíncronos.

- Quando escolher sistemas síncronos:
    - Em aplicações que requerem uma sequência exata e previsível de operações.
    - Quando a integridade e a ordem dos dados são críticas e não podem ser comprometidas.
    - Em sistemas em tempo real onde o cumprimento de prazos estritos é fundamental.

- Quando evitar sistemas síncronos:
    - Em sistemas altamente escaláveis onde a latência e a ociosidade de recursos podem ser um problema.
    - Em ambientes onde as tarefas são largamente independentes e podem ser executadas de forma desacoplada.

Recomendo para vocês pessoal realizar a leitura deste artigo e desta thread sobre o tópico:
- [Synchronous vs asynchronous programming and their use cases](https://ahmedsadman.medium.com/synchronous-vs-asynchronous-programming-and-their-use-cases-88a7d2f04205)
- [Is there any proof that async/await is actually better than synchronous code?](https://www.reddit.com/r/csharp/comments/qaadm7/is_there_any_proof_that_asyncawait_is_actually/)

:::

## Sistemas Assíncronos

Os sistemas assíncronos, em contraste com os sistemas síncronos, não dependem de uma sincronização estrita de tempo entre as operações. Em vez disso, eles permitem que as operações ocorram de forma independente, sem que uma operação precise esperar diretamente pela conclusão de outra antes de iniciar. Isso confere uma flexibilidade considerável e pode melhorar a eficiência e a escalabilidade em muitos contextos.

Definição de programação assíncrona:

> Uma forma de permitir que o programa possa executar mais de uma tarefa de uma única vez, ao invés de esperar uma tarefa terminar e iniciar a próxima. Todas as tarefas são executas em conjunto.

A programa síncrona, realiza uma tarefa por vez, o que pode resultar em uma condição bloqueante para execução de alguma tarefa ou função.

Nem tudo são maravilhas, existe um tradeoff a ser considerado. Ao trabalhar com programação concorrente, alguns problemas podem acontecer:
- Race Conditions;
- Deadlocks;
- Resources Starvation (quando multiplos processos ou threads tentam acessar o mesmo conjunto de registros);

Esses problemas ocorrem principalmente quando a sincronização não está propriamente configurada. A ***Programação Assíncrona*** permite utilizar uma forma estruturada e controlada para trabalhar com concorrência. Utilizando uma arquitetura orientada a eventos e um controle explicito sobre o fluxo de execução do programa.

Benefícios da programação Assíncrona:
- Permite a execução concorrente de tarefas;
- Oferece um melhor aproveitamento de desempenho e utilização de recursos;
- Resolve os problemas de execução concorrente utilizando a aproximação de evento;
- É bastante útil em cenários que envolve a execução longa de uma requisição ou operações de I/O custosas.

Na figura abaixo, é possível visualizar um exemplo de sistema assíncrono, onde as operações ocorrem de forma independente e não sequencial. Uma operação pode iniciar antes da conclusão da anterior. Vale destacar que isso é alcançado por meio de mecanismos de controle de fluxo e eventos.

<img src="https://buildfire.com/wp-content/uploads/2023/03/Requests.png" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom: '24px' }}/>

:::warning[Programação Assíncrona é melhor que Síncrona?]

<img src="https://miro.medium.com/v2/resize:fit:1000/1*0I-RxEy9YIiWilMNRFUYMg.gif" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom: '24px' }}/>

Podemos deixar quase a mesma resposta que a da pergunta anterior, variando as características do sistema. Lembrem-se sempre que a escolha entre sistemas síncronos e assíncronos depende amplamente das necessidades específicas e do contexto de cada aplicação. Ambos os tipos de sistemas têm suas vantagens e desvantagens, e a adequação depende do que é necessário para o sistema em questão.

- Características dos Sistemas Assíncronos:
    - Independência Temporal: As tarefas ou operações em um sistema assíncrono são executadas sem a necessidade de se alinharem a um relógio central ou esperar por um evento específico. Isso permite que as tarefas sejam processadas assim que os recursos estão disponíveis ou quando um evento relevante ocorre.
    - Uso Eficiente de Recursos: Em sistemas assíncronos, os recursos não ficam ociosos esperando a conclusão de outras tarefas. Isso pode levar a uma utilização de recursos mais eficiente e a uma resposta mais rápida do sistema, especialmente em ambientes de alta carga.
    - Escalabilidade: Sem a necessidade de processamento sequencial e sincronizado, sistemas assíncronos são frequentemente mais fáceis de escalar. Eles podem lidar com um aumento no volume de operações ou usuários mais facilmente, distribuindo tarefas de forma mais flexível.
    - Complexidade de Gerenciamento de Estado: Embora ofereçam muitas vantagens, os sistemas assíncronos podem introduzir complexidade adicional no gerenciamento de estado, uma vez que o estado do sistema pode mudar em momentos inesperados, e o controle de dependências entre tarefas pode ser desafiador.
    - Desafios de Depuração: A depuração e o teste podem ser mais complexos em sistemas assíncronos devido à natureza imprevisível e não sequencial das operações. Rastrear problemas específicos ou condições de corrida pode ser difícil sem ferramentas e técnicas adequadas.

- Quando usar sistemas assíncronos:
    - Em Aplicações de Alto Volume: Como serviços web ou sistemas de processamento de mensagens onde a capacidade de lidar com muitas tarefas ou solicitações de forma independente é crucial.
    - Em Operações de I/O Intensivo: Sistemas que envolvem operações de entrada/saída intensivas, como acesso a redes ou a discos, podem beneficiar-se do modelo assíncrono para evitar bloqueios e aumentar a resposta do sistema.
    - Em Ambientes Distribuídos: Em sistemas distribuídos, especialmente em computação em nuvem, onde os componentes podem estar fisicamente separados e as latências variáveis, a assincronicidade pode ajudar a melhorar a eficiência geral.

- Quando evitar sistemas assíncronos:
    - Quando a Ordem Exata é Crítica: Em sistemas onde a sequência precisa de operações é fundamental para a integridade dos dados ou para a lógica do negócio, a abordagem assíncrona pode introduzir riscos inaceitáveis.
    - Em Ambientes com Requisitos de Tempo Real Estritos: Em aplicações onde o cumprimento de prazos precisos é crucial, a natureza imprevisível dos sistemas assíncronos pode ser um problema.

:::

## Como os Sistemas Assíncronos Funcionam?

Vamos analisar a imagem a seguir e entender como os sistemas assíncronos funcionam:

<img src="https://miro.medium.com/v2/resize:fit:1400/0*I_nlWjD6faxLrjAY.gif" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom: '24px' }}/>

Sistemas assíncronos são baseados em eventos e callbacks. Em vez de esperar que uma operação seja concluída antes de iniciar outra, o sistema pode iniciar várias operações simultaneamente e lidar com os resultados à medida que eles se tornam disponíveis. Isso é frequentemente feito por meio de callbacks, que são funções que são chamadas quando uma operação assíncrona é concluída.

> Mas Murilo, quem é que chama a função de callback? Quem lida com os eventos?

Em sistemas assíncronos, um loop de eventos é frequentemente usado para gerenciar a execução de tarefas e a chamada de callbacks. O loop de eventos é responsável por monitorar a fila de eventos e executar as funções de callback associadas a esses eventos. Isso permite que o sistema seja altamente responsivo e eficiente, pois pode lidar com várias operações concorrentes sem bloquear o thread principal.

Podemos pensar no loop de eventos como um gerenciador de fila que processa eventos à medida que eles chegam. Quando uma operação assíncrona é concluída, um evento é gerado e colocado na fila de eventos. O loop de eventos verifica continuamente a fila e executa as funções de callback associadas a esses eventos.

> Ahhhh entendi Murilo! Então é como se eu tivesse rodando várias threads ao mesmo tempo né? (AQUI EU FORCEI A BARRA NA PERGUNTA MAS É PARA VERMOS UMA DIFERENÇA IMPORTANTE)

Então, não.

Aqui está uma diferença importante entre sistemas assíncronos e sistemas baseados em threads. Em sistemas baseados em threads, cada thread tem seu próprio contexto de execução e pode executar operações de forma independente. No entanto, o uso excessivo de threads pode levar a problemas de concorrência, como condições de corrida e dead locks. Quando estamos falando de sistemas assíncronos, geralmente estamos falando de um único thread que gerencia várias operações assíncronas, o que pode ser mais eficiente e seguro em muitos casos. O tempo de execução é compartilhado entre as operações, e o loop de eventos garante que as operações sejam executadas de forma ordenada e eficiente.

A figura abaixo demonstra uma comparação entre sistemas baseados em threads e sistemas assíncronos:

<img src="https://miro.medium.com/v2/resize:fit:1189/1*k5n4Px1Pe8nbmnD-TaWvBA.png" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom: '24px' }}/>

Com o Python, podemos utilizar a biblioteca `asyncio` para trabalhar com programação assíncrona. A biblioteca `asyncio` fornece uma estrutura para escrever código assíncrono usando a sintaxe `async` e `await`. Isso permite que você escreva código que pode lidar com operações assíncronas de forma eficiente e concorrente.

<img src="https://www.scaler.com/topics/images/asyncio-python-thumbnail.webp" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom: '24px' }}/>

## Para saber mais

Pessoal vou deixar aqui mais alguns vídeos que eu recomendo para compreender a forma como os sistemas assíncronos evoluiram no Python. Eles são densos, recomendo assistir eles na ordem qu eu vou deixar aqui (menos denso para mais denso):

- Asyncio in Python - Full Tutorial (tem propaganda no meio do vídeo, mas é um bom tutorial)

<iframe width="600" height="480" max-width="80vw" src="https://www.youtube.com/embed/Qb9s3UiMSTA?si=Lj6Ga-bzgA5733XF" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style={{display: 'block', marginLeft: 'auto', maxHeight: '80vh', marginRight: 'auto', marginBottom: '16px'}}></iframe>

- Live de Python #154 - Uma introdução histórica à corrotinas PARTE 3 (AsyncIO):

<iframe width="600" height="480" max-width="80vw" src="https://www.youtube.com/embed/I8doc-MlQ9g?si=W3lMWHdG-crAwjDl" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style={{display: 'block', marginLeft: 'auto', maxHeight: '80vh', marginRight: 'auto', marginBottom: '16px'}}></iframe>

- Petr Viktorin: Building an async event loop

<iframe width="600" height="480" max-width="80vw" src="https://www.youtube.com/embed/CRPnkTv1phs?si=VGf8AiwMKqO3lhhi" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style={{display: 'block', marginLeft: 'auto', maxHeight: '80vh', marginRight: 'auto', marginBottom: '16px'}}></iframe>

