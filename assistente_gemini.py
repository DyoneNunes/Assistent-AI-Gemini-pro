import google.generativeai as genai

# Substitua com sua chave
genai.configure(api_key="COLOQUE-SUA-CHAVE-AQUI")

# Criar o modelo (gemini-pro funciona com texto)
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")

# Loop de conversa
print("Assistente Gemini iniciado (digite 'sair' para encerrar)\n")

while True:
    prompt = input("Você: ")
    if prompt.lower() in ['sair', 'exit', 'quit']:
        break

    try:
        response = model.generate_content(prompt)
        print("Gemini:", response.text)
    except Exception as e:
        print("Erro:", e)
