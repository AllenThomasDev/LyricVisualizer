import pandas as pd
import re
stopwords=['i',"i'm" ,'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 
            'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 
            'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were',
             'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if',
              'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during',
               'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 
               'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no',
                'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 
                'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', 
                "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', 
                "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
def text_to_dataframe(lines,ignore_stopwords=True):
    words=[]
    song = [re.sub("[^a-zA-Z0-9\-' .]", '', x).replace('-',' ') for x in lines if ('[' not in x or ']' not in x) and x !='\n']
    for line in song:
        wlist=line.split(' ')
        for word in wlist:
            words.append(word.lower())

    number_of_words=len(words)
    points={'x':[],'y':[],'words':[],'freq':[],'occ':[]}
    for x in range(number_of_words):
        for y in range(number_of_words):
            if words[x] == words[y]:
                points['x'].append(x)
                points['y'].append(y)
                points['words'].append(words[x])
                points['freq'].append(words.count(words[x])/len(words))
                points['occ'].append(words.count(words[x]))

    df=pd.DataFrame.from_dict(points)
    if ignore_stopwords:
        df=df[df['words'].isin(stopwords)==0]
    return(df)

