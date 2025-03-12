# test 3 for creating a tkinter GUI for the main program

# importing modules
import tkinter as tk
from PIL import ImageTk, Image

# main window
main_window = tk.Tk()
main_window.title("test 3")
main_window.geometry("800x500")

# the image
image_open = ImageTk.PhotoImage(file="vibrant-fluid-gradient-background-with-curvy-shapes_1017-32108.jpg")

# canvas for the background image
bg_canvas = tk.Canvas(main_window, width=main_window.winfo_width(), height=main_window.winfo_height())
bg_canvas.pack(fill=tk.BOTH, expand=True)

# resizing the image with the window using event binding
def resizer(e):
    global background_img, resized_background, new_background

    # open image
    background_img = Image.open("vibrant-fluid-gradient-background-with-curvy-shapes_1017-32108.jpg")

    # resizing the image
    resized_background = background_img.resize((e.width, e.height), Image.Resampling.LANCZOS)

    # define the image
    new_background = ImageTk.PhotoImage(resized_background)

    # apply the image to the canvas
    bg_canvas.create_image(0,0, image= new_background, anchor = "nw")

main_window.bind("<Configure>", resizer)

# main loop to keep the window open
main_window.mainloop()

