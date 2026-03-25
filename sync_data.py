import pandas as pd
import requests
import os

def processar_assertividade():
    path_hist = "data/historico_permanente.csv"
    # URL de resultados reais da Premier League temporada atual 24/25
    url_resultados = "https://www.football-data.co.uk/mmz4281/2425/E0.csv"
    
    if os.path.exists(path_hist):
        try:
            print("⚖️ JARVIS: Iniciando conferência de resultados...")
            hist = pd.read_csv(path_hist)
            res = pd.read_csv(url_resultados)
            
            for index, row in hist.iterrows():
                # O Juiz procura o jogo pelo nome dos times
                jogo_real = res[(res['HomeTeam'] == row['casa']) & (res['AwayTeam'] == row['fora'])]
                
                if not jogo_real.empty:
                    # Soma os gols do placar real
                    gols_total = jogo_real['FTHG'].values[0] + jogo_real['FTAG'].values[0]
                    
                    # Regra do Juiz: Se aposta foi OVER 1.5 e saiu 2 ou mais gols = GREEN
                    if row['gols'] == "OVER 1.5" and gols_total >= 2:
                        hist.at[index, 'resultado_ia'] = "GREEN"
                    elif row['gols'] == "OVER 1.5" and gols_total < 2:
                        hist.at[index, 'resultado_ia'] = "RED"
            
            hist.to_csv(path_hist, index=False)
            print("✅ JARVIS: Assertividade atualizada no banco de dados.")
        except Exception as e:
            print(f"❌ Erro no Juiz: {e}")

if __name__ == "__main__":
    processar_assertividade()
