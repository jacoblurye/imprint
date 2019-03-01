# -*- coding : utf-8 -*-
"""
View images and video as printed text.
"""

__version__ = '0.1.0'

from abc import ABC, abstractmethod
from typing import Sequence

import numpy as np
import cv2

from .util import assert_exists, is_image_file, is_video_file


DEFAULT_MAX_WIDTH = 300


class AbstractASCIIMedia(ABC):
    """
      A printable piece of visual media.
    """

    def __init__(self, filepath: str, symbols: str = u' ·:+*@', bitdepth: int = 255):
        """
          Initialize new ascii-able media.

          Parameters:
            filepath : str
              Path to a media file to make ascii-able.
            symbols : str
              Characters to use for pixels, listed in order of increasing "brightness".
            bitdepth : int
              Bitdepth of the images this printer will consume.
        """
        assert_exists(filepath)
        self.filepath = filepath
        self.symbols = symbols
        self.bitdepth = bitdepth

        # The range of pixel values is split into even buckets.
        # TODO: explore other bucketing-schemes.
        self.pixel_value_bucket_size = bitdepth / len(symbols)

        self._validate()
        self._prepare()

    @abstractmethod
    def _validate(self):
        """
          Subclass-specific validations on input to __init__.
        """
        pass

    @abstractmethod
    def _prepare(self):
        """
          Subclass-specific setup that runs at the end of __init__.
        """
        pass

    @abstractmethod
    def print(self, max_width: int = DEFAULT_MAX_WIDTH, **kwargs):
        """
          Print media to stdout.
        """
        raise NotImplementedError()


class ASCIIMedia(AbstractASCIIMedia):
    def _validate(self):
        if is_image_file(self.filepath):
            self._PrinterClass = ASCIIImage
        elif is_video_file(self.filepath):
            self._PrinterClass = ASCIIVideo
        else:
            raise Exception('File format not supported: %s' % self.filepath)

    def _prepare(self):
        self.printer = self._PrinterClass(
            self.filepath, self.symbols, self.bitdepth)

    def print(self, max_width: int = DEFAULT_MAX_WIDTH, **kwargs):
        """
          Print media to stdout.

          Parameters:
            max_width: int
              Maximum permitted width of output string in characters.
            **kwargs:
              Additional subclass-specific config.
        """
        self.printer.print(max_width, **kwargs)


class ASCIIImage(AbstractASCIIMedia):
    """
      Factory for image-to-ASCII printers.
    """

    # Pixels are square, but characters in a font are (generally)
    # taller than they are wide. Vertically squishing images
    # by this factor roughly offsets this discrepancy.
    VERTICAL_SQUISH = .6

    def _validate(self):
        assert is_image_file(
            self.filepath), "Not an image file: %s" % self.filepath

    def _prepare(self):
        self._ptoc_vectorized = np.vectorize(self._pixel_to_char)

    def _pixel_to_char(self, pixel: int):
        """
          Assuming self.symbols are listed from 'darkest' to 'brightest',
          replace pixel with symbol according to its light intensity.
        """
        thresh = self.pixel_value_bucket_size
        for char in self.symbols:
            if pixel < thresh:
                return char
            thresh += self.pixel_value_bucket_size
        return char

    def print(self, max_width: int = DEFAULT_MAX_WIDTH, **kwargs):
        """
          Print the image to stdout.

          Parameters:
            max_width: int
              Maximum permitted width of output string in characters.
            **kwargs:
              Keyword arguments for additional config, currently unused.
        """
        imdata = cv2.imread(self.filepath)
        print(self._image_to_string(imdata, max_width))

    def _image_to_string(self, imdata: np.ndarray, max_width: int):
        """
          Convert a matrix of image data to an ASCII string.
        """
        # Convert color image to black and white,
        bw_image = cv2.cvtColor(imdata, cv2.COLOR_BGR2GRAY)

        # Decrease image resolution to achieve max_width
        if max_width and max_width <= bw_image.shape[1]:
            new_height = bw_image.shape[0] * max_width / bw_image.shape[1]
            new_width = max_width
        else:
            new_height = bw_image.shape[0]
            new_width = bw_image.shape[1]
        squished_height = round(new_height * ASCIIImage.VERTICAL_SQUISH)
        new_shape = (new_width, squished_height)
        resized_image = cv2.resize(bw_image, new_shape)

        # Convert pixels to corresponding symbols
        character_matrix = self._ptoc_vectorized(resized_image)

        # Compose the full image from matrix of chars
        image_string = u'\n'.join([u''.join(row) for row in character_matrix])

        return image_string


class ASCIIVideo(ASCIIImage):
    """
      Factory for video-to-ASCII printers.
    """

    def _validate(self):
        assert is_video_file(
            self.filepath), "Not a video file: %s" % self.filepath

    def print(self,  max_width: int = DEFAULT_MAX_WIDTH, loop: bool = False):
        """
          Print a video to stdout.

          Parameters:
            max_width : str, (default 300)
              A path to a video file.
            loop : bool
              If true, loop file. GIFs always loop.
        """
        loop = loop or self.filepath.endswith("gif")

        # Make the video string generator
        frames = self._gen_video_frames(self.filepath, loop)
        string_frames = self._video_to_string(frames, max_width)

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

    def _video_to_string(self, frames: np.ndarray, max_width: int):
        """
          Generate string representations of a video, frame-by-frame.
        """
        for frame in frames:
            yield self._image_to_string(frame, max_width)

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
