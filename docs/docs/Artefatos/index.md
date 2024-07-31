---
sidebar_position: 2
title: Artefatos
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Resumo dos Artefatos

Aqui pessoal vou colocar um resumo dos artefatos. 

:::danger[ATUALIZAÇÃO A CAMINHO]
Eles serão atualizados no ADALOVE ainda, peço um pouco de paciencia para essa modificação.
:::

Os nossos artefatos serão entregues seguindo os padrões do desenvolvimento ágil, com entregas de valor a cada sprint. Para cada uma das etapas do projeto, teremos artefatos específicos que serão entregues, com valor incremental em cada uma delas.

Pessoal um ponto muito importante que deve estar sempre claro para vocës é que a entrega de valor é o que importa. Não adianta entregar um monte de artefatos se eles não agregam valor ao projeto. Estou colocando aqui quais são os artefatos esperados para cada sprint, mas vocês devem, como equipe de desenvolvimento, verificar qual valor será entregue em cada sprint.

<img class="image-intro" src="https://i.pinimg.com/originals/22/81/36/228136787949a85c103a630c753726aa.gif" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto' }}/>

## Sprint 1

:::tip[Objetivo da Sprint]
 Proposta de Modelo de Predição em Versão Notebook (conhecimento prévio).
:::

Está sprint tem por objetivo entregar um modelo de predição em versão notebook. O modelo deve ser construído com base nos dados fornecidos e deve ser validado com o cliente. A documentação do modelo deve ser entregue, com a descrição do problema, a descrição dos dados, a descrição do modelo e a descrição dos resultados. 

A metodoologia de CRISP-DM deve ser seguida, com a construção do modelo de predição, a avaliação do modelo e a implementação do modelo.

Os dados do modelo, taxa de acerto, taxa de erro, matriz de confusão e curva ROC devem ser apresentados.


### Artefato - Entendimento do Negócio

:::danger[ATUALIZAÇÃO A CAMINHO]
Eles serão atualizados no ADALOVE ainda, peço um pouco de paciencia para essa modificação.
:::

### Artefato - Economia Circular e Mapeamento do Ciclo de Produção e Consumo

Realizar mapeamento (incluindo levantamento e representação visual interativa) de matérias-primas, recursos, processos e impactos (sociais e ambientais) implicados na fabricação, logística, utilização, reutilização, reciclagem e descarte (incluindo possibilidades adequadas e inadequadas) dos componentes na atividade produtiva do parceiro de negócio. Os itens da entrega serão:

1. Levantamento de requisitos de visualização para o projeto (quais as necessidades, opções e possibilidades de acesso e visualização de dados para o projeto?).

2. A partir do briefing e material fornecido pelo parceiro, realizar o levantamento de matérias-primas, recursos, processos e impactos (sociais e ambientais) envolvidos na atividade fim do parceiro.

3. Partindo da compreensão da relação entre os elementos no processo produtivo, elaborar um infográfico interativo que inclua, em sua representação:
- Ciclo principal atual de produção e suas variações e subdivisões;
- Indicativos e justificativas para os principais pontos de fragilidade e risco (em que contextos do ciclo produtivo há mais chances de acontecerem problemas na cadeia? Por quê?);
- Se aplicável, tipos de usuário e permissões de acesso à informação (quem deve acessar determinados dados e em qual contexto?).

O grupo apresentará e justificará um infográfico interativo que deve descrever com clareza o ciclo produtivo e seus pontos de risco e fragilidade, apontando também impactos sociais e ambientais do ciclo produtivo. As fontes de dados representados devem ser referenciadas. 

1. Entendimento do problema; qualidade e detalhamento dos dados levantados sobre o ciclo de produção e consumo. (peso 3)

2. Apresentação, de forma didática, dos dados levantados de modo a oferecer um panorama geral do ciclo produtivo, contextualizando-o ao tema de ESG e economia circular. (peso 4)

