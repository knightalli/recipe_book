# Recipe Book API

**Зачем этот API:** backend кулинарной книги — публикация рецептов, их поиск по фильтрам и правка/удаление своих рецептов их авторами.

## Промт

Напиши api.yaml OpenAPI для кулинарной книги (сущность Recipe: title, description, difficulty, cookingTimeMinutes, tags, ingredients, steps). Нужно 5 эндпоинтов под разные глаголы: GET-список с фильтрами
и пагинацией, GET-одного, POST, PATCH, DELETE. Добавь аутентификацию . У каждого эндпоинта - summary, параметры, успешный код и ошибки: 401, 403, 404. Для повторяющихся объектов или осмысленно важных сделай компоненты и используй через $ref. Затем сгенерируй каркас: openapi-generator-cli generate -i api.yaml -g python-flask -o service. Подними сервис и убедись, что эндпоинты отвечают. В README напиши зачем API, таблицу эндпоинтов, команду кодогенерации, как запустить и как проверяли.

## Структура

```
api.yaml    — спецификация OpenAPI 3.0.3 (источник истины)
service/    — каркас сервиса, сгенерированный openapi-generator-cli (python-flask)
```

## Спека: `api.yaml`

5 эндпоинтов, все — под разные HTTP-глаголы:

| Метод | Путь | Назначение |
|-------|------|------------|
| GET    | `/recipes` | список с фильтрами (тег, сложность, время) и пагинацией |
| POST   | `/recipes` | публикация рецепта |
| GET    | `/recipes/{recipeId}` | один рецепт целиком |
| PATCH  | `/recipes/{recipeId}` | частичное обновление (только автор) |
| DELETE | `/recipes/{recipeId}` | удаление (только автор) |

Что заложено по требованиям:

- **Коды ошибок с причиной:** `401` — нет/просрочен Bearer-токен (сервер не знает,
  кто ты), `403` — токен валиден, но ты не автор (знаю — но нельзя), `404` —
  рецепта нет, `400` — валидация тела/параметров.
- **DTO в `components/schemas`:** внутреннее наружу не едет — серверные поля
  (`id`, `author`, `createdAt`) помечены `readOnly` и в `RecipeCreate`/
  `RecipeUpdate` не принимаются; для списка отдаётся `RecipeSummary` без
  ингредиентов и шагов; статусы модерации и прочие служебные поля сущности в
  контракт вообще не включены.

## Как делали

Сделано **с агентом** — Devin (модель SWE-2) в Devin Desktop, весь процесс в
одной сессии:

1. **Спека** — промтом было само задание (OpenAPI 3.0, разные глаголы,
   401/403/404 с причинами, DTO без внутренних полей). Агент написал `api.yaml`
   целиком; руками ничего не правилось — только выбрана тема (папка уже
   называлась `recipe_book`).
2. **Кодоген** — команда:
   ```bash
   java -jar openapi-generator-cli.jar generate \
     -i api.yaml -g python-flask -o service \
     --additional-properties=packageName=recipe_book_server
   ```
   (`openapi-generator-cli.jar` 7.14.0 скачан с Maven Central; можно заменить
   на `npx @openapitools/openapi-generator-cli` или docker-образ).
3. **Проверка** — `validate` дал «No validation issues detected»; сгенерированный
   код не правился руками вообще, только поднят для проверки.

## Запуск сгенерированного сервиса

```bash
cd service
python -m venv .venv
.venv/Scripts/pip install -r requirements.txt   # Linux: .venv/bin/pip
.venv/Scripts/python -m recipe_book_server      # слушает :8080
```

Проверено вживую:

```
GET    /api/v1/recipes?pageSize=5          -> 200 (заглушка "do some magic!")
GET    /api/v1/recipes/{uuid}              -> 200 
DELETE /api/v1/recipes/{uuid}              -> 200
POST   /api/v1/recipes {}                  -> 400 (валидация по спеке работает, после авторизации заглушка "do some magic!")
```

Swagger UI (connexion): `http://localhost:8080/api/v1/ui/`.

Бизнес-логику нужно дописывать в `service/recipe_book_server/controllers/recipes_controller.py` —
генератор оставляет заглушки `do some magic!`.
