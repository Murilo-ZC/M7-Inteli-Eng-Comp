---
sidebar_position: 3
title: Modelos de Regressão
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Modelos de regressão são um tipo de modelo de machine learning supervisionado utilizado para prever valores contínuos. Eles são usados quando o objetivo é entender a relação entre uma variável dependente (ou variável de resposta) e uma ou mais variáveis independentes (ou variáveis preditoras). Esses modelos estimam uma função que mapeia as variáveis preditoras para a variável de resposta, permitindo prever valores para novos dados baseados nos padrões identificados durante o treinamento.

**Regressão Linear Simples** é o modelo mais básico de regressão, onde há apenas uma variável preditora. A relação entre a variável preditora e a variável dependente é modelada como uma linha reta. O modelo tenta encontrar os coeficientes dessa linha que minimizam a diferença (ou erro) entre os valores previstos e os valores reais da variável dependente. 

**Regressão Linear Múltipla** é uma extensão da regressão linear simples para o caso onde há mais de uma variável independente. Este modelo é útil quando a variável de resposta é influenciada por múltiplos fatores, e o objetivo é entender como cada uma dessas variáveis contribui para o valor final da previsão.

Além da regressão linear, existem outros tipos de modelos de regressão, como a **Regressão Logística** (utilizada para prever probabilidades e, portanto, é popular em problemas de classificação binária), **Regressão Polinomial** (que modela relações não lineares entre as variáveis), e **Regressão Ridge** e **Lasso** (que incluem penalidades para evitar overfitting em casos de modelos com muitas variáveis independentes). Cada tipo de regressão é escolhido com base na natureza dos dados e no tipo de relação que se espera capturar entre as variáveis preditoras e a variável dependente.

## Princípais Métricas de Avaliação

As principais métricas de avaliação para modelos de regressão variam dependendo do tipo de problema e da natureza dos dados. Essas métricas são utilizadas para quantificar a precisão e a qualidade das previsões feitas pelo modelo. As mais comuns incluem:

### 1. **Erro Quadrático Médio (MSE - Mean Squared Error)**: 
   - O MSE é uma das métricas mais usadas para avaliar modelos de regressão. Ele mede a média dos quadrados das diferenças entre os valores reais e os valores previstos pelo modelo. 
   - Um MSE menor indica um modelo melhor, já que representa uma menor discrepância entre as previsões e os valores reais. No entanto, como os erros são elevados ao quadrado, o MSE é mais sensível a outliers.

### 2. **Erro Absoluto Médio (MAE - Mean Absolute Error)**: 
   - O MAE mede a média das diferenças absolutas entre os valores reais e os valores previstos. 
   - Esta métrica é mais intuitiva que o MSE porque mede os erros em unidades de medida originais, sem elevá-los ao quadrado. É menos sensível a outliers em comparação com o MSE, mas não penaliza grandes erros de forma tão severa.

### 3. **R² (Coeficiente de Determinação)**: 
   - O R² mede a proporção da variação na variável dependente que é explicada pelas variáveis independentes no modelo. Ele varia entre 0 e 1, onde 1 indica que o modelo explica toda a variação dos dados, e 0 indica que o modelo não explica nenhuma variação.

### 4. **Erro Quadrático Médio da Raiz (RMSE - Root Mean Squared Error)**: 
   - O RMSE é a raiz quadrada do MSE, o que traz a métrica de volta à escala original dos valores de saída, facilitando a interpretação.
   - É uma métrica que combina a facilidade de interpretação do MAE com a sensibilidade a outliers do MSE.

### 5. **Erro Percentual Absoluto Médio (MAPE - Mean Absolute Percentage Error)**: 
   - O MAPE mede o erro médio em termos percentuais entre os valores reais e os valores previstos.
   - É útil para entender o erro em termos percentuais, mas pode ser instável se houver valores reais próximos de zero, o que leva a grandes valores de erro percentual.

Essas métricas fornecem diferentes perspectivas sobre o desempenho do modelo e, em muitos casos, várias métricas são usadas em conjunto para obter uma visão mais completa da qualidade das previsões. A escolha da métrica certa depende do contexto do problema e dos objetivos específicos do modelo.

## Exemplos de Implementação

