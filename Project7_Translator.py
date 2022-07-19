#Get sentence from user
original = input("Enter sentence: ").strip().lower()

#split sentence into words
words = original.split()

#loop through words and convert to pig latin
new_words = []
construct = ""

for word in words:
    #if it starts with vowel, just add "yay"
    #otherwise, move the first consonant cluser to the end and add "ay"
    
    if word[0] in "aeiou":
        construct = word + "yay"
        new_words.append(construct)
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                break
        con = word[:vowel_pos]
        rest = word[vowel_pos:]
        construct = rest + con + "ay"
        new_words.append(construct)

#stick words back together
output = " ".join(new_words)

#output the final string
print(output)
