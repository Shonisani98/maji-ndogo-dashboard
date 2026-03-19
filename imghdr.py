# imghdr.py - shim for Python 3.14
from PIL import Image
import io

def what(file, h=None):
    try:
        if h is None:
            data = file.read(64)
            file.seek(0)
        else:
            data = h
        img = Image.open(io.BytesIO(data))
        return img.format.lower()
    except Exception:
        return None
