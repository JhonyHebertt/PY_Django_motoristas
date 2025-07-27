# imagem base oficial python
FROM python:3.11-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Copia e instala dependências
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copia o projeto
COPY . /app/

# Dá permissão de execução ao entrypoint
RUN chmod +x /app/entrypoint.sh

# Coleta arquivos estáticos
# RUN python manage.py collectstatic --noinput

ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["gunicorn", "motorista_project.wsgi:application", "--bind", "0.0.0.0:8000"]
