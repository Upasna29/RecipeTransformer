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

    ingredients_raw = WebScraper.findElementsByClassName("span", "recipe-ingred_txt")
    ingredients_raw = list(map(lambda x: x.getText(), ingredients_raw))
    ingredients = []
    for ingredient in ingredients_raw:
        if ingredient == 'Add all ingredients to list':
            pass
        else:
            ingredients.append(Ingredients.determineIngredients(ingredient)["name"])


    return steps, ingredients


def stat_parse(steps, ingredients):
    stop_words = ['is', 'and', 'to', 'time']

    vp_steps = []

    separatedIngredients = []
    for ingredient in ingredients:
        ingredient = ingredient.replace('(' ,'').replace(')', '')
        separatedIngredients.extend(ingredient.split())

    dict_steps = []
    for step in steps:
        # Extracting steps from each step, and putting into dictionary describing step
        step_dict = {}
        if step[0:2] != 'In' and step[0:4] != 'With':
            step = 'You ' + step[0].lower() + step[1:]
        split_steps = step.split(' ')
        time_idxs = [idx for idx, word in enumerate(split_steps) if word in ['second', 'seconds', 'minute', 'minutes', 'hour', 'hours']]
        times = [split_steps[idx - 1] + ' ' + split_steps[idx] for idx in time_idxs]
        step_dict['time'] = times

        tools = [x for x in split_steps if x in utensils]
        step_dict['tools'] = tools

        step_ing = [x for x in split_steps if x in separatedIngredients]
        step_dict['ingredients'] = list(set(step_ing))

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
            if child.label() == 'VB' or child.label() == 'VBP':
                method = child.leaves()[0]
                dict_steps[idx]['method'] = [method]

    return dict_steps

def remove_duplicates(seq):
   # not order preserving
   set = {}
   map(set.__setitem__, seq, [])
   return set.keys()

def tools():
    '''
    From command line input, print all tools involved for recipe
    :Output: Tools found in recipe
    '''
    steps, ingredients = getDirections()
    dict_steps = stat_parse(steps, ingredients)
    tools = []
    for step in dict_steps:
        tools = tools + step['tools']
    tools = remove_duplicates(tools)
    print 'Tools: ', ', '.join(tools)

def steps():
    steps, ingredients = getDirections()
    dict_steps = stat_parse(steps, ingredients)
    print dict_steps
    for i, step in enumerate(dict_steps):
        print 'Step ', str(i)
        for component in step:
            if step[component]:
                print component, ": ", ' '.join(step[component])

        print '\n'

def methods():
    '''
    From command line input, print all tools involved for recipe
    :Output: Tools found in recipe
    '''
    steps, ingredients = getDirections()
    dict_steps = stat_parse(steps, ingredients)
    methods = []
    for step in dict_steps:
        try:
            methods = methods + step['method']
        except:
            continue
    methods = remove_duplicates(methods)
    print 'Methods: ', ', '.join(methods)


