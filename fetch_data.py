import urllib2
from bs4 import BeautifulSoup

lyrics= urllib2.urlopen('http://www.metrolyrics.com/i-miss-you-lyrics-blink-182.html')

#print lyrics.info()

lyrics_1=lyrics.read()
#print lyrics_1



lyrics_2= BeautifulSoup(lyrics_1, 'lxml')
lyrics.close()


lyrics_3=lyrics_2.find('p', {'class',"verse"})

#print lyrics_3.get_text()
lyrics_4= lyrics_3.get_text()


#print lyrics_2.prettify()