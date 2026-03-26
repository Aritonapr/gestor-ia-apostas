# --- TELA: ASSERTIVIDADE IA (AGORA COM 8 KPI CARDS) ---
elif st.session_state.aba_ativa == "assertividade":
    st.markdown("<h2 style='color:white;'>🧠 CENTRAL DE ASSERTIVIDADE & IA</h2>", unsafe_allow_html=True)
    
    # LINHA 1 DE KPIS
    k1, k2, k3, k4 = st.columns(4)
    with k1: draw_card("ACERTOS (GREENS)", f"{len(df_performance[df_performance['STATUS']=='GREEN'])}", 100, "#00ff88")
    with k2: draw_card("ERROS (REDS)", f"{len(df_performance[df_performance['STATUS']=='RED'])}", 100, "#ff4b4b")
    with k3: draw_card("ROI GLOBAL", "14.2%", 75, "#9d54ff")
    with k4: draw_card("LUCRO LÍQUIDO", f"R$ 420,00", 100, "#00ff88")
    
    # LINHA 2 DE KPIS
    k5, k6, k7, k8 = st.columns(4)
    with k5: draw_card("DRAWDOWN MÁX", "4.1%", 20, "#ffcc00")
    with k6: draw_card("MERCADO ELITE", "CANTOS (88%)", 88, "#06b6d4")
    with k7: draw_card("STREAK ATUAL", "5 ✅", 100, "#00ff88")
    with k8: draw_card("MEMÓRIA IA", f"{len(df_performance)} JOGOS", 100, "#9d54ff")

    # --- LÓGICA DO SCANNER CONECTADO (PRÉ-LIVE) ---
elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE CONECTADO</h2>", unsafe_allow_html=True)
    
    # Aqui eu injetarei a lógica que lê o df_diario 
    # e preenche os nomes dos times automaticamente.
