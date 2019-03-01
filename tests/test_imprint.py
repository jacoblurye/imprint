from unittest import TestCase
import numpy as np
from imprint.imprint import AbstractASCIIMedia, ASCIIImage, ASCIIMedia, ASCIIVideo


mock_image_path = "mock_media/test.png"
mock_video_path = "mock_media/test.m4v"


class TestAbstractASCIIMedia(TestCase):
    def test_nonexistent_file(self):
        with self.assertRaises(AssertionError):
            ASCIIMedia("nope")


class TestASCIIMedia(TestCase):
    def test_mediatype_selection(self):
        image_media = ASCIIMedia(mock_image_path)
        self.assertIs(image_media._PrinterClass, ASCIIImage)

        video_media = ASCIIMedia(mock_video_path)
        self.assertIs(video_media._PrinterClass, ASCIIVideo)


class TestASCIIImage(TestCase):
    def setUp(self):
        self.image = ASCIIImage(mock_image_path, symbols='abc', bitdepth=3)

    def make_imdata(self, im: list):
        return np.array(im, dtype=np.uint8)

    def test_pixel_to_char(self):
        pixels = [0, 1, 2]
        chars = list(self.image._ptoc_vectorized(pixels))
        self.assertEqual(chars, ['a', 'b', 'c'])

    def test_image_to_string(self):
        # Image gets vertically squished and values get averaged
        imdata = self.make_imdata([[0, 2, 1], [1, 2, 0]])
        string = self.image._image_to_string(imdata, max_width=None)
        self.assertEqual(string, 'bcb')

    def test_image_to_string_max_width(self):
        # Image's width and height will be cut in half to achieve max width,
        # then the image's height will be ~halved again (vertical squish)
        imdata = self.make_imdata([[0, 2]] * 8)
        string = self.image._image_to_string(imdata, max_width=1)
        self.assertEqual(string, 'b\nb')

    def test_image_to_string_corner_cases(self):
        # A value greater than configured bitdepth
        imdata = self.make_imdata([[100]])
        string = self.image._image_to_string(imdata, max_width=None)
        self.assertEqual(string, 'c')

        # A value less than 0
        # TODO: is this surprising behavior? should this throw an exception?
        imdata = np.array([[-1]])
        string = self.image._image_to_string(imdata, max_width=None)
        self.assertEqual(string, 'a')
