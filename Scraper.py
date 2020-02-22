import urllib.request as req
#pip install beautifulsoup4
from bs4 import BeautifulSoup 
class Scraper:
    def __init__(self,url = "https://docs.python.org/3/"):
        self.url = url
        
        
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self,url):
        #I will add some validation urls later.
        self._url =url
        self.page =self._url
        
    @url.getter
    def url(self):
        return self._url
        
    
    @property
    def page(self):
           return self._page
    @page.getter
    def page(self):
           return self._page
    @page.setter
    def page(self,url):
           self._page =  req.urlopen(url).read()
    
    def readPage(self):
        
        return BeautifulSoup(self.page, "html.parser")

    
    
    #hansard_menu = soup.find_all("div","itemContainer")
    
    def find_Title(self):
        return self.readPage().title.string

    #@override
    def __str__(self):
        return f"{self.url}"
    
#x = Scraper()
#print(f"{x}\n {x.readPage} ")
x = Scraper("https://pl.wikipedia.org/wiki/1-Wire")
print(f"{x}\n {x.find_Title()} ")

