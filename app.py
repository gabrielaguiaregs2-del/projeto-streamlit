import pandas as pd
import scipy.stats
import streamlit as st
import time

# 1. Configuração da Memória do App (Session State)
# Isso faz com que o app não "esqueça" os resultados anteriores
if 'experiment_no' not in st.session_state:
    st.session_state['experiment_no'] = 0
if 'df_experiment_results' not in st.session_state:
    st.session_state['df_experiment_results'] = pd.DataFrame(columns=['no', 'iterations', 'mean'])

st.header('Jogando uma moeda')

# 2. Criar o gráfico vazio (começando em 0.5)
chart = st.line_chart([0.5])

# 3. Função que emula o lançamento da moeda
def toss_coin(n):
    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)

    mean = None
    outcome_no = 0
    outcome_1_count = 0

    for r in trial_outcomes:
        outcome_no += 1
        if r == 1:
            outcome_1_count += 1
        mean = outcome_1_count / outcome_no
        chart.add_rows([mean])  # Adiciona uma linha nova no gráfico em tempo real
        time.sleep(0.05)       # Faz uma pequena pausa para dar o efeito de animação

    return mean

# 4. Widgets de Entrada (Slider e Botão)
number_of_trials = st.slider('Número de tentativas?', 1, 1000, 10)
start_button = st.button('Executar')

# 5. Lógica ao clicar no botão
if start_button:
    st.write(f'Executando o experimento de {number_of_trials} tentativas.')
    
    # Aumenta o contador de experimentos
    st.session_state['experiment_no'] += 1
    
    # Chama a função e guarda a média final
    mean = toss_coin(number_of_trials)
    
    # Adiciona o resultado na tabela (DataFrame) na memória
    st.session_state['df_experiment_results'] = pd.concat([
        st.session_state['df_experiment_results'],
        pd.DataFrame(data=[[st.session_state['experiment_no'],
                            number_of_trials,
                            mean]],
                     columns=['no', 'iterations', 'mean'])
        ],
        axis=0)
    
    # Reseta o índice da tabela para ficar organizado
    st.session_state['df_experiment_results'] = \
        st.session_state['df_experiment_results'].reset_index(drop=True)

# 6. Exibe a tabela de resultados acumulados
st.write(st.session_state['df_experiment_results'])