import pandas as pd
import requests
import io
import os

def baixar_e_salvar():
    print("🚀 Iniciando Coleta de Big Data (2021-2026)...")
    ligas = ['E0', 'SP1', 'I1', 'D1', 'F1']
    base_url = "https://www.football-data.co.uk/mmz4281/"
    
    # Configuração de Temporadas
    temporadas_hist = ['2021', '2122', '2223', '2324', '2425']
    temporada_atual = ['2526'] # Representa a temporada que termina em 2026

    def coletar(lista):
        df_final = pd.DataFrame()
        for temp in lista:
            for liga in ligas:
                url = f"{base_url}{temp}/{liga}.csv"
                try:
                    res = requests.get(url, timeout=15)
                    if res.status_code == 200:
                        df_temp = pd.read_csv(io.StringIO(res.text))
                        df_resumo = df_temp[['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']].copy()
                        df_resumo.columns = ['CASA', 'FORA', 'GOLS_CASA', 'GOLS_FORA']
                        df_resumo['TEMPORADA'] = temp
                        df_final = pd.concat([df_final, df_resumo], ignore_index=True)
                        print(f"✅ Baixado: {liga} {temp}")
                except: continue
        return df_final

    if not os.path.exists('data'): os.makedirs('data')

    # Gerar Histórico
    df_h = coletar(temporadas_hist)
    if not df_h.empty:
        df_h.to_csv('data/historico_5_temporadas.csv', index=False)
        print("📦 Histórico 2021-2025 salvo.")

    # Gerar 2026
    df_26 = coletar(temporada_atual)
    if not df_26.empty:
        df_26.to_csv('data/temporada_2026.csv', index=False)
        print("📦 Temporada 2026 salva.")

if __name__ == "__main__":
    baixar_e_salvar()
