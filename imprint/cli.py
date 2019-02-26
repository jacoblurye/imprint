# -*- coding : utf-8 -*-
"""
  Implements functionality for use as a command-line utility.
"""

from argparse import ArgumentParser

from .util import is_image_file, is_video_file
from .imprint import ImagePrinter, VideoPrinter

parser = ArgumentParser()
parser.add_argument('file', help='path to image or video file to display')
parser.add_argument('--max_width', help='maximum width in characters of string representation',
                    type=int, default=200)
parser.add_argument('--is_gif', help='if true, loop video forever (defaults to true for .gif files)',
                    type=bool, default=False)
args = parser.parse_args()


def main():
    if is_image_file(args.file):
        imprint = ImagePrinter()
        imprint(args.file, max_width=args.max_width)
    elif is_video_file(args.file):
        vprint = VideoPrinter()
        vprint(args.file, max_width=args.max_width, is_gif=args.is_gif)
    else:
        raise Exception('%s: file format not supported' % args.file)
