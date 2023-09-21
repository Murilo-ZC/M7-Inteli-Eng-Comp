# Encontro 11 - Integração de Dados (API) com Frontend

## Objetivos

Este encontro possui alguns objetivos específicos:
- Compreender como construir uma API para servir os dados
- Compreeender como consumir uma API com o frontend
- Construir uma aplicação utilizando o Streamlit
- Realizar o deploy da aplicação da API e da interface
- Implementar um controle de usuário simples com o Streamlit e o RDS


## Desenvolvimento da Aplicação de Login com o Streamlit

Com o ambiente virtual criado, instalar as depencias necessárias:

```bash
python -m pip install requirements.txt
```

Agora vamos desenvolver o primeiro código que será o da nossa página de login. Primeiro vamos colocar algumas funcionalidades básicas nela, como criar o layout e verificar um usuário pré-definido:
    
```python
import streamlit as st

# Método para verificar usuário e senha
def check_login(user, password):
    if user == "admin" and password == "admin":
        return True
    else:
        return False

# Cria a página de login
def login():
    # Título da página
    st.title("Login")
    # Imagem da página
    st.image("http://placekitten.com/300/300")
    with st.form("login"):
        st.write("Login:")
        user = st.text_input("Usuário", type="default")
        password = st.text_input("Senha", type="password")
        submit = st.form_submit_button("Entrar")

        # Verifica se o usuário clicou em "Entrar"
        if submit:
            # Verifica se o usuário e senha estão vazios
            if user == "" or password == "":
                st.error("Usuário ou senha são obrigatórios!")
            # Verifica se o usuário e senha estão corretos
            elif check_login(user, password):
                st.success("Login realizado com sucesso!")
            else:
                st.error("Usuário ou senha incorretos!")

if __name__ == "__main__":
    login()
```

Agora vamos criar uma página inicial do nosso sistema, que será a página de boas vindas. Para isso, vamos criar um novo arquivo chamado `pages/home.py` e colocar o seguinte código:

```python
import streamlit as st

st.title("Boas Vindas")
st.write("Seja bem vindo ao nosso sistema!")
```

Agora, para nevegar até essa página, vamos adicionar a funcionaidade de navegação no nosso arquivo `login.py`:

```python
