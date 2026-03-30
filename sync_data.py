import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime

# ==============================================================================
# [PROTOCOLO JARVIS v62.3 - O "TANQUE DE GUERRA" - FONTE: PLACAR DE FUTEBOL]
# ==============================================================================

def calcular_confianca_jarvis(time_casa, df_hist):
    conf = 70.0
    if df_hist is not None:
        try:
            # Busca super flexível (3 primeiras letras)
            termo = str(time_casa)[:3]
            filtro = df_hist[df_hist['Casa'].str.contains(termo, case=False, na=False)]
            if not filtro.empty:
                taxa = (len(filtro[filtro['Resultado'] == 'H']) / len(filtro)) * 100
                conf = round(taxa + 5, 1)
        except: pass
    return f"{min(max(conf, 65.0), 98.4)}%"

def sync():
    print(f"🤖 JARVIS v62.3 | DATA DA OPERAÇÃO: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    
    path_hist = "data/historico_5_temporadas.csv"
    df_hist = pd.read_csv(path_hist) if os.path.exists(path_hist) else None

    # FONTE ESTÁVEL: Placar de Futebol (Focado em resultados, não em apostas)
    url = "https://www.placardefutebol.com.br/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

    try:
        response = requests.get(url, headers=headers, timeout=20)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # BUSCA POR TAGS BÁSICAS (Dificilmente mudam)
        jogos_container = soup.find_all('a', href=True)
        
        lista_final = []
        
        for link in jogos_container:
            # Filtramos apenas links que parecem ser de jogos (contêm "partida/")
            if '/partida/' in link['href']:
                try:
                    # Buscamos os nomes dos times dentro do link do jogo
                    times = link.find_all('span', class_='team-name')
                    if len(times) >= 2:
                        casa = times[0].get_text(strip=True)
                        fora = times[1].get_text(strip=True)
                        
                        # Liga (Geralmente está em um elemento anterior ou próximo)
                        liga = "FUTEBOL"
                        
                        # Status (Ao vivo ou Hora)
                        status = "HOJE"
                        status_el = link.find('span', class_='status-name')
                        if status_el: status = status_el.get_text(strip=True)

                        conf = calcular_confianca_jarvis(casa, df_hist)
                        
                        lista_final.append({
                            "STATUS": status.upper(),
                            "LIGA": liga,
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

        if lista_final:
            df = pd.DataFrame(lista_final).drop_duplicates(subset=['CASA', 'FORA'])
            if not os.path.exists('data'): os.makedirs('data')
            df.to_csv("data/database_diario.csv", index=False)
            print(f"✅ SUCESSO ABSOLUTO: {len(df)} JOGOS DE HOJE CAPTURADOS!")
        else:
            # SE NÃO ENCONTRAR, ELE LIMPA O ARQUIVO PARA NÃO MOSTRAR 2024
            print("⚠️ AVISO: Nada encontrado hoje. Limpando dados antigos para evitar erro.")
            df_vazio = pd.DataFrame(columns=["STATUS","LIGA","CASA","FORA","GOLS","CONF","CANTOS","CHUTES","DEFESAS","TMETA"])
            df_vazio.to_csv("data/database_diario.csv", index=False)

    except Exception as e:
        print(f"❌ ERRO CRÍTICO: {e}")

if __name__ == "__main__":
    sync()
