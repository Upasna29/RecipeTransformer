import urllib2
from bs4 import BeautifulSoup

# url = 'http://allrecipes.com/recipe/219164/the-best-parmesan-chicken-bake/'
# url = 'http://allrecipes.com/recipe/165190/spicy-vegan-potato-curry/'
# url = 'http://allrecipes.com/recipe/219164/the-best-parmesan-chicken-bake/'
# url = 'http://allrecipes.com/recipe/24685/blue-cheese-burgers/'
# url = 'http://allrecipes.com/recipe/236311/baked-eggplant/'
url = 'http://allrecipes.com/recipe/19291/sausage-pasta'
# url = 'http://allrecipes.com/recipe/50233/black-pepper-beef-and-cabbage-stir-fry/'
# url = 'http://allrecipes.com/recipe/241105/sausage-hash-brown-breakfast-casserole/'
# url = 'http://allrecipes.com/recipe/111823/cheeses-baked-macaroni-and-cheese'


page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page, 'html.parser')
soup.prettify()

def findElementsByClassName(element, className):
  return soup.findAll(element, { "class" : className })

