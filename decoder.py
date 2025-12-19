from PIL import Image

def decrypt_message(message, password):
    decrypted = ""
    for i in range(len(message)):
        decrypted += chr(ord(message[i]) ^ ord(password[i % len(password)]))
    return decrypted

def reveal_message(image_path, password):
    img = Image.open(image_path).convert("RGB")
    width, height = img.size

    binary_data = ""
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            binary_data += str(r & 1)

    extracted = ""
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        if len(byte) == 8:
            char = chr(int(byte, 2))
            extracted += char
            if extracted.endswith("<END>"):
                encrypted_message = extracted[:-5]
                message = decrypt_message(encrypted_message, password)
                print("Hidden message:", message)
                return

    print("No hidden message found or wrong password.")
