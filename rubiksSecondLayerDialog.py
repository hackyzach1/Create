import textwrap

def rubiksSecondLayerDialog(favoriteColor):
    searching = input(textwrap.fill("Now that you've completed the first layer of the cube, we're going to complete the second layer. In order to to this, look for an edge piece on the bottom layer that matches both center colors in the second layer. In the rare case that there's no edge pieces in the bottom layer, proceed to the next step and don't worry about matching the colors .Enter 'done' to proceed or 'help' if you need additional assistance.",width=160))
    if searching == 'done':
            found = input(textwrap.fill("Now that you've found an edge piece, match either one of the edge pieces colors to one of its corresponding center pieces. Enter 'done' to move onto the next step or 'help' if you need extra help. ", width=160))
    elif searching == 'help':
        print("Check out the sergs B on youtube for some detailed, helpful instructions. ")
        found = input(textwrap.fill("Now that you've found an edge piece, match either one of the edge pieces colors to one of its corresponding center pieces. Enter 'done' to move onto the next step or 'help' if you need extra help. ", width=160))
    else:
         print("I'm not sure what you mean. Please enter 'done' or 'help to proceed")

    if found == 'done':
        flip = input(textwrap.fill(" Now move the bottom layer away from where the edge piece is supposed to go. Eg: if the place you want your edge to go is to the right of where your edge piece is currently aligned, move the bottom layer to the left. After you move it left, bring the right side down. (Move the left side down if you moved the bottom layer down right). Then do the opposite of what you just did: if you moved bottom left then right down, then move bottom right and right up. If you moved bottom right and left down, then move bottom left and left up. Enter 'done' to move on or 'help' if you need additional assistance.", width=160))
    elif found == 'help':
        print("Check out the sergs B on youtube for some detailed, helpful instructions. ")
        flip = input(textwrap.fill(" Now move the bottom layer away from where the edge piece is supposed to go. Eg: if the place you want your edge to go is to the right of where your edge piece is currently aligned, move the bottom layer to the left. After you move it left, bring the right side down. (Move the left side down if you moved the bottom layer down right). Then do the opposite of what you just did: if you moved bottom left then right down, then move bottom right and right up. If you moved bottom right and left down, then move bottom left and left up. Enter 'done' to move on or 'help' if you need additional assistance.", width=160))

    else:
        print("I'm not sure what you mean. Please enter 'done' or 'help to proceed")

    if flip == 'done':
        flip2 = input(textwrap.fill("Now orient the cube so the" + favoriteColor + " corner that was brought down to the bottom layer is facing you. (The corner piece brought down should be aligned under the empty spot where it's supposed to go. Then if the piece the piece is on the right side (as it is facing you) move the bottom layer to the left. And vise versa: if it is on the left side as it is facing you, move the bottom layer to the right. Then move the side that has the empty piece where the corner piece is supposed to go. Similar to the corners step, reverse what you just did and move the bottom layer back to where it just was toward the right or left side that you moved down. Then move the right or left side back up. Now the corner along with its corresponding edge should be reallocated to where it should be. Now repeat these last few steps you did with a different edge piece. Enter 'done' to move onto the next step or 'help' if you need additional help. ", width=160))
    elif flip == 'help':
        print("Check out the sergs B on youtube for some detailed, helpful instructions. ")
        flip2 = input(textwrap.fill("Now orient the cube so the" + favoriteColor + " corner that was brought down to the bottom layer is facing you. (The corner piece brought down should be aligned under the empty spot where it's supposed to go. Then if the piece the piece is on the right side (as it is facing you) move the bottom layer to the left. And vise versa: if it is on the left side as it is facing you, move the bottom layer to the right. Then move the side that has the empty piece where the corner piece is supposed to go. Similar to the corners step, reverse what you just did and move the bottom layer back to where it just was toward the right or left side that you moved down. Then move the right or left side back up. Now the corner along with its corresponding edge should be reallocated to where it should be. Now repeat these last few steps you did with a different edge piece. Enter 'done' to move onto the next step or 'help' if you need additional help. ", width=160))
    else: 
        print("I'm not sure what you mean. Please enter 'done' or 'help to proceed")

    if flip2 == 'done':
         print("You're a quick learner! Now that you're done with the second layer, move onto the third and final layer!")
    else: 
         print("Make sure to check out the sergs B on youTube for some extra helpful, detailed instructions.")

         


         