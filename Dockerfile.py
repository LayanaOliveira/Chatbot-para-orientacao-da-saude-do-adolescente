# Use uma imagem base de Python
FROM python:3.9-slim

# Define o diretório de trabalho
WORKDIR /app

# Copie os requisitos do seu projeto
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o código do bot
COPY . .

# Execute o bot
CMD ["python", "your_bot_script.py"]