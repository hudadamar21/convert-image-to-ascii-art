import PIL.Image
import os
import sys

# ascii characters used to build the output text
ASCCI_CHARS = ["@","#","$","%","?","*","'",";",":",",","."]

# resize image according to a new width
def resize_image(image, new_width=100):
  width, height = image.size
  ratio = height / width / 1.65
  new_height = int(new_width * ratio - 10)
  resized_image = image.resize((new_width, new_height))
  return(resized_image)

# convert each pixel to grayscale
def grayify(image):
  grayscale_image = image.convert("L")
  return(grayscale_image)


# convert pixels to a string of ASCII characters
def pixels_to_ascii(image):
  pixels = image.getdata()
  characters = "".join([ASCCI_CHARS[pixel//25] for pixel in pixels ])
  return(characters)


def saveAsText(image_path, error, success):
  new_width=100
  # attempt to open image from user-input
  try: 
    image = PIL.Image.open(image_path)
    filename = image_path.split("/")[-1].split('.')[0]
    print(filename)
  except:
    error("Image not found")

  try:
    # convert image to ASCII
    new_image_data = pixels_to_ascii(grayify(resize_image(image)))

    # format
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))

    # print result
    print(ascii_image)

    # save result to "ascii_image.text"
    result_filename = f'result_{filename}.txt'
    with open(result_filename, "w") as f:
      f.write(ascii_image)

    success("Gambar Berhasil di Convert ke ASCII Art")
    os.startfile(result_filename)
  except:
    error("Error when converting")