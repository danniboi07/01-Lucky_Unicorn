# functions

def yes_no (question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
             response = "no"
             return response

        else:
             print("please answer yes/no")

# main function goes here

show_instructions = yes_no("have you played the game before?")
print("you chose {}".format(show_instructions))
print()
having_fun = yes_no("are you having fun")
if having_fun == "no":
    print("╰（'□′）╯ HOW DARE YOU")

elif having_fun == "yes":
    print("(*^▽^*) YAY")

