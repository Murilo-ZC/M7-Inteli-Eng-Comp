---
sidebar_position: 1
title: Encontro 07 - Gerenciamento de estado com framework híbrido
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Ola pessoas 📱🐼😎!!

Chegamos em um momento que vamos fazer um swift no nosso foco. Vamos deixar de observar o backend da nossa aplicação com maior foco e vamos olhar nossa aplicação móvel.

Para isso, vamos estudar o gerenciamento de estado com um framework híbrido, o MobX. A ideia é que vocês possam entender como funciona o MobX e como ele pode ser utilizado para gerenciar o estado da sua aplicação móvel. Contudo, antes de iniciarmos nosso estudo com MobX, vamos avaliar uma forma de estruturar melhor nosso código da aplicação, utilizando o padrão de arquitetura `Model View Controller (MVC)`.

<img src="https://archives.bulbagarden.net/media/upload/thumb/2/25/Friede_Captain_Pikachu.png/800px-Friede_Captain_Pikachu.png" style={{ display: 'block', marginLeft: 'auto', maxHeight: '50vh', marginRight: 'auto', marginBottom: '24px' }}/>

Dentro deste encontro, temos como principais objetivos:
- Compreender o que é o MVC e como ele pode ser utilizado para estruturar o código da aplicação móvel;
- Refatorar a aplicação "hello world" para utilizar o padrão MVC;
- Compreender o que é o gerenciamento de estado de uma aplicação e como ele deve ser utilizado;
- Compreender o que é o MobX e como ele deve ser utilizado em uma aplicação.

:::tip[Implementem!!]

Pessoal, acredito que já está bastante claro nessa altura do campeonato, mas é sempre bom reforçar: **implementem**! A prática é fundamental para a fixação do conteúdo e para a evolução de vocês como pessoas desenvolvedoras, engenheiras e arquitetas de solução.

:::

> Poxa Murilo, mas a gente não vai trabalhar com mais nada do backend?

Aqui está nosso maior truque! Vamos sim! Contudo, durante nossos autoestudos e aqui no material vamos conversar bastante sobre eles. Por enquanto, durante nossos encontros, vamos focar nossas energias na aplicação móvel.