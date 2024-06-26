import textwrap

def rubiksCornersDialog(favoriteColor):
    
    orientation = input(textwrap.fill("""Look for a """ + favoriteColor + """ corner piece on the bottom layer and align it under the spot where it's supposed to go. Hint: look at center pieces. A Corner always goes in between each center. Say 'done' to move onto the next step, or 'help' to learn more.  """, width=160))
    if orientation == "help":
        print("Check out the sergs B on youtube for some detailed, helpful instructions. ")
        miniAlgorithm = input(textwrap.fill("Once you've completed the previous step, make sure the side  of the color you chose for the cross is facing toward your right. Input 'done' to move onto the next step or 'help' for additional assistance.", width=160))

    elif orientation == "done":
        miniAlgorithm = input(textwrap.fill("Once you've completed the previous step, make sure the side  of the color you chose for the cross is facing toward your right. Input 'done' to move onto the next step or 'help' for additional assistance.", width=160))
    while orientation not in ["done", "help"]:
        print("I'm not sure what you mean. Please enter 'done' or 'help' to move forward.")
        orientation = input(textwrap.fill("""Look for a """ + favoriteColor + """ corner piece on the bottom layer and align it under the spot where it's supposed to go. Hint: look at center pieces. A Corner always goes in between each center. Say 'done' to move onto the next step, or 'help' to learn more.  """, width=160))
        if orientation == "help":
            print("Check out the sergs B on youtube for some detailed, helpful instructions. ")
            miniAlgorithm = input(textwrap.fill("Once you've completed the previous step, make sure the side  of the color you chose for the cross is facing toward your right. Input 'done' to move onto the next step or 'help' for additional assistance.", width=160))
        elif orientation == "done":
            miniAlgorithm = input(textwrap.fill("Once you've completed the previous step, make sure the side  of the color you chose for the cross is facing toward your right. Input 'done' to move onto the next step or 'help' for additional assistance.", width=160))
    
    if miniAlgorithm == "done":
        miniAlgorithm2 = input(textwrap.fill("Now that you've verified that everything is in the correct position, move the rightmost layer downward, the bottom layer to the left, and the rightmost layer upwards. After this the corner piece should be in the correct place. ", width=160))
    elif miniAlgorithm == "help":
        print("Check out the sergs B on youtube for some detailed, helpful instructions. ")
        miniAlgorithm2 = input(textwrap.fill("Now that you've verified that everything is in the correct position, move the rightmost layer downward, the bottom layer to the left, and the rightmost layer upwards. After this the corner piece should be in the correct place. ", width=160))

    while miniAlgorithm not in ["done", "help"]:
        print("I'm not sure what you mean. Please enter 'done' or 'help' to move forward.")
        miniAlgorithm = input(textwrap.fill("Once you've completed the previous step, make sure the side  of the color you chose for the cross is facing toward your right. Input 'done' to move onto the next step or 'help' for additional assistance.", width=160))
        if miniAlgorithm == "done":
            miniAlgorithm2 = input(textwrap.fill("Now that you've verified that everything is in the correct position, move the rightmost layer downward, the bottom layer to the left, and the rightmost layer upwards. After this the corner piece should be in the correct place. ", width=160))
        elif miniAlgorithm == "help":
            print("Check out the sergs B on youtube for some detailed, helpful instructions. ")
            miniAlgorithm2 = input(textwrap.fill("Now that you've verified that everything is in the correct position, move the rightmost layer downward, the bottom layer to the left, and the rightmost layer upwards. After this the corner piece should be in the correct place. ", width=160))

    if miniAlgorithm2 == "done":
        print(textwrap.fill("Repeat this task until all corners are in their allotted locations. If there are already some corners in the top layer, but they're oriented wrong, use the previous algorithm (right down, bottom left, right up) to move your piece into the bottom layer. Keep repeating this algorithm until your desired piece is oriented correctly. Now you are done with the 'corners' step. Therefore, move onto second layer in order to continue.  ",width=160))

    elif miniAlgorithm2 == "help":
        print("Check out the sergs B on youtube for some detailed, helpful instructions. ")
        print(textwrap.fill("Repeat this task until all corners are in their allotted locations. If there are already some corners in the top layer, but they're oriented wrong, use the previous algorithm (right down, bottom left, right up) to move your piece into the bottom layer. Keep repeating this algorithm until your desired piece is oriented correctly. Now you are done with the 'corners' step. Therefore, move onto second layer in order to continue.  ",width=160))


    while miniAlgorithm2 not in ["done", "help"]:
        print("I'm not sure what you mean. Please enter 'done' or 'help' to move forward.")
        miniAlgorithm2 = input(textwrap.fill("Now that you've verified that everything is in the correct position, move the rightmost layer downward, the bottom layer to the left, and the rightmost layer upwards. After this the corner piece should be in the correct place. ", width=160))
        if miniAlgorithm2 == "done":
            print(textwrap.fill("Repeat this task until all corners are in their allotted locations. If there are already some corners in the top layer, but they're oriented wrong, use the previous algorithm (right down, bottom left, right up) to move your piece into the bottom layer. Keep repeating this algorithm until your desired piece is oriented correctly. Now you are done with the 'corners' step. Therefore, move onto second layer in order to continue.  ",width=160))

        elif miniAlgorithm2 == "help":
            print("Check out the sergs B on youtube for some detailed, helpful instructions. ")
            print(textwrap.fill("Repeat this task until all corners are in their allotted locations. If there are already some corners in the top layer, but they're oriented wrong, use the previous algorithm (right down, bottom left, right up) to move your piece into the bottom layer. Keep repeating this algorithm until your desired piece is oriented correctly. Now you are done with the 'corners' step. Therefore, move onto second layer in order to continue.  ",width=160))






    