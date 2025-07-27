# Motorista API

API REST para gerenciamento de motoristas, construída com Django, Django REST Framework, Celery, Redis e Docker.

## Funcionalidades

- CRUD de motoristas
- Autenticação JWT
- Envio assíncrono de e-mails com Celery e Redis
- Documentação automática da API (Swagger)
- Dockerização completa

## Tecnologias

- Python 3.11
- Django
- Django REST Framework
- Celery
- Redis
- Docker & Docker Compose
- drf-yasg (Swagger)

## Como rodar o projeto

### Pré-requisitos

- [Docker](https://www.docker.com/) e [Docker Compose](https://docs.docker.com/compose/)

### Passos

1. **Clone o repositório:**
   ```sh
   git clone https://github.com/seu-usuario/motorista.git
   cd motorista
   ```

2. **Configure as variáveis de ambiente:**
   - Copie o arquivo `.env.example` para `.env` e ajuste conforme necessário.

3. **Suba os containers:**
   ```sh
   docker-compose up --build
   ```

4. **Acesse a aplicação:**
   - API: [http://localhost:8000/](http://localhost:8000/)
   - Swagger: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)

## Endpoints principais

- `POST /auth/login/` — Login JWT
- `GET /motoristas/` — Lista motoristas
- `POST /motoristas/` — Cria motorista
- `GET /motoristas/{id}/` — Detalhe do motorista
- `PUT /motoristas/{id}/` — Atualiza motorista
- `DELETE /motoristas/{id}/` — Remove motorista

## Usuário administrador

O superusuário é criado automaticamente ao subir o projeto, usando as variáveis do arquivo `.env.example`:

```
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@admin.com
DJANGO_SUPERUSER_PASSWORD=admin123
```

## Estrutura do projeto

```
.
├── docker-compose.yml
├── .env.example
├── requirements.txt
├── motorista_project/
│   ├── settings.py
│   └── urls.py
├── usuarios/
│   └── (App de autenticação)
├── motoristas/
│   ├── models.py
│   ├── views.py
│   ├── tasks.py
│   ├── signals.py
│   └── urls.py
```

## Licença

MIT

---

> Projeto desenvolvido para estudos e demonstração de boas práticas com Django e Docker.