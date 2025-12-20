import os
import tkinter as tk
from tkinter import filedialog, messagebox
from encoder import hide_message
from decoder import reveal_message, decrypt_message
from PIL import Image

OUTPUT_DIR = "Encrypted-Images"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ---------------- FUNCTIONS ---------------- #

def select_image():
    path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png *.jpg *.bmp")]
    )
    image_path_entry.delete(0, tk.END)
    image_path_entry.insert(0, path)

def set_encode_mode():
    mode_label.config(text="Mode: ENCODE", fg="green")

    # Show encode-only fields
    message_label.pack(pady=5)
    message_text.pack()
    output_label.pack(pady=5)
    output_entry.pack()

    # Show ENCODE button, hide DECODE button
    decode_button.pack_forget()
    encode_button.pack(pady=10)


def set_decode_mode():
    mode_label.config(text="Mode: DECODE", fg="blue")

    # 🔐 Clear sensitive info ONLY when switching to DECODE
    clear_sensitive_fields()

    # Hide encode-only fields
    message_text.delete("1.0", tk.END)
    message_label.pack_forget()
    message_text.pack_forget()

    output_entry.delete(0, tk.END)
    output_label.pack_forget()
    output_entry.pack_forget()

    # Show DECODE button, hide ENCODE button
    encode_button.pack_forget()
    decode_button.pack(pady=10)



def encode_image():
    image_path = image_path_entry.get()
    message = message_text.get("1.0", tk.END).strip()
    password = password_entry.get()
    output_name = output_entry.get()

    if not image_path or not message or not password or not output_name:
        messagebox.showerror("Error", "All encode fields are required!")
        return

    if not output_name.lower().endswith(".png"):
        messagebox.showwarning("Warning", "PNG format is recommended.")

    output_path = os.path.join(OUTPUT_DIR, output_name)

    try:
        hide_message(image_path, message, password, output_path)
        messagebox.showinfo("Success", f"Message hidden in:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def decode_image():
    image_path = image_path_entry.get()
    password = password_entry.get()

    if not image_path or not password:
        messagebox.showerror("Error", "Image and password are required!")
        return

    try:
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
                    encrypted = extracted[:-5]
                    message = decrypt_message(encrypted, password)
                    messagebox.showinfo("Hidden Message", message)
                    return

        messagebox.showerror("Error", "No hidden message or wrong password.")

    except Exception as e:
        messagebox.showerror("Error", str(e))

def clear_sensitive_fields():
    image_path_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)


# ---------------- GUI WINDOW ---------------- #

root = tk.Tk()
root.title("Secure Image Steganography")
root.geometry("520x520")
root.resizable(False, False)

tk.Label(root, text="Secure Image Steganography Tool",
         font=("Arial", 16, "bold")).pack(pady=10)

mode_label = tk.Label(root, text="Mode: ENCODE",
                      fg="green", font=("Arial", 10, "bold"))
mode_label.pack()

mode_frame = tk.Frame(root)
mode_frame.pack(pady=5)

tk.Button(mode_frame, text="Encode Mode",
          command=set_encode_mode, bg="#4CAF50", fg="white").pack(side="left", padx=5)

tk.Button(mode_frame, text="Decode Mode",
          command=set_decode_mode, bg="#2196F3", fg="white").pack(side="left", padx=5)

tk.Label(root, text="Image File:").pack()
image_path_entry = tk.Entry(root, width=55)
image_path_entry.pack(pady=3)
tk.Button(root, text="Browse Image", command=select_image).pack()

message_label = tk.Label(root, text="Secret Message (Encode Only):")
message_label.pack(pady=5)

message_text = tk.Text(root, height=5, width=55)
message_text.pack()

tk.Label(root, text="Password:").pack(pady=5)
password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack()

output_label = tk.Label(root, text="Output Image Name (PNG):")
output_label.pack(pady=5)

output_entry = tk.Entry(root, width=30)
output_entry.pack()

action_frame = tk.Frame(root)
action_frame.pack(pady=15)

encode_button = tk.Button(
    action_frame,
    text="ENCODE",
    command=encode_image,
    bg="#4CAF50",
    fg="white",
    width=15
)

decode_button = tk.Button(
    action_frame,
    text="DECODE",
    command=decode_image,
    bg="#2196F3",
    fg="white",
    width=15
)

encode_button.pack(padx=10)

root.mainloop()
