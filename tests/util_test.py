from unittest import TestCase
from imprint import is_image_file, is_video_file

video_files = ["test.gif", "test.mov", "test.mp4", "test.mpeg", "test.m4v"]
image_files = ["test.jpg", "test.jpeg", "test.png", "test.bmp"]
no_ext = "test"


class TestFiletypeIdentification(TestCase):
    def test_is_image_file(self):
        for image in image_files:
            self.assertTrue(is_image_file(image))
        for video in video_files:
            self.assertFalse(is_image_file(video))
        self.assertFalse(is_image_file(no_ext))

    def test_is_video_file(self):
        for video in video_files:
            self.assertTrue(is_video_file(video))
        for image in image_files:
            self.assertFalse(is_video_file(image))
        self.assertFalse(is_video_file(no_ext))
