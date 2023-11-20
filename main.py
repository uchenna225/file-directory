#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

holder = "[name]"

with open("input/Names/invited_names.txt") as file:
    Names = file.readlines()

with open("input/letters/starting_letter.txt") as file:
    letter_contents = file.read()
    for name in Names:
        contents = letter_contents.replace(holder, name.strip())
        with open(f"output/ReadyToSend/letter_for-{name.strip()}.txt", mode="w") as file_to_be_sent:
            ready = file_to_be_sent.write(contents)
            print(ready)
