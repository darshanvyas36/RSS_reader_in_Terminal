from bs4 import BeautifulSoup
import requests

url = requests.get('https://realpython.com/atom.xml')
# print(url)

soup = BeautifulSoup(url.content, 'xml')

entries = soup.find_all('entry')

for entry in entries:
    title = entry.title.text
    summary = entry.summary.text
    link = entry.link['href']
    print(f"Tittle : {title}\n\nSummary : {summary}\n\nLink : {link}\n\n_______________________________________\n\n")



