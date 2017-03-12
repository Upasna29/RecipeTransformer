import Ingredients
import WebScraper

# instructions_raw = WebScraper.findElementsByClassName("span", "recipe-ingred_txt")
# instructions = list(map(lambda x: x.getText(), instructions_raw))

# print 'Original Recipe'
# for ingredient in ingredients:
#   step = Ingredients.determineIngredients(ingredient)
#   if not step['measurement'] and not step['quantity']:
#     continue
#   else:
#     print step['original']




def commandLinePrompt():
  user_input = raw_input("How should we adjust the serving size of the recipe? (Please enter a value from 0.1 - 5) ")

  try:
    if float(user_input) < 0.1 or float(user_input) > 5:
      print "Error, number out of range"
      return commandLinePrompt()
  except:
    print "Invalid input"
    return commandLinePrompt()
  return user_input


def transformServingSize(instructions):
  multiple = commandLinePrompt()

  print 'Original Recipe'
  for instruction in instructions:
    old_step = Ingredients.determineIngredients(instruction)


    if not old_step['measurement'] and not old_step['quantity']:
      continue
    else:
      print old_step['original']

  print '\nChanging original recipe by a factor of ' + multiple + '...' 
  
  for instruction in instructions:
    old_step = Ingredients.determineIngredients(instruction)

    if not old_step['measurement'] and not old_step['quantity']:
      continue
    else:
      instruction = instruction.split(' ')
      for i in range(0, len(instruction)):
        instruction[i] = str2float(instruction[i])

        if type(instruction[i]) is float:
          instruction[i] *= float(multiple)
          instruction[i] = str(instruction[i])
        elif(instruction[i][0] == '('):
          instruction[i] = str2float(instruction[i][1:])
          instruction[i] *= float(multiple)
          instruction[i] = '('+str(instruction[i])

      print ' '.join(instruction)

def str2float(s):
  for letter in s:
    if letter == '/':
      s = s.split('/')
      return float(s[0]) * 1.0 / float(s[1])
  try:
    return float(s)
  except:
    return s
  

def main():
  instructions_raw = WebScraper.findElementsByClassName("span", "recipe-ingred_txt")
  instructions = list(map(lambda x: x.getText(), instructions_raw))
  transformServingSize(instructions)




