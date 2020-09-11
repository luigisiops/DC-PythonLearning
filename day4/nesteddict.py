
address1 = {"street": "Fern hill road", "house_num": 90, "city": "Springfield","state": "NJ", "postalcode": "07081"}
address2 = {"street": "Skylark road", "house_num": 100, "city": "NYC", "state": "NY", "postalcode": "05608"}

identification = {
    "firstname": "Luigi", 
    "lastname": "Siopongco", 
    "addresses":[
        {"address1": address1, 
        "address2":address2}
        ]}

print(identification)
print(identification["addresses"][0]["address1"])
"""
address: [
    address1: {street: jdlajfk , postal: 2189301},
    address2: {street: jdlajfk , postal: 2189301}
]
"""