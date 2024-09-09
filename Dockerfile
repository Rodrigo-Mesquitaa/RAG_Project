# Use a imagem oficial do Python 3.9 como base
FROM python:3.9-slim

# Instale dependências de sistema necessárias
RUN apt-get update && apt-get install -y \
    build-essential \
    poppler-utils \
    libgl1-mesa-glx \
    && apt-get clean

# Defina o diretório de trabalho
WORKDIR /app

# Copie o arquivo de requisitos
COPY requirements.txt .

# Instale as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código para o contêiner
COPY . .

# Exponha a porta para o Flask
EXPOSE 5000

# Defina a variável de ambiente para habilitar o modo de produção
ENV FLASK_ENV=production

# Execute o aplicativo Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
