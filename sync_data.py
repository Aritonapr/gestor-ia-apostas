import pandas as pd
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def calcular_metricas_jarvis(time_casa, time_fora, df_hist):
    confianca = 50.0
    if df_hist is not None:
        # Busca inteligente (pega os primeiros 5 caracteres do nome)
        filtro = df_hist[df_hist['Casa'].str.contains(str(time_casa)[:5], case=False, na=False)]
        if not filtro.empty:
            vitorias = len(filtro[filtro['Resultado'] == 'H'])
            taxa = (vitorias / len(filtro)) * 100
            confianca = round(taxa + 15, 1)
    return f"{min(confianca, 98.4)}%"

def sync():
    print("🤖 JARVIS v60.0 | Iniciando Varredura Multi-Seletores...")
    
    path_hist = "data/historico_5_temporadas.csv"
    df_hist = pd.read_csv(path_hist) if os.path.exists(path_hist) else None

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        driver.get("https://br.betano.com/sport/futebol/jogos-de-hoje/")
        time.sleep(15) # Aumentamos o tempo para garantir o carregamento
        
        # Tenta encontrar os jogos por diferentes caminhos (Seletores de Elite)
        jogos_encontrados = driver.find_elements(By.CSS_SELECTOR, "[data-testid='event-card']")
        
        # Se falhar, tenta o seletor secundário
        if not jogos_encontrados:
            jogos_encontrados = driver.find_elements(By.CLASS_NAME, "events-list__grid__event")

        lista_jogos = []
        print(f"🔎 Detectados {len(jogos_encontrados)} blocos de eventos.")

        for evento in jogos_encontrados:
            try:
                # Captura o texto completo do bloco e tenta separar os times
                dados = evento.text.split('\n')
                # Geralmente o nome dos times aparece em sequência no texto do card
                # Vamos buscar padrões de nomes (Ex: Time A vs Time B ou Time A - Time B)
                casa = ""
                fora = ""
                
                # Lógica de extração robusta
                for i in range(len(dados)):
                    if " / " in dados[i] or ":" in dados[i]: # Pula horários ou mercados
                        continue
                    if i < len(dados) - 1:
                        casa = dados[i].strip()
                        fora = dados[i+1].strip()
                        if len(casa) > 3 and len(fora) > 3: # Validação básica de nome
                            break
                
                if casa and fora:
                    conf = calcular_metricas_jarvis(casa, fora, df_hist)
                    lista_jogos.append({
                        "PAIS": "LIVE 📡",
                        "LIGA": "BETANO REAL-TIME",
                        "CASA": casa,
                        "FORA": fora,
                        "GOLS": "OVER 1.5",
                        "CONF": conf,
                        "CARTOES": "3+",
                        "CANTOS": "9.5+",
                        "CHUTES": "10+",
                        "DEFESAS": "7+",
                        "TMETA": "15+"
                    })
            except:
                continue
        
        if lista_jogos:
            df_final = pd.DataFrame(lista_jogos)
            if not os.path.exists('data'): os.makedirs('data')
            df_final.to_csv("data/database_diario.csv", index=False)
            print(f"✅ SUCESSO: {len(df_final)} jogos processados pela IA.")
        else:
            print("⚠️ AVISO: O site carregou mas os nomes dos times não foram extraídos.")
            
    except Exception as e:
        print(f"❌ ERRO CRÍTICO: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    sync()
