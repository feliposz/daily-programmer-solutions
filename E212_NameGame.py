"""
[2015-04-20] Challenge #211 [Easy] The Name Game

Description

If computer programmers had a "patron musician" (if such a thing even exists), it would
surely be the great Shirley Ellis. It is my opinion that in the history of music, not song
has ever come closer to replicating the experience of programming as her 1964 novelty hit
The Name Game. In the lyrics of that song she lays out quite an elegant and fun algorithm
for making a rhyme out of anybody's name. The lyrics are almost like sung pseudo-code!
Your challenge today will be to implement a computer program that can play Ms. Ellis' Name
Game. You will recieve a name for input, and output the rhyme for that name. It should be
noted that while the rhyming algorithm is very elegant and easy for humans to follow, Ms.
Ellis description is not quite rigorous. For instance, there's an extra rule that she
doesn't mention that only applies when names start with a vowel (such as "Arnold"), and
it's not quite clear exactly what you should do when the names start with M, F or B. You
will have to fill in the blanks as best you can on your own. If you're not sure how a
specific rule goes, implement what sounds best to you. You should primarily refer to the
song for instructions, but I've includeded the relevant lyrics here:

Come on everybody! I say now let's play a game I betcha I can make a rhyme out of
anybody's name The first letter of the name, I treat it like it wasn't there But a "B" or
an "F" or an "M" will appear And then I say "bo", add a "B", then I say the name and
"Bonana fanna" and a "fo" And then I say the name again with an "F" very plain and a "fee
fy" and a "mo" And then I say the name again with an "M" this time and there isn't any
name that I can't rhyme But if the first two letters are ever the same, I drop them both
and say the name like Bob, Bob drop the B's "Bo-ob" For Fred, Fred drop the F's "Fo-red"
For Mary, Mary drop the M's Mo-ary That's the only rule that is contrary.

Formal Inputs & Outputs

Input description

Your input will be a single line with a single name on it. Note that in all the
excitement, an exclamation point has been added to the end. Output description

The rhyme of the name!

Example Inputs & Outputs

Examples helpfully provided by Ms. Ellis herself.

Example 1

Lincoln!

Output 1

Lincoln, Lincoln bo Bincoln,
Bonana fanna fo Fincoln,
Fee fy mo Mincoln,
Lincoln!

2

Nick!

Output 2

Nick, Nick bo Bick,
Bonana fanna fo Fick,
Fee fy mo Mick,
Nick!

Challenge input

Input 1

Arnold!

Input 2

Billy!

Input 3

Your username! Or even, if you feel comfortable sharing it, your real name! Or even my
name! Or whatever! I've listened to this music video, like, six times in a row while
writing this challenge, and all I want to do is dance!

Finally

Have a good challenge idea? Consider submitting it to /r/dailyprogrammer_ideas
"""

def name_game_rhyme(name):
    name = name.strip('!').strip().capitalize()
    first_letter = name[0]
    if first_letter in 'AEIOU':
        rest = name.lower()
    elif name.startswith('Sh'):
        rest = name[2:]
    else:
        rest = name[1:]
    bname = rest if first_letter == 'B' else 'B'+rest
    fname = rest if first_letter == 'F' else 'F'+rest
    mname = rest if first_letter == 'M' else 'M'+rest
    rhyme = [
        '%s, %s bo %s' % (name, name, bname),
        'Bonana fanna fo %s' % fname,
        'Fee fy mo %s' % mname,
        '%s!' % name
    ]
    return ',\n'.join(rhyme)

def tests():
    assert name_game_rhyme('Lincoln!') == 'Lincoln, Lincoln bo Bincoln,\nBonana fanna fo Fincoln,\nFee fy mo Mincoln,\nLincoln!', 'Lincoln test'
    assert name_game_rhyme('Nick!') == 'Nick, Nick bo Bick,\nBonana fanna fo Fick,\nFee fy mo Mick,\nNick!', 'Nick test'
    assert name_game_rhyme('Billy!') == 'Billy, Billy bo illy,\nBonana fanna fo Filly,\nFee fy mo Milly,\nBilly!', 'Billy test'
    assert name_game_rhyme('Katie!') == 'Katie, Katie bo Batie,\nBonana fanna fo Fatie,\nFee fy mo Matie,\nKatie!', 'Katie test'
    assert name_game_rhyme('Fred!') == 'Fred, Fred bo Bred,\nBonana fanna fo red,\nFee fy mo Mred,\nFred!', 'Fred test'
    assert name_game_rhyme('Marsha!') == 'Marsha, Marsha bo Barsha,\nBonana fanna fo Farsha,\nFee fy mo arsha,\nMarsha!', 'Marsha test'
    assert name_game_rhyme('Nick!') == 'Nick, Nick bo Bick,\nBonana fanna fo Fick,\nFee fy mo Mick,\nNick!', 'Nick test'
    assert name_game_rhyme('Tony!') == 'Tony, Tony bo Bony,\nBonana fanna fo Fony,\nFee fy mo Mony,\nTony!', 'Tony test'
    assert name_game_rhyme('Judy!') == 'Judy, Judy bo Budy,\nBonana fanna fo Fudy,\nFee fy mo Mudy,\nJudy!', 'Judy test'
    assert name_game_rhyme('Lana!') == 'Lana, Lana bo Bana,\nBonana fanna fo Fana,\nFee fy mo Mana,\nLana!', 'Lana test'
    assert name_game_rhyme('Mary!') == 'Mary, Mary bo Bary,\nBonana fanna fo Fary,\nFee fy mo ary,\nMary!', 'Mary test'
    assert name_game_rhyme('Kit!') == 'Kit, Kit bo Bit,\nBonana fanna fo Fit,\nFee fy mo Mit,\nKit!', 'Kit test'
    assert name_game_rhyme('Pepper!') == 'Pepper, Pepper bo Bepper,\nBonana fanna fo Fepper,\nFee fy mo Mepper,\nPepper!', 'Pepper!'
    assert name_game_rhyme('Bob!') == 'Bob, Bob bo ob,\nBonana fanna fo Fob,\nFee fy mo Mob,\nBob!', 'Bob test'
    assert name_game_rhyme('Arnold!') == 'Arnold, Arnold bo Barnold,\nBonana fanna fo Farnold,\nFee fy mo Marnold,\nArnold!', 'Arnold test'
    assert name_game_rhyme('Shirley!') == 'Shirley, Shirley bo Birley,\nBonana fanna fo Firley,\nFee fy mo Mirley,\nShirley!', 'Shirley test'

def repl():
    while True:
        name = input('Type in a name to rhyme: ')
        if name:
            print(name_game_rhyme(name))
        else:
            break

if __name__ == '__main__':
    tests()
    repl()
