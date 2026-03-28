if st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    
    # 1. DATABASE COMPLETO (LÓGICA)
    db_hierarquia = {
        "🇧🇷 BRASIL": {
            "Ligas Nacionais": ["BRASILEIRÃO SÉRIE A", "BRASILEIRÃO SÉRIE B", "BRASILEIRÃO SÉRIE C", "BRASILEIRÃO SÉRIE D"],
            "Campeonatos Estaduais": ["CAMPEONATO CARIOCA", "CAMPEONATO PAULISTA", "CAMPEONATO MINEIRO", "CAMPEONATO GAUCHO"],
            "Copas": ["COPA DO BRASIL", "COPA DO NORDESTE"]
        },
        "🌎 INTERNACIONAIS": {
            "Ligas Europeias": ["PREMIER LEAGUE", "LA LIGA", "SERIE A ITÁLIA", "BUNDESLIGA", "LIGUE 1"],
            "Copas Internacionais": ["CHAMPIONS LEAGUE", "LIGA EUROPA", "COPA DO MUNDO"],
            "Ásia/Outros": ["SAUDI PRO LEAGUE", "MLS"]
        }
    }

    # 2. SELEÇÃO DE FILTROS (INTERFACE)
    c1, c2, c3 = st.columns(3)
    with c1: sel_cat = st.selectbox("🌎 CATEGORIA", list(db_hierarquia.keys()))
    with c2: sel_tipo = st.selectbox("📂 TIPO", list(db_hierarquia[sel_cat].keys()))
    with c3: sel_camp = st.selectbox("🏆 CAMPEONATO", db_hierarquia[sel_cat][sel_tipo])

    c4, c5 = st.columns(2)
    with c4: t_casa = st.selectbox("🏠 MANDANTE", ["Flamengo", "Palmeiras", "São Paulo", "Corinthians", "Real Madrid", "Man City", "Brasil", "Argentina"])
    with c5: t_fora = st.selectbox("🚀 VISITANTE", ["Fluminense", "Vasco", "Barcelona", "Liverpool", "França", "Alemanha", "Bayer Leverkusen"])

    # 3. BOTÃO DE EXECUÇÃO
    if st.button("⚡ EXECUTAR ALGORITIMO", use_container_width=True):
        v_calc = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
        st.session_state.analise_bloqueada = {
            "liga": sel_camp, "casa": t_casa, "fora": t_fora, "vencedor": "CASA",
            "gols": "OVER 1.5", "stake": f"R$ {v_calc:,.2f}", "cantos": "9.5+", "data": datetime.now().strftime("%H:%M")
        }

    # 4. EXIBIÇÃO DOS RESULTADOS (CARDS)
    if st.session_state.analise_bloqueada:
        m = st.session_state.analise_bloqueada
        st.markdown(f"<h3 style='color:#9d54ff; text-align:center; margin-top:20px;'>RESULTADO: {m['casa']} vs {m['fora']}</h3>", unsafe_allow_html=True)
        
        r1, r2, r3, r4 = st.columns(4)
        with r1: draw_card("VENCEDOR", m['vencedor'], 85)
        with r2: draw_card("GOLS", m['gols'], 70)
        with r3: draw_card("STAKE", m['stake'], 100)
        with r4: draw_card("CANTOS", m['cantos'], 65)
        
        if st.button("📥 SALVAR CALL NO HISTÓRICO", use_container_width=True):
            st.session_state.historico_calls.append(m.copy())
            st.toast("✅ CALL SALVA NO HISTÓRICO!")
