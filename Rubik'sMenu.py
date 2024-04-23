from rubiksCrossDialog import *
from rubiksCornersDialog import *
# # from rubiksSecondLayerDialog import *
# # from rubiksThirdLayerDialog import *


def printWhatToDo():
    favoriteColor = str(input("What is your favorite color on the cube? Input 'white', 'blue', 'yellow', 'orange', 'red', or 'green' to move onto the next step. "))
    while favoriteColor not in ["white", "blue", "yellow", "orange", "red", "green"]:
          print("I'm not sure what you mean. Please enter one of the colors listed in order to proceed.  ")
          favoriteColor = input("What is your favorite color on the cube? Input 'white', 'blue', 'yellow', 'orange', 'red', or 'green' to move onto the next step. ")
    return favoriteColor


print("**************************************************************************************************************")
print("Rubik's Cube helper")
print()
printWhatToDo()
print()
while True
    print("*** What step are you on?***")
    print("*** Cross ***")
    print("*** Corners ***")
    print("*** Middle Layer ***")
    print("*** Bottom layer")


step = input("what step are you on?  ")


while step.lower() != "done":
    if step.lower() == "cross":
        rubiksCrossDialog(favoriteColor)
    elif step.lower() == "corners":
        rubiksCornersDialog(favoriteColor)
    elif step.lower() == "middle layer":
        rubiksSecondLayerDialog()
    elif step.lower() == "bottom layer":
        rubiksThirdLayerDialog()
    else:
        print("Please enter 'Cross', 'Corners', 'Middle Layer', or 'Bottom Layer'")
    print()
    print()
    printWhatToDo()
    print()
    step = input("what step are you on?  ")
    print()
# from rubiksCrossDialog import *
# from rubiksCornersDialog import *
# # from rubiksSecondLayerDialog import *
# # from rubiksThirdLayerDialog import *

# def printWhatToDo():
#     favoriteColor = input("What is your favorite color on the cube? Input 'white', 'blue', 'yellow', 'orange', 'red', or 'green' to move onto the next step: ").lower()
#     while favoriteColor not in ["white", "blue", "yellow", "orange", "red", "green"]:
#         print("I'm not sure what you mean. Please enter one of the colors listed in order to proceed.")
#         favoriteColor = input("What is your favorite color on the cube? Input 'white', 'blue', 'yellow', 'orange', 'red', or 'green' to move onto the next step: ").lower()
#     return favoriteColor

# print("**************************************************************************************************************")
# print("Rubik's Cube helper")
# print()

# favoriteColor = printWhatToDo()

# while True:
#     print("*** What step are you on? ***")
#     print("*** Cross ***")
#     print("*** Corners ***")
#     print("*** Middle Layer ***")
#     print("*** Bottom layer ***")
#     print()

#     step = input("What step are you on? (Type 'done' to exit): ").lower()

#     if step == "done":
#         break

#     if step == "cross":
#         rubiksCrossDialog(favoriteColor)
#     elif step == "corners":
#         rubiksCornersDialog(favoriteColor)
#     elif step == "middle layer":
#         rubiksSecondLayerDialog()
#     elif step == "bottom layer":
#         rubiksThirdLayerDialog()
#     else:
#         print("Please enter 'Cross', 'Corners', 'Middle Layer', or 'Bottom Layer'")
#     print()
