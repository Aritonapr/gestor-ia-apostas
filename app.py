elif st.session_state.aba_ativa == "gestao":
    # 1. INICIALIZAÇÃO LÓGICA (BACK-END)
    if 'meta_diaria' not in st.session_state: st.session_state.meta_diaria = 3.0
    if 'stop_loss' not in st.session_state: st.session_state.stop_loss = 5.0

    # 2. HEADER DA SEÇÃO (CSS PRESERVADO)
    st.markdown('<div class="banca-title-banner">💰 GESTÃO DE BANCA INTELIGENTE</div>', unsafe_allow_html=True)
    
    # 3. ESTRUTURA DE COLUNAS (CONFORME IMAGEM)
    col_input, col_display = st.columns([1.2, 2])
    
    with col_input:
        st.session_state.banca_total = st.number_input("BANCA TOTAL (R$)", value=float(st.session_state.banca_total), step=50.0)
        st.session_state.stake_padrao = st.slider("STAKE POR OPERAÇÃO (%)", 0.1, 10.0, float(st.session_state.stake_padrao))
        st.session_state.meta_diaria = st.slider("META DIÁRIA - STOP GAIN (%)", 0.5, 20.0, float(st.session_state.meta_diaria))
        st.session_state.stop_loss = st.slider("LIMITE DE PERDA - STOP LOSS (%)", 0.5, 50.0, float(st.session_state.stop_loss))

    # 4. PROCESSAMENTO MATEMÁTICO (INVISÍVEL)
    v_stake = st.session_state.banca_total * (st.session_state.stake_padrao / 100)
    v_gain = st.session_state.banca_total * (st.session_state.meta_diaria / 100)
    v_loss = st.session_state.banca_total * (st.session_state.stop_loss / 100)
    v_alvo = st.session_state.banca_total + v_gain
    
    qtd_meta = int(v_gain / v_stake) if v_stake > 0 else 0
    qtd_loss = int(v_loss / v_stake) if v_stake > 0 else 0
    
    # Lógica de Saúde de Banca
    saude_label = "EXCELENTE" if st.session_state.stake_padrao <= 1.5 else "MODERADA" if st.session_state.stake_padrao <= 3 else "ALTO RISCO"
    cor_saude = "linear-gradient(90deg, #10b981, #059669)" if saude_label == "EXCELENTE" else "linear-gradient(90deg, #f59e0b, #d97706)"
    if saude_label == "ALTO RISCO": cor_saude = "linear-gradient(90deg, #ef4444, #991b1b)"

    with col_display:
        # Linha 1 de Cards (SAÍDA DE DATA)
        r1_c1, r1_c2, r1_c3, r1_c4 = st.columns(4)
        with r1_c1: draw_card("VALOR ENTRADA", f"R$ {v_stake:,.2f}", 100)
        with r1_c2: draw_card("STOP GAIN (R$)", f"R$ {v_gain:,.2f}", 100)
        with r1_c3: draw_card("STOP LOSS (R$)", f"R$ {v_loss:,.2f}", 100)
        with r1_c4: draw_card("ALVO FINAL", f"R$ {v_alvo:,.2f}", 100)
        
        # Linha 2 de Cards
        r2_c1, r2_c2, r2_c3, r2_c4 = st.columns(4)
        with r2_c1: draw_card("RISCO TOTAL", f"{st.session_state.stake_padrao}%", st.session_state.stake_padrao * 10)
        with r2_c2: draw_card("ENTRADAS/META", f"{qtd_meta}", 70)
        with r2_c3: draw_card("ENTRADAS/LOSS", f"{qtd_loss}", 40)
        with r2_c4: draw_card("SAÚDE BANCA", saude_label, 100, color_footer=cor_saude)
