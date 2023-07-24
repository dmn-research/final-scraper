import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

page = requests.get('https://senate.texas.gov/coi.php')

doc = BeautifulSoup(page.text, 'html.parser')
web_links = doc.select('a')

web_links = [str(i) for i in web_links]
web_links = [i for i in web_links if '_assets/coi/docs/' in i]

link_text = [(re.findall('(?<=\>).*?(?=\<)', str(i)))[0] for i in web_links]
links = ['https://senate.texas.gov/' + (re.findall('(?<=href=").*?(?=")', str(i)))[0] for i in web_links]
if len(link_text) == len(links):
    df = pd.DataFrame()
    df['text'] = link_text
    df['links'] = links
    df.to_csv("links.csv", index=False)
