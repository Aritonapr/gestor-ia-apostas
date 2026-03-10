import streamlit as st

# Configuração da página
st.set_page_config(page_title="GIAE - Gestor IA", layout="wide")

# CSS para padronizar os botões (Tamanho, Cor e Alinhamento)
st.markdown("""
    <style>
    div.stButton > button {
        width: 100%;
        height: 80px;
        border-radius: 10px;
        background-color: #5B9BD5;
        color: white;
        font-weight: bold;
        font-size: 16px;
        border: 2px solid #41719C;
        text-transform: uppercase;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    div.stButton > button:hover {
        background-color: #41719C;
        color: white;
    }
    h1 {
        text-align: left;
        color: #000000;
        font-family: Arial;
        border-bottom: 2px solid #000;
        padding-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Título Principal
st.title("GIAE - GESTOR IA APOSTA ESPORTIVA")

# Criando as Colunas conforme seu desenho no Word
col1, col2, col3, col4 = st.columns([1, 1.5, 1.5, 1.2])

# Coluna 1: Categorias
with col1:
    if st.button("CAMPEONATOS"):
        st.info("Lista de Campeonatos Selecionada")
    
    st.write("") # Espaçamento
    if st.button("EUROPA"):
        st.info("Filtro: Europa Ativado")
    
    st.write("")
    if st.button("UEFA / INTER"):
        st.info("Filtro: Competições Internacionais")
        
    st.write("")
    if st.button("AMERICA DO SUL"):
        st.info("Filtro: América do Sul Ativado")

# Coluna 2 e 3: Processamento Central
with col2:
    if st.button("PROCESSAR APOSTAS DO\nDIA AUTOMATICAMENTE"):
        st.warning("Processando IA... (Aguardando seu código)")

with col3:
    if st.button("APOSTAS DO DIA\nSEGUINTE"):
        st.warning("Analisando calendário de amanhã...")

# Coluna 4: Resultados (Lado Direito)
with col4:
    if st.button("OPORTUNIDADE DE\nAPOSTAS ENCONTRADA"):
        st.success("Exibindo Melhores Odds...")
        
    st.write("")
    if st.button("TABELA DE JOGOS\nAUTOMATICO"):
        st.write("Gerando Tabela...")

# Rodapé de Status
st.markdown("---")
st.caption("Sistema GIAE pronto para receber integração de dados.")
