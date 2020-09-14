# here we are creating the Address class
class Address():
    #initialize the attributes of the class
    def __init__(self, street, city, state, zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

#create the user class
class User ():
    #initialize the attributes of the User 
    def __init__(self,first_name, last_name, addresses=None):
        self.first_name = first_name
        self.last_name = last_name
        
        if addresses is None:
            self.addresses = []
        else:
            self.addresses = addresses

    #we will pass in an address object as an argument for this method
    def add_address(self,address):
        #we check if the address we pass in is in our addresses array yet, if it is not then we add the address array to it
        if address not in self.addresses:
            self.addresses.append(address)

    def display_address(self):
        #looping to print the addresses
        for i in range(0,len(self.addresses)):
            print(f"{self.addresses[i].street}, {self.addresses[i].city}, {self.addresses[i].state}, {self.addresses[i].zip_code}")

a1 = Address('60 green hill', 'Springfield', 'New Jersey', '07081')
a2 = Address('70 fernhill hill', 'Springfield', 'New Jersey', '07081')

a3 = Address('100 worth hilt', 'Edison', 'New Jersey', '07081')

user = User('Luigi','Siopongco')
u2 = User('Rizelyn', 'Benito')
u2.add_address(a3)
user.add_address(a1)
user.add_address(a2)

u2.display_address()



