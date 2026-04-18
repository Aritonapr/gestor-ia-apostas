import google.generativeai as genai

# Sua chave para teste
genai.configure(api_key="AIzaSyC83QqObkFM5QaJfVrivAmdqIp1ruWHo-4")

try:
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("Teste de conexão. Responda apenas: OK")
    print(f"Status da Chave: {response.text}")
except Exception as e:
    print(f"Erro na chave: {e}")
