def rubiksThirdLayerDialog(favoriteColor):


    favoriteColorList = ["red", "blue", "yellow", "white", "green", "orange" ]
    opposingColorDict = dict()


    opposingColorDict["red"] = "orange"
    opposingColorDict["orange"] = "red"
    opposingColorDict["green"] = "blue"
    opposingColorDict["blue"] = "green"
    opposingColorDict["white"] = "yellow"
    opposingColorDict["yellow"] = "white"
    oppositeFavoriteColor = []


    for color in favoriteColorList:
        if color in opposingColorDict:
            oppositeFavoriteColor.append(opposingColorDict[color])
    oppositeFavoriteColor[0] = str(oppositeFavoriteColor[0])


   


    # if favoriteColor in favoriteColorList:
    #     if favoriteColor == 'red':
    #         oppositeFavoriteColor.append(favoriteColor)
    # white  works!
    if favoriteColor == "white":
        rotate = input("Since you solved the first layer using " + favoriteColor + ", now you're gonna want to keep " + str(oppositeFavoriteColor[3]) +" on the top for this last step. Enter 'done' to proceed onward. ")
    # blue works!
    if favoriteColor == "blue":
        rotate = input("Since you solved the first layer using " + favoriteColor + ", now you're gonna want to keep " + str(oppositeFavoriteColor[1]) +" on the top for this last step. Enter 'done' to proceed onward.")
   
    if favoriteColor == "green":
        rotate = input("Since you solved the first layer using " + favoriteColor + ", now you're gonna want to keep " + str(oppositeFavoriteColor[4]) +" on the top for this last step. Enter 'done' to proceed onward.")
   
    if favoriteColor == "yellow":
        rotate = input("Since you solved the first layer using " + favoriteColor + ", now you're gonna want to keep " + str(oppositeFavoriteColor[2]) +" on the top for this last step. Enter 'done' to proceed onward.")
   
    if favoriteColor == "orange":
        rotate = input("Since you solved the first layer using " + favoriteColor + ", now you're gonna want to keep " + str(oppositeFavoriteColor[5]) +" on the top for this last step. Enter 'done' to proceed onward.")
   
    if favoriteColor == "red":
        rotate = input("Since you solved the first layer using " + favoriteColor + ", now you're gonna want to keep " + str(oppositeFavoriteColor[0]) +" on the top for this last step. Enter 'done' to proceed onward.")
   




    if (rotate == "done") and (favoriteColor == "white"):
        arcCross = input("Similar to what we did on the first step, we're going to create a cross on the bottom layer. Before you start your cross, notice what the initial pattern of " + str(oppositeFavoriteColor[3]) +" pieces is on the bottom face. There will either be a lowercase 'r' shape, a horizontal line shape, or just a center without any " + str(oppositeFavoriteColor[3]) + " pieces facing upwards. If you have the 'r' shape enter 1, if you have the horizontal shape  enter 2, if you have no pattern enter 3." )


    if (rotate == "done") and (favoriteColor == "blue"):
        arcCross = input("Similar to what we did on the first step, we're going to create a cross on the bottom layer. Before you start your cross, notice what the initial pattern of " + str(oppositeFavoriteColor[1]) +" pieces is on the bottom face. There will either be a lowercase 'r' shape, a horizontal line shape, or just a center without any " + str(oppositeFavoriteColor[1]) + " pieces facing upwards. If you have the 'r' shape enter 1, if you have the horizontal shape  enter 2, if you have no pattern enter 3." )


    if (rotate == "done") and (favoriteColor == "green"):
        arcCross = input("Similar to what we did on the first step, we're going to create a cross on the bottom layer. Before you start your cross, notice what the initial pattern of " + str(oppositeFavoriteColor[4]) +" pieces is on the bottom face. There will either be a lowercase 'r' shape, a horizontal line shape, or just a center without any " + str(oppositeFavoriteColor[4]) + " pieces facing upwards. If you have the 'r' shape enter 1, if you have the horizontal shape  enter 2, if you have no pattern enter 3." )


    if (rotate == "done") and (favoriteColor == "yellow"):
        arcCross = input("Similar to what we did on the first step, we're going to create a cross on the bottom layer. Before you start your cross, notice what the initial pattern of " + str(oppositeFavoriteColor[2]) +" pieces is on the bottom face. There will either be a lowercase 'r' shape, a horizontal line shape, or just a center without any " + str(oppositeFavoriteColor[2]) + " pieces facing upwards. If you have the 'r' shape enter 1, if you have the horizontal shape  enter 2, if you have no pattern enter 3." )


    if (rotate == "done") and (favoriteColor == "orange"):
        arcCross = input("Similar to what we did on the first step, we're going to create a cross on the bottom layer. Before you start your cross, notice what the initial pattern of " + str(oppositeFavoriteColor[5]) +" pieces is on the bottom face. There will either be a lowercase 'r' shape, a horizontal line shape, or just a center without any " + str(oppositeFavoriteColor[5]) + " pieces facing upwards. If you have the 'r' shape enter 1, if you have the horizontal shape  enter 2, if you have no pattern enter 3." )


    if (rotate == "done") and (favoriteColor == "red"):
        arcCross = input("Similar to what we did on the first step, we're going to create a cross on the bottom layer. Before you start your cross, notice what the initial pattern of " + str(oppositeFavoriteColor[0]) +" pieces is on the bottom face. There will either be a lowercase 'r' shape, a horizontal line shape, or just a center without any " + str(oppositeFavoriteColor[0]) + " pieces facing upwards. If you have the 'r' shape enter 1, if you have the horizontal shape  enter 2, if you have no pattern enter 3." )




    # if statements for arcCross
   
    if arcCross == "1":
        one = input("If you have the lowercase 'r' shape on the bottom layer, rotate the cube so that the lowercase 'r' is the new top layer and keep the r on the upside. Now that you have the 'r' upwards with the base of the r pointing toward you, rotate the face closest to you clockwise (NOT THE BOTTOM LAYER, BUT THE LAYER WITH THE BOTTOM TIP OF THE 'r'). After you have the 'r' facing upwards and the base of the 'r' facing you, rotate the layer facing you clockwise (again, not the side that you're making the cross on), move the right side up, top layer left, right side down, top layer back to the right, and the side facing you back to where it was (should be counter clockwise). enter '2' to move onto the following step.    ")
        if one == "2":
            two = input("If you have the line shape on the bottom layer, rotate the cube so that the line becomes horizontal and is the new top layer. Now that you have the horizontal line facing up with the face that is two-thirds-filled facing you, rotate the face closest to you clockwise (NOT THE BOTTOM LAYER WITH THE HORIZONTAL LINE PATTERN, BUT THE LAYER THAT HAS TWO LAYERS FILLED). After you rotated it clockwise, move the right side up, top layer left, right side down, top layer back to the right, and the side facing you back to where it was (should be counter clockwise). enter 'done' to move onto the following step.  ")
            if two == "done":
                arcAlignment = input("The next step is to align each edge piece on the cross with its center piece. Align as many edges on the bottom layer as you can. The most that you can possible do is two. If all of them are already aligned, skip to the next step. To do align the edges we will use an algorithm similar to what we did in the previous step. This algorithm will rearrange the edges. Enter 'done' to move on to the algorithm. ")
                if arcAlignment == "done":
                    align = input("Now that you've aligned the bottom layer's edge pieces so that as many edges as possible are aligned, (probably two), orient the cube so that the bottom layer is on top, and the side you're working on is the side with a completed edge facing you're direction, with the other completed edge facing toward your right. Then complete this algorithm: right side up, new top layer clockwise twice, right down, new top layer counter-clockwise once, right side up, new layer counter-clockwise again, then right side down. All edges should be aligned now. If they're not, you might have to repeat that algorithm again. Enter 'done' to move onward. ")
                    if align == "done":
                        cornerAllocation = input("The algorithm for corner allocation is a simple one. Once you have your cross with each of its edges aligned, check for which corners are in their correct locations. Note: a corner might be in the right spot, just not rotated correctly. We will fix that in the next step. There are four possible occurences. There are either zero, one, two or four assorted corners. Once you've found all of the corners that are in the correct places (if there aren't, any just do this algorithm twice), keep the correctly assorted corner on your right side with the new top layer facing upward as usual. If there are two already assorted, keep which ever one you'd like on the right. The algorithm goes as follows: Left up, new top layer clockwise, right side up, new top layer back counterclockwise, left side down, new top layer back clockwise, and finally right layer down. Enter 'done' to proceed or 'help' if you need extra assistance.")
                        if cornerAllocation == "done":
                            finalMoves = input("Now you should have at the very worst four corners that are all in the correct places, but just not oriented correctly. This following algorithm should rotate two adjecent corners counterclockwise, (for the one that will be closest to you) and clockwise (for the corner that will be on the other side of the cube). Worse case scenario, you'll only have to do this algorithm twice until you're done with the cube. The algorithm goes as follows: right side up, new top layer clockwise twice, right down, new top layer counter-clockwise once, right side up, new layer counter-clockwise again, then right side down. Then left side up, new top layer clockwise twice, left down, new top layer clockwise once, left side back up, and new top layer clockwise one more time. After moving the left side down (as I'm sure you already have out of excitement) your cube should be solved! enter 'done' to restart the program or 'help' if you need additional assistance.  ")     
                            if finalMoves == "done":
                                exit()
                            elif finalMoves == "help":
                                print("If you need extra help, check out the sergs B on youTube for some detailed, helpful videos. ")
    
                else: 
                    print("I'm not sure what you mean. Please enter 'done' to proceed onward. ")
                    align = input("Now that you've aligned the bottom layer's edge pieces so that as many edges as possible are aligned, (probably two), orient the cube so that the bottom layer is on top, and the side you're working on is the side with a completed edge facing you're direction, with the other completed edge facing toward your right. Then complete this algorithm: right side up, new top layer clockwise twice, right down, new top layer counter-clockwise once, right side up, new layer counter-clockwise again, then right side down. All edges should be aligned now. If they're not, you might have to repeat that algorithm again. Enter 'done' to move onward. ")
                    if align == "done":
                        cornerAllocation = input("The algorithm for corner allocation is a simple one. Once you have your cross with each of its edges aligned, check for which corners are in their correct locations. Note: a corner might be in the right spot, just not rotated correctly. We will fix that in the next step. There are four possible occurences. There are either zero, one, two or four assorted corners. Once you've found all of the corners that are in the correct places (if there aren't, any just do this algorithm twice), keep the correctly assorted corner on your right side with the new top layer facing upward as usual. If there are two already assorted, keep which ever one you'd like on the right. The algorithm goes as follows: Left up, new top layer clockwise, right side up, new top layer back counterclockwise, left side down, new top layer back clockwise, and finally right layer down. Enter 'done' to proceed or 'help' if you need extra assistance.")
                        if cornerAllocation == "done":
                            finalMoves = input("Now you should have at the very worst four corners that are all in the correct places, but just not oriented correctly. This following algorithm should rotate two adjecent corners counterclockwise, (for the one that will be closest to you) and clockwise (for the corner that will be on the other side of the cube). Worse case scenario, you'll only have to do this algorithm twice until you're done with the cube. The algorithm goes as follows: right side up, new top layer clockwise twice, right down, new top layer counter-clockwise once, right side up, new layer counter-clockwise again, then right side down. Then left side up, new top layer clockwise twice, left down, new top layer clockwise once, left side back up, and new top layer clockwise one more time. After moving the left side down (as I'm sure you already have out of excitement) your cube should be solved! enter 'done' to restart the program or 'help' if you need additional assistance.  ")     
                            if finalMoves == "done":
                                exit()
                            elif finalMoves == "help":
                                print("If you need extra help, check out the sergs B on youTube for some detailed, helpful videos. ")
    


   
    elif arcCross == '2':
        two = input("If you have the line shape on the bottom layer, rotate the cube so that the line becomes horizontal and is the new top layer. Now that you have the horizontal line facing up with the face that is two-thirds-filled facing you, rotate the face closest to you clockwise (NOT THE BOTTOM LAYER WITH THE HORIZONTAL LINE PATTERN, BUT THE LAYER THAT HAS TWO LAYERS FILLED). After you rotated it clockwise, move the right side up, top layer left, right side down, top layer back to the right, and the side facing you back to where it was (should be counter clockwise). enter 'done' to move onto the following step.  ")
        if two == "done":
                arcAlignment = input("The next step is to align each edge piece on the cross with its center piece. Align as many edges on the bottom layer as you can. The most that you can possible do is two. If all of them are already aligned, skip to the next step. To do align the edges we will use an algorithm similar to what we did in the previous step. This algorithm will rearrange the edges. Enter 'done' to move on to the algorithm. ")
                if arcAlignment == "done":
                    align = input("Now that you've aligned the bottom layer's edge pieces so that as many edges as possible are aligned, (probably two), orient the cube so that the bottom layer is on top, and the side you're working on is the side with a completed edge facing you're direction, with the other completed edge facing toward your right. Then complete this algorithm: right side up, new top layer clockwise twice, right down, new top layer counter-clockwise once, right side up, new layer counter-clockwise again, then right side down. All edges should be aligned now. If they're not, you might have to repeat that algorithm again. Enter 'done' to move onward. ")
                    if align == "done":
                        cornerAllocation = input("The algorithm for corner allocation is a simple one. Once you have your cross with each of its edges aligned, check for which corners are in their correct locations. Note: a corner might be in the right spot, just not rotated correctly. We will fix that in the next step. There are four possible occurences. There are either zero, one, two or four assorted corners. Once you've found all of the corners that are in the correct places (if there aren't, any just do this algorithm twice), keep the correctly assorted corner on your right side with the new top layer facing upward as usual. If there are two already assorted, keep which ever one you'd like on the right. The algorithm goes as follows: Left up, new top layer clockwise, right side up, new top layer back counterclockwise, left side down, new top layer back clockwise, and finally right layer down. Enter 'done' to proceed or 'help' if you need extra assistance.")
                        if cornerAllocation == "done":
                            finalMoves = input("Now you should have at the very worst four corners that are all in the correct places, but just not oriented correctly. This following algorithm should rotate two adjecent corners counterclockwise, (for the one that will be closest to you) and clockwise (for the corner that will be on the other side of the cube). Worse case scenario, you'll only have to do this algorithm twice until you're done with the cube. The algorithm goes as follows: right side up, new top layer clockwise twice, right down, new top layer counter-clockwise once, right side up, new layer counter-clockwise again, then right side down. Then left side up, new top layer clockwise twice, left down, new top layer clockwise once, left side back up, and new top layer clockwise one more time. After moving the left side down (as I'm sure you already have out of excitement) your cube should be solved! enter 'done' to restart the program or 'help' if you need additional assistance.  ")     
                            if finalMoves == "done":
                                exit()
                            elif finalMoves == "help":
                                print("If you need extra help, check out the sergs B on youTube for some detailed, helpful videos. ")
    
                else: 
                    print("I'm not sure what you mean. Please enter 'done' to proceed onward. ")
                    align = input("Now that you've aligned the bottom layer's edge pieces so that as many edges as possible are aligned, (probably two), orient the cube so that the bottom layer is on top, and the side you're working on is the side with a completed edge facing you're direction, with the other completed edge facing toward your right. Then complete this algorithm: right side up, new top layer clockwise twice, right down, new top layer counter-clockwise once, right side up, new layer counter-clockwise again, then right side down. All edges should be aligned now. If they're not, you might have to repeat that algorithm again. Enter 'done' to move onward. ")
                    if align == "done":
                        cornerAllocation = input("The algorithm for corner allocation is a simple one. Once you have your cross with each of its edges aligned, check for which corners are in their correct locations. Note: a corner might be in the right spot, just not rotated correctly. We will fix that in the next step. There are four possible occurences. There are either zero, one, two or four assorted corners. Once you've found all of the corners that are in the correct places (if there aren't, any just do this algorithm twice), keep the correctly assorted corner on your right side with the new top layer facing upward as usual. If there are two already assorted, keep which ever one you'd like on the right. The algorithm goes as follows: Left up, new top layer clockwise, right side up, new top layer back counterclockwise, left side down, new top layer back clockwise, and finally right layer down. Enter 'done' to proceed or 'help' if you need extra assistance.")
                        if cornerAllocation == "done":
                            finalMoves = input("Now you should have at the very worst four corners that are all in the correct places, but just not oriented correctly. This following algorithm should rotate two adjecent corners counterclockwise, (for the one that will be closest to you) and clockwise (for the corner that will be on the other side of the cube). Worse case scenario, you'll only have to do this algorithm twice until you're done with the cube. The algorithm goes as follows: right side up, new top layer clockwise twice, right down, new top layer counter-clockwise once, right side up, new layer counter-clockwise again, then right side down. Then left side up, new top layer clockwise twice, left down, new top layer clockwise once, left side back up, and new top layer clockwise one more time. After moving the left side down (as I'm sure you already have out of excitement) your cube should be solved! enter 'done' to restart the program or 'help' if you need additional assistance.  ")     
                            if finalMoves == "done":
                                exit()
                            elif finalMoves == "help":
                                print("If you need extra help, check out the sergs B on youTube for some detailed, helpful videos. ")
    
    elif arcCross == '3':
        three = input("If you have no pattern on the bottom layer, rotate the cube so that the bottom layer the new top layer. Rotate the face closest to you clockwise (NOT THE NEW TOP LAYER, BUT THE ONE THAT IS TWO THIRDS FILLED)  After you rotated it clockwise, move the right side up, top layer left, right side down, top layer back to the right, and the side facing you back to where it was (should be counter clockwise). enter '1' to move onto the following step.  ")
        if three == "1":
            one = input("If you have the lowercase 'r' shape on the bottom layer, rotate the cube so that the lowercase 'r' is the new top layer and keep the r on the upside. Now that you have the 'r' upwards with the base of the r pointing toward you, rotate the face closest to you clockwise (NOT THE BOTTOM LAYER, BUT THE LAYER WITH THE BOTTOM TIP OF THE 'r'). After you have the 'r' facing upwards and the base of the 'r' facing you, rotate the layer facing you clockwise (again, not the side that you're making the cross on), move the right side up, top layer left, right side down, top layer back to the right, and the side facing you back to where it was (should be counter clockwise). enter '2' to move onto the following step.    ")
            if one == "2":
                two = input("If you have the line shape on the bottom layer, rotate the cube so that the line becomes horizontal and is the new top layer. Now that you have the horizontal line facing up with the face that is two-thirds-filled facing you, rotate the face closest to you clockwise (NOT THE BOTTOM LAYER WITH THE HORIZONTAL LINE PATTERN, BUT THE LAYER THAT HAS TWO LAYERS FILLED). After you rotated it clockwise, move the right side up, top layer left, right side down, top layer back to the right, and the side facing you back to where it was (should be counter clockwise). enter 'done' to move onto the following step.  ")
            if two == "done":
                arcAlignment = input("The next step is to align each edge piece on the cross with its center piece. Align as many edges on the bottom layer as you can. The most that you can possible do is two. If all of them are already aligned, skip to the next step. To do align the edges we will use an algorithm similar to what we did in the previous step. This algorithm will rearrange the edges. Enter 'done' to move on to the algorithm. ")
                if arcAlignment == "done":
                    align = input("Now that you've aligned the bottom layer's edge pieces so that as many edges as possible are aligned, (probably two), orient the cube so that the bottom layer is on top, and the side you're working on is the side with a completed edge facing you're direction, with the other completed edge facing toward your right. Then complete this algorithm: right side up, new top layer clockwise twice, right down, new top layer counter-clockwise once, right side up, new layer counter-clockwise again, then right side down. All edges should be aligned now. If they're not, you might have to repeat that algorithm again. Enter 'done' to move onward. ")
                    if align == "done":
                        cornerAllocation = input("The algorithm for corner allocation is a simple one. Once you have your cross with each of its edges aligned, check for which corners are in their correct locations. Note: a corner might be in the right spot, just not rotated correctly. We will fix that in the next step. There are four possible occurences. There are either zero, one, two or four assorted corners. Once you've found all of the corners that are in the correct places (if there aren't, any just do this algorithm twice), keep the correctly assorted corner on your right side with the new top layer facing upward as usual. If there are two already assorted, keep which ever one you'd like on the right. The algorithm goes as follows: Left up, new top layer clockwise, right side up, new top layer back counterclockwise, left side down, new top layer back clockwise, and finally right layer down. Enter 'done' to proceed or 'help' if you need extra assistance.")
                        if cornerAllocation == "done":
                            finalMoves = input("Now you should have at the very worst four corners that are all in the correct places, but just not oriented correctly. This following algorithm should rotate two adjecent corners counterclockwise, (for the one that will be closest to you) and clockwise (for the corner that will be on the other side of the cube). Worse case scenario, you'll only have to do this algorithm twice until you're done with the cube. The algorithm goes as follows: right side up, new top layer clockwise twice, right down, new top layer counter-clockwise once, right side up, new layer counter-clockwise again, then right side down. Then left side up, new top layer clockwise twice, left down, new top layer clockwise once, left side back up, and new top layer clockwise one more time. After moving the left side down (as I'm sure you already have out of excitement) your cube should be solved! enter 'done' to restart the program or 'help' if you need additional assistance.  ")     
                            if finalMoves == "done":
                                exit()
                            elif finalMoves == "help":
                                print("If you need extra help, check out the sergs B on youTube for some detailed, helpful videos. ")
    
                else: 
                    print("I'm not sure what you mean. Please enter 'done' to proceed onward. ")
                    align = input("Now that you've aligned the bottom layer's edge pieces so that as many edges as possible are aligned, (probably two), orient the cube so that the bottom layer is on top, and the side you're working on is the side with a completed edge facing you're direction, with the other completed edge facing toward your right. Then complete this algorithm: right side up, new top layer clockwise twice, right down, new top layer counter-clockwise once, right side up, new layer counter-clockwise again, then right side down. All edges should be aligned now. If they're not, you might have to repeat that algorithm again. Enter 'done' to move onward. ")
                    if align == "done":
                        cornerAllocation = input("The algorithm for corner allocation is a simple one. Once you have your cross with each of its edges aligned, check for which corners are in their correct locations. Note: a corner might be in the right spot, just not rotated correctly. We will fix that in the next step. There are four possible occurences. There are either zero, one, two or four assorted corners. Once you've found all of the corners that are in the correct places (if there aren't, any just do this algorithm twice), keep the correctly assorted corner on your right side with the new top layer facing upward as usual. If there are two already assorted, keep which ever one you'd like on the right. The algorithm goes as follows: Left up, new top layer clockwise, right side up, new top layer back counterclockwise, left side down, new top layer back clockwise, and finally right layer down. Enter 'done' to proceed or 'help' if you need extra assistance.")
                        if cornerAllocation == "done":
                            finalMoves = input("Now you should have at the very worst four corners that are all in the correct places, but just not oriented correctly. This following algorithm should rotate two adjecent corners counterclockwise, (for the one that will be closest to you) and clockwise (for the corner that will be on the other side of the cube). Worse case scenario, you'll only have to do this algorithm twice until you're done with the cube. The algorithm goes as follows: right side up, new top layer clockwise twice, right down, new top layer counter-clockwise once, right side up, new layer counter-clockwise again, then right side down. Then left side up, new top layer clockwise twice, left down, new top layer clockwise once, left side back up, and new top layer clockwise one more time. After moving the left side down (as I'm sure you already have out of excitement) your cube should be solved! enter 'done' to restart the program or 'help' if you need additional assistance.  ")     
                            if finalMoves == "done":
                                exit()
                            elif finalMoves == "help":
                                print("If you need extra help, check out the sergs B on youTube for some detailed, helpful videos. ")
                        elif cornerAllocation == "help":
                            print("If you need extra help, check out the sergs B on youTube for some detailed, helpful videos. ")
                        else: 
                            print("I'm not sure what you mean. Please enter 'done' or 'help' to move onward. ")

    else:
        print("I'm not sure what you mean. Please enter 1 to proceed to the next step. ")
        one = input("If you have the lowercase 'r' shape on the bottom layer, rotate the cube so that the lowercase 'r' is the new top layer and keep the r on the upside. Now that you have the 'r' upwards with the base of the r pointing toward you, rotate the face closest to you clockwise (NOT THE BOTTOM LAYER, BUT THE LAYER WITH THE BOTTOM TIP OF THE 'r'). After you have the 'r' facing upwards and the base of the 'r' facing you, rotate the layer facing you clockwise (again, not the side that you're making the cross on), move the right side up, top layer left, right side down, top layer back to the right, and the side facing you back to where it was (should be counter clockwise). enter '2' to move onto the following step.    ")