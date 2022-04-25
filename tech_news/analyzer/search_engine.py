from tech_news.database import db
import datetime


# Requisito 6
def search_by_title(title):
    news = []
    for new in db.news.find({"title": {"$regex": title, "$options": "i"}}):
        insert_title = new["title"], new["url"]
        news.append(insert_title)
    return news


# Requisito 7
def search_by_date(date):
    date_true = ''
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        date_true = True
    except ValueError:
        date_true = False

    if date_true:
        news = []
        for new in db.news.find(
            {"timestamp": {"$regex": date, "$options": "i"}}
        ):
            insert_title = new["title"], new["url"]
            news.append(insert_title)
        return news
    else:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    news = []
    for new in db.news.find(
            {"sources": {"$elemMatch": {"$regex": source, "$options": "i"}}}
            ):
        insert_title = new["title"], new["url"]
        news.append(insert_title)
    return news


# Requisito 9
def search_by_category(category):
    news = []
    for new in db.news.find(
        {"categories": {"$elemMatch": {"$regex": category, "$options": "i"}}}
            ):
        insert_title = new["title"], new["url"]
        news.append(insert_title)
    return news
