#!/usr/bin/env python
# coding: utf-8

# In[15]:


import requests
from wordcloud import WordCloud
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


# In[16]:


def Topnews():
    # API keys for multiple news sources
    api_keys = {
        "bbc": "509ca54a17e9429b8b7cc33cc1c50aa3",
        "cnn": "509ca54a17e9429b8b7cc33cc1c50aa3",
        "ap": "509ca54a17e9429b8b7cc33cc1c50aa3"
    }
    
    # URLs for multiple news sources
    urls = {
        "bbc": "https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=" + api_keys["bbc"],
        "cnn": "https://newsapi.org/v1/articles?source=cnn&sortBy=top&apiKey=" + api_keys["cnn"],
        "ap": "https://newsapi.org/v1/articles?source=associated-press&sortBy=top&apiKey=" + api_keys["ap"]
    }
    
    # Get the top news from each source
    results = []
        
    for source in urls:
        open_page = requests.get(urls[source]).json()
        #print(open_page)
        article = open_page["articles"]
          
        for ar in article:
            results.append(ar["title"])
    
    # Combine all the results into one string
    headlines_text = ' '.join(results)
    #print(headlines_text)
    
    # Create the word cloud
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(
        background_color='black',
        stopwords=stopwords,
        max_words=100,
        max_font_size=60,
        scale=3)
    
    wordcloud=wordcloud.generate(headlines_text)
    fig = plt.figure(1, figsize=(12, 12))
    plt.axis('off')
    plt.imshow(wordcloud)
    plt.show()


# In[17]:


if __name__ == '__main__':
    
    # Function call
    Topnews()


# In[ ]:





# In[ ]:




