import Ingredients, ServingSizeTransform, Tools, Transformations

def commandLineIntro():
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
      return commandLinePrompt()
  except:
    print "Invalid input"
    return commandLinePrompt()
  return user_input

def commandLinePrompt():
  user_input = float(commandLineIntro())

  #Ingredients
  if user_input == 0:
    Ingredients.main()
    user_input = commandLinePrompt()
  elif user_input == 1:
     Tools.main()
     user_input = commandLinePrompt()

  # elif user_input == 2:

  # elif user_input == 3:

  elif user_input == 4:
    ServingSizeTransform.main()
    user_input = commandLinePrompt()

  # Healthier
  elif user_input == 5:
    Transformations.main(3)
    user_input = commandLinePrompt()
  # Less Healthy
  elif user_input == 6:
    Transformations.main(4)
    user_input = commandLinePrompt()
  # Vegetarian
  elif user_input == 7:
    Transformations.main(1)
    user_input = commandLinePrompt()
  # Non-Vegetarian
  elif user_input == 8:
    Transformations.main(2)
    user_input = commandLinePrompt()
  elif user_input == 9:
    return
commandLinePrompt()
