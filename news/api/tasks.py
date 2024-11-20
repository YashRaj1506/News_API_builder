from celery import shared_task
from api.webscraper import scraper

from api.webscraper.scraper import scrape_news_indiatoday_func


@shared_task(bind=True)
def test_not_func(self):
    # operations
    for i in range(10):
        print(i)
    return "Done"

@shared_task(bind=True)
def test_func(self):
    scrape_news_indiatoday_func('https://www.indiatoday.in/rss/1206550', 'sports')
    return "Done"