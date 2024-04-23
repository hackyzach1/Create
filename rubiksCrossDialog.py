from rubiksCornersDialog import *
def rubiksCrossDialog(favoriteColor):
    # favoriteColor = str(input("What is your favorite color on the cube? Input 'white', 'blue', 'yellow', 'orange', 'red', or 'green' to move onto the next step. "))
    # while favoriteColor not in ["white", "blue", "yellow", "orange", "red", "green"]:
    #       print("I'm not sure what you mean. Please enter one of the colors listed in order to proceed.  ")
    #       favoriteColor = input("What is your favorite color on the cube? Input 'white', 'blue', 'yellow', 'orange', 'red', or 'green' to move onto the next step. ")

    topEdges = input("Good choice! Now that you've chosen " + favoriteColor + ", keep the center piece of " + favoriteColor + " facing towards you. This will be the first of three layers that you will solve. Say 'done' to move onto the next step, or       'help' to learn more.  ")
    if favoriteColor == "help":
        print("Check out the sergs B on youtube for some detailed, helpful instructions. ")
    
        
       
    if topEdges != "done":
        if topEdges == "help":
               print("Check out the sergs B on youtube for some detailed, helpful instructions. ")
        else: print("I'm not sure what you mean. Say 'help' or 'done' to move on. ")
    align1 = input("Find a " + favoriteColor + " edge piece and move it next to the " + favoriteColor + " center piece. Notice how each edge piece has two sides, each with a different color? Align the" +favoriteColor+ "edge piece's other color with its corresponding center. Repeat this step until you're done with the cross! Say anything to move on, or enter 'help' if you want more specific instructions.  ")
    if align1 != "done":
        if align1 == "help":
            print("Check out the sergs B on youtube for some detailed, helpful instructions. ")
        else: print("I'm not sure what you mean. Say 'help' or 'done' to move on. ")
    
#     rubiksCornersDialog(favoriteColor)
    print("Move onto rubiks corners.")
#     return favoriteColor

    
# rubiksCrossDialog()