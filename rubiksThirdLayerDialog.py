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
                arcCorners = input("The next step is to get the corners into their allotted locations. This algorithm won't rotate the corners, but it will put them in the places that they need to go so that they can be rotated later. ")
    

    
    elif arcCross == '2':
        two = input("If you have the line shape on the bottom layer, rotate the cube so that the line becomes horizontal and is the new top layer. Now that you have the horizontal line facing up with the face that is two-thirds-filled facing you, rotate the face closest to you clockwise (NOT THE BOTTOM LAYER WITH THE HORIZONTAL LINE PATTERN, BUT THE LAYER THAT HAS TWO LAYERS FILLED). After you rotated it clockwise, move the right side up, top layer left, right side down, top layer back to the right, and the side facing you back to where it was (should be counter clockwise). enter 'done' to move onto the following step.  ")
        if two == "done":
                arcCorners = input("The next step is to get the corners into their allotted locations. This algorithm won't rotate the corners, but it will put them in the places that they need to go so that they can be rotated later. ")
    
    elif arcCross == '3':
        three = input("If you have no pattern on the bottom layer, rotate the cube so that the bottom layer the new top layer. Rotate the face closest to you clockwise (NOT THE NEW TOP LAYER, BUT THE ONE THAT IS TWO THIRDS FILLED)  After you rotated it clockwise, move the right side up, top layer left, right side down, top layer back to the right, and the side facing you back to where it was (should be counter clockwise). enter '1' to move onto the following step.  ")
        if three == "1":
            one = input("If you have the lowercase 'r' shape on the bottom layer, rotate the cube so that the lowercase 'r' is the new top layer and keep the r on the upside. Now that you have the 'r' upwards with the base of the r pointing toward you, rotate the face closest to you clockwise (NOT THE BOTTOM LAYER, BUT THE LAYER WITH THE BOTTOM TIP OF THE 'r'). After you have the 'r' facing upwards and the base of the 'r' facing you, rotate the layer facing you clockwise (again, not the side that you're making the cross on), move the right side up, top layer left, right side down, top layer back to the right, and the side facing you back to where it was (should be counter clockwise). enter '2' to move onto the following step.    ")
            if one == "2":
                two = input("If you have the line shape on the bottom layer, rotate the cube so that the line becomes horizontal and is the new top layer. Now that you have the horizontal line facing up with the face that is two-thirds-filled facing you, rotate the face closest to you clockwise (NOT THE BOTTOM LAYER WITH THE HORIZONTAL LINE PATTERN, BUT THE LAYER THAT HAS TWO LAYERS FILLED). After you rotated it clockwise, move the right side up, top layer left, right side down, top layer back to the right, and the side facing you back to where it was (should be counter clockwise). enter 'done' to move onto the following step.  ")
            if two == "done":
                arcCorners = input("The next step is to get the corners into their allotted locations. This algorithm won't rotate the corners, but it will put them in the places that they need to go so that they can be rotated later. ")
    else: 
        print("I'm not sure what you mean. Please enter 1 to proceed to the next step. ")
        one = input("If you have the lowercase 'r' shape on the bottom layer, rotate the cube so that the lowercase 'r' is the new top layer and keep the r on the upside. Now that you have the 'r' upwards with the base of the r pointing toward you, rotate the face closest to you clockwise (NOT THE BOTTOM LAYER, BUT THE LAYER WITH THE BOTTOM TIP OF THE 'r'). After you have the 'r' facing upwards and the base of the 'r' facing you, rotate the layer facing you clockwise (again, not the side that you're making the cross on), move the right side up, top layer left, right side down, top layer back to the right, and the side facing you back to where it was (should be counter clockwise). enter '2' to move onto the following step.    ")


            
    # # if statements for one 
    
    # # if one == "1":
    # #     two = input("If you have the line shape on the bottom layer, rotate the cube so that the line becomes horizontal and is the new top layer. Now that you have the horizontal line facing up with the face that is two-thirds-filled facing you, rotate the face closest to you clockwise (NOT THE BOTTOM LAYER WITH THE HORIZONTAL LINE PATTERN, BUT THE LAYER THAT HAS TWO LAYERS FILLED). After you rotated it clockwise, move the right side up, top layer left, right side down, top layer back to the right, and the side facing you back to where it was (should be counter clockwise). enter 'done' to move onto the following step.  ")
    # # else: 
    # #     print("I'm not sure what you mean. Please enter 1 to proceed to the next step. ")
    # #     one = input("If you have the lowercase 'r' shape on the bottom layer, rotate the cube so that the lowercase 'r' is the new top layer and keep the r on the upside. Now that you have the 'r' upwards with the base of the r pointing toward you, rotate the face closest to you clockwise (NOT THE BOTTOM LAYER, BUT THE LAYER WITH THE BOTTOM TIP OF THE 'r'). After you have the 'r' facing upwards and the base of the 'r' facing you, rotate the layer facing you clockwise (again, not the side that you're making the cross on), move the right side up, top layer left, right side down, top layer back to the right, and the side facing you back to where it was (should be counter clockwise). enter '2' to move onto the following step.    ")

    # # if statements for 2 
     
    # if two == "done":
    #     arcCorners = input("The next step is to get the corners into their allotted locations. This algorithm won't rotate the corners, but it will put them in the places that they need to go so that they can be rotated later. ")
    # else:
    #     print("I'm not sure what you mean. Please enter 1 to proceed to the next step. ")
    #     two = input("If you have the line shape on the bottom layer, rotate the cube so that the line becomes horizontal and is the new top layer. Now that you have the horizontal line facing up with the face that is two-thirds-filled facing you, rotate the face closest to you clockwise (NOT THE BOTTOM LAYER WITH THE HORIZONTAL LINE PATTERN, BUT THE LAYER THAT HAS TWO LAYERS FILLED). After you rotated it clockwise, move the right side up, top layer left, right side down, top layer back to the right, and the side facing you back to where it was (should be counter clockwise). enter 'done' to move onto the following step.  ")

    # # if statements for 3 

    # if three == "2":
    #     two = input("If you have the line shape on the bottom layer, rotate the cube so that the line becomes horizontal and is the new top layer. Now that you have the horizontal line facing up with the face that is two-thirds-filled facing you, rotate the face closest to you clockwise (NOT THE BOTTOM LAYER WITH THE HORIZONTAL LINE PATTERN, BUT THE LAYER THAT HAS TWO LAYERS FILLED). After you rotated it clockwise, move the right side up, top layer left, right side down, top layer back to the right, and the side facing you back to where it was (should be counter clockwise). enter 'done' to move onto the following step.  ")
        
    #     if two == "done":
    #         arcCorners = input("The next step is to get the corners into their allotted locations. This algorithm won't rotate the corners, but it will put them in the places that they need to go so that they can be rotated later. ")
     
    # else: 
    #     print("I'm not sure what you mean. Please enter 1 to proceed to the next step. ")
    #     three = input("If you have no pattern on the bottom layer, rotate the cube so that the bottom layer the new top layer. Rotate the face closest to you clockwise (NOT THE NEW TOP LAYER, BUT THE ONE THAT IS TWO THIRDS FILLED)  After you rotated it clockwise, move the right side up, top layer left, right side down, top layer back to the right, and the side facing you back to where it was (should be counter clockwise). enter '2' to move onto the following step.  ")

    
    # if arcCorners == "done":
    #     return 1





















































        
    