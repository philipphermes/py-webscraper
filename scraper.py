import requests
from bs4 import BeautifulSoup

print('Enter the cyberport url you want to scrape:')
url = input()

page = requests.get(url, headers={
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'})

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find_all("span", class_="productOmnibox-price__price--delivery")

print(page.status_code)

if len(results) != 0:
    result = results[0].text
    result = result.replace("€ ", "")
    result = result.replace(",", ".")
    resultFloat = float(result)

    print(result)
else:
    print("no results found")
