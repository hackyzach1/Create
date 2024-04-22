from rubiksCrossDialog import *
# from rubiksCornersDialog import *
# from rubiksSecondLayerDialog import *
# from rubiksThirdLayerDialog import *


def printWhatToDo():
    print("*** What step are you on?***")
    print("*** Cross ***")
    print("*** Corners ***")
    print("*** Middle Layer ***")
    print("*** Bottom layer")
print("**************************************************************************************************************8")
print("Rubik's Cube helper")
print()
printWhatToDo()
print()


step = input("what step are you on?  ")


while step.lower() != "done":
    if step.lower() == "cross":
        rubiksCrossDialog()
    elif step.lower() == "corners":
        rubiksCornersDialog()
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
