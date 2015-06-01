"""
[2015-04-27] Challenge #212 [Easy] Rövarspråket 

Description 

When we Swedes are young, we are taught a SUPER-SECRET language that only kids 
know, so we can hide secrets from our confused parents. This language is known 
as "Rövarspråket" (which means "Robber's language", more or less), and is 
surprisingly easy to become fluent in, at least when you're a kid. Recently, 
the cheeky residents of /r/Sweden decided to play a trick on the rest on 
reddit, and get a thread entirely in Rövarspråket to /r/all. The results were 
hilarious. Rövarspråket is not very complicated: you take an ordinary word 
and replace the consonants with the consonant doubled and with an "o" in 
between. So the consonant "b" is replaced by "bob", "r" is replaced with "ror", 
"s" is replaced with "sos", and so on. Vowels are left intact. It's made for 
Swedish, but it works just as well in English. Your task today is to write a 
program that can encode a string of text into Rövarspråket. (note: this is a 
higly guarded Swedish state secret, so I trust that none of you will share this 
very privileged information with anyone! If you do, you will be extradited to 
Sweden and be forced to eat surströmming as penance.) (note 2: surströmming 
is actually not that bad, it's much tastier than its reputation would suggest! 
I'd go so far as to say that it's the tastiest half-rotten fish in the world!) 
Formal inputs & outputs 

Input 

You will recieve one line of input, which is a text string that should be 
encoded into Rövarspråket. Output 

The output will be the encoded string. A few notes: your program should be able 
to handle case properly, which means that "Hello" should be encoded to 
"Hohelollolo", and not as "HoHelollolo" (note the second capital "H"). Also, 
since Rövarspråket is a Swedish invention, your program should follow Swedish 
rules regarding what is a vowel and what is a consonant. The Swedish alphabet 
is the same as the English alphabet except that there are three extra 
characters at the end (Å, Ä and Ö) which are all vowels. In addition, Y is 
always a vowel in Swedish, so the full list of vowels in Swedish is A, E, I, O, 
U, Y, Å, Ä and Ö. The rest are consonants. Lastly, any character that is not 
a vowel or a consonant (i.e. things like punctuation) should be left intact in 
the output. Example inputs 

Input 1 

Jag talar Rövarspråket! Output 1 

Jojagog totalolaror Rorövovarorsospoproråkoketot! Input 2 

I'm speaking Robber's language! Output 2 

I'mom sospopeakokinongog Rorobobboberor'sos lolanongoguagoge! Challenge inputs 

Input 1 

Tre Kronor är världens bästa ishockeylag. Input 2 

Vår kung är coolare än er kung. Bonus 

Make your program able to decode a Rövarspråket-encoded sentence as well as 
encode it. Notes 

This excellent problem (which filled my crusty old Swedish heart with glee) was 
suggested by /u/pogotc. Thanks so much for the suggestion! If you have an idea 
for a problem, head on over to /r/dailyprogrammer_ideas and post your 
suggestion! If it's good idea, we might use it, and you'll be as cool as 
/u/pogotc. 

"""

import string
import random

CONSONANTS = 'BCDFGHJKLMNPQRSTVWXZ'
VOWELS = 'aeiouyåäö'

def encode(input):
    output = []
    for char, next_char in zip(input, input[1:] + ' '):
        if char in CONSONANTS:
            if next_char in (VOWELS+CONSONANTS).lower():
                output.append(char + 'o' + char.lower())
            else:
                output.append(char + 'O' + char)            
        elif char in CONSONANTS.lower():
            output.append(char + 'o' + char)
        else:
            output.append(char)
    return ''.join(output)
    
def decode(input):
    output = []
    size = len(input)
    i = 0
    while i < size:
        output.append(input[i])
        # TODO: check for malformed input?
        if i <= size - 3 and input[i].upper() in CONSONANTS:
            i += 3
        else:
            i += 1
    return ''.join(output)

def encode_tests():
    assert encode('AEIOUYÅÄÖ') == 'AEIOUYÅÄÖ', 'Upper vowels'
    assert encode('aeiouyåäö') == 'aeiouyåäö', 'Lower vowels'
    assert encode('BCDFGHJKLMNPQRSTVWXZ') == 'BOBCOCDODFOFGOGHOHJOJKOKLOLMOMNONPOPQOQRORSOSTOTVOVWOWXOXZOZ', 'Upper consonants'
    assert encode('bcdfghjklmnpqrstvwxz') == 'bobcocdodfofgoghohjojkoklolmomnonpopqoqrorsostotvovwowxoxzoz', 'Lower consonants'
    assert encode('!@#$%¨&*()_+-=[]{}~^,<.>;:/?') == '!@#$%¨&*()_+-=[]{}~^,<.>;:/?', 'Other characters'
    assert encode('BCD') == 'BOBCOCDOD', 'Upper case'
    assert encode('BOB') == 'BOBOBOB', 'Upper case vowels and consonants'
    assert encode('BOB.') == 'BOBOBOB.', 'Ending in punctuation 1'
    assert encode('XYZ!') == 'XOXYZOZ!', 'Ending in punctuation 2'
    assert encode('XWZ$') == 'XOXWOWZOZ$', 'Ending in punctuation 3'
    assert encode('bcd') == 'bobcocdod', 'Lower case'
    assert encode('BcD') == 'BobcocDOD', 'Mixed case'
    assert encode('Hello') == 'Hohelollolo', 'Mixed hello'
    assert encode('mad') == 'momadod', 'Mad case 1'
    assert encode('maD') == 'momaDOD', 'Mad case 2'
    assert encode('mAd') == 'momAdod', 'Mad case 3'
    assert encode('mAD') == 'momADOD', 'Mad case 4'
    assert encode('Mad') == 'Momadod', 'Mad case 5'
    assert encode('MaD') == 'MomaDOD', 'Mad case 6'
    assert encode('MAd') == 'MOMAdod', 'Mad case 7'
    assert encode('MAD') == 'MOMADOD', 'Mad case 8'    
    assert encode('Jag talar Rövarspråket!') == 'Jojagog totalolaror Rorövovarorsospoproråkoketot!', 'Example 1'
    assert encode("I'm speaking Robber's language!") == "I'mom sospopeakokinongog Rorobobboberor'sos lolanongoguagoge!", 'Example 2'
    assert encode("Tre Kronor är världens bästa ishockeylag.") == "Totrore Kokrorononoror äror vovärorloldodenonsos bobäsostota isoshohocockokeylolagog.", "Challenge 1"
    assert encode("Vår kung är coolare än er kung.") == "Vovåror kokunongog äror cocoololarore änon eror kokunongog.", "Challenge 2"    
    print('All encode tests passed!')

