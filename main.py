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
    global encoded_password
    encoded_password_password = ''
    for digit in password:
        digit = str((int(digit) + 3) % 10)
        encoded_password_password += digit
    print('Your password has been encoded and stored!\n')


# Function for decoding and storing decoded password.
def decode(password):
    global decoded_password


# Main function that runs through a menu loop with the other functions.
def main():
    run = True
    while run:
        menu()
        menu_option = int(input('Please enter an option: '))
        if menu_option == 1:
            password = (input('Please enter your password to encode: '))
            encode(password)
        elif menu_option == 2:
            if encoded_password != '':
                decode(password)
                print('The encoded password is ', encoded_password, end= '')
                print('and the original password is ', decoded_password, end='.\n')
            else:
                print('Error: no password to decode.\n')
        elif menu_option == 3:
            run = False
            break
        else:
            print('Error: that is not a valid menu option.\n')


if __name__ == "__main__":
    main()
