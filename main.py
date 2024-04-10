def encode(password):
    encoded_password = ""
    for digit in password:
        digit_int = int(digit)
        encoded_digit = (digit_int + 3)
        encoded_password += str(encoded_digit)
    return encoded_password

def decode(encoded_password):
    numlist = list(str(encoded_password))
    intlist = []
    final = []
    for i in numlist:
        x = int(i)
        intlist.append(x)
    for i in intlist:
        x = i - 3
        final.append(x)
    return ("".join(str(num) for num in final))



encoded_password = None
while True:
    if __name__ == '__main__':
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")

        option = int(input("Please enter an option: "))

        if option == 1:
            password = str(input("Please enter your password to encode: "))
            encoded_password = encode(password)
            print("Your password has been encoded and stored!\n")

        elif option == 2:
            if encoded_password is not None:
                print(f"The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}.\n")
            else:
                print("There is no password to be decoded\n")
        elif option == 3:
            break
        else:
            print("Invalid option, please try again\n")