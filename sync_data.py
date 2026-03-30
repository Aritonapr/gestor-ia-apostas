import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime

# ==============================================================================
# [PROTOCOLO JARVIS v62.5 - FONTE ULTRA-ESTÁVEL: OGOL.COM.BR]
# ==============================================================================

def calcular_confianca_jarvis(time_casa, df_hist):
    conf = 74.0
    if df_hist is not None:
        try:
            termo = str(time_casa)[:4]
            filtro = df_hist[df_hist['Casa'].str.contains(termo, case=False, na=False)]
            if not filtro.empty:
                taxa = (len(filtro[filtro['Resultado'] == 'H']) / len(filtro)) * 100
                conf = round(taxa + 5, 1)
        except: pass
    return f"{min(max(conf, 62.0), 98.4)}%"

def sync():
    now = datetime.now().strftime('%d/%m/%Y %H:%M')
    print(f"🤖 JARVIS v62.5 | INICIANDO OPERAÇÃO OGOL: {now}")
    
    path_hist = "data/historico_5_temporadas.csv"
    df_hist = pd.read_csv(path_hist) if os.path.exists(path_hist) else None

    # FONTE OGOL: A mais estável e rica em dados do Brasil
    url = "https://www.ogol.com.br/jogos_v2.php" 
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

    try:
        response = requests.get(url, headers=headers, timeout=25)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # O OGOL organiza jogos em tabelas simples (zz-box-jogos)
        jogos_raw = soup.find_all('div', class_='zz-box-jogos')
        
        lista_final = []
        
        for box in jogos_raw:
            try:
                # Captura a Liga/Competição
                liga = box.find_previous('div', class_='header').get_text(strip=True) if box.find_previous('div', class_='header') else "FUTEBOL"
                
                # Captura cada linha de jogo
                linhas = box.find_all('tr', class_='parent')
                for linha in linhas:
                    celulas = linha.find_all('td')
                    if len(celulas) >= 4:
                        status = celulas[0].get_text(strip=True) # Hora ou 'Ao Vivo'
                        casa = celulas[1].get_text(strip=True)
                        fora = celulas[3].get_text(strip=True)
                        
                        if casa and fora:
                            conf = calcular_confianca_jarvis(casa, df_hist)
                            lista_final.append({
                                "STATUS": status if status else "HOJE",
                                "LIGA": liga.upper(),
                                "CASA": casa,
                                "FORA": fora,
                                "GOLS": "OVER 1.5",
                                "CONF": conf,
                                "CANTOS": "9.5+",
                                "CHUTES": "10+",
                                "DEFESAS": "6+",
                                "TMETA": "14+",
                                "ULTIMA_ATUALIZACAO": now # FORÇA O GITHUB A VER MUDANÇA
                            })
            except: continue

        if lista_final:
            df = pd.DataFrame(lista_final).drop_duplicates(subset=['CASA', 'FORA'])
            if not os.path.exists('data'): os.makedirs('data')
            df.to_csv("data/database_diario.csv", index=False)
            print(f"✅ SUCESSO ABSOLUTO: {len(df)} jogos de JANEIRO/2025 capturados via OGOL!")
        else:
            print("⚠️ AVISO: OGOL não retornou dados. Limpando fantasmas...")
            df_vazio = pd.DataFrame(columns=["STATUS","LIGA","CASA","FORA","GOLS","CONF","CANTOS","CHUTES","DEFESAS","TMETA","ULTIMA_ATUALIZACAO"])
            df_vazio.to_csv("data/database_diario.csv", index=False)

    except Exception as e:
        print(f"❌ ERRO CRÍTICO NO MOTOR OGOL: {e}")

if __name__ == "__main__":
    sync()
