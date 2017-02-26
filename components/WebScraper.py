import urllib2
from bs4 import BeautifulSoup

url = 'http://allrecipes.com/recipe/219164/the-best-parmesan-chicken-bake/'
url_yahoo = 'http://yahoo.com'

page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page, 'html.parser')
soup.prettify()

def findElementsByClassName(element, className):
  return soup.findAll(element, { "class" : className })

