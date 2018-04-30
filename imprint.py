#! usr/bin/env python3
# -*- coding : utf-8 -*-

"""
View images and video as printed text.
"""
import sys
import time
import itertools

import numpy as np
from skimage.transform import resize
from skimage.io import imread
from skvideo.io import vreader, ffprobe


class ImgPrinter:
  """
    Implements an image-to-string converter.
  """
  def __init__(self, symbols=u' ·:+*@', bitdepth=255):
    """
      Initialize an image-printer.

      Parameters
      ----------
      symbols : str or str list
        String representations to use for pixels of increasing brightness.
      bitdepth : int
        Bitdepth of the images this printer will consume.
    """
    self.symbols = symbols
    self._inc = bitdepth / len(symbols)
    self._ptoc_vec = np.vectorize(self._pixel_to_char)

  def __call__(self, img, max_width=200):
    """
      Print an image to the console. 
      To obtain a string representation directly, use img_to_str.

      Parameters
      ----------
      img : string or numpy.ndarray
        Either a path to an image file or a matrix representing image data.
      max_width : int

      Returns
      -------
      None
    """
    print(self.img_to_str(img, max_width))

  def img_to_str(self, img, max_width=150):
    """
      Convert img into its string representation.
    """
    if type(img) == str:
      img = imread(img)

    # Convert color image to black and white,
    tall_bw_img = img.mean(axis=2) if len(img.shape) == 3 else img

    # Remove every other row to prevent vertical stretching
    bw_img = tall_bw_img[::2]

    # Decrease image resolution to achieve max_width
    if max_width <= img.shape[1]:
      max_height = round(bw_img.shape[0] * (max_width / img.shape[1]))
      smaller_shape = (max_height, max_width)
      bw_img = resize(bw_img, smaller_shape, mode='constant')

    # Convert pixels to corresponding symbols
    chr_img = self._ptoc_vec(bw_img)

    # Compose the full image from matrix of chars
    str_img = u'\n'.join([u''.join(row) for row in chr_img])

    return str_img

  def _pixel_to_char(self, pixel):
    """
      Assuming self.symbols are listed from 'darkest' to 'brightest',
      replace pixel with symbol according to its light intensity.
    """
    thresh = self._inc
    for char in self.symbols:
      if pixel < thresh: 
        return char
      thresh += self._inc
    return char

CURSOR_UP_ONE_LINE= '\x1b[1A'
class VidPrinter(ImgPrinter):
  """
    Implements an image-to-string converter for watching videos 
    at the commandline.
  """
  def str_to_vid(self, vid, max_width=200):
    for frame in vid:
      yield self.img_to_str(frame, max_width)
  
  def __call__(self, vid, max_width=200, max_frames=1000, framerate=24):
    if type(vid) == str:
      vinfo = ffprobe(vid)['video']
      height, width = int(vinfo['@height']), int(vinfo['@width'])
      vid = vreader(vid)
    else:
      height, width = vid[0].shape[1]
      height = vid[0].shape[0]
    max_height = round(height * max_width / width)
    self._delstring = CURSOR_UP_ONE_LINE * max_height
    vidstr_gen = self.str_to_vid(vid)
    self._play(vidstr_gen, framerate)

  def _play(self, vidstr_gen, framerate):
    for frame in vidstr_gen:
      print(frame)
      self._clear_frame()

  def _clear_frame(self):
    sys.stdout.write(self._delstring)


if __name__ == '__main__':
  # imprinter = ImgPrinter()
  # imprinter('img/flower.jpg', max_width=600)
  vprinter = VidPrinter()
  vprinter('local_img/scene1.mp4')