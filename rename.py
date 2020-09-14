import os


for i, file in enumerate(os.listdir("."), 1):
    if file.endswith("png"):
        size = file.split("_")[-1]
        os.rename(file, f"{i}-{size}")
