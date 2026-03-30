import pandas as pd
import requests
import os

# ----------------------------------------------------------------
# PROTOCOLO JARVIS v62.0 - CONSOLIDADOR DE BIG DATA (2021-2025)
# ----------------------------------------------------------------

def baixar_e_consolidar_historico():
    print("🤖 Jarvis: Iniciando download das temporadas 2021 a 2025...")
    
    # Lista de ligas e temporadas (EPL como base principal)
    # Fontes oficiais de CSV de futebol (Football-Data.co.uk)
    urls = [
        "https://www.football-data.co.uk/mmz4281/2021/E0.csv",
        "https://www.football-data.co.uk/mmz4281/2122/E0.csv",
        "https://www.football-data.co.uk/mmz4281/2223/E0.csv",
        "https://www.football-data.co.uk/mmz4281/2324/E0.csv",
        "https://www.football-data.co.uk/mmz4281/2425/E0.csv"
    ]
    
    dfs = []
    
    for url in urls:
        try:
            print(f"📥 Baixando: {url}")
            # Baixa o CSV e mantém as colunas que o Jarvis usa (Gols, Cantos, Resultados)
            df_temp = pd.read_csv(url)
            dfs.append(df_temp)
        except Exception as e:
            print(f"⚠️ Erro ao baixar temporada: {e}")

    if dfs:
        # Junta todos os anos em um único banco de dados
        super_historico = pd.concat(dfs, ignore_index=True)
        
        # Garante a pasta data
        if not os.path.exists('data'):
            os.makedirs('data')
            
        # Salva o arquivo final que o App.py e o Sync_Data.py vão ler
        super_historico.to_csv('data/historico_5_temporadas.csv', index=False)
        
        print(f"✅ Sucesso! O arquivo 'historico_5_temporadas.csv' agora tem {len(super_historico)} jogos reais.")
        print("🚀 Jarvis está pronto para calcular a assertividade real para 29/03/2026.")
    else:
        print("❌ Nenhuma temporada foi baixada. Verifique a conexão.")

if __name__ == "__main__":
    baixar_e_consolidar_historico()
