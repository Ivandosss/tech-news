from tech_news.database import find_news


# Requisito 10
def top_5_news():
    news = find_news()

    news.sort(
        key=lambda new: new['shares_count'] + new['comments_count']
        )

    news.reverse()

    top_5_news = []

    for new in news[:5]:
        top_5_news.append((new['title'], new['url']))

    return top_5_news


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
