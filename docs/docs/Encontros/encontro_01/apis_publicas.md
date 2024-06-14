---
sidebar_position: 5
title: Atividade em Conjunto 
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Atividade em Conjunto - Estudar APIs públicas famosas no que são REST para eles identificarem os pilares nelas

O objetivo desta atividade é explorar algumas APIs públicas e identificar os pilares REST presentes nelas. É importante verificar se as APIs seguem os princípios REST, como a utilização de verbos HTTP, códigos de status, URIs, entre outros.

Cada equipe não precisa estudar todas as APIs, mas sim escolher uma ou duas para analisar. A ideia é que, ao final, todas as APIs tenham sido estudadas por pelo menos uma equipe.

Os resultados do estudo devem ser compartilhados com os demais grupos, para que todos possam conhecer as APIs estudadas e os pilares REST identificados.

Para realização dos testes vamos utilizar o ~~[Thunder Client](https://www.thunderclient.com/)~~ [Insomnia](https://insomnia.rest/), um cliente HTTP para testar APIs RESTful. 

### Utilizando o Cliente REST

Primeiro vamos fazer o download do Insomnia, para isso acesse o site oficial do [Insomnia](https://insomnia.rest/) e faça o download da versão compatível com o seu sistema operacional. Nós vamos utilizar a versão gratuita do Insomnia, que é bem completa e atende as nossas necessidades.

<details> 
<summary mdxType="summary">Playlist de Utilização do Insomnia</summary>

<iframe width="600" height="480" max-width="80vw" src="https://www.youtube.com/embed/Dzp-oVzh_ug?si=GUUOC9oRII3fV--D" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style={{display: 'block', marginLeft: 'auto', maxHeight: '80vh', marginRight: 'auto', marginBottom: '16px'}}></iframe>

<iframe width="600" height="480" max-width="80vw" src="https://www.youtube.com/embed/6Jch0cKz6hE?si=Ips0DV0SZMrteRgl" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style={{display: 'block', marginLeft: 'auto', maxHeight: '80vh', marginRight: 'auto', marginBottom: '16px'}}></iframe>

<iframe width="600" height="480" max-width="80vw" src="https://www.youtube.com/embed/a7X3ZIdtbNc?si=1gsv7-o5FGTIsg7u" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style={{display: 'block', marginLeft: 'auto', maxHeight: '80vh', marginRight: 'auto', marginBottom: '16px'}}></iframe>


</details>

Para os nossos testes para compreender o uso da ferramenta, vamos utilizar a API [Deck of Cards](https://www.deckofcardsapi.com/), que é uma API que simula um baralho de cartas.

A tela inicial do Insomnia é a seguinte:

<img src={useBaseUrl("/img/insomnia/tela_inicial_insomnia.png")} alt="Tela Inicial do Insomnia" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'24px' }} />

Primeiro vamos criar uma collection. Uma collection no Insomnia é um conjunto de requisições HTTP que são salvas juntas sob um mesmo agrupamento. Esta coleção pode incluir chamadas GET, POST, PUT, DELETE, entre outras, permitindo ao usuário testar diferentes endpoints de uma API de forma organizada. As collections podem ser usadas para agrupar requisições que fazem parte do mesmo projeto, teste ou cenário de uso.

Os propósitos de uma Collection são:
- ***Organização:*** Facilita a organização de múltiplas requisições relacionadas a uma única API ou a múltiplas APIs que fazem parte de um mesmo sistema.

- ***Compartilhamento e Colaboração:*** Collections podem ser compartilhadas com outros desenvolvedores, promovendo colaboração em projetos de desenvolvimento de software.

- ***Testes Automatizados:*** As collections podem ser utilizadas para executar testes automatizados de APIs. Com o uso de scripts, pode-se automatizar a execução das requisições e o processamento de suas respostas.

Ja os componentes de uma Collection são:

- ***Requisições HTTP:*** Cada collection contém uma ou mais requisições HTTP, cada uma configurada com seu próprio método, URL, cabeçalhos, corpo da mensagem e parâmetros.

- ***Pastas:*** Dentro de uma collection, as requisições podem ser organizadas em pastas. Isso é útil para agrupar requisições por funcionalidade, tipo de teste, ou outros critérios.

- ***Variáveis de Ambiente:*** Collections no Insomnia permitem definir variáveis de ambiente que podem ser usadas nas requisições. Isso é particularmente útil para alternar facilmente entre diferentes configurações de ambiente, como desenvolvimento, teste e produção.

<img src={useBaseUrl("/img/insomnia/criando_collection.png")} alt="Criando uma coleção" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'24px' }} />

