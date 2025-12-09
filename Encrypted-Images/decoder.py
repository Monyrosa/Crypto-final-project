from PIL import Image

def reveal_message(image_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    width, height = img.size

    binary_data = ''
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            binary_data += str(r & 1)

    message = ''
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        if len(byte) == 8:
            char = chr(int(byte, 2))
            message += char
            if message.endswith("<END>"):
                print("Hidden message:", message[:-5])
                return

    print("No hidden message found.")
