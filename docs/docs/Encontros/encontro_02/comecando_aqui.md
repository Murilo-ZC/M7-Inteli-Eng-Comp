---
sidebar_position: 2
title: Modelos de Machine Learning
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Modelos de machine learning são estruturas matemáticas e estatísticas que aprendem a partir de dados para fazer previsões ou tomar decisões. Um modelo de machine learning é uma função que mapeia entradas (dados) para saídas (predições ou classificações) com base em padrões extraídos dos dados de treinamento. Esses modelos podem variar em complexidade, desde simples regressões lineares até redes neurais profundas com milhões de parâmetros.

O processo de criação de um modelo de machine learning envolve várias etapas: coleta e preparação dos dados, escolha do algoritmo apropriado, treinamento do modelo com os dados de treinamento, e validação e teste para garantir que o modelo generaliza bem para novos dados. Durante o treinamento, o modelo ajusta seus parâmetros internos para minimizar um erro ou maximizar uma métrica de desempenho, o que é feito através de técnicas de otimização, como o gradiente descendente. O resultado final é um modelo que pode ser utilizado para fazer previsões em dados que nunca viu antes, aplicando os padrões e relações que aprendeu durante o treinamento.

## Modelos Supervisionados

Os modelos são treinados em um conjunto de dados rotulado, onde a resposta correta é fornecida para cada exemplo de treinamento. O objetivo é aprender uma função que mapeia entradas para saídas corretas. Alguns exemplos:

- ***Regressão Linear:*** Um modelo simples que tenta prever um valor contínuo baseado em uma ou mais variáveis independentes.
- ***Classificação:*** Modelos como regressão logística, árvores de decisão, e máquinas de vetores de suporte (SVM), que são usados para classificar dados em categorias discretas.
- ***Redes Neurais:*** Estruturas complexas que simulam o funcionamento do cérebro humano e são utilizadas em tarefas como reconhecimento de imagem e processamento de linguagem natural.

## Modelos Não Supervisionados

Os modelos são usados quando os dados de treinamento não possuem rótulos. Eles tentam encontrar padrões ou estruturas ocultas nos dados. Exemplos incluem:

- ***Clustering (Agrupamento):*** Modelos como k-means ou hierárquico que agrupam dados semelhantes juntos.
- ***Redução de Dimensionalidade:*** Técnicas como Análise de Componentes Principais (PCA) ou t-SNE, que reduzem a quantidade de variáveis nos dados enquanto retêm a maior parte da informação relevante.
- ***Modelos de Mistura Gaussiana:*** Utilizados para identificar subpopulações dentro de um conjunto de dados sem rótulos.

## Feature Engineering

**Feature Engineering** é o processo de criar, transformar e selecionar as características (features) mais relevantes a partir dos dados brutos para melhorar o desempenho de um modelo de machine learning. As features são as variáveis independentes que o modelo usa para fazer previsões. O objetivo do feature engineering é fornecer ao modelo a representação mais informativa e relevante dos dados, permitindo que ele capture os padrões mais importantes.

Este processo envolve várias etapas, como a criação de novas features a partir de dados existentes (por exemplo, extraindo a hora do dia a partir de uma marca de tempo), a transformação de features (como normalizar valores ou converter dados categóricos em numéricos), e a seleção de features que são mais relevantes para o problema em questão, enquanto se descarta aquelas que são irrelevantes ou redundantes. Técnicas como one-hot encoding, binning, transformação logarítmica, e PCA (Análise de Componentes Principais) são frequentemente utilizadas nesta fase.

O sucesso de um modelo de machine learning muitas vezes depende da qualidade das features que são utilizadas. Um bom trabalho de feature engineering pode melhorar significativamente a precisão e a generalização do modelo, enquanto features mal escolhidas podem levar a um desempenho insatisfatório, mesmo com modelos complexos. Por isso, o feature engineering é considerado uma arte e uma ciência no campo do machine learning, exigindo tanto conhecimento do domínio dos dados quanto habilidades técnicas para manipulação e análise dos mesmos.