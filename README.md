# Students API

FastAPI-приложение для управления студентами и группами студентов.

## Возможности

- создание студентов;
- создание групп;
- получение студента по `id`;
- получение группы по `id`;
- получение списка студентов;
- получение списка групп;
- удаление студентов;
- удаление групп;
- добавление студента в группу;
- удаление студента из группы;
- получение всех студентов группы;
- перевод студента из одной группы в другую.

## Технологии

- Python
- FastAPI
- SQLModel
- PostgreSQL
- Docker Compose
- Uvicorn

## Структура проекта

```text
app/
├── api/            # API endpoints
├── db/             # подключение к базе данных
├── models/         # ORM-модели
├── repositories/   # работа с БД
├── schemas/        # схемы запросов и ответов
├── services/       # бизнес-логика
├── config.py
└── main.py
```

## Переменные окружения

Пример `.env`:

```env
POSTGRES_DB=students_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

В репозитории находится файл `.env.example`.

## Запуск

Запустить базу данных:

```bash
docker compose up -d
```

Создать и активировать виртуальное окружение:

```bash
python3 -m venv venv
source venv/bin/activate
```

Установить зависимости:

```bash
pip install -r requirements.txt
```

Запустить приложение:

```bash
uvicorn app.main:app --reload
```

Если приложение запускается на виртуальной машине:

```bash
uvicorn app.main:app --reload --host 0.0.0.0
```

## Swagger

```text
http://127.0.0.1:8000/docs
```

Для виртуальной машины:

```text
http://<IP_ВМ>:8000/docs
```

## Endpoints

### Students

| Метод | Endpoint | Описание |
|---|---|---|
| `POST` | `/students` | Создать студента |
| `GET` | `/students` | Получить список студентов |
| `GET` | `/students/{student_id}` | Получить студента по id |
| `DELETE` | `/students/{student_id}` | Удалить студента |
| `POST` | `/students/{student_id}/transfer` | Перевести студента в другую группу |

### Groups

| Метод | Endpoint | Описание |
|---|---|---|
| `POST` | `/groups` | Создать группу |
| `GET` | `/groups` | Получить список групп |
| `GET` | `/groups/{group_id}` | Получить группу по id |
| `DELETE` | `/groups/{group_id}` | Удалить группу |
| `POST` | `/groups/{group_id}/students/{student_id}` | Добавить студента в группу |
| `DELETE` | `/groups/{group_id}/students/{student_id}` | Удалить студента из группы |
| `GET` | `/groups/{group_id}/students` | Получить студентов группы |

## Остановка

```bash
docker compose down
```
