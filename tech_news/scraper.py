import time
import requests
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(url, timeout=3)
        response.raise_for_status()
    except (requests.HTTPError, requests.Timeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    scraped = selector.css("main .tec--card__thumb__link::attr(href)").getall()
    return scraped


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    button_selector = selector.css("a.tec--btn::attr(href)").get()
    return button_selector


def scrap(selector, context):
    return context.css(selector).get()


def scrap_all(selector, context):
    return context.css(selector).getall()


# Requisito 4
def scrape_noticia(html_content):
    context = Selector(html_content)

    news = {}

    news["url"] = scrap('head link[rel="canonical"]::attr(href)', context)
    news["title"] = scrap(".tec--article__header__title::text", context)
    news["timestamp"] = scrap("#js-article-date::attr(datetime)", context)

    writer = scrap(".z--font-bold *::text", context)
    news["writer"] = writer.strip() if writer else None

    raw_shares = scrap(".tec--toolbar__item::text", context)
    if (raw_shares):
        news["shares_count"] = int(raw_shares.split(" ")[1])
    else:
        news["shares_count"] = 0

    raw_comments_count = scrap("#js-comments-btn::attr(data-count)", context)
    if (raw_comments_count):
        news["comments_count"] = int(raw_comments_count)
    else:
        news["comments_count"] = 0

    summary = scrap_all(
        "div.tec--article__body > p:nth-child(1) *::text",
        context
    )
    news["summary"] = "".join(summary)

    raw_sources = scrap_all(".z--mb-16 div a::text", context)
    news["sources"] = [source.strip() for source in raw_sources]

    raw_categories = scrap_all("#js-categories a::text", context)
    news["categories"] = [category.strip() for category in raw_categories]

    return news


def get_all_news(endpoints):
    all_news = []

    for endpoint in endpoints:
        all_news.append(scrape_noticia(fetch(endpoint)))

    return all_news


# Requisito 5
def get_tech_news(amount):
    page = 1
    endpoints = []

    while(len(endpoints) < amount):
        complete_endpoint = "https://www.tecmundo.com.br/novidades"
        quary = f"?page={page}"

        endpoint = complete_endpoint if page < 2 else complete_endpoint + quary

        for url in scrape_novidades(fetch(endpoint)):
            if (len(endpoints) < amount):
                endpoints.append(url)

        page += 1

    all_news = get_all_news(endpoints)

    create_news(all_news)

    return all_news
