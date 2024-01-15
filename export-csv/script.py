import csv
import requests

from bs4 import BeautifulSoup


response = requests.get("https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(response.content, 'html.parser')

products_info = []
products = soup.select('div.thumbnail')

for product in products:
    title = product.select('h4> a.title')[0].text
    review = product.select('div.ratings')[0].text

    product_info = {
        "title": title.strip(),
        "review": review.strip()
    }
    products_info.append(product_info)

keys = products_info[0].keys()

with open('export-csv/products.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(products_info)
