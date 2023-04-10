import Welcome
import gamemode

isUserEnter = False
enterKeyPressed = Welcome.userEnterValidation()

if enterKeyPressed == "":
    isUserEnter = True

if isUserEnter:
    # User agree to play game(open game)
    isGameStarted = True
    Welcome.instructionBeforeGame() 
    isNewUser = True
    score = 10
    while isGameStarted: 
        #display menu
        Welcome.displayMenu(isNewUser)
        userAgreePlay = False
        userWantToPlay = input("")
        if userWantToPlay == "p":
            userAgreePlay = True
            # Game Reset (new game)
            isNewUser = True
            score = 10
            # Resume Game
        elif userWantToPlay == "r":
            userAgreePlay = True            
        elif userWantToPlay == "exit":
            isGameStarted == False
            break
        else:
            print("Enter Valid Operation!")
        # User pressed play button
        print("===If you want to go back to the menu press \" b \"===".upper())
        while userAgreePlay:
            # User validation : whether user is existed or not
            if isNewUser:
                openInstructionKey = input("Press letter \"o\" key to instruction list...").lower()
                score = 10
                if openInstructionKey == "o":
                    Welcome.mainInstructions()
                    isNewUser = False                                  
                elif openInstructionKey == "b":
                    userAgreePlay == False
                    break
                else:
                    print("Please enter valid keyword!")
                    continue
            else:
                openInstructionKey = input("Are you want to dispaly instructions? (y/n)")    
                if openInstructionKey == "y":
                    Welcome.mainInstructions()
                elif openInstructionKey == "n":
                    pass
                elif openInstructionKey == "b":
                    userAgreePlay == False
                    break                    
                else:
                    print("Please enter valid key")
                    continue
            gameresult = gamemode.game(score)                 
            if gameresult[1]:
                # display score
                displayscore = gameresult[0]-10
                score = gameresult[0]
                if displayscore < 0:
                    print("Score : 0")
                else:
                    print({f"Score : {displayscore}"})
                break
            break