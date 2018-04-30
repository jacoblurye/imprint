import numpy as np
from skimage.transform import resize
from imageio import imread
from skvideo.io import vreader

# Symbols are listed in order from "darkest" to "lightest"
DEFAULT_SYMBOLS = [u" ", u"·", u":", u"+", u"*", u"@"]

class ImgPrinter:
  """
    Convert images to strings that hopefully sort of look like them.
  """
  def __init__(self, 
               symbols=DEFAULT_SYMBOLS,
               bitdepth=255):
    self.symbols = symbols
    self._inc = bitdepth / len(symbols)
    self._ptoc_vec = np.vectorize(self._pixel_to_char)

  def img_to_str(self, img, max_width=200):
    """
      Convert img (a matrix of rgb-triples representing an image)
      into its string representation.
    """
    if type(img) == str:
      img = imread(img)

    # Convert image to black and white,
    # dropping every other row to prevent vertical stretch
    tall_bw_img = img.mean(axis=2)
    bw_img = resize(tall_bw_img, (img.shape[0] // 2, img.shape[1]))
    if max_width <= img.shape[1]:
      max_height = round(bw_img.shape[0] * (max_width / img.shape[1]))
      lo_res_shape = (max_height, max_width)
      bw_img = resize(bw_img, lo_res_shape)

    # Convert pixels to corresponding symbols
    chr_img = self._ptoc_vec(bw_img)

    # Compose the full image from matrix of chars
    str_img = u'\n'.join([u''.join(row) for row in chr_img])

    return str_img

  def print(self, img, max_width=200):
    print(self.img_to_str(img, max_width))

  def _pixel_to_char(self, pixel):
    """
      Assuming self.symbols are listed from "darkest" to "brightest",
      replace pixel appropriately according to its light intensity.
    """
    thresh = self._inc
    for char in self.symbols:
      if pixel < thresh: 
        return char
      thresh += self._inc
    return char

if __name__ == "__main__":
  imprinter = ImgPrinter()
  imprinter.print('img/flower.jpg', max_width=150)