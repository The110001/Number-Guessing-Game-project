# test 2 (tkinter GUI)

import tkinter as tk
from PIL import Image, ImageTk

class ResizableImageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Resizable Image")

        # Load the original image
        self.original_image = Image.open("vibrant-fluid-gradient-background-with-curvy-shapes_1017-32108.jpg")  # Replace with your image file
        self.img_width, self.img_height = self.original_image.size

        # Create a label to hold the image
        self.label = tk.Label(root)
        self.label.pack(fill=tk.BOTH, expand=True)

        # Bind resize event
        self.root.bind("<Configure>", self.resize_image)

        # Initial display
        self.resize_image(None)

    def resize_image(self, event):
        # Get new window size
        new_width = self.root.winfo_width()
        new_height = self.root.winfo_height()

        # Resize the image while maintaining aspect ratio
        img_resized = self.original_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        self.tk_image = ImageTk.PhotoImage(img_resized)

        # Update the label with the new image
        self.label.config(image=self.tk_image)

# Run the application
root = tk.Tk()
app = ResizableImageApp(root)
root.mainloop()
