import fitz  # PyMuPDF

def read_pdf(file_path):
    """
    Lê o conteúdo de um PDF e retorna o texto extraído.
    :param file_path: Caminho para o arquivo PDF.
    :return: Texto extraído do PDF.
    """
    try:
        text = ""
        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text()
        return text
    except Exception as e:
        print(f"Erro ao ler o PDF: {e}")
        return None
