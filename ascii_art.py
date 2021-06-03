from tkinter import *
from handler_gui import Handler

# create the window window
window = Tk()
window.title('Convert Image to ASCII Art')
window.resizable(False, False)
window.geometry('300x220+300+200')

handler = Handler(window)

def result_image_path(image_path='image not selected'):
  # Label Title
  label_open_image = Label(
    window, 
    text=image_path,  
    font=("Arial", 10)
  )
  label_open_image.place(relx=0.5, rely=0.32, anchor=CENTER)

# Label Title
label_open_image = Label(
  window, 
  text="Convert Image to ASCII Art",  
  font=("Arial", 15)
)
label_open_image.place(relx=0.5, rely=0.05, anchor=CENTER)

# open button
open_button = Button(
  window, 
  text='Open an Image',
  bg="white",
  command=lambda: handler.open_image(lambda image_path: result_image_path(image_path))
)
open_button.place(relx=0.5, rely=0.2, anchor=CENTER)

# convert to image button
convert_button = Button(
  window, 
  text="Convert as Image", 
  bg="#0C71E0", 
  fg="white", 
  font=("Arial", 12), 
  command=handler.convert_to_image
)
convert_button.place(relx=0.5, rely=0.5, anchor=CENTER)

# convert to text button
convert_button = Button(
  window, 
  text="Convert as Txt", 
  bg="#0C71E0", 
  fg="white", 
  font=("Arial", 12), 
  command=handler.convert_to_text
)
convert_button.place(relx=0.5, rely=0.7, anchor=CENTER)

info_button = Button(
  window, 
  text="Info",
  font=("Arial", 10),
  bg="white",
  command=handler.show_info
)
info_button.place(relx=0.9, rely=0.9, anchor=CENTER)

# run the application
window.mainloop()