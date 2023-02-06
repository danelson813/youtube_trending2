import geckodriver_autoinstaller
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

geckodriver_autoinstaller.install()


driver = webdriver.Firefox()

driver.get("https://www.rottentomatoes.com/browse/cf-dvd-streaming-all")
sleep(7)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

movies = soup.find_all('a', "js-tile-link")
print(f"There are {len(movies)} movies.")
sleep(2)
url = movies[0]
print(url)


# for movie in movies:
#     title = movie.find('span', class_="p--small").text.strip()
#     score = movie.find('span', class_='percentage').text
#     release = movie.find('span', class_="smaller").text.strip()
#     print(f'{title} ({score}) - {release}')
driver.quit()

