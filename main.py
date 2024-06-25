#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

f = open("../Mail Merge Project Start/Input/Names/invited_names.txt", "r")
for person in f:
    name = person.strip()
    email = open("../Mail Merge Project Start/Input/Letters/starting_letter.txt", "r").readlines()
    x = email[0].replace("[name]", f"{name}")
    email[0] = x
    filled = open(f"../Mail Merge Project Start/Output/ReadyToSend/{name}.txt","w")
    filled.write(' '.join(email))
