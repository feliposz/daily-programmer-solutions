"""
[Weekly #17] Mini Challenges
http://www.reddit.com/r/dailyprogrammer/comments/2mkh5g/weekly_17_mini_challenges/

So this week mini challenges. Too small for an easy but great for a mini challenge.
Here is your chance to post some good warm up mini challenges.
How it works. Start a new main thread in here. Use my formatting (or close to it) -- if you want to solve a mini challenge you reply off that thread.
Simple. Keep checking back all week as people will keep posting challenges and solve the ones you want.
Please check other mini challenges before posting one to avoid duplications within a certain reason.
"""

import string
import re
import datetime
from collections import defaultdict

def count_letters(str):
    """
    Count it - count the letters in a string.
    Given: A string - like "Hello World"
    Output: Letters and how often they show up. - d:1 e:1 h:1 l:3 o:2 r:1 w:1
    Special: convert all to lowercase. Ignore whitespace and anything not [a-z][A-Z]
    Challenge input: "The quick brown fox jumps over the lazy dog and the sleeping cat early in the day."
    """
    letters = defaultdict(int)
    for c in str.lower():
        if c in string.ascii_lowercase:
            letters[c] += 1
    return letters

rhyme_db = {
    'ack': ['back', 'lack', 'pack', 'rack', 'sack', 'tack', 'yak', 'black', 'knack', 'quack', 'slack', 'smack', 'snack', 'stack', 'track', 'whack', 'attack'],
    'ail': ['bale', 'fail', 'hail', 'mail', 'male', 'nail', 'pail', 'tale', 'rail', 'sail', 'stale', 'scale', 'snail', 'whale', 'detail', 'email'],
    'air': ['air', 'bare', 'care', 'chair', 'dare', 'fair', 'hair', 'pair', 'rare', 'wear', 'chair', 'flare', 'stare', 'scare', 'share', 'spare', 'square', 'there', 'where', 'aware', 'beware', 'compare', 'declare', 'despair', 'prepare', 'repair', 'unfair'],
    'ake': ['ache', 'bake', 'fake', 'lake', 'make', 'rake', 'take', 'brake', 'break', 'flake', 'quake', 'snake', 'steak', 'awake', 'mistake'],
    'all': ['all', 'ball', 'call', 'doll', 'hall', 'fall', 'tall', 'crawl', 'small', 'baseball', 'football'],
    'an': ['an', 'can', 'fan', 'man', 'pan', 'ran', 'tan', 'van', 'plan', 'scan', 'span', 'began'],
    'and': ['and', 'band', 'hand', 'land', 'sand', 'bland', 'command', 'demand', 'expand', 'stand', 'understand'],
    'ap': ['cap', 'gap', 'map', 'nap', 'tap', 'zap', 'chap', 'clap', 'flap', 'slap', 'snap', 'strap', 'trap', 'wrap'],
    'ar': ['are', 'bar', 'car', 'far', 'jar', 'tar', 'star', 'scar', 'afar', 'guitar'],
    'at': ['at', 'bat', 'fat', 'mat', 'pat', 'rat', 'sat', 'flat', 'that', 'splat', 'combat'],
    'ate': ['ate', 'date', 'fate', 'mate', 'late', 'gate', 'rate', 'wait', 'crate', 'great', 'plate', 'skate', 'slate', 'state', 'straight', 'trait', 'weight', 'create'],
    'ed': ['bed', 'dead', 'fed', 'head', 'led', 'read', 'red', 'said', 'bread', 'fled', 'spread', 'thread', 'tread', 'instead'],
    'ell': ['bell', 'fell', 'sell', 'well', 'yell', 'shell', 'smell', 'spell', 'farewell', 'hotel', 'motel'],
    'en': ['den', 'hen', 'men', 'pen', 'ten', 'glen', 'then', 'when', 'wren', 'again'],
    'et': ['bet', 'get', 'jet', 'let', 'met', 'pet', 'set', 'vet', 'wet', 'yet', 'threat', 'barrette', 'reset', 'upset'],
    'in': ['bin', 'chin', 'in', 'pin', 'tin', 'grin', 'thin', 'twin', 'skin', 'begin', 'within'],
    'ing': ['king', 'ring', 'sing', 'wing', 'zing', 'bring', 'cling', 'fling', 'sling', 'spring', 'sting', 'string', 'swing', 'thing'],
    'it': ['bit', 'fit', 'hit', 'it', 'kit', 'lit', 'pit', 'sit', 'flit', 'knit', 'quit', 'skit', 'slit', 'spit', 'split', 'admit', 'commit', 'permit'],
    'ite': ['bite', 'kite', 'bright', 'fight', 'fright', 'knight', 'night', 'might', 'right', 'tight', 'white', 'write', 'delight', 'tonight'],
    'oh': ['go', 'hoe', 'low', 'mow', 'row', 'sew', 'toe', 'blow', 'crow', 'dough', 'flow', 'know', 'glow', 'grow', 'know', 'show', 'slow', 'snow', 'stow', 'though', 'throw', 'ago', 'although', 'below'],
    'ot': ['cot', 'dot', 'got', 'hot', 'lot', 'not', 'pot', 'rot', 'tot', 'bought', 'fought', 'knot', 'taught', 'shot', 'spot', 'squat', 'forgot'],
    'ound': ['crowned', 'found', 'ground', 'hound', 'mound', 'pound', 'round', 'sound', 'wound', 'around', 'surround'],
    'oze': ['bows', 'hose', 'nose', 'rose', 'toes', 'blows', 'flows', 'froze', 'grows', 'those'],
    'ub': ['cub', 'rub', 'sub', 'tub', 'club', 'stub', 'scrub', 'shrub'],
    'un': ['bun', 'fun', 'gun', 'one', 'run', 'son', 'sun', 'ton', 'won', 'done', 'none', 'begun', 'outdone', 'undone'],
}

