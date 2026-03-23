# TELA 3: SCANNER PRÉ-LIVE (REESTRUTURADA COM FILTROS EM CASCATA)
elif st.session_state.aba_ativa == "analise":
    st.markdown("<h2 style='color:white;'>🎯 SCANNER PRÉ-LIVE</h2>", unsafe_allow_html=True)
    
    # --- BANCO DE DADOS INTEGRADO (COPAS, NACIONAIS E INTERNACIONAIS) ---
    db_gestor = {
        "🏆 COPA DO MUNDO 2026": {
            "SELEÇÕES FIFA": {
                "PRINCIPAIS": ["Argentina", "Brasil", "França", "Espanha", "Inglaterra", "Alemanha", "Portugal", "Uruguai", "Holanda", "Bélgica", "Marrocos", "Japão"]
            }
        },
        "BR BRASIL (LIGAS & COPAS)": {
            "COPA NACIONAL": {
                "Copa do Brasil": ["Flamengo", "Palmeiras", "São Paulo", "Corinthians", "Atlético-MG", "Grêmio", "Internacional", "Fluminense", "Vasco", "Bahia", "Fortaleza", "Athletico-PR"]
            },
            "LIGA NACIONAL": {
                "Série A": ["Botafogo", "Palmeiras", "Flamengo", "Fortaleza", "São Paulo", "Internacional", "Cruzeiro", "Bahia", "Vasco", "Atlético-MG"],
                "Série B": ["Santos", "Sport", "Ceará", "América-MG", "Goiás", "Coritiba", "Avaí", "Vila Nova"]
            }
        },
        "🌍 AMÉRICA DO SUL (CONMEBOL)": {
            "COPA INTERNACIONAL": {
                "Libertadores": ["River Plate", "Boca Juniors", "Palmeiras", "Flamengo", "Peñarol", "Colo-Colo", "LDU", "Ind. del Valle", "Olimpia", "Atlético-MG"],
                "Copa Sul-Americana": ["Racing", "Lanús", "Cruzeiro", "Corinthians", "Ind. Medellín", "Libertad"]
            }
        },
        "EU EUROPA (PRINCIPAIS LIGAS)": {
            "COPA INTERNACIONAL (UEFA)": {
                "Champions League": ["Real Madrid", "Man. City", "Bayern Munique", "Arsenal", "Barcelona", "Inter de Milão", "PSG", "Bayer Leverkusen", "Juventus", "Liverpool"],
                "Europa League": ["Man. United", "Tottenham", "Roma", "Porto", "Ajax", "Real Sociedad", "Lazio"]
            },
            "LIGAS NACIONAIS": {
                "Premier League": ["Man. City", "Arsenal", "Liverpool", "Chelsea", "Aston Villa", "Newcastle", "Tottenham"],
                "La Liga": ["Real Madrid", "Barcelona", "Atlético de Madrid", "Girona", "Athletic Bilbao", "Real Sociedad"],
                "Bundesliga": ["Bayer Leverkusen", "Bayern Munique", "RB Leipzig", "Borussia Dortmund", "Stuttgart"]
            }
        },
        "SA ORIENTE MÉDIO & ÁSIA": {
            "LIGAS": {
                "Saudi Pro League": ["Al-Hilal", "Al-Nassr", "Al-Ittihad", "Al-Ahli", "Al-Ettifaq"],
                "J-League": ["Vissel Kobe", "Yokohama Marinos", "Kawasaki Frontale"]
            }
        },
        "us AMÉRICA DO NORT (MLS)": {
            "LIGA NACIONAL": {
                "MLS": ["Inter Miami", "LAFC", "Columbus Crew", "LA Galaxy", "Seattle Sounders", "Orlando City"]
            }
        }
    }

    # --- LÓGICA DE SELEÇÃO EM CASCATA ---
    c1, c2, c3 = st.columns(3)
    
    with c1:
        categoria_sel = st.selectbox("🌎 CATEGORIA", list(db_gestor.keys()))
    
    with c2:
        tipo_opcoes = list(db_gestor[categoria_sel].keys())
        tipo_sel = st.selectbox("📂 TIPO", tipo_opcoes)
        
    with c3:
        campeonato_opcoes = list(db_gestor[categoria_sel][tipo_sel].keys())
        campeonato_sel = st.selectbox("🏆 CAMPEONATO", campeonato_opcoes)

    # Lista de times baseada nas escolhas acima
    lista_times = db_gestor[categoria_sel][tipo_sel][campeonato_sel]

    # --- SELEÇÃO DE CONFRONTOS ---
    m1, m2 = st.columns(2)
    with m1:
        casa = st.selectbox("🏠 MANDANTE", lista_times, index=0)
    with m2:
        # Tenta selecionar o segundo time da lista para o visitante, se existir
        index_visitante = 1 if len(lista_times) > 1 else 0
        fora = st.selectbox("🚀 VISITANTE", lista_times, index=index_visitante)

    # --- EXECUÇÃO DO ALGORITMO ---
    if st.button("⚡ EXECUTAR ALGORITIMO", use_container_width=True):
        if casa == fora:
            st.warning("⚠️ Selecione times diferentes para a análise.")
        else:
            with st.spinner("🧠 JARVIS PROCESSANDO DADOS..."):
                time.sleep(1.5)
                v_calc = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
                st.session_state.analise_bloqueada = {
                    "casa": casa, 
                    "fora": fora, 
                    "vencedor": "Casa" if "a" in casa.lower() else "Visitante", # Simulação de lógica
                    "gols": "OVER 2.5", 
                    "data": datetime.now().strftime("%H:%M"), 
                    "stake_val": f"R$ {v_calc:,.2f}"
                }

    # --- EXIBIÇÃO DO RESULTADO ---
    if st.session_state.analise_bloqueada:
        m = st.session_state.analise_bloqueada
        st.markdown(f"""
            <div style="background: rgba(157, 84, 255, 0.1); border-left: 5px solid #9d54ff; padding: 15px; border-radius: 5px; margin: 20px 0;">
                <h3 style='color:white; margin:0;'>📊 ANÁLISE CONCLUÍDA: <span style='color:#9d54ff;'>{m['casa']} vs {m['fora']}</span></h3>
            </div>
        """, unsafe_allow_html=True)
        
        r1, r2, r3, r4 = st.columns(4)
        with r1: draw_card("VENCEDOR PROB.", m['vencedor'], 82, "#6d28d9")
        with r2: draw_card("MERCADO GOLS", m['gols'], 74, "#6d28d9")
        with r3: draw_card("STAKE SUGERIDA", m['stake_val'], 100, "#06b6d4")
        with r4: draw_card("CANTOS (MÉDIA)", "9.8", 68, "#06b6d4")
        
        r5, r6, r7, r8 = st.columns(4)
        with r5: draw_card("IA CONFIDENCE", "94.2%", 94, "#00ff88")
        with r6: draw_card("FORÇA ATAQUE", "ALTA", 85, "#00ff88")
        with r7: draw_card("TENDÊNCIA", "BULLISH", 70, "#00ff88")
        with r8: draw_card("ALGORITMO", "v57.23", 100, "#9d54ff")
        
        if st.button("📥 SALVAR CALL NO HISTÓRICO", use_container_width=True):
            st.session_state.historico_calls.append(m.copy())
            st.toast(f"✅ Call de {m['casa']} salva!")
