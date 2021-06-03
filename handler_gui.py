from tkinter import filedialog as fd
from tkinter import messagebox

from save_as_image import saveAsImage
from save_as_text import saveAsText

class Handler():
  def __init__(self, window):
    self.window = window
    self.image_path = None
    self.filename = None

  def open_image(self, callback=None):
    filetypes = (('images', '*.png jpg jpeg'), ('All files', '*.*'))
    self.image_path = fd.askopenfilename(
      title='Open a file', 
      initialdir='/', 
      filetypes=filetypes
    )
    if callback:
      callback(self.image_path)

  def convert_to_image(self):
    print(self.image_path)
    saveAsImage(self.image_path, self.show_error, self.show_success)
  
  def convert_to_text(self):
    print(self.image_path)
    saveAsText(self.image_path, self.show_error, self.show_success)

  def show_error(self, message):
    messagebox.showerror(title = "Error", message = message)

  def show_success(self, message):
    messagebox.showinfo(title = "Success", message = message)

  def show_info(self):
    messagebox.showinfo(
      title="Information", 
      message='''
        Save Image
        - gunakan gambar dengan resolusi tinggi, hasilnya akan lebih baik
        - tidak boleh menggunakan gambar yang transparant (error)

        Save Text
        - Bagus untuk Logo, hasil lebih maksimal
        - boleh menggunkan gambar yang transparant
      '''
     )