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
    # Referência: Adriano Monteiro Turma-13-c


# Requisito 11
def top_5_categories():
    news = find_news()

    categories = {}

    for new in news:
        for category in new['categories']:
            if category in categories:
                categories[category] += 1
            else:
                categories[category] = 1

    rank = list(categories.keys())

    rank.sort()

    return rank[:5]
