from bs4 import BeautifulSoup
import requests

url="https://www.tripadvisor.com/SmartDeals-g255055-Australia-Hotel-Deals.html"


def scraper(link):
    myreg=requests.get(link).text
    soup=BeautifulSoup(myreg,'lxml')

    #print (soup.prettify())

    thediv=soup.find_all('div',class_='ui_column is-8 main_col allowEllipsis ')
    for x in thediv:    
        title11=x.find('a',class_='property_title prominent ')
        rating11=x.find('a',class_='review_count').text.replace("reviews","").replace(",","")
        image11=x.find('div',class_='inner')
        result="Title: "+title11.text+"\nReview: "+rating11+"\nLink: https://tripadvisor.com"+title11.get('href')
        print()
        print(result)

def getlinks(link):
    #print("apa kabar")
    myreg=requests.get(link).text
    soup=BeautifulSoup(myreg,'lxml')
    pagenum=soup.find('div',class_='unified ui_pagination standard_pagination ui_section listFooter')
    print(pagenum)

getlinks(url)
