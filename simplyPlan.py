class Task:
    def __init__(self, task_name, image, task_impact_description):
        self.name = task_name
        self.image = image
        self.impact = task_impact_description

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
            # isalpha
            print("Unknown Option")
        return True

    # running = True
    # while running:
    #     print("Welcome to Simply Plan!")
    #     selection = user_input(
    #         "Press A to Add to list, D to Delete, R to access an item, U to Update item, C to mark as Completed,and P to show list. Press Q to Exit ")
    #     running = select(selection)

class Visual:
    #create helper functions for the task objects
        # a helpful function if the image link is an image
        # a helpful function to make sure the user doesn't input words to break
        # your code

    def build_task_one(self):
        #create task_name
        task_name = input("Input Step 1 here: ")
        print("Who requested the task from you.")
        # input image url
        image = input("Input an image of the person who requested the task here ->")
        task_impact_description = input("What impact will this task have on the end goal?")
        task_1 = Task(task_name, image, task_impact_description)





    def build_task_two():
        pass

    def build_task_three():
        pass

    def simply_plan(self):
        # get_tasks_for_goal = 3
        print("Hi Friend! Welcome to Simply Plan!")

        end_goal = input("What do you want to accomplish today? ")

        print("I know you want to get a lot of things done.")
        print("However, focus on getting a piece of a project done")
        print("or setting yourself up for sucess for a project your")
        print("wanting to build in the near future.")
        print("Furthermore, if you are part of a team you probably get many")
        print("request from your team members for a projectself.")
        print("Make your goal for today the goal of that project. ")

        print(f"Your goal: {end_goal}")
        end_goal_name = input("Give your goal a title, such as Finish CS Assignment. ->")
        # while get_tasks_for_goal > 0:
        print("In the perspective of 1 to 3 steps, what would those steps be to accomplish your goal.")
        print("For instance, to finish my CS Assignment I need to complete challenge #1 in the course packet.")
        visual.build_task_one()
        # build_task_two()
        # build_task_three()

        #get_tasks_for_goal -= 1
        # program loop that prompts the user to create a goal
            # inside that goal they assign task
            # Ask the user would you like to create more tasks more tasks? (Y/N)
                #if user input is Y:
                    # allow them to create more task (you can create up to three tasks)
                #if user_input is N:
                    # exit the loop
        # display tasks and end goal in workflow diagram

visual = Visual()

visual.simply_plan()
