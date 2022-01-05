#!/usr/bin/env python3

#Dictionary to establish questions and answers
#Would like to move this to its own file and import the data into the code
quiz = {
        1: {"question": "What is War Machine\'s first name?", "answer": "james"},
        2: {"question": "What country is the scarlet witch from?", "answer": "sokovia"},
        3: {"question": "What is the first name of Tony Stark's daughter?", "answer": "morgan"},
        4: {"question": "Peter Quill's father is considered what type of being?", "answer": "celestial"},
        5: {"question": "What was the acronym for the agency that imprisoned Loki?", "answer": "tva"},
        6: {"question": "What city was Steve Roger's from", "answer": "brooklyn"},
        7: {"question": "What type of doctor is Michael Morbius?", "answer": "biochemist"},
        8: {"question": "On what planet does the soul stone reside?", "answer": "volmir"},
        9: {"question": "What fruit is Pepper Potts allergic to?", "answer": "strawberries"},
        10: {"question": "What is the Winter Soldiers middle name?", "answer": "buchanan"}
        }
#Establishes score and sets it to zero.
score = 0

#Begins if statements with nested while loops to start the quiz
#Would like to condense this to a single set that increases the dict integer after each comepletion to minimize code
print("There are 10 questions total and you get three guesses per question. Good Luck!!!")
counter = 0
print(quiz[1]['question'])
while counter < 3:
    answer = input("Make your choice >>>> ")
    if answer.lower == quiz[1]['answer']:
        print("Correct!")
        score += 1
        break
    else:
        print("That is incorrect. Try Again")
        counter += 1

counter = 0
print(quiz[2]['question'])
while counter < 3:
    answer = input("Make your choice >>>> ")
    if answer.lower == quiz[2]['answer']:
        print("Correct!")
        score += 1
        break
    else:
        print("That is incorrect. Try Again")
        counter += 1

counter = 0
print(quiz[3]['question'])
while counter < 3:
    answer = input("Make your choice >>>> ")
    if answer.lower == quiz[3]['answer']:
        print("Correct!")
        score += 1
        break
    else:
        print("That is incorrect. Try Again")
        counter += 1

counter = 0
print(quiz[4]['question'])
while counter < 3:
    answer = input("Make your choice >>>> ")
    if answer.lower == quiz[4]['answer']:
        print("Correct!")
        score += 1
        break
    else:
        print("That is incorrect. Try Again")
        counter += 1

counter = 0
print(quiz[5]['question'])
while counter < 3:
    answer = input("Make your choice >>>> ")
    if answer.lower == quiz[5]['answer']:
        print("Correct!")
        score += 1
        break
    else:
        print("That is incorrect. Try Again")
        counter += 1

counter = 0
print(quiz[6]['question'])
while counter < 3:
    answer = input("Make your choice >>>> ")
    if answer.lower == quiz[6]['answer']:
        print("Correct!")
        score += 1
        break
    else:
        print("That is incorrect. Try Again")
        counter += 1

counter = 0
print(quiz[7]['question'])
while counter < 3:
    answer = input("Make your choice >>>> ")
    if answer.lower == quiz[7]['answer']:
        print("Correct!")
        score += 1
        break
    else:
        print("That is incorrect. Try Again")
        counter += 1

counter = 0
print(quiz[8]['question'])
while counter < 3:
    answer = input("Make your choice >>>> ")
    if answer.lower == quiz[8]['answer']:
        print("Correct!")
        score += 1
        break
    else:
        print("That is incorrect. Try Again")
        counter += 1

counter = 0
print(quiz[9]['question'])
while counter < 3:
    answer = input("Make your choice >>>> ")
    if answer.lower == quiz[9]['answer']:
        print("Correct!.")
        score += 1
        break
    else:
        print("That is incorrect. Try Again")
        counter += 1

counter = 0
print(quiz[10]['question'])
while counter < 3:
    answer = input("Make your choice >>>> ")
    if answer.lower == quiz[10]['answer']:
        print("Correct!")
        score += 1
        break
    else:
        print("That is incorrect. Try Again")
        counter += 1

#Code to print ending score and corresponding comments depending on home many questions were correct
if score == 10:
    print("Your Total score was " + str(score) + " out of 10.\nYou really know your Marvel trivia.")
elif score >= 7:
    print("Your Total score was " + str(score) + " out of 10.\nNot too bad of a score but theres room for improvement"),
elif score >= 4:
    print("Your Total score was " + str(score) + " out of 10.\nYou know some stuff but need to watch the films again.")
else:
    print("Your Total score was " + str(score) + " out of 10.\nYou have either never watched the movies or you slept threw them. You really need to watch them in order to improve.")

