# 📄 ChatPDF Inteligente

Uma aplicação de leitura inteligente de PDFs com IA, criada com LangChain, Gradio e modelos de linguagem de código aberto. Com o **ChatPDF Inteligente**, você pode **fazer perguntas sobre qualquer documento PDF** e receber respostas claras, rápidas e baseadas no conteúdo.

---

## 🚀 Funcionalidades

- ✅ Upload de arquivos PDF
- 💬 Perguntas em linguagem natural
- 🤖 Respostas baseadas em IA (LLM via OpenRouter)
- 🧠 Vetorização com embeddings da Hugging Face
- 🔍 Busca semântica com FAISS
- 🌐 Interface amigável com Gradio

---

## 🛠️ Tecnologias utilizadas

- [LangChain](https://www.langchain.com/)
- [Gradio](https://www.gradio.app/)
- [FAISS (Facebook AI Similarity Search)](https://github.com/facebookresearch/faiss)
- [Hugging Face Embeddings](https://huggingface.co/)
- [OpenRouter](https://openrouter.ai/)
- Python 3.10+

---

## 📦 Como usar

1. Clone o repositório (ou acesse via Hugging Face Spaces):
   ```bash
   git clone https://github.com/seuusuario/chatpdf-inteligente.git
   cd chatpdf-inteligente
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure a chave da API do OpenRouter (coloque no `.env` ou defina no terminal):
   ```bash
   export OPENROUTER_API_KEY=sua-chave-aqui
   ```

4. Rode o app:
   ```bash
   python app.py
   ```

---

## 🧪 Exemplo de uso

1. Faça upload de um PDF.
2. Digite uma pergunta como:
   - "Qual é o objetivo deste documento?"
   - "Resuma os principais pontos em tópicos."
   - "Explique o conceito de forma simples."
3. Clique em **Enviar** e aguarde a resposta gerada pela IA.

---

## 💡 Sobre o projeto

Este projeto foi desenvolvido como parte de um experimento educacional com LangChain e IA generativa. Ideal para estudantes, profissionais e curiosos que desejam explorar documentos de forma interativa e inteligente.

---

## 📚 Bootcamp

📌 Este projeto foi desenvolvido durante o **Bootcamp de LLM (Modelos de Linguagem de Grande Escala)** da [SoulCode Academy](https://soulcode.com), com apoio do Grupo Petrópolis.

