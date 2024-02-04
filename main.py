# Created the txt files
with open("Input/Letters/starting_letter.txt", mode="w") as starting_letter:
    starting_letter.write(f"Dear [name],\nYou are invited to my birthday this Saturday.\nHope you can make it!\nEmre")

with open("Input/Names/invited_names.txt", mode="w") as invited_names:
    invited_names.write("Aang\nZuko\nAppa\nKatara\nSokka\nMono\nUncle Iroh\nToph")

# Reading the line
with open("Input/Names/invited_names.txt", mode="r") as name:
    """Each line is added to a list called 'names'"""
    names = name.readlines()


# Creating the letter text file for each guest
# Replacing the name for each letter
for i in range(len(names)):
    """We open the starting_letter file and read it then replace the '[name] with each individual name from the guest_list"""
    with open("Input/Letters/starting_letter.txt", mode="r") as file:
        # Reading the content of the file
        data = file.read()
        # Replacing the text
        new_data = data.replace("[name]", names[i].strip())
    """Opening our text file for each invitation in write only mode to create and write the replaced content into it"""
    with open(f"Output/ReadyToSend/letter_for_{names[i]}.txt", mode="w") as file:
        file.write(new_data)
