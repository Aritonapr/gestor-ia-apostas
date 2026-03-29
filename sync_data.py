import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime

# ==============================================================================
# [PROTOCOLO JARVIS v62.2 - MOTOR DE CAPTURA ULTRA-ROBUSTO]
# ==============================================================================

def calcular_confianca_jarvis(time_casa, df_hist):
    conf = 75.0
    if df_hist is not None:
        termo = str(time_casa)[:4]
        try:
            filtro = df_hist[df_hist['Casa'].str.contains(termo, case=False, na=False)]
            if not filtro.empty:
                taxa = (len(filtro[filtro['Resultado'] == 'H']) / len(filtro)) * 100
                conf = round(taxa + 5, 1)
        except: pass
    return f"{min(conf, 98.4)}%"

def sync():
    print(f"🤖 JARVIS v62.2 | FORÇANDO ATUALIZAÇÃO: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    
    path_hist = "data/historico_5_temporadas.csv"
    df_hist = pd.read_csv(path_hist) if os.path.exists(path_hist) else None

    url = "https://www.placardefutebol.com.br/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

    try:
        response = requests.get(url, headers=headers, timeout=20)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # BUSCA AMPLA POR JOGOS (Layout 2025)
        jogos_raw = soup.find_all(['div', 'a'], class_=['match-card', 'match-link'])
        
        lista_final = []
        
        for jogo in jogos_raw:
            try:
                # Extração de Times
                teams = jogo.find_all('span', class_='team-name')
                if len(teams) < 2: continue
                casa = teams[0].get_text(strip=True)
                fora = teams[1].get_text(strip=True)
                
                # Extração de Status/Hora
                status = "HOJE"
                status_box = jogo.find('span', class_='status-name')
                if status_box: status = status_box.get_text(strip=True)

                # Extração de Liga
                liga = "FUTEBOL PROFISSIONAL"
                liga_box = jogo.find_previous('h3', class_='league-name')
                if liga_box: liga = liga_box.get_text(strip=True)

                conf = calcular_confianca_jarvis(casa, df_hist)
                
                lista_final.append({
                    "STATUS": status.upper(),
                    "LIGA": liga.upper(),
                    "CASA": casa,
                    "FORA": fora,
                    "GOLS": "OVER 1.5",
                    "CONF": conf,
                    "CANTOS": "9.5+",
                    "CHUTES": "10+",
                    "DEFESAS": "6+",
                    "TMETA": "14+"
                })
            except: continue

        # --- A GRANDE MUDANÇA: LIMPEZA DE FANTASMAS ---
        if lista_final:
            df = pd.DataFrame(lista_final)
            if not os.path.exists('data'): os.makedirs('data')
            df.to_csv("data/database_diario.csv", index=False)
            print(f"✅ SUCESSO: {len(df)} jogos de JANEIRO/2025 capturados!")
        else:
            # Se não encontrar nada, ele cria um arquivo vazio para não mostrar dados de 2024
            print("⚠️ AVISO: Nenhum jogo encontrado. Limpando arquivo antigo...")
            df_vazio = pd.DataFrame(columns=["STATUS","LIGA","CASA","FORA","GOLS","CONF","CANTOS","CHUTES","DEFESAS","TMETA"])
            df_vazio.to_csv("data/database_diario.csv", index=False)

    except Exception as e:
        print(f"❌ ERRO CRÍTICO: {e}")

if __name__ == "__main__":
    sync()
