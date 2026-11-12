import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from recipe_book_server.models.difficulty import Difficulty  # noqa: E501
from recipe_book_server.models.error import Error  # noqa: E501
from recipe_book_server.models.recipe_create import RecipeCreate  # noqa: E501
from recipe_book_server.models.recipe_detail import RecipeDetail  # noqa: E501
from recipe_book_server.models.recipe_page import RecipePage  # noqa: E501
from recipe_book_server.models.recipe_update import RecipeUpdate  # noqa: E501
from recipe_book_server import util


def create_recipe(body):  # noqa: E501
    """Опубликовать новый рецепт

     # noqa: E501

    :param recipe_create: 
    :type recipe_create: dict | bytes

    :rtype: Union[RecipeDetail, Tuple[RecipeDetail, int], Tuple[RecipeDetail, int, Dict[str, str]]
    """
    recipe_create = body
    if connexion.request.is_json:
        recipe_create = RecipeCreate.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_recipe(recipe_id):  # noqa: E501
    """Удалить рецепт (только автор)

     # noqa: E501

    :param recipe_id: Идентификатор рецепта
    :type recipe_id: str
    :type recipe_id: str

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_recipe(recipe_id):  # noqa: E501
    """Получить один рецепт целиком (с ингредиентами и шагами)

     # noqa: E501

    :param recipe_id: Идентификатор рецепта
    :type recipe_id: str
    :type recipe_id: str

    :rtype: Union[RecipeDetail, Tuple[RecipeDetail, int], Tuple[RecipeDetail, int, Dict[str, str]]
    """
    return 'do some magic!'


def list_recipes(tag=None, difficulty=None, max_cooking_time=None, page=None, page_size=None):  # noqa: E501
    """Список рецептов с фильтрами и пагинацией

     # noqa: E501

    :param tag: Фильтр по тегу (например, &#x60;vegan&#x60;, &#x60;dessert&#x60;)
    :type tag: str
    :param difficulty: Фильтр по сложности
    :type difficulty: dict | bytes
    :param max_cooking_time: Максимальное время приготовления, минут
    :type max_cooking_time: int
    :param page: Номер страницы (с 1)
    :type page: int
    :param page_size: Размер страницы (макс. 50)
    :type page_size: int

    :rtype: Union[RecipePage, Tuple[RecipePage, int], Tuple[RecipePage, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        difficulty =  Difficulty.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_recipe(recipe_id, body):  # noqa: E501
    """Частично обновить рецепт (только автор)

     # noqa: E501

    :param recipe_id: Идентификатор рецепта
    :type recipe_id: str
    :type recipe_id: str
    :param recipe_update: Только те поля, которые нужно изменить
    :type recipe_update: dict | bytes

    :rtype: Union[RecipeDetail, Tuple[RecipeDetail, int], Tuple[RecipeDetail, int, Dict[str, str]]
    """
    recipe_update = body
    if connexion.request.is_json:
        recipe_update = RecipeUpdate.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
