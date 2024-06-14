---
sidebar_position: 1
title: Introdução ao Módulo
slug: /
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Introdução ao Módulo

Bem vindos ao módulo 7 de Engenharia de Computação - ***Sistema de manutenção preditiva com IA e arquitetura em nuvem***.

<img class="image-intro" src="https://i.pinimg.com/originals/e8/4e/db/e84edb279472c7ab49e97ec276d4ffda.gif" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto' }}/>


Ao longo deste módulo, vamos discutir sobre alguns conceitos principais:

- **Machine Learning**;
- **Séries Temporais**;
- **Arquitetura de Software**;
- **Fundamentos de solução em Cloud**;

Além destes tópicos, vamos abordar outras técnicas e ferramentas que são essenciais para o desenvolvimento de aplicações modernas.
No material, você encontrará diversos exemplos práticos e exercícios para fixação do conteúdo. 

Vamos lá! 🐼

## Avisos Importantes

Aqui vão alguns avisos importantes para o módulo, em especial quanto a organização e execução das atividades que vocês vão desenvolver ao longo do módulo. Para iniciar, vamos utilizar uma fala do professor [Nicola](https://github.com/rmnicola), que [eu](https://github.com/Murilo-ZC), faço das palavras deles as minhas: 

:::danger[Acesse a Adalove!]

Esse material NÃO substitui de forma alguma o uso da Adalove. Você DEVE entrar na Adalove com frequência e REGISTRAR O SEU PROGRESSO. Entendeu? Ainda não? Pera aí que vou desenhar:

<img src="img/aviso-adalove.png" alt="ACESSE A ADALOVE" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto' }} />

:::

## Organização do Material do Módulo

Nosso material está organizado da seguinte maneira:

- `Artefatos`: Nesta seção, você encontrará os artefatos que serão desenvolvidos ao longo do módulo. Cada artefato possui um conjunto de atividades que devem ser realizadas para a sua conclusão. Em caso de dúvidas, procurar o professor [Orientador](mailto:murilo.zanini@prof.inteli.edu.br).

- `Encontros`: Nesta seção, você encontrará o cronograma de encontros do módulo. Em cada encontro, serão abordados tópicos específicos do módulo, com o objetivo de fixar o conteúdo e desenvolver o projeto.

- `Atividades Ponderadas`: Nesta seção, você encontrará as atividades ponderadas que serão realizadas ao longo do módulo. Cada atividade possui um peso específico na nota final do módulo. A descrição, material de consulta e prazo de entrega de cada atividade estão disponíveis nesta seção.


:::tip[Sistema Operacional Recomendado]

Pessoal ao longo do módulo, o sistema operacional utilizado `oficialmente` será o Ubuntu Linux 22.04 LTS. RECOMENDO FORTEMENTE que você iniciem com um `clean install` do Ubuntu. Caso você não tenha um microsd com o Ubuntu, ou esteja utilizando outro sistema operacional, recomendo pegar um cartão no laboratório e realizar a instalação padrão.

<img class="image-intro" src="https://64.media.tumblr.com/aefc0fa20da07843ef8ce5db9271513b/e6d7f259c430d198-6b/s540x810/c35f214dc733fda5f9fe182f143296fcf189a6c2.gif" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto' }}/>

:::

## Referências Bibliográficas

Aqui estão listas nossas referências bibliográficas para o módulo. É importante que vocês consultem essas referências para aprofundar o conhecimento sobre os tópicos abordados.

### Bibliográfia Básica

- [`BARRETO, J. dos S. et al. Interface humano-computador. Porto Alegre: SAGAH, 2018.`](https://integrada.minhabiblioteca.com.br/#/books/9788595027374)

 Este livro apresenta os principais conceitos para a construção de interface com computadores e sistemas computadorizados.

- [`BRAGA FILHO, W. Fenômenos de transporte para engenharia. 2. ed. Rio de Janeiro: LTC, 2012.`](https://integrada.minhabiblioteca.com.br/#/books/978-85-216-2079-2)

  Livro essencial para os estudantes, pois apresenta de forma clara e didática os conceitos e técnicas fundamentais da transferência de massa, calor e momento. O volume abrange desde os princípios básicos até aplicações práticas, fornecendo uma visão abrangente e aplicada dos fenômenos de transporte.

- [`EDMONDSON, A. C. A Organização sem medo. Rio de Janeiro: Alta Books, 2020.`](https://integrada.minhabiblioteca.com.br/#/books/9786555204087)

  Este livro é a principal referência na descrição do conceito de segurança psicológica. Nele, a autora descreve a importância da construção de confiança entre os membros de um time comprometido com a performance e com as pessoas.

- [`FACELI, K.; LORENA, A. C.; GAMA, J.; et al. Inteligência artificial: uma abordagem de aprendizado de máquina. 2. ed. Rio de Janeiro: LTC, 2023.`] (https://integrada.minhabiblioteca.com.br/#/books/9788521637509)

  Este livro traz uma abordagem clássica sobre o aprendizado de máquina, apresentando os principais conceitos e algoritmos utilizados no aprendizado de máquinas.

- [`GARRISON, R. H.; NOREEN, E. W.; BREWER, P. C. Contabilidade gerencial. 14. ed. Porto Alegre: AMGH, 2013.`](https://integrada.minhabiblioteca.com.br/#/books/9788580551624)

  A contabilidade gerencial é instrumento essencial para a análise das necessidades internas de qualquer organização e por meio dela, obtemos as informações necessárias para os planos de ação, as atividades de controle e as tomadas de decisão. Esse livro mostra como coletar e interpretar as informações contábeis e apresenta novas ferramentas didáticas para auxiliar o estudo.

- [`GIL, A. C. Como fazer pesquisa qualitativa. 1. ed. Barueri: Atlas, 2021.`](https://integrada.minhabiblioteca.com.br/#/books/9786559770496)

  Este livro apresenta em detalhes como desenvolver uma pesquisa qualitativa, suas etapas e boas práticas, apresentados o método qualitativo e seus respectivos métodos de pesquisa e aplicações.

- [`JUNIOR, O. da S. Análise e modelagem preditiva. São Paulo: Platos Soluções Educacionais S.A., 2021.`](https://integrada.minhabiblioteca.com.br/#/books/9786589881063)

  O livro apresenta os principais conceitos e técnicas para a realização de análise e modelagem preditiva em diferentes áreas do conhecimento. Com uma abordagem prática e didática, o livro apresenta desde os conceitos básicos até técnicas mais avançadas, abrangendo temas como regressão linear, séries temporais, árvores de decisão, redes neurais, entre outros.

- [`LIVI, C. P. Fundamentos de fenômenos de transporte: um texto para cursos básicos. 2. ed. Rio de Janeiro: LTC, 2012.`](https://integrada.minhabiblioteca.com.br/#/books/978-85-216-2145-4)

  Este livro apresenta de forma clara e didática os conceitos e técnicas fundamentais da transferência de massa, calor e momento. O volume abrange desde os princípios básicos até aplicações práticas, fornecendo uma visão abrangente e aplicada dos fenômenos de transporte.

- [`MÁLAGA, F. K. Análise de demonstrativos financeiros e da performance empresarial: para empresas não financeiras. São Paulo: Saint Paul Publishing, 2017.`](https://integrada.minhabiblioteca.com.br/#/books/9788580041330)

  O entendimento contábil e da performance empresarial com base na análise das demonstrações financeiras é fator crucial para se obter êxito na gestão de empresas e no mercado de capitais. A evolução desse mercado tornou a emissão de ações ou de títulos de crédito uma alternativa viável na captação de recursos pelas empresas no mercado de capitais.

- [`MILANI, A. M. P. et al. Visualização de dados. 1. ed. Porto Alegre: SAGAH, 2020.`](https://integrada.minhabiblioteca.com.br/#/books/9786556900278)

  No contexto atual em que vivemos, o uso de dados nos mais diversos âmbitos é uma realidade cada vez mais frequente. No entanto, os dados de nada servem se não puderem ser visualizados e acessados de forma compreensível. Pensando nisso, este livro mostra diferentes formas de processamento, análise e apresentação de dados para que o estudante esteja apto a utilizá-los da forma mais proveitosa possível.

- [`MISSEL, S. Feedback corporativo: como saber se está indo bem. 2. ed. São Paulo: Benvirá, 2017.`](https://integrada.minhabiblioteca.com.br/books/9788557170322)

  Este livro analisa e descreve como o feedback pode ser utilizado em organizações e em processos de avaliação, dando subsídios para os estudantes conheçam essa ferramenta de desenvolvimento pessoal e organizacional. 

- [`NETTO, A.; MACIEL, F. Python para Data Science e Machine Learning: descomplicado. Rio de Janeiro: Alta Books, 2021.`](https://integrada.minhabiblioteca.com.br/#/books/9786555203172)

  Este livro é uma excelente escolha para aprender Python aplicado a análise de dados e machine learning. Com uma abordagem prática, o livro cobre desde conceitos básicos até tópicos avançados como redes neurais e deep learning.

- [`PRESSMAN, R. S.; MAXIM, B. R. Engenharia de software: uma abordagem profissional. 9. ed. Porto Alegre: AMGH, 2021.`](https://integrada.minhabiblioteca.com.br/#/books/9786558040118)

  O livro é uma obra indispensável para quem deseja entender os conceitos e práticas fundamentais da área, cobre desde a definição de requisitos até a implementação e teste de sistemas, incluindo também tópicos sobre metodologias ágeis e segurança de software.

- [`RAGSDALE, C. T. Modelagem de planilha e análise de decisão: uma introdução prática a business analytics. São Paulo: Cengage, 2019.`](https://integrada.minhabiblioteca.com.br/#/books/9788522128303)

  Este livro traz uma abordagem sobre como tratar de análises de dados em uma perspectiva de negócios. Ele apresenta o processo que torna possível a tomada de decisão utilizando o suporte de dados.

- [`SILVA, R. F. da. Deep Learning. São Paulo: Platos Soluções Educacionais S.A., 2021.`](https://integrada.minhabiblioteca.com.br/#/books/9786589881520)

  O livro é uma referência para quem busca compreender e aplicar técnicas de aprendizado profundo. Com uma linguagem acessível e exemplos práticos, o livro aborda redes neurais convolucionais, recorrentes e generativas, além de temas como otimização e transferência de aprendizado.

- [`STEPHAN, A. P. Dez cases do design brasileiro. São Paulo: Blucher, 2008.`](https://integrada.minhabiblioteca.com.br/reader/books/9788521215431)

  Este livro traz a apresentação de um estudo de caso que buscou uma forma de modificar o processo de checkout em filas de lojas e mercados.

### Bibliográfia Complementar 

- [`AMÉRICO, B. Método de pesquisa qualitativa: analisando fora da caixa a prática de pesquisar organizações. Rio de Janeiro: Alta Books, 2021.`](https://integrada.minhabiblioteca.com.br/#/books/9786555203875)

  Este livro combina e apresenta Métodos de Pesquisa Qualitativa de forma inovadora e rigorosa. Por Métodos de Pesquisa Qualitativa entende-se ferramentas que permitem a coleta e análise de dados, online e presencialmente, sobre como: acessar o campo de estudos/trabalho; mapear a literatura especializada sobre o tema estudado; definir quais práticas organizacionais devem ser exploradas; e escrever a versão final da investigação qualitativa.

- [`ANDRADE, E. L. D. Introdução à pesquisa operacional: método e modelos para análise de decisões. 5. ed. Rio de Janeiro: LTC, 2015.`](https://integrada.minhabiblioteca.com.br/reader/books/978-85-216-2967-2)

  O livro é essencial para os estudantes e profissionais de engenharia, pois apresenta de forma clara e didática os conceitos e técnicas da pesquisa operacional. O volume abrange modelos matemáticos e métodos para a tomada de decisões em situações complexas, contribuindo para a formação de uma visão estratégica e analítica dos problemas empresariais.

- [`CAMARGO, R. A. de; RIBAS, T. Gestão ágil de projetos. São Paulo: Saraiva, 2019.`](https://integrada.minhabiblioteca.com.br/#/books/9788553131891)

  O livro aborda a gestão de projetos e desenvolvimento de produtos através de abordagens ágeis e modernas de gestão.

- [`FASCIONI, Ligia; COSTA, Alberto. Atitude Pró-Liderança. Belo Horizonte: DMT Consulting, 2016.`](https://d335luupugsy2.cloudfront.net/cms/files/39758/1533238967Atitude_Pro_Liderana_-_Ligia_Fascioni.pdf)

  Este livro é uma introdução sobre práticas e frameworks de liderança, dando subsídios para a construção de competências dos estudantes de tecnologia que estão no início de carreira. 

- [`GOMES, J. M. Elaboração e análise de viabilidade econômica de projetos: tópicos práticos de finanças para gestores não financeiros. São Paulo: Atlas, 2013.`](https://integrada.minhabiblioteca.com.br/#/books/9788522479634)

  Neste livro são apresentados a metodologia e o passo a passo na Elaboração e Análise de Viabilidade Econômica de Projetos, sendo discutidos os conceitos, com exemplo, para o perfeito entendimento do processo de elaboração e análise. A metodologia é extremamente poderosa e garante ao estudante visão integrada e consistente do modelo de análise proposto, tornando-o apto a desenvolver seus próprios projetos.

- [`GRUS, J. Data science do zero: noções fundamentais com Python. 2. ed. Rio de Janeiro: Alta Books, 2016.`](https://integrada.minhabiblioteca.com.br/#/books/9788550816463)

  Além de ser uma leitura essencial para iniciantes em ciência de dados, o livro também pode ser utilizado como um guia de referência prático para profissionais experientes que buscam aprimorar suas habilidades em Python e explorar novas técnicas de análise de dados.

- [`IUDÍCIBUS, S. de. Contabilidade gerencial: da teoria à prática. 7. ed. São Paulo: Atlas, 2020.`](https://integrada.minhabiblioteca.com.br/#/books/9788597024197)

  O livro traz noções introdutórias da Contabilidade Gerencial, além de conceitos sobre lucro empresarial, variação de preços e análise de balanço como instrumento da Avaliação de Desempenho.Nesta nova edição, foi adicionado um capítulo inédito, integralmente dedicado à estrutura das demonstrações contábeis e financeiras.

- [`MARTIN, R. C. Desenvolvimento ágil limpo: de volta às origens. Rio de Janeiro: Alta Books, 2020.`](https://integrada.minhabiblioteca.com.br/#/books/9788550816890)

  Esta obra traz uma revisão do manifesto ágil e a forma como ele é utilizado na entrega de valor com o projeto. Ele traz uma visão do framework Scrum e outras ferramentas ágeis do ponto de vista dos desenvolvedores, refletindo sua experiência ao longo dos anos e como este manifesto foi revisitado.

- [`MORETTIN, P. A. Estatística básica. 9. ed. São Paulo: Saraiva, 2017.`](https://integrada.minhabiblioteca.com.br/#/books/9788547220228)

  Este livro é uma referência para estudantes, pois apresenta um entendimento claro e objetivo dos conceitos estatísticos. O volume abrange desde os conceitos fundamentais até técnicas avançadas de análise de dados, tornando-se uma ferramenta indispensável para quem trabalha com pesquisa, planejamento e tomada de decisões baseadas em dados.

- [`NETO, J. A. A era do ecobusiness: criando negócios sustentáveis. Barueri: Manole, 2015.`](https://integrada.minhabiblioteca.com.br/#/books/9788520448953)

  O desenvolvimento sustentável é uma abordagem necessária para o mundo e para as organizações. Neste livro, o autor descreve as bases dessa visão para o mundo dos negócios, dando subsídios para que lideranças tomem decisões conscientes no aspecto ambiental. 

- [`VETORAZZO, A. S. Engenharia de software. Porto Alegre: SAGAH, 2018.`](https://integrada.minhabiblioteca.com.br/#/books/9788595026780)

  Este livro é uma obra de referência na área, abordando desde conceitos básicos até as práticas mais avançadas da engenharia de software. Com uma linguagem clara e exemplos práticos, o livro traz ainda discussões sobre metodologias ágeis, gestão de projetos e qualidade de software.

- [`ZABADAL, J. R. S.; RIBEIRO, V. G. Fenômenos de transporte: fundamentos e métodos. São Paulo: Cengage Learning Brasil, 2016.`](https://integrada.minhabiblioteca.com.br/#/books/9788522125135)

  O livro aborda de maneira clara e objetiva os conceitos teóricos dos fenômenos de transporte, como transferência de massa, calor e quantidade de movimento. Além disso, o livro apresenta exemplos e exercícios resolvidos que ajudam o leitor a entender e aplicar os conceitos apresentados.

### Periódicos

- [`Scalable Computing: Practice & Experience`](https://www.scpe.org/index.php/scpe)
- [`Journal of Manufacturing Systems`](https://www.sciencedirect.com/journal/journal-of-manufacturing-systems)
- [`International Journal of Computer Integrated Manufacturing`](https://www.tandfonline.com/journals/tcim20)