def rhyme_analyser(str, rhyme_db):
    """
    Rhyme Analyzer - Print out the rhyme scheme of a poem.
    Given: A string - like
    If you want to smell a rose
    You must put it to your nose.
    If you want to eat some bread
    You must not eat it in bed
    Or I will eat your toes.
    Output: Rhyme scheme of the poem. - AABBA
    Use a rhyme list such as this one.
    """
    lines = str.lower().split('\n')
    rhyme_letter = {}
    rhyme_scheme = []
    letter = 'A'
    for line in lines:
        last_word = re.sub('[^a-z]', '', line.split(' ')[-1])
        for rhyme in rhyme_db:
            if last_word in rhyme_db[rhyme]:
                if rhyme not in rhyme_letter:
                    rhyme_letter[rhyme] = letter
                    letter = chr(ord(letter) + 1)
                rhyme_scheme.append(rhyme_letter[rhyme])
    return ''.join(rhyme_scheme)

def islands(array):
    """
    Identify islands In a given array, identify groups ("islands") of identical elements. A group must consist of 2 or more contiguous identical elements.
    Given: An array like: "proogrrrammminggg"
    Output: o, r, m, g
    Challenge output: o:2, r:5, m:9, g:14 (positions of first occurrences of these letters)
    Bonus Do this for a 2d array.
    """
    prev = None
    in_island = False
    output = {}
    for i, a in enumerate(array):
        if a == prev:
            if not in_island:
                output[a] = i-1
            in_island = True
        else:
            in_island = False
        prev = a
    return output
    
def islands2d(w, h, array2d):
    output = {}
    for i in range(h):
        for j in range(w):
            if (j > 0 and array2d[i][j] == array2d[i][j-1]) or (i > 0 and array2d[i][j] == array2d[i-1][j]):
                char = array2d[i][j]
                if char not in output:
                    output[char] = (j+1, i+1)
    return output

