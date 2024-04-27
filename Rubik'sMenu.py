from rubiksCrossDialog import *
from rubiksCornersDialog import *
from rubiksSecondLayerDialog import *
from rubiksThirdLayerDialog import *

def printWhatToDo():
    favoriteColor = input("What is your favorite color on the cube? Input 'white', 'blue', 'yellow', 'orange', 'red', or 'green' to move onto the next step: ").lower()
    while favoriteColor not in ["white", "blue", "yellow", "orange", "red", "green"]:
        print("I'm not sure what you mean. Please enter one of the colors listed in order to proceed.")
        favoriteColor = input("What is your favorite color on the cube? Input 'white', 'blue', 'yellow', 'orange', 'red', or 'green' to move onto the next step: ").lower()
    return favoriteColor

def selection(favoriteColor):
    while True:
        print("*** What step are you on? Following are the four steps in order... ***")
        print("*** Step 1: Cross ***")
        print("*** Step 2: Corners ***")
        print("*** Step 3: Middle Layer ***")
        print("*** Step 4: Bottom layer ***")
        print()

        step = input("what step are you on?  ")

        if step.lower() == "cross":
            rubiksCrossDialog(favoriteColor)
        elif step.lower() == "corners":
            rubiksCornersDialog(favoriteColor)
        elif step.lower() == "middle layer":
            rubiksSecondLayerDialog(favoriteColor)
        elif step.lower() == "bottom layer":
            rubiksThirdLayerDialog(favoriteColor)
        else:
            print("Please enter 'Cross', 'Corners', 'Middle Layer', or 'Bottom Layer'")
        print()

# Ask for favorite color once
favoriteColor = printWhatToDo()

# Start the selection process
selection(favoriteColor)

while True:
    print("*** What step are you on? ***")
    print("*** Cross ***")
    print("*** Corners ***")
    print("*** Middle Layer ***")
    print("*** Bottom layer ***")
    print()

    step = input("What step are you on? (Type 'done' to exit): ").lower()

    if step == "done":
        break

    if step == "cross":
        rubiksCrossDialog(favoriteColor)
    elif step == "corners":
        rubiksCornersDialog(favoriteColor)
    elif step == "middle layer":
        rubiksSecondLayerDialog(favoriteColor)
    elif step == "bottom layer":
        rubiksThirdLayerDialog(favoriteColor)
    else:
        print("Please enter 'Cross', 'Corners', 'Middle Layer', or 'Bottom Layer'")
    print()
