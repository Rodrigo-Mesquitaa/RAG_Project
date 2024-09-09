from modules.file_reader import read_file
from modules.text_processor import process_text, train_model
from modules.chromadb_handler import store_data

def main():
    # Leitura do arquivo (suporta PDF, DOCX, TXT)
    file_text = read_file("Politica_de_Privacidade.pdf")  # Troque o arquivo aqui
    if file_text is None:
        print("Erro ao ler o arquivo.")
        return
    
    # Processamento do texto extraído do arquivo
    processed_text = process_text(file_text)
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
