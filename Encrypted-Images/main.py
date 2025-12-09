import os
from encoder import hide_message
from decoder import reveal_message

def show_menu():
    print("Welcome to Image Steganography")
    print("1. Hide a secret message in an image")
    print("2. Reveal a hidden message from an image")
    choice = input("Choose an option (1/2): ")

    return choice

def main():
    while True:
        choice = show_menu()

        if choice == "1":
            image_path = input("Enter image file path: ")
            message = input("Enter the message you want to hide: ")
            output_image = input("Enter the output image filename (e.g., hidden.png): ")
            if os.path.exists(image_path):
                hide_message(image_path, message, output_image)
            else:
                print("The image path does not exist. Please try again.")
        
        elif choice == "2":
            image_path = input("Enter image file path to reveal the hidden message: ")
            if os.path.exists(image_path):
                reveal_message(image_path)
            else:
                print("The image path does not exist. Please try again.")
        
        else:
            print("Invalid choice! Please select 1 or 2.")

if __name__ == "__main__":
    main()
