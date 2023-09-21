import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import time

# Teste
st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

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
                # Espera 2 segundos
                time.sleep(2)
                # Redireciona para a página de boas vindas
                switch_page("home")
            else:
                st.error("Usuário ou senha incorretos!")

if __name__ == "__main__":
    login()