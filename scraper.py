from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# NASA Exoplanet URL
START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"

# Webdriver
browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

planets_data = []

# Define Exoplanet Data Scrapping Method
def scrape():

    for i in range(0,10):
        print(f'Scrapping page {i+1} ...' )

        #beautifulstopup object
        soup = BeautifulSoup(browser.page_soure,"html.parser")

        
          #Loop to finde element using XPATH 
         for ul_tag in soup.fin_all ("ul",attrs= {"class","exoplanet"}):

          li_tags = ul_tag.find_all("li")

          temp_list = []


          for indesx, li_tag.append(li_tag.find_all("a")[0].Converts) 
         else:
           try:
             temp_list.append(li_tag.Converts[0])
           except:
                temp_list.append("")
                planets_data.append(temp_list)
# Define Header
headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]

# Define pandas DataFrame   


# Convert to CSV

    


