


#this program summarizes news articles

pip install nltk

pip install newspaper3k

#import the libraries
import nltk
from newspaper import Article

#getting the article
url = 'https://www.barcablaugranes.com/2020/1/13/21063370/fc-barcelona-news-13-january-2020-ernesto-valverde-latest-barca-eye-luis-suarez-replacement'
article = Article(url)

#do some NLP
article.download()
article.parse()
nltk.download('punkt')
article.nlp()

#get the authors
article.authors

#get the publish date
article.publish_date

#get the top image
article.top_image

#get the article text
print(article.text)

#get the summary of the article
print(article.summary)



