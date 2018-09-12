from termcolor import colored #to print colors to terminal

##Unused colors to format print statements
#colorblue = "\033[01;34m{0}\033[00m"
#coloryellow = "\033[01;33m{0}\033[00m"
#colorgreen = "\033[01;32m{0}\033[00m"
#colorred = "\033[01;31m{0}\033[00m"
#colorpurple = "\033[01;35m{0}\033[00m"

checklist = list();

def create(item):
    checklist.append(item)

def read(index):
    return checklist[int(index)]

def update(index, item):
    checklist[int(index)] = item

def destroy(index):
    checklist.pop(int(index))

def clear():
    print("\033c")

#Prints all items in list. If an item starts with a certain color it is
#printed in that color in the terminal
def list_all_items():
    index = 0
    for list_item in checklist:
        words = list_item.split(' ')
        if(words[0].lower() == "red" or words[0].lower() == "√red"):
            print (colored((str(index) + " " + list_item),'red'))
        elif(words[0].lower() == "blue" or words[0].lower() == "√blue"):
            print (colored((str(index) + " " + list_item),'blue'))
        elif(words[0].lower() == "green" or words[0].lower() == "√green"):
            print (colored((str(index) + " " + list_item),'green'))
        elif(words[0].lower() == "cyan" or words[0].lower() == "√cyan"):
            print (colored((str(index) + " " + list_item),'cyan'))
        elif(words[0].lower() == "purple") or words[0].lower() == "√magenta":
            print (colored((str(index) + " " + list_item),'magenta'))
        elif(words[0].lower() == "grey" or words[0].lower() == "gray" or words[0].lower() == "√gray" or words[0].lower() =="√grey"):
            print (colored((str(index) + " " + list_item),'grey'))
        elif(words[0].lower() == "yellow" or words[0].lower() == "√yellow"):
            print (colored((str(index) + " " + list_item),'yellow'))
        else:
            print (colored((str(index) + " " + list_item),'white'))
        index += 1

def mark_completed(index):
    update(index,"√"+checklist[int(index)])

def mark_incomplete(index):
    index=int(index)
    if checklist[index][0] == "√":
        checklist[index] = checklist[index][1:]
    else:
        print("Item is not completed already")

def select(function_code):
    # Create item
    if function_code == "A" or function_code == "a":
        input_item = user_input("Input item: ")
        create(input_item)

    # Read item
    elif function_code == "R" or function_code == "r":
        item_index = user_input("Index Number? ")
        if is_inbounds(item_index):
            print(read(item_index))
        # Remember that item_index must actually exist or our program will crash.

    # Print all items
    elif function_code == "P" or function_code == "p":
        list_all_items()

    elif function_code == "X" or function_code == "x":
        clear()

    elif function_code == "U" or function_code == "u":
        item_index = user_input("Index Number? ")
        input_item = user_input("Input item: ")
        if is_inbounds(item_index):
            print("Completed items will be changed to incomplete")
            update(item_index,input_item)

    elif function_code == "C" or function_code == "c":
        item_index = user_input("Index Number? ")
        if is_inbounds(item_index):
            mark_completed(item_index)

    elif function_code == "I" or function_code == "i":
        item_index = user_input("Index Number? ")
        if is_inbounds(item_index):
            mark_incomplete(item_index)

    elif function_code == "D" or function_code == "d":
        item_index = user_input("Index Number? ")
        if is_inbounds(item_index):
            destroy(item_index)

    elif function_code == "Q" or function_code == "q":
    # This is where we want to stop our loop
        return False
    # Catch all
    else:
        print("Unknown Option")
    return True

def is_inbounds(index):
    try:
        if(int(index)<0 or int(index)>len(checklist)-1):
            print("Index not in list")
            return False
    except ValueError:
        print("Value is not a number")
        return False
    return True

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

def test():
    create("purple sox")
    create("red cloak")

    #print (colorpurple.format(read(0)))
    #print (colorred.format(read(1)))

    update(0, "purple socks")
    mark_completed(0)

    destroy(1)

    print(read(0))

    list_all_items()
    select("C")
    list_all_items()
    # Call function with new value
    print(select("R"))
    # View results
    select("P")
    # Continue until all code is run

running = True
while running:
    selection = user_input("Press A to add to list, C to mark as Completed, I to remove mark as completed, D to delete item, R to Read from list, U to update a list item, P to display list, X to clear the screen, and Q to quit: ")
    running=select(selection)
