import Steps, WebScraper, Ingredients
import random


meats = ['chicken', 'pork', 'beef', 'steak', 'turkey', 'ham', 'lamb', 'rabbit', 'duck', 'goose', 'sausage']
seafood = ['fish', 'tuna', 'salmon']
shellfish = ['lobster', 'snail', 'scallop', 'crab', 'prawn']
vegetables = ['tofu', 'mushroom', 'eggplant', 'quinoa', 'soy']
liquidDairy = ['almond milk', 'soy milk', 'coconut milk']
solidDairy = ['nutritional yeast', 'dairy free cheese']


meatSubstitutes = {"chicken": vegetables, "pork": vegetables, "beef": vegetables, "steak": vegetables, "turkey": vegetables, "ham": vegetables, "lamb": vegetables, "rabbit": vegetables, "duck": vegetables, "goose": vegetables, "sausage":vegetables}

vegSubstitutes = {"tofu": meats, "mushroom": meats, "eggplant": meats, "quinoa": meats, "soy": meats}

# TODO
# dairySubstitutes     we need dairy substitutes
dairySubstitutes = {"milk": liquidDairy, "cheese": solidDairy, "cream": liquidDairy, "yogurt": liquidDairy}
# healthySubstitutes    we need healthy substitutes
healthySubstitutes = {'sugar': ['brown sugar', 'honey', 'cinnamon', 'vanilla'], 'corn': ['flour'], 'butter': ['unsweetened apple sauce', 'olive oil', 'mashed banana'], 'pasta': ['whole-wheat pasta', 'zucchini pasta'], 'milk': ['fat free milk', 'almond milk', 'soy milk'], 'pickles': ['cucumbers'], 'olives': ['cherry tomatoes'], 'mayonnaise':['reduced fat spreads'], 'jelly': ['mashed fresh berries'] }
# unhealthySubstitues    healthy to unhealthy?
unhealthySubstitutes = {"pine nuts": meats,'olive oil': ['butter'], 'whole-wheat pasta': ['pasta'], 'unsweetened apple sauce': ['butter'], 'flour': ['corn'], 'vanilla': ['sugar'], 'zucchini pasta': ['pasta'], 'almond milk': ['milk'], 'cucumbers': ['pickles'], 'honey': ['sugar'], 'cherry tomatoes': ['olives'], 'cinnamon': ['sugar'], 'fat-free milk': ['milk'], 'mashed fresh berries': ['jelly'], 'reduced-fat spreads': ['mayonnaise'], 'soy milk': ['milk'], 'mashed banana': ['butter'], 'brown sugar': ['sugar']}

americanSubstitutes = {'Parmesan': ['American'],"sausage":['hot dog', "hamburger"],'olive oil': ['butter'], 'whole-wheat pasta': ['macaroni'],'cucumbers': ['pickles'], 'honey': ['sugar'], "tofu": meats, "mushroom": meats, "eggplant": meats, "quinoa": meats, "soy": meats, "ham": ['hamburger', 'hot dog'], 'fat free milk': ['milk'], 'mashed fresh berries': ['jelly'], 'sour cream': ['mayonnaise'], 'soy milk': ['milk'], 'mashed banana': ['butter'], 'brown sugar': ['sugar'] }

# ingredients = Steps.getListIngredients()



def findIngredientSubstitution(ingredients, num):
    '''
    Finds the problem ingredient and maps it to a random substitution.
    Input:
        ingredients: list of ingredients
        num can be:
            1: To vegan/vegetarian
            2: To NON vegan/vegetarian
            3: To healthy
            4: To unhealthy
    Output: Dictionary with one-to-one mapping for the ingredient.
    Example output: {'chicken': 'tofu', 'milk': 'almond milk'}
    '''

    ingredientSubs = {}
    for ingredient in ingredients:
        # 1: To vegan/vegetarian
        bigrams = [b for l in [ingredient] for b in zip(l.split(" ")[:-1], l.split(" ")[1:])]
        tempbigrams = []
        for each in bigrams:
            tempbigrams.append(each[0]+ " "+ each[1])

        temp = ingredient.split()
        if num == 1:
            for word in temp:
                if word in meatSubstitutes:
                    idx = random.randint(0, len(meatSubstitutes[word])-1)
                    substitute = meatSubstitutes[word][idx]
                    ingredientSubs[ingredient] = substitute
                    ingredientSubs[word] = substitute
                    break
                elif word in dairySubstitutes:
                    idx = random.randint(0, len(dairySubstitutes[word])-1)
                    substitute = dairySubstitutes[word][idx]
                    ingredientSubs[ingredient] = substitute
                    ingredientSubs[word] = substitute
                    break

        # 2: To NON vegan/vegetarian
        if num == 2:
            for word in temp:
                if word in vegSubstitutes:
                    idx = random.randint(0, len(vegSubstitutes[word])-1)
                    substitute = vegSubstitutes[word][idx]
                    ingredientSubs[ingredient] = substitute
                    ingredientSubs[word] = substitute
                    break

        # 3: To unhealthy
        if num == 4:
            for word in temp:
                if word in unhealthySubstitutes:
                    idx = random.randint(0, len(unhealthySubstitutes[word])-1)
                    substitute = unhealthySubstitutes[word][idx]
                    ingredientSubs[ingredient] = substitute
                    ingredientSubs[word] = substitute
                    break
            for word in tempbigrams:
                if word in unhealthySubstitutes:
                    idx = random.randint(0, len(unhealthySubstitutes[word])-1)
                    substitute = unhealthySubstitutes[word][idx]
                    ingredientSubs[ingredient] = substitute
                    ingredientSubs[word] = substitute
                    break

        # 4: To healthy
        if num == 3:
            for word in temp:
                if word in healthySubstitutes:
                    idx = random.randint(0, len(healthySubstitutes[word])-1)
                    substitute = healthySubstitutes[word][idx]
                    ingredientSubs[ingredient] = substitute
                    ingredientSubs[word] = substitute
                    break

        #5: To American
        if num == 5:
            for word in temp:
                if word in americanSubstitutes:
                    idx = random.randint(0, len(americanSubstitutes[word])-1)
                    substitute = americanSubstitutes[word][idx]
                    ingredientSubs[ingredient] = substitute
                    ingredientSubs[word] = substitute
                    break
            for word in tempbigrams:
                if word in americanSubstitutes:
                    idx = random.randint(0, len(americanSubstitutes[word])-1)
                    substitute = americanSubstitutes[word][idx]
                    ingredientSubs[ingredient] = substitute
                    ingredientSubs[word] = substitute
                    break

    return ingredientSubs

