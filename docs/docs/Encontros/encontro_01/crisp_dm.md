---
sidebar_position: 5
title: CRISP-DM
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

O CRISP-DM (Cross-Industry Standard Process for Data Mining) é uma metodologia abrangente e estruturada para orientar projetos de mineração de dados e machine learning. Desenvolvida na década de 1990, tornou-se um padrão amplamente adotado na indústria para gerenciar projetos de análise de dados. O CRISP-DM divide o processo de desenvolvimento de um projeto de mineração de dados em seis fases principais:

1. **Compreensão do Negócio:** Esta fase inicial foca na compreensão dos objetivos e requisitos do projeto do ponto de vista do negócio. Envolve definir o problema, avaliar a situação atual, estabelecer metas e desenvolver um plano de projeto.
2. **Compreensão dos Dados:** Nesta fase, os dados são coletados e explorados. Inclui a identificação de problemas de qualidade dos dados, a descoberta de insights preliminares e a detecção de subconjuntos interessantes para formar hipóteses.
3. **Preparação dos Dados:** Esta etapa cobre todas as atividades necessárias para construir o conjunto de dados final. Inclui seleção de dados, limpeza, construção de novos atributos, integração de diferentes fontes e formatação dos dados.
4. **Modelagem:** Nesta fase, várias técnicas de modelagem são selecionadas e aplicadas, e seus parâmetros são calibrados para valores ótimos. Geralmente, existem várias técnicas para o mesmo tipo de problema, e algumas podem ter requisitos específicos sobre a forma dos dados.
5. **Avaliação:** Neste estágio, o modelo (ou modelos) construído é avaliado minuciosamente e os passos executados para construí-lo são revisados para garantir que ele alcance adequadamente os objetivos de negócio. Um ponto-chave é determinar se alguma questão de negócio importante não foi suficientemente considerada.
6. **Implantação:** A criação do modelo geralmente não é o fim do projeto. O conhecimento adquirido precisa ser organizado e apresentado de uma forma que o cliente possa usar. Dependendo dos requisitos, a fase de implantação pode ser tão simples quanto gerar um relatório ou tão complexa quanto implementar um processo de mineração de dados repetível.

O CRISP-DM é particularmente valioso porque proporciona uma abordagem sistemática e estruturada para projetos de mineração de dados e machine learning. Ele também é flexível e pode ser adaptado para diferentes tipos de projetos e indústrias. Enfatiza a importância de entender o contexto de negócio antes de mergulhar na análise técnica e promove uma avaliação contínua e iterativa do processo e dos resultados.

<img src="https://upload.wikimedia.org/wikipedia/commons/b/b9/CRISP-DM_Process_Diagram.png" style={{ display: 'block', marginLeft: 'auto', maxHeight: '50vh', marginRight: 'auto', marginBottom: '24px' }}/> 

---

:::tip[IMPORTANTE: Tipos de Encoding]

<img src="https://i.pinimg.com/originals/9c/c5/3d/9cc53d773b11df8bf93737eef1b0757b.gif" style={{ display: 'block', marginLeft: 'auto', maxHeight: '50vh', marginRight: 'auto', marginBottom: '24px' }}/> 

Trazendo uma observação muito importante trazida do professor Nicola! Nem sempre faz sentindo utilizar o `One-Hot Encoding` para transformar as variáveis categóricas em variáveis numéricas. Em alguns casos, a utilização de `Label Encoding` pode ser mais adequada. O `Label Encoding` transforma as variáveis categóricas em variáveis numéricas, atribuindo um valor numérico para cada valor único da variável categórica. A escolha entre `One-Hot Encoding` e `Label Encoding` depende do tipo de variável categórica e do modelo que você está utilizando. O `One-Hot Encoding` é mais adequado para variáveis categóricas que não possuem uma ordem natural, enquanto o `Label Encoding` é mais adequado para variáveis categóricas que possuem uma ordem natural.

Recomendo fortemente a leitura do arquivo: [Converting Categorical Data into Numerical Form: A Practical Guide for Data Science](https://medium.com/@brandon93.w/converting-categorical-data-into-numerical-form-a-practical-guide-for-data-science-99fdf42d0e10)

Recomendo fortemente testar outras formas de encoding e verificar qual é a mais adequada para o seu problema.

:::