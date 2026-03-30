import pandas as pd
import requests
import os
from datetime import datetime

# ==============================================================================
# [PROTOCOLO JARVIS v62.6 - MOTOR DE ELITE: API GLOBO ESPORTE (GE)]
# ==============================================================================

def calcular_confianca_jarvis(time_casa, df_hist):
    conf = 75.0
    if df_hist is not None:
        try:
            termo = str(time_casa)[:4]
            filtro = df_hist[df_hist['Casa'].str.contains(termo, case=False, na=False)]
            if not filtro.empty:
                taxa = (len(filtro[filtro['Resultado'] == 'H']) / len(filtro)) * 100
                conf = round(taxa + 5, 1)
        except: pass
    return f"{min(max(conf, 65.0), 98.4)}%"

def sync():
    now_str = datetime.now().strftime('%d/%m/%Y %H:%M')
    print(f"🤖 JARVIS v62.6 | ACESSANDO API GLOBO ESPORTE: {now_str}")
    
    path_hist = "data/historico_5_temporadas.csv"
    df_hist = pd.read_csv(path_hist) if os.path.exists(path_hist) else None

    # ENDPOINT DA API DA GLOBO (Altamente estável e oficial)
    url = "https://api.globoesporte.globo.com/tabela/jogos-do-dia"
    
    try:
        response = requests.get(url, timeout=20)
        dados = response.json() # A API já devolve os dados prontos
        
        lista_final = []
        
        # A API da Globo organiza por jogos
        for jogo in dados:
            try:
                casa = jogo['equipes']['mandante']['nome_popular']
                fora = jogo['equipes']['visitante']['nome_popular']
                liga = jogo['campeonato']['nome']
                
                # Status amigável
                status_raw = jogo['status'] # 'agendado', 'andamento', 'encerrado'
                hora = jogo['hora_real'] if jogo['hora_real'] else "---"
                
                status_final = "AO VIVO" if status_raw == "andamento" else hora.upper()
                if status_raw == "encerrado": status_final = "ENCERRADO"

                conf = calcular_confianca_jarvis(casa, df_hist)
                
                lista_final.append({
                    "STATUS": status_final,
                    "LIGA": liga.upper(),
                    "CASA": casa,
                    "FORA": fora,
                    "GOLS": "OVER 1.5",
                    "CONF": conf,
                    "CANTOS": "9.5+",
                    "CHUTES": "10+",
                    "DEFESAS": "6+",
                    "TMETA": "14+",
                    "ULTIMA_ATUALIZACAO": now_str
                })
            except: continue

        if lista_final:
            df = pd.DataFrame(lista_final).drop_duplicates(subset=['CASA', 'FORA'])
            if not os.path.exists('data'): os.makedirs('data')
            df.to_csv("data/database_diario.csv", index=False)
            print(f"✅ SUCESSO TOTAL: {len(df)} JOGOS REAIS DE HOJE CAPTURADOS!")
        else:
            print("⚠️ API retornou zero jogos para este exato momento.")

    except Exception as e:
        print(f"❌ ERRO CRÍTICO NA API GLOBO: {e}")

if __name__ == "__main__":
    sync()
