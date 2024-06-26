from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/Dhading_District'
container = requests.get(url)
soup = BeautifulSoup(container.content,'html.parser')
tables = soup.find_all('table')[1]#, class_= 'wikitable')
titles = tables.find_all('th')
title_list = [title.text.strip() for title in titles]
#print(title_list)
#for table in tables :
#  th_elements = table.find_all('th')
#  print(th_elements)
import pandas as pd
df = pd.DataFrame(columns = title_list)
#print(df)
rows = tables.find_all('tr')
#print(rows)
for row in rows[1:]:
  td_elements = row.find_all('td')
  td_element = [td.text.strip() for td in td_elements]
  length = len(df)
  df.loc[length] = td_element
print(df)