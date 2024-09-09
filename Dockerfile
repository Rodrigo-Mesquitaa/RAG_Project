# Use uma imagem base oficial do Python 3.9
FROM python:3.9-slim

# Definir diretório de trabalho no container
WORKDIR /app

# Copiar o arquivo requirements.txt para instalar as dependências
COPY requirements.txt .

# Instalar as dependências especificadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante da aplicação para o container
COPY . .

# Comando para iniciar a aplicação
CMD ["python", "main.py"]
