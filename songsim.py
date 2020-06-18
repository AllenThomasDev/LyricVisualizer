import pandas as pd
import re
def text_to_dataframe(lines):
    words=[]
    song = [re.sub("[^a-zA-Z0-9\-' .]", '', x).replace('-',' ') for x in lines if ('[' not in x or ']' not in x) and x !='\n']
    for line in song:
        wlist=line.split(' ')
        for word in wlist:
            words.append(word)

    number_of_words=len(words)
    points={'x':[],'y':[],'words':[],'freq':[]}
    for x in range(number_of_words):
        for y in range(number_of_words):
            if words[x] == words[y]:
                points['x'].append(x)
                points['y'].append(y)
                points['words'].append(words[x])
                points['freq'].append(words.count(words[x])/len(words))
    df=pd.DataFrame.from_dict(points)
    return(df)

