import pandas as pd
import os
import random
from datetime import datetime

if not os.path.exists('data'): os.makedirs('data')

# DNA DOS TIMES (Base para os 7 cálculos)
# atk: chutes/gols | def: defesas/tiros de meta | aggressive: cartões | pressure: cantos
dna_ia = {
    "Man City": {"atk": 9.8, "def": 8.5, "agg": 2, "pres": 10},
    "Arsenal": {"atk": 9.2, "def": 9.0, "agg": 3, "pres": 9},
    "Real Madrid": {"atk": 9.6, "def": 8.8, "agg": 4, "pres": 8},
    "Flamengo": {"atk": 8.8, "def": 8.2, "agg": 5, "pres": 9},
    "Luton": {"atk": 4.0, "def": 3.0, "agg": 7, "pres": 4},
}

def motor_preditivo(casa, fora):
    c = dna_ia.get(casa, {"atk": 5, "def": 5, "agg": 5, "pres": 5})
    f = dna_ia.get(fora, {"atk": 5, "def": 5, "agg": 5, "pres": 5})
    
    # 1. Probabilidade Vencedor
    prob_c = round(min(98, 45 + (c['atk'] - f['def']) * 5), 1)
    
    # 2. Gols (Total e Tempos)
    total_gols = round((c['atk'] + f['atk']) / 4 + random.uniform(0.5, 1.5), 1)
    gols_ht = "SIM" if total_gols > 2.5 else "NÃO"
    
    # 3. Cartões (Baseado em Agressividade)
    total_cartoes = int((c['agg'] + f['agg']) / 2 + random.randint(1, 3))
    
    # 4. Escanteios (Baseado em Pressão)
    cantos = int((c['pres'] + f['pres']) + random.randint(0, 4))
    
    # 5. Tiros de Meta (Quanto menos posse/ataque, mais tiro de meta o time dá)
    tm_casa = int(15 - c['atk'] + random.randint(0, 5))
    tm_fora = int(15 - f['atk'] + random.randint(0, 5))
    
    # 6. Chutes no Gol
    chutes = int((c['atk'] + f['atk']) + random.randint(2, 6))
    
    # 7. Defesas do Goleiro
    defesas = int((c['atk'] + f['atk']) / 3 + random.randint(1, 4))
    
    return {
        "PROB_CASA": f"{prob_c}%",
        "GOLS_FT": f"+{int(total_gols)}.5",
        "GOLS_AMBOS_T": gols_ht,
        "CARTÕES": total_cartoes,
        "CANTOS": cantos,
        "TIROS_META": tm_casa + tm_fora,
        "CHUTES": chutes,
        "DEFESAS": defesas
    }

def processar_ia():
    jogos = [
        ["INGLATERRA", "PREMIER", "Man City", "Luton"],
        ["INGLATERRA", "PREMIER", "Arsenal", "Aston Villa"],
        ["ESPANHA", "LA LIGA", "Real Madrid", "Athletic Bilbao"],
        ["BRASIL", "SÉRIE A", "Flamengo", "Palmeiras"],
        ["BRASIL", "SÉRIE A", "Vasco", "Grêmio"],
        ["BRASIL", "SÉRIE A", "Corinthians", "Atlético-MG"],
        ["BRASIL", "SÉRIE A", "São Paulo", "Fortaleza"],
        ["ITÁLIA", "SERIE A", "Inter Milan", "Cagliari"],
        ["ALEMANHA", "BUNDESLIGA", "Bayern Munchen", "FC Koln"],
        ["FRANÇA", "LIGUE 1", "PSG", "Lorient"]
    ]
    
    db = []
    for p, l, casa, fora in jogos:
        res = motor_preditivo(casa, fora)
        db.append([p, l, casa, fora, res['GOLS_FT'], res['PROB_CASA'], res['CARTÕES'], res['CANTOS'], res['CHUTES'], res['DEFESAS'], res['TIROS_META']])
    
    df = pd.DataFrame(db, columns=['PAÍS','GRUPO','TIME_CASA','TIME_FORA','MERCADO','CONFIDANÇA','CARTOES','CANTOS','CHUTES','DEFESAS','TMETA'])
    df.to_csv('data/database_diario.csv', index=False)

if __name__ == "__main__": processar_ia()
