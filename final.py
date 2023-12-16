from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

#url being scraped 
wikipedia_page = "https://en.wikipedia.org/wiki/The_World%27s_Billionaires"

#sends a request to server and gets a response
getting_request = requests.get(wikipedia_page)

#uses beautifulsoup to parse through the web page and gather data
wiki_parse = BeautifulSoup(getting_request.content, "html")





