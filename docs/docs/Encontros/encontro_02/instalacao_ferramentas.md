---
sidebar_position: 1
title: Instalação das Ferramentas
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Instalação das Ferramentas para Desenvolvimento

Realizar a instalação dos pacotes que vamos utilizar ao longo do nosso encontro e no restante do módulo.


### 1. Primeiro, atualizar os pacotes:

```bash
sudo apt update
sudo apt upgrade
```

### 2. Adicionar o painel de controle:

```bash
sudo apt install gnome-control-center
```

### 3. Instalar o curl:

```bash
sudo apt install curl
```

### 4. Instalar o Git:

```bash
sudo apt-get install git-all
```

### 5. Instalar o VS Code e o Chrome (rodando pelo instalador padrão).

### 6. Vamos realizar a instalação do Docker utilizando um Script de instalação disponĩvel em [get Docker](https://get.docker.com/):

```bash
curl -fsSL https://get.docker.com -o install-docker.sh
sh install-docker.sh --dry-run
```

Agora, execute o próximo script como root:

```bash
sudo sh install-docker.sh
```

Agora vamos ajustar a instalação para não precisarmos utilizar os comandos como root:

```bash
sudo apt-get install -y uidmap
dockerd-rootless-setuptool.sh install
```

Acredito que com essas ferramentas básicas já temos os programas básicos para seguir. 

---

<img src="https://i.makeagif.com/media/8-11-2023/WQhn3E.gif" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom: '24px' }}/>


