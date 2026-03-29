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
        # Busca por aproximação no histórico
        filtro = df_hist[df_hist['Casa'].str.contains(str(time_casa)[:5], case=False, na=False)]
        if not filtro.empty:
            taxa = (len(filtro[filtro['Resultado'] == 'H']) / len(filtro)) * 100
            conf = round(taxa + 10, 1)
    return f"{min(conf, 98.4)}%"

def sync():
    print("🚀 JARVIS v60.0 | Iniciando Varredura de Alta Precisão...")
    
    path_hist = "data/historico_5_temporadas.csv"
    df_hist = pd.read_csv(path_hist) if os.path.exists(path_hist) else None

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        driver.get("https://br.betano.com/sport/futebol/jogos-de-hoje/")
        time.sleep(25) # Espera o site carregar totalmente
        
        # Tenta capturar os jogos por múltiplos seletores (Betano atualiza sempre)
        eventos = driver.find_elements(By.CSS_SELECTOR, "[class*='tw-flex tw-flex-col tw-w-full']")
        
        if not eventos:
            eventos = driver.find_elements(By.XPATH, "//div[contains(@class, 'events-list__grid__event')]")

        lista_jogos = []
        print(f"🔎 Analisando {len(eventos)} blocos detectados...")

        for ev in eventos:
            try:
                texto = ev.text.split('\n')
                if len(texto) < 3: continue
                
                # Identifica Status (Ao Vivo ou Horário) e Times
                status = texto[0]
                casa, fora = "", ""
                
                for linha in texto:
                    if " - " in linha and len(linha) > 5:
                        partes = linha.split(" - ")
                        casa, fora = partes[0].strip(), partes[1].strip()
                        break
                
                if casa and fora:
                    conf = calcular_ia_jarvis(casa, df_hist)
                    lista_jogos.append({
                        "STATUS": status,
                        "LIGA": "BETANO PRO",
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
        
        if lista_jogos:
            df_final = pd.DataFrame(lista_jogos)
            if not os.path.exists('data'): os.makedirs('data')
            df_final.to_csv("data/database_diario.csv", index=False)
            print(f"✅ JARVIS ATUALIZADO: {len(df_final)} jogos de HOJE salvos.")
        else:
            print("⚠️ ERRO: O robô não conseguiu ler os nomes dos times.")
            
    except Exception as e:
        print(f"❌ FALHA CRÍTICA: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    sync()
