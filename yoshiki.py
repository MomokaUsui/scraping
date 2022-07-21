import requests
import time
from bs4 import BeautifulSoup
import json

for i in range(350):
    #print(f"getting{i+1}")
    site_data = requests.get(f"https://8212.teacup.com/kanagawa894/bbs?page={i+1}&")
    soup = BeautifulSoup(site_data.content, 'html.parser')
    content_array = ['title', 'author', 'created', 'article']
    title_array = []
    author_array = []
    created_array = []
    article_array = []
    title = soup.find_all('a', class_='Kiji_Title')
    for i in title:
        title_array.append(i.get_text())
    author = soup.find_all('span', class_='Kiji_Author')
    for i in author:
        author_array.append(i.get_text())
    created = soup.find_all('span', class_='Kiji_Created')
    for i in created:
        created_array.append(i.get_text())
    article = soup.find_all('span', class_='Kiji_Article')
    for i in article:
        article_array.append(i.get_text())
    for i in range(len(title_array)):
        i_array = []
        i_array.append(title_array[i].replace('\u3000', '').replace('\n', '').replace('\xa0', ''))
        i_array.append(author_array[i].replace('\u3000', '').replace('\n', '').replace('\xa0', ''))
        i_array.append(created_array[i].replace('\u3000', '').replace('\n', '').replace('\xa0', ''))
        i_array.append(article_array[i].replace('\u3000', '').replace('\n', '').replace('\xa0', ''))
        print(i_array)
    with open(f"html/page{i+1}.html", "w") as f:
        f.write(site_data.text)
    time.sleep(3)