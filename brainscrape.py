# BrainyQuote Web Scraper (By Keyword)
# SPECIAL POMMUNISM EDITION
# Alaina Kafkes

import requests
from bs4 import BeautifulSoup

example_key = "lemons"
example_author = "kurt_vonnegut"

def getQuotes(keyword=example_key, numpages=7):
    """
    Given a keyword and the number of HTML pages of quotes to parse, uses Requests & BeautifulSoup to obtain (quote, author) tuples from BrainyQuote.
    Returns list of (quote, author) tuples and the length of this list.
    """
    # Initialize lists
    quoteArray = []
    authorArray = []
    pageNameArray = [keyword]
    for i in range(2,numpages+1):
        pageNameArray.append(keyword + "_" + str(i))

    # For every page pertaining to a topic
    for page in pageNameArray:
        # Obtain BrainyQuote page html
        base_url = "http://www.brainyquote.com/quotes/keywords/"
        url = base_url + keyword + ".html"
        response_data = requests.get(url).text[:]
        soup = BeautifulSoup(response_data, 'html.parser')

        # Populate quoteArray
        for item in soup.find_all("a", title="view quote"):
            quoteArray.append(item.get_text().rstrip())

        # Populate authorArray
        #for item in soup.find_all("div", class_="bq-aut"):
        #    authorArray.append(item.get_text())

    with open('quotes.txt', 'a') as f:
        for item in quoteArray:
            f.write("%s" % item)
        
    # Create list of tuples of the form (quote, author)
    #ans = zip(quoteArray, authorArray)
    #return ans, len(ans)

