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

def delete_person(people):
    for i, person in enumerate(people):
        print(i + 1, " -" , person["name"], "|", person["age"], "|", person["email"])
        
        while True:
            number = input("Enter a number to delete: ")
            try:
                number = int(number)
                if number <= 0 or number > len(people):
                    print("Invalid number")
                else:
                    break
            except:
                print("Invalid number")
        
        people.pop(number -1)
        print("Person deleted")

#INICIO:
print("Hi welcome to my agenda! ")
print("")

people = []

while True:
    print("Contact list size: ",  len(people))
    command = input("You can 'ADD', 'DELETE' or 'SEARCH'. Press 'q' for quit: ").lower()

    

    if command == "add":
        person = add_person()
        people.append(person)
        print("Perdon added")
    elif command == "delete":
        delete_person(people)
    elif command == "search":
        pass
    elif command == "q":
        print("See you later!")
        break
    else:
        print("Invalid expression")

print(people)