def decode_tests():
    assert decode('AEIOUYÅÄÖ') == 'AEIOUYÅÄÖ', 'Upper vowels'
    assert decode('aeiouyåäö') == 'aeiouyåäö', 'Lower vowels'
    assert decode('BOBCOCDODFOFGOGHOHJOJKOKLOLMOMNONPOPQOQRORSOSTOTVOVWOWXOXZOZ') == 'BCDFGHJKLMNPQRSTVWXZ', 'Upper consonants'
    assert decode('bobcocdodfofgoghohjojkoklolmomnonpopqoqrorsostotvovwowxoxzoz') == 'bcdfghjklmnpqrstvwxz', 'Lower consonants'
    assert decode('!@#$%¨&*()_+-=[]{}~^,<.>;:/?') == '!@#$%¨&*()_+-=[]{}~^,<.>;:/?', 'Other characters'
    assert decode('BOBCOCDOD') == 'BCD', 'Upper case'
    assert decode('BOBOBOB') == 'BOB', 'Upper case vowels and consonants'
    assert decode('BOBOBOB.') == 'BOB.', 'Ending in punctuation 1'
    assert decode('XOXYZOZ!') == 'XYZ!', 'Ending in punctuation 2'
    assert decode('XOXWOWZOZ$') == 'XWZ$', 'Ending in punctuation 3'
    assert decode('bobcocdod') == 'bcd', 'Lower case'
    assert decode('BobcocDOD') == 'BcD', 'Mixed case'
    assert decode('Hohelollolo') == 'Hello', 'Mixed hello'
    assert decode('momadod') == 'mad', 'Mad case 1'
    assert decode('momaDOD') == 'maD', 'Mad case 2'
    assert decode('momAdod') == 'mAd', 'Mad case 3'
    assert decode('momADOD') == 'mAD', 'Mad case 4'
    assert decode('Momadod') == 'Mad', 'Mad case 5'
    assert decode('MomaDOD') == 'MaD', 'Mad case 6'
    assert decode('MOMAdod') == 'MAd', 'Mad case 7'
    assert decode('MOMADOD') == 'MAD', 'Mad case 8'
    assert decode('Jojagog totalolaror Rorövovarorsospoproråkoketot!') == 'Jag talar Rövarspråket!', 'Example 1'
    assert decode("I'mom sospopeakokinongog Rorobobboberor'sos lolanongoguagoge!") == "I'm speaking Robber's language!", 'Example 2'
    assert decode("Totrore Kokrorononoror äror vovärorloldodenonsos bobäsostota isoshohocockokeylolagog.") == "Tre Kronor är världens bästa ishockeylag.", "Challenge 1"
    assert decode("Vovåror kokunongog äror cocoololarore änon eror kokunongog.") == "Vår kung är coolare än er kung.", "Challenge 2"
    print('All decode tests passed!')
    
def encode_decode_tests():
    tests = [
        'AEIOUYÅÄÖ',
        'aeiouyåäö',
        'BCDFGHJKLMNPQRSTVWXZ',
        'bcdfghjklmnpqrstvwxz',
        '!@#$%¨&*()_+-=[]{}~^,<.>;:/?',
        'BCD',
        'BOB',
        'BOB.',
        'XYZ!',
        'XWZ$',
        'bcd',
        'BcD',
        'Hello',
        'Jag talar Rövarspråket!',
        "I'm speaking Robber's language!",
        "Tre Kronor är världens bästa ishockeylag.",
        "Vår kung är coolare än er kung.",
    ]
    for test in tests:
        assert decode(encode(test)) == test, 'decode(encode(a)) == a should match!'
    print('All encode/decode tests passed!')

def random_tests():
    for _ in range(500):
        test = ''.join([random.choice(string.printable) for _ in range(200)])
        assert decode(encode(test)) == test, 'Failed at random string: %r' % test
    print('All random string tests passed!')
    
encode_tests()
decode_tests()
encode_decode_tests()
random_tests()

