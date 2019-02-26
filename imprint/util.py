import os
import mimetypes


def assert_exists(path: str):
    assert os.path.isfile(path), "File not found: %s" % path


def is_image_file(fname):
    typ, _ = mimetypes.guess_type(fname)
    return typ and typ.startswith('image') and not typ.endswith('gif')


def is_video_file(fname):
    typ, _ = mimetypes.guess_type(fname)
    return typ and (typ.startswith('video') or typ.endswith('gif'))
