# Usa imagem base leve com Python
FROM python:3.12-alpine

# Variáveis de ambiente úteis
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Instala dependências do sistema (para compilar libs como pandas, psycopg2, etc.)
RUN apk add --no-cache \
    build-base \
    libffi-dev \
    musl-dev \
    gcc \
    python3-dev \
    py3-pip \
    postgresql-dev \
    bash \
    curl

# Define diretório de trabalho no container
WORKDIR /app

# Copia os arquivos da pipeline para o container
COPY . .

# Instala as dependências Python
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# Comando que roda o script diretamente
ENTRYPOINT ["sh", "entrypoint.sh"]
