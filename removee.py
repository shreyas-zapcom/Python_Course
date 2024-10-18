current_choice='-'
computer_parts=["monitor","keyboard","computer"]

while current_choice !='0':
    if current_choice in "123":
        if current_choice=='1':
            part ='monitor'
        elif current_choice=='2':
            part='keyboard'
        elif current_choice=='3':
            part='computer'

        if part in computer_parts:
            print("Removing {}".format(part))
            computer_parts.remove(part)
        else:
            print("{} is not in the list.".format(part))

        print("Your list now contains: {}".format(computer_parts))

    else:
        print("The parts list (choose to remove):")
        print("1: computer")
        print("2: monitor")
        print("3: keyboard")
        print("0: exit")

    current_choice = input("Enter your choice: ")