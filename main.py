import csv
import requests

from bs4 import BeautifulSoup


response = requests.get('https://codedamn.com')
soup = BeautifulSoup(response.content, 'html.parser')

head = soup.head
body = soup.body

title = soup.title.text
h1_list = soup.select('h1')
p_list = soup.select('p')


response = requests.get("https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(response.content, 'html.parser')

image_data = []
images = soup.select('img')

for image in images:
    src = image.get('src')
    alt = image.get('alt')

    image_data.append({
        "src": src,
        "alt": alt
    })
