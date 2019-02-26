# -*- coding : utf-8 -*-
"""
View images and video as printed text.
"""

__version__ = '0.1.0'

import sys
import time
import itertools

import numpy as np
from skimage.transform import resize
from skimage.io import imread
from skvideo.io import vreader, ffprobe


class ImagePrinter:
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

    def __call__(self, img, max_width=150):
        """
          Print an image to the console. 
          To obtain a string representation directly, use img_to_str.

          Parameters
          ----------
          img : string or numpy.ndarray
            Either a path to an image file or a matrix representing image data.
          max_width : int
            Restrict width of string representation to max_width characters.

          Returns
          -------
          None
        """
        print(self.img_to_str(img, max_width))

    def img_to_str(self, img, max_width=100):
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
            max_height = round(bw_img.shape[0] * max_width / bw_img.shape[1])
            smaller_shape = (max_height, max_width)
            bw_img = resize(bw_img, smaller_shape, mode='reflect')

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


CURSOR_UP_ONE_LINE = '\x1b[1A'


class VideoPrinter(ImagePrinter):
    """
      Implements an image-to-string converter for watching videos 
      at the command line.
    """

    def __call__(self, vid, max_width=200, is_gif=False):
        """
          Continuously print a video's string representation (i.e., watch it).
          To obtain a generator producing string representations of the video's frames
          directly, use vid_to_str.

          Parameters
          ----------
          vid : string or numpy.ndarray
            Either a path to a video file or a matrix representing video data.
          max_width : int
            Restrict width of string representation to max_width characters.
          is_gif : bool
            If true, loop the video forever.

          Returns
          -------
          None
        """
        # Make the video string generator
        vidstr_gen = self.str_to_vid(vid, max_width, is_gif)

        # Play back video to terminal
        self._play(vidstr_gen)

    def str_to_vid(self, vid, max_width=200, is_gif=False):
        """
          Generate string representations of a video, frame-by-frame.
        """
        # Get video metadata and load video if necessary
        if type(vid) == str:
            vinfo = ffprobe(vid)['video']
            height, width = int(vinfo['@height']), int(vinfo['@width'])
            is_gif = vinfo['@codec_name'] == 'gif'
            vid = vreader(vid)
        else:
            height, width = vid[0].shape[0], vid[0].shape[1]

        # Construct string used for clearing printed frames
        max_height = round(height * max_width / width)
        self._delstring = CURSOR_UP_ONE_LINE * max_height

        # Generate video frame by frame, collecting
        # generated strings if video is a gif
        framelist = []
        for frame in vid:
            frame = self.img_to_str(frame, max_width)
            if is_gif:
                framelist.append(frame)
            yield frame

        # Keep looping gifs forever
        while is_gif:
            for frame in framelist:
                yield frame

    def _play(self, vidstr_gen):
        """
          Continuously print string representations of frames.
        """
        for frame in vidstr_gen:
            print(frame)
            self._clear_frame()

    def _clear_frame(self):
        sys.stdout.write(self._delstring)
