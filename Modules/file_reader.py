import fitz  # PyMuPDF para PDFs
import docx  # python-docx para arquivos DOCX

def read_pdf(file_path):
    try:
        text = ""
        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text()
        return text
    except Exception as e:
        print(f"Erro ao ler o PDF: {e}")
        return None

def read_docx(file_path):
    try:
        doc = docx.Document(file_path)
        text = '\n'.join([para.text for para in doc.paragraphs])
        return text
    except Exception as e:
        print(f"Erro ao ler o DOCX: {e}")
        return None

def read_txt(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        return text
    except Exception as e:
        print(f"Erro ao ler o arquivo TXT: {e}")
        return None

def read_file(file_path):
    if file_path.endswith('.pdf'):
        return read_pdf(file_path)
    elif file_path.endswith('.docx'):
        return read_docx(file_path)
    elif file_path.endswith('.txt'):
        return read_txt(file_path)
    else:
        print("Formato de arquivo não suportado")
        return None
