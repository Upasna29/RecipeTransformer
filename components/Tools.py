import nltk
import re
import WebScraper

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
    steps = [step for direction in nested_directions for step in direction if step]
    return steps

def tagSteps(steps):
    '''
    Given list of "steps", return a part-of-speech-tagged representation of the directions
    Note: prepends 'you' onto every phrase prior to tagging to maintain command structure
    :param steps:  List of strings where each element is a step/sentence of the directions.
    :return: List of List of Tuples of word and part of speech tag
    '''
    tagged_steps = [None]*len(steps)
    for i, step in enumerate(steps):
        tokens = nltk.word_tokenize(step)
        if step:
            tokens.insert(0, u'You')
        pos = nltk.pos_tag(tokens)
        tagged_steps[i] = pos
    return tagged_steps

def chunkSteps(taggedSteps):
    patterns = r"""
                NP: {<DT>*<JJ>*<NN|NNS|NNP|PRP>+}
                    {<NP>+<CC|,>+<NP>+}
                VP: {<VB.*><TO>*<IN>*<DT>*<NP>}
                    {<VB.*><PP>}
                PP: {<IN|TO><CD|DT>*<NP>}"""

    cp = nltk.RegexpParser(patterns)
    chunked_steps = [None]*len(taggedSteps)

    for i, step in enumerate(taggedSteps):
        chunked_steps[i] = cp.parse(step)

    return chunked_steps

def listTools(taggedSteps, ingredients):
    '''
    Given the directions and ingredients, produce candidates (nouns) for tools needed in recipe
    :param taggedSteps: pos-tagged representation of the recipe directions (List of lists)
    :param ingredients: list of identity words for recipe ingredients
    :return: List of strings -- tools
    '''
    all_nouns = [None]

    for i, step in enumerate(taggedSteps):
        nouns = list(filter(lambda x: re.match('NN*', x[1]), step))
        nouns = [x[0] for x in nouns]
        all_nouns = all_nouns + nouns

    all_nouns = set(all_nouns)

    return [x for x in all_nouns if x not in ingredients]


steps = getDirections()
tagged = tagSteps(steps)
print tagged
tools = listTools(tagged, ['potatoes', 'water', 'vegetable', 'oil', 'onion',
                           'garlic', 'cumin', 'cayenne', 'pepper', 'curry',
                           'powder', 'garam', 'masala', 'ginger', 'salt',
                           'tomatoes', 'garbanzo', 'beans', 'peas', 'coconut',
                           'milk'])

print tools