def reverse_in_place(array):
    """
    Array Memory Flip:
    Given: An Array of Integers.
    Challenge: We want to reverse the order of the array in memory and you are only allowed the array and 1 integer variable to do this. 
               No pre-canned library calls or frameworks are not allowed. You must do all the work.
    Bonus: Can it be done with just the array and no other allocated storage or variables (outside index counters/pointers are okay but storage wise only the array.
           Cannot just allocate a 2nd array in memory and copy over values)
    """
    for i in range(len(array)//2):
        array[i] += array[-i-1]
        array[-i-1] = array[i] - array[-i-1]
        array[i] -= array[-i-1]
    return array
        
def next_saturday(str_date):
    """
    Saturday Birthday - print the next year in which a given date falls on Saturday.
    Given: a date in string form, e.g. '2002-1-1'.
    Output: the next year for which the provided date falls on Saturday, e.g. '2028-1-1'.
    Special: print the user's age on that date and the time between now and then.
    Challenge: see how many different date input formats you can support.
    """
    year, month, day = (int(x) for x in str_date.split('-'))
    date = datetime.date(year, month, day)
    while True:
        year += 1
        date = date.replace(year=year)
        if date.isoweekday() == 6:
            break
    return date.isoformat()
    
def reverse_int(n):
    """
    Late to the party, but here's a good one.
    Integer Reverse:
    Given: Any random integer in decimal.
    Challenge: Reverse it, without using any of the obvious toString tricks, or transient conversions to a data type other than an int.
    """
    r = 0
    while n > 0:
        r = r * 10 + n % 10
        n //= 10
    return r
    
def test():
    assert count_letters('Hello world!') == { 'd':1, 'e':1, 'h':1, 'l':3, 'o':2, 'r':1, 'w':1 }, 'count_letters hello'
    assert count_letters('The quick brown fox jumps over the lazy dog and the sleeping cat early in the day.') == {'a': 5, 'b': 1, 'c': 2, 'd': 3, 'e': 8, 'f': 1, 'g': 2, 'h': 4, 'i': 3, 'j': 1, 'k': 1, 'l': 3, 'm': 1, 'n': 4, 'o': 4, 'p': 2, 'q': 1, 'r': 3, 's': 2, 't': 5, 'u': 2, 'v': 1, 'w': 1, 'x': 1, 'y': 3, 'z': 1}, 'count_letters quick'
    assert rhyme_analyser('If you want to smell a rose\nYou must put it to your nose.\nIf you want to eat some bread\nYou must not eat it in bed\nOr I will eat your toes.', rhyme_db) == 'AABBA', 'rhyme_analyser'
    assert islands("proogrrrammminggg") == { 'o':2, 'r':5, 'm':9, 'g':14}, 'islands'
    assert islands2d(5, 3, ["proog", "rramg", "rinmg"]) == { 'o':(4,1), 'r':(2,2), 'g':(5,2), 'm':(4,3)}, 'islands2d'
    assert reverse_in_place([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1], 'reverse 1'
    assert reverse_in_place([1, 2, 3, 4, 5, 6]) == [6, 5, 4, 3, 2, 1], 'reverse 2'
    assert reverse_in_place([1, 2]) == [2, 1], 'reverse 3'
    assert reverse_in_place([]) == [], 'reverse 4'
    assert reverse_in_place([1]) == [1], 'reverse 5'
    assert next_saturday('2022-01-01') == '2028-01-01', 'next_saturday'
    assert reverse_int(0) == 0, 'reverse int 1'
    assert reverse_int(1) == 1, 'reverse int 2'
    assert reverse_int(100) == 1, 'reverse int 3'
    assert reverse_int(12345) == 54321, 'reverse int 4'
    assert reverse_int(1020) == 201, 'reverse int 5'
    assert reverse_int(123456789) = 987654321, 'reverse int 6'
 
test()
