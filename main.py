import os
from encoder import hide_message
from decoder import reveal_message

def show_banner():
    print(r"""
  ███████╗████████╗███████╗ ██████╗  █████╗ ███╗   ██╗ ██████╗ 
  ██╔════╝╚══██╔══╝██╔════╝██╔════╝ ██╔══██╗████╗  ██║██╔════╝ 
  ███████╗   ██║   █████╗  ██║  ███╗███████║██╔██╗ ██║██║  ███╗
  ╚════██║   ██║   ██╔══╝  ██║   ██║██╔══██║██║╚██╗██║██║   ██║
  ███████║   ██║   ███████╗╚██████╔╝██║  ██║██║ ╚████║╚██████╔╝
  ╚══════╝   ╚═╝   ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ 

        Secure Image Steganography System
        Password-Protected | LSB Technique
---------------------------------------------------------------
""")


def show_menu():
    print("\nWelcome to Image Steganography")
    print("1. Hide a secret message in an image")
    print("2. Reveal a hidden message from an image")
    print("3. Exit")
    return input("Choose an option (1/2/3): ")

def main():
    show_banner()
    while True:
        choice = show_menu()

        if choice == "1":
            image_path = input("Enter image file path: ")
            message = input("Enter the message you want to hide: ")
            password = input("Enter a password: ")
            output_image = input("Enter the output image filename (e.g., hidden.png): ")

            if os.path.exists(image_path):
                hide_message(image_path, message, password, output_image)
            else:
                print("The image path does not exist.")

        elif choice == "2":
            image_path = input("Enter image file path to reveal the hidden message: ")
            password = input("Enter the password: ")

            if os.path.exists(image_path):
                reveal_message(image_path, password)
            else:
                print("The image path does not exist.")

        elif choice == "3":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice! Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
