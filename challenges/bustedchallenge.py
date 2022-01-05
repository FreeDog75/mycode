#!/usr/bin/python3

def main():

    nums = [1, 2, 3, 4, 5]
    words = {
            "verb": "sprint",
            "adjective": "awesome",
            "noun": "Python",
            }

    name = input("What is your name? \n")

    # Hi <name>! Welcome to Day 2 of Python Training!
    print("Hi " + name.capitalize() + "! Welcome to Day " + str(nums[1]) + " of " + words['noun'] + " Training!")

main()
