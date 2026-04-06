import pandas as pd
import requests
import io
import os
import time

def baixar_e_salvar():
    print("🚀 Jarvis: Iniciando Coleta de Big Data (2021-2026)...")
    # Ligas principais: Inglaterra, Espanha, Itália, Alemanha, França
    ligas = ['E0', 'SP1', 'I1', 'D1', 'F1']
    base_url = "https://www.football-data.co.uk/mmz4281/"
    
    # Temporadas históricas e a atual de 2026
    temporadas_hist = ['2021', '2122', '2223', '2324', '2425']
    temporada_atual = ['2526']

    def coletar(lista):
        df_final = pd.DataFrame()
        for temp in lista:
            for liga in ligas:
                url = f"{base_url}{temp}/{liga}.csv"
                try:
                    # Timeout maior e User-Agent para evitar bloqueios
                    headers = {'User-Agent': 'Mozilla/5.0'}
                    res = requests.get(url, headers=headers, timeout=30)
                    if res.status_code == 200:
                        df_temp = pd.read_csv(io.StringIO(res.text))
                        # Padroniza as colunas necessárias para o seu App.py
                        df_resumo = df_temp[['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']].copy()
                        df_resumo.columns = ['CASA', 'FORA', 'GOLS_CASA', 'GOLS_FORA']
                        df_resumo['TEMPORADA'] = temp
                        df_final = pd.concat([df_final, df_resumo], ignore_index=True)
                        print(f"✅ Download concluído: {liga} {temp}")
                    else:
                        print(f"⚠️ Ignorado: {liga} {temp} (Status {res.status_code})")
                    
                    # Pausa estratégica para evitar banimento de IP
                    time.sleep(2)
                except Exception as e:
                    print(f"❌ Erro em {liga} {temp}: {e}")
                    continue
        return df_final

    # Garante que a pasta data existe
    if not os.path.exists('data'):
        os.makedirs('data')

    # Processa Histórico (2021-2025)
    print("\n--- Baixando Bloco Histórico ---")
    df_historico = coletar(temporadas_hist)
    if not df_historico.empty:
        df_historico.to_csv('data/historico_5_temporadas.csv', index=False)
        print(f"📦 Super Histórico Salvo: {len(df_historico)} jogos.")

    # Processa Temporada 2026
    print("\n--- Baixando Bloco 2026 ---")
    df_2026 = coletar(temporada_atual)
    if not df_2026.empty:
        df_2026.to_csv('data/temporada_2026.csv', index=False)
        print(f"📦 Temporada 2026 Salva: {len(df_2026)} jogos.")

if __name__ == "__main__":
    baixar_e_salvar()
