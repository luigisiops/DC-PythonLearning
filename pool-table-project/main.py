from datetime import datetime

"""class PlayerTable():
    def __init__(self):
        self.start_time = datetime.now()
        self.end_time = None
        self.time_played = None"""

class PoolTableManager():
    def __init__(self):
        self.size = 12
        self.table = [None] * self.size

        #here we need to create a table of table class elements
        for i in range(0, len(self.table)):
            self.table[i] = {}

    #this will insert people into a table of finite size 
    ##need logic to add one per table
    #need to add start time upon insertion
    def time_change(self, start_time, end_time, total_time):
        start_time = datetime.now()

        useable_time = f"{start_time.hour}:{start_time.minute}:{start_time.second}"
        return useable_time

    def total_cost(self,total_time):
        seconds = total_time.seconds
        minutes_cost = 2 * (seconds//60)
        print(minutes_cost)
        return minutes_cost
    
    def send_entry(self, player, table_number, start_time, end_time, total_time, cost):
        today = datetime.now()
        month, day, year = today.month, today.day, today.year
        seconds, minutes, hours = [total_time.seconds, (total_time.seconds//60)%60, total_time.seconds//3600]

        with open(f"{month}-{day}-{year}.txt","a") as file_object:
            file_object.write(f"""
            --------------------------------------------------
            table number:{table_number}
            player: {player}
            start_time: {start_time.hour}:{start_time.minute}:{start_time.second} 
            end_time: {end_time.hour}:{end_time.minute}:{end_time.second}
            total_time: {hours}:{minutes}:{seconds}
            cost: ${cost}
            --------------------------------------------------""")

    def insert(self, key, value):
        table_input = int(input("Pick a table: "))
        if len(self.table[table_input -1]) >= 1:
            print("This table is OCCUPIED TO FULL CAPACITY")
        else:
            index = table_input -1
            self.table[index].update({key: value, "start_time":datetime.now()})
            #self.table[index][startTime].update({"start_time": datetime.timestamp()})

    def remove(self,key):
        for i in range(0, len(self.table)):
            if key in self.table[i]:
                self.table[i].update({"end_time": datetime.now()})
                total_time = self.table[i]["end_time"]- self.table[i]["start_time"]
                total_price = self.total_cost(total_time)
                print(f"cost = {total_price}")

                self.table[i].update({"total_time": total_time})
                self.table[i].update({"cost": total_price})
                print(self.table[i])

                self.send_entry(self.table[i][key], i, self.table[i]["start_time"], self.table[i]["end_time"], self.table[i]["total_time"], total_price)

                del self.table[i][key]
                del self.table[i]['start_time']
                del self.table[i]['end_time']
                del self.table[i]['total_time']
                del self.table[i]['cost']
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




    