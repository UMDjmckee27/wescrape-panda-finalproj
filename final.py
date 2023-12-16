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

#searches and finds the tables on the page (2023 networths)
tables = wiki_parse.find_all("table", {"class": "wikitable"})
# Specifies that the second table or "index [1]" is being used
data_for_2023 = tables[1]

#where the data is stored. *acts as a list of lists*
individual_column_data = []

#gets data from the table and create the list of lists
rows = data_for_2023.find_all("tr")
#focusing on the individual rows
for row in rows:
    columns = row.find_all(["th", "td"])
    #strips just the text
    columns_data = [col.get_text(strip=True) for col in columns]
    individual_column_data.append(columns_data)

#gets rows max length to make data standardized 
max_row_length = max(len(row) for row in individual_column_data)

#targets shorter rows with empty strings to make them of equal length (for numpy)
for row in individual_column_data:
    while len(row) < max_row_length:
        row.append("")

#convert the data within the "list of lists" to numpy array
np_data = np.array(individual_column_data)

#creates dataframe from array
df = pd.DataFrame(np_data)

#save the dataframe to CSV 
df.to_csv("networths.csv", index=False)
print("CSV created: check source control")






