import requests
from bs4 import BeautifulSoup
from convert import *


def pull_lyric(url,ignore_stopwords):
    page = requests.get(url)
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
    df=text_to_dataframe(l,ignore_stopwords)
    return(df)

