import streamlit as st
import random

st.header('Jogando uma moeda')

# Adicionando um botão interativo
if st.button('Lançar Moeda'):
    resultado = random.choice(['Cara', 'Coroa'])
    st.success(f'O resultado é: {resultado}')
else:
    st.info('Clique no botão acima para tentar a sorte!')