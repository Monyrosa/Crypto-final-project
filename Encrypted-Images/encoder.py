from PIL import Image

def hide_message(image_path, message, output_image):
    img = Image.open(image_path)
    img = img.convert("RGB")
    width, height = img.size

    # Prepare message with END marker
    end_marker = "<END>"
    full_message = message + end_marker
    binary_message = ''.join(format(ord(char), '08b') for char in full_message)

    if len(binary_message) > width * height:
        print("The message is too large to fit in this image.")
        return

    data_index = 0
    for y in range(height):
        for x in range(width):
            if data_index < len(binary_message):
                r, g, b = img.getpixel((x, y))
                r = (r & 0xFE) | int(binary_message[data_index])
                img.putpixel((x, y), (r, g, b))
                data_index += 1
            else:
                img.save(output_image)
                print(f"Message successfully hidden in {output_image}.")
                return

    print("Message embedding failed. Ensure the image is large enough.")
