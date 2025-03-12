# test 1 (tkinter GUI)

# import modules
import tkinter as tk
from PIL import Image, ImageTk

# display surface
display_surface = tk.Tk()
display_surface.geometry("800x800")
display_surface.resizable(False, False)
window_title = display_surface.title("Practice 1")

# importing images
def background_image_import(image_path):
    image_opening = Image.open(image_path).resize((800,800))
    photo = ImageTk.PhotoImage(image_opening)
    background_image = tk.Label(display_surface, image = photo)
    background_image.image = photo
    background_image.place(width = 800, height = 800)

background_image_import("./vibrant-fluid-gradient-background-with-curvy-shapes_1017-32108.jpg")

# buttons and actions
close = tk.Button(display_surface, text='close', font= ("Arial",17), width=8, height=3, command=display_surface.destroy)
close.place(x=660, y=710)

display_surface.mainloop()
