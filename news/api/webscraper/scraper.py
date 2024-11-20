import feedparser
import requests
from bs4 import BeautifulSoup
import os
import google.generativeai as genai
from dotenv import load_dotenv
import time

from celery import shared_task
from django.conf import settings

from api.models import News_data

HEADERS = ({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Referer': 'https://www.amazon.in/',
    'DNT': '1'
})


def scrape_news_indiatoday_func(url, category):
    rss_url = url
    response = requests.get(rss_url)

    if response.status_code == 200:
        response.encoding = 'utf-8'
        feed = feedparser.parse(response.text)

        if feed.bozo:
            print("Failed to parse RSS feed:", feed.bozo_exception)
        else:
            # Extract data
            feed_data = []
            # print(feed.entries)
            for entry in feed.entries:
                item = {
                    'title': entry.title,
                    'link': entry.link,
                    'summary': entry.summary,
                    'published': entry.published
                }
                feed_data.append(item)  # Feed_data is the list collection of all the news present

            content_block_collected = []
            content_block_collected_topass = [] #Content to pass

            for i in range(len(feed_data)):  # Loop runs as many times as number of news available from feed_data
                current_dict = feed_data[i]  # Iterates one news link at a time (we get a dictionary)
                current_link = current_dict['link']

                content_block_collected_local = ""

                webpage = requests.get(current_link, headers=HEADERS)
                soup = BeautifulSoup(webpage.content, "lxml")

                # print("Heading :" + current_dict['title'])

                title_topass = current_dict['title'] #this stores the title for us
                print(title_topass)

                content_block_collected_local = content_block_collected_local + "Heading :" + current_dict['title']
                # print(content_block_collected_local)
                content_block_collected_local = content_block_collected_local + "\n\n"

                content_block_collected_local_topass = ""

                content = soup.find_all("div", attrs={
                    "class": "jsx-ace90f4eca22afc7 Story_description__fq_4S description paywall"})

                # content_block_collected = ""

                for p in content:
                    # print(p.text)
                    p_tags = p.find_all("p")

                    for p_tag in p_tags:

                        content_block_collected_local_topass = content_block_collected_local_topass + p_tag.text
                        content_block_collected_local_topass = content_block_collected_local_topass + "\n"

                    content_block_collected_topass.append(content_block_collected_local_topass)

                    object_creation = News_data.objects.create(title=title_topass, category=category,content=content_block_collected_local_topass)
                    object_creation.save()

                    # print(content_block_collected_local)
                    break



                # print(content_block_collected)
                # print("ok")
                print("ENDS" + " " + f" news {i}")

        # print(content_block_collected)
        # print(feed_data)
    else:
        print(f"Failed to fetch RSS feed: {response.status_code}")

    # load_dotenv()
    # genai.configure(api_key=os.environ.get('GENAI_API_KEY'))
    #
    # # Create the model
    # generation_config = {
    #     "temperature": 1,
    #     "top_p": 0.95,
    #     "top_k": 64,
    #     "max_output_tokens": 8192,
    #     "response_mime_type": "text/plain",
    # }
    #
    # model = genai.GenerativeModel(
    #     model_name="gemini-1.5-flash",
    #     generation_config=generation_config,
    # )
    #
    # chat_session = model.start_chat(
    #     history=[
    #     ]
    # )

    summarize_data = []

    # for refined_text in content_block_collected:
    #     response = chat_session.send_message(f"rephrase the given content into one paragraph: {refined_text}")
    #     summarize_data.append(response.text)
    #     print(response.text)

    for refined_text in content_block_collected_topass:
        summarize_data.append(refined_text)
        print(refined_text)
        break

if __name__ == "__main__":
    url_indiatoday = "https://www.indiatoday.in/rss/1206550"
    url_livemint = "https://www.livemint.com/rss/companies"
    url_nytimes = "https://rss.nytimes.com/services/xml/rss/nyt/Politics.xml"
    url_timesofindia = "https://timesofindia.indiatimes.com/rssfeedstopstories.cms"

    scrape_news_indiatoday_func(url_indiatoday,'sports')
