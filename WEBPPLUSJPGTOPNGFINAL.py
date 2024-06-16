import os
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinterdnd2 import TkinterDnD, DND_FILES
# conversion function do NOT mess with
def convert_to_png(file_paths):
    for file_path in file_paths:
        if file_path.endswith(('.webp', '.jpg', '.jpeg')):
            png_path = os.path.splitext(file_path)[0] + '.png'
            with Image.open(file_path) as img:
                img.save(png_path, 'PNG')
                print(f"Converted {file_path} to {png_path}")

    messagebox.showinfo("Success", "Conversion Completed!")
#To drop on
def on_drop(event):
    file_paths = root.tk.splitlist(event.data)
    convert_to_png(file_paths)
#File browsing
def browse_files():
    file_paths = filedialog.askopenfilenames(filetypes=[("Image files", "*.webp *.jpg *.jpeg")])
    if file_paths:
        convert_to_png(file_paths)

# This is the main window
root = TkinterDnD.Tk()
root.title("Image to PNG Converter")

# just a label
info_label = tk.Label(root, text="Drag and drop WebP or JPG files here or click 'Browse...' to select files")
info_label.pack(padx=10, pady=10)

browse_button = tk.Button(root, text="Browse...", command=browse_files)
browse_button.pack(padx=10, pady=10)
# Set up drag-and-drop functionality, IT WORKS FINALLY
root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', on_drop)

root.mainloop()
