class Grocery_item():
    def __init__(self, item_name):
        self.item_name = item_name
        self.price = "5"
        self.quantity = "2"

class Shopping_list():
    def __init__(self, title):
        self.title = title
        self.groceries = []


class User():
    def __init__(self,name):
        self.name = name
        self.shopping_list = []

    def create_list (self):
        name_input = input("insert a title: ")
        new_list = Shopping_list(name_input)
        if new_list not in self.shopping_list:
            self.shopping_list.append(new_list)
            print(self.shopping_list)
            print(f'You have created new list: {name_input}!')

    def add_item (self):
        print("add an item to an existing list")
        for i in range(0, len(self.shopping_list)):
            print(f"list{i+1}: {self.shopping_list[i].title}")

        list_input = int(input("list index: "))
        groceries_list = self.shopping_list[list_input-1].groceries
        item = Grocery_item(input("Add item:" ))
        groceries_list.append(item)
        for i in range(0,len(groceries_list)):
            print(f"""You have added item: {item}, 
            your current list is: {groceries_list[i]}""")

    def display_list(self):

        print('Choose which list to access')
        for i in range(0,len(self.shopping_list)):
            print(f"""Shopping list {i+1}: {self.shopping_list[i].title}""")

        list_input = input("list number: ")
        items = self.shopping_list[int(list_input)-1].groceries
        storename = self.shopping_list[int(list_input)-1].title
        print(items)
        for i in range(0, len(items)):
            print(f"************  {storename} List  ************")
            print("")
            print(f"amount:{items[i].quantity}X - {items[i].item_name} - price of each: {items[i].price}")

users = []
def main():
    while(True):
        print("""
            Select an option: 
            1) create a new list
            2) add an item to a list
            3) display all lists
            4) switch user
            q) Quit
            """)
        user_input = (input("option: "))
        if (user_input) == "1":
            users[0].create_list()

        elif (user_input) == "2":
            users[0].add_item()

        elif (user_input) == "3":
            users[0].display_list()


        elif user_input == "q" or "Q":
            break

def menu ():
    while(True):    
        print ("""
        *******Welcome to virtual shopping list*******
                CREATE A USER OR SIGN BACK IN!
                1)login
                2)sign in
                q) Quit
                """)
        login_choice = input("Option: ")

        if (login_choice) == "1":
            login = input("Enter a valid username: ")
            if login in users:
                main()
            else:
                print('user does not exist!')
        elif (login_choice) == "2":
            signup = input("Create a username to signup: ")
            user = User("signup")
            users.append(user)
            main()

        elif login_choice == "q" or "Q":
            break
menu()

