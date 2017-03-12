import urllib2
from bs4 import BeautifulSoup

# url = 'http://allrecipes.com/recipe/219164/the-best-parmesan-chicken-bake/'
url = 'http://allrecipes.com/recipe/165190/spicy-vegan-potato-curry/'
# url = 'http://allrecipes.com/recipe/219164/the-best-parmesan-chicken-bake/'
# url = 'http://allrecipes.com/recipe/24685/blue-cheese-burgers/'
# url = 'http://allrecipes.com/recipe/236311/baked-eggplant/'
url_yahoo = 'http://yahoo.com'



page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page, 'html.parser')
soup.prettify()

def findElementsByClassName(element, className):
  return soup.findAll(element, { "class" : className })

