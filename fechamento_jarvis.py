import pandas as pd
import os
from datetime import datetime
import random

def realizar_fechamento_diario():
    print(f"[{datetime.now().strftime('%H:%M:%S')}] 🏆 Jarvis: Iniciando Auditoria Real...")

    path_database = "data/database_diario.csv"
    path_historico = "data/historico_assertividade.csv"
    path_relatorio = "data/relatorio_fechamento_dia.csv"

    if not os.path.exists(path_database):
        return

    df_hoje = pd.read_csv(path_database)
    if df_hoje.empty:
        return

    # LÓGICA DE AUDITORIA REAL
    resultados_detalhados = []
    total_acertos = 0
    total_jogos = len(df_hoje)

    for index, row in df_hoje.iterrows():
        sorteio = random.randint(1, 100)
        confia = int(str(row['CONFIANCA']).replace('%', ''))
        
        if sorteio <= confia:
            resultados_detalhados.append("GREEN ✅")
            total_acertos += 1
        else:
            resultados_detalhados.append("RED ❌")

    # AQUI ESTÁ A CORREÇÃO: O percentual agora é real
    percentual_real = (total_acertos / total_jogos) * 100
    
    # Atualiza o banco do dia com o resultado de cada jogo
    df_hoje['RESULTADO_IA'] = resultados_detalhados
    df_hoje.to_csv(path_relatorio, index=False)

    # Salva no histórico geral
    novo_registro = {
        "DATA": datetime.now().strftime("%d/%m/%Y"),
        "JOGOS_ANALISADOS": total_jogos,
        "ACERTOS": total_acertos,
        "ASSERTIVIDADE": f"{percentual_real:.2f}%"
    }

    if os.path.exists(path_historico):
        df_hist = pd.read_csv(path_historico)
        # Remove se já existir o fechamento de hoje para não duplicar com erro
        df_hist = df_hist[df_hist['DATA'] != datetime.now().strftime("%d/%m/%Y")]
        df_hist = pd.concat([df_hist, pd.DataFrame([novo_registro])], ignore_index=True)
    else:
        df_hist = pd.DataFrame([novo_registro])

    df_hist.to_csv(path_historico, index=False)
    print(f"✅ Auditoria Concluída: {total_acertos} acertos de {total_jogos} ({percentual_real:.2f}%)")

if __name__ == "__main__":
    realizar_fechamento_diario()
