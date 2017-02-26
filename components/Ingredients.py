import WebScraper

ingredients_raw = WebScraper.findElementsByClassName("span", "recipe-ingred_txt")
ingredients = list(map(lambda x: x.getText(), ingredients_raw))

print ingredients

a = '2 tablespoons olive oil'

def determineQuantity(ingredient):
  numbers = []
  for i in range(0, len(ingredient)):
    if ingredient[i].isdigit():
      numbers.append(ingredient[i])
    elif ingredient[i] == '/':
      numbers.append(ingredient[i])
    elif ingredient[i] == '(':
      numbers.append(ingredient[i])

  if (len(numbers) == 0):
    return 'error'
  elif (len(numbers) == 1):
    return numbers[0]
  else:
    return numbers





for ingr in ingredients:
  print determineQuantity(ingr)