# def makeSubstitutions(steps, ingredientSubs):
#     for i, step in enumerate(steps):
#         stepArray = step.split()
#         for index, ingredient in enumerate(stepArray):
#             if ingredient in ingredientSubs:
#                 stepArray[index] = ingredientSubs[ingredient]
#                 print 'After change: ', stepArray
#         step = " ".join(stepArray)
#         steps[i] = step
#
#     print steps
def makeSubstitutions(steps, ingredientSubs):
    new_steps = []
    for i, step in enumerate(steps):
        for ingredient in ingredientSubs:
            if ingredient in step:
                step = step.replace(ingredient, ingredientSubs[ingredient])
        new_steps.append(step)

    return new_steps

def makeSubstitutionInInstructions(instructions, ingredientSubs):
    new_instructions = []

    for instruction in instructions:
        ins_bigrams = [b for l in [instruction] for b in zip(l.split(" ")[:-1], l.split(" ")[1:])]
        ins_tempbigrams = []
        for each in ins_bigrams:
            ins_tempbigrams.append(each[0]+ " "+ each[1])

        instruction = instruction.split(' ')

        for i,each in enumerate(ins_tempbigrams):
            if each in ingredientSubs:
                instruction[i] = ingredientSubs[each]
                del instruction[i+1]


        for i in range(0, len(instruction)):
            for ingredient in ingredientSubs:
                if ingredient == instruction[i]:
                    instruction[i] = ingredientSubs[ingredient]
        new_instructions.append(' '.join(instruction))
    return new_instructions



# tempIngredients = ['olive oil', 'garlic', 'crushed red pepper flakes', 'chicken breasts', 'prepared marinara sauce', 'chopped fresh basil', 'shredded mozzarella cheese', 'grated Parmesan cheese', 'garlic croutons', 'Add all ingredients to list', '', 'Add all ingredients to list']
# tempSteps = ['Preheat oven to 350 degrees F (175 degrees C)', 'Coat the bottom of a 9x13 inch casserole dish with olive oil, and sprinkle with garlic and hot red pepper flakes', 'Arrange the chicken breasts in bottom of the dish, and pour marinara sauce over chicken', 'Sprinkle basil over marinara sauce, and top with half the mozzarella cheese, followed by half the Parmesan cheese', 'Sprinkle on the croutons, then top with the remaining mozzarella cheese and remaining Parmesan cheese', 'Bake in preheated oven until cheese and croutons are golden brown and the chicken is no longer pink inside, about 35 minutes to an hour, depending on the shape and thickness of your chicken breasts', 'An instant-read thermometer inserted into the thickest part of a chicken breast should read at least 160 degrees F (70 degrees C)']
# ingredientSubs = findIngredientSubstitution(tempIngredients, 1)
# print ingredientSubs
# makeSubstitutions(tempSteps, ingredientSubs)
# ingredientSubs = findIngredientSubstitution(ingredients, 1)
# print ingredientSubs
# makeSubstitutionInInstructions(steps, ingredientSubs)


def main(i, steps, instructions):
    # instructions_raw = WebScraper.findElementsByClassName("span", "recipe-ingred_txt")
    # instructions = list(map(lambda x: x.getText(), instructions_raw))
    # print steps
    dummy, ingredients = Steps.getDirections(steps, instructions)
    ingredientSubs = findIngredientSubstitution(ingredients, i)
    new_steps = makeSubstitutions(steps, ingredientSubs)
    new_recipe = makeSubstitutionInInstructions(instructions, ingredientSubs)

    print 'Original Recipe'
    new_instructions = []
    new_directions = []
    for instruction in instructions:
        old_step = Ingredients.determineIngredients(instruction)


        if not old_step['measurement'] and not old_step['quantity']:
            continue
        else:
            print old_step['original']

    print '\nDirections: '
    for i, step in enumerate(steps):
        if step:
            print str(i+1)+'. ', step

    print '\nNew Recipe'
    print '\nIngredients: '
    for instruction in new_recipe:
        old_step = Ingredients.determineIngredients(instruction)

        if not old_step['measurement'] and not old_step['quantity']:
            continue
        else:
            print old_step['original']
            new_instructions.append(old_step['original'])

    print '\nDirections: '
    for i, step in enumerate(new_steps):
        if step:
            print str(i+1)+'. ', step

    return new_instructions, new_steps
