from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_Nigerian_states_by_GDP"

response = requests.get(url, "html.parser*")

print(response.status_code)

soup = BeautifulSoup(response.text)

soup_table= soup.find_all("table")[3]

soup_table_df = pd.read_html(str(soup_table))

soup_table_df = pd.DataFrame(soup_table_df[0])

soup_table_df.rename(columns = {'GDP (in millions  of USD)' : 'GDP (in millions of USD)'}, inplace =  True)

soup_table_df['GDP (in millions of USD)'] = soup_table_df['GDP (in millions of USD)'].str.replace('US$', '', regex=False)

soup_table_df['GDP (in millions of USD)'] = soup_table_df['GDP (in millions of USD)'].str.replace(',', '', regex=False)

soup_table_df['GDP (in millions of USD)'] = soup_table_df['GDP (in millions of USD)'].astype('int')

soup_table_df.to_csv('List of Nigerian States by GDP data.csv')





