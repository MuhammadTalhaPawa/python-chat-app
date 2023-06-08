import json

filename = "data.txt"

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
class mydatabase:
    def __init__(self):
        self.data = []

    def append_data(self):
        data.append({"name": person.name, "age": person.age})



def append_data(person):
    data.append({"name": person.name, "age": person.age})
    
def search_one(key,value):
    
    return

def write_data():
    json_data = json.dumps(data)
    with open(filename, "w") as file:
        file.write(json_data)

def read_data():
    with open(filename, "r") as file:
        json_data = file.read()

    data = json.loads(json_data)
    print(data)


p1 = Person("Talha",19)
p2 = Person("Saad",18)
p3 = Person("Awais",17)

append_data(p1)
append_data(p2)
append_data(p3)

write_data()
read_data()