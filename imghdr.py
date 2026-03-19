# imghdr.py - minimal shim for Streamlit on Python 3.14
from PIL import Image
import io

def what(file, h=None):
    try:
        if h is None:
            data = file.read(32)
            file.seek(0)
        else:
            data = h
        img = Image.open(io.BytesIO(data))
        fmt = img.format.lower()
        return fmt
    except Exception:
        return None