<img src={useBaseUrl("/img/insomnia/resultado_collection_criada.png")} alt="Tela Inicial da Collection Criada" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'24px' }} />

Vamos criar agora uma requisição utilizando o método GET para a URL `https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1`. Para isso, clique no botão `+` ao lado de `Filter` e selecione `HTTP Request`.

<img src={useBaseUrl("/img/insomnia/criando_novo_request.png")} alt="Tela Inicial da Collection Criada" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'24px' }} />

:::info[User-Agent]

O User-Agent é um cabeçalho de requisição que contém uma descrição do sistema operacional, navegador e versão do software do cliente que está fazendo a requisição. O User-Agent é utilizado pelos servidores para identificar o tipo de cliente que está fazendo a requisição e, assim, fornecer uma resposta adequada.

Entre os seus propósitosa de utilização, podemos destacar:
- Servir diferentes versões de um site (por exemplo, móvel vs. desktop).
- Bloquear certos agentes de usuário que são conhecidos por serem maliciosos.
- Coletar estatísticas sobre quais navegadores e sistemas operacionais os visitantes estão usando.
- Testes de Compatibilidade: Verificar como diferentes clientes impactam a resposta do servidor.
- Desenvolvimento Web: Assegurar que o conteúdo serve corretamente em diferentes tipos de dispositivos e navegadores.
- Segurança e Análise: Identificar requisições maliciosas ou acompanhar o uso do sistema através dos logs que registram os valores de User-Agent.

Exemplos de `User-Agent`:
- ***Chrome em um computador Windows:*** `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36`
- ***Firefox em um computador macOS:*** `Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:76.0) Gecko/20100101 Firefox/76.0`
- ***Curl Command:*** `curl/7.64.1`

:::

Como resultado, vamos obter a seguinte tela:

<img src={useBaseUrl("/img/insomnia/resultado_primeiro_request.png")} alt="Tela Inicial da Collection Criada" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'24px' }} />

Vamos criar agora um ambiente para armazenar variáveis de ambiente. O objetivo dele é permitir que diferentes valores possam ser atribuidos para variáveis e parâmetros. Ele permite também pegar o resultado de uma requisição e já colocar uma resposta obtida como um desses valores.Para isso, clique no botão `Manage Environments` e depois em `Add Environment`.

Ao criar os `Environments`, você pode definir variáveis de ambiente que podem ser usadas em suas requisições. Isso é útil para alternar facilmente entre diferentes configurações de ambiente, como desenvolvimento, teste e produção. Eles podem ser públicos, onde todos os membros da equipe podem acessar, ou privados, onde apenas você pode acessar. Quando uma collection é compartilhada, os ambientes públicos também são compartilhados.

<img src={useBaseUrl("/img/insomnia/criando-um-ambiente.png")} alt="Criando um ambiente" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'24px' }} />

Todo ambiente criado é salvo automaticamente e pode ser acessado a qualquer momento. Para alternar entre diferentes ambientes, basta selecionar o ambiente desejado no menu suspenso no canto superior direito da tela. Ele é criado utilizando um arquivo JSON, que pode ser exportado e importado para outros ambientes.

Vamos configurar a variável `baseUrl` para a URL `https://deckofcardsapi.com/api/deck/`. Para isso, clique no botão `+` ao lado de `baseUrl` e insira o valor `https://deckofcardsapi.com/api/deck/`.

```json
{
	"baseUrl":"https://deckofcardsapi.com/api/deck"
}
```

Agora vamos utilizar essa variável para fazer uma nova requisição. Clique no botão `+` ao lado de `Filter` e selecione `HTTP Request`. Na URL, insira `{{baseUrl}}/new/shuffle/?deck_count=1`.

<img src={useBaseUrl("/img/insomnia/utilizando-base-url.png")} alt="Utilizando baseUrl" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'24px' }} />

