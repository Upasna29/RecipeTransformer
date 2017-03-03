# import WebScraper

# ingredients_raw = WebScraper.findElementsByClassName("span", "recipe-ingred_txt")
# ingredients = list(map(lambda x: x.getText(), ingredients_raw))

ingredients = [
  u'4 potatoes, peeled and cubed', 
  u'2 tablespoons vegetable oil', 
  u'1 yellow onion, diced', 
  u'3 cloves garlic, minced', 
  u'2 teaspoons ground cumin', 
  u'1 1/2 teaspoons cayenne pepper', 
  u'4 teaspoons curry powder', 
  u'4 teaspoons garam masala', 
  u'1 (1 inch) piece fresh ginger root, peeled and minced', 
  u'2 teaspoons salt', 
  u'1 (14.5 ounce) can diced tomatoes', 
  u'1 (15 ounce) can garbanzo beans (chickpeas), rinsed and drained', 
  u'1 (15 ounce) can peas, drained', 
  u'1 (14 ounce) can coconut milk', 
  u'Add all ingredients to list', 
  u'', 
  u'Add all ingredients to list'
]

## determineQuantity
# string -> Arr of Str
#
# determineQuantity takes a ingredient string and parses out the quantities to determine the quantity

def determineIngredients(ingredient):
  quantities = []
  measurments = []
  ingredient_names = []
  measurment_flag = False
  
  ingredient_names = ingredient.split(' ')
  print ingredient
  numerics, ingredient_names = parseIngredients(ingredient_names)


  for word in numerics:
    if measurment_flag:
      measurments.append(word)
      measurment_flag = False
    for letter in word:
      if letter.isdigit():
        quantities.append(word)
        measurment_flag = True
        break

  # for word in ingredient:



  quantities = filterQuantity(quantities)
  measurments = filterMeasurment(measurments)
  ingredient_names = filterIngredient(ingredient_names)
  if quantities or measurments:
    print ''
    print 'quantity'
    print quantities
    print ''
    print 'measurment'
    print measurments
    print ''
    print 'ingredient'
    print ingredient_names

def filterQuantity(quantities):
  correct_quantities = []

  for number in quantities:
    if '(' in number:
      correct_quantities = [number[1:]]
    else:
      correct_quantities.append(number)
  return correct_quantities


def filterMeasurment(measurments):
  correct_measurements = []
  for measurment in measurments:
    # print measurment
    if ')' in measurment:
      correct_measurements = [measurment[:-1]]
      return correct_measurements
    elif num_there(measurment):
      continue
    else:
      correct_measurements.append(measurment)
  return correct_measurements

def filterIngredient(ingredient):
  for i in range(0, len(ingredient)):
    if ',' in ingredient[i]:
      return ingredient[:(i+1)]
  return ingredient



def num_there(s):
    return any(i.isdigit() for i in s)


def parseIngredients(ingredient):
  number_index = 0
  for i in range(0, len(ingredient)):
    if ')' in ingredient[i]:
      return ingredient[:(i+2)], ingredient[(i+2):]
    elif num_there(ingredient[i]):
      number_index = i
  return ingredient[:(number_index+2)], ingredient[(number_index+2):]







for ingredient in ingredients:
  print determineIngredients(ingredient)


