# -*- coding : utf-8 -*-
"""
  Implements functionality for use as a command-line utility.
"""

from argparse import ArgumentParser
from .imprint import ASCIIMedia

parser = ArgumentParser()
parser.add_argument('file', help='path to image or video file to display')
parser.add_argument('--max_width', help='maximum width in characters of string representation',
                    type=int, default=300)
parser.add_argument('--loop', help='if present, loop video forever (gifs loop by default)',
                    action="store_true")
args = parser.parse_args()


def main():
    ASCIIMedia(args.file).print(args.max_width, loop=args.loop)
