import json
from termcolor import colored, cprint

def add_person():
    name = input("Name: ").capitalize()
    age = input("Age: ")
    email = input("Email: ").lower()
    
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
    print("")
    cprint("Person deleted", "red")
    print("")
        
def search(people):
    search_name = input("Search for a name: ").lower()
    results = []
    
    for person in people:
        name = person["name"]
        if search_name in name.lower():
            results.append(person)
    
    display_people(results)

#START:
print("")
cprint("Hi welcome to my agenda! ", "light_cyan")
print("")

#LIST OF PEOPLE
with open("contacts.json", "r") as f:
    people = json.load(f)["contacts"]


while True:
    
   
    print("Contact list size: ", len(people))
    print("")
    print("-----------------------------------")
    command = input("Select option: \n'SHOW LIST(ls)' \n'ADD(a)'\n'DELETE(d)'\n'SEARCH(s)'\n'QUIT(q)'\n ").lower()
    print("-----------------------------------")
    

    if command == "a":
        person = add_person()
        people.append(person)
        print("")
        cprint("Person added", "light_green")
        print("")
        display_people(people)
    elif command == "d":
        delete_person(people)
        display_people(people)
    elif command == "s":
        search(people)
    elif command == "ls":
        display_people(people)
        print("")
    elif command == "q":
        cprint("See you later!", "light_blue")
        break
    else:
        cprint("Invalid expression" ,"red")
        
with open("contacts.json", "w") as f:
    json.dump({"contacts": people}, f)