3. Fundamentação dos dados em referências. (peso 3)

### Artefato - Requisitos de viabilidade técnica

Realizar a análise de requisitos e elaborar um documento preliminar de viabilidade técnica. Apresentar a visão geral do sistema e seus principais componentes. Os itens da entrega serão: análise de requisitos, viabilidade técnica e proposta geral do sistema.
A documentação deve ser atualizada no arquivo markdown disponível no repositório da equipe no GitHub, sempre na branch principal e com uma tag referente à entrega do sprint. 

1. Apresentar quais são os requisitos funcionais do sistema. (peso 2)
2. Apresentar quais são os requisitos não funcionais do sistema. (peso 2)
3. Apresentar o estudo da viabilidade técnica realizada. (peso 2)
4. Definição clara do objeto da proposta geral do sistema. (peso 2)
5. Descrição objetiva dos elementos gerais que vão compor a solução inicial proposta (diagrama de blocos). (peso 2)

### Artefato - Primeiro modelo de predição

Construir e documentar um modelo de predição utilizando as ferramentas apresentadas até o momento. Ele deve ser construído utilizando um notebook Python. As métricas de avaliação do modelo devem ser apresentadas em sua documentação.

O modelo deve ser construído utilizando os dados fornecidos pelo parceiro. Todo o processo deve ser documentado seguindo a metodologia CRISP-DM. Verificar mais detalhes no material de apoio do projeto: [link](https://murilo-zc.github.io/M7-Inteli-Eng-Comp/Artefatos/).

A modelagem deve ser construída utilizando a metodologia [CRISP-DM](https://www.datascience-pm.com/crisp-dm-2/). Das etapas propostas na metodologia, está implementação vai da etapa 1 até a etapa 5. Elas devem estar bem caracterízadas na documentação do modelo.

A construção de cada uma das etapas, deve trazer consigo uma explicação clara para as escolhas realizadas e as métricas de avaliação que sustentam a escolha do modelo. Incluir essas informações na documentação do modelo. A documentação do modelo não deve estar apenas nos notebooks desenvolvidos. Ela deve ser acessível na documentação do projeto.

:::danger[IMPORTANTE: Não esqueça a privacidade]

Cuidado para não deixar informações sensíveis publicamente expostas. Notebooks não devem estar públicos e a documentação do projeto não deve conter informações do parceiro que possam caracterizar ele.

:::

***Barema de avaliação:***

| Grupo de Avaliação | Descrição | Intervalo de Nota |
| --- | --- | --- |
| Não Iniciou | Não entregou o artefato ou apenas entregou um notebook sem conteúdo relacionado. | 0.0 - 1.0 |
| Iniciou | Iniciou a construção do modelo, mas não justificou nenhuma das escolhas e não apresentou nenhuma métrica de avaliação do modelo. | 1.1 - 3.0 |
| Em Andamento | Iniciou a construção do modelo, mas não justificou as escolhas realizadas e não apresentou as métricas de avaliação do modelo. | 3.1 - 5.0 |
| Atende | Construiu o modelo, justificou todas as escolhas e apresentou todas as métricas de avaliação do modelo. | 5.1 - 9.0 |
| Supera | Construiu o modelo, justificou todas as escolhas e apresentou todas as métricas de avaliação do modelo. Além disso, apresentou um modelo com bom desempenho dentro das métricas apresentadas. | 9.1 - 10.0 |


## Sprint 2

:::tip[Objetivo da Sprint]
Deploy do Modelo com uma API de Interface, Modelo implementado com rede neural recorrente
:::

Está sprint tem por objetivo aprimorar os modelos apresentados até aqui. As comparações quanto a evolução do modelo devem ser apresentadas. A documentação do modelo deve ser atualizada, com a descrição do problema, a descrição dos dados, a descrição do modelo e a descrição dos resultados.

Além disso, a implementação de uma API de interface deve ser realizada, com a integração do modelo de predição. O modelo deve ser implementado com uma rede neural recorrente. A API deve ser implementada utilizando o framework FastAPI. O modelo deve ser capaz de receber uma requisição com os dados necessários para fazer a predição e retornar a predição.

O modelo deve ser treinado utilizando os dados fornecidos pelo parceiro. O modelo deve ser avaliado utilizando as métricas de avaliação definidas na documentação do modelo. Deve ser apresentado a documentação da API e a documentação do modelo. Verificar mais detalhes no material de apoio do projeto: [link](https://murilo-zc.github.io/M7-Inteli-Eng-Comp/Artefatos/).

***Barema de avaliação:***

| Grupo de Avaliação | Descrição | Intervalo de Nota |
| --- | --- | --- |
| Não Iniciou | Não entregou a implementação do modelo e nenhuma API de acesso. | 0.0 - 1.0 |
| Iniciou | Implementou parcialmente o modelo sem utilizar rede recorrente e a API de acesso. | 1.1 - 3.0 |
| Em Andamento | Possui um modelo sem utilizar rede recorrente e uma API implementados parcialmente. A API não atende todas as requisições corretamente e o desempenho do modelo não apresenta um desempenho satisfatório. | 3.1 - 5.0 |
| Atende | Construiu o modelo utilizando rede recorrente, justificou todas as escolhas e apresentou todas as métricas de avaliação do modelo. Implementou uma API para sua utilização que responde corretamente as requisições enviadas para ela. | 5.1 - 9.0 |
| Supera | Construiu o modelo utilizando rede recorrente, justificou todas as escolhas e apresentou todas as métricas de avaliação do modelo. Além disso, apresentou um modelo com bom desempenho dentro das métricas apresentadas. | 9.1 - 10.0 |


## Sprint 3

:::tip[Objetivo da Sprint]
Dockerização da Aplicação e construção de Datalake
:::

Nessa sprint, a aplicação deve ser dockerizada, com a construção de um datalake para armazenamento dos dados. A documentação do sistema deve ser atualizada, com a descrição do problema, a descrição dos dados, a descrição do modelo e a descrição dos resultados.

A aplicação ainda estará em execução local, com a integração do modelo de predição.

| Grupo de Avaliação | Descrição | Intervalo de Nota |
| --- | --- | --- |
| Não Iniciou | Não implementou a solução dockerizada e não entregou o Datalake. | 0.0 - 1.0 |
| Iniciou | Implementou parcialmente o Datalake, mas não dockerizou a solução. | 1.1 - 3.0 |
| Em Andamento | Iniciou o processo de dockerização e implementação do Datalake. O Datalake ainda não está totalmente implementado e os elementos dockerizados ainda não estão complementamente integrados. | 3.1 - 5.0 |
| Atende | A solução está dockerizada e o Datalake foi implementado corretamente. | 5.1 - 9.0 |
| Supera | Além da implementação dockerizada e do Datalake, implementou um sistema de monitoramento da saúde das instâncias, permitindo verificar se ele está em funcionamento. | 9.1 - 10.0 |

## Sprint 4

:::tip[Objetivo da Sprint]
Implementação do ETL, Datawarehouse, Pipeline de treinamento, Dashboard de visualização
:::

Nesta sprint, o processo de ETL (Extract, Transform, Load) deve ser implementado, com a construção de um datawarehouse para armazenamento dos dados. Um pipeline de treinamento deve ser construído, com a integração do modelo de predição.

Todo o processo será implementado localmente. Além disso, um dashboard de visualização deve ser construído, com a apresentação dos dados e dos resultados do modelo.

## Sprint 5

:::tip[Objetivo da Sprint]
Cloud
:::

Nesta sprint, a aplicação será migrada para a nuvem, com a implementação de um pipeline de treinamento e de um dashboard de visualização. A documentação do sistema deve ser atualizada, com a descrição do problema, a descrição dos dados, a descrição do modelo e a descrição dos resultados.