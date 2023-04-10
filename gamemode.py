from modules import readtxt
import random


def game(score):
    nameList = readtxt.openTextFile("instructions/namelist.txt", [])
    isLeave = False
    while True:
        if score > 0:
            personName = random.choice(nameList)
            print(personName)
            userAction = input("Action : ").lower()
            normal_people_greetings = ["Hi", "hi", "HI", "Hello", "HELLO", "hello"]
            cold_people = ["S", "D", "K", "L", ]
            normal_people = ["R", "A", "J"]
            hot_people = ["B", "C", "E", "G", "F", "H", "I", "M", "N", "O", "P", "Q", "T", "U", "V", "W", "X", "Y", "Z"]
            keywords = ["ff", "f", 'w'] + normal_people_greetings

            if not userAction == "exit":
                if userAction in keywords:
                    if personName[0] in cold_people:
                        if userAction == "f":
                            print("Correct")
                            score += 1
                        else:
                            print("Wrong")
                            score -= 1
                    elif personName[0] in normal_people:
                        if userAction in normal_people_greetings:
                            print("Correct")
                            score += 1                
                        else:
                            print("Wrong")
                            score -= 1                
                    elif personName[0] in hot_people:
                        if userAction == "ff":
                            print("Correct")
                            score += 1                
                        else:
                            print("Wrong")
                            score -= 1                
                    else:
                        break
                    print("--------------")
                else:
                    print("Please enter valid keyword")
            else:
                isLeave = True
                print("Exit Game")
                break
    return [score, isLeave]

