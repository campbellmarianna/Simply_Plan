class Task:
    def __init__(self, name, image, impact_description):
        self.name = name
        self.image = image
        self.impact_description = impact_description
        self.tasks = list()

    #Create
    def create(item):
        self.tasks.append(item)

    #Read
    def read(index):
        print(task_name_list[index])

    #Update
    def update(self, index, item):
        self.tasks[int(index)] = str(item)

    #Destroy
    def destroy(index):
        task_name_list.pop(int(index))

    def list_all_items(self):
        index = 0
        for list_item in self.tasks:
            print("{} {}".format(index, list_item))
            index += 1

    # Mark Complete - Add code here that marks an item as completed
    def mark_completed(index):
            # print ("√" + checklist[str(index)]
            task_name_list[int(index)] = "√" + task_name_list[index]
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


class Visual():
    #create helper functions for the task objects
        # a helpful function if the image link is an image
        # a helpful function to make sure the user doesn't input words to break
        # your code

    def build_task_one(self):
        pass

    def build_task_two():
        pass

    def build_task_three(task_1):
        pass

    def visualize(self, task_1, end_goal_name):
        print("\n")
        print("Here is a workflow diagram of your tasks!!!")
        print("           ___________________________              ")
        print("          /                           \                ")
        print(f"                {task_1.tasks[0]}                         ")
        print(f" TASK IMPACT:                                         ")
        print(f" {task_1.impact_description}                           ")
        print("                           Who you are doing this for: ")
        print(f"                              {task_1.image}          ")
        print("          \                           /                ")
        print("           \  _____________________  /                  ")
        print("                       ||                               ")
        print("                       ||                              ")
        print("                       \/                              ")
        print("           ___________________________              ")
        print("          /                           \                ")
        print(f"                {task_1.tasks[1]}                         ")
        print(f" TASK IMPACT:                                         ")
        print(f" {task_1.impact_description}                           ")
        print("                           Who you are doing this for: ")
        print(f"                              {task_1.image}          ")
        print("          \                           /                ")
        print("           \  _____________________  /                  ")
        print("                       ||                               ")
        print("                       ||                              ")
        print("                       \/                              ")
        print("           ___________________________              ")
        print("          /                           \                ")
        print(f"                {task_1.tasks[2]}                         ")
        print(f" TASK IMPACT:                                         ")
        print(f" {task_1.impact_description}                           ")
        print("                           Who you are doing this for: ")
        print(f"                              {task_1.image}          ")
        print("          \                           /                ")
        print("           \  _____________________  /                  ")
        print("                       ||                               ")
        print("                       ||                              ")
        print("                       \/                              ")
        print("           ___________________________                 ")
        print("          /                           \                ")
        print("                  END GOAL:                            ")
        print(f"              {end_goal_name}                         ")
        print("          \                           /                ")
        print("           \  _____________________  /                 ")

    def simply_plan(self):
        # get_tasks_for_goal = 3
        print("\n")
        print("Hi Friend! Welcome to Simply Plan!")
        print("Think in your mind what you want to accomplish today? ")
        print("\n")
        pause1 = input("(press enter to continue)")
        print("\n")
        print("I know you want to get a lot of things done.")
        print("However, focus on getting a piece of a project done")
        print("or setting yourself up for success for a project your")
        print("wanting to build in the near future.")
        print("\n")
        pause2 = input("(press enter to continue)")
        print("\n")
        print("Furthermore, if you are part of a team you probably get many")
        print("requests from your team members for a project.")
        print("With that in mind what will your goal be for today?")
        print("Suggestion: Make your goal the goal of that project.")
        end_goal_name = input("Input Goal Here-> ")
        print("\n")
        pause3 = input("(press enter to continue)")
        print("\n")
        # end_goal_name = input("Give your goal a title, such as Finish CS Assignment.-> ")
        # while get_tasks_for_goal > 0:
        print("\n")
        print("In the perspective of 1 to 3 steps, what would those steps be to accomplish your goal.")
        print("For instance, to finish my Intenive Project I need to make a digital prototype.")
        # build task 1
        # create task_name
        print("\n")
        name = input("Input Step 1 here: ")
        print("Who requested the task from you.")
        print("\n")
        # input image url
        image = input("Input an image of the person who requested the task here -> ")
        print("\n")
        impact_description = input("What impact will this task have on the end goal?")
        task_1 = Task(name, image, impact_description)
        task_name = task_1.name
        task_1.tasks.append(task_name)
        # build task 2
        # create task_name
        print("\n")
        name = input("Input Step 2 here: ")
        print("Who requested the task from you.")
        print("\n")
        # input image url
        image = input("Input an image of the person who requested the task here -> ")
        print("\n")
        impact_description = input("What impact will this task have on the end goal?")
        task_2 = Task(name, image, impact_description)
        task_name = task_2.name
        task_1.tasks.append(task_name)

        # create task_name
        print("\n")
        name = input("Input Step 3 here: ")
        print("Who requested the task from you.")
        print("\n")
        # input image url
        image = input("Input an image of the person who requested the task here -> ")
        print("\n")
        impact_description = input("What impact will this task have on the end goal?")
        task_3 = Task(name, image, impact_description)
        task_name = task_3.name
        task_1.tasks.append(task_name)
        # Display workflow diagram
        visual.visualize(task_1, end_goal_name)
        #task_1.create(task_name)
        change = True
        while change:
            change_task = input("Do you want to change the name of the task? (Y/N)")
            if change_task.upper() == "Y":
                task_1.list_all_items()
                print("\n")
                input_item = input("What is the index of the item you want to update? ")
                print("\n")
                input_update = input("What title would you like to replace it with? -> ")
                task_1.update(input_item, input_update)
                task_1.list_all_items()
            if change_task.upper() == "N":
                visual.visualize(task_1, end_goal_name)
                change = False
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
