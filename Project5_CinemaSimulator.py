films = {
    "Finding Dory": [3,5],
    "Bourne": [3,5],
    "Tarzan": [15,5],
    "Ghost Busters": [12,5]
    }

while True:
    choice = input("What film do you want to watch?: ").strip().title()

    if choice in films:
        age = int(input("How old are you?").strip())

        #check age
        if age >= films[choice][0]:
            
            #check enough seats
            if films[choice][1] > 0:
                print("Enjoy the film")
                films[choice][1] = films[choice][1] - 1                    
            else:
                print("Sold out")
        else:
            print("You are not old enough")
    else:
        print("We don't have that film!")

