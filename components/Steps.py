import nltk
import re
import WebScraper
import Ingredients
from pyStatParser.stat_parser import Parser


utensils = ['pot', 'pan', 'skillet', 'sheet', 'dish', 'oven', 'rice cooker', 'pressure', 'cooker'
            'grater', 'whisk', 'spoon', 'fork', 'knife', 'tongs', 'spatula', 'peeler', 'thermometer', 'funnel',
            'knife', 'baking', 'dish', 'press', 'grater', 'scissors', 'mortar', 'pestle', 'slotted spoon', 'pin',
            'measuring', 'zester', 'funnel', 'sink', 'cakepan', 'board', 'strainer', 'tray', 'blender', 'mitts',
            'bowl', 'grill', 'nutcracker', 'ladle', 'cutter', 'whisk', 'scoop', 'griddle', 'cleaver', 'masher',
            'colander', 'dutch']

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


def stat_parse(steps):
    stop_words = ['is', 'and', 'to', 'time']

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

        tools = [x for x in split_steps if x in utensils]
        step_dict['tools'] = tools

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
            print child
            if child.label() == 'VB' or child.label == 'VBP':
                method = child.leaves()[0]
                dict_steps[idx]['method'] = method
            else:
                rest = child.leaves()[1:]
                rest = [x for x in rest if x not in stop_words]
                step_ing = [x for x in rest if x.lower() in ingredients]
                dict_steps[idx]['ingredients'] = list(set(step_ing))
                pos_rest = child.pos()[1:]

    return dict_steps

def tools(dict_steps):
    '''
    Given parsed recipe steps, return all tools involved for recipe
    :param dict_steps: Dictionary representation of recipe steps as returned by stat_parse
    :return: List of tools found in recipe.
    '''
    tools = []
    for step in dict_steps:
        tools = tools + step['tools']
    return tools



def steps():
    steps = getDirections()
    dict_steps = stat_parse(steps)



