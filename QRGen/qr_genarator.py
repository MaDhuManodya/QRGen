import qrcode
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import filedialog

def generate_qr_codes():
    input_value = entry.get()
    if not input_value:
        messagebox.showerror("Error", "Please enter a value.")
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(input_value)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img_resized = qr_img.resize((200, 200))  # Resize the QR code image for display
    qr_img_tk = ImageTk.PhotoImage(qr_img_resized)  # Convert QR image to Tkinter-compatible image

    qr_label = tk.Label(window, image=qr_img_tk)
    qr_label.image = qr_img_tk  # Keep a reference to prevent garbage collection
    qr_label.pack()

    # Add download button to save QR code as image file
    download_btn = tk.Button(window, text="Download QR Code", command=lambda: save_qr_code(input_value, qr_img))
    download_btn.pack()

def save_qr_code(value, qr_image):
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        qr_image.save(file_path)
        messagebox.showinfo("Success", f"QR code saved successfully as {file_path}.")

# Create the main window
window = tk.Tk()
window.title("QR Code Generator")

# Create input label and entry widget
label = tk.Label(window, text="Enter a word or phrase:")
label.pack()

entry = tk.Entry(window, width=50)
entry.pack()

# Create generate button
generate_btn = tk.Button(window, text="Generate QR Code", command=generate_qr_codes)
generate_btn.pack()

# Run the main loop
window.mainloop()
