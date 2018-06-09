should_continue = True
if should_continue:
    print ("Hello")

know_people = ["John", "Anna", "Mary"]
person = input("Enter the person you know: ")

if person in know_people:
    print ("We know {}".format(person))
else:
    print ("We don't know {}".format(person))

if person not in know_people:
    print ("We don't know this person")


def who_do_you_know():
    # Ask the user for a list of people they know
    # Split the string into a list
    # Return that list
    names = input("Please type the list of names of people you know, and separate by comma: ")
    names_list = names.split(",")
    names_without_spaces = []
    for name in names_list:
        names_without_spaces.append(name.strip())
    return names_without_spaces

names = who_do_you_know()
print (names)

def ask_user(names):
    # Ask user for a name
    # See if their name is in the list of people they know
    # Print out that they know the person
    name = input("Please type a name you know: ")
    if name in names:
        print ("We also know {}".format(name))
    else:
        print ("We don't know {}".format(name))

ask_user(names)







numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Modify the method below to make sure only even numbers are returned.
def even_numbers():
    evens = []
    for number in numbers:
        if number%2 == 0:
            evens.append(number)
    return evens


# Modify the below method so that "Quit" is returned if the choice parameter is "q".
def user_menu(choice):
    if choice == "q":
        return "Quit"

print (even_numbers())


