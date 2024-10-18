import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 

st.title("Meu primeiro dashboard")
st.header("Esse é um header")

st.markdown("""
    # Header
    ## Title
    ### Sub title 
    #### jjjj
""")

# Corrigido de st.tabs para st.tabs com lista
abs = st.tabs(["Botão", "Radio", "DataFrame", "Gráfico"])

# Corrigido o bloco with para incluir dois-pontos ":" e indentação correta
with abs[0]:
    if st.button("Clique aqui"):
        st.text("Você apertou o botão!")

with abs[1]:
    opcao = st.radio(
        "Escolha a opção:",
        ("flamengo", "corinthians", "palmeiras")
    )

    if opcao == "flamengo":
        st.info("Você é um urubu!")
    elif opcao == "corinthians":
        st.warning("Você é um campeão!")
    else:
        st.error("Você é um perdedor.")

# Removido o "with" solto e corrigido o caminho
caminho = "C:\\Users\\annac\\OneDrive\\Documentos\\projetos\\laerte\\frontend\\ibov.csv"
df = pd.read_csv(caminho)
st.dataframe(df)

fig, ax = plt.subplots()

fruits = ['apple', 'blueberry', 'cherry', 'orange']
counts = [40, 100, 30, 55]
bar_labels = ['red', 'blue', '_red', 'orange']
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('Fruit supply')
ax.set_title('Fruit supply by kind and color')
ax.legend(title='Fruit color')

st.pyplot(fig)


