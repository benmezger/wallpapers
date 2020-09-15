import re
import os
import mimetypes

FILENAME_REGEX = re.compile("^\d+\.(jpg|jpeg|png)$")

for i, file in enumerate(os.listdir("."), 1):
    if FILENAME_REGEX.search(file):
        continue

    mime, _ = mimetypes.guess_type(file)
    if mime == "image/png" or mime == "image/jpeg":
        size = file.split("_")[-1]
        os.rename(file, f"{i}-{size}")
