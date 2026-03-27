import pandas as pd
import os
import random
from datetime import datetime

if not os.path.exists('data'): os.makedirs('data')

def motor_ia(casa, fora):
    times_fortes = ["Man City", "Real Madrid", "Arsenal", "Flamengo", "Liverpool", "Bayern Munchen", "PSG", "Inter Milan", "Bayer Leverkusen", "Barcelona"]
    c_f = 9.0 if casa in times_fortes else 5.5
    f_f = 9.0 if fora in times_fortes else 5.5
    prob = round(45 + (c_f - f_f) * 5 + random.randint(-3, 3), 1)
    return {
        "GOLS": f"+{random.choice([1, 2])}.5",
        "CONF": f"{min(prob + 25, 99)}%",
        "CARTOES": random.randint(3, 8),
        "CANTOS": random.randint(7, 15),
        "CHUTES": random.randint(12, 25),
        "DEFESAS": random.randint(1, 7),
        "TMETA": random.randint(10, 18)
    }

def processar():
    # LISTA EXPANDIDA PARA 20 JOGOS
    jogos = [
        ["ING", "PREMIER", "Man City", "Luton"], ["ING", "PREMIER", "Arsenal", "Aston Villa"],
        ["ESP", "LA LIGA", "Real Madrid", "Bilbao"], ["BRA", "SÉRIE A", "Flamengo", "Palmeiras"],
        ["ITA", "SERIE A", "Inter Milan", "Cagliari"], ["ALE", "BUNDESLIGA", "Bayern", "FC Koln"],
        ["FRA", "LIGUE 1", "PSG", "Lyon"], ["POR", "LIGA", "Benfica", "Porto"],
        ["ING", "PREMIER", "Liverpool", "Palace"], ["ESP", "LA LIGA", "Barcelona", "PSG"],
        ["BRA", "SÉRIE A", "Vasco", "Grêmio"], ["BRA", "SÉRIE A", "Corinthians", "Atlético-MG"],
        ["BRA", "SÉRIE A", "São Paulo", "Fortaleza"], ["ALE", "BUNDESLIGA", "Leverkusen", "Bremen"],
        ["ITA", "SERIE A", "Juventus", "Torino"], ["ING", "PREMIER", "Chelsea", "Everton"],
        ["ING", "PREMIER", "Newcastle", "Tottenham"], ["ESP", "LA LIGA", "Atletico", "Girona"],
        ["FRA", "LIGUE 1", "Monaco", "Lille"], ["HOL", "EREDIVISIE", "Ajax", "PSV"]
    ]
    db = []
    for p, l, c, f in jogos:
        r = motor_ia(c, f)
        db.append([p, l, c, f, r['GOLS'], r['CONF'], r['CARTOES'], r['CANTOS'], r['CHUTES'], r['DEFESAS'], r['TMETA']])
    
    pd.DataFrame(db, columns=['PAIS','LIGA','CASA','FORA','GOLS','CONF','CARTOES','CANTOS','CHUTES','DEFESAS','TMETA']).to_csv('data/database_diario.csv', index=False)
    print("✅ Sucesso: 20 jogos processados.")

if __name__ == "__main__": processar()
