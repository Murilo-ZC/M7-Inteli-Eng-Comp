---
sidebar_position: 3
title: Análise Exploratória e Análise Descritiva
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


## Análise Exploratória

A análise exploratória de dados é um processo de investigação preliminar dos dados, realizado antes da modelagem formal ou testes de hipóteses. Seu objetivo principal é obter insights sobre os dados, entender suas características, identificar padrões, anomalias e relações entre variáveis. Esta etapa é fundamental para informar as decisões subsequentes no processo de machine learning.

No contexto de machine learning, a análise exploratória serve para vários propósitos importantes:

1. ***Compreensão dos dados:*** Ajuda a entender a natureza e estrutura dos dados, incluindo tipos de variáveis, distribuições e relações entre elas.
2. ***Identificação de problemas nos dados:*** Permite detectar valores ausentes, outliers, erros de entrada e outras anomalias que podem afetar o desempenho do modelo.
3. ***Seleção de features:*** Auxilia na identificação de variáveis relevantes para o problema em questão, o que pode guiar a seleção de features para o modelo.
4. ***Formulação de hipóteses:*** Gera *insights* que podem levar à formulação de hipóteses sobre relações nos dados, que podem ser testadas posteriormente.
5. ***Auxilia na escolha de modelos:*** Auxilia na escolha de modelos de machine learning apropriados com base nas características dos dados.
6. ***Preparação para pré-processamento:*** Identifica necessidades de transformação de dados, como normalização, codificação de variáveis categóricas, etc.
7. ***Detecção de padrões temporais:*** No caso de séries temporais, ajuda a identificar tendências, sazonalidades e outros padrões temporais.

:::tip[Observação]

<img src="https://i.pinimg.com/originals/50/c5/f1/50c5f1847013012ee0f25f67fdddb8d9.gif" style={{ display: 'block', marginLeft: 'auto', maxHeight: '50vh', marginRight: 'auto', marginBottom: '24px' }}/>

Pessoal utilizem a analise exploratória para compreender os dados que estão disponíveis. Ela está fortemente ligada a ***FORMA COMO OS DADOS ESTÃO DISPONÍVEIS***. É importante lembrar que essa etapa é muito importante para conhecer a distribuição dos dados, identificar outliers, valores nulos, entre outros. Utilizar gráficos para visualizar os dados é uma prática comum e recomendada.

:::

---

## Análise Descritiva

A Análise Descritiva concentra-se em resumir e descrever as principais características de um conjunto de dados de forma quantitativa. Ela busca responder à pergunta "O que aconteceu?" ou "O que os dados mostram?". Ela fornece um resumo conciso das características essenciais dos dados, tornando-os mais fáceis de entender e interpretar. A análise descritiva é geralmente realizada usando uma combinação de técnicas estatísticas e visualizações. 

Importância da análise descritiva em machine learning:

1. ***Compreensão inicial:*** Fornece uma visão geral dos dados antes de aplicar modelos complexos.
2. ***Detecção de anomalias:*** Ajuda a identificar outliers e valores atípicos.
3. ***Seleção de features:*** Auxilia na identificação de variáveis potencialmente importantes para o modelo.
4. ***Pré-processamento:*** Informa decisões sobre normalização, padronização ou transformação de dados.
5. ***Escolha de modelos:*** Características dos dados podem sugerir certos tipos de modelos.
6. ***Interpretação de resultados:*** Fornece contexto para interpretar os resultados dos modelos de machine learning.
7. ***Comunicação:*** Facilita a comunicação de insights sobre os dados para stakeholders não técnicos.

Diversas técncias estastísticas podem ser utilizadas para realizar a análise descritiva, onde podemos destacar:

1. Medidas de tendência central:
    - **Média:** o valor médio dos dados
    - **Mediana:** o valor central quando os dados são ordenados
    - **Moda:** o valor mais frequente
2. Medidas de dispersão:
    - **Variância:** mede a variabilidade dos dados em relação à média
    - **Desvio padrão:** raiz quadrada da variância, na mesma unidade dos dados originais
    - **Amplitude:** diferença entre o maior e o menor valor
    - **Quartis e intervalo interquartil:** dividem os dados em quatro partes iguais
3. Medidas de forma:
    - **Assimetria:** indica se a distribuição é simétrica ou inclinada para um lado
    - **Curtose:** mede o achatamento da distribuição em relação à distribuição normal
