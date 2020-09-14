
"""data = [
    {title:
    priority:
    },
     {title:
     priority:
    },

]"""


def menu():
    data = []
    switch = False

    while(switch == False): 
        option = input(
    """
    Press 1 to add task
    Press 2 to delete task
    Press 3 to view all tasks
    Press q to quit
    """)
        if (option == "1"):
            add_switch = False
            title = input("What is the title? ")

            while(add_switch == False):
                priority = input("Set the priority: (low, medium, or high) ")
                if (priority == "low" or priority == "medium" or priority == "high"):
                    print('accepted')
                    add_switch = True
                else:
                    print('not an option')

            data.append({"title": title, "priority": priority})
            print("task added")
            print(data)

        elif (option == "2"):
            if data == []:
                print('no data is stored yet!')
            else:
                for i in range(len(data)):
                    print(f"{i} - {data[i]['title']} - {data[i]['priority']}")
        
                to_delete = input("Pick index of task to delete ")
                if int(to_delete) in list(range(0,len(data))): 
                    del data[int(to_delete)]
                    print('task deleted!')
                else:
                    print("no such index!")

        elif (option == "3"):
            for i in range(len(data)):
                print(f"{i} - {data[i]['title']} - {data[i]['priority']}")

        elif (option == "q" or option =="Q"):
            switch = True
        else:
            print('Not an option')
            
menu()