import requests
from bs4 import BeautifulSoup

print('Enter the cyberport url you want to scrape:')
url = input()

headers = {
    'authority': 'www.cyberport.de',
    'accept': '*/*',
    'accept-language': 'de-DE,de;q=0.9',
    'dnt': '1',
    'referer': url,
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
page = requests.get(url, headers=headers)

print("Status: " + str(page.status_code))

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find_all("span", class_="productOmnibox-price__price--delivery")


if len(results) != 0:
    result = results[0].text
    result = result.replace("€ ", "")
    result = result.replace(".", "")
    result = result.replace(",", ".")
    result = result.replace("\n", "")

    resultFloat = float(result)

    print(result)
else:
    print("no results found")
