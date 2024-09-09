# RAG_Project
Projeto RAG. Ele integra leitura de PDFs, processamento de texto com LangChain, treinamento de IA e armazenamento de vetores no ChromaDB. 
Cada componente foi cuidadosamente estruturado em módulos separados para facilitar a manutenção e organização.


## Projeto de Recuperação Aumentada de Conhecimento (RAG)
### Objetivo do Projeto
Este projeto tem como objetivo criar um sistema de Recuperação Aumentada de Conhecimento (RAG) utilizando tecnologias modernas,
como LangChain, ChromaDB e Ollama, para processar, treinar e armazenar dados extraídos de um PDF. O sistema usa Docker e Docker Compose para configuração
e orquestração do ambiente, garantindo uma fácil replicação e execução do projeto.

- A aplicação lê um PDF da política de privacidade, processa o conteúdo utilizando processamento de linguagem natural, 
treina um modelo de IA e armazena os vetores de conhecimento no ChromaDB, permitindo recuperação e consultas futuras.

### Tecnologias Utilizadas

- LangChain: Framework para processamento de linguagem natural (NLP) e gerenciamento de modelos de IA.
- ChromaDB: Banco de dados especializado em armazenamento e recuperação de vetores.
- Ollama: Ferramenta para gerenciamento de grandes modelos de linguagem, neste caso, usamos Llama3.
- PyMuPDF: Biblioteca Python para leitura e extração de texto de arquivos PDF.
- Docker: Ferramenta de containerização usada para criar e gerenciar contêineres.
- Docker Compose: Orquestração de múltiplos serviços (aplicação e ChromaDB) com um único comando.


### Funcionalidades

- Leitura de PDF: O sistema lê um arquivo PDF da política de privacidade utilizando PyMuPDF e extrai o conteúdo em texto.
- Processamento de Texto: Com a ajuda do LangChain, o texto extraído é processado e preparado para ser usado pelo modelo de IA.
- Treinamento do Modelo de IA: Usamos o Llama3 para treinar um modelo com o texto processado.
- Armazenamento no ChromaDB: Os vetores resultantes do processamento de texto são armazenados no ChromaDB, permitindo recuperação e consulta futura.
- Consulta e Recuperação: A aplicação é capaz de consultar os dados armazenados no ChromaDB para fins de recuperação de conhecimento.

## Estrutura do Projeto

RAG_Project/
- ├── Dockerfile                   # Definição do ambiente de desenvolvimento
- ├── docker-compose.yml            # Orquestração dos serviços (app e ChromaDB)
- ├── requirements.txt              # Dependências do projeto
- ├── main.py                       # Arquivo principal que integra a aplicação
- ├── modules/                      # Módulos do projeto
- ├── pdf_reader.py             # Leitura e extração do texto do PDF
- │   ├── text_processor.py         # Processamento de texto e treinamento do modelo
- │   └── chromadb_handler.py       # Armazenamento e consulta no ChromaDB
- └── Politica_de_Privacidade.pdf   # Arquivo PDF de exemplo para extração
- ├── api/
- │   └── app.py                    # Nova API REST para consultar ChromaDB
- ├── templates/
- │   └── index.html                 # Interface Web
- └── static/
    - └── style.css                  # Estilos para a Interface Web*


## Configuração do Ambiente

### Pré-requisitos
Certifique-se de ter as seguintes ferramentas instaladas no seu ambiente:

.Docker: Instalar Docker
.Docker Compose: Instalar Docker Compose
.Passo a Passo para Executar o Projeto

## Explicação do Dockerfile
### Imagem Base:
A imagem base usada é python:3.9-slim, que é uma versão leve do Python 3.9.

### Instalação de Dependências do Sistema:
São instaladas dependências de sistema para garantir o suporte à manipulação de PDFs e renderização gráfica no caso de uso do PyMuPDF.
- poppler-utils: Essencial para manipulação de PDFs.
- libgl1-mesa-glx: Usado para renderização gráfica em certos casos necessários pelo PyMuPDF.

