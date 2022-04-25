import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category
)
from tech_news.analyzer.ratings import (top_5_news, top_5_categories)


def populate_db():
    amount = input("Digite quantas notícias serão buscadas: ")
    get_tech_news(int(amount))


def get_title():
    title = input("Digite o título: ")
    search_by_title(title)


def get_date():
    data = input("Digite a data no formato aaaa-mm-dd: ")
    search_by_date(data)


def get_source():
    source = input("Digite a fonte: ")
    search_by_source(source)


def get_category():
    category = input("Digite a Categoria: ")
    search_by_category(category)


def get_news():
    top_5_news()


def get_categories():
    top_5_categories()


# Requisito 12
def analyzer_menu():
    options = input(
        "Selecione uma das opções a seguir: \n"
        "0 - Popular o banco com notícias: \n"
        "1 - Buscar notícias por título: \n"
        "2 - Buscar notícias por data: \n"
        "3 - Buscar notícias por fonte: \n"
        "4 - Buscar notícias por categoria: \n"
        "5 - Listar top 5 notícias: \n"
        "6 - Listar top 5 categorias: \n"
        "7 - Sair."
    )
    menu = {
        "0": populate_db,
        "1": get_title,
        "2": get_date,
        "3": get_source,
        "4": get_category,
        "5": get_news,
        "6": get_categories
    }
    if options in menu:
        menu[options]()
    elif options == "7":
        print("Encerrando script")
    else:
        sys.stderr.write("Opção inválida\n")
