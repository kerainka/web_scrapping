import requests
from bs4 import BeautifulSoup

KEYWORDS = {'дизайн', 'фото', 'web', 'python', 'cisco'}

URL = 'https://habr.com/ru/all/'

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.find_all('article')
for article in articles:
    article.find()
    content = {text.strip().lower() for text in article.find('div', class_='post__text').text.split()}
    title = {text.strip().lower() for text in article.find('a', class_='post__title_link').text.split()}
    words = content.union(title)
    result = words & KEYWORDS
    if result:
        title_element = article.find('a', class_='post__title_link')
        title_text = title_element.text.strip()
        title_link = title_element.attrs.get('href')
        post_time = article.find('span', class_='post__time').text
        print(post_time + ' - ' + title_text + ' - ' + title_link)
