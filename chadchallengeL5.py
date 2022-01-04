#!/usr/bin/env python3
char_name = input("Which character do you want to know about? (Flash, Batman, Superman)").lower
char_stat = input("What statistic do you want to know about? (strength, speed, or intelligence)").lower
charlist =  {"flash":
                {"speed": "fastest", "intelligence": "lowest", "strength": "lowest"}, 
            "batman":
                {"speed": "slowest", "intelligence": "Highest", "strength": "Money"}, 
            "superman":
                {"speed": "fast", "intelligence": "average", "strength": "strongest"}}

#Following command replaced by adding .lower to end of input
#print(charlist[char_name.lower()][char_stat.lower()])


print(f"{char_name()}'s {char_stat()} {charlist[char_name()][char_stat()]}")




