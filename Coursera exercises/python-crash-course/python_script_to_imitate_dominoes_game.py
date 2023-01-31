'''
There's a bunch of fun games you can play with these tiles. In case you're not familiar, each Domino Tiles has two
numbers represented by a collection of dots carved on each half of the tile. The numbers go from zero to six. 
Tiles can be rotated so that each combination of numbers is represented only once in a set of Domino Tiles.
'''
for left in range(7):
    for right in range(left, 7):
        print("[" + str(left)+"|" + str(right) + "]", end=" ")
    print()