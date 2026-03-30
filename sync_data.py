import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime

# ==============================================================================
# [PROTOCOLO JARVIS v63.2 - BRUTE FORCE REAL-TIME | PONTE 2025 -> 2026]
# ==============================================================================

def calcular_confianca_jarvis(time_casa, df_hist):
    conf = 74.5
    if df_hist is not None:
        try:
            termo = str(time_casa)[:4]
            filtro = df_hist[df_hist['Casa'].str.contains(termo, case=False, na=False)]
            if not filtro.empty:
                taxa = (len(filtro[filtro['Resultado'] == 'H']) / len(filtro)) * 100
                conf = round(taxa + 4, 1)
        except: pass
    return f"{min(max(conf, 65.0), 98.4)}%"

def get_jogos_reserva():
    """FONTE DE RESERVA: Placar de Futebol (Sempre tem dados)"""
    lista = []
    try:
        url = "https://www.placardefutebol.com.br/"
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(res.text, 'html.parser')
        cards = soup.find_all('a', href=True)
        for card in cards:
            if '/partida/' in card['href']:
                times = card.find_all('span', class_='team-name')
                if len(times) >= 2:
                    status_el = card.find('span', class_='status-name')
                    lista.append({
                        "CASA": times[0].get_text(strip=True),
                        "FORA": times[1].get_text(strip=True),
                        "STATUS": status_el.get_text(strip=True).upper() if status_el else "HOJE",
                        "LIGA": "FUTEBOL REAL-TIME"
                    })
    except: pass
    return lista

def sync():
    now_real = datetime.now()
    data_ponte = "29/03/2026 " + now_real.strftime("%H:%M")
    print(f"🤖 JARVIS v63.2 | SINCRONIA ATIVA: {data_ponte}")
    
    path_hist = "data/historico_5_temporadas.csv"
    df_hist = pd.read_csv(path_hist) if os.path.exists(path_hist) else None

    # TENTA FONTE 1 (API GLOBO)
    lista_final = []
    try:
        url_ge = "https://api.globoesporte.globo.com/tabela/jogos-do-dia"
        res = requests.get(url_ge, timeout=15).json()
        for j in res:
            lista_final.append({
                "STATUS": "AO VIVO" if j['status'] == 'andamento' else str(j.get('hora_real', 'HOJE')).upper(),
                "LIGA": j['campeonato']['nome'].upper(),
                "CASA": j['equipes']['mandante']['nome_popular'],
                "FORA": j['equipes']['visitante']['nome_popular'],
                "GOLS": "OVER 1.5", "CANTOS": "9.5+", "CHUTES": "10+", "DEFESAS": "6+", "TMETA": "14+",
                "ULTIMA_SYNC": data_ponte 
            })
    except: pass

    # SE ESTIVER VAZIO, TENTA FONTE 2 (BRUTE FORCE)
    if not lista_final:
        print("⚠️ API Globo Vazia. Acionando Brute Force...")
        reserva = get_jogos_reserva()
        for r in reserva:
            lista_final.append({
                "STATUS": r['STATUS'], "LIGA": r['LIGA'], "CASA": r['CASA'], "FORA": r['FORA'],
                "GOLS": "OVER 1.5", "CANTOS": "9.5+", "CHUTES": "10+", "DEFESAS": "6+", "TMETA": "14+",
                "ULTIMA_SYNC": data_ponte
            })

    # CALCULA CONFIANÇA E SALVA
    if lista_final:
        for item in lista_final:
            item['CONF'] = calcular_confianca_jarvis(item['CASA'], df_hist)
        
        df = pd.DataFrame(lista_final).drop_duplicates(subset=['CASA', 'FORA'])
        if not os.path.exists('data'): os.makedirs('data')
        df.to_csv("data/database_diario.csv", index=False)
        print(f"✅ SUCESSO: {len(df)} jogos de 2025 sincronizados para 2026!")
    else:
        print("❌ Nenhuma fonte encontrou jogos.")

if __name__ == "__main__":
    sync()
