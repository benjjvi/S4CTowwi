import requests
from bs4 import BeautifulSoup
import json
import warnings
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from googletrans import Translator
import twikit

def analyze_headline(title):
    print(f"Analysing {title}")
    translator = Translator()

    # Translate title from Welsh to English
    translated_title = translator.translate(title, src='cy', dest='en').text

    sentiment = SentimentIntensityAnalyzer()
    analysis = sentiment.polarity_scores(translated_title)

    score = analysis['compound']

    return score


def fetch_news_as_json():
    url = 'https://newyddion.s4c.cymru/topics/0'

    # Make a GET request to the URL
    response = requests.get(url)
    response.encoding = "utf-8"

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the content with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the script tag with id '__NEXT_DATA__'
        script_tag = soup.find('script', id='__NEXT_DATA__')

        # Extract JSON data from the script tag if it exists
        if script_tag:
            try:
                # Get the content within the script tag
                script_content = script_tag.string

                # Ensure script content is not None and parse JSON
                if script_content:
                    json_data = json.loads(script_content)

                    # Extract articles from JSON data
                    articles = json_data['props']['pageProps']['articles']

                    if len(articles) < 2:
                        warnings.warn("Articles contains less than two elements.", UserWarning)
                else:
                    raise Exception("Script tag with id '__NEXT_DATA__' has no content.")
            except json.JSONDecodeError as e:
                raise Exception(f"Error decoding JSON: {e}")
        else:
            raise Exception("Script tag with id '__NEXT_DATA__' not found.")
    else:
        raise Exception(f"Failed to retrieve the web page. Status code: {response.status_code}")

    return articles

def process_articles(articles):
    new_articles = []
    for article in articles:
        new_article = {
            "title": article["title"].replace("&#039;", "'"),
            "id": article["id"],
            "weight": analyze_headline(article["title"])
        }
        new_articles.append(new_article)
    
    return new_articles

def get_id_history():
    with open("seen.pydict", "r") as file:
        seen = eval(file.read())

    return seen

def compare_history_with_new_request():
    pass

def add_unseen_articles_to_history():
    pass

def tweet():
    pass

# run loop
while True:
    # get all already logged IDs.
    prelogged_ids = get_id_history()

    # get new items, and remove any already logged
    articles = fetch_news_as_json()
    unseen_articles = compare_history_with_new_request()

    # add unseen items to history log.
    add_unseen_articles_to_history(unseen_articles)

    # tweet! (X it? i hate the new rebranding.)
    for item in unseen_articles:
        tweet(item)


