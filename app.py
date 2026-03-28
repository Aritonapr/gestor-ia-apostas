if st.button("⚡ EXECUTAR ALGORITIMO", use_container_width=True):
        v_calc = (st.session_state.banca_total * st.session_state.stake_padrao / 100)
        res = motor_ia_jarvis(df_diario, t_casa, t_fora)
        
        # Injeção Direta
        st.session_state.analise_bloqueada = {
            "casa": t_casa, "fora": t_fora, "vencedor": res['vencedor'], "gols": res['gols'], 
            "data": datetime.now().strftime("%H:%M"), "stake_val": f"R$ {v_calc:,.2f}",
            "luz": res['luz'], "motivo": res['motivo'], "cor": res['cor'], 
            "confia": res['confia'], "cantos": res['cantos'], "pressao": res['pressao']
        }
