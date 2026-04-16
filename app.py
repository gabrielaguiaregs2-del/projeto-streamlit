import streamlit as st
import random

# Título do App
st.title('🪙 Simulador de Lançamento de Moeda')

st.write('Este é um aplicativo para testar a sorte!')

# Criando um botão
if st.button('Lançar Moeda'):
    resultado = random.choice(['Cara', 'Coroa'])
    if resultado == 'Cara':
        st.success(f'Resultado: **{resultado}**! ✨')
    else:
        st.warning(f'Resultado: **{resultado}**! 🎲')
    
    st.balloons() # Isso joga balões na tela quando clica!
else:
    st.info('Clique no botão para jogar.')