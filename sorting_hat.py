import random

name_index = 0

magicians = ["Harry Potter", "Ron Weasley", "Hermione Granger", "Draco Malfoy", "Neville Longbottom", "Luna Lovegood"]

clubs = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]


def sorting_hat(full_name):
    if isinstance(full_name[1], str):
        if "Weasley" in full_name[1]:
            print("Ah! Another Weasley. I know just what to do with you. Gryffindor!")
        else:
            magician = random.choice(clubs)
            return print(magicians[name_index], "is in", magician, "club")
    return None


for i in enumerate(magicians):
    sorting_hat(i)
    name_index += 1
