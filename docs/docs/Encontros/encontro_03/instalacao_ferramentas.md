---
sidebar_position: 2
title: Instalação das Ferramentas
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Ferramentas utilizadas

Pessoal para o desenvolvimento de aplicações mobile com o Flutter, vamos precisar de algumas ferramentas aqui. Primeiro vou apresentar a lista das ferramentas que vamos utilizar ao longo dos encontros:

- [Android Studio](https://developer.android.com/studio): Ele facilita a instalação do SDK do Android, do emulador e de outras ferramentas que vamos precisar para o desenvolvimento de aplicações Android.
- [Flutter](https://flutter.dev/docs/get-started/install): O framework que vamos utilizar para o desenvolvimento de aplicações mobile.
- [VSCode](https://code.visualstudio.com/): Editor de código que vamos utilizar para o desenvolvimento das aplicações.

:::note[IDE utilizada]

Pessoal a escolha da IDE é um decisão importante que pode tanto impactar na produtivo quanto na qualidade do código. Por isso, a escolha do VSCode é uma sugestão, mas fiquem a vontade para testar e utilizar o Android Studio. Ele é uma IDE muito poderosa e que facilita o desenvolvimento de aplicações Android.

Não estou sugerindo a sua utilização, devido a quantidade de recursos que ele demanda. Contudo, é uma sugestão para quem deseja utilizar uma IDE mais completa.

<img src="https://media.licdn.com/dms/image/D4E12AQHtREb53PNwQg/article-cover_image-shrink_720_1280/0/1688953588350?e=2147483647&v=beta&t=d_QlKY1SubahwH-nEVcY-ML7dpDIq0QWikzDMxm8UtI" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom: '24px' }}/>

:::

Para a instalação das ferramentas, vamos seguir os passos recomendados por cada um dos fabricantes. O [@ViniciosLugli](https://github.com/ViniciosLugli) gentilmente disponibilizou um passo a passo de instalação de algumas das ferramentas. Recomendo que vocês verifiquem ele também.

Aqui tem um vídeo para a instalação das ferramentas que eu achei que pode ajudar vocês:

<iframe style={{
            display: 'block',
            margin: 'auto',
            width: '100%',
            height: '50vh',
        }} src="https://www.youtube.com/embed/dpppZ9ySJSY?si=4zracZC70qafEtgm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Já neste vídeo temos a configuração do emulador:

<iframe style={{
            display: 'block',
            margin: 'auto',
            width: '100%',
            height: '50vh',
        }} src="https://www.youtube.com/embed/gNYNvHUSW1s?si=nSfLzEiofUt_2Ubv" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

### Observações na Instalação

Pessoal depois de instalado o Android Studio, no momento que vamos escolher qual a versão do Android no menu `SDK Platforms`, vamos escolher a versão `Android 13.0 Tiramisu`. No meu `SDK Tools`, selecionar `Android SDK Command-line Tools (lastest)`, `Google Play services` e `Google Web Driver`. Selecionar a opção `Apply` e depois `OK`.

Agora vamos configurar nosso dispositivo virtual. Ainda no menu `More Actions` do Android Studio, selecionar `Virtual Device Manager`. Vamos criar um novo dispositivo virtual, selecionando a opção `Create Virtual Device`. Vamos escolher a opção `Pixel 4` e a versão `Android 13.0 Tiramisu`. Vai ser necessário realizar o downlaod da imagem selecionada para prosseguir. Selecionar a opção `Next` e depois `Finish`.

Depois de iniciado, é possível que o emulador leve um tempo BASTANTE GRANDE para iniciar. Basta aguardar e depois você já poderá utilizar o emulador!

Depois, com o VS Code aberto, vamos instalar a extensão do Flutter. Para isso, vamos na aba de extensões e pesquisar por `Flutter`. Vamos instalar a extensão e depois vamos instalar a extensão do `Dart`.

Pronto! Agora vocês estão prontos para começar a desenvolver nossas aplicações com o Flutter! Bons estudos e qualquer dúvida, estou a disposição!