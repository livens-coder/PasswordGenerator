from passwordgenerator import passwordgenerator as generate_password


question = input("Do you want a short password? (y/n) ")
if question == 'y':
    try:
        length = int(input("Enter the lenght for a short password: "))
        short_password = generate_password.generate_password(length)
        print(f"Short password: {short_password}")
    except ValueError:
        print("You must enter a number")
else:
    question = input("Do you want a strong password? (y/n) ")
    if question == 'y':
        try:
            length = int(input("Enter the lenght for a strong password: "))
            strong_password = generate_password.generate_password(length, uppercase=True, digits=True, special_chars=True)
            print(f"Strong password: {strong_password}")
        except ValueError:
            print("You must enter a number")
    else:
        print("You must enter a valid answer")
        exit()
        






