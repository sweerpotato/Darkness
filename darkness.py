from __future__ import print_function
import sys

class Direction:
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4
    
def ERROR(s):
    sys.exit("ERROR: " + s)

def check_darkness_size(lines):
    columns = len(lines[0])
    for line in lines:
        if(len(line) != columns):
            ERROR("MALFORMED DARKNESS")

def generate_darkness(program):
    lines = program.split("\n")
    check_darkness_size(lines)
    
    darkness = [[char for char in line] for line in lines]
    
    return darkness
    
def navigate(darkness):
    debug = False
    
    value = 0
    direction = Direction.EAST
    increment_mode = True
    ascii = False
    x, y = 0, 0

    #Flipped darkness, real world solution
    while darkness[y][x] != ' ':
        op = darkness[y][x].encode("utf-8")
        
        if(debug is True):
            print("DEBUG: op is " + op.decode("utf-8") + ", x is " + chr(x + 48) + ", y is " + chr(y + 48))
        
        if(op == "█"):
            if(increment_mode is False and value != 0):
                value -= 1
            elif(increment_mode is True):
                value += 1
        elif(op == "▀"):
            increment_mode = True
        elif(op == "▄"):
            increment_mode = False
        elif(op == "■"):
            if(ascii is True):
                print(chr(value))
            else:
                print(value, end = "")
        elif(op == "─"):
            ascii = not ascii
        elif(op == "╬" or op == "┼"):
            if(direction == Direction.NORTH):
                if(value != 0):
                    direction = Direction.EAST
                else:
                    direction = Direction.WEST
            elif(direction == Direction.EAST):
                if(value != 0):
                    direction = Direction.SOUTH
                else:
                    direction = Direction.NORTH
            elif(direction == Direction.SOUTH):
                if(value != 0):
                    direction = Direction.WEST
                else:
                    direction = Direction.EAST
            elif(direction == Direction.WEST):
                if(value != 0):
                    direction = Direction.NORTH
                else:
                    direction = Direction.SOUTH
            if(op == "┼"):
                value = 0
        
        if(debug is True):
            print("DEBUG: DIRECTION IS " + chr(direction + 48))
        
        if(direction == Direction.NORTH):
            y -= 1
        elif(direction == Direction.EAST):
            x += 1
        elif(direction == Direction.SOUTH):
            y += 1
        elif(direction == Direction.WEST):
            x -= 1
    
def main():
    if(len(sys.argv) > 1):
        program = open(sys.argv[-1], "r").read().decode("string-escape").decode("utf-8")
        darkness = generate_darkness(program)
        navigate(darkness)
    else:
        ERROR("EXPECTED FILE")

if __name__ == '__main__':
    main()