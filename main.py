# Julia Martin
# Lab 6
# 3/20/2023
# Lab Partner: Emma Cavaneau

# Defines password variables to be stored later.
encoded_password = ''
decoded_password = ''


# Function for the menu.
def menu():
    print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n')


# Function for encoding and storing password input.
def encode(password):
    encoded_password = ''
    for digit in password:
        digit = str((int(digit) + 3))
        encoded_password += digit
    print('Your password has been encoded and stored!\n')
    # Emma: added return statement
    return encoded_password


# Emma: Function for decoding and storing decoded password.
def decode(encoded_password):
    decoded_password = ""
    # Emma: Loops trough digits in encoded password and subtracts 3
    for i in range(0, len(encoded_password)):
        num = int(encoded_password[i])
        num -= 3
        # Emma: Adds original values to decoded string
        decoded_password += str(num)
    return decoded_password


# Main function that runs through a menu loop with the other functions.
def main():
    run = True
    while run:
        menu()
        menu_option = int(input('Please enter an option: '))
        if menu_option == 1:
            password = (input('Please enter your password to encode: '))
            encoded_password = encode(password)
        elif menu_option == 2:
            if password != '':
                # Emma: added function to decode password
                decoded_password = decode(encoded_password)
                # Emma: Changed spacing in print statement
                print('The encoded password is ', encoded_password, sep='', end='')
                print(', and the original password is', decoded_password, end='.\n')
            else:
                print('Error: no password to decode.\n')
        elif menu_option == 3:
            run = False
            break
        else:
            print('Error: that is not a valid menu option.\n')


if __name__ == "__main__":
    main()


