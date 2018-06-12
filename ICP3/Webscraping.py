from bs4 import BeautifulSoup #import package for web scraping
import urllib.request  #import url library
import os

url = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India" #define the url for the web scraping
source_code = urllib.request.urlopen(url)    #request the wiki url using url lib
plain_text = source_code   #assign the value
soup = BeautifulSoup(plain_text, "html.parser") #call the Beautifulsoup method for parsing wiki page html file
print("Title is: ",soup.title.string) #print the Title of the page
results = soup.find_all('a') #find the hyper links of wiki html page
print("Links are: ")
for link in results:  #loop each hyper links
    print(link.get('href')) #print the links value
rt_tab=soup.find('table', class_='wikitable sortable plainrowheaders') #find the table from the wiki html page
print(rt_tab) #prints the table