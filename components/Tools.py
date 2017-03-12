import nltk
import re
import WebScraper
import Ingredients
from pyStatParser.stat_parser import Parser

# ingredients = ['potatoes', 'water', 'vegetable', 'oil', 'onion',
#                            'garlic', 'cumin', 'cayenne', 'pepper', 'curry',
#                            'powder', 'garam', 'masala', 'ginger', 'salt',
#                            'tomatoes', 'garbanzo', 'beans', 'peas', 'coconut',
#                            'milk']

# ingredients = ['olive', 'oil', 'cloves', 'garlic', 'hot', 'red', 'pepper', 'flakes', 'chicken', 'breast',
            #    'marinara', 'sauce', 'basil', 'mozzarella', 'cheese', 'parmesan', 'croutons']

utensils = ['pot', 'pan', 'skillet', 'sheet', 'dish', 'oven', 'rice cooker', 'pressure', 'cooker'
            'grater', 'whisk', 'spoon', 'fork', 'knife', 'tongs', 'spatula', 'peeler', 'thermometer', 'funnel',
            'knife', 'baking', 'dish']

def getListIngredients():
    '''
    Outputs an array of the ingredient names.
    Output: ['parmesan cheese', 'potatoes']
    '''

    ingredients_raw = WebScraper.findElementsByClassName("span", "recipe-ingred_txt")
    ingredientsList = list(map(lambda x: x.getText(), ingredients_raw))
    allIngredients = []
    for ingredient in ingredientsList:
      allIngredients.append(Ingredients.determineIngredients(ingredient)["name"])

    return allIngredients

def ingredientsSeparated(allIngredients):
    '''
    Outputs an array of the ingredient names broken down by whitespace, if any.
    Output: ['parmesan', 'cheese', 'potatoes']
    '''
    separatedIngredients = []
    for ingredient in allIngredients:
        separatedIngredients.extend(ingredient.split())

    return separatedIngredients

allIngredients = getListIngredients()
ingredients = ingredientsSeparated(allIngredients)

def getDirections():
    '''
    Pulls direction from recipe defined in WebScraper.py and returns a flat list of all "steps",
    delineated by '.' or ';'.
    :return: List of strings where each element is a step/sentence of the directions.
    '''
    directions_raw = WebScraper.findElementsByClassName("span", "recipe-directions__list--item")
    len_directs = len(directions_raw)
    directions_raw = directions_raw[:len_directs - 1]
    directions = list(map(lambda x: x.getText(), directions_raw))

    nested_directions = [re.split('\.|;', direction) for direction in directions]
    steps = [step.lstrip() for direction in nested_directions for step in direction if step]
    return steps
#
# def tagSteps(steps):
#     '''
#     Given list of "steps", return a part-of-speech-tagged representation of the directions
#     Note: prepends 'you' onto every phrase prior to tagging to maintain command structure
#     :param steps:  List of strings where each element is a step/sentence of the directions.
#     :return: List of List of Tuples of word and part of speech tag
#     '''
#     tagged_steps = [None]*len(steps)
#     for i, step in enumerate(steps):
#         tokens = nltk.word_tokenize(step)
#         if step:
#             tokens.insert(0, u'You')
#         pos = nltk.pos_tag(tokens)
#         tagged_steps[i] = pos
#     return tagged_steps

# def chunkSteps(taggedSteps):
#     patterns = r"""
#                 NP: {<DT>*<JJ>*<NN|NNS|NNP|PRP>+}
#                     {<NP>+<CC|,>+<NP>+}
#                 VP: {<VB.*><TO>*<IN>*<DT|PDT|RB>*<NP>}
#                     {<VB.*><PP>}
#                 PP: {<IN|TO><CD|DT>*<NP>}
#                 STEP: {<NP><VP>}"""
#
#     cp = nltk.RegexpParser(patterns)
#     chunked_steps = [None]*len(taggedSteps)
#
#     for i, step in enumerate(taggedSteps):
#         chunked_steps[i] = cp.parse(step)
#
#     return chunked_steps

def stat_parse(steps):
    stop_words = ['is', 'and']

    vp_steps = []

    dict_steps = []
    for step in steps:
        # Extracting steps from each step, and putting into dictionary describing step
        step_dict = {}
        step = 'You ' + step[0].lower() + step[1:]
        split_steps = step.split(' ')
        time_idxs = [idx for idx, word in enumerate(split_steps) if word in ['second', 'seconds', 'minute', 'minutes', 'hour', 'hours']]
        times = [split_steps[idx - 1] + split_steps[idx] for idx in time_idxs]
        step_dict['time'] = times

        # Parsing sentence structure from each step and putting in array steps
        parser = Parser()
        direction_tree = parser.parse(step)

        # extracting verb phrases from each step and putting into distinct array
        for i in direction_tree.subtrees():

            if i.label() == 'VP':
                vp_list = i.leaves()
                if vp_list[0] in stop_words:
                    pass
                else:
                    vp_steps.append(i)
                    dict_steps.append(step_dict)

    for idx, vp_step in enumerate(vp_steps):
        for child in vp_step:
            if child.label() == 'VB' or child.label == 'VBP':
                method = child.leaves()[0]
                dict_steps[idx]['method'] = method
            else:
                rest = child.leaves()[1:]
                step_ing = [x for x in rest if x.lower() in ingredients]
                dict_steps[idx]['ingredients'] = step_ing
                pos_rest = child.pos()[1:]

    print dict_steps







    # def listTools(taggedSteps, ingredients):


# '''
#     Given the directions and ingredients, produce candidates (nouns) for tools needed in recipe
#     :param taggedSteps: pos-tagged representation of the recipe directions (List of lists)
#     :param ingredients: list of identity words for recipe ingredients
#     :return: List of strings -- tools
#     '''
#     all_nouns = [None]
#
#     for i, step in enumerate(taggedSteps):
#         nouns = list(filter(lambda x: re.match('NN*', x[1]), step))
#         nouns = [x[0] for x in nouns]
#         all_nouns = all_nouns + nouns
#
#     all_nouns = set(all_nouns)
#     all_nouns = [x for x in all_nouns if x]
#     print all_nouns
#     not_ingredients = [x for x in all_nouns if x.lower() not in ingredients]
#     tools = [x for x in not_ingredients if x.lower() in utensils]
#     return tools
#

# def getMethods(steps, ingredients):
#     commands = []
#
#     for step in steps:
#         tokens = nltk.word_tokenize(step)
#         commands.append(tokens[0])
#
#     commands = [x for x in commands if x]
#     not_ingredients = [x for x in commands if x.lower() not in ingredients]
#     methods = [x for x in not_ingredients if x.lower() not in utensils]
#     return methods



def main():
    steps = getDirections()
    stat_parse(steps)
# print getMethods(steps, ingredients)
# tagged = tagSteps(steps)
# tools = listTools(tagged, ingredients)
