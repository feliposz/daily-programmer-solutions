"""
[2015-05-06] Challenge #213 [Intermediate] The Lazy Typist
http://www.reddit.com/r/dailyprogrammer/comments/351b0o/20150506_challenge_213_intermediate_the_lazy/
"""

import re

KEYBOARD_LAYOUT = """
qwertyuiop
asdfghjkl
^zxcvbnm ^
   #####
"""

print(KEYBOARD_LAYOUT)

pos_key = {}
key_pos = {}
for y, line in enumerate(KEYBOARD_LAYOUT.split('\n')):
    if len(line) == 0:
        continue
    for x, key in enumerate(line):
        pos_key[x,y] = key
        key_pos[key] = key_pos.get(key, [])
        key_pos[key].append((x, y))

def manhattan_distance(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x1-x2)+abs(y1-y2)

def nearest_pos(pos, key):
    x, y = pos
    best_x, best_y, best_dist = None, None, None
    for x2, y2 in key_pos[key]:
        dist = manhattan_distance((x, y), (x2, y2))
        if not best_dist or dist < best_dist:
            best_dist, best_x, best_y = dist, x2, y2
    return (best_dist, (best_x, best_y))

def text_to_keystrokes(text):    
    return re.sub(r'([A-Z])', r'^\1', text).lower().replace(' ', '#')

def key_name(key):
    if key == '#':
        return 'Space'
    elif key == '^':
        return 'Shift'
    else:
        return key.upper()

def hand_name(hand):
    return {'L': 'left', 'R': 'right'}[hand]

def typing_plan(keystrokes):
    plan = []
    left_hand, right_hand = None, None
    force_hand = ' '
    for key in keystrokes:
        if not left_hand:
            left_hand = key_pos[key][0]            
            plan.append(('L', key, None, 0))
        elif not right_hand:
            right_hand = key_pos[key][0]
            plan.append(('R', key, None, 0))
        else:
            left_effort, new_left_pos = nearest_pos(left_hand, key)
            right_effort, new_right_pos = nearest_pos(right_hand, key)            
            if left_effort == 0:
                plan.append(('L', key, pos_key[left_hand], 0))
            elif right_effort == 0:
                plan.append(('R', key, pos_key[right_hand], 0))
            elif (left_effort < right_effort and force_hand != 'R') or force_hand == 'L':
                plan.append(('L', key, pos_key[left_hand], left_effort))
                left_hand = new_left_pos
            else:
                plan.append(('R', key, pos_key[right_hand], right_effort))
                right_hand = new_right_pos
        if key == '^':
            if plan[-1][0] == 'L':
                force_hand = 'R'
            else:
                force_hand = 'L'
        else:
            force_hand = ' '
    return plan

def plan_text(plan):
    plan_text = []
    total_effort = 0
    for step in plan:
        hand, new_key, old_key, effort = step
        total_effort += effort
        if old_key == None:
            plan_text.append('%s: Use %s hand' % (key_name(new_key), hand_name(hand)))
        elif old_key == new_key:
            plan_text.append('%s: Use %s hand again' % (key_name(new_key), hand_name(hand)))
        else:
            plan_text.append('%s: Move %s hand from %s (effort: %d)' % 
                (key_name(new_key), hand_name(hand), key_name(old_key), effort))
    plan_text.append('Total effort: %d' % total_effort)
    return plan_text

def print_typing_plan(text):
    print('\n'.join(plan_text(typing_plan(text_to_keystrokes(text)))))
    
assert text_to_keystrokes('hello world') == 'hello#world'
assert text_to_keystrokes('qpalzm woskxn') == 'qpalzm#woskxn'
assert text_to_keystrokes('The quick brown Fox') == '^the#quick#brown#^fox'
assert text_to_keystrokes('Hello there DailyProgrammers') == '^hello#there#^daily^programmers'
assert text_to_keystrokes('QPgizm QFpRKbi Qycn') == '^q^pgizm#^q^fp^r^kbi#^qycn'

texts = [
    'The quick brown Fox',
    'hello world',
    'qpalzm woskxn',
    'Hello there DailyProgrammers',
    'QPgizm QFpRKbi Qycn'
]
for i, text in enumerate(texts):
    print('\nInput %d: %s' % (i, text))
    print_typing_plan(text)
