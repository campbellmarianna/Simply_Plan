"""
Check Connection:

def func_check():
    print("Hello World")

func_check()
"""
tasks_list = list()

#Create
def create(item):
    tasks_list.append(item)

#Read
def read(index):
    print(tasks_list[index])

#Update
def update(index, item):
    tasks_list[int(index)] = str(item)

#Destroy
def destroy(index):
    tasks_list.pop(int(index))

def list_all_items():
    index = 0
    for list_item in tasks_list:
        print("{} {}".format(index, list_item))
        index += 1
# Mark Complete - Add code here that marks an item as completed
def mark_completed(index):
        # print ("√" + checklist[str(index)]
        tasks_list[int(index)] = "√" + tasks_list[index]
        # print("{} √{}".format(index, list_item))
        # checklist[int(index)] =
        #return("√" + checklist[index])

def user_input(prompt):
        # the input function will display a message in the terminal
        # and wait for user input.
        user_input = input(prompt)
        return user_input

#Select which functions we want to run
def select(function_code):
    #Create item
    if function_code == "A" or function_code == "a":
        input_item = user_input("Add your task: ")
        create(input_item)
    #Delete item
    elif function_code == "D" or function_code == "d":
        input_item = user_input("Which item do you want to delete? ")
        destroy(input_item)
    #Read item
    elif function_code =="R" or function_code == "r":
        input_item = user_input("What is the number of that item? ")

        #Remember that item_index (was used as the variable that holds user input and inside read below) must actually exist or our program will crash.
        read(int(input_item))

    # Update item
    elif function_code == "U" or function_code == "u":
        input_item = user_input("What is the index of the item you want to update? ")
        input_update = user_input("What item would you like to replace it with? ")
        update(input_item, input_update)
    # Print all items
    elif function_code == "P" or function_code == "p":
        list_all_items()
    #Mark Complete
    elif function_code == "C" or function_code == "c":
        input_item = input("What item would you like to mark complete? ")
        mark_completed(int(input_item))
    # Close out of program
    elif function_code =="Q" or function_code == "q":
        #This is where we want to stop our loop
        return False
    #Catch all - Works
    else:
        print("Unknown Option")
    return True

running = True
while running:
    print("Welcome to Simply Plan!")
    selection = user_input(
        "Press A to Add to list, D to Delete, R to access an item, U to Update item, C to mark as Completed,and P to show list. Press Q to Exit ")
    running = select(selection)

#Testing code
def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    #print(read(1))

    list_all_items()
    mark_completed(0)

    #Call your new function with the appropriate value
    select("C")
    # View the results
    list_all_items()
    # Call function with new value
    select("R")
    # View results
    list_all_items()
    # Continue until all code is run
    user_value = user_input("Please Enter a value:")
    print(user_value)
