from time import sleep
from modules import readtxt


def userEnterValidation():
    welcometxt = readtxt.openTextFile("instructions/welcome.txt", [])  
    for line in welcometxt:
        print(line)
        # sleep(1)
    return input("If you want to continue press \"enter key\" or you can exit by typing any other key!: ")

def instructionBeforeGame():
    instructions = readtxt.openTextFile("instructions/instructionsbeforemenu.txt", [])  
    for line in instructions:
        print(line)
        # sleep(1)

def mainInstructions():
    mainInstructionFile = readtxt.openTextFile("instructions/maininstructions.txt", [])  
    for line in mainInstructionFile:
        print(line.strip())
        # sleep(1.5)

# Display menu
def displayMenu(isNewUser):
    print("======Menu=====")
    if not isNewUser:
        print("Resume Game : Press \" r \"")           
    print("New Game : Press \" p \"")
    print("Exit : Press \" exit \"")

    