A escolha da métrica de avaliação mais apropriada para um modelo de regressão depende do tipo de problema que você está tentando resolver e da natureza dos dados com os quais você está trabalhando. Aqui estão alguns exemplos de problemas de regressão com suas respectivas métricas de avaliação:

### 1. **Previsão de Preços Imobiliários**
   - **Problema**: Prever o preço de casas com base em características como tamanho, localização, número de quartos, etc.
   - **Métricas Usadas**: 
     - **MAE** (Erro Absoluto Médio): Ideal para este caso porque fornece uma média simples dos erros em termos de unidades monetárias, o que é facilmente interpretável pelos *stakeholders*.
     - **RMSE** (Erro Quadrático Médio da Raiz): Também útil aqui porque penaliza mais os grandes erros. Isso é importante em previsões de preços imobiliários, onde grandes discrepâncias (*overestimations* ou *underestimations*) podem ter impactos financeiros significativos.

### 2. **Previsão de Consumo de Energia**
   - **Problema**: Prever o consumo de energia elétrica de uma cidade em determinado horário do dia.
   - **Métricas Usadas**:
     - **MSE** (Erro Quadrático Médio): Pode ser uma boa escolha porque, em problemas como este, grandes desvios entre a previsão e o valor real podem indicar problemas graves no modelo, e o MSE amplifica esses desvios devido ao quadrado dos erros.
     - **R² (Coeficiente de Determinação)**: Útil para entender a proporção de variação no consumo de energia que o modelo consegue explicar. Um valor alto de R² indicaria que o modelo é capaz de capturar bem as tendências gerais de consumo.

### 3. **Previsão de Demanda de Produtos**
   - **Problema**: Prever a demanda por produtos em um supermercado.
   - **Métricas Usadas**:
     - **MAPE** (Erro Percentual Absoluto Médio): Como a demanda por diferentes produtos pode variar amplamente (desde itens de baixo custo e alta rotatividade até itens caros e de baixa rotatividade), o MAPE é útil para normalizar esses erros em termos percentuais, oferecendo uma visão geral da precisão do modelo em diferentes escalas.
     - **MAE**: Também pode ser relevante se a interpretação dos erros em termos absolutos for mais importante para o negócio, como quando a demanda deve ser transformada diretamente em números de estoque.

### 4. **Previsão de Riscos de Crédito**
   - **Problema**: Prever a probabilidade de um cliente inadimplir em um empréstimo.
   - **Métricas Usadas**:
     - **Regressão Logística** (usada para previsão de probabilidade de eventos binários) seria avaliada através de **AUC-ROC** (área sob a curva ROC) ou **Precisão/Recall** se o problema principal for a distinção entre bons e maus pagadores. No entanto, se o modelo prevê uma variável contínua, como o score de crédito, métricas como **MAE** ou **RMSE** podem ser usadas.
     - **R²**: Pode ser menos útil neste contexto, já que estamos mais interessados na precisão das previsões individuais do que na proporção de variância explicada.

### 5. **Previsão de Séries Temporais para Vendas**
   - **Problema**: Prever as vendas semanais de um produto ao longo do tempo.
   - **Métricas Usadas**:
     - **RMSE**: Comum em séries temporais, onde o erro absoluto e a penalização de grandes erros são importantes, especialmente se as previsões estão sendo usadas para planejamento estratégico.
     - **MAPE**: Pode ser relevante se as vendas variam amplamente ao longo do tempo, permitindo que o modelo seja avaliado de forma consistente em diferentes níveis de venda.

### 6. **Previsão de Temperatura**
   - **Problema**: Prever a temperatura diária em uma cidade.
   - **Métricas Usadas**:
     - **MSE** ou **RMSE**: Comuns nesse tipo de previsão, pois a precisão em graus Celsius é fácil de interpretar e grandes desvios podem representar falhas significativas no modelo.
     - **R²**: Também pode ser utilizado para entender quanto da variabilidade nas temperaturas diárias o modelo consegue explicar.

Cada um desses exemplos destaca como as diferentes métricas de avaliação são escolhidas com base nas características específicas do problema e nos requisitos dos stakeholders. A interpretação dos resultados e o impacto dos erros no contexto do negócio ou da aplicação também influenciam fortemente essa escolha.

