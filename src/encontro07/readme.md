# Intruções Gerais para o Encontro

Ao longo do encontro, o JupyterNotebook será utilizado para realizar as análises dos dados. Para isso, vamos realizar sua utilização em conjunto com o Docker.

Primeiro precisamos compreender o conceito de volume no Docker.

<p align="center">
  <img src="https://docs.docker.com/storage/images/types-of-mounts-volume.png" width="100%" height="auto" title="Volumes no Docker">
</p>
<p align="center">Volumes no Docker</p>

Vamos trabalhar com o ***bind mount*** para permitir que nosso container com o Jupyternotebook possa acessar os arquivos que estão no nosso computador.

A nossa imagem vai rodar como descrito na [referência](https://github.com/jupyter/docker-stacks#example-2), onde o container, quando não estiver mais em execução, será removido. Ele vai mapear o diretório atual de onde ele for executado.

- Para Linux/MacOS:
```bash
docker run -it --rm -p 10000:8888 -v "${PWD}":/home/jovyan/work jupyter/datascience-notebook:2023-08-19
```

- Para Windows:
```bash
docker run -it --rm -p 10000:8888 -v "%cd%":/home/jovyan/work jupyter/datascience-notebook:2023-08-19
```

Para o encontro, vamos utilizar a imagem do JupyterNotebook com Python, que já vem com as principais bibliotecas instaladas para trabalhar com análise de dados. Ela será executada dentro do diretório ***encontro07***, assim, o diretório ***datasets*** estará disponível para ser utilizado.

```bash
# Navegar até o diretório encontro07
cd encontro07
docker run -it --rm -p 10000:8888 -v "%cd%":/home/jovyan/work jupyter/datascience-notebook:2023-08-19
```