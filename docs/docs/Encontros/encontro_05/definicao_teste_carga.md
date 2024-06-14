---
sidebar_position: 2
title: Definições de Teste de Carga
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## O que é Teste de Carga?

O teste de carga é uma técnica de teste de software que visa avaliar o comportamento de um sistema sob condições de carga específicas. O objetivo é verificar se o sistema é capaz de suportar a carga esperada, garantindo que o mesmo funcione de forma eficiente e eficaz.

> Mas Murilo, quando fazemos uma requisição com o Insomnia, Postman ou até mesmo acessamos uma página web, não estamos realizando um teste de carga?

Sim, de certa forma estamos realizando um teste de carga, porém, o teste de carga que estamos falando é um pouco mais complexo. Ele é realizado com o intuito de avaliar o comportamento do sistema sob condições de carga específicas, como por exemplo, o número de usuários simultâneos, a quantidade de requisições por segundo, entre outros.

## Por que realizar um Teste de Carga?

O teste de carga é uma etapa muito importante no ciclo de desenvolvimento de software, pois ele permite avaliar o comportamento do sistema sob condições de carga específicas, garantindo que o mesmo funcione de forma eficiente e eficaz.

Além disso, o teste de carga permite identificar possíveis gargalos e problemas de desempenho no sistema, possibilitando a correção dos mesmos antes que o sistema seja disponibilizado para os usuários finais.

## Como realizar um Teste de Carga?

Para realizar um teste de carga, é necessário seguir os seguintes passos:

1. **Definir os objetivos do teste**: Antes de iniciar o teste, é importante definir os objetivos que se deseja alcançar com o mesmo. Por exemplo, verificar se o sistema é capaz de suportar um determinado número de usuários simultâneos, a quantidade de requisições por segundo, entre outros.

2. **Definir as métricas de avaliação**: Após definir os objetivos do teste, é importante definir as métricas que serão utilizadas para avaliar o comportamento do sistema. Por exemplo, tempo de resposta, taxa de erro, entre outros.

3. **Elaborar o plano de teste**: Com os objetivos e métricas definidos, é necessário elaborar o plano de teste, que consiste em definir as condições de carga que serão aplicadas ao sistema, como por exemplo, o número de usuários simultâneos, a quantidade de requisições por segundo, entre outros.

4. **Executar o teste**: Após elaborar o plano de teste, é necessário executar o teste, aplicando as condições de carga definidas ao sistema e coletando os resultados obtidos.

5. **Analisar os resultados**: Por fim, é necessário analisar os resultados obtidos, verificando se o sistema foi capaz de suportar a carga esperada e se o mesmo funcionou de forma eficiente e eficaz.

## Métricas de Desempenho

Durante o teste de carga, é importante avaliar algumas métricas de desempenho que podem indicar possíveis problemas no sistema. Algumas das métricas mais comuns são:

- **Tempo de Resposta**: Tempo que o sistema leva para responder a uma requisição.

- **Taxa de Erro**: Porcentagem de requisições que resultaram em erro.

- **Taxa de Transferência**: Quantidade de dados transferidos por segundo.

- **Utilização de Recursos**: Porcentagem de utilização dos recursos do sistema, como CPU, memória, disco, entre outros.

## Tipos de Teste de Carga

[Tadjudin](https://medium.com/@rico098098) faz uma definição bastante interessante de tipos de teste de carga em seu trabalho [*Load Testing with Python*](https://medium.com/@rico098098/load-testing-with-python-fea13369af43). Vamos avaliar as definições que ele pontua:

### Teste de Carga

Verifica como o sistema se comporta sob uma carga específica, como por exemplo, o número de usuários simultâneos, a quantidade de requisições por segundo, entre outros.

<img src="https://miro.medium.com/v2/resize:fit:720/format:webp/1*vylgyAgdatwOn0ZyXj8WpA.png" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom: '24px' }}/>

<p style={{ textAlign:"center", marginBottom:'24px' }}>(Referência: [link](https://miro.medium.com/v2/resize:fit:720/format:webp/1*vylgyAgdatwOn0ZyXj8WpA.png))</p>

### Teste de Estresse

Verifica como o sistema se comporta sob uma carga extrema, como por exemplo, o número máximo de usuários simultâneos, a quantidade máxima de requisições por segundo, entre outros. O objetivo deste teste é verificar o limite do sistema e identificar possíveis problemas de desempenho.

<img src="https://miro.medium.com/v2/resize:fit:720/format:webp/1*dyrsK-uyeG0N7tDR0DuXSw.png" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom: '24px' }}/>

<p style={{ textAlign:"center", marginBottom:'24px' }}>(Referência: [link](https://miro.medium.com/v2/resize:fit:720/format:webp/1*dyrsK-uyeG0N7tDR0DuXSw.png))</p>

### Teste de Estabilidade (Endurance)

Verifica como o sistema se comporta sob uma carga constante, por um longo período de tempo. O objetivo deste teste é verificar se o sistema é capaz de manter o desempenho ao longo do tempo, identificando possíveis problemas de vazamento de recursos.

<img src="https://miro.medium.com/v2/resize:fit:720/format:webp/1*CtRQh9cGZX2fKTQ85KSNew.png" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom: '24px' }}/>

<p style={{ textAlign:"center", marginBottom:'24px' }}>(Referência: [link](https://miro.medium.com/v2/resize:fit:720/format:webp/1*CtRQh9cGZX2fKTQ85KSNew.png))</p>

## Considerações Finais

O teste de carga é uma etapa muito importante no ciclo de desenvolvimento de software, pois ele permite avaliar o comportamento do sistema sob condições de carga específicas, garantindo que o mesmo funcione de forma eficiente e eficaz. Aqui fizemos o estudo de algumas definições e métricas que podem ser utilizadas para elaborar nossos testes de carga.

Estudamos brevemente alguns dos tipos de teste de carga, como o teste de carga, teste de estresse e teste de estabilidade, que podem ser utilizados para avaliar o comportamento do sistema sob diferentes condições de carga.

## Recomendações de Vídeo

<iframe width="560" height="315" src="https://www.youtube.com/embed/KECr2BujqtM?si=oRaHu1C62bQQf0GE" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'24px' }}></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/RiM1GsVSbzM?si=e4IITWxzQxbbHXCo" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'24px' }}></iframe>

