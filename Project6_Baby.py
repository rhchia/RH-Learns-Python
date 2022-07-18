from random import choice

# alternative way of import
# import random
# random.choice()

questions = ["Why is sky blue?: ", "where is there a face on the moon?: ", "where are all the dinosaurs?: "]

question = choice(questions)

answer = input(question).strip().lower()


while answer != "because":
    answer = input("why?: ").strip().lower()
    
print("Oh... Okay")