4. Contagens e frequências:
    - Para dados categóricos, contagem de ocorrências de cada categoria
    - Frequências relativas e absolutas
5. Correlações:
    - Coeficientes de correlação entre variáveis (ex: correlação de Pearson)

:::tip[Observação]

<img src="https://i.pinimg.com/originals/50/c5/f1/50c5f1847013012ee0f25f67fdddb8d9.gif" style={{ display: 'block', marginLeft: 'auto', maxHeight: '50vh', marginRight: 'auto', marginBottom: '24px' }}/>

A análise descritiva oferece uma visão geral e resumida do conjunto de dados. Ela busca solucionar o desafio inicial de compreender as características essenciais das informações disponíveis, revelando padrões, tendências e anomalias que podem não ser imediatamente evidentes. Esta análise serve como base para a tomada de decisões informadas, auxilia na preparação dos dados para análises mais avançadas e estabelece um ponto de referência para comparar resultados de modelos mais complexos.

Em essência, a análise descritiva estabelece uma base sólida para todo o projeto de machine learning, otimizando recursos e direcionando esforços para os aspectos mais promissores ou desafiadores dos dados.

:::

---

## Exemplo Prático

Pessoal vamos avaliar como podemos realizar um conjunto de analise exploratória e descritiva. Para isso, vamos utilizar um dataset disponível no Kaggle, chamado [Video Game Sales with Ratings](https://www.kaggle.com/rush4ratio/video-game-sales-with-ratings). Este dataset contém informações sobre vendas de jogos de vídeo game e suas avaliações.


Primeiro vamos fazer o download do nosso dataset e então explorar nossos dados. Os datasets podem ser formados de diversas maneiras, desde arquivos CSV enviados por e-mail, até conexões com bancos de dados. O importante é que você tenha acesso a esses dados e que eles sejam suficientes para resolver o problema que você deseja resolver. Para nossa exploração, vamos utilizar o Python e a biblioteca Pandas. Vou utilizar também o Jupyter Notebook para fazer essa exploração.

Primeiro vou criar um ambiente virtual para realizar a instalação das bibliotecas necessárias. Vou utilizar o `venv` para criar o ambiente virtual e o `pip` para instalar as bibliotecas. Aqui todos os comandos serão informados utilizando o sistema operacional Windows.

```bash showLineNumbers
python -m venv venv
.\venv\Scripts\Activate
python -m pip install pandas matplotlib seaborn
```

Aqui estamos criando nosso ambiente virtual (linha 1) e realizando sua ativação (linha 2). Na sequência estamos instalando as bibliotecas Pandas, Matplotlib e Seaborn (linha 3).

Vou realizar o download do dataset utilizando uma conta cadastrada no Kaggle. Uma alternativa é realizar o download diretamente do repositório da disciplina. Agora vamos criar um arquivo para realizar a exploração dos dados.

:::tip[Observação]

Vocês não precisam criar um notebook para realizar a exploração, ela pode ser realizada utilizando Scripts Python. A utilização de notebooks é uma prática comum entre cientistas de dados, mas não é uma regra. A ferramenta para utilizar os notebooks também é opcional, vocês podem utilizar o Jupyter Notebook, o Google Colab, o Jupyter Lab, o VS Code, entre outros. Vou utilizar o VS Code e Jupyter Lab. Para utilizar o Jupyter Lab, basta instalar o Jupyter Lab no seu ambiente virtual e então executar o comando `jupyter lab`.

```bash
python -m pip install jupyterlab
juptyer lab
```

:::

Deste ponto em diante, vamos utilizar o Pandas para explorar os dados. Vamos carregar o dataset e então verificar as primeiras linhas do nosso dataset. Minha sugestão é deixar aberto essa folha de comandos do Pandas para realizar a consulta quando necessário. Não se preocupe em decorar comandos, mas sim em entender o que e porque estamos executando cada etapa do processo. Link para folha de comandos [aqui](https://cheatsheets.zip/pandas).

```python showLineNumbers
# Importa a biblioteca do Pandas
import pandas as pd
# Abre o dataset em um DataFrame do Pandas
dados = pd.read_csv('Video_Games_Sales_as_at_22_Dec_2016.csv')
# Exibe as primeiras linhas do dataset
dados.head()
```

Aqui temos a primeira etapa da exploração dos dados. Carregamos eles dentro do Pandas para exploração. O Pandas carrrega os dados como `Series` ou `DataFrames`, que são estruturas de dados que facilitam a manipulação dos dados. O método `head()` exibe as primeiras linhas do dataset, permitindo que possamos visualizar as colunas e os dados. Um `DataFrame` é uma estrutura de dados bidimensional, com linhas e colunas, que permite a manipulação de dados de forma mais eficiente. Ele é implementado como uma abstração do NumPy, que é uma biblioteca de computação científica para Python.

Cada coluna de um `DataFrame` é chamada de `feature`. Ela representa uma característica dos dados que estamos analisando. Cada linha de um `DataFrame` é chamada de `sample`. Ela representa uma observação dos dados que estamos analisando. O `DataFrame` é uma estrutura de dados muito utilizada em análise de dados e machine learning, pois permite a manipulação de dados de forma eficiente e organizada.

Vamos explorar um pouco mais os nossos dados. Vamos verificar o tipo de cada coluna do nosso dataset:

```python showLineNumbers
# Explorando o nosso conjunto de dados
# Verificando os tipos
dados.dtypes
```

Ao executar essa célula, podemos observar que existem dados que são numéricos e outros que são categóricos. Os dados numéricos são aqueles que representam valores quantitativos, como idade, peso, altura, entre outros. Os dados categóricos são aqueles que representam valores qualitativos, como sexo, cor, estado civil, entre outros. O Pandas vai inferir o tipo de cada coluna do dataset, mas é importante que você verifique se o tipo está correto. Caso necessário, é possível alterar o tipo de uma coluna utilizando o método `astype()`.

Agora vamos buscar informações dos dados no dataframe.

```python showLineNumbers
# Trazendo características dos dados
dados.info()
```

Podemos ver que existem dados que são nulos. Dados nulos são aqueles que não possuem valor. Eles podem ser representados de diversas formas, como `NaN`, `None`, `NA`, entre outros. O Pandas trata os dados nulos de forma especial, permitindo que você os identifique e os trate de forma adequada. Existem diversas formas de tratar dados nulos, como preencher com um valor padrão, remover as linhas que possuem valores nulos, entre outros.

Para contar o número de dados ausentes:

```python showLineNumbers
# Contando os dados nulos
dados.isnull().sum()
```

Podemos observar aqui que diversos valores estão ausentes. Como dito anteriormente, podemos escolher diferentes estratégias para lidar com esses dados que estão ausentes, variando de acordo com o problema que estamos resolvendo. Aqui cabe destacar um detalhe importante: o caminho que escolhermos para tratar os nossos dados pode não ser o melhor caminho. A criação e validação dos modelos vai nos ajudar a entender se a estratégia escolhida foi a melhor ou se devemos alterar ela.

Para conhecer a distribuição dos dados numéricos:

```python showLineNumbers
# Conhecendo a distribuição dos dados numéricos
dados.describe()
```

Para contarmos a quantidade de elementos em `features` que não são numéricas

```python showLineNumbers
# Exibe a quantidade de valores em cada coluna categórica
dados.select_dtypes(include='object').nunique()
```

Para visualizar os dados, podemos utilizar algumas ferramentas para plotar os dados. Nesse mommento, vamos utilizar 3 conjuntos de ferramentas: o próprio Pandas, o Matplotlib e o Seaborn. O Pandas possui métodos para plotar gráficos diretamente a partir de um DataFrame. O Matplotlib é uma biblioteca de visualização de dados em Python, que permite a criação de gráficos personalizados. O Seaborn é uma biblioteca de visualização de dados baseada no Matplotlib, que facilita a criação de gráficos estatísticos complexos.

Para plotar um gráfico de barras com a quantidade de jogos por plataforma:

```python showLineNumbers
# Importando as bibliotecas
import matplotlib.pyplot as plt
import seaborn as sns

# Plotando um gráfico de barras com a quantidade de jogos por plataforma
plt.figure(figsize=(16, 8))
# O conjunto de dados avaliados é o DataFrame. A variável de contagem é a Platform. 
# Os dados são ordenados de forma decrescente.
sns.countplot(data=dados, y='Platform', order=dados['Platform'].value_counts().index)

plt.title('Quantidade de Jogos por Plataforma')
plt.xlabel('Quantidade de Jogos')
plt.ylabel('Plataforma')
plt.show()
```

Para plotar um gráfico de barras com a quantidade de jogos por gênero:

```python showLineNumbers
# Exibe a quantidade de jogos por genero
plt.figure(figsize=(16, 8))
sns.countplot(data=dados, y='Genre', order=dados['Genre'].value_counts().index)

plt.title('Quantidade de Jogos por Genero')
plt.xlabel('Quantidade de Jogos')
plt.ylabel('Genero')
plt.show()
```

O objetivo desses gráficos é permitir que você visualize a distribuição dos dados e busque identificar padrões, tendências e anomalias. A visualização de dados é uma etapa análise exploratória que permite entender melhor as características dos dados e tome decisões informadas sobre o pré-processamento e modelagem dos dados.

Busquem na documentação das ferramentas para plotar gráficos mais visualizações que podem ser construídas. A exploração dessas ferramentas pode auxiliar na identificação de padrões e relações nos dados, que podem ser úteis para a construção de modelos de machine learning.

## Análise Descritiva

A análise descritiva é uma etapa importante da análise exploratória de dados, que visa resumir e descrever as principais características dos dados de forma quantitativa. Ela fornece um resumo conciso dos dados, tornando-os mais fáceis de entender e interpretar. A análise descritiva é geralmente realizada usando uma combinação de técnicas estatísticas e visualizações.

Uma ferramenta que pode nos auxiliar a visualização dos dados é o `pandas_profiling`. Essa biblioteca gera um relatório com diversas informações sobre os dados, como estatísticas descritivas, distribuições, correlações, entre outros. O `pandas_profiling` passou por uma atualização no projeto e agora se chama `ydata_profiling`. Vamos instalar a biblioteca e gerar o relatório.

```bash showLineNumbers
pip install -U ydata-profiling
```

Importante: para visualizar o relatório no Jupyter Notebook, é necessário instalar o `ipywidgets`. Para instalar, utilize o seguinte comando:

```bash showLineNumbers
pip install ipywidgets
# Recomendação do Co-Pilot, não precisei para executar o código
# jupyter nbextension enable --py widgetsnbextension
# Para permitir que as saídas dos widgets sejam exibidas no notebook
# Ref.: https://stackoverflow.com/questions/43288550/iopub-data-rate-exceeded-in-jupyter-notebook-when-viewing-image
jupyter lab --NotebookApp.iopub_data_rate_limit=1.0e10
```

Para visualizar o relatório, vamos utilizar o seguinte código:

```python showLineNumbers
from ydata_profiling import ProfileReport
import pandas as pd

# Abre o dataset em um DataFrame do Pandas
dados = pd.read_csv('Video_Games_Sales_as_at_22_Dec_2016.csv')

# Gerando o relatório
profile = ProfileReport(dados, title='Relatório de Análise Descritiva', explorative=True)

# Salvando o relatório em um arquivo HTML
profile.to_file("relatorio_analise_descritiva.html")
```

Para exibir o relatório no Jupyter Notebook, basta utilizar o seguinte código:

```python showLineNumbers
# Forma 1
# profile.to_widgets()
# Forma 2
profile.to_notebook_iframe()
```



## Material de Estudo Adicional

- https://github.com/ydataai/ydata-profiling
- https://www.influxdata.com/blog/pandas-profiling-tutorial/
- https://docs.profiling.ydata.ai/latest/
- https://www.kdnuggets.com/2021/02/pandas-profiling-one-line-magical-code-eda.html
- https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/index.html
- https://medium.com/@muralimanohar6/leveraging-the-way-you-interpret-the-descriptive-statistics-in-python-bd2111fb5211
- https://discovery.cs.illinois.edu/guides/DataFrame-Fundamentals/descriptive-statistics-of-columns-in-dataframes/#List-of-Functions
- https://discovery.cs.illinois.edu/guides/
- https://discovery.cs.illinois.edu/guides/Statistics-Formulas/correlated-independent-variables/
- https://discovery.cs.illinois.edu/guides/Descriptive-Statistics/eda-start/
- https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf
- https://www.kaggle.com/discussions/getting-started/481538
- https://realpython.com/python-statistics/