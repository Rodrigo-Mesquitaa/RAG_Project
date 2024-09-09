from modules.pdf_reader import read_pdf
from modules.text_processor import process_text, train_model
from modules.chromadb_handler import store_data

def main():
    # Leitura do PDF
    pdf_text = read_pdf("Politica_de_Privacidade.pdf")
    if pdf_text is None:
        print("Erro ao ler o PDF.")
        return
    
    # Processamento do texto extraído do PDF
    processed_text = process_text(pdf_text)
    if processed_text is None:
        print("Erro ao processar o texto.")
        return
    
    # Treinamento do modelo de IA com o texto processado
    train_model(processed_text)
    
    # Armazenamento dos vetores resultantes no ChromaDB
    vectors = processed_text  # Aqui você pode converter o texto processado em vetores
    store_data(vectors)

if __name__ == "__main__":
    main()
