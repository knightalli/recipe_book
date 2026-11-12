import sys
from setuptools import setup, find_packages

NAME = "recipe_book_server"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion>=2.0.2",
    "swagger-ui-bundle>=0.0.2",
    "python_dateutil>=2.6.0"
]

setup(
    name=NAME,
    version=VERSION,
    description="Recipe Book API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Recipe Book API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['recipe_book_server=recipe_book_server.__main__:main']},
    long_description="""\
    REST API кулинарной книги: публикация и поиск рецептов.  ## Аутентификация Все операции требуют JWT в заголовке &#x60;Authorization: Bearer &lt;token&gt;&#x60;.  ## Модель ошибок - &#x60;401&#x60; — токен отсутствует или просрочен: сервер **не знает, кто вы**. - &#x60;403&#x60; — токен валиден, но прав не хватает: сервер **знает, кто вы, но нельзя**   (например, правка чужого рецепта). - &#x60;404&#x60; — ресурс с таким идентификатором не существует.  ## Про DTO Наружу отдаются только DTO (&#x60;components/schemas&#x60;). Внутренние поля сущности — статус модерации, служебные метки, вес в поисковой выдаче — в контракт не попадают. Поля, которые выставляет сервер (&#x60;id&#x60;, &#x60;author&#x60;, &#x60;createdAt&#x60;), помечены &#x60;readOnly&#x60; и в запросах не принимаются. 
    """
)

