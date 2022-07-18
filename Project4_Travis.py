known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgia", "Harry"]

#print(len(known_users))

while True:
    print("Hi! My name is Travis")
    name = input("What is your name?: ").strip().capitalize()

    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the system? (y/n)").strip().lower()

        if remove == "y":
            known_users.remove(name)
            print(known_users)
        elif remove == "n":
            print("No problem. Name will not be removed")
            print(known_users)
    else:
        print("I don't think I met you yet {}!".format(name))
        add = input("Would you like to be added to the system? (y/n)").strip().lower()

        if add == "y":
            known_users.append(name)
            print(known_users)
        elif add == "n":
            print("No worries! See you around!")
            print(known_users)
