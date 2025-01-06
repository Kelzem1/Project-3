def add_person():
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")
    
    person = {  
    "name":name,
    "age": age,
    "email": email
    }
    
    return person

#INICIO:
print("Hi welcome to my agenda! ")
print("")

command = input("You can 'ADD', 'DELETE' or 'SEARCH': ").lower()

people = []

if command == "add":
    person = add_person()
    people.append(person)
    print("Perdon added")
elif command == "delete":
    pass
elif command == "search":
    pass
else:
    print("Invalid expression")

print(people)
