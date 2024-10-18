current_choice='-'
computer_parts=[]

while current_choice !='0':
    if current_choice in "12345":
        print("Adding {}".format(current_choice))
        if current_choice == '1':
            computer_parts.append("computer")
        elif current_choice == '2':
            computer_parts.append("monitor")
        elif current_choice=='3':
            computer_parts.append('keyboard')

    else:
        print("The parts list")
        print("1: computer")
        print("2: monitor")
        print("3: keyboard")
        print("0: exit")    

    current_choice=input()
