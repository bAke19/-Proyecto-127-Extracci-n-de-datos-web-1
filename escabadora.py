from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

options = webdriver.FirefoxOptions()
browser = webdriver.Firefox(options=options)
browser.get('https://en.wikipedia.org/wiki/List_of_nearest_stars_and_brown_dwarfs')

time.sleep(10)

scraped_data = []

def scrape():
    
    soup = BeautifulSoup(browser.page_source, "html.parser")

    tables = soup.find_all('table', attrs={'class', 'wikitable'})
    

    for table_star in tables:
        bright_start_table = soup.find('table', attrs={'class','mw-collapsible'})
    
    
    table_body = bright_start_table.find('tbody')
    table_rows = table_body.find_all('tr')

    for row in table_rows:
        table_cols = row.find_all('td')
        numbers_cols = len(table_cols)

        temp_list = []

        for col_data in table_cols:

            if numbers_cols == 10:
                data = col_data.text.strip()

                temp_list.append(data)

        scraped_data.append(temp_list)

scrape()

stars_data = []

for i in range(0,len(scraped_data)):

    if(len(scraped_data[i]) > 0):
        Starts_names = scraped_data[i][0]
        Distance = scraped_data[i][2]
        Mass = scraped_data[i][5]
        Parallax = scraped_data[i][8]
        Lum = scraped_data[i][7]
        required_data = [Starts_names, Distance, Mass, Parallax, Lum]
        stars_data.append(required_data)

headers = ["Star_name", 'Distances', 'Mass', 'Parallax', 'Luminosity']

#Definición del data frame de pandas

star_df_1 = pd.DataFrame(stars_data, columns=headers)
star_df_1.to_csv('scraped_data.csv', index=True, index_label='id')