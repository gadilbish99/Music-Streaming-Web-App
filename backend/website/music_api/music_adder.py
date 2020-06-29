import os
from .models import *
from os.path import basename
from django.core.files import File

main_path = '/Users/ganbold/Music/My songs/Pop'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(main_path):
    for file in f:
        if '.mp3' in file:
            files.append(os.path.join(r, file))

for path in files:
    song = Song()
    song.file.save(basename(path), content=File(open(path, 'rb')))
