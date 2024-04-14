# Test Account

def encode_password(password):
    output = ""
    for i in password:
        char = int(i) + 3
        if char > 9:
            char -= 10
        output += str(char)
    return output

def decode_password(output):
    pass

def main():
    menu_options = ["Encode", "Decode", "Quit"]
    encoded_password = ""
    
    while True:
        print("Menu")
        print("-------------")
        for i in range(len(menu_options)):
            print(f"{i + 1}. {menu_options[i]}")
        
        option = input("Please enter an option number: ")

        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode_password(password)
            print("Your password has been encoded and stored!")
        elif option == "2":
            if encoded_password:
                decoded_password = decode_password(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
            else:
                print("Please encode a password first.")
        elif option == "3":
            break
    
if __name__ == "__main__":
    main()



