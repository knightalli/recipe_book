import unittest

from flask import json

from recipe_book_server.models.difficulty import Difficulty  # noqa: E501
from recipe_book_server.models.error import Error  # noqa: E501
from recipe_book_server.models.recipe_create import RecipeCreate  # noqa: E501
from recipe_book_server.models.recipe_detail import RecipeDetail  # noqa: E501
from recipe_book_server.models.recipe_page import RecipePage  # noqa: E501
from recipe_book_server.models.recipe_update import RecipeUpdate  # noqa: E501
from recipe_book_server.test import BaseTestCase


class TestRecipesController(BaseTestCase):
    """RecipesController integration test stubs"""

    def test_create_recipe(self):
        """Test case for create_recipe

        Опубликовать новый рецепт
        """
        recipe_create = {"difficulty":"easy","cookingTimeMinutes":1,"description":"description","ingredients":[{"amount":250,"unit":"г","name":"Мука пшеничная"},{"amount":250,"unit":"г","name":"Мука пшеничная"}],"title":"title","steps":["steps","steps"],"tags":["tags","tags"]}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/v1/recipes',
            method='POST',
            headers=headers,
            data=json.dumps(recipe_create),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_recipe(self):
        """Test case for delete_recipe

        Удалить рецепт (только автор)
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/v1/recipes/{recipe_id}'.format(recipe_id='recipe_id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_recipe(self):
        """Test case for get_recipe

        Получить один рецепт целиком (с ингредиентами и шагами)
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/v1/recipes/{recipe_id}'.format(recipe_id='recipe_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_recipes(self):
        """Test case for list_recipes

        Список рецептов с фильтрами и пагинацией
        """
        query_string = [('tag', 'tag_example'),
                        ('difficulty', recipe_book_server.Difficulty()),
                        ('maxCookingTime', 56),
                        ('page', 1),
                        ('pageSize', 20)]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/v1/recipes',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_recipe(self):
        """Test case for update_recipe

        Частично обновить рецепт (только автор)
        """
        recipe_update = {"difficulty":"easy","cookingTimeMinutes":1,"description":"description","ingredients":[{"amount":250,"unit":"г","name":"Мука пшеничная"},{"amount":250,"unit":"г","name":"Мука пшеничная"}],"title":"title","steps":["steps","steps"],"tags":["tags","tags"]}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/v1/recipes/{recipe_id}'.format(recipe_id='recipe_id_example'),
            method='PATCH',
            headers=headers,
            data=json.dumps(recipe_update),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
