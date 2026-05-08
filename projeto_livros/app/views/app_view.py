import streamlit as st
import os
import requests

st.set_page_config(page_title='Biblioteca')

API_URL = os.getenv('API_URL')

st.title('Gestor de Livros')

with st.sidebar:
    st.header('Novo livro')
    titulo = st.text_input('Informe o título do livro')
    autor = st.text_input('Autor')
    if st.button('Cadastrar'):
        if titulo and autor:
            res = requests.post(API_URL, json={'título': titulo, 'autor':autor})
            if res.status_code == 200:
                st.success('Livro salvo')
            else:
                st.error('Ocorreu um erro')

st.subheader('Livros disponíveis')
if st.button('Livros disponíveis'):
    try:
        livros = requests.get(API_URL).json()
        for l in livros:
            st.info(f'{l['titulo']} : {l['autor']}')
    except:
        st.error('Não foi possível conectar a API - Verifique o servidor')
