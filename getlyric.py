import requests
from bs4 import BeautifulSoup
page = requests.get("https://www.metrolyrics.com/thinking-about-you-lyrics-frank-ocean.html")

soup = BeautifulSoup(page.content, 'html.parser')
verses=soup.find_all('p','class'=="verse")
l=[]
for verse in verses:
    if 'Lyrics Terms of Use' in verse.text or 'Advisory - the following lyrics contain explicit language:' in verse.text or 'All rights reserved.' in verse.text:
        pass
    else:
        lines=verse.text.split('\n')
        for line in lines:
            l.append(line)
print(l)