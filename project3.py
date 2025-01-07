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

def display_people(people):
    for i, person in enumerate(people):
        print(i + 1, " - " , person["name"], "|", person["age"], "|", person["email"])

def delete_person(people):
    
    display_people(people)
        
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
        
def search(people):
    search_name = input("Search for a name: ").lower()
    results = []
    
    for person in people:
        name = person["name"]
        if search_name in name.lower():
            results.append(person)
    
    display_people(results)

#START:
print("Hi welcome to my agenda! ")
print("")

#LIST OF PEOPLE
people = [
    {"name": "Kelu", "age": "27", "email": "rodolfomews@gmail.com"},
    {"name": "Nat", "age": "25", "email": "natalinerja@gmail.com"}
    ]

while True:
    print("Contact list size: ",  len(people))
    command = input("You can 'ADD(a)', 'DELETE(d)' or 'SEARCH(s)'. Press 'q' for quit: ").lower()

    

    if command == "a":
        person = add_person()
        people.append(person)
        print("Perdon added")
    elif command == "d":
        delete_person(people)
    elif command == "s":
        search(people)
    elif command == "q":
        print("See you later!")
        break
    else:
        print("Invalid expression")

print(people)
