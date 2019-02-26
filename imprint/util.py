import mimetypes


def is_image_file(fname):
    typ, _ = mimetypes.guess_type(fname)
    return typ and typ.startswith('image') and not typ.endswith('gif')


def is_video_file(fname):
    typ, _ = mimetypes.guess_type(fname)
    return typ and (typ.startswith('video') or typ.endswith('gif'))
