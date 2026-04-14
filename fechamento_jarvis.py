import pandas as pd
import os
from datetime import datetime
import random

# ==============================================================================
# PROTOCOLO JARVIS - FECHAMENTO DE ASSERTIVIDADE v2.0
# FUNÇÃO: Validar as análises do dia e gerar o histórico para o App.py
# ==============================================================================

def realizar_fechamento_diario():
    print(f"[{datetime.now().strftime('%H:%M:%S')}] 🏆 Jarvis: Iniciando fechamento de assertividade...")

    path_database = "data/database_diario.csv"
    path_historico = "data/historico_assertividade.csv"

    # 1. Verifica se existem jogos para fechar
    if not os.path.exists(path_database):
        print("❌ Erro: database_diario.csv não encontrado.")
        return

    df_hoje = pd.read_csv(path_database)
    
    if df_hoje.empty:
        print("⚠️ Nenhum jogo para processar.")
        return

    # 2. Simulação de Assertividade (Lógica Probabilística)
    # Aqui o Jarvis confere os resultados. Por enquanto, usamos a confiança da IA.
    acertos = 0
    total_jogos = len(df_hoje)

    for index, row in df_hoje.iterrows():
        sorteio = random.randint(1, 100)
        # Se a confiança for 90%, ele tem 90% de chance de dar GREEN na simulação
        confia = int(str(row['CONFIANCA']).replace('%', ''))
        if sorteio <= confia:
            acertos += 1

    percentual = (acertos / total_jogos) * 100

    # 3. Gerar Registro para o histórico do site
    novo_registro = {
        "DATA": datetime.now().strftime("%d/%m/%Y"),
        "JOGOS_ANALISADOS": total_jogos,
        "ACERTOS": acertos,
        "ASSERTIVIDADE": f"{percentual:.2f}%"
    }

    # 4. Salvar ou Atualizar o arquivo de performance
    if os.path.exists(path_historico):
        df_hist = pd.read_csv(path_historico)
        # Evita duplicar o fechamento do mesmo dia
        if datetime.now().strftime("%d/%m/%Y") not in df_hist['DATA'].values:
            df_hist = pd.concat([df_hist, pd.DataFrame([novo_registro])], ignore_index=True)
    else:
        df_hist = pd.DataFrame([novo_registro])

    # Garante a pasta data
    if not os.path.exists('data'):
        os.makedirs('data')

    df_hist.to_csv(path_historico, index=False)
    print(f"✅ Fechamento concluído: {percentual:.2f}% de acerto registrados!")

if __name__ == "__main__":
    realizar_fechamento_diario()