Agora, vamos vincular essa requisição com uma variável de ambiente, para conseguir guardar o resultado vindo da requisição. Para isso, vamos dar um nome para nossa requisição anterior, clicar duas vezes no nome `New Request` e alterar ele para `pede novo baralho`.

Agora vamos criar a variável que vai receber o valor do `deck_id` que é retornado na requisição. Para isso, vamos criar uma outra variável de ambiente, clicando no botão `+` ao lado de `deck_id` e inserindo o valor `""`.

```json
{
	"baseUrl":"https://deckofcardsapi.com/api/deck",
	"deck_id":""
}
```

Agora vamos configurar que o valor de retorno da requisição possa ser atribuído a ela. Para isso, vamos editar o conteúdo de `deck_id`, vamos iniciar adicionando o valor `response`, para selecionarmos a opção `Response - Body Atribute`.

<img src={useBaseUrl("/img/insomnia/editando_resposta.png")} alt="Utilizando baseUrl" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'24px' }} />

Ao confirmarmos, vamos ter uma indicação de erro, que o valor do atributo da resposta ainda não foi selecionado. Para isso, vamos clicar no elemento `response` e vamos configurar ele.

<img src={useBaseUrl("/img/insomnia/edicao_da_resposta.png")} alt="Utilizando baseUrl" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'24px' }} />

Ao clicar nele, a tela do editor de Tags será aberta. Agora, em `Request`, vamos selecionar a requisição que queremos pegar o valor, que é a `pede novo baralho`. Em `Filter (JSONPath or XPath)` vamos configurar que desejamos acessar. Vamos iniciar com `$`, que é o início do JSON, e vamos acessar o atributo `deck_id`, que é o valor que queremos pegar. Logo ao colocar o `$`, o Insomnia já nos mostra as opções disponíveis para acessar. Acessamos os campos internos utilizando o operador `.`. Portanto, para acessar o `deck_id`, vamos utilizar `$.deck_id`.	

Agora o `Trigger Behavior` é o comportamento que o Insomnia vai ter ao pegar o valor. Quando deixamos ele em `Never - never resend request`, estamos dependendo da requisição anterior ter sido realizada e então podemos utilizar o valor. Se alterarmos para `Always - resend request when needed`, a requisição será realizada quando não existir um valor para o atribuito. Vamos deixar em `Never`.

<img src={useBaseUrl("/img/insomnia/configurando-editor-tag.png")} alt="Utilizando baseUrl" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'24px' }} />

Vamos agora criar uma nova requisição para a URL `{{baseUrl}}/{{deck_id}}/return/`. Para isso, clique no botão `+` ao lado de `Filter` e selecione `HTTP Request`. Ajuste o nome da requisição para `verifica baralho`. Repare que o Insomnia já traz um preview de como fica a URL de acordo com as variáveis de ambiente.

<img src={useBaseUrl("/img/insomnia/criando-nova-requisicao.png")} alt="Utilizando baseUrl" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom:'24px' }} />

Pessoal esse é o básico para utilizarmos o Insomnia. Vamos agora fazer a atividade de estudar as APIs públicas 🐼.

Para mais informações sobre o Insomnia, acesse a [documentação oficial](https://support.insomnia.rest/). E lembrem-se, por mais que tenhamos vistos estes conceitos para o Insomina, eles são quase que diretamente aplicáveis para outros clientes REST, como o Postman.

### APIs para Estudo

Dentro do repositório [`public-apis`](https://github.com/public-apis/public-apis) do Github, é possível ver uma série de APIs públicas que podem ser utilizadas para estudo. Vamos escolher algumas APIs para estudar e identificar os pilares REST presentes nelas.

Cada equipe deve escolher uma ou duas APIs para estudar. A ideia é que, ao final, tenhamos uma boa quantidade de APIs estudadas e os pilares REST identificados em cada uma delas.

Exportem a Collection que vocês criarem para fazer o teste das APIs escolhuidas, junto com um arquivo Markdown que descreve as observações de vocês quanto cada API.

:::danger[ESSA NÃO É UMA ATIVIDADE AVALIATIVA]

O objetivo desta atividade é realizar a identificação dos pilares REST em APIs públicas. A atividade não será avaliada, mas é importante que todos participem para que possamos compartilhar conhecimento e experiências.

:::