### Diretório de Trabalho:
O diretório de trabalho é definido como /app, onde o código da aplicação será armazenado.

### Instalação de Dependências Python:
As bibliotecas Python necessárias são instaladas usando o arquivo requirements.txt 
(deve incluir Flask, LangChain, PyMuPDF, python-docx, etc.).

### Cópia de Código:
O restante do código da aplicação é copiado para o contêiner.

#### Porta Expota:
A porta 5000 é exposta, já que o Flask será executado nessa porta.

#### Variável de Ambiente:
A variável FLASK_ENV=production é configurada para rodar a aplicação em modo de produção.

#### Comando de Execução:
O comando CMD define a execução do Flask na porta 5000 com o host 0.0.0.0 para que possa ser acessado externamente.

### Clonar o Repositório

Clone o repositório do projeto para a sua máquina local:

-*git clone https://github.com/seu-usuario/RAG_Project.git
cd RAG_Project*

### Instalar Dependências

-*pip install -r requirements.txt*

### Executar com Docker Compose

-*docker-compose up --build*

Isso irá:

- Baixar as imagens Docker necessárias.
- Construir a aplicação dentro do container.
- Iniciar os serviços da aplicação e ChromaDB.

### Acessar a Aplicação

Após a execução, a aplicação estará rodando na porta 5000, e o ChromaDB estará na porta 8000

Se tudo estiver correto, a aplicação realizará os seguintes passos:

- Leitura do PDF Politica_de_Privacidade.pdf.
- Processamento do texto extraído usando LangChain.
- Treinamento do modelo de IA Llama3 com o texto processado.
- Armazenamento dos vetores gerados no ChromaDB.

## Estrutura dos Arquivos e Módulos

### 1. Dockerfile
Define a configuração do ambiente de desenvolvimento, como instalação do Python e dependências.

### 2. docker-compose.yml
Orquestra a aplicação e o serviço do ChromaDB para serem executados em contêineres separados,
permitindo uma arquitetura modular e fácil de replicar.

### 3. requirements.txt
Lista todas as dependências Python necessárias para o funcionamento da aplicação:

- langchain
- chromadb
- PyMuPDF
- requests

### 4. main.py
Arquivo principal que faz a integração de todos os módulos. Ele lê o PDF, processa o texto,
treina o modelo de IA e armazena os vetores no ChromaDB.

### 5. Módulos Python
- pdf_reader.py: Lê e extrai texto de um PDF utilizando a biblioteca PyMuPDF.
- text_processor.py: Processa o texto extraído e treina um modelo de IA usando o LangChain.
- chromadb_handler.py: Armazena e consulta vetores no ChromaDB.

## Erros Comuns e Soluções

### 1 - Problemas de Conexão com o ChromaDB:
Verifique se o contêiner do ChromaDB está rodando corretamente com o comando:

-*docker ps*

Certifique-se de que a porta 8000 está disponível no host.

### 2 - Falhas na Leitura do PDF:
- Certifique-se de que o arquivo Politica_de_Privacidade.pdf está no diretório correto.
- Verifique se o formato do PDF está intacto e legível.

### 3 - Erros ao Processar o Texto ou Treinar o Modelo:
. Verifique se todas as dependências estão instaladas corretamente.
. Confirme se a versão do LangChain e do Llama3 são compatíveis com a versão utilizada no projeto.


# Conclusão
API REST: Criado uma API com Flask que permite realizar consultas ao ChromaDB por meio de chamadas HTTP.
Suporte para Mais Formatos: Agora o projeto suporta arquivos PDF, DOCX e TXT.
Interface Web: Implementamos uma interface simples em HTML e CSS que permite aos usuários consultar o ChromaDB e visualizar os resultados.

Essas mudanças tornam a aplicação mais flexível e interativa, permitindo uma melhor usabilidade tanto pela API quanto pela interface web.
