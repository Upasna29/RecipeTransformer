from components import Ingredients, Transform

def commandLineIntro():
  user_input = raw_input(
    "Welcome to our wonderful recipe transformation program! What would you like to do? \n \n" +
    "Print Ingredients(0) \n" +
    "Print Tools(1) \n" +
    "Print Methods(2) \n" +
    "Print Steps(3) \n" +
    "Transform Serving Size(4) \n" +
    "Transform to healthier recipe(5) \n" +
    "Transform to vegetarian recipe(6) \n" +
    "Type 7 to quit \n"

    )

  try:
    if float(user_input) < 0 or float(user_input) > 7:
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
  # elif user_input == 1:

  # elif user_input == 2:

  # elif user_input == 3:

  elif user_input == 4:
    Transform.main()
    user_input = commandLinePrompt()

  # elif user_input == 5:

  # elif user_input == 6:    
  elif user_input == 7: 
    return
commandLinePrompt()