# ask user if they have played before

show_instructions = input("have you played this before").lower()

# if yes 'program continues'

if show_instructions == "yes":
    print("program continues")
    
elif show_instructions == "y":
    print("program continues")

elif show_instructions == "no":
    print("display instructions")
elif show_instructions == "n":
        print("display instructions")

# if other 'try again'

else:
    print("please answer yes/no")

