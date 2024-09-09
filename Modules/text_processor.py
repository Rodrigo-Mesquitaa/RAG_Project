from langchain import TextProcessor, ModelTrainer

def process_text(text):
    """
    Processa o texto extraído do PDF usando LangChain.
    :param text: Texto extraído do PDF.
    :return: Texto processado.
    """
    try:
        processor = TextProcessor(text)
        processed_text = processor.process()  # Processa o texto
        return processed_text
    except Exception as e:
        print(f"Erro ao processar o texto: {e}")
        return None

def train_model(processed_text):
    """
    Treina um modelo de IA com o texto processado.
    :param processed_text: Texto processado.
    """
    try:
        model = ModelTrainer(model="llama3")  # Usa o Llama3
        model.train(processed_text)  # Treina o modelo com o texto processado
    except Exception as e:
        print(f"Erro ao treinar o modelo: {e}")
