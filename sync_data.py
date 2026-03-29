import pandas as pd
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def calcular_ia_jarvis(time_casa, df_hist):
    conf = 72.0
    if df_hist is not None:
        filtro = df_hist[df_hist['Casa'].str.contains(str(time_casa)[:5], case=False, na=False)]
        if not filtro.empty:
            taxa = (len(f[f['Resultado']=='H']) / len(f)) * 100 if len(f) > 0 else 72.0
            conf = round(taxa + 10, 1)
    return f"{min(conf, 98.4)}%"

def sync():
    print("🚀 JARVIS v60.0 | Iniciando Limpeza e Busca Real-Time...")
    
    path_hist = "data/historico_5_temporadas.csv"
    df_hist = pd.read_csv(path_hist) if os.path.exists(path_hist) else None

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        # Acessa a agenda da Betano para HOJE
        driver.get("https://br.betano.com/sport/futebol/jogos-de-hoje/")
        time.sleep(20) # Tempo extra para o site carregar totalmente
        
        # Procura todos os blocos de jogos
        cards = driver.find_elements(By.XPATH, "//div[contains(@class, 'events-list__grid__event')]")
        
        novos_jogos = []
        print(f"🔎 Analisando {len(cards)} possíveis confrontos...")

        for card in cards:
            try:
                texto = card.text.split('\n')
                # Na Betano, o horário ou status fica no topo
                status = texto[0]
                
                # Procura o separador " - " para identificar os times
                casa, fora = "", ""
                for linha in texto:
                    if " - " in linha:
                        partes = linha.split(" - ")
                        casa, fora = partes[0].strip(), partes[1].strip()
                        break
                
                if casa and fora:
                    conf = calcular_ia_jarvis(casa, df_hist)
                    novos_jogos.append({
                        "STATUS": status,
                        "LIGA": "BETANO",
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
        
        if novos_jogos:
            df_final = pd.DataFrame(novos_jogos)
            if not os.path.exists('data'): os.makedirs('data')
            df_final.to_csv("data/database_diario.csv", index=False)
            print(f"✅ JARVIS ATUALIZADO: {len(df_final)} jogos reais encontrados.")
        else:
            print("⚠️ ERRO: O robô não encontrou jogos novos. O arquivo não foi alterado.")
            
    except Exception as e: print(f"❌ FALHA NO SCANNER: {e}")
    finally: driver.quit()

if __name__ == "__main__":
    sync()
