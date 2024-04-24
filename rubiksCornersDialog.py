# from rubiksCrossDialog import *
# def rubiksCrossDialog():
#     favoriteColor = str(input("What is your favorite color on the cube? Input 'white', 'blue', 'yellow', 'orange', 'red', or 'green' to move onto the next step. "))
#     while favoriteColor not in ["white", "blue", "yellow", "orange", "red", "green"]:
#           print("I'm not sure what you mean. Please enter one of the colors listed in order to proceed.  ")
#           favoriteColor = input("What is your favorite color on the cube? Input 'white', 'blue', 'yellow', 'orange', 'red', or 'green' to move onto the next step. ")

#     topEdges = input("Good choice! Now that you've chosen " + favoriteColor + ", keep the center piece of " + favoriteColor + " facing towards you. This will be the first of three layers that you will solve. Say 'done' to move onto the next step, or       'help' to learn more.  ")
#     if favoriteColor == "help":
#         print("Check out the sergs B on youtube for some detailed, helpful instructions. ")
    
        
       
#     if topEdges != "done":
#         if topEdges == "help":
#                print("Check out the sergs B on youtube for some detailed, helpful instructions. ")
#         else: print("I'm not sure what you mean. Say 'help' or 'done' to move on. ")
#     align1 = input("Find a " + favoriteColor + " edge piece and move it next to the " + favoriteColor + " center piece. Notice how each edge piece has two sides, each with a different color? Align the" +favoriteColor+ "edge piece's other color with its corresponding center. Repeat this step until you're done with the cross! Say anything to move on, or enter 'help' if you want more specific instructions.  ")
#     if align1 != "done":
#         if align1 == "help":
#             print("Check out the sergs B on youtube for some detailed, helpful instructions. ")
#         else: print("I'm not sure what you mean. Say 'help' or 'done' to move on. ")
#     # rubiksCornersDialog(favoriteColor)
#     print("Move onto rubiks corners.")
#     return favoriteColor

def rubiksCornersDialog(favoriteColor):
    
    orientation = input(str("Look for a " + favoriteColor + " corner piece on the bottom layer and align it under the spot where it's supposed to go. Hint: look at center pieces. A Corner always goes in between each center. Say 'done' to move onto the next step, or 'help' to learn more.  "))
    if orientation == "help":
        print("Check out the sergs B on youtube for some detailed, helpful instructions. ")
        miniAlgorithm = input("Once you've completed the previous step, make sure the side  of the color you chose for the cross is facing toward your right. Input 'done' to move onto the next step or 'help' for additional assistance.")

    elif orientation == "done":
         miniAlgorithm = input("Once you've completed the previous step, make sure the side  of the color you chose for the cross is facing toward your right. Input 'done' to move onto the next step or 'help' for additional assistance.")
    while orientation not in ["done", "help"]:
        print("I'm not sure what you mean. Please enter 'done' or 'help' to move forward.")
        orientation = input(str("Look for a " + favoriteColor + " corner piece on the bottom layer and align it under the spot where it's supposed to go. Hint: look at center pieces. A Corner always goes in between each center. Say 'done' to move onto the next step, or 'help' to learn more.  "))
        if orientation == "help":
            print("Check out the sergs B on youtube for some detailed, helpful instructions. ")
            miniAlgorithm = input("Once you've completed the previous step, make sure the side  of the color you chose for the cross is facing toward your right. Input 'done' to move onto the next step or 'help' for additional assistance.")
        elif orientation == "done":
            miniAlgorithm = input("Once you've completed the previous step, make sure the side  of the color you chose for the cross is facing toward your right. Input 'done' to move onto the next step or 'help' for additional assistance.")
    
    if miniAlgorithm == "done":
        miniAlgorithm2 = input("Now that you've verified that everything is in the correct position, move the rightmost layer downward, the bottom layer to the left, and the rightmost layer upwards. After this the corner piece should be in the correct place. ")
    elif miniAlgorithm == "help":
        print("Check out the sergs B on youtube for some detailed, helpful instructions. ")
        miniAlgorithm2 = input("Now that you've verified that everything is in the correct position, move the rightmost layer downward, the bottom layer to the left, and the rightmost layer upwards. After this the corner piece should be in the correct place. ")

    while miniAlgorithm not in ["done", "help"]:
        print("I'm not sure what you mean. Please enter 'done' or 'help' to move forward.")
        miniAlgorithm = input("Once you've completed the previous step, make sure the side  of the color you chose for the cross is facing toward your right. Input 'done' to move onto the next step or 'help' for additional assistance. Please input 'done' to move on or 'help' if you need additional assistance. ")
        if miniAlgorithm == "done":
            miniAlgorithm2 = input("Now that you've verified that everything is in the correct position, move the rightmost layer downward, the bottom layer to the left, and the rightmost layer upwards. After this the corner piece should be in the correct place. ")
        elif miniAlgorithm == "help":
            print("Check out the sergs B on youtube for some detailed, helpful instructions. ")
            miniAlgorithm2 = input("Now that you've verified that everything is in the correct position, move the rightmost layer downward, the bottom layer to the left, and the rightmost layer upwards. After this the corner piece should be in the correct place. ")

    if miniAlgorithm2 == "done":
        print("Repeat this task until all corners are in their allotted locations. If there are already some corners in the top layer, but they're oriented wrong, use the previous algorithm (right down, bottom left, right up) to move your piece into the bottom layer. Keep repeating this algorithm until your desired piece is oriented correctly. Now you are done with the 'corners' step. Therefore, move onto second layer in order to continue.  ")

    elif miniAlgorithm2 == "help":
        print("Check out the sergs B on youtube for some detailed, helpful instructions. ")
        print("Repeat this task until all corners are in their allotted locations. If there are already some corners in the top layer, but they're oriented wrong, use the previous algorithm (right down, bottom left, right up) to move your piece into the bottom layer. Keep repeating this algorithm until your desired piece is oriented correctly. Now you are done with the 'corners' step. Therefore, move onto second layer in order to continue.  ")


    while miniAlgorithm2 not in ["done", "help"]:
        print("I'm not sure what you mean. Please enter 'done' or 'help' to move forward.")
        miniAlgorithm2 = input("Now that you've verified that everything is in the correct position, move the rightmost layer downward, the bottom layer to the left, and the rightmost layer upwards. After this the corner piece should be in the correct place. ")
        if miniAlgorithm2 == "done":
            print("Repeat this task until all corners are in their allotted locations. If there are already some corners in the top layer, but they're oriented wrong, use the previous algorithm (right down, bottom left, right up) to move your piece into the bottom layer. Keep repeating this algorithm until your desired piece is oriented correctly. Now you are done with the 'corners' step. Therefore, move onto second layer in order to continue.  ")

        elif miniAlgorithm2 == "help":
            print("Check out the sergs B on youtube for some detailed, helpful instructions. ")
            print("Repeat this task until all corners are in their allotted locations. If there are already some corners in the top layer, but they're oriented wrong, use the previous algorithm (right down, bottom left, right up) to move your piece into the bottom layer. Keep repeating this algorithm until your desired piece is oriented correctly. Now you are done with the 'corners' step. Therefore, move onto second layer in order to continue.  ")
# rubiksCornersDialog()





    