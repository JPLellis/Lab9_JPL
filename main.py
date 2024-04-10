def encode(password):
    encoded_password = ""
    for digit in password:
        digit_int = int(digit)
        encoded_digit = (digit_int + 3)
        encoded_password += str(encoded_digit)
    return encoded_password


if __name__ == '__main__':
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

    option = int(input("Please enter an option: "))
    password = str(input("Please enter your password to encode: "))

    if option == 1:
        encoded_password = encode(password)
        print("Your password has been encoded and stored!")

    elif option == 2:
        print(f"The encoded password is {}, and the original password is{}.")

    elif option == 3:
        exit()