import gradio as gr
from langchain_community.chat_models import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
import os
import re

# Carrega o modelo
llm = ChatOpenAI(
    openai_api_base="https://openrouter.ai/api/v1",
    openai_api_key=os.getenv("OPENROUTER_API_KEY", ""),
    model='deepseek/deepseek-r1-zero:free',
    temperature=0.3
)

def clean_response(text):
    """Função para limpar a resposta do modelo"""
    # Remove o padrão boxed{...}
    text = re.sub(r'boxed\{([^}]*)\}', r'\1', text)
    # Remove marcadores de código markdown se existirem
    text = re.sub(r'```markdown\n|\n```', '', text)
    # Remove espaços em branco extras
    text = text.strip()
    return text

def process_pdf(pdf_file, pergunta):
    try:
        # 1. Carrega o PDF
        loader = PyPDFLoader(pdf_file.name)
        documents = loader.load()
        
        # 2. Processa o texto
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        docs = text_splitter.split_documents(documents)
        
        # 3. Cria embeddings
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        
        # 4. Cria vetorstore
        vectorstore = FAISS.from_documents(docs, embeddings)
        
        # 5. Configura QA chain
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
            return_source_documents=True
        )
        
        # 6. Obtém e limpa a resposta
        resposta = qa_chain.invoke({"query": pergunta})
        resposta_limpa = clean_response(str(resposta['result']))
        
        return resposta_limpa
    
    except Exception as e:
        return f"❌ Erro ao processar: {str(e)}"

# Interface Gradio melhorada
with gr.Blocks(theme=gr.themes.Soft()) as app:
    gr.Markdown("""
    # 📄 ChatPDF Inteligente
    Faça perguntas sobre seus documentos PDF
    """)
    
    with gr.Row():
        with gr.Column():
            file_input = gr.File(
                label="Upload do PDF",
                type="filepath",
                file_types=[".pdf"]
            )
            question_input = gr.Textbox(
                label="Sua pergunta",
                placeholder="Ex: Qual é o resumo deste documento?"
            )
            submit_btn = gr.Button("Enviar", variant="primary")
        
        with gr.Column():
            output = gr.Textbox(
                label="Resposta",
                interactive=True,
                show_copy_button=True
            )
    
    # Exemplos
    gr.Examples(
        examples=[
            ["Qual é o objetivo deste documento?"],
            ["Resuma os pontos principais em tópicos"],
            ["Explique o conceito principal de forma simples"]
        ],
        inputs=[question_input]
    )

    submit_btn.click(
        fn=process_pdf,
        inputs=[file_input, question_input],
        outputs=output
    )

if __name__ == "__main__":
    app.launch()