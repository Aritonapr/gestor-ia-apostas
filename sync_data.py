import pandas as pd
import requests
import os

def sync():
    print("Iniciando Bot 3 - Sincronizador Automático...")
    # URL do seu banco de dados no GitHub
    url = "https://raw.githubusercontent.com/Aritonapr/gestor-ia-apostas/main/data/database_diario.csv"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            if not os.path.exists('data'): os.makedirs('data')
            with open('data/database_diario.csv', 'wb') as f:
                f.write(response.content)
            print("✅ Dados atualizados com sucesso!")
        else:
            print(f"❌ Erro ao acessar arquivo: Status {response.status_code}")
    except Exception as e:
        print(f"❌ Erro na sincronização: {e}")

if __name__ == "__main__":
    sync()
