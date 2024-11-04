import zipfile as zf

f = zf.ZipFile("./video/video.zip")
f.extractall("./video/")
