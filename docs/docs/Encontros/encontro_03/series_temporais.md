---
sidebar_position: 2
title: Definição e Aplicações
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Quando estamos analisando dados para construção de modelos de Machine Learning, alguns dos dados coletados apresentam uma característica especial: a ***ordem temporal***. Essa informação, para o contexto do problema, é bastante relevante, pois a ordem temporal dos dados pode influenciar diretamente no comportamento do modelo.

Para este conjunto de dados, utilizamos o termo ***série temporal***. Uma série temporal é uma sequência de observações coletadas ao longo do tempo. Essas observações podem ser coletadas em intervalos regulares ou irregulares, e podem ser de diferentes tipos, como valores contínuos, categóricos ou binários, por exemplo.

<img src="https://miro.medium.com/max/810/1*_AoEVp3eqJGrJD9R-6uuNg.gif" style={{ display: 'block', marginLeft: 'auto', maxHeight: '50vh', marginRight: 'auto', marginBottom: '24px' }}/>

## Por que as séries temporais são especiais?

Como mencionado anteriormente, uma série temporal é uma coleção de observações feitas sequencialmente no decorrer do tempo. Ela traz não apenas a informação sobre o valor de cada observação, mas também sobre a ordem em que essas observações foram feitas. Isso faz com que as séries temporais sejam diferentes de outros tipos de dados, como tabelas ou imagens, por exemplo.

Quando analisamos séries temporais, estamos interessados em entender o comportamento dos dados ao longo do tempo, e como esse comportamento pode ser utilizado para fazer predições sobre o futuro. Por isso, é importante que tenhamos em mente que as séries temporais são diferentes de outros tipos de dados, e que a análise desses dados requer métodos e técnicas específicas. Muitas vezes, nossas previsões não estão apenas interessadas em saber o valor futuro de uma variável, mas também em entender como essa variável se comporta ao longo do tempo, indicando padrões e tendências que podem ser úteis para a tomada de decisões.

## Trabalhando com séries temporais

Ao trabalhar com séries temporais, é importante que tenhamos em mente que esses dados possuem uma ordem temporal, e que essa ordem é relevante para a análise. Por isso, é importante que tenhamos em mente que a ordem temporal dos dados deve ser preservada ao longo da análise, e que devemos utilizar métodos e técnicas que levem em consideração essa ordem.

Iniciamos nossa análise da mesma forma que fazemos com outros tipos de dados: coletando, explorando e visualizando os dados. Para isso, vamos utilizar o Python e a biblioteca Pandas, que nos permite trabalhar com séries temporais de forma eficiente e intuitiva. Além do Pandas, vamos utilizar outras bibliotecas para realizar as manipulações dos dados, mas elas serão apresentadas no momento adequado.