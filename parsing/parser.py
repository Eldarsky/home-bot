from pprint import pprint
import requests

from bs4 import BeautifulSoup as BS
URL = 'https://kinozed.com/horror/'
HEADERS ={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

def get_html(url, params=''):
    req = requests.get(url=url,headers= HEADERS, params=params)
    return req

def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='short clearfix with-mask newshort')
    horors = []
    for item in items:
        info = item.find_all('div', class_='padshort')
        horors.append({
            'title': item.find('div', class_='short-text').find('a').string,
            'ling': item.find('div', class_='short-text').find('a').get('href'),
            'info': [i.text for i in info],
            'biography': item.find('div', class_='sd-text').text
        })
    return horors

def parser():
    html = get_html(URL)
    if html.status_code == 200:
        horor = []
        for i in range(1,2):
            html = get_html(f'{URL}page/{i}/')
            current_page = get_data(html.text)
            horor.extend(current_page)
        return horor
    else:
        raise Exception ('Error 404 ')


