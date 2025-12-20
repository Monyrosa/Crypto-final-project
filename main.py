import os
from encoder import hide_message
from decoder import reveal_message

OUTPUT_DIR = "Encrypted-Images"
os.makedirs(OUTPUT_DIR, exist_ok=True)

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
            output_image = input("Enter output image filename (e.g., hidden.png): ")

            if not os.path.exists(image_path):
                print("The image path does not exist.")
                continue

            output_path = os.path.join(OUTPUT_DIR, output_image)

            hide_message(image_path, message, password, output_path)

        elif choice == "2":
            image_path = input("Enter encoded image path: ")
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
