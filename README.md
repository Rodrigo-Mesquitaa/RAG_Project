# RAG_Project
Projeto RAG. Ele integra leitura de PDFs, processamento de texto com LangChain, treinamento de IA e armazenamento de vetores no ChromaDB. 
Cada componente foi cuidadosamente estruturado em módulos separados para facilitar a manutenção e organização.


## Revisão Geral

Dockerfile e docker-compose.yml:

Estrutura do Docker e do Docker Compose está correta, conectando o serviço principal da aplicação com o serviço do ChromaDB.
As dependências estão listadas corretamente no requirements.txt.
No docker-compose.yml, a exposição correta das portas (5000 para a aplicação e 8000 para o ChromaDB) está garantida.
Módulos Python:

Os módulos estão organizados corretamente, cada um com uma responsabilidade específica:
pdf_reader.py: Lê e extrai texto do PDF usando PyMuPDF.
text_processor.py: Processa o texto usando LangChain e treina o modelo.
chromadb_handler.py: Interage com o ChromaDB para armazenamento e consulta de vetores.