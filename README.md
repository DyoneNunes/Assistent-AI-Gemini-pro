# 🤖 Assistente Gemini CLI (Cyberpunk Edition)

Este é um assistente de IA pessoal, desenvolvido com a **API do Google Gemini** e interface em **linha de comando (terminal)** — no melhor estilo hacker cyberpunk.  
Foi criado para rodar de forma leve, independente do navegador, diretamente em sua máquina Linux.

---

## 🧠 Funcionalidades

- Chat com o modelo **Gemini Pro** da Google
- Totalmente executável via terminal (`.exe` ou binário Linux)
- Interface estilo prompt, sem distrações
- Suporte a entrada de texto ilimitada
- Resposta formatada no estilo chat IA
- Código isolado com ambiente virtual (seguro)
- **Backup offline** do binário para rodar sem dependências Python

---

## 🧑‍💻 Desenvolvido por

- **Dyone Andrade** ([@dyone](https://github.com/DyoneNunes)) — Desenvolvedor Linux + AI
- Com suporte técnico e código gerado por [ChatGPT](https://chat.openai.com)

---

## 🚀 Como usar

### 1. Clone ou crie a pasta do projeto

```bash
mkdir ~/AssistenteGemini
cd ~/AssistenteGemini
```

### 2. Crie um ambiente virtual Python

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install google-generativeai pyinstaller
```

### 4. Crie o script `assistente.py`

```python
import google.generativeai as genai

genai.configure(api_key="SUA_CHAVE_AQUI")

model = genai.GenerativeModel(model_name="models/gemini-pro")

print("🧠 Gemini CLI iniciado — digite 'sair' para encerrar\n")

while True:
    prompt = input("Você > ")
    if prompt.lower() in ["sair", "exit", "quit"]:
        break

    try:
        response = model.generate_content(prompt)
        print("\nGemini >", response.text, "\n")
    except Exception as e:
        print("[Erro]:", e)
```

> Substitua `"SUA_CHAVE_AQUI"` pela sua chave da API do [Google AI Studio](https://aistudio.google.com/app/apikey).

---

## 🔧 Gerando o binário (executável)

```bash
pyinstaller --onefile assistente.py
```

O executável estará disponível em:
```
./dist/assistente
```

### (Opcional) Tornar comando global:

```bash
sudo mv dist/assistente /usr/local/bin/gemini
```

Agora basta digitar:

```bash
gemini
```

---

## 💬 Exemplo de uso

```bash
🧠 Gemini CLI iniciado — digite 'sair' para encerrar

Você > Quem foi Ada Lovelace?

Gemini > Ada Lovelace foi uma matemática britânica, considerada a primeira programadora da história...
```

---

## 🎯 Próximas ideias (em desenvolvimento)

- [ ] Adicionar histórico local (`~/.gemini-history`)
- [ ] Modo escuro com tema ASCII cyberpunk
- [ ] Leitura em voz alta com `espeak`
- [ ] Interface GUI opcional (Tkinter)

---

## 📜 Licença

Este projeto é open-source e livre para uso pessoal, educacional e experimental.

---
