from PIL import Image, ImageDraw, ImageFont
import os
import sys

def saveAsImage(image_path, error, success):
  chars = " .'`^\",:;I1!i><-+_-?][}{1)(|\/tfjrxnuvczXYUCLQ0OZmwqpbdkhao*#MW&8%B@$"

  char_width = 11
  char_height = 11

  # open image
  try: 
    image = Image.open(image_path)
    filename = image_path.split("/")[-1]
    print(filename)
  except:
    error("image not found")

  WIDTH, HEIGHT = image.size
  image = image.resize((
    int(WIDTH / char_width), 
    int(HEIGHT / char_height)
  ), Image.NEAREST)
  width, height = image.size
  image = image.load()

  ascii_image = Image.new('RGB', (WIDTH, HEIGHT), (0,0,0))

  font = ImageFont.truetype("arial.ttf", 14)

  drawImage = ImageDraw.Draw(ascii_image)

  def getChar(value):
    return chars[int(value * (len(chars) / 256))]

  try:
    for i in range(height):
      for j in range(width):
        r, g, b = image[j, i]
        k = int((r + g + b) / 3)
        drawImage.text(
          (j * char_width, i * char_height), 
          getChar(k), 
          font=font, 
          fill=(r, g, b)
        )
    result_filename = f'result_{filename}'
    ascii_image.save(result_filename)
    success("Gambar Berhasil di Convert ke ASCII Art")
    os.startfile(result_filename)
  except Exception as e:
    print(e)
    error('''
      Error when converting.
      Note: tidak boleh menggunakan gambar yang transparant (akan mendapatkan error)
    ''')





