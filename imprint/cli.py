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
                    type=int, default=300)
parser.add_argument('--loop', help='if true, loop video forever (gifs loop by default)',
                    type=bool)
args = parser.parse_args()


def main():
    if is_image_file(args.file):
        imprint = ImagePrinter(max_width=args.max_width)
        imprint(args.file)
    elif is_video_file(args.file):
        vprint = VideoPrinter(max_width=args.max_width)
        vprint(args.file, loop=args.loop)
    else:
        raise Exception('%s: file format not supported' % args.file)
