---
sidebar_position: 4
title: Ferramentas de Teste
---

import useBaseUrl from '@docusaurus/useBaseUrl';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Ferramentas de Teste

Pessoal agora vamos falar sobre as ferramentas de teste que serão utilizadas para avaliar as aplicações que foram construídas. Cada ferramenta apresentada aqui tem suas particularidades e é importante entender como elas funcionam.

Nosso objetivo será compreender como elas são utilizadas. Vamos realizar todos os testes na aplicação 1. A comparação com as demais aplicações fica como tarefa de implementação de vocês.

### JMeter

:::tip[Vem Depois]

<img src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/1d9ef916-0d2a-4096-9dba-fab980341540/ddlj9td-cff79788-be8a-4660-9507-e96ef0859e41.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzFkOWVmOTE2LTBkMmEtNDA5Ni05ZGJhLWZhYjk4MDM0MTU0MFwvZGRsajl0ZC1jZmY3OTc4OC1iZThhLTQ2NjAtOTUwNy1lOTZlZjA4NTllNDEuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.9A4AevZ1agVAJ-vjdMcx0r0ojyeYgroxekKvbylZiA0" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom: '24px' }}/>


:::

---

### Locust

O Locust é uma ferramenta de teste de carga de código aberto que permite que você escreva cenários de teste em Python. Ele é altamente escalável e pode ser usado para testar aplicações web, APIs e outros sistemas. Sua documentação oficial pode ser acessada [aqui](https://locust.io).

Vamos testar nossa aplicação 1 com o Locust. Para isso, vamos seguir os seguintes passos:

```bash
# criar um venv
python3 -m venv venv
# ativar o venv
source venv/bin/activate
# instalar o locust
pip install locust
```

Agora vamos criar um arquivo chamado `locustfile.py` com o seguinte conteúdo:

```python
from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def criar_usuario(self):
        self.client.post("/usuarios", json={"nome": "Fulano",  "email": "mail@mail.com" })

    @task
    def pegar_usuarios(self):
        self.client.get(f"/usuarios")
```

Agora no terminal execute a aplicação com o comando:

```bash
locust -f locustfile.py
```

Acesse o endereço `http://localhost:8089` e configure o número de usuários e a taxa de requisições. Depois clique em `Start Swarming` para iniciar o teste.


---

### K6

:::tip[Vem Depois]

<img src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/1d9ef916-0d2a-4096-9dba-fab980341540/ddlj9td-cff79788-be8a-4660-9507-e96ef0859e41.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzFkOWVmOTE2LTBkMmEtNDA5Ni05ZGJhLWZhYjk4MDM0MTU0MFwvZGRsajl0ZC1jZmY3OTc4OC1iZThhLTQ2NjAtOTUwNy1lOTZlZjA4NTllNDEuZ2lmIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.9A4AevZ1agVAJ-vjdMcx0r0ojyeYgroxekKvbylZiA0" style={{ display: 'block', marginLeft: 'auto', maxHeight: '40vh', marginRight: 'auto', marginBottom: '24px' }}/>


:::

---