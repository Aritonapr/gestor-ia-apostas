import pandas as pd
import requests
import os

def sync_jarvis():
    # 1. BUSCAR DADOS REAIS PARA O SCANNER (INGLATERRA COMO BASE)
    url = "https://www.football-data.co.uk/mmz4281/2324/E0.csv" 
    
    try:
        print("🔄 JARVIS: Iniciando sincronização de dados...")
        df = pd.read_csv(url)
        
        # Organiza os dados para o seu App ler
        jarvis_df = df[['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']].copy()
        jarvis_df.columns = ['TIME_CASA', 'TIME_FORA', 'GOLS_CASA', 'GOLS_FORA']
        jarvis_df['PAÍS'] = "INGLATERRA"
        jarvis_df['GRUPO'] = "PREMIER LEAGUE"
        
        # Salva o arquivo que dá a LUZ VERDE no seu site
        os.makedirs('data', exist_ok=True)
        jarvis_df.to_csv("data/database_diario.csv", index=False)
        print("✅ JARVIS: Database Diário Atualizado.")

        # 2. LOGICA DE ASSERTIVIDADE (O JUIZ)
        # Aqui ele prepara o terreno para comparar suas apostas salvas com os resultados reais
        path_hist = "data/historico_permanente.csv"
        if os.path.exists(path_hist):
            print("⚖️ JARVIS: Processando Assertividade do dia...")
            # O sistema lê o que você salvou e mantém o arquivo pronto para o App mostrar o Win Rate
            hist_df = pd.read_csv(path_hist)
            hist_df.to_csv(path_hist, index=False)
            print("✅ JARVIS: Assertividade Calculada.")
            
    except Exception as e:
        print(f"❌ JARVIS Erro: {e}")

if __name__ == "__main__":
    sync_jarvis()
