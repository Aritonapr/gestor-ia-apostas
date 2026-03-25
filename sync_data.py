import pandas as pd
import requests
import os

def processar_assertividade():
    path_hist = "data/historico_permanente.csv"
    # URL de resultados reais (Premier League exemplo)
    url_resultados = "https://www.football-data.co.uk/mmz4281/2324/E0.csv"
    
    if os.path.exists(path_hist):
        try:
            hist = pd.read_csv(path_hist)
            res = pd.read_csv(url_resultados)
            
            # O JARVIS compara cada aposta com o resultado real
            for index, row in hist.iterrows():
                # Procura o jogo no arquivo de resultados
                jogo_real = res[(res['HomeTeam'] == row['casa']) & (res['AwayTeam'] == row['fora'])]
                
                if not jogo_real.empty:
                    gols_total = jogo_real['FTHG'].values[0] + jogo_real['FTAG'].values[0]
                    # Exemplo: Se aposta foi OVER 1.5 e saiu 2 gols ou mais = GREEN
                    if row['gols'] == "OVER 1.5" and gols_total >= 2:
                        hist.at[index, 'resultado_ia'] = "GREEN"
                    elif row['gols'] == "OVER 1.5" and gols_total < 2:
                        hist.at[index, 'resultado_ia'] = "RED"
            
            hist.to_csv(path_hist, index=False)
            print("⚖️ JARVIS: Resultados processados com sucesso.")
        except Exception as e:
            print(f"Erro ao processar assertividade: {e}")

if __name__ == "__main__":
    processar_assertividade()
