#There are 12 tables

#Check if occupied or not occupied

# if occuppied, show start time of table and number
# of minutes played (if >60 min show in hours)

#only give out tables that are not occupied

##This project makes me think of dictionaires and hastables so lets 
#use that
from datetime import datetime

class PoolTableManager():
    def __init__(self):
        self.size = 12
        self.table = [None] * self.size
        for i in range(0, len(self.table)):
            self.table[i] = {}
        self.occupied = False
        self.startTime = None
        self.endTime = None

    #this will insert people into a table of finite size 
    ##need logic to add one per table
    #need to add start time upon insertion
    def insert(self, key, value):
        table_input = int(input("Pick a table: "))
        if len(self.table[table_input -1]) >= 1:
            print("This table is OCCUPIED TO FULL CAPACITY")
        else:
            self.table[table_input -1].update({key: value})

    def remove(self,key):
        for i in range(0, len(self.table)):
            if key in self.table[i]:
                del self.table[i][key]
            else:
                print("player is not at any table")

    #will return what table search is at
    def search(self,key):
        for i in range(0, len(self.table)):
            if key in self.table[i]:
                table_num = print(f"player: {key} is currently at table number {i+1}")
            else:
                print("player is not at any table")
        return table_num

    def view_all_tables(self):
        return self.table

def pool_table_manager():
    pool = PoolTableManager()
    while(True):
        print(f"""
                        POOL TABLES
        ==============================================
                Options: 
                1) Add Customer to table
                2) Remove Customer from table
                3) Search what table Customer is at
                q) Quit

                    Current Table Vacancies 
                    -----------------------
    {pool.view_all_tables()}
        """)

        user_choice = input("Choose an option: ")
        if user_choice == "1":
            user_firstname = input("Write customer first name to be added to a random table: ")
            user_lastname = input("Write customer last name to be added to a random table: ")
            pool.insert(user_firstname, user_lastname)

            table_user_current = pool.search(user_firstname)
            print(f"You have assigned customer {user_firstname} {user_lastname} to table {table_user_current} ")

        if user_choice == "2":
            user_firstname = input("Write customer first name to be remove from table: ")
            pool.remove(user_firstname)

        if user_choice == "3":
            user_firstname = input("Write customer first name to be searched: ")
            pool.search(user_firstname)

        if user_choice =="q":
            break



pool_table_manager()




    