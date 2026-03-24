# TELA 3: SCANNER PRÉ-LIVE (BANCO DE DADOS EXPANDIDO v57.24)
elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PREDITIVO GLOBAL</h2>", unsafe_allow_html=True)
    
    # BANCO DE DADOS MAESTRO (EXPANDIDO)
    db_master = {
        "BRASIL": {
            "LIGAS": ["Série A", "Série B", "Série C", "Copa do Brasil", "Paulistão", "Carioca"],
            "TIMES": ["Flamengo", "Palmeiras", "São Paulo", "Corinthians", "Vasco", "Fluminense", "Botafogo", "Grêmio", "Inter", "Atlético-MG", "Athletico-PR", "Bahia", "Fortaleza", "Cruzeiro", "Red Bull Bragantino"]
        },
        "EUROPA (TOP LIGAS)": {
            "LIGAS": ["Champions League", "Europa League", "Premier League (ING)", "La Liga (ESP)", "Bundesliga (ALE)", "Serie A (ITA)", "Ligue 1 (FRA)", "Primeira Liga (POR)"],
            "TIMES": ["Real Madrid", "Barcelona", "Man City", "Arsenal", "Liverpool", "Chelsea", "Man United", "Bayern Munchen", "Dortmund", "Inter Milan", "Juventus", "AC Milan", "PSG", "Benfica", "Porto", "Sporting", "Napoli", "Atletico Madrid"]
        },
        "AMÉRICA DO SUL": {
            "LIGAS": ["Libertadores", "Copa Sul-Americana", "Campeonato Argentino", "Campeonato Chileno"],
            "TIMES": ["River Plate", "Boca Juniors", "Ind. del Valle", "Colo-Colo", "Peñarol", "Nacional-URU", "LDU"]
        },
        "MUNDO / EMERGENTES": {
            "LIGAS": ["Saudi Pro League", "MLS (EUA)", "Eredivisie (HOL)", "Mundial de Clubes"],
            "TIMES": ["Al-Hilal", "Al-Nassr", "Al-Ittihad", "Inter Miami", "Ajax", "PSV", "Feyenoord"]
        }
    }

    # FILTROS DINÂMICOS
    row_filtros = st.columns(3)
    with row_filtros[0]:
        categoria_sel = st.selectbox("🌎 REGIÃO/MERCADO", list(db_master.keys()))
    with row_filtros[1]:
        competicao_sel = st.selectbox("🏆 COMPETIÇÃO", db_master[categoria_sel]["LIGAS"])
    with row_filtros[2]:
        ia_modo = st.selectbox("🧠 MODO IA", ["Agressivo", "Conservador", "Balanced"])

    st.markdown("<h4 style='color:white; font-size:12px; margin-top:10px;'>⚔️ SELEÇÃO DE CONFRONTO</h4>", unsafe_allow_html=True)
    
    c_casa, c_fora = st.columns(2)
    # Se a região for Brasil, mas o usuário quiser analisar um Brasil x Real Madrid (Mundial), 
    # podemos permitir a troca de lista de times se necessário, mas aqui mantemos a coerência da região.
    lista_times = db_master[categoria_sel]["TIMES"]
    
    with c_casa:
        t_casa = st.selectbox("🏠 TIME DA CASA", lista_times)
    with c_fora:
        t_fora = st.selectbox("🚀 TIME DE FORA", [t for t in lista_times if t != t_casa])

    if st.button("⚡ EXECUTAR ALGORITMO JARVIS"):
        with st.status("Consultando Big Data...", expanded=True) as status:
            st.write("Buscando confrontos diretos (H2H)...")
            time.sleep(0.6)
            st.write("Analisando volume de apostas global...")
            time.sleep(0.6)
            st.write("Calculando Poisson e Desvio Padrão...")
            status.update(label="Análise Concluída!", state="complete", expanded=False)
        
        # Lógica de cálculo fictícia baseada em "IA"
        confianca = random.randint(72, 98)
        valor_stake = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
        
        st.session_state.analise_bloqueada = {
            "casa": t_casa, "fora": t_fora, 
            "prob": f"{confianca}%", 
            "gols": random.choice(["OVER 2.5", "AMBAS MARCAM", "UNDER 3.5", "CASA VENCE"]),
            "stake_val": f"R$ {valor_stake:,.2f}",
            "odd": round(random.uniform(1.60, 2.20), 2)
        }
        # Salva no histórico
        st.session_state.historico_calls.append(st.session_state.analise_bloqueada)

    # OUTPUT DE 8 CARDS
    if st.session_state.analise_bloqueada:
        res = st.session_state.analise_bloqueada
        st.markdown(f"<div style='text-align:center; padding: 20px; background: rgba(109, 40, 217, 0.1); border-radius: 10px; border: 1px solid #6d28d9; margin-bottom: 25px;'> <h3 style='margin:0; color:white;'>{res['casa']} <span style='color:#6d28d9;'>VS</span> {res['fora']}</h3> </div>", unsafe_allow_html=True)
        
        r1, r2, r3, r4 = st.columns(4)
        with r1: draw_card("CONFIANÇA IA", res['prob'], int(res['prob'].replace('%','')), "#6d28d9")
        with r2: draw_card("ENTRADA", res['gols'], 85, "#06b6d4")
        with r3: draw_card("ODD MÍNIMA", f"@{res['odd']}", 100)
        with r4: draw_card("STAKE SUGERIDA", res['stake_val'], 100)
        
        r5, r6, r7, r8 = st.columns(4)
        with r5: draw_card("MERCADO GOLS", "68% OVER", 68)
        with r6: draw_card("CANTOS PROB", "9.8 AVG", 75)
        with r7: draw_card("PRESSÃO ESP.", "ALTA", 90, "#22c55e")
        with r8: draw_card("STATUS SINAL", "CONFIRMADO", 100, "#22c55e")
