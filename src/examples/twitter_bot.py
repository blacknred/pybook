'''
Twitter bot that scrapes web pages and posts content

It will:
    - scrapes content from The Coursera Blog
    - tweets them periodically

Prerequisites:
    - API keys for Twitter from developer.twitter.com
    - pip3:
        - lxml & requests (web scraping)
        - nltk ((natural language toolkit) You will use to split
        paragraphs of blogs into sentences)
        - twitter (lib for making API calls to Twitter’s servers)
    - also lib:
        - random (randomly select parts of an entire scraped blog post)
        - time (bot sleep periodically after certain actions)

As of 2019, it is estimated that bots account for about 24% of all tweets on Twitter.
Advanced Twitter bot that can do multiple things simultaneously: https://github.com/schedutron/chirps
Also You can implement word prefilter using regular expressions and natural language processing.
'''

import requests
import random
import time
import nltk
import sys
from lxml.html import fromstring
from twitter import OAuth, Twitter


def extract_paratext(paras, tokenizer):
    """Extracts text from <p> elements and returns a clean, tokenized random
    paragraph."""

    paras = [para.text_content() for para in paras if para.text_content()]
    para = random.choice(paras)

    '''
    for breaking the paragraph into sentences you can:
    - using the Python’s split() method. However this can be difficult
    since a sentence can be split at multiple breakpoints.
    - leverage natural language processing through the nltk library
    '''
    return tokenizer.tokenize(para)


def extract_text(para):
    """Returns a sufficiently-large random text from a tokenized paragraph,
    if such text exists. Otherwise, returns None."""

    '''
    find random sentence that  be a quote for a tweet, so it can’t
    exceed 280 characters. It is possible that none of the sentences
    meet this size condition within ten attempts. In this case, you’ll
    ignore the corresponding blog post and move on to the next one.
    '''
    for _ in range(10):
        text = random.choice(para)
        if text and 60 < len(text) < 210:
            return text

    return None


def scrape_coursera(HEADERS, tokenizer):
    """Scrapes content from the Coursera blog."""

    url = 'https://blog.coursera.org'
    feed = requests.get(url, headers=HEADERS)

    # tree structure of the feed webpage
    tree = fromstring(feed.content)

    # get the links
    links = tree.xpath('//div[@class="recent"]//div[@class="title"]/a/@href')

    # get the a random sentence from the post by every link
    for link in links:
        # get post
        post = requests.get(link, headers=HEADERS)
        # tree structure of the post webpage
        blog_tree = fromstring(post.content)
        # all paragraphs obj
        paras = blog_tree.xpath('//div[@class="entry-content"]/p')
        # random paragraph text
        para = extract_paratext(paras, tokenizer)
        # find sentence
        text = extract_text(para)
        if not text:
            continue

        #
        yield '"%s" %s' % (text, link)


def main():
    # twitter api keys
    ACCESS_TOKEN = 'your-access-token'
    ACCESS_SECRET = 'your-access-secret'
    CONSUMER_KEY = 'your-consumer-key'
    CONSUMER_SECRET = 'your-consumer-secret'
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
                      ' AppleWebKit/537.36 (KHTML, like Gecko) Cafari/537.36'
    }

    # Checks
    try:
        # downloads a dataset necessary for parsing paragraphs and
        # tokenizing (splitting) them into smaller components.
        nltk.download('punkt')
        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

        # authentication object
        oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET,
                      CONSUMER_KEY, CONSUMER_SECRET)

        # bot
        t = Twitter(auth=oauth)
    except Exception as e:
        print("Error {} - {}!".format(type(e), e))
        sys.exit(1)

    # The main loop of the bot
    print('---Bot started---\n')

    news_funcs = ['scrape_coursera']
    news_iterators = []

    for func in news_funcs:
        news_iterators.append(globals()[func](HEADERS, tokenizer))

    while True:
        for i, iterator in enumerate(news_iterators):
            try:
                tweet = next(iterator)
                t.statuses.update(status=tweet)
                print(tweet, end='\n\n')
                time.sleep(600)
            except StopIteration:
                news_iterators[i] = globals()[news_funcs[i]]()


if __name__ == '__main__':
    main()
