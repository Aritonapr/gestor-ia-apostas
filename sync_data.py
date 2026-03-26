import pandas as pd
import os
import random
from datetime import datetime

if not os.path.exists('data'): os.makedirs('data')

def motor_ia(casa, fora):
    # Lógica de pesos por time (DNA)
    times_fortes = ["Man City", "Real Madrid", "Arsenal", "Flamengo", "Liverpool", "Bayern Munchen", "PSG", "Inter Milan"]
    c_f = 8.5 if casa in times_fortes else 5.0
    f_f = 8.5 if fora in times_fortes else 5.0
    
    prob = round(45 + (c_f - f_f) * 5 + random.randint(-5, 5), 1)
    return {
        "GOLS": f"+{random.choice([1, 2])}.5",
        "CONF": f"{min(prob + 20, 98)}%",
        "CARTOES": random.randint(3, 7),
        "CANTOS": random.randint(8, 14),
        "CHUTES": random.randint(10, 22),
        "DEFESAS": random.randint(2, 8),
        "TMETA": random.randint(12, 20)
    }

def processar():
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
    for p, l, c, f in jogos:
        r = motor_ia(c, f)
        db.append([p, l, c, f, r['GOLS'], r['CONF'], r['CARTOES'], r['CANTOS'], r['CHUTES'], r['DEFESAS'], r['TMETA']])
    
    pd.DataFrame(db, columns=['PAIS','LIGA','CASA','FORA','GOLS','CONF','CARTOES','CANTOS','CHUTES','DEFESAS','TMETA']).to_csv('data/database_diario.csv', index=False)

if __name__ == "__main__": processar()
