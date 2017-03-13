import Ingredients, ServingSizeTransform, Steps, Transformations, WebScraper
url = 'http://allrecipes.com/recipe/19291/sausage-pasta'


ingredients_raw = WebScraper.findElementsByClassName(url, "span", "recipe-ingred_txt")
directions_raw = WebScraper.findElementsByClassName(url, "span", "recipe-directions__list--item")
len_directs = len(directions_raw)
directions_raw = directions_raw[:len_directs - 1]

current_ingredients = list(map(lambda x: x.getText(), ingredients_raw))
current_steps = list(map(lambda x: x.getText(), directions_raw))

# print current_ingredients
def commandLineIntro(current_steps, current_ingredients):
  user_input = raw_input(
    "Welcome to our wonderful recipe transformation program! What would you like to do? \n \n" +
    "Print Ingredients(0) \n" +
    "Print Tools(1) \n" +
    "Print Methods(2) \n" +
    "Print Steps(3) \n" +
    "Transform Serving Size(4) \n" +
    "Transform to healthier recipe(5) \n" +
    "Transform to less healthy recipe(6) \n" +
    "Transform to vegetarian recipe(7) \n" +
    "Transform to non-vegetarian recipe(8) \n" +
    "Type 9 to quit \n"
    )

  try:
    if float(user_input) < 0 or float(user_input) > 9:
      print "Error, number out of range"
      return commandLinePrompt(current_steps, current_ingredients)
  except:
    print "Invalid input"
    return commandLinePrompt(current_steps, current_ingredients)
  return user_input

def commandLinePrompt(current_steps, current_ingredients):
  user_input = float(commandLineIntro(current_steps, current_ingredients))

  #Ingredients
  if user_input == 0:
    Ingredients.main(current_ingredients)
    user_input = commandLinePrompt(current_steps, current_ingredients)
  elif user_input == 1:
    Steps.tools(current_steps, current_ingredients)
    user_input = commandLinePrompt(current_steps, current_ingredients)
  elif user_input == 2:
    Steps.methods(current_steps, current_ingredients)
    user_input = commandLinePrompt(current_steps, current_ingredients)
  elif user_input == 3:
    Steps.steps(current_steps, current_ingredients)
    user_input = commandLinePrompt(current_steps, current_ingredients)
  elif user_input == 4:
    current_ingredients = ServingSizeTransform.main(current_ingredients)
    user_input = commandLinePrompt(current_steps, current_ingredients)

  # Healthier
  elif user_input == 5:
    current_ingredients, current_steps = Transformations.main(3, current_steps, current_ingredients)
    user_input = commandLinePrompt(current_steps, current_ingredients)
  # Less Healthy
  elif user_input == 6:
    current_ingredients, current_steps = Transformations.main(4, current_steps, current_ingredients)
    user_input = commandLinePrompt(current_steps, current_ingredients)
  # Vegetarian
  elif user_input == 7:
    current_ingredients, current_steps = Transformations.main(1, current_steps, current_ingredients)
    user_input = commandLinePrompt(current_steps, current_ingredients)
  # Non-Vegetarian
  elif user_input == 8:
    current_ingredients, current_steps = Transformations.main(2, current_steps, current_ingredients)
    user_input = commandLinePrompt(current_steps, current_ingredients)
  elif user_input == 9:
    return

commandLinePrompt(current_steps, current_ingredients)
