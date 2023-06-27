#loop

show_instructions = ""
while show_instructions.lower() != "xxx":

    # ask user if they have played before

    show_instructions = input("have you played this before").lower()

    # if yes 'program continues'

    if show_instructions == "yes" or show_instructions == "y":
        show_instructions = "yes"
        print("program continues")

    elif show_instructions == "no" or show_instructions == "n":
        show_instructions = "no"
        print("display instructions")

    # if other 'try again'

    else:
        print("please answer yes/no")


