import pandas as pd
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def calcular_metricas_jarvis(time_casa, df_hist):
    confianca = 75.0
    if df_hist is not None:
        filtro = df_hist[df_hist['Casa'].str.contains(str(time_casa)[:5], case=False, na=False)]
        if not filtro.empty:
            taxa = (len(filtro[filtro['Resultado'] == 'H']) / len(filtro)) * 100
            confianca = round(taxa + 15, 1)
    return f"{min(confianca, 98.4)}%"

def sync():
    print("🤖 JARVIS v60.0 | Capturando Horários e Jogos...")
    path_hist = "data/historico_5_temporadas.csv"
    df_hist = pd.read_csv(path_hist) if os.path.exists(path_hist) else None

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        driver.get("https://br.betano.com/sport/futebol/jogos-de-hoje/")
        time.sleep(15)
        
        eventos = driver.find_elements(By.CSS_SELECTOR, "[data-testid='event-card']")
        lista_jogos = []

        for evento in eventos:
            try:
                texto_completo = evento.text.split('\n')
                # A Betano coloca o horário ou 'AO VIVO' nas primeiras linhas do card
                status_hora = texto_completo[0] 
                
                # Identifica times (lógica robusta de pulo de mercados)
                casa = ""
                fora = ""
                for i in range(1, len(texto_completo)):
                    if " - " in texto_completo[i]:
                        partes = texto_completo[i].split(" - ")
                        casa = partes[0].strip()
                        fora = partes[1].strip()
                        break
                
                if not casa: # Fallback caso os nomes estejam em linhas separadas
                    casa = texto_completo[1]
                    fora = texto_completo[2]

                if casa and fora:
                    conf = calcular_metricas_jarvis(casa, df_hist)
                    lista_jogos.append({
                        "STATUS": status_hora,
                        "LIGA": "BETANO",
                        "CASA": casa,
                        "FORA": fora,
                        "GOLS": "OVER 1.5",
                        "CONF": conf,
                        "CANTOS": "9.5+",
                        "CHUTES": "10+",
                        "DEFESAS": "7+",
                        "TMETA": "15+"
                    })
            except: continue
        
        if lista_jogos:
            df_final = pd.DataFrame(lista_jogos)
            if not os.path.exists('data'): os.makedirs('data')
            df_final.to_csv("data/database_diario.csv", index=False)
            print(f"✅ SUCESSO: {len(df_final)} jogos com horários capturados.")
            
    except Exception as e: print(f"❌ ERRO: {e}")
    finally: driver.quit()

if __name__ == "__main__":
    sync()
