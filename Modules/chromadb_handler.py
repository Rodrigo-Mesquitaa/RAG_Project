from chromadb import ChromaDB

def store_data(vectors):
    """
    Armazena os vetores gerados no ChromaDB.
    :param vectors: Vetores a serem armazenados.
    """
    try:
        db = ChromaDB()
        db.store(vectors)
        print("Dados armazenados com sucesso.")
    except Exception as e:
        print(f"Erro ao armazenar dados no ChromaDB: {e}")

def query_data(query):
    """
    Realiza uma consulta no ChromaDB.
    :param query: Termo de busca.
    :return: Resultados da consulta.
    """
    try:
        db = ChromaDB()
        return db.query(query)
    except Exception as e:
        print(f"Erro ao consultar dados no ChromaDB: {e}")
        return None
