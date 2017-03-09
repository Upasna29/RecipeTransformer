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

measurments = ['tablespoons', 'cloves', 'teaspoons', 'inch', 'ounce', 'piece', 'can']

## determineQuantity
# string -> Arr of Str
#
# determineQuantity takes a ingredient string and parses out the quantities to determine the quantity

def determineIngredients(instruction):
  # Initialize items
  ingredient = []
  quantity = []
  measurment = []
  preperation = []
  
  words = instruction.split(' ')
  print instruction

  # split 
  # quantity_and_measurement, ingredient_and_preperation = parseIngredients(words)
  # print quantity_and_measurement
  # print ingredient_and_preperation

  # extract measurments
  for word in words:
    if word in measurments:
      if not measurment:
        measurment = word
      instruction = removeWord(instruction, word)
    elif word.replace(')', '') in measurments:
      measurment = word
      instruction = removeWord(instruction, measurment)

  if ')' in measurment:
    measurment = measurment.replace(')', '')
  # extract quantity
  for word in words:
    for letter in word:
      if letter.isdigit():
        quantity.append(word)
        instruction = removeWord(instruction, word)
        break

  for num in quantity:
    if '(' in num:
      quantity = num.replace('(', '')

  ingredient, preperation = filterIngredient(instruction)

  if ',' in ingredient:
    ingredient = ingredient.replace(',', '')

  print 'The quantity is: ' + ' '.join(quantity) if isinstance(quantity, list) else 'The quantity is: ' + ''.join(quantity)
  print 'The measurment is: ' + measurment if measurment else 'No measurment'
  print 'The ingredient is: ' + ingredient
  print 'The preperation is: ' + preperation if preperation else 'No preperation'
  print ''


def filterQuantity(quantities):
  correct_quantities = []

  for number in quantities:
    if '(' in number:
      correct_quantities = [number[1:]]
    else:
      correct_quantities.append(number)
  return ' '.join(correct_quantities)


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
      return ingredient[:(i+1)], ingredient[(i+1):]
  return ingredient, False



def num_there(s):
    return any(i.isdigit() for i in s)

def removeWord(s, r):
  return ' '.join([word for word in s.split(' ') if not (word == r)])

# for the instruction, if there is a number, call it the number index.
#
def parseIngredients(ingredient):
  number_index = 0
  for i in range(0, len(ingredient)):
    if ')' in ingredient[i]:
      print ingredient[:(i+2)], ingredient[(i+2):]
      return ingredient[:(i+2)], ingredient[(i+2):]
    elif num_there(ingredient[i]):
      number_index = i
  print ingredient[:(number_index+2)], ingredient[(number_index+2):]
  return ingredient[:(number_index+2)], ingredient[(number_index+2):]






for ingredient in ingredients:
  print determineIngredients(ingredient)


