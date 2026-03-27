import pandas as pd
import requests
import os
from datetime import datetime
import io
import time

# ==============================================================================
# 🧠 JARVIS AUTO-LEARNING & SYNC v96.00 (CONSTRUTOR DE BASE HISTÓRICA)
# ==============================================================================

PATH_HISTORICO = "data/historico_5_temporadas.csv"
PATH_DATABASE = "data/database_diario.csv"

def criar_base_historica_se_nao_existir():
    """
    JARVIS: "Se o senhor não tem os dados, eu os busco para o senhor."
    Baixa dados reais das últimas 5 temporadas das ligas principais.
    """
    if os.path.exists(PATH_HISTORICO):
        print("✅ Memória de 5 temporadas já existe. Pulando download.")
        return

    print("📡 Iniciando construção de base histórica (5 temporadas)... Isso pode levar um minuto.")
    leagues = ['E0', 'SP1', 'I1', 'D1', 'F1'] # Inglaterra, Espanha, Itália, Alemanha, França
    seasons = ['1920', '2021', '2122', '2223', '2324']
    
    all_data = []
    
    for season in seasons:
        for league in leagues:
            try:
                url = f"https://www.football-data.co.uk/mmz4281/{season}/{league}.csv"
                print(f"📥 Baixando Temporada {season} - Liga {league}...")
                df = pd.read_csv(url)
                # Padronizar colunas essenciais
                df = df[['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR']]
                all_data.append(df)
                time.sleep(1) # Evitar bloqueio do servidor
            except Exception as e:
                print(f"⚠️ Erro ao baixar {league} {season}: {e}")

    if all_data:
        df_final = pd.concat(all_data, ignore_index=True)
        # Renomear para o padrão do nosso motor de 7 níveis
        df_final.columns = ['Data', 'Casa', 'Fora', 'GolsCasa', 'GolsFora', 'Resultado']
        if not os.path.exists('data'): os.makedirs('data')
        df_final.to_csv(PATH_HISTORICO, index=False)
        print(f"✅ Base histórica criada com {len(df_final)} jogos reais!")

def motor_ia_v96(casa, fora, df_hist):
    """
    Cálculo Real baseado na média de gols dos últimos 5 anos.
    """
    # Estatísticas do Time da Casa
    hist_casa = df_hist[df_hist['Casa'] == casa]
    # Estatísticas do Time de Fora
    hist_fora = df_hist[df_hist['Fora'] == fora]
    
    media_gols = 1.5 # Padrão
    if not hist_casa.empty and not hist_fora.empty:
        media_gols = (hist_casa['GolsCasa'].mean() + hist_fora['GolsFora'].mean()) / 2

    conf = round(55 + (media_gols * 10), 1)
    if conf > 99: conf = 98.8

    return {
        "GOLS": "OVER 1.5" if media_gols > 1.3 else "UNDER 3.5",
        "CONF": f"{conf}%",
        "CARTOES": f"{int(media_gols + 2)}+",
        "CANTOS": f"{int(media_gols * 4)}+",
        "CHUTES": int(media_gols * 8),
        "DEFESAS": int(media_gols * 3),
        "TMETA": int(10 + media_gols)
    }

def processar():
    # 1. Garantir que temos os dados históricos
    criar_base_historica_se_nao_existir()
    
    # 2. Carregar o que acabamos de baixar
    df_hist = pd.read_csv(PATH_HISTORICO)
    
    # 3. Jogos de hoje (Simulando o scraper de jogos atuais)
    # Aqui o senhor pode editar os jogos do dia manualmente ou via scraper
    jogos_do_dia = [
        ["ING", "PREMIER", "Man City", "Arsenal"],
        ["ESP", "LA LIGA", "Real Madrid", "Barcelona"],
        ["ITA", "SERIE A", "Inter", "Milan"],
        ["ALE", "BUNDESLIGA", "Bayern Munich", "Bayer Leverkusen"],
        ["FRA", "LIGUE 1", "PSG", "Monaco"]
    ]
    
    db_final = []
    for p, l, c, f in jogos_do_dia:
        r = motor_ia_v96(c, f, df_hist)
        db_final.append([p, l, c, f, r['GOLS'], r['CONF'], r['CARTOES'], r['CANTOS'], r['CHUTES'], r['DEFESAS'], r['TMETA']])
    
    # 4. Salvar para o APP
    df_res = pd.DataFrame(db_final, columns=['PAIS','LIGA','CASA','FORA','GOLS','CONF','CARTOES','CANTOS','CHUTES','DEFESAS','TMETA'])
    df_res.to_csv(PATH_DATABASE, index=False)
    print("✅ Sucesso: Bilhete do dia gerado com base em 5 anos de história.")

if __name__ == "__main__":
    processar()
