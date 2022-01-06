#!/usr/bin/env python3
"""Author: James Freeman | Learning about Functions"""


import crayons

"""functions that have one specific purpose"""

def snork():
 
    # print 'red string' in red
    print(crayons.red('red string'))

    # Red White and Blue text
    print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))



def sloppy():

    # print 'yellow string' in yellow
    print(crayons.yellow('yellow string', bold=True))


    # print 'white string' in white
    print(crayons.white('white string', bold=True))

"""This function prints a line with my name and favorite color with color formatting"""
def tuba():
 
    print(f"My name is " + crayons.red("James") + " and my favorit color is " + crayons.blue("BLUE", bold=True) + " !")



"""This function combines (nests) three functions into a single function"""
def main():
    snork()
    sloppy()
    tuba()

#Calling for the combined function to output all three at once
main()


if __name__ == "__main__":
    main()
