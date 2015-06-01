"""
[2015-05-13] Challenge #214 [Intermediate] Pile of Paper

Description

Have you ever layered colored sticky notes in interesting patterns in order to make pictures? You can create surprisingly complex pictures you can make out of square/rectangular pieces of paper. An interesting question about these pictures, though, is: what area of each color is actually showing? We will simulate this situation and answer that question.
Start with a sheet of the base color 0 (colors are represented by single integers) of some specified size. Let's suppose we have a sheet of size 20x10, of color 0. This will serve as our "canvas", and first input:
20 10
We then place other colored sheets on top of it by specifying their color (as an integer), the (x, y) coordinates of their top left corner, and their width/height measurements. For simplicity's sake, all sheets are oriented in the same orthogonal manner (none of them are tilted). Some example input:
1 5 5 10 3
2 0 0 7 7 
This is interpreted as:
Sheet of color 1 with top left corner at (5, 5), with a width of 10 and height of 3.
Sheet of color 2 with top left corner at (0,0), with a width of 7 and height of 7.
Note that multiple sheets may have the same color. Color is not unique per sheet.
Placing the first sheet would result in a canvas that looks like this:
00000000000000000000
00000000000000000000
00000000000000000000
00000000000000000000
00000000000000000000
00000111111111100000
00000111111111100000
00000111111111100000
00000000000000000000
00000000000000000000
Layering the second one on top would look like this:
22222220000000000000
22222220000000000000
22222220000000000000
22222220000000000000
22222220000000000000
22222221111111100000
22222221111111100000
00000111111111100000
00000000000000000000
00000000000000000000
This is the end of the input. The output should answer a single question: What area of each color is visible after all the sheets have been layered, in order? It should be formatted as an one-per-line list of colors mapped to their visible areas. In our example, this would be:
0 125
1 26
2 49
Sample Input:

20 10
1 5 5 10 3
2 0 0 7 7
Sample Output:

0 125
1 26
2 49
Challenge Input

Redditor /u/Blackshell has a bunch of inputs of varying sizes from 100 up to 10000 rectangles up here, with solutions: https://github.com/fsufitch/dailyprogrammer/tree/master/ideas/pile_of_paper
Credit

This challenge was created by user /u/Blackshell. If you have an idea for a challenge, please submit it to /r/dailyprogrammer_ideas and there's a good chance we'll use it!
"""

import sys

class Canvas(object):

    def __init__(self, color, width, height):
        assert width > 0, 'Invalid canvas width'
        assert height > 0, 'Invalid canvas height'
        self.width, self.height = width, height
        self.canvas = []
        for y in range(0, height):            
            row = []
            for x in range(0, width):
                row.append(color)
            self.canvas.append(row)
        
    def place_paper(self, color, x, y, w, h):
        #assert 0 <= x < self.width, 'Invalid x coordinate'
        #assert 0 <= y < self.height, 'Invalid y coordinate'
        #assert 0 <= w <= self.width, 'Invalid w coordinate'
        #assert 0 <= h <= self.height, 'Invalid h coordinate ' + str(h)
        #assert 0 <= x+w <= self.width, 'Invalid width'
        #assert 0 <= y+h <= self.height, 'Invalid height'
        #x2 = x+w if x+w < self.width else self.width-1
        #y2 = y+h if x+h < self.height else self.height-1        
        x2 = x + w
        y2 = y + h
        for _x in range(x, x2):
            for _y in range(y, y2):
                self.canvas[_y][_x] = color

    def show(self):
        for row in self.canvas:
            print(''.join(row))

    def get_color_areas(self):
        color_areas = {}
        for row in self.canvas:
            for cell_color in row:
                color_areas[cell_color] = color_areas.get(cell_color, 0) + 1
        return color_areas

def test():
    canvas = Canvas('0', 20, 10)
    canvas.place_paper('1', 5, 5, 10, 3)
    canvas.place_paper('2', 0, 0, 7, 7)
    assert canvas.get_color_areas() == {'0': 125, '1': 26, '2': 49}, 'Test pile of paper'
    print('All tests passed.')
    
if __name__ == '__main__':
    if len(sys.argv) < 2:
        test()
        exit(0)
    filename = sys.argv[1]
    print(filename)
    with open(filename, 'r') as f:
        width, height = map(int, f.readline().split())
        canvas = Canvas(0, width, height)
        for line in f.readlines():
            color, x, y, w, h = map(int, line.split())
            canvas.place_paper(color, x, y, w, h)
    color_areas = canvas.get_color_areas()
    for color, area in sorted(color_areas.items()):
        print('%s %d' % (color, area))
    #print('Total area = %d' % sum(color_areas.values()))
