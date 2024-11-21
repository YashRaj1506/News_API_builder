from celery import shared_task
from api.webscraper import scraper

from api.webscraper.scraper import scrape_news_indiatoday_func, scrape_news_nytimes_func

from api.webscraper.helper_functions import create_superuser, flush_database


@shared_task(bind=True)
def test_not_func(self):
    # operations
    for i in range(10):
        print(i)
    return "Done"

@shared_task(bind=True)
def test_func(self):

    flush_database()

    create_superuser('yash', 'yash@gmail.com', 'yash')

    scrape_news_indiatoday_func('https://www.indiatoday.in/rss/1206550', 'sports')
    scrape_news_indiatoday_func('https://www.indiatoday.in/rss/1206513', 'economy')
    scrape_news_indiatoday_func('https://www.indiatoday.in/rss/1206577', 'world')
    scrape_news_indiatoday_func('https://www.indiatoday.in/rss/1206504', 'society&arts')

    scrape_news_nytimes_func('https://rss.nytimes.com/services/xml/rss/nyt/Politics.xml', 'politics')
    scrape_news_nytimes_func('https://rss.nytimes.com/services/xml/rss/nyt/Sports.xml', 'sports')
    scrape_news_nytimes_func('https://rss.nytimes.com/services/xml/rss/nyt/Science.xml', 'science')
    scrape_news_nytimes_func('https://rss.nytimes.com/services/xml/rss/nyt/Climate.xml', 'environment')
    scrape_news_nytimes_func('https://rss.nytimes.com/services/xml/rss/nyt/Space.xml', 'space')
    return "Done"