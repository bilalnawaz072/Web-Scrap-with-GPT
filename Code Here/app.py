# import requests
# from bs4 import BeautifulSoup
# import csv

# # Send a GET request to the website
# url = 'https://books.toscrape.com/'
# response = requests.get(url)

# # Parse the HTML content of the page using BeautifulSoup
# soup = BeautifulSoup(response.content, 'html.parser')

# # # Find all book titles on the page
# # book_titles = [h3.a['title'] for h3 in soup.find_all('h3')]


# # # Find all book titles and prices on the page
# # book_titles = [h3.a['title'] for h3 in soup.find_all('h3')]
# # book_prices = [p.text for p in soup.find_all('p', class_='price_color')]

# # Find all book titles, prices, and links on the page
# book_titles = [h3.a['title'] for h3 in soup.find_all('h3')]
# book_prices = [p.text for p in soup.find_all('p', class_='price_color')]
# book_links = [url + a['href'] for a in soup.find_all('a', href=True)]


# # # Print the book titles
# # for title in book_titles:
# #     print(title)

# # for title, price in zip(book_titles, book_prices):
# #     print(f"{title} - {price}")

# # Print the book titles, prices, and links
# for title, price, link in zip(book_titles, book_prices, book_links):
#     print(f"{title} - {price} - {link}")


# # Write the book data to a CSV file
# with open('books.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['Title', 'Price', 'Link'])


# --------------------------

import requests
import csv
from bs4 import BeautifulSoup

# Send a GET request to the website
url = 'https://books.toscrape.com/'
response = requests.get(url)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all book titles, prices, and links on the page
book_titles = [h3.a['title'] for h3 in soup.find_all('h3')]
book_prices = [p.text for p in soup.find_all('p', class_='price_color')]
book_links = [url + a['href'] for a in soup.find_all('a', href=True)]

# Write the book data to a CSV file
with open('books.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title', 'Price', 'Link'])
    for title, price, link in zip(book_titles, book_prices, book_links):
        writer.writerow([title, price, link])
