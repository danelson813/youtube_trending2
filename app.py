import requests
from bs4 import BeautifulSoup
from helpers import write2file
import pandas as pd

res = requests.get('https://www.imdb.com/chart/tvmeter/?ref_=nv_tvv_mptv')
soup = BeautifulSoup(res.text, 'html.parser')
shows = soup.find('tbody').find_all('tr')
print(f'There are {len(shows)} shows')

best_shows = []
for show in shows:
    title = show.find('td', class_='titleColumn').find('a').text.strip()
    year = show.find('td', class_='titleColumn').find('span').text.strip()
    try:
        rating = show.find('td', class_='ratingColumn imdbRating').find('strong').get('title').replace(',', '_')
    except:
        rating = "None"
    link = 'https://www.imdb.com' + show.find('td', class_='titleColumn').find('a').get('href')
    img_link = show.find('td', class_='posterColumn').find('img').get('src')
    result = {
        'title': title,
        'year': year,
        'rating': rating,
        'link': link,
        'img_link': img_link
    }
    str_ = f"{title}, {year}, {str(rating)}, {link}, {img_link}\n"
    best_shows.append(result)
    write2file(str_)
    print(str_)

df = pd.DataFrame(best_shows)
df.to_csv('Best_shows_df.csv', index=False)
