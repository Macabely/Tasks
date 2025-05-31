from PIL import Image
from PIL.ExifTags import TAGS
import sys

imagen = sys.argv[1]
image = Image.open(imagen)

exifdata = image.getexif()
if not exifdata:
    print("No EXIF data found in the image.")
else:
    for id in exifdata:
        tag = TAGS.get(id, id)
        data = exifdata.get(id)
        if isinstance(data, bytes):
            data = data.decode()
        print(f"{tag}: {data}")