# -*- coding : utf-8 -*-
"""
View images and video as printed text.
"""

__version__ = '0.1.0'

from typing import Sequence

import numpy as np
import cv2

from .util import assert_exists, is_image_file, is_video_file


class Printer:
    def __init__(self, max_width: int, symbols: str = u' ·:+*@', bitdepth: int = 255):
        self.max_width = max_width
        self.symbols = symbols
        self.bitdepth = bitdepth
        self._inc = bitdepth / len(symbols)

    def print(self, path: int):
        raise NotImplementedError()


class MediaPrinter(Printer):
    """
      Constructs a printer given a path to an image or video file.
    """

    def print(self, path: str,  loop: bool = False):
        assert_exists(path)
        if is_image_file(path):
            imprint = ImagePrinter(self.max_width)
            imprint.print(path)
        elif is_video_file(path):
            vprint = VideoPrinter(self.max_width)
            vprint.print(path, loop=loop)
        else:
            raise Exception('File format not supported: %s' % path)


class ImagePrinter(Printer):
    """
      Factory for image-to-ASCII printers.
    """

    # Pixels are square, but characters in a font are (generally)
    # taller than they are wide. Vertically squishing images
    # by this factor roughly offsets this discrepancy.
    VERTICAL_SQUISH = .6

    def __init__(self, max_width: int, symbols: str = u' ·:+*@', bitdepth: int = 255):
        """
          Initialize an image-printer.

          Parameters:            
            max_width : int
              Restrict width of string representation to max_width characters.
            symbols : str
              Characters to use for pixels in order of increasing brightness.
            bitdepth : int
              Bitdepth of the images this printer will consume.
        """
        self.max_width = max_width
        self.symbols = symbols
        self._inc = bitdepth / len(symbols)
        self._ptoc_vec = np.vectorize(self._pixel_to_char)

    def print(self, path: str):
        """
          Print an image to stdout.

          Parameters:
            path: str
              A path to an image file.

          Returns:
            None
        """
        assert_exists(path)
        imdata = cv2.imread(path)
        print(self._image_to_string(imdata))

    def _image_to_string(self, imdata: np.ndarray):
        """
          Convert a matrix of image data to an ASCII string.
        """
        # Convert color image to black and white,
        bw_img = imdata.mean(axis=2) if len(imdata.shape) == 3 else imdata

        # Decrease image resolution to achieve max_width
        if self.max_width and self.max_width <= imdata.shape[1]:
            max_height = round(
                bw_img.shape[0] * self.max_width / bw_img.shape[1] * ImagePrinter.VERTICAL_SQUISH)
            smaller_shape = (self.max_width, max_height)
            bw_img = cv2.resize(bw_img, smaller_shape)

        # Convert pixels to corresponding symbols
        chr_img = self._ptoc_vec(bw_img)

        # Compose the full image from matrix of chars
        str_img = u'\n'.join([u''.join(row) for row in chr_img])

        return str_img

    def _pixel_to_char(self, pixel: int):
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


class VideoPrinter(ImagePrinter):
    """
      Factory for video-to-ASCII printers.
    """

    def print(self, path: str, loop: bool = False):
        """
          Print a video to stdout.

          Parameters:
            path : str
              A path to a video file.
            loop : bool
              If true, loop file. GIFs always loop.

          Returns:
            None
        """
        assert_exists(path)

        loop = loop or path.endswith("gif")

        # Make the video string generator
        frames = self._gen_video_frames(path, loop)
        string_frames = self._video_to_string(frames)

        # Play back video to terminal
        self._play(string_frames)

    def _gen_video_frames(self, path: str, loop: bool):
        while True:
            cap = cv2.VideoCapture(path)
            while True:
                success, frame = cap.read()
                if not success:
                    break
                yield frame
            if not loop:
                break

    def _video_to_string(self, frames: np.ndarray):
        """
          Generate string representations of a video, frame-by-frame.
        """
        for frame in frames:
            yield self._image_to_string(frame)

    def _play(self, string_frames: Sequence[int]):
        """
          Continuously print ASCII frames.
        """
        # Clear the terminal
        print("\033[2J")

        for frame in string_frames:
            # Return cursor to home before printing next frame
            print("\033[H")
            print(